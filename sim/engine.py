"""Game engine for CICATRICI (regolamento v0.1 condiviso).

The engine holds only the skeleton of the game: zones, turn loop, Fornace/Brace/
Guardia, playing cards, infusion, the 9-step combat with its two defender decisions,
Vita/Cicatrici and the colpo finale. Every other rule is a module (sim/rules.py) and
every card effect is data (sim/data/*.json, interpreted by sim/effects.py).

It is a decision-point state machine:
  state.decider()        which player must choose now (None when the game is over)
  state.legal_actions()  the choices
  state.step(action)     apply one choice
Decision points (`state.phase`): "main" (active player), "intercept" and "react"
(defender, §8 steps 3 and 5). Section numbers refer to tcg/regolamento_v0.1.md.
"""
import random

from . import effects
from . import rules as rule_modules
from .cards import CARDS, LEADERS
from .config import DEFAULT

G1, G2 = 0, 1
RULES_VERSION = "v0.1-condiviso"


class Unit:
    __slots__ = ("uid", "cid", "exposed", "attacks", "entered", "inf", "temp", "perm", "renew")

    def __init__(self, uid, cid, entered):
        self.uid = uid
        self.cid = cid
        self.exposed = False
        self.attacks = 0
        self.entered = entered      # owner's turn number when it entered
        self.inf = 0                # infusion counter this turn (§5.3)
        self.temp = 0               # +Forza until end of turn (includes infusion)
        self.perm = 0               # permanent +Forza
        self.renew = False          # Rinnovo until end of turn

    def clone(self):
        u = Unit.__new__(Unit)
        u.uid, u.cid, u.exposed, u.attacks, u.entered = self.uid, self.cid, self.exposed, self.attacks, self.entered
        u.inf, u.temp, u.perm, u.renew = self.inf, self.temp, self.perm, self.renew
        return u


class Player:
    __slots__ = ("leader", "awakened", "l_exposed", "l_attacks", "l_inf", "l_temp",
                 "life", "scars", "hand", "deck", "discard", "units", "relics",
                 "furnace", "brace", "guard", "spark", "turn_no", "lost_this_turn",
                 "reactions_used", "furia_bonus", "flags", "once_flags")

    def __init__(self, leader):
        self.leader = leader
        self.awakened = False
        self.l_exposed = False
        self.l_attacks = 0
        self.l_inf = 0
        self.l_temp = 0
        self.life = []
        self.scars = []
        self.hand = []
        self.deck = []              # top of the deck is the END of the list
        self.discard = []
        self.units = []
        self.relics = []
        self.furnace = 0
        self.brace = 0
        self.guard = 0
        self.spark = False
        self.turn_no = 0
        self.lost_this_turn = 0
        self.reactions_used = 0
        self.furia_bonus = 0        # extra Furia count until end of turn (Vey)
        self.flags = set()          # per-turn flags owned by rule modules
        self.once_flags = set()     # "once per turn" card triggers

    def flag(self, name):
        return name in self.flags

    def set_flag(self, name):
        self.flags.add(name)

    def clone(self):
        p = Player.__new__(Player)
        for s in Player.__slots__:
            v = getattr(self, s)
            if s == "units":
                v = [u.clone() for u in v]
            elif isinstance(v, (list, set)):
                v = v.copy()
            setattr(p, s, v)
        return p


class Combat:
    __slots__ = ("att", "tgt", "att_mod", "def_mod", "interceptor", "ready_interceptor_after",
                 "would_hit_pre")

    def __init__(self, att, tgt):
        self.att = att              # "L" or uid of an attacking unit (active player)
        self.tgt = tgt              # "L" or uid of a defending unit
        self.att_mod = 0
        self.def_mod = 0
        self.interceptor = None
        self.ready_interceptor_after = False
        self.would_hit_pre = None

    def clone(self):
        c = Combat.__new__(Combat)
        for s in Combat.__slots__:
            setattr(c, s, getattr(self, s))
        return c


def new_stats():
    return {
        "lives_lost": [{}, {}],          # per player: source -> count
        "attacks_leader": [0, 0],        # attacks on the enemy Leader declared by player
        "hits_leader": [0, 0],
        "stopped_by_reaction": [0, 0],   # player's attacks on the Leader stopped by a reaction
        "stopped_by_intercept": [0, 0],
        "threats_at_reaction": [0, 0],   # player's attacks on the Leader that would hit at step 5
        "reactions": [{}, {}],           # kind -> count, by reacting player
        "rim_used": [0, 0],
        "rim_possible": [0, 0],          # turns in which Rimarginare was legal at some point
        "guard_stored": [0, 0],
        "guard_hist": [{}, {}],          # Guardia accantonata a fine turno -> numero di turni
        "turns_ended": [0, 0],
        "awaken_turn": [None, None],
        "life_at_round6": None,          # (Vite G1, Vite G2) at the start of G1's turn 7
        "infusions": [0, 0],
        "leader_attacks": [0, 0],
        "cards_played": [{}, {}],        # cid -> count
        "cards_drawn": [{}, {}],         # cid -> count (opening hand included)
    }


class GameState:
    def __init__(self, rules=DEFAULT):
        self.r = rules
        self.modules = rule_modules.build(rules.modules)
        self.p = [None, None]
        self.active = G1
        self.phase = "main"
        self.combat = None
        self.snapshot = False       # §6.1 step 2: opponent Alle Corde at start of this turn
        self.winner = None
        self.end_reason = None
        self.next_uid = 1
        self.rng = random.Random()
        self.stats = new_stats()
        self.log = None             # list of lines when logging is on
        self._rim_flag = False

    # ------------------------------------------------------------------ utils
    def clone(self):
        s = GameState.__new__(GameState)
        s.r = self.r
        s.modules = self.modules            # modules are stateless
        s.p = [self.p[0].clone(), self.p[1].clone()]
        s.active = self.active
        s.phase = self.phase
        s.combat = self.combat.clone() if self.combat else None
        s.snapshot = self.snapshot
        s.winner = self.winner
        s.end_reason = self.end_reason
        s.next_uid = self.next_uid
        s.rng = random.Random(self.rng.random())
        s.stats = None              # search clones do not collect stats
        s.log = None
        s._rim_flag = self._rim_flag
        return s

    def say(self, msg):
        if self.log is not None:
            self.log.append(msg)

    def stat(self, key, player, inc=1, sub=None):
        if self.stats is None:
            return
        if sub is None:
            self.stats[key][player] += inc
        else:
            d = self.stats[key][player]
            d[sub] = d.get(sub, 0) + inc

    def mark_rim_possible(self, a):
        self._rim_flag = True

    @property
    def over(self):
        return self.end_reason is not None

    def decider(self):
        if self.over:
            return None
        if self.phase in ("intercept", "react"):
            return 1 - self.active
        return self.active

    def unit(self, owner, uid):
        for u in self.p[owner].units:
            if u.uid == uid:
                return u
        return None

    # ------------------------------------------------------------------ derived values
    def clock(self):
        """Turn number used by every 'dal turno N' threshold (§6, variant V4)."""
        if self.r.clessidra_counter == "round":
            return self.p[G1].turn_no
        return self.p[self.active].turn_no

    def saldo_cap(self):
        cap = None
        for m in self.modules:
            cap = m.saldo_cap(self, cap)
        return cap

    def alle_corde(self, q):
        if not self.p[q].life:
            return True
        return any(m.is_alle_corde(self, q) for m in self.modules)

    def guard_max(self, q):
        g = self.r.guard_max_awakened if self.p[q].awakened else self.r.guard_max
        return g + effects.static_total(self, q, "guard_max")

    def furia_count(self, q):
        return len(self.p[q].scars) + self.p[q].furia_bonus

    def unit_power(self, owner, u, vs_exposed_unit=False):
        c = CARDS[u.cid]
        p = c.power + u.perm + u.temp + effects.static_power(self, owner, u)
        if vs_exposed_unit and c.has("bracconiere"):
            p += c.kw("bracconiere")
        return p

    def leader_power(self, q):
        pl = self.p[q]
        return (self.r.leader_power_awakened if pl.awakened else self.r.leader_power) + pl.l_temp

    def tempra(self, q):
        return self.r.leader_tempra

    def parry_per_guard(self, q):
        return effects.leader_modifier(self, q, "parry_per_guard", self.r.parry_per_guard)

    # ------------------------------------------------------------------ Vita
    def lose_life(self, q, n, source, ignore_saldo=False):
        pl = self.p[q]
        for _ in range(n):
            if not pl.life:
                return
            cap = None if ignore_saldo else self.saldo_cap()
            if cap is not None and pl.lost_this_turn >= cap:
                return
            card = pl.life.pop()
            if not any(m.on_life_lost(self, q, card) for m in self.modules):
                pl.scars.append(card)
            if not ignore_saldo:
                pl.lost_this_turn += 1
            self.stat("lives_lost", q, 1, source)
            self.say(f"    P{q+1} perde 1 Vita ({source}): restano {len(pl.life)}")

    def can_pay_life(self, q, n, floor=0):
        pl = self.p[q]
        cap = self.saldo_cap()
        return len(pl.life) - n >= max(floor, 0) and (cap is None or pl.lost_this_turn + n <= cap)

    def draw(self, q, n=1):
        pl = self.p[q]
        for _ in range(n):
            if pl.deck:
                cid = pl.deck.pop()
                pl.hand.append(cid)
                self.stat("cards_drawn", q, 1, cid)
            else:
                if not pl.life:
                    self.lose(q, "mazzo_vuoto")
                    return
                self.lose_life(q, 1, "mazzo_vuoto")

    def lose(self, q, reason):
        if self.over:
            return
        self.winner = 1 - q
        self.end_reason = reason
        self.say(f"P{q+1} perde ({reason})")

    def win(self, q, reason):
        if self.over:
            return
        self.winner = q
        self.end_reason = reason
        self.say(f"P{q+1} vince ({reason})")

    def awaken(self, q):
        self.p[q].awakened = True
        if self.stats is not None and self.stats["awaken_turn"][q] is None:
            self.stats["awaken_turn"][q] = self.p[q].turn_no
        self.say(f"    {LEADERS[self.p[q].leader].name.split(',')[0]} (P{q+1}) si Risveglia")

    def state_checks(self):
        """§7.4."""
        if self.over:
            return
        for m in self.modules:
            m.state_check(self)
        for q in (G1, G2):
            gm = self.guard_max(q)
            if self.p[q].guard > gm:
                self.p[q].guard = gm

    # ------------------------------------------------------------------ setup
    def setup(self, leader1, deck1, leader2, deck2, seed=None, mulligan=None):
        """§4. `mulligan(state, q) -> hand indices to put on the bottom`."""
        if seed is not None:
            self.rng.seed(seed)
        decks = [list(deck1), list(deck2)]
        leaders = [leader1, leader2]
        for q in (G1, G2):
            pl = Player(leaders[q])
            pl.deck = decks[q]
            self.rng.shuffle(pl.deck)
            n = self.r.hand_g1 if q == G1 else self.r.hand_g2
            self.p[q] = pl
            self.draw(q, n)
        for q in (G1, G2):
            pl = self.p[q]
            idx = sorted(set((mulligan or default_mulligan)(self, q)))[: self.r.mulligan_max]
            if idx:
                out = [pl.hand[i] for i in idx]
                pl.hand = [c for i, c in enumerate(pl.hand) if i not in idx]
                pl.deck = out + pl.deck
                self.draw(q, len(out))
        for q in (G1, G2):
            pl = self.p[q]
            for _ in range(self.r.life):
                pl.life.append(pl.deck.pop())
        for m in self.modules:
            m.on_setup(self)
        self.active = G1
        self.begin_turn()
        return self

    # ------------------------------------------------------------------ turn
    def begin_turn(self):
        """§6.1 Ripristino and §6.2 Pesca."""
        a = self.active
        pl, op = self.p[a], self.p[1 - a]
        pl.turn_no += 1
        if pl.turn_no > self.r.max_turns and op.turn_no >= self.r.max_turns:
            self.end_reason = "non_conclusa"
            return
        if self.stats is not None and a == G1 and pl.turn_no == 7:
            self.stats["life_at_round6"] = (len(self.p[G1].life), len(self.p[G2].life))
        self.say(f"--- Turno {pl.turn_no} di P{a+1} | Vite {len(self.p[0].life)}-{len(self.p[1].life)}")
        for q in (G1, G2):
            self.p[q].lost_this_turn = 0
            self.p[q].flags.clear()
            self.p[q].once_flags.clear()
        op.reactions_used = 0
        self._rim_flag = False
        self.snapshot = self.alle_corde(1 - a)          # step 2
        for m in self.modules:                          # step 3 and other start-of-turn rules
            m.on_turn_start(self, a)
            if self.over:
                return
        pl.guard = 0                                    # step 4
        pl.l_exposed = False                            # step 5
        pl.l_attacks = 0
        for u in pl.units:
            u.exposed = False
            u.attacks = 0
            u.renew = False
        pl.furnace = min(pl.furnace + 1, self.r.furnace_max)   # step 6
        pl.brace = pl.furnace
        self.state_checks()
        if self.over:
            return
        if not any(m.skip_draw(self, a) for m in self.modules):
            self.draw(a)
        self.state_checks()
        self.phase = "main"

    def end_turn(self):
        """§6.4 Fine."""
        a = self.active
        pl = self.p[a]
        stored = min(pl.brace, self.guard_max(a))
        pl.guard = stored
        if self.stats is not None:
            self.stats["guard_stored"][a] += stored
            gh = self.stats["guard_hist"][a]
            gh[stored] = gh.get(stored, 0) + 1
            self.stats["turns_ended"][a] += 1
            if self._rim_flag:
                self.stats["rim_possible"][a] += 1
        pl.brace = 0
        pl.l_inf = pl.l_temp = 0
        pl.furia_bonus = 0
        for u in pl.units:
            u.inf = u.temp = 0
            u.renew = False
        if len(pl.hand) > self.r.hand_limit:
            pl.hand.sort(key=lambda c: CARDS[c].cost)
            while len(pl.hand) > self.r.hand_limit:
                pl.discard.append(pl.hand.pop())
        self.state_checks()
        if self.over:
            return
        self.active = 1 - a
        self.combat = None
        self.begin_turn()

    # ------------------------------------------------------------------ legal actions
    def legal_actions(self):
        if self.over:
            return []
        if self.phase == "main":
            return self._main_actions()
        if self.phase == "intercept":
            return self._intercept_actions()
        if self.phase == "react":
            return self._react_actions()
        return []

    def attackers(self, a):
        pl = self.p[a]
        if not all(m.can_attack(self, a) for m in self.modules):
            return []
        out = []
        if not pl.l_exposed and pl.l_attacks == 0:
            out.append("L")
        for u in pl.units:
            c = CARDS[u.cid]
            if u.attacks == 0 and not u.exposed:
                if u.entered < pl.turn_no or c.has("assalto"):
                    out.append(u.uid)
            elif u.attacks == 1 and u.renew:
                out.append(u.uid)
        return out

    def _main_actions(self):
        a = self.active
        pl, op = self.p[a], self.p[1 - a]
        acts = [("end",)]
        for m in self.modules:
            acts += m.extra_actions(self, a)
        seen = set()
        for cid in pl.hand:
            if cid in seen:
                continue
            seen.add(cid)
            c = CARDS[cid]
            if c.cost > pl.brace or c.type == "reaction":
                continue
            if c.type == "unit":
                if len(pl.units) < self.r.max_units:
                    acts.append(("play", cid, None))
            elif c.type == "relic":
                if len(pl.relics) < self.r.max_relics:
                    acts.append(("play", cid, None))
            elif c.type == "tactic":
                for t in self._play_targets(a, c.play or {}):
                    acts.append(("play", cid, t))
        if pl.brace >= 1:
            cap = self.r.infusion_cap
            if not cap or pl.l_inf < cap:
                acts.append(("infuse", "L"))
            for u in pl.units:
                if not cap or u.inf < cap:
                    acts.append(("infuse", u.uid))
        for i, ab in enumerate(effects.leader_abilities(self, a)):
            if ab.get("activated") and pl.brace >= ab.get("cost", 0) and not (ab.get("exhaust") and pl.l_exposed):
                for t in self._play_targets(a, ab):
                    acts.append(("leader_ability", i, t))
        tgts = ["L"] + [u.uid for u in op.units if u.exposed]
        for att in self.attackers(a):
            for t in tgts:
                acts.append(("attack", att, t))
        return acts

    def _play_targets(self, a, spec):
        if not effects.pay_costs(self, a, spec.get("costs"), check_only=True):
            return []
        sel = spec.get("target")
        if sel is None:
            return [None]
        return effects.select(self, a, sel)

    def _intercept_actions(self):
        d = 1 - self.active
        return [("no_intercept",)] + [("intercept", u.uid) for u in self.p[d].units
                                       if not u.exposed and CARDS[u.cid].has("scudo")]

    def reaction_limit(self, d):
        lim = self.r.reactions_per_turn
        for m in self.modules:
            lim = m.reaction_limit(self, d, lim)
        return lim

    def _react_actions(self):
        d = 1 - self.active
        pl = self.p[d]
        acts = [("no_react",)]
        if pl.reactions_used >= self.reaction_limit(d) or pl.guard < 1:
            return acts
        kmax = pl.guard if not self.r.parry_max_guard else min(pl.guard, self.r.parry_max_guard)
        for k in range(1, kmax + 1):
            acts.append(("parry", k))
        seen = set()
        for src, pile in (("hand", pl.hand), ("scar", pl.scars)):
            for cid in pile:
                c = CARDS[cid]
                if c.type == "reaction" and (src, cid) not in seen and max(c.cost, 1) <= pl.guard:
                    seen.add((src, cid))
                    acts.append(("reaction", cid, src))
        if not pl.l_exposed:
            for i, ab in enumerate(effects.leader_abilities(self, d)):
                if ab.get("reaction") and max(ab.get("guard_cost", 1), 1) <= pl.guard:
                    acts.append(("leader_reaction", i))
        return acts

    # ------------------------------------------------------------------ step
    def step(self, action):
        if self.phase == "main":
            self._main_step(action)
        elif self.phase == "intercept":
            self._do_intercept(action)
        elif self.phase == "react":
            self._do_react(action)
        if self.phase == "main" and not self.over:
            self.state_checks()

    def _main_step(self, action):
        a = self.active
        pl = self.p[a]
        kind = action[0]
        if kind == "end":
            self.end_turn()
        elif kind == "play":
            self._play(a, action[1], action[2])
        elif kind == "infuse":
            self._infuse(a, action[1])
        elif kind == "leader_ability":
            ab = effects.leader_abilities(self, a)[action[1]]
            pl.brace -= ab.get("cost", 0)
            if ab.get("exhaust"):
                pl.l_exposed = True
            effects.run_ops(self, a, ab["do"], self._ctx_chosen(a, ab, action[2]))
        elif kind == "attack":
            self._declare(a, action[1], action[2])
        else:
            for m in self.modules:
                if m.do_action(self, a, action):
                    return
            raise ValueError(f"azione sconosciuta: {action}")

    def _ctx_chosen(self, a, spec, target):
        sel = spec.get("target") or {}
        owner = a if sel.get("side", "own") == "own" else 1 - a
        return {"chosen": target, "chosen_owner": owner, "self": "L"}

    def _play(self, a, cid, target):
        pl = self.p[a]
        c = CARDS[cid]
        pl.hand.remove(cid)
        pl.brace -= c.cost
        self.stat("cards_played", a, 1, cid)
        self.say(f"  P{a+1} gioca {c.name}")
        if c.type == "unit":
            u = Unit(self.next_uid, cid, pl.turn_no)
            self.next_uid += 1
            pl.units.append(u)
            effects.fire(self, "on_enter", a, {"self": u.uid})
        elif c.type == "relic":
            pl.relics.append(cid)
        elif c.type == "tactic":
            spec = c.play or {}
            effects.pay_costs(self, a, spec.get("costs"))
            effects.run_ops(self, a, spec.get("do", []), self._ctx_chosen(a, spec, target))
            pl.discard.append(cid)

    def _infuse(self, a, who):
        pl = self.p[a]
        pl.brace -= 1
        self.stat("infusions", a)
        if who == "L":
            pl.l_inf += 1
            pl.l_temp += 1
            n = pl.l_inf
        else:
            u = self.unit(a, who)
            u.inf += 1
            u.temp += 1
            n = u.inf
        effects.fire(self, "on_infuse", a, {"infused": who, "count": n})

    # ------------------------------------------------------------------ combat (§8)
    def _declare(self, a, att, tgt):
        pl, op = self.p[a], self.p[1 - a]
        if att == "L":
            pl.l_exposed = True
            pl.l_attacks += 1
            self.stat("leader_attacks", a)
        else:
            u = self.unit(a, att)
            u.exposed = True
            u.attacks += 1
        if tgt == "L":
            self.stat("attacks_leader", a)
        self.combat = Combat(att, tgt)
        self.say(f"  P{a+1} attacca: {self.describe(a, att)} -> {self.describe(1 - a, tgt)}")
        if att != "L":                                   # step 2
            effects.fire(self, "on_attack", a, {"self": att})
        if any(not v.exposed and CARDS[v.cid].has("scudo") for v in op.units):
            self.phase = "intercept"                     # step 3
            return
        self._to_react()

    def _do_intercept(self, action):
        a, d = self.active, 1 - self.active
        cb = self.combat
        if action[0] == "intercept":
            u = self.unit(d, action[1])
            u.exposed = True
            if cb.tgt == "L" and self.would_hit():
                self.stat("stopped_by_intercept", a)
            cb.tgt = u.uid
            cb.interceptor = u.uid
            self.say(f"    P{d+1} intercetta con {CARDS[u.cid].name}")
            effects.fire(self, "on_intercept", d, {"self": u.uid})    # step 4
        self._to_react()

    def _to_react(self):
        if self.combat.tgt == "L" and self.would_hit():
            self.stat("threats_at_reaction", self.active)
        if len(self._react_actions()) > 1:
            self.combat.would_hit_pre = self.would_hit()
            self.phase = "react"                         # step 5
        else:
            self._resolve()

    def _do_react(self, action):
        a, d = self.active, 1 - self.active
        pl = self.p[d]
        cb = self.combat
        kind = action[0]
        if kind != "no_react":
            pl.reactions_used += 1
            if kind == "parry":
                k = action[1]
                pl.guard -= k
                cb.def_mod += self.parry_per_guard(d) * k
                self.stat("reactions", d, 1, "parata")
            elif kind == "reaction":
                cid, src = action[1], action[2]
                c = CARDS[cid]
                pl.guard -= max(c.cost, 1)
                (pl.hand if src == "hand" else pl.scars).remove(cid)
                pl.discard.append(cid)
                ops = c.react.get("do_from_scars", c.react["do"]) if src == "scar" else c.react["do"]
                effects.run_ops(self, d, ops, {"self": None})
                self.stat("reactions", d, 1, cid + ("@cicatrice" if src == "scar" else ""))
            elif kind == "leader_reaction":
                ab = effects.leader_abilities(self, d)[action[1]]
                pl.guard -= max(ab.get("guard_cost", 1), 1)
                effects.run_ops(self, d, ab["do"], {"self": "L"})
                self.stat("reactions", d, 1, "leader")
            self.say(f"    P{d+1} reagisce: {action}")
            if cb.tgt == "L" and cb.would_hit_pre and not self.would_hit():
                self.stat("stopped_by_reaction", a)
        self._resolve()

    def att_power(self):
        a = self.active
        cb = self.combat
        if cb.att == "L":
            return self.leader_power(a) + cb.att_mod
        u = self.unit(a, cb.att)
        return self.unit_power(a, u, vs_exposed_unit=cb.tgt != "L") + cb.att_mod

    def def_value(self):
        d = 1 - self.active
        cb = self.combat
        if cb.tgt == "L":
            return self.tempra(d) + cb.def_mod
        return self.unit_power(d, self.unit(d, cb.tgt)) + cb.def_mod

    def would_hit(self):
        fa, db = self.att_power(), self.def_value()
        if self.combat.tgt == "L":
            return fa > db if self.r.leader_hit_strict else fa >= db
        return fa >= db

    def _resolve(self):
        """§8 steps 6-9."""
        a, d = self.active, 1 - self.active
        cb = self.combat
        att_unit = self.unit(a, cb.att) if cb.att != "L" else None
        tgt_unit = self.unit(d, cb.tgt) if cb.tgt != "L" else None
        defeated = []
        hit = False
        if (cb.att == "L" or att_unit) and (cb.tgt == "L" or tgt_unit):     # step 6
            fa, db = self.att_power(), self.def_value()
            if cb.tgt == "L":
                hit = fa > db if self.r.leader_hit_strict else fa >= db
            elif cb.att == "L":
                if db <= fa:
                    defeated.append((d, tgt_unit))
            elif fa > db:
                defeated.append((d, tgt_unit))
            elif fa < db:
                defeated.append((a, att_unit))
            else:
                defeated += [(d, tgt_unit), (a, att_unit)]
        for owner, u in defeated:                                            # step 7
            self.p[owner].units.remove(u)
            self.p[owner].discard.append(u.cid)
            self.say(f"    {CARDS[u.cid].name} (P{owner+1}) sconfitta")
        if hit:
            self.stat("hits_leader", a)
            if self.snapshot:
                self.win(a, "colpo_finale")
                return
            self.lose_life(d, 1, "attacco_leader" if cb.att == "L" else "attacco_unita")
        self.state_checks()                                                  # step 8
        if self.over:
            return
        lost_ids = {id(u) for _, u in defeated}                              # step 9
        if att_unit is not None and id(att_unit) in lost_ids and tgt_unit is not None:
            effects.fire(self, "on_defeats_attacker", d, {"self": tgt_unit.uid, "self_unit": tgt_unit})
            effects.fire(self, "on_own_unit_defeats_exposed", d, {"defeated": defeated})
        if att_unit is not None and tgt_unit is not None and id(tgt_unit) in lost_ids:
            effects.fire(self, "on_own_unit_defeats_exposed", a, {"defeated": defeated})
        if cb.ready_interceptor_after and cb.interceptor is not None:
            u = self.unit(d, cb.interceptor)
            if u:
                u.exposed = False
        self.combat = None
        self.phase = "main"
        self.state_checks()

    def describe(self, q, ref):
        if ref == "L":
            return LEADERS[self.p[q].leader].name.split(",")[0]
        u = self.unit(q, ref)
        return CARDS[u.cid].name if u else str(ref)


def default_mulligan(state, q):
    """Bottom up to 3 cards costing 5 or more (simple fixed policy)."""
    return [i for i, c in enumerate(state.p[q].hand) if CARDS[c].cost >= 5]


def new_game(leader1, deck1, leader2, deck2, rules=DEFAULT, seed=None, log=False, mulligan=None):
    s = GameState(rules)
    if log:
        s.log = []
    return s.setup(leader1, deck1, leader2, deck2, seed=seed, mulligan=mulligan)
