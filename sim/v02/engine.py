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
import json
import os
import random

from ..cards import load as load_db
from .config import B0

G1, G2 = 0, 1
RULES_VERSION = "v0.2-B0"
DATA = os.path.join(os.path.dirname(__file__), "cards_v02.json")
CARDS, LEADERS = load_db(DATA)


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
        self.scars = []             # [cid, fresh]
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
        return sum(1 for _, f in self.scars if f)


class Combat:
    __slots__ = ("att", "opposer", "a", "d", "react", "a_visible", "att_mod", "def_mod", "opened")

    def __init__(self, att):
        self.att = att              # "L" or uid of the attacking unit
        self.opposer = None         # uid of the defender's opposing unit, or None (target = Leader)
        self.a = None               # attacker's gems in the pugno
        self.d = None               # defender's gems in the pugno (Reaction cost included)
        self.react = None           # (cid, "hand"|"scar")
        self.a_visible = False
        self.att_mod = 0            # from triggers resolved in this combat
        self.def_mod = 0
        self.opened = False

    def clone(self):
        c = Combat.__new__(Combat)
        for k in Combat.__slots__:
            setattr(c, k, getattr(self, k))
        return c


def new_stats():
    return {
        "attacks": [0, 0], "attacks_leader_hit": [0, 0], "stopped": [0, 0],
        "opposed": [0, 0], "units_defeated_in_combat": [0, 0],
        "pugno_att": [[0, 0, 0, 0], [0, 0, 0, 0]],   # [combats with gems available, empty, full, gems]
        "pugno_def": [[0, 0, 0, 0], [0, 0, 0, 0]],
        "reactions": [0, 0], "mods": {}, "legal_actions": [0, 0], "decisions": [0, 0],
        "idle_turns": [0, 0], "idle3_turns": [0, 0], "turns": [0, 0],
        "lives_lost": [{}, {}], "life_at_round6": None, "awaken_round": [None, None],
        "rim_used": [0, 0], "cards_played": [{}, {}], "guard_stored": [0, 0],
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

    def static_sources(self, q):
        src = list(self.leader_abilities(q))
        for rid in self.p[q].relics:
            src += CARDS[rid].abilities
        return src

    def static_sum(self, q, name):
        total = 0
        sources = self.static_sources(q) + [ab for u in self.p[q].units for ab in CARDS[u.cid].abilities]
        for ab in sources:
            if ab.get("static") == name and self.cond_ok(q, ab.get("if"), {}):
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
        return g

    def furia(self, q):
        return len(self.p[q].scars) + self.static_sum(q, "furia_bonus")

    def parata_per_gemma(self, q):
        for ab in self.leader_abilities(q):
            if ab.get("static") == "parata_per_gemma":
                return ab["value"]
        return self.r.parata_per_gemma

    def num(self, v, q=None):
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
            if k == "infusion_count":       # v0.1 condition: never true in v0.2
                return False
        return True

    def matches(self, q_unit, u, sel, ctx=None):
        c = CARDS[u.cid]
        if "cost_le" in sel and c.cost > sel["cost_le"]:
            return False
        if "ready" in sel and u.ready != sel["ready"]:
            return False
        if "power_le" in sel and self.unit_power(q_unit, u) > sel["power_le"]:
            return False
        if "keyword" in sel and not c.has(sel["keyword"]):
            return False
        if sel.get("attacker") and (ctx or {}).get("attacker_uid") != u.uid:
            return False
        return True

    def unit_power(self, q, u, ctx=None):
        """Printed Forza + static bonuses. ctx (during a combat): attacker_uid, pugno."""
        ctx = dict(ctx or {}, self=u.uid)
        c = CARDS[u.cid]
        p = c.power
        for ab in c.abilities:
            if ab.get("static") == "power" and "applies_to" not in ab and self.cond_ok(q, ab.get("if"), ctx):
                p += self.num(ab["value"], q)
        sources = self.static_sources(q) + [ab for v in self.p[q].units for ab in CARDS[v.cid].abilities
                                            if "applies_to" in ab]
        for ab in sources:
            if ab.get("static") == "power" and "applies_to" in ab:
                sel = ab["applies_to"]
                if sel.get("side", "own") == "own" and self.matches(q, u, sel, ctx) and self.cond_ok(q, ab.get("if"), ctx):
                    p += self.num(ab["value"], q)
        return p

    def leader_power(self, q, ctx=None):
        p = self.r.leader_power_awakened if self.p[q].awakened else self.r.leader_power
        if ctx and ctx.get("attacker_uid") == "L":
            for ab in self.static_sources(q):
                sel = ab.get("applies_to")
                if ab.get("static") == "power" and sel and sel.get("attacker") and set(sel) <= {"side", "attacker"} \
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
        pl.scars.append([pl.life.pop(), not ignore_saldo])
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
            for _ in range(self.r.life):
                pl.life.append(pl.deck.pop())
        self.active = G1
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
        stored = min(pl.brace, self.guard_max(a))           # 10b
        pl.guard = stored
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
            return [("no_oppose",)] + [("oppose", u.uid) for u in self.p[d].units if u.ready]
        if ph == "pugno_def":
            return self._parry_options(d)
        if ph == "risposta":
            return ([("oppose", u.uid) for u in self.p[d].units if u.ready] + self._parry_options(d))
        return []

    def reaction_options(self, d):
        pl = self.p[d]
        out, seen = [], set()
        for src, pile in (("hand", pl.hand), ("scar", [c for c, f in pl.scars if not f])):
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
            for cid in sorted({c for c, f in pl.scars if not f}):
                acts.append(("rim", cid))
        if pl.l_ready:
            for i, ab in enumerate(self.leader_abilities(a)):
                if ab.get("activated") and pl.brace >= ab.get("cost", 0):
                    for t in self._targets(a, ab.get("target")):
                        acts.append(("ability", "L", i, t))
        for u in pl.units:
            if u.ready:
                for i, ab in enumerate(CARDS[u.cid].abilities):
                    if ab.get("activated") and pl.brace >= ab.get("cost", 0):
                        for t in self._targets(a, ab.get("target")):
                            acts.append(("ability", u.uid, i, t))
        if self.can_attack(a):
            if pl.l_ready:
                acts.append(("attack", "L"))
            for u in pl.units:
                if u.ready:
                    acts.append(("attack", u.uid))
        return acts

    def _targets(self, a, sel):
        if sel is None:
            return [None]
        side = a if sel.get("side", "own") == "own" else 1 - a
        return [u.uid for u in self.p[side].units if self.matches(side, u, sel)]

    def pay_costs(self, q, costs, check_only=False):
        for c in costs or ():
            if "lose_life" in c and not self.can_pay_life(q, c["lose_life"], c.get("floor", 0)):
                return False
        if not check_only:
            for c in costs or ():
                for _ in range(c.get("lose_life", 0)):
                    self.lose_life(q, "costo")
        return True

    # ------------------------------------------------------------------ step
    def step(self, act):
        if self.stats is not None:
            q = self.decider()
            self.stats["decisions"][q] += 1
            self.stats["legal_actions"][q] += len(self.legal_actions())
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
            self.run_ops(a, ab["do"], self._chosen(a, ab.get("target"), t))
        elif k == "attack":
            self._declare(a, act[1])
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
    def fire(self, q, abilities, event, ctx):
        for ab in abilities:
            if ab.get("trigger") == event and self.cond_ok(q, ab.get("if"), ctx):
                self.run_ops(q, [o for o in ab["do"] if o["op"] not in ("att_mod", "def_mod")], ctx)

    def fire_global(self, q, event, ctx):
        for u in list(self.p[q].units):
            self.fire(q, CARDS[u.cid].abilities, event, dict(ctx, self=u.uid))
        self.fire(q, self.leader_abilities(q), event, dict(ctx, self="L"))

    def run_ops(self, q, ops, ctx):
        for op in ops:
            if self.over:
                return
            k = op["op"]
            n = self.num(op.get("n", 0), q)
            if k == "draw":
                self.draw(q, n)
            elif k in ("stanca", "defeat", "raddrizza"):
                u = self.unit(ctx["chosen_owner"], ctx["chosen"])
                if u is None:
                    continue
                if k == "stanca":
                    u.ready = False
                elif k == "raddrizza":
                    u.ready = True
                else:
                    self.p[ctx["chosen_owner"]].units.remove(u)
                    self.p[ctx["chosen_owner"]].discard.append(u.cid)
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
                    if o["op"] == "att_mod":
                        am += self.num(o.get("n", 0), q)
                    elif o["op"] == "def_mod":
                        dm += self.num(o.get("n", 0), q)
        return am, dm

    # ------------------------------------------------------------------ combat
    def _declare(self, a, att):
        pl = self.p[a]
        d = 1 - a
        if att == "L":
            pl.l_ready = False
        else:
            self.unit(a, att).ready = False
            self.fire(a, CARDS[self.unit(a, att).cid].abilities, "on_attack", {"self": att})
        self.combat = Combat(att)
        self.stat_add("attacks", a)
        self.say(f"  P{a+1} attacca con {self.describe(a, att)}")
        if self.over:
            return
        if self.r.pugno == "nessuno":
            self.phase = "impeto"
        elif self.r.opposizione == "prima" and any(u.ready for u in self.p[d].units):
            self.phase = "oppose"
        else:
            self.phase = "pugno_att"

    def _oppose(self, uid):
        a, d = self.active, 1 - self.active
        u = self.unit(d, uid)
        self.combat.opposer = uid
        if not (CARDS[u.cid].has("scudo") and self.r.scudo == "oppone_senza_ruotarsi"):
            u.ready = False
        self.stat_add("opposed", a)
        self.say(f"    P{d+1} oppone {CARDS[u.cid].name}")
        self.fire(d, CARDS[u.cid].abilities, "on_oppose", {"self": uid})

    def compute(self, a_gems, d_gems, react, opposer, count_mods=False):
        """(Fa, Db, modifiers) for given pugno contents. Pure: used by the engine and by the AI."""
        a, d = self.active, 1 - self.active
        cb = self.combat
        mods = 0
        ctx_a = {"attacker_uid": cb.att, "pugno": a_gems}
        if cb.att == "L":
            base_a = self.r.leader_power_awakened if self.p[a].awakened else self.r.leader_power
            fa = self.leader_power(a, ctx_a)
            mods += fa != base_a
        else:
            u = self.unit(a, cb.att)
            fa = self.unit_power(a, u, ctx_a)
            mods += fa != CARDS[u.cid].power
            if opposer is not None and CARDS[u.cid].has("bracconiere"):
                fa += CARDS[u.cid].kw("bracconiere")
                mods += 1
            am, _ = self.trigger_mods(a, CARDS[u.cid].abilities, "on_attack", dict(ctx_a, self=cb.att))
            fa += am
            mods += am != 0
        fa += a_gems * self.r.forza_per_gemma
        mods += a_gems > 0
        parry = d_gems
        r_att = r_def = 0
        if react is not None:
            cid, src = react
            c = CARDS[cid]
            cost = max(c.cost, 1)
            if d_gems >= cost:
                parry -= cost
                ops = c.react.get("do_from_scars", c.react["do"]) if src == "scar" else c.react["do"]
                for o in ops:
                    if o["op"] == "att_mod":
                        r_att += self.num(o["n"], d)
                    elif o["op"] == "def_mod":
                        r_def += self.num(o["n"], d)
                mods += 1
        ctx_d = {"pugno": d_gems, "attacker_uid": cb.att}
        if opposer is None:
            db = self.r.tempra
        else:
            ou = self.unit(d, opposer)
            db = self.unit_power(d, ou)
            mods += db != CARDS[ou.cid].power
            _, dm = self.trigger_mods(d, CARDS[ou.cid].abilities, "on_oppose", {"self": opposer})
            db += dm
            mods += dm != 0
        db += parry * self.parata_per_gemma(d)
        mods += parry > 0
        for ab in self.static_sources(d):
            if ab.get("static") == "combat" and ab.get("role") == "defense" and self.cond_ok(d, ab.get("if"), ctx_d):
                fa += ab.get("att_mod", 0)
                db += ab.get("def_mod", 0)
                mods += 1
        fa += r_att + cb.att_mod
        db += r_def + cb.def_mod
        return fa, db, mods

    def outcome(self, fa, db, opposer):
        """(leader_hit, attacker_unit_defeated, opposer_defeated)."""
        a, d = self.active, 1 - self.active
        if opposer is None:
            return fa >= db, False, False
        pareggi = self.r.scudo == "vince_pareggi" and CARDS[self.unit(d, opposer).cid].has("scudo")
        if self.combat.att == "L":
            return False, False, (fa > db) if pareggi else (db <= fa)
        if fa > db:
            return False, False, True
        if fa < db:
            return False, True, False
        return False, True, not pareggi

    def _open_and_resolve(self):
        a, d = self.active, 1 - self.active
        cb = self.combat
        pa, pd = self.p[a], self.p[d]
        cb.opened = True
        fa, db, mods = self.compute(cb.a, cb.d, cb.react, cb.opposer)
        hit, att_dead, opp_dead = self.outcome(fa, db, cb.opposer)
        if self.stats is not None:
            for side, key, gems, avail in ((a, "pugno_att", cb.a, pa.brace), (d, "pugno_def", cb.d, pd.guard)):
                st = self.stats[key][side]
                if avail > 0:
                    st[0] += 1
                    st[1] += gems == 0
                    st[2] += gems == avail
                st[3] += gems
            self.stats["mods"][mods] = self.stats["mods"].get(mods, 0) + 1
            if cb.react:
                self.stats["reactions"][d] += 1
        self.say(f"    pugni: attaccante {cb.a}, difensore {cb.d}" + (f" + {CARDS[cb.react[0]].name}" if cb.react else "")
                 + f" -> {fa} contro {db}")
        pa.brace -= cb.a
        pd.guard -= cb.d
        if cb.react:
            cid, src = cb.react
            if cb.d >= max(CARDS[cid].cost, 1):
                if src == "hand":
                    pd.hand.remove(cid)
                else:
                    for sc in pd.scars:
                        if sc[0] == cid and not sc[1]:
                            pd.scars.remove(sc)
                            break
                pd.discard.append(cid)
        att_unit = self.unit(a, cb.att) if cb.att != "L" else None
        opp_unit = self.unit(d, cb.opposer) if cb.opposer is not None else None
        if opp_dead:
            pd.units.remove(opp_unit)
            pd.discard.append(opp_unit.cid)
            self.stat_add("units_defeated_in_combat", a)
        if att_dead:
            pa.units.remove(att_unit)
            pa.discard.append(att_unit.cid)
        if hit:
            self.stat_add("attacks_leader_hit", a)
            if self.alle_corde(d) and pd.fresh() == 0:
                self.lose(d, "colpo_finale")
            else:
                self.lose_life(d, "attacco_leader" if cb.att == "L" else "attacco")
        elif not opp_dead:
            self.stat_add("stopped", a)
        self.combat = None
        self.phase = "main"
        if self.over:
            return
        self.state_checks()
        if att_dead and opp_unit is not None and not opp_dead:
            self.fire(d, CARDS[opp_unit.cid].abilities, "on_defeats_attacker", {"self": opp_unit.uid})
            self.fire_global(d, "on_own_unit_defeats_unit", {})
        if opp_dead and att_unit is not None and not att_dead:
            self.fire_global(a, "on_own_unit_defeats_unit", {})


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
