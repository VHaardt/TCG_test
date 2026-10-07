"""Players for the simulator.

  RandomAgent  - uniform over legal actions (sanity checks only)
  RuleAgent    - "IA semplice": fast hand-written priorities, also the rollout policy
  MCTSAgent    - "IA forte": information-set Monte Carlo tree search (determinized,
                 rollouts with RuleAgent, evaluation cut-off)
Every agent implements `act(state) -> action` for the player `state.decider()`.
They only read public information plus their own hand (MCTS re-samples the rest)."""
import math
import random

from .cards import CARDS


class RandomAgent:
    name = "random"

    def __init__(self, seed=None):
        self.rng = random.Random(seed)

    def act(self, s):
        return self.rng.choice(s.legal_actions())


# ---------------------------------------------------------------------------- heuristics
def evaluate(s, q):
    """Static evaluation in [0, 1] from player q's point of view."""
    if s.over:
        if s.winner is None:
            return 0.5
        return 1.0 if s.winner == q else 0.0
    me, op = s.p[q], s.p[1 - q]

    def side(p, who):
        v = 0.0
        v += 1.6 * len(p.life)
        if not p.life:
            v -= 2.5
        v += 0.25 * min(len(p.hand), 7)
        v += 0.12 * len(p.scars)
        for u in p.units:
            v += 0.35 + 0.18 * s.unit_power(who, u)
        v += 0.3 * p.guard
        v += 0.1 * p.furnace
        v += 0.5 if p.awakened else 0
        return v
    x = side(me, q) - side(op, 1 - q)
    return 1 / (1 + math.exp(-x / 3.0))


def _parry_cap(s, q):
    return s.p[q].guard * s.parry_per_guard(q)


class RuleAgent:
    """Hand-written policy. Deliberately simple: it is the baseline the strong AI must
    beat (pillar target >= 65%) and the fast rollout policy of MCTS."""
    name = "semplice"

    def __init__(self, seed=None, noise=0.0):
        self.rng = random.Random(seed)
        self.noise = noise

    def act(self, s):
        acts = s.legal_actions()
        if len(acts) == 1:
            return acts[0]
        if self.noise and self.rng.random() < self.noise:
            return self.rng.choice(acts)
        if s.phase == "intercept":
            return self._intercept(s, acts)
        if s.phase == "react":
            return self._react(s, acts)
        return self._main(s, acts)

    # -------------------------------------------------- defender
    def _intercept(self, s, acts):
        a, d = s.active, 1 - s.active
        cb = s.combat
        fa = s.att_power()
        threat = cb.tgt == "L" and (fa > s.tempra(d) if s.r.leader_hit_strict else fa >= s.tempra(d))
        best, best_score = ("no_intercept",), 0.0
        for act in acts[1:]:
            u = s.unit(d, act[1])
            pw = s.unit_power(d, u)
            score = 0.0
            if pw > fa:
                score = 3.0                       # kills the attacker, survives
            elif pw == fa:
                score = 1.5
            if threat:
                guard_stops = fa < s.tempra(d) + _parry_cap(s, d)
                if s.snapshot or len(s.p[d].life) <= 1:
                    score += 5.0                  # must not take the hit
                elif not guard_stops:
                    score += 1.0 + 0.5 * (len(s.p[d].life) <= 2)
                score -= CARDS[u.cid].cost * 0.2
            elif cb.tgt != "L":
                score += 0.5 if pw >= fa else 0
            if score > best_score:
                best, best_score = act, score
        return best

    def _react(self, s, acts):
        a, d = s.active, 1 - s.active
        cb = s.combat
        fa, db = s.att_power(), s.def_value()
        if cb.tgt == "L":
            hit = fa > db if s.r.leader_hit_strict else fa >= db
            if not hit:
                return ("no_react",)
            gap = fa - db + (0 if s.r.leader_hit_strict else 1)
            lethal = s.snapshot
            options = []
            for act in acts[1:]:
                stop, cost = self._react_value(s, d, act)
                if stop >= gap:
                    options.append((cost, act))
            if options:
                options.sort(key=lambda x: x[0])
                return options[0][1]
            return ("no_react",)
        # attack on a unit: save it if cheap and the unit is worth it
        u = s.unit(d, cb.tgt)
        if u is None or fa < db:
            return ("no_react",)
        gap = fa - db + 1
        if CARDS[u.cid].cost < 3:
            return ("no_react",)
        options = []
        for act in acts[1:]:
            stop, cost = self._react_value(s, d, act)
            if stop >= gap and cost <= 1:
                options.append((cost, act))
        if options:
            options.sort(key=lambda x: x[0])
            return options[0][1]
        return ("no_react",)

    def _react_value(self, s, d, act):
        """(how much it shifts the fight in the defender's favour, Guard spent)."""
        kind = act[0]
        if kind == "parry":
            return s.parry_per_guard(d) * act[1], act[1]
        if kind == "reaction":
            c = CARDS[act[1]]
            ops = c.react.get("do_from_scars", c.react["do"]) if act[2] == "scar" else c.react["do"]
            v = sum(abs(_num(s, o.get("n", 0))) for o in ops if o["op"] in ("att_mod", "def_mod"))
            return v, max(c.cost, 1) - 0.1
        if kind == "leader_reaction":
            from .effects import leader_abilities
            ab = leader_abilities(s, d)[act[1]]
            v = sum(abs(_num(s, o.get("n", 0))) for o in ab["do"] if o["op"] in ("att_mod", "def_mod"))
            return v, max(ab.get("guard_cost", 1), 1) - 0.05
        return 0, 0

    # -------------------------------------------------- active player
    def _main(self, s, acts):
        a = s.active
        pl, op = s.p[a], s.p[1 - a]
        by = {}
        for act in acts:
            by.setdefault(act[0], []).append(act)
        tempra = s.tempra(1 - a) + (1 if s.r.leader_hit_strict else 0)
        exp_def = tempra + _parry_cap(s, 1 - a)
        attackers = set(s.attackers(a))

        def power_of(ref):
            return s.leader_power(a) if ref == "L" else s.unit_power(a, s.unit(a, ref))

        # 1. lethal: opponent was Alle Corde at the start of the turn
        if s.snapshot and "attack" in by:
            cands = sorted(attackers, key=lambda r: -power_of(r))
            for ref in cands:
                if power_of(ref) >= exp_def or (power_of(ref) >= tempra and op.guard == 0):
                    return ("attack", ref, "L")
            for ref in cands:
                need = exp_def - power_of(ref)
                if 0 < need <= pl.brace and ("infuse", ref) in acts:
                    return ("infuse", ref)
            if cands:
                ref = cands[0]
                need = tempra - power_of(ref)
                if 0 < need <= pl.brace and ("infuse", ref) in acts:
                    return ("infuse", ref)
                if power_of(ref) >= tempra:
                    return ("attack", ref, "L")
        # 2. Scintilla early
        if ("spark",) in acts and pl.turn_no >= 2:
            return ("spark",)
        # 3. play the most expensive useful card
        plays = by.get("play", [])
        best = None
        for act in plays:
            c = CARDS[act[1]]
            score = c.cost + (0.5 if c.type == "unit" else 0)
            if c.type == "relic":
                score = 1.0
            if act[1] == "patto" and (len(pl.life) <= 2 or len(pl.hand) > 4):
                continue
            if act[1] == "colpo":
                score += 2
            if act[1] == "esca":
                tgt = s.unit(1 - a, act[2])
                if not any(r != "L" and power_of(r) > s.unit_power(1 - a, tgt) for r in attackers):
                    continue
                score += 1.5
            if act[1] == "carica":
                score += 1
            if best is None or score > best[0]:
                best = (score, act)
        if best:
            return best[1]
        # 4. attacks with units
        unit_atts = sorted((r for r in attackers if r != "L"), key=lambda r: -power_of(r))
        exposed = [u for u in op.units if u.exposed]
        for ref in unit_atts:
            p = power_of(ref)
            u = s.unit(a, ref)
            vs_unit = [e for e in exposed
                       if s.unit_power(a, u, vs_exposed_unit=True) > s.unit_power(1 - a, e)]
            if vs_unit:
                tgt = max(vs_unit, key=lambda e: CARDS[e.cid].cost)
                return ("attack", ref, tgt.uid)
            if p >= tempra:
                return ("attack", ref, "L")
        # 5. infuse to enable a hit, keeping some Guard if threatened
        keep = min(s.guard_max(a), 2) if any(True for _ in op.units) else 0
        spare = pl.brace - keep
        for ref in unit_atts + (["L"] if "L" in attackers else []):
            need = tempra - power_of(ref)
            if 0 < need <= spare and ("infuse", ref) in acts:
                return ("infuse", ref)
        # 6. Leader attacks
        if "L" in attackers:
            lp = power_of("L")
            weak = [e for e in exposed if s.unit_power(1 - a, e) <= lp]
            if weak:
                return ("attack", "L", max(weak, key=lambda e: CARDS[e.cid].cost).uid)
            if lp >= tempra:
                return ("attack", "L", "L")
        # 7. Rimarginare when the Leader has nothing better to do
        if "rim" in by and pl.brace > 0:
            reactions = [x for x in by["rim"] if CARDS[x[1]].type != "reaction"]
            if reactions and len(pl.hand) <= 4:
                return max(reactions, key=lambda x: CARDS[x[1]].cost)
        # 8. Leader activated abilities (e.g. Thorn) if it enables an attack
        for act in by.get("leader_ability", []):
            tgt = s.unit(1 - a, act[2])
            if tgt and any(r != "L" and power_of(r) > s.unit_power(1 - a, tgt) for r in attackers):
                return act
        return ("end",)


def _num(s, v):
    from .effects import num
    return num(s, v)


# ---------------------------------------------------------------------------- MCTS
class _Node:
    __slots__ = ("parent", "action", "player", "children", "visits", "value", "avail")

    def __init__(self, parent, action, player):
        self.parent = parent
        self.action = action
        self.player = player        # player who chose `action`
        self.children = {}
        self.visits = 0
        self.value = 0.0
        self.avail = 0


def determinize(s, q, rng):
    """Re-sample everything player q cannot see: opponent hand, both decks, both Vite."""
    t = s.clone()
    t.rng = random.Random(rng.random())
    o = 1 - q
    me, op = t.p[q], t.p[o]
    pool = op.hand + op.deck + op.life
    rng.shuffle(pool)
    nh, nd = len(op.hand), len(op.deck)
    op.hand, op.deck, op.life = pool[:nh], pool[nh:nh + nd], pool[nh + nd:]
    pool = me.deck + me.life
    rng.shuffle(pool)
    nd = len(me.deck)
    me.deck, me.life = pool[:nd], pool[nd:]
    return t


class MCTSAgent:
    """Single-observer information-set MCTS. Each iteration samples a determinization,
    descends the shared tree with UCB over the actions legal in that sample, then plays
    a RuleAgent rollout for at most `horizon` turns (default: to the end of the game, which
    tested far stronger than short rollouts + `evaluate`) and scores the result."""
    name = "forte"

    def __init__(self, iterations=300, horizon=100, c=0.9, seed=None, rollout_noise=0.1):
        self.iterations = iterations
        self.horizon = horizon
        self.c = c
        self.rng = random.Random(seed)
        self.rollout = RuleAgent(seed=self.rng.random(), noise=rollout_noise)
        self.fallback = RuleAgent()

    def act(self, s):
        acts = s.legal_actions()
        if len(acts) == 1:
            return acts[0]
        me = s.decider()
        root = _Node(None, None, None)
        for _ in range(self.iterations):
            st = determinize(s, me, self.rng)
            node = root
            # selection / expansion
            while not st.over:
                legal = st.legal_actions()
                player = st.decider()
                for act in legal:
                    ch = node.children.get(act)
                    if ch is not None:
                        ch.avail += 1
                untried = [act for act in legal if act not in node.children]
                if untried:
                    act = self.rng.choice(untried)
                    ch = _Node(node, act, player)
                    ch.avail = 1
                    node.children[act] = ch
                    st.step(act)
                    node = ch
                    break
                best, best_u = None, -1e9
                for act in legal:
                    ch = node.children[act]
                    u = ch.value / ch.visits + self.c * math.sqrt(math.log(max(ch.avail, 1)) / ch.visits)
                    if u > best_u:
                        best, best_u = ch, u
                node = best
                st.step(best.action)
            # rollout
            start_turns = st.p[0].turn_no + st.p[1].turn_no
            while not st.over and st.p[0].turn_no + st.p[1].turn_no - start_turns < self.horizon:
                st.step(self.rollout.act(st))
            v = evaluate(st, me)
            # backpropagation (value stored from the chooser's point of view)
            while node is not None and node.parent is not None:
                node.visits += 1
                node.value += v if node.player == me else 1 - v
                node = node.parent
        best = max((ch for act, ch in root.children.items() if act in acts),
                   key=lambda ch: ch.visits, default=None)
        return best.action if best else self.fallback.act(s)


AGENTS = {"random": RandomAgent, "semplice": RuleAgent, "forte": MCTSAgent}


def make_agent(spec, seed=None):
    """'semplice', 'random', 'forte' or 'forte:500' (iterations)."""
    name, _, arg = spec.partition(":")
    if name == "forte":
        return MCTSAgent(iterations=int(arg) if arg else 300, seed=seed)
    return AGENTS[name](seed=seed)
