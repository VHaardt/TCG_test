"""Engine for the CICATRICI v0.2 candidate core (B0 of Q-013).

Specification: tcg/swarm/questioni/Q-013_rework_nucleo_v0.2/esperimento.md §1.
Differences from v0.1 (sim/engine.py): one kind of gem in four zones (Brace, Guardia,
pugno, scorta), a shared round track (Brace = min(round, 8)), characters are Ready or
Rotated ("has acted"), every attack targets the enemy Leader and the defender may
oppose one Unit, combat is a closed "pugno" of gems (+1 Forza each for the attacker,
+2 defence each for the defender, plus at most one covered Reaction), fresh Scars
(rotated) replace the Saldo counter and the colpo-finale snapshot. No modifier
survives a combat.

Decision points (`state.phase`):
  main          active player
  impeto        attacker commits gems face up (only pugno = "nessuno")
  risposta      defender's single face-up answer (only pugno = "nessuno")
  oppose        defender may oppose one ready Unit (opposizione = "prima")
  pugno_att     attacker closes the pugno (0..Brace gems)
  pugno_def     defender closes the pugno (0..Guardia gems, at most one Reaction)
  oppose_after  defender may oppose after the opening (opposizione = "dopo")
With pugno = "simultaneo" the defender's agent must not read `combat.a`; with
"sequenziale" it may (`combat.a_visible`)."""
import dataclasses
import json
import os
import random

from ..cards import load as load_db
from .config import B0
from .validate import validate

G1, G2 = 0, 1
RULES_VERSION = "v0.2"
DATA = os.path.join(os.path.dirname(__file__), "cards_v02.json")
KW_ALIAS = {"infuso": "impeto"}     # nome di v0.1/Q-013, accettato nei file vecchi
CARDS, LEADERS = {}, {}
META = {}                           # campi di carta non letti dal motore (slot, rarity): metriche M15
LOADED = [None]                     # file di carte caricato


def load_cards(path=DATA):
    """Fills CARDS, LEADERS, META in place from a v0.2 card file, after the strict check
    (validate.py): ValueError listing every unknown key, condition, event, op or selector."""
    path = os.path.abspath(path)
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    errors = validate(raw)
    if errors:
        raise ValueError(f"{path}: {len(errors)} errori\n" + "\n".join(errors))
    cards, leaders = load_db(path)
    for cid, c in cards.items():
        if c.keywords & set(KW_ALIAS):
            cards[cid] = dataclasses.replace(c, keywords=frozenset(KW_ALIAS.get(k, k) for k in c.keywords))
    LOADED[0] = path
    CARDS.clear(); CARDS.update(cards)
    LEADERS.clear(); LEADERS.update(leaders)
    META.clear()
    META.update({c["id"]: {k: c[k] for k in ("slot", "tags", "rarity") if k in c} for c in raw["cards"]})


from .validate import CONDITIONS as CONDS, SELECTOR as SEL_KEYS   # noqa: E402

load_cards()


class Unit:
    __slots__ = ("uid", "cid", "ready")

    def __init__(self, uid, cid, ready):
        self.uid, self.cid, self.ready = uid, cid, ready

    def clone(self):
        return Unit(self.uid, self.cid, self.ready)


class Player:
    __slots__ = ("leader", "awakened", "l_ready", "life", "scars", "hand", "deck", "discard",
                 "units", "relics", "brace", "guard")

    def __init__(self, leader):
        self.leader = leader
        self.awakened = False
        self.l_ready = True
        self.life = []
        self.scars = []             # [cid, fresh, origine della perdita di Vita]
        self.hand = []
        self.deck = []              # top = end of list
        self.discard = []
        self.units = []
        self.relics = []
        self.brace = 0
        self.guard = 0

    def clone(self):
        p = Player.__new__(Player)
        p.leader, p.awakened, p.l_ready = self.leader, self.awakened, self.l_ready
        p.life, p.hand, p.deck, p.discard, p.relics = (self.life[:], self.hand[:], self.deck[:],
                                                       self.discard[:], self.relics[:])
        p.scars = [sc[:] for sc in self.scars]
        p.units = [u.clone() for u in self.units]
        p.brace, p.guard = self.brace, self.guard
        return p

    def fresh(self):
        return sum(1 for sc in self.scars if sc[1])


# conditions that exist only inside a combat (R-009 T-9: not read by the "Forza attuale" filters)
COMBAT_CONDS = {"attacking", "opposing", "pugno_ge", "target_is_unit", "attacker_has", "react_from_scars",
                "hunted_ready", "survived"}

class Combat:
    __slots__ = ("att", "opposer", "hunted", "hunted_ready", "a", "d", "react", "a_visible", "att_mod", "def_mod",
                 "opened", "rim_legal")

    def __init__(self, att, hunted=None, hunted_ready=None):
        self.att = att              # "L" or uid of the attacking unit
        self.opposer = None         # uid of the defender's opposing unit, or None
        self.hunted = hunted        # uid of the Unit chosen with Caccia (C1), or None
        self.hunted_ready = hunted_ready    # was the hunted Unit Ready at the declaration (E3)
        self.a = None               # attacker's gems in the pugno
        self.d = None               # defender's gems in the pugno (Reaction cost included)
        self.react = None           # (cid, "hand"|"scar")
        self.a_visible = False
        self.rim_legal = False
        self.att_mod = 0            # from triggers resolved in this combat
        self.def_mod = 0
        self.opened = False

    def clone(self):
        c = Combat.__new__(Combat)
        for k in Combat.__slots__:
            setattr(c, k, getattr(self, k))
        return c

    def target(self, opposer="current"):
        """uid of the target Unit (opposer, else the hunted Unit), or None = the Leader."""
        o = self.opposer if opposer == "current" else opposer
        return o if o is not None else self.hunted


def new_stats():
    return {
        "attacks": [0, 0], "attacks_leader_hit": [0, 0], "stopped": [0, 0],
        "leader_hits": [[0, 0, 0, 0], [0, 0, 0, 0]],   # Q-017: colpi del Leader [Base, Base senza gemme, Risv., Risv. senza gemme]
        "opposed": [0, 0], "units_defeated_in_combat": [0, 0],
        "pugno_att": [[0, 0, 0, 0], [0, 0, 0, 0]],   # [combats with gems available, empty, full, gems]
        "pugno_def": [[0, 0, 0, 0], [0, 0, 0, 0]],
        "reactions": [0, 0], "mods": {}, "legal_actions": [0, 0], "decisions": [0, 0],
        "idle_turns": [0, 0], "idle3_turns": [0, 0], "turns": [0, 0],
        "lives_lost": [{}, {}], "life_at_round6": None, "awaken_round": [None, None],
        "rim_used": [0, 0], "cards_played": [{}, {}], "drawn": [{}, {}], "leader_free_rim": [{}, {}], "stanca_removed": [0, 0], "turns_both022": [0, 0], "atk_leader_both022": [0, 0], "guard_stored": [0, 0],
        # R-005, metriche M1-M14 (indice = giocatore che difende per M1-M3, che attacca per M4-M5)
        "react_avail": [0, 0], "react_decisive": [0, 0],                 # M1, M2
        "react_scar": [0, 0], "react_scar_life": [0, 0],                 # M3
        "decided_pre": [0, 0],                                           # M4
        "hunt": [0, 0], "hunt_ready": [0, 0], "hunt_rotated": [0, 0],    # M5
        "target_leader": [0, 0],
        "unit_turns": [0, 0], "unit_idle": [0, 0],                       # M6
        "opp_repeat": [0, 0],                                            # M7
        "double_gems": [0, 0],                                           # M8
        "opp_elig": [0, 0], "opp_elig_impeto": [0, 0], "opp_impeto": [0, 0],   # M9
        "activations": [{}, {}],                                         # M11
        "removals": [0, 0],                                              # M12
        "life_costs": [0, 0],                                            # M14
    }


class GameState:
    def __init__(self, rules=B0):
        self.r = rules
        self.p = [None, None]
        self.active = G1
        self.phase = "main"
        self.combat = None
        self.round = 0
        self.winner = None
        self.end_reason = None
        self.next_uid = 1
        self.rng = random.Random()
        self.stats = new_stats()
        self.log = None
        self.track = None           # stato delle metriche M6/M7 (solo la partita vera, non i cloni)

    # ------------------------------------------------------------------ basics
    def clone(self):
        s = GameState.__new__(GameState)
        s.r = self.r
        s.p = [self.p[0].clone(), self.p[1].clone()]
        s.active, s.phase, s.round = self.active, self.phase, self.round
        s.combat = self.combat.clone() if self.combat else None
        s.winner, s.end_reason, s.next_uid = self.winner, self.end_reason, self.next_uid
        s.rng = random.Random(self.rng.random())
        s.stats = None
        s.log = None
        s.track = None
        return s

    @property
    def over(self):
        return self.end_reason is not None

    def say(self, msg):
        if self.log is not None:
            self.log.append(msg)

    def stat_add(self, key, q, sub=None, n=1):
        if self.stats is None:
            return
        if sub is None:
            self.stats[key][q] += n
        else:
            d = self.stats[key][q]
            d[sub] = d.get(sub, 0) + n

    def decider(self):
        if self.over:
            return None
        if self.phase in ("main", "impeto", "pugno_att"):
            return self.active
        return 1 - self.active

    def unit(self, q, uid):
        for u in self.p[q].units:
            if u.uid == uid:
                return u
        return None

    def describe(self, q, ref):
        if ref == "L":
            return f"Leader {LEADERS[self.p[q].leader].name}"
        u = self.unit(q, ref)
        return f"{CARDS[u.cid].name}#{ref}" if u else f"#{ref}"

    def lose(self, q, reason):
        if self.over:
            return
        self.winner = 1 - q
        self.end_reason = reason
        self.say(f"*** P{q+1} perde ({reason})")

    # ------------------------------------------------------------------ derived values
    def saldo_cap(self):
        return self.r.saldo_late if self.round >= self.r.saldo_late_round else self.r.saldo

    def alle_corde(self, q):
        n = len(self.p[q].life)
        return n == 0 or (self.round >= self.r.corde_one_life_round and n <= 1)

    def leader_abilities(self, q):
        pl = self.p[q]
        return LEADERS[pl.leader].side(pl.awakened)

    def sources(self, q, units=None):
        """[(source id, ability)] of q's Leader and Relics, plus the Units' abilities (units="all")
        or only their auras (units="aura"). "stack": false enters once per card id (N2)."""
        pl = self.p[q]
        out = [(pl.leader, ab) for ab in self.leader_abilities(q)]
        out += [(r, ab) for r in pl.relics for ab in CARDS[r].abilities]
        if units:
            out += [(u.cid, ab) for u in pl.units for ab in CARDS[u.cid].abilities
                    if units == "all" or "applies_to" in ab]
        if any(ab.get("stack") is False for _, ab in out):
            seen, res = set(), []
            for sid, ab in out:
                if ab.get("stack") is False:
                    if (sid, id(ab)) in seen:
                        continue
                    seen.add((sid, id(ab)))
                res.append((sid, ab))
            out = res
        return out

    def static_sources(self, q):
        return [ab for _, ab in self.sources(q)]

    def static_sum(self, q, name):
        total = 0
        for sid, ab in self.sources(q, "all"):
            if ab.get("static") == name and self.cond_ok(q, ab.get("if"), {"self": sid}):
                total += self.num(ab["value"], q)
        return total

    def modifier(self, q, name, default):
        for ab in self.leader_abilities(q):
            if ab.get("modifier") == name:
                return ab.get("value", default)
        return default

    def guard_max(self, q):
        g = self.r.guard_max_awakened if self.p[q].awakened else self.r.guard_max
        g += self.static_sum(q, "guard_max")
        if self.alle_corde(q):
            g += self.r.guard_alle_corde_bonus
        for sid, ab in self.sources(q, "all"):             # tetto ("cap"), applicato per ultimo
            if ab.get("static") == "guard_max" and "cap" in ab and self.cond_ok(q, ab.get("if"), {"self": sid}):
                g = min(g, ab["cap"])
        return g

    def furia(self, q):
        return len(self.p[q].scars) + self.static_sum(q, "furia_bonus")

    def parata_per_gemma(self, q):
        for ab in self.leader_abilities(q):
            if ab.get("static") == "parata_per_gemma":
                return ab["value"]
        return self.r.parata_per_gemma

    def num(self, v, q=None):
        if isinstance(v, dict):                             # valori dinamici
            if "scars" in v:                                # {"scars": "own"|"opp"}
                return len(self.p[q if v["scars"] == "own" else 1 - q].scars)
            if "n" in v:                                    # {"n": 2, "plus": 1, "if": [...]}
                return self.num(v["n"], q) + (self.num(v.get("plus", 0), q) if self.cond_ok(q, v.get("if"), {}) else 0)
            raise ValueError(f"valore dinamico sconosciuto: {v}")
        if isinstance(v, str):
            neg = v.startswith("-")
            name = v.lstrip("-@")
            v = getattr(self.r, name)
            return -v if neg else v
        return v

    def cond_ok(self, q, conds, ctx):
        for c in conds or ():
            (k, v), = c.items()
            if k == "furia" and self.furia(q) < v:
                return False
            if k == "scars_ge" and len(self.p[q].scars) < v:
                return False
            if k == "awakened" and self.p[q].awakened != v:
                return False
            if k == "attacking" and ctx.get("attacker_uid") != ctx.get("self"):
                return False
            if k == "pugno_ge" and ctx.get("pugno", -1) < v:
                return False
            if k == "deck_nonempty" and bool(self.p[q].deck) != v:
                return False
            if k == "target_is_unit" and (ctx.get("target_uid") is not None) != v:
                return False
            if k == "opposing":
                # Unità: è lei a opporsi; Reliquia o Leader del difensore (statiche combat): si oppone una tua Unità
                me, opp = ctx.get("self"), ctx.get("opposer_uid")
                ok = opp is not None and (me == opp or (me is not None and not isinstance(me, int) and me != "L"
                                                      and ctx.get("role") == "defense"))
                if ok != v:
                    return False
            if k == "react_from_scars" and (ctx.get("react_src") == "scar") != v:
                return False
            if k == "hunted_ready" and ctx.get("hunted_ready") != v:
                return False
            if k == "survived" and ctx.get("survived", True) != v:   # chi ha sconfitto è ancora in gioco
                return False
            if k == "attacker_has":
                cid = ctx.get("attacker_cid")
                if cid is None or not CARDS[cid].has(KW_ALIAS.get(v, v)):
                    return False
            if k not in CONDS:
                raise ValueError(f"condizione sconosciuta in v0.2: {k}")
        return True

    def matches(self, q_unit, u, sel, ctx=None, chooser=None):
        """chooser: who reads the selector (dynamic values, "if"); default the Unit's owner."""
        ch = q_unit if chooser is None else chooser
        if "any" in sel:                                    # unione di selettori, dopo le chiavi comuni
            rest = {k: v for k, v in sel.items() if k != "any"}
            return self.matches(q_unit, u, rest, ctx, chooser) and \
                any(self.matches(q_unit, u, s2, ctx, chooser) for s2 in sel["any"])
        if "if" in sel and not self.cond_ok(ch, sel["if"], ctx or {}):
            return False
        c = CARDS[u.cid]
        for k in sel:
            if k not in SEL_KEYS:
                raise ValueError(f"chiave di selettore sconosciuta in v0.2: {k}")
        if "cost_le" in sel and c.cost > self.num(sel["cost_le"], ch):
            return False
        if "ready" in sel and u.ready != sel["ready"]:
            return False
        if "power_le" in sel and self.unit_power(q_unit, u, outside=True) > self.num(sel["power_le"], ch):
            return False
        if "keyword" in sel and not c.has(KW_ALIAS.get(sel["keyword"], sel["keyword"])):
            return False
        if sel.get("attacker") and (ctx or {}).get("attacker_uid") != u.uid:
            return False
        return True

    def unit_power(self, q, u, ctx=None, trace=None, outside=False):
        """Printed Forza + static bonuses. ctx (during a combat): see combat_ctx; "pugno" = gems
        committed by the Unit's side (Parata only for the defender). trace: list of (q, source)
        of conditional bonuses that applied (metrica M11). outside: "Forza attuale" of the
        filters (Q-015 S-4, R-009 T-9) = printed + auras without combat conditions; the Unit's
        own conditional bonuses (Furia, "in questo scontro") are combat bonuses and don't count."""
        ctx = dict(ctx or {}, self=u.uid)
        c = CARDS[u.cid]
        p = c.power
        for ab in c.abilities:
            if outside and ab.get("if"):
                continue
            if ab.get("static") == "power" and "applies_to" not in ab and self.cond_ok(q, ab.get("if"), ctx):
                p += self.num(ab["value"], q)
                if trace is not None and ab.get("if"):
                    trace.append((q, u.cid))
        for sid, ab in self.sources(q, "aura"):
            if ab.get("static") == "power" and "applies_to" in ab:
                sel = ab["applies_to"]
                if outside and (sel.get("attacker") or any(set(c2) & COMBAT_CONDS for c2 in ab.get("if") or [])):
                    continue
                if sel.get("side", "own") == "own" and self.matches(q, u, sel, ctx) and self.cond_ok(q, ab.get("if"), ctx):
                    p += self.num(ab["value"], q)
                    if trace is not None and (ab.get("if") or sel.get("attacker")):
                        trace.append((q, sid))
        return p

    def leader_power(self, q, ctx=None):
        p = self.r.leader_power_awakened if self.p[q].awakened else self.r.leader_power
        if ctx and ctx.get("attacker_uid") == "L":
            for ab in self.static_sources(q):
                sel = ab.get("applies_to")
                if ab.get("static") == "power" and sel and sel.get("attacker") and set(sel) <= {"side", "attacker"} \
                        and sel.get("kind") != "unit" \
                        and self.cond_ok(q, ab.get("if"), dict(ctx, self="L")):
                    p += self.num(ab["value"], q)
        return p

    # ------------------------------------------------------------------ Vita
    def lose_life(self, q, source, ignore_saldo=False):
        pl = self.p[q]
        if not pl.life:
            return False
        if not ignore_saldo and pl.fresh() >= self.saldo_cap():
            return False
        pl.scars.append([pl.life.pop(), not ignore_saldo, source])
        self.stat_add("lives_lost", q, source)
        self.say(f"    P{q+1} perde 1 Vita ({source}): restano {len(pl.life)}")
        return True

    def can_pay_life(self, q, n, floor=0):
        pl = self.p[q]
        return len(pl.life) - n >= max(floor, 0) and pl.fresh() + n <= self.saldo_cap()

    def draw(self, q, n=1):
        pl = self.p[q]
        for _ in range(n):
            if pl.deck:
                pl.hand.append(pl.deck.pop())
                self.stat_add("drawn", q, pl.hand[-1])          # E-000: carte viste
            elif not pl.life:
                self.lose(q, "mazzo_vuoto")
                return
            else:
                self.lose_life(q, "mazzo_vuoto")

    def state_checks(self):
        for q in (G1, G2):
            pl = self.p[q]
            if not pl.awakened and len(pl.life) <= self.r.awaken_at_life:
                pl.awakened = True
                if self.stats is not None and self.stats["awaken_round"][q] is None:
                    self.stats["awaken_round"][q] = self.round
                self.say(f"    P{q+1}: il Leader si Risveglia")

    # ------------------------------------------------------------------ setup / turn
    def setup(self, leader1, deck1, leader2, deck2, seed=None, mulligan=None):
        self.rng = random.Random(seed)
        for q, (lid, deck) in enumerate(((leader1, deck1), (leader2, deck2))):
            pl = Player(lid)
            pl.deck = list(deck)
            self.rng.shuffle(pl.deck)
            self.p[q] = pl
            self.draw(q, self.r.hand)
            (mulligan or default_mulligan)(self, q)
            if q == G2:
                self.draw(q, self.r.g2_hand_extra)
            for _ in range(self.r.life):
                pl.life.append(pl.deck.pop())
        self.active = G1
        if self.stats is not None:
            self.track = {"seen": set(), "attacked": set(), "opposed": set(), "cand": [set(), set()], "stancate": set()}
        self.begin_turn()
        return self

    def begin_turn(self):
        """Ripristino (7) and Pesca (8)."""
        a = self.active
        pl = self.p[a]
        if a == G1:
            self.round += 1
            if self.round > self.r.max_rounds:
                self.end_reason = "non_conclusa"
                return
            if self.round == 7 and self.stats is not None:
                self.stats["life_at_round6"] = (len(self.p[0].life), len(self.p[1].life))
        self.say(f"--- Round {self.round}, P{a+1} | Vite {len(self.p[0].life)}-{len(self.p[1].life)}")
        if self.round >= self.r.crepuscolo_round:          # 7b
            if self.alle_corde(a):
                self.lose(a, "crepuscolo")
                return
            for _ in range(self.r.crepuscolo_loss):
                self.lose_life(a, "crepuscolo", ignore_saldo=True)
        pl.guard = 0                                        # 7c
        if self.r.raddrizzo == "ripristino":                # 7d
            self._straighten(a)
        pl.brace = min(self.round, self.r.brace_max)        # 7e
        if a == G2 and self.round == 1:
            pl.brace += self.r.scintilla_g2_gems
        if a == G2 and self.round == self.r.scintilla_extra_round:
            pl.brace += self.r.scintilla_extra_gems
        self.state_checks()
        if not (a == G1 and self.round == 1):               # 8
            self.draw(a)
        self.state_checks()
        self.phase = "main"
        if self.stats is not None:
            self.stats["turns"][a] += 1

    def _straighten(self, q):
        pl = self.p[q]
        pl.l_ready = True
        for u in pl.units:
            u.ready = True

    def end_turn(self):
        """Fine (10)."""
        a = self.active
        pl = self.p[a]
        if self.stats is not None and self.round > self.r.no_attack_round:
            idle = sum(1 for u in pl.units if u.ready)
            if idle:
                self.stats["idle_turns"][a] += 1
            if idle >= 3:
                self.stats["idle3_turns"][a] += 1
        if self.track is not None:                          # M6: ferma = Pronta, non attacca e non si oppone
            tr = self.track
            self.stats["unit_idle"][1 - a] += len(tr["cand"][1 - a] - tr["opposed"])
            tr["cand"][1 - a] = set()
            if self.round > self.r.no_attack_round:
                self.stats["unit_turns"][a] += len(tr["seen"])
                tr["cand"][a] = {u.uid for u in pl.units if u.ready and u.uid in tr["seen"]} - tr["attacked"]
            tr["seen"], tr["attacked"], tr["opposed"], tr["stancate"] = set(), set(), set(), set()
            if self.both_022(a):
                self.stat_add("turns_both022", a)              # R-009 #6
        stored = min(pl.brace, self.guard_max(a))           # 10b
        pl.guard = stored
        if a == G2 and self.round == 1:
            pl.guard += self.r.scintilla_guardia_g2          # oltre il massimo, per gli attacchi di G1 nel round 2
        pl.brace = 0
        self.stat_add("guard_stored", a, n=stored)
        if self.r.raddrizzo == "fine":                      # 10c
            self._straighten(a)
        for q in (G1, G2):                                  # 10d
            for sc in self.p[q].scars:
                sc[1] = False
        if len(pl.hand) > self.r.hand_limit:                # 10e
            pl.hand.sort(key=lambda c: CARDS[c].cost)
            while len(pl.hand) > self.r.hand_limit:
                pl.discard.append(pl.hand.pop())
        self.state_checks()
        self.active = 1 - a
        self.combat = None
        self.begin_turn()

    # ------------------------------------------------------------------ legal actions
    def legal_actions(self):
        if self.over:
            return []
        ph = self.phase
        a, d = self.active, 1 - self.active
        if ph == "main":
            return self._main_actions()
        if ph in ("impeto", "pugno_att"):
            return [("gems", k) for k in range(self.p[a].brace + 1)]
        if ph in ("oppose", "oppose_after"):
            return [("no_oppose",)] + [("oppose", uid) for uid in self.opposer_options()]
        if ph == "pugno_def":
            return self._parry_options(d)
        if ph == "risposta":
            return ([("oppose", uid) for uid in self.opposer_options()] + self._parry_options(d))
        return []

    def opposer_options(self):
        """C2: ready Units of the defender, except the Unit hunted with Caccia."""
        hunted = self.combat.hunted if self.combat else None
        return [u.uid for u in self.p[1 - self.active].units if u.ready and u.uid != hunted]

    def reaction_options(self, d):
        pl = self.p[d]
        out, seen = [], set()
        for src, pile in (("hand", pl.hand), ("scar", [sc[0] for sc in pl.scars if not sc[1]])):
            for cid in pile:
                if CARDS[cid].type == "reaction" and (cid, src) not in seen:
                    seen.add((cid, src))
                    out.append((cid, src))
        return out

    def _parry_options(self, d):
        g = self.p[d].guard
        acts = [("parry", k, None) for k in range(g + 1)]
        for r in self.reaction_options(d):
            c = max(CARDS[r[0]].cost, 1)
            for k in range(c, g + 1):
                acts.append(("parry", k, r))
        return acts

    def can_attack(self, q):
        return self.round > self.r.no_attack_round

    def _main_actions(self):
        a = self.active
        pl = self.p[a]
        acts = [("end",)]
        seen = set()
        for cid in pl.hand:
            if cid in seen:
                continue
            seen.add(cid)
            c = CARDS[cid]
            if c.cost > pl.brace or c.type == "reaction":
                continue
            if c.costs and not self.pay_costs(a, c.costs, check_only=True):
                continue
            if c.type == "unit" and len(pl.units) < self.r.max_units:
                acts.append(("play", cid, None))
            elif c.type == "relic" and len(pl.relics) < self.r.max_relics:
                acts.append(("play", cid, None))
            elif c.type == "tactic":
                spec = c.play or {}
                if self.pay_costs(a, spec.get("costs"), check_only=True):
                    for t in self._targets(a, spec.get("target")):
                        acts.append(("play", cid, t))
        rim_cost = self.modifier(a, "rim_cost", 1)
        if pl.l_ready and pl.brace >= rim_cost:
            for cid in sorted({sc[0] for sc in pl.scars if not sc[1]}):
                acts.append(("rim", cid))
        if pl.l_ready:
            for i, ab in enumerate(self.leader_abilities(a)):
                if ab.get("activated") and pl.brace >= ab.get("cost", 0) and self.pay_costs(a, ab.get("costs"), True):
                    for t in self._targets(a, ab.get("target")):
                        acts.append(("ability", "L", i, t))
        for u in pl.units:
            if u.ready:
                for i, ab in enumerate(CARDS[u.cid].abilities):
                    if ab.get("activated") and pl.brace >= ab.get("cost", 0) and self.pay_costs(a, ab.get("costs"), True):
                        for t in self._targets(a, ab.get("target")):
                            acts.append(("ability", u.uid, i, t))
        if self.can_attack(a):
            if pl.l_ready:
                acts.append(("attack", "L"))
            foes = [v.uid for v in self.p[1 - a].units]
            for u in pl.units:
                if u.ready:
                    acts.append(("attack", u.uid))
                    if CARDS[u.cid].has("caccia"):          # Caccia: bersaglio un'Unità, Pronta o Ruotata
                        acts += [("attack", u.uid, t) for t in foes]
        return acts

    def _targets(self, a, sel):
        if sel is None:
            return [None]
        side = a if sel.get("side", "own") == "own" else 1 - a
        return [u.uid for u in self.p[side].units if self.matches(side, u, sel, chooser=a)]

    def pay_costs(self, q, costs, check_only=False):
        for c in costs or ():
            if "lose_life" in c and not self.can_pay_life(q, c["lose_life"], c.get("floor", 0)):
                return False
        if not check_only:
            for c in costs or ():
                for _ in range(c.get("lose_life", 0)):
                    self.lose_life(q, "costo")
                    self.stat_add("life_costs", q)
        return True

    # ------------------------------------------------------------------ step
    def step(self, act):
        if self.stats is not None:
            q = self.decider()
            self.stats["decisions"][q] += 1
            self.stats["legal_actions"][q] += len(self.legal_actions())
            if self.phase == "main" and self.track is not None and self.can_attack(q):
                self.track["seen"].update(u.uid for u in self.p[q].units if u.ready)
        ph = self.phase
        if ph == "main":
            self._main_step(act)
        elif ph == "impeto":
            self.combat.a = act[1]
            self.combat.a_visible = True
            self.phase = "risposta"
        elif ph == "risposta":
            if act[0] == "oppose":
                self._oppose(act[1])
                self.combat.d = 0
            else:
                self.combat.d, self.combat.react = act[1], act[2]
            self._open_and_resolve()
        elif ph == "oppose":
            if act[0] == "oppose":
                self._oppose(act[1])
            self.phase = "pugno_att"
        elif ph == "pugno_att":
            self.combat.a = act[1]
            self.combat.a_visible = self.r.pugno == "sequenziale"
            self.phase = "pugno_def"
        elif ph == "pugno_def":
            self.combat.d, self.combat.react = act[1], act[2]
            self.combat.opened = True
            if self.r.opposizione == "dopo" and any(u.ready for u in self.p[1 - self.active].units):
                self.phase = "oppose_after"
            else:
                self._open_and_resolve()
        elif ph == "oppose_after":
            if act[0] == "oppose":
                self._oppose(act[1])
            self._open_and_resolve()
        if not self.over and self.phase == "main":
            self.state_checks()

    def _main_step(self, act):
        a = self.active
        pl = self.p[a]
        k = act[0]
        if k == "end":
            self.end_turn()
        elif k == "play":
            self._play(a, act[1], act[2])
        elif k == "rim":
            pl.l_ready = False
            pl.brace -= self.modifier(a, "rim_cost", 1)
            for sc in pl.scars:
                if sc[0] == act[1] and not sc[1]:
                    pl.scars.remove(sc)
                    break
            pl.hand.append(act[1])
            self.stat_add("rim_used", a)
            self.say(f"  P{a+1} Rimargina {CARDS[act[1]].name}")
        elif k == "ability":
            src, i, t = act[1], act[2], act[3]
            if src == "L":
                ab = self.leader_abilities(a)[i]
                pl.l_ready = False
            else:
                u = self.unit(a, src)
                ab = CARDS[u.cid].abilities[i]
                u.ready = False
            pl.brace -= ab.get("cost", 0)
            self.pay_costs(a, ab.get("costs"))              # Cicatrici contate prima (bersaglio già scelto)
            self.stat_add("activations", a, LEADERS[pl.leader].id if src == "L" else u.cid)
            self.run_ops(a, ab["do"], dict(self._chosen(a, ab.get("target"), t), self=src))
        elif k == "attack":
            self._declare(a, act[1], act[2] if len(act) > 2 else None)
        else:
            raise ValueError(f"azione sconosciuta: {act}")

    def _chosen(self, a, sel, t):
        owner = a if (sel or {}).get("side", "own") == "own" else 1 - a
        return {"chosen": t, "chosen_owner": owner}

    def _play(self, a, cid, target):
        pl = self.p[a]
        c = CARDS[cid]
        pl.hand.remove(cid)
        pl.brace -= c.cost
        self.stat_add("cards_played", a, cid)
        self.say(f"  P{a+1} gioca {c.name}")
        self.pay_costs(a, c.costs)
        if c.type == "unit":
            u = Unit(self.next_uid, cid, ready=c.has("assalto"))
            self.next_uid += 1
            pl.units.append(u)
            self.fire(a, CARDS[cid].abilities, "on_enter", {"self": u.uid})
        elif c.type == "relic":
            pl.relics.append(cid)
        else:
            spec = c.play or {}
            self.pay_costs(a, spec.get("costs"))
            self.run_ops(a, spec.get("do", []), self._chosen(a, spec.get("target"), target))
            pl.discard.append(cid)

    # ------------------------------------------------------------------ effects (small DSL)
    def _stancata_rimossa(self, q, owner, u):
        """R-009 #5: q removes an opposing Unit it made Stanca (from Ready) in this same turn."""
        if self.track is not None and (owner, u.uid) in self.track["stancate"]:
            self.stat_add("stanca_removed", q)

    def both_022(self, q):
        ids = {u.cid for u in self.p[q].units}
        return "ROS-022" in ids and "VER-022" in ids

    def tempra(self, q):
        """Tempra of q's Leader (tempra_awakened when set and q is Awakened)."""
        return self.r.tempra_awakened if self.p[q].awakened and self.r.tempra_awakened else self.r.tempra

    def fire(self, q, abilities, event, ctx, src=None, once=None):
        """once: set shared by one fire_global call; a trigger with "stack": false fires once
        per card id there ("Più copie non si sommano", R-007)."""
        for i, ab in enumerate(abilities):
            if ab.get("trigger") == event and self.cond_ok(q, ab.get("if"), ctx):
                if ab.get("stack") is False and once is not None:
                    if (src, i) in once:
                        continue
                    once.add((src, i))
                ops = [o for o in ab["do"] if o["op"] not in ("att_mod", "def_mod")]
                c = ctx
                if "target" in ab:                          # N1: bersaglio scelto dal motore
                    cands = self._targets(q, ab["target"])
                    if not cands:
                        continue
                    c = dict(ctx, **self._chosen(q, ab["target"], self.trigger_target(q, ab["target"], cands)))
                if ops and src is not None:
                    self.stat_add("activations", q, src)
                self.run_ops(q, ops, c)

    def trigger_target(self, q, sel, cands):
        """Deterministic choice for a trigger's target (not a decision point): the candidate with
        the highest (Forza, cost), then the lowest uid."""
        side = q if sel.get("side", "own") == "own" else 1 - q
        return max(cands, key=lambda uid: (self.unit_power(side, self.unit(side, uid)),
                                           CARDS[self.unit(side, uid).cid].cost, -uid))

    def fire_global(self, q, event, ctx, gone=()):
        """gone: Units of q defeated in this combat, whose look-back triggers still fire (§7.5)."""
        once = set()
        for u in list(self.p[q].units) + list(gone):
            self.fire(q, CARDS[u.cid].abilities, event, dict(ctx, self=u.uid), src=u.cid, once=once)
        self.fire(q, self.leader_abilities(q), event, dict(ctx, self="L"), src=self.p[q].leader)
        for rid in list(self.p[q].relics):                  # N3: anche le Reliquie
            self.fire(q, CARDS[rid].abilities, event, dict(ctx, self=rid), src=rid, once=once)

    def op_target(self, q, op, ctx):
        """(owner, Unit) named by op["target"]: "chosen" (default), "self", "opposer", "attacker";
        "sel" (optional) is a selector the Unit must match, read by q."""
        t = op.get("target", "chosen")
        if t == "self":
            owner, uid = q, ctx.get("self")
        elif t == "opposer":
            owner, uid = q, ctx.get("opposer_uid")
        elif t == "attacker":
            owner, uid = 1 - q, ctx.get("attacker_uid")
        elif t == "chosen":
            owner, uid = ctx.get("chosen_owner"), ctx.get("chosen")
        else:
            raise ValueError(f"bersaglio di op sconosciuto in v0.2: {t}")
        u = self.unit(owner, uid) if owner is not None and uid not in (None, "L") else None
        if u is not None and "sel" in op and not self.matches(owner, u, op["sel"], chooser=q):
            u = None
        return owner, u

    def run_ops(self, q, ops, ctx):
        for op in ops:
            if self.over:
                return
            if not self.cond_ok(q, op.get("if"), ctx):      # condizione sulla singola op
                continue
            k = op["op"]
            n = self.num(op.get("n", 0), q)
            if k == "draw":
                self.draw(q, n)
            elif k in ("stanca", "defeat", "raddrizza"):
                if k == "stanca" and q != self.active:      # Q-016: Stanca solo nel tuo turno
                    continue
                owner, u = self.op_target(q, op, ctx)
                if u is None:
                    continue
                if k == "stanca":
                    if self.track is not None and u.ready:
                        self.track["stancate"].add((owner, u.uid))  # R-009 #5
                    u.ready = False
                elif k == "raddrizza":
                    u.ready = True
                else:
                    self.p[owner].units.remove(u)
                    self.p[owner].discard.append(u.cid)
                    if owner != q:
                        self.stat_add("removals", q)
                        self._stancata_rimossa(q, owner, u)
            elif k == "att_mod" and self.combat:
                self.combat.att_mod += n
            elif k == "def_mod" and self.combat:
                self.combat.def_mod += n
            else:
                raise ValueError(f"operazione sconosciuta in v0.2: {k}")

    def trigger_mods(self, q, abilities, event, ctx):
        """att_mod / def_mod written in triggers are read as fixed combat modifiers."""
        am = dm = 0
        for ab in abilities:
            if ab.get("trigger") == event and self.cond_ok(q, ab.get("if"), ctx):
                for o in ab["do"]:
                    if o["op"] in ("att_mod", "def_mod") and self.cond_ok(q, o.get("if"), ctx):
                        if o["op"] == "att_mod":
                            am += self.num(o.get("n", 0), q)
                        else:
                            dm += self.num(o.get("n", 0), q)
        return am, dm

    # ------------------------------------------------------------------ combat
    def _declare(self, a, att, hunted=None):
        pl = self.p[a]
        d = 1 - a
        self.combat = Combat(att, hunted, self.unit(d, hunted).ready if hunted is not None else None)
        if att == "L":
            # Q-017 (Ne, An): attaccando, il Leader rinuncia a un Rimarginare legale?
            self.combat.rim_legal = pl.brace >= self.modifier(a, "rim_cost", 1) and any(not sc[1] for sc in pl.scars)
            pl.l_ready = False
        else:
            u = self.unit(a, att)
            u.ready = False
            self.fire(a, CARDS[u.cid].abilities, "on_attack", dict(self.combat_ctx(self.combat), self=att), src=u.cid)
        self.stat_add("attacks", a)
        if self.track is not None:
            self.track["attacked"].add(att)
            if hunted is None and self.both_022(a):
                self.stat_add("atk_leader_both022", a)         # R-009 #6 (bersaglio dichiarato: il Leader)
        if hunted is not None:
            self.stat_add("hunt", a)
            self.stat_add("hunt_ready" if self.unit(d, hunted).ready else "hunt_rotated", a)
            self.stat_add("activations", a, self.unit(a, att).cid)
        self.say(f"  P{a+1} attacca con {self.describe(a, att)}"
                 + (f" (Caccia: {self.describe(d, hunted)})" if hunted is not None else ""))
        if self.over:
            return
        if self.r.pugno == "nessuno":
            self.phase = "impeto"
        elif self.r.opposizione == "prima" and self.opposer_options():
            self.phase = "oppose"
        else:
            self.phase = "pugno_att"
        if self.stats is not None and (self.phase in ("oppose", "impeto") or self.r.opposizione == "dopo"):
            opts = self.opposer_options()                   # M9: Unità che potrebbero opporsi
            self.stats["opp_elig"][d] += len(opts)
            self.stats["opp_elig_impeto"][d] += sum(CARDS[self.unit(d, x).cid].has("impeto") for x in opts)

    def _oppose(self, uid):
        a, d = self.active, 1 - self.active
        u = self.unit(d, uid)
        self.combat.opposer = uid
        if not (CARDS[u.cid].has("scudo") and self.r.scudo == "oppone_senza_ruotarsi"):
            u.ready = False
        self.stat_add("opposed", a)
        if self.stats is not None:
            self.stats["opp_impeto"][d] += CARDS[u.cid].has("impeto")
            if self.track is not None:
                self.stats["opp_repeat"][d] += uid in self.track["opposed"]     # M7
                self.track["opposed"].add(uid)
        self.say(f"    P{d+1} oppone {CARDS[u.cid].name}")
        self.fire(d, CARDS[u.cid].abilities, "on_oppose", dict(self.combat_ctx(self.combat), self=uid), src=u.cid)

    def combat_ctx(self, cb, opposer="current", pugno=None, react_src=None):
        """Condition context of a combat: attacker, opposer, target (Unit uid or None = Leader),
        hunted_ready (only if the hunted Unit is still the target), source of the Reaction."""
        att = None if cb.att == "L" else self.unit(self.active, cb.att)
        opp = cb.opposer if opposer == "current" else opposer
        ctx = {"attacker_uid": cb.att, "attacker_cid": att.cid if att else None,
               "opposer_uid": opp, "target_uid": opp if opp is not None else cb.hunted,
               "hunted_ready": cb.hunted_ready if opp is None and cb.hunted is not None else None,
               "react_src": react_src}
        if pugno is not None:
            ctx["pugno"] = pugno
        return ctx

    def compute(self, a_gems, d_gems, react, opposer, count_mods=False, cb=None, trace=None):
        """(Fa, Db, modifiers) for given pugno contents. Pure: used by the engine and by the AI.
        opposer: the opposing Unit (None = nobody opposes: target = hunted Unit or Leader).
        cb: a Combat other than the current one (AI previews). trace: dict filled for the metrics."""
        a, d = self.active, 1 - self.active
        cb = cb or self.combat
        tgt = cb.target(opposer)
        src = trace["src"] if trace is not None else None
        mods = 0
        rs = react[1] if react is not None and d_gems >= max(CARDS[react[0]].cost, 1) else None
        ctx_a = self.combat_ctx(cb, opposer, pugno=a_gems, react_src=rs)
        if cb.att == "L":
            base_a = self.r.leader_power_awakened if self.p[a].awakened else self.r.leader_power
            fa = self.leader_power(a, ctx_a)
            mods += fa != base_a
            if src is not None and fa != base_a:
                src.append((a, self.p[a].leader))
        else:
            u = self.unit(a, cb.att)
            fa = self.unit_power(a, u, ctx_a, src)
            mods += fa != CARDS[u.cid].power
            if tgt is not None and CARDS[u.cid].has("bracconiere"):     # attacca un'Unità
                fa += CARDS[u.cid].kw("bracconiere")
                mods += 1
                if src is not None:
                    src.append((a, u.cid))
            am, _ = self.trigger_mods(a, CARDS[u.cid].abilities, "on_attack", dict(ctx_a, self=cb.att))
            fa += am
            mods += am != 0
        fa += a_gems * self.r.forza_per_gemma
        mods += a_gems > 0
        parry = d_gems
        r_att = r_def = 0
        if react is not None:
            cid, rsrc = react
            c = CARDS[cid]
            cost = max(c.cost, 1)
            if d_gems >= cost:
                parry -= cost
                ops = c.react.get("do_from_scars", c.react["do"]) if rsrc == "scar" else c.react["do"]
                rctx = self.combat_ctx(cb, opposer, pugno=parry, react_src=rs)
                for o in ops:
                    if o["op"] in ("att_mod", "def_mod") and self.cond_ok(d, o.get("if"), rctx):
                        if o["op"] == "att_mod":
                            r_att += self.num(o["n"], d)
                        else:
                            r_def += self.num(o["n"], d)
                mods += 1
                if src is not None:
                    src.append((d, cid))
        ctx_d = dict(self.combat_ctx(cb, opposer, pugno=parry, react_src=rs), role="defense")   # Q-015 S-2: solo Parata
        if tgt is None:
            db = self.tempra(d)
        else:
            tu = self.unit(d, tgt)
            if tu is None:                                  # il bersaglio ha lasciato il gioco
                return fa, 0, mods
            ctx_t = self.combat_ctx(cb, opposer, pugno=parry, react_src=rs)    # Impeto in difesa: solo la Parata
            db = self.unit_power(d, tu, ctx_t, src)
            mods += db != CARDS[tu.cid].power
            if trace is not None:
                trace["pugno_target"] = parry
            if opposer is not None:
                _, dm = self.trigger_mods(d, CARDS[tu.cid].abilities, "on_oppose", dict(ctx_t, self=opposer))
                db += dm
                mods += dm != 0
                if src is not None and dm:
                    src.append((d, tu.cid))
        db += parry * self.parata_per_gemma(d)
        mods += parry > 0
        for sid, ab in self.sources(d):
            if ab.get("static") == "combat" and ab.get("role") == "defense" \
                    and self.cond_ok(d, ab.get("if"), dict(ctx_d, self=sid)):
                fa += ab.get("att_mod", 0)
                db += ab.get("def_mod", 0)
                mods += 1
                if src is not None:
                    src.append((d, sid))
        fa += r_att + cb.att_mod
        db += r_def + cb.def_mod
        return fa, db, mods

    def outcome(self, fa, db, opposer, cb=None, a_gems=None):
        """(leader_hit, attacker_unit_defeated, target_unit_defeated). a_gems: attacker's gems
        (default cb.a), read only by leader_min_gems (Q-017 B3)."""
        a, d = self.active, 1 - self.active
        cb = cb or self.combat
        tgt = cb.target(opposer)
        if tgt is None:
            if cb.att == "L" and self.r.leader_min_gems:
                g = cb.a if a_gems is None else a_gems
                if (g or 0) < self.r.leader_min_gems:
                    return False, False, False
            return fa >= db, False, False
        tu = self.unit(d, tgt)
        if tu is None:
            return False, False, False
        pareggi = self.r.scudo == "vince_pareggi" and CARDS[tu.cid].has("scudo")    # "quando è il bersaglio"
        if cb.att == "L":
            return False, False, (fa > db) if pareggi else (db <= fa)
        if fa > db:
            return False, False, True
        if fa < db:
            return False, True, False
        return False, True, not pareggi

    def preview(self, att, hunted, a_gems, d_gems, react=None, opposer=None):
        """Pure: (Fa, Db, outcome) of an attack not yet declared (AI heuristics)."""
        cb = Combat(att, hunted, self.unit(1 - self.active, hunted).ready if hunted is not None else None)
        fa, db, _ = self.compute(a_gems, d_gems, react, opposer, cb=cb)
        return fa, db, self.outcome(fa, db, opposer, cb=cb, a_gems=a_gems)

    def decided_before_commit(self):
        """M4: no legal commitment of either player changes the outcome. Fa grows with the
        attacker's gems, so for each answer of the defender 0 and all gems bound the outcomes."""
        cb = self.combat
        B = self.p[self.active].brace
        first = None
        for _, d_gems, react in self._parry_options(1 - self.active):
            for a_gems in (0, B):
                fa, db, _ = self.compute(a_gems, d_gems, react, cb.opposer)
                o = self.outcome(fa, db, cb.opposer, a_gems=a_gems)
                if first is None:
                    first = o
                elif o != first:
                    return False
        return True

    def _open_and_resolve(self):
        a, d = self.active, 1 - self.active
        cb = self.combat
        pa, pd = self.p[a], self.p[d]
        cb.opened = True
        trace = {"src": [], "pugno_target": None} if self.stats is not None else None
        fa, db, mods = self.compute(cb.a, cb.d, cb.react, cb.opposer, trace=trace)
        hit, att_dead, tgt_dead = self.outcome(fa, db, cb.opposer)
        tgt = cb.target()
        r_cost = max(CARDS[cb.react[0]].cost, 1) if cb.react else 0
        paid = cb.react is not None and cb.d >= r_cost
        if self.stats is not None:
            st_all = self.stats
            for side, key, gems, avail in ((a, "pugno_att", cb.a, pa.brace), (d, "pugno_def", cb.d, pd.guard)):
                st = st_all[key][side]
                if avail > 0:
                    st[0] += 1
                    st[1] += gems == 0
                    st[2] += gems == avail
                st[3] += gems
            st_all["mods"][mods] = st_all["mods"].get(mods, 0) + 1
            if cb.react:
                st_all["reactions"][d] += 1
            if any(max(CARDS[c].cost, 1) <= pd.guard for c, _ in self.reaction_options(d)):
                st_all["react_avail"][d] += 1                          # M1
            if paid:                                                    # M2: stesse gemme di Parata, senza Reazione
                fa2, db2, _ = self.compute(cb.a, cb.d - r_cost, None, cb.opposer)
                st_all["react_decisive"][d] += self.outcome(fa2, db2, cb.opposer) != (hit, att_dead, tgt_dead)
                if cb.react[1] == "scar":                               # M3
                    st_all["react_scar"][d] += 1
                    sc = next((x for x in pd.scars if x[0] == cb.react[0] and not x[1]), None)
                    st_all["react_scar_life"][d] += sc is not None and sc[2] == "costo"
            st_all["decided_pre"][a] += self.decided_before_commit()   # M4
            st_all["target_leader"][a] += tgt is None                   # M5
            if trace["pugno_target"] is not None and paid:              # M8: gemme contate due volte
                st_all["double_gems"][d] += max(0, min(r_cost, trace["pugno_target"] - (cb.d - r_cost)))
            for q, sid in trace["src"]:                                 # M11
                self.stat_add("activations", q, sid)
        self.say(f"    pugni: attaccante {cb.a}, difensore {cb.d}" + (f" + {CARDS[cb.react[0]].name}" if cb.react else "")
                 + f" -> {fa} contro {db}")
        pa.brace -= cb.a
        pd.guard -= cb.d
        rctx = self.combat_ctx(cb)
        late_ops = []
        if paid:
            cid, rsrc = cb.react
            if rsrc == "hand":
                pd.hand.remove(cid)
            else:
                for sc in pd.scars:
                    if sc[0] == cid and not sc[1]:
                        pd.scars.remove(sc)
                        break
            pd.discard.append(cid)
            c = CARDS[cid]
            ops = c.react.get("do_from_scars", c.react["do"]) if rsrc == "scar" else c.react["do"]
            ops = [o for o in ops if o["op"] not in ("att_mod", "def_mod")]
            late_ops = [o for o in ops if "target" in o]                # sulle Unità: dopo lo scontro (C6e)
            self.run_ops(d, [o for o in ops if "target" not in o], rctx)     # C4 (d): pesca
            if self.over:
                return
        att_unit = self.unit(a, cb.att) if cb.att != "L" else None
        tgt_unit = self.unit(d, tgt) if tgt is not None else None
        if tgt_dead:
            pd.units.remove(tgt_unit)
            pd.discard.append(tgt_unit.cid)
            self.stat_add("units_defeated_in_combat", a)
            self._stancata_rimossa(a, d, tgt_unit)
            if cb.opposer is None:
                self.stat_add("removals", a)                             # M12: sconfitta da Caccia
        if att_dead:
            pa.units.remove(att_unit)
            pa.discard.append(att_unit.cid)
        if hit:
            self.stat_add("attacks_leader_hit", a)
            if cb.att == "L" and self.stats is not None:
                lh = self.stats["leader_hits"][a]
                k = 2 if pa.awakened else 0
                lh[k] += 1
                lh[k + 1] += not cb.a
                if not cb.a:
                    side = "Risvegliato" if pa.awakened else "Base"
                    self.stat_add("leader_free_rim", a, f"{pa.leader}|{side}|tot")
                    if getattr(cb, "rim_legal", False):
                        self.stat_add("leader_free_rim", a, f"{pa.leader}|{side}|rim")
            if self.alle_corde(d) and pd.fresh() == 0:
                self.lose(d, "colpo_finale")
            else:
                self.lose_life(d, "attacco_leader" if cb.att == "L" else "attacco")
        elif not tgt_dead:
            self.stat_add("stopped", a)
        self.combat = None
        self.phase = "main"
        if self.over:
            return
        self.state_checks()
        # C6 (e): prima i trigger del giocatore attivo, poi quelli del difensore
        # §7.5 (R-007 T-8): i trigger "quando sconfigge" guardano indietro e scattano anche se la loro
        # fonte è stata sconfitta nello stesso scontro; {"survived": true} li limita a chi è ancora in gioco
        if tgt_dead:
            abil, sid = (CARDS[att_unit.cid].abilities, att_unit.cid) if att_unit else (self.leader_abilities(a), pa.leader)
            self.fire(a, abil, "on_attack_defeats_unit", dict(rctx, self=cb.att, survived=not att_dead), src=sid)    # Rinnovo
            if att_unit is not None:
                gone = [att_unit] if att_dead else []
                self.fire_global(a, "on_own_unit_defeats_unit", {"survived": not att_dead}, gone)
                self.fire_global(a, "on_own_unit_attack_defeats_unit", {"survived": not att_dead}, gone)   # N4
        if att_dead and tgt_unit is not None:
            self.fire(d, CARDS[tgt_unit.cid].abilities, "on_defeats_attacker",
                      {"self": tgt_unit.uid, "survived": not tgt_dead}, src=tgt_unit.cid)
            self.fire_global(d, "on_own_unit_defeats_unit", {"survived": not tgt_dead}, [tgt_unit] if tgt_dead else [])
        if late_ops and not self.over:
            self.run_ops(d, late_ops, rctx)                             # es. raddrizza l'Unità che si opponeva
        if paid and not self.over:
            self.fire_global(d, "on_own_reaction", {})                  # N4: dopo lo scontro


def default_mulligan(s, q):
    pl = s.p[q]
    bottom = [c for c in pl.hand if CARDS[c].cost >= 5][: s.r.mulligan_max]
    for c in bottom:
        pl.hand.remove(c)
        pl.deck.insert(0, c)
    s.draw(q, len(bottom))


def new_game(leader1, deck1, leader2, deck2, rules=B0, seed=None, log=False, mulligan=None):
    s = GameState(rules)
    if log:
        s.log = []
    return s.setup(leader1, deck1, leader2, deck2, seed=seed, mulligan=mulligan)
