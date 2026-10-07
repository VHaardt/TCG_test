"""Players for the v0.2 core.

The pugno is a small simultaneous zero-sum game. Every agent solves it the same way
(esperimento.md §3): a matrix M[a][(d, r)] of the attacker's value for each pair of
pugno contents, each cell = evaluate() of the state after the combat + a shadow price
`lam` for every gem left unspent, solved by regret matching. The mixed move is sampled
from the agent's own random source, separate from the game seed, so arms stay paired.

  RuleAgent2("semplice")  heuristics in the main phase, equilibrium pugno
  RuleAgent2(det=True)    same, but pure maxmin pugno (control for the exploitability test)
  BestResponseAgent       knows the opponent's pugno distribution and best-responds
  MCTSAgent2("forte")     ISMCTS in the main phase and for oppositions, equilibrium pugno
"""
import math
import random

import numpy as np

from .engine import CARDS

LAMBDA = 0.03


# ---------------------------------------------------------------------------- evaluation
def raw_eval(s, q):
    me, op = s.p[q], s.p[1 - q]
    late = s.r.raddrizzo == "fine"

    def side(p, who):
        v = 1.6 * len(p.life)
        if not p.life:
            v -= 2.5
        v += 0.25 * min(len(p.hand), 7)
        v += 0.12 * sum(1 for _, f in p.scars if not f) + 0.04 * len(p.scars)
        for u in p.units:
            v += 0.35 + 0.18 * s.unit_power(who, u)
            if u.ready or not late:
                v += 0.1
        v += 0.5 if p.awakened else 0
        return v
    return side(me, q) - side(op, 1 - q)


def evaluate(s, q):
    """Win estimate in [0, 1] for player q (gems excluded: they are priced by lam)."""
    if s.over:
        if s.winner is None:
            return 0.5
        return 1.0 if s.winner == q else 0.0
    return 1 / (1 + math.exp(-raw_eval(s, q) / 3.0))


# ---------------------------------------------------------------------------- the pugno game
def regret_matching(M, iters=300):
    """Zero-sum matrix game: row player maximises M, column player minimises.
    Saddle points are returned directly; otherwise regret matching+ with linear
    averaging (converges much faster than plain regret matching). Average strategies."""
    n, m = M.shape
    row_min = M.min(axis=1)
    col_max = M.max(axis=0)
    i, j = int(np.argmax(row_min)), int(np.argmin(col_max))
    if row_min[i] >= col_max[j] - 1e-12:
        x = np.zeros(n); y = np.zeros(m)
        x[i] = 1; y[j] = 1
        return x, y
    rx = np.zeros(n); ry = np.zeros(m)
    sx = np.zeros(n); sy = np.zeros(m)
    x = np.full(n, 1.0 / n); y = np.full(m, 1.0 / m)
    for t in range(1, iters + 1):
        u_rows = M @ y
        rx = np.maximum(rx + u_rows - x @ u_rows, 0)
        tx = rx.sum()
        x = rx / tx if tx > 0 else np.full(n, 1.0 / n)
        u_cols = x @ M
        ry = np.maximum(ry + (u_cols @ y) - u_cols, 0)
        ty = ry.sum()
        y = ry / ty if ty > 0 else np.full(m, 1.0 / m)
        sx += t * x; sy += t * y
    return sx / sx.sum(), sy / sy.sum()


class PugnoGame:
    """Builds the payoff matrix for the current combat from attacker a's point of view."""

    def __init__(self, s, lam=LAMBDA, defender_hand=None, opposer="current"):
        self.s = s
        self.lam = lam
        self.a, self.d = s.active, 1 - s.active
        self.cache = {}
        self.base = s
        if defender_hand is not None:            # determinization seen by the attacker
            self.base = s.clone()
            self.base.p[self.d].hand = list(defender_hand)
        self.opposer = s.combat.opposer if opposer == "current" else opposer
        st = self.base
        self.B = st.p[self.a].brace
        self.G = st.p[self.d].guard
        self.rows = list(range(self.B + 1))
        self.cols = [act for act in st._parry_options(self.d)]   # ("parry", k, react)
        self.opp_choices = [None] + [u.uid for u in st.p[self.d].units if u.ready]

    def _value_outcome(self, a_gems, d_gems, react, opposer):
        st = self.base
        fa, db, _ = st.compute(a_gems, d_gems, react, opposer)
        hit, ad, od = st.outcome(fa, db, opposer)
        used = react if (react is not None and d_gems >= max(CARDS[react[0]].cost, 1)) else None
        key = (hit, ad, od, used, opposer)
        v = self.cache.get(key)
        if v is None:
            c = st.clone()
            cb = c.combat
            if opposer is not None and cb.opposer is None:
                c._oppose(opposer)
            cb.a, cb.d, cb.react = a_gems, d_gems, react
            c.p[self.a].brace = max(c.p[self.a].brace, a_gems)
            c.p[self.d].guard = max(c.p[self.d].guard, d_gems)
            c._open_and_resolve()
            v = evaluate(c, self.a)
            self.cache[key] = v
        return v

    def cell(self, a_gems, col, opposer_mode):
        _, d_gems, react = col
        gems = self.lam * (self.B - a_gems) - self.lam * (self.G - d_gems)
        if opposer_mode == "after":
            best = None
            for o in self.opp_choices:
                v = self._value_outcome(a_gems, d_gems, react, o) + (0.01 if o is not None else 0)
                best = v if best is None else min(best, v)
            return best + gems
        return self._value_outcome(a_gems, d_gems, react, self.opposer) + gems

    def matrix(self, opposer_mode="fixed"):
        M = np.empty((len(self.rows), len(self.cols)))
        for i, a_gems in enumerate(self.rows):
            for j, col in enumerate(self.cols):
                M[i, j] = self.cell(a_gems, col, opposer_mode)
        return M


def _opposer_mode(s):
    return "after" if (s.r.opposizione == "dopo" and s.combat.opposer is None and s.phase in ("pugno_att", "pugno_def")) \
        else "fixed"


# ---------------------------------------------------------------------------- determinization
def unseen_for(s, q):
    """Cards of player 1-q that q cannot see: hand + deck + Vita, as one pool."""
    op = s.p[1 - q]
    return op.hand + op.deck + op.life


def sample_hand(s, q, rng):
    pool = unseen_for(s, q)
    n = len(s.p[1 - q].hand)
    return rng.sample(pool, n) if n <= len(pool) else list(pool)


def determinize(s, q, rng):
    c = s.clone()
    op = c.p[1 - q]
    pool = op.hand + op.deck + op.life
    rng.shuffle(pool)
    nh, nl = len(op.hand), len(op.life)
    op.hand, op.life, op.deck = pool[:nh], pool[nh:nh + nl], pool[nh + nl:]
    me = c.p[q]
    pool = me.deck + me.life
    rng.shuffle(pool)
    me.life, me.deck = pool[:len(me.life)], pool[len(me.life):]
    if c.combat is not None and c.phase == "pugno_def" and not c.combat.a_visible and q == c.active:
        pass
    return c


# ---------------------------------------------------------------------------- agents
class RuleAgent2:
    name = "semplice"

    def __init__(self, seed=None, lam=LAMBDA, iters=300, k_det=4, det=False):
        self.rng = random.Random((seed or 0) * 7919 + 17)     # separate from the game seed
        self.lam = lam
        self.iters = iters
        self.k_det = k_det
        self.det = det

    # ------------------------------------------------ pugno decisions
    def attacker_strategy(self, s):
        """Mixed strategy over 0..B gems for the attacker (determinized over the defender's hand)."""
        mode = _opposer_mode(s)
        acc = None
        for _ in range(max(1, self.k_det)):
            g = PugnoGame(s, self.lam, defender_hand=sample_hand(s, s.active, self.rng))
            M = g.matrix(mode)
            if self.det or s.r.pugno != "simultaneo":
                x = np.zeros(M.shape[0]); x[int(np.argmax(M.min(axis=1)))] = 1
            else:
                x, _ = regret_matching(M, self.iters)
            acc = x if acc is None else acc + x
        return acc / acc.sum()

    def defender_strategy(self, s, a_seen=None):
        mode = _opposer_mode(s)
        g = PugnoGame(s, self.lam)
        M = g.matrix(mode)
        if a_seen is not None:
            y = np.zeros(M.shape[1]); y[int(np.argmin(M[a_seen]))] = 1
            return g.cols, y
        if self.det:
            y = np.zeros(M.shape[1]); y[int(np.argmin(M.max(axis=0)))] = 1
            return g.cols, y
        _, y = regret_matching(M, self.iters)
        return g.cols, y

    def _sample(self, probs):
        r = self.rng.random()
        acc = 0.0
        for i, p in enumerate(probs):
            acc += p
            if r <= acc:
                return i
        return len(probs) - 1

    def game_value(self, s, opposer):
        """Attacker's value of the pugno game if `opposer` is chosen now (defender's view)."""
        g = PugnoGame(s, self.lam, opposer=opposer)
        M = g.matrix("fixed")
        if s.r.pugno == "simultaneo" and not self.det:
            x, y = regret_matching(M, max(100, self.iters // 3))
            return float(x @ M @ y)
        return float(M.min(axis=1).max())

    def act(self, s):
        acts = s.legal_actions()
        if len(acts) == 1:
            return acts[0]
        ph = s.phase
        if ph == "pugno_att":
            x = self.attacker_strategy(s)
            return ("gems", self._sample(x))
        if ph == "pugno_def":
            seen = s.combat.a if s.combat.a_visible else None
            cols, y = self.defender_strategy(s, seen)
            return cols[self._sample(y)]
        if ph == "oppose":
            best, best_v = ("no_oppose",), self.game_value(s, None)
            for act in acts[1:]:
                u = s.unit(1 - s.active, act[1])
                v = self.game_value(s, act[1]) + (0.01 if not CARDS[u.cid].has("scudo") else 0)
                if v < best_v:
                    best, best_v = act, v
            return best
        if ph == "oppose_after":
            g = PugnoGame(s, self.lam, opposer=None)
            cb = s.combat
            best, best_v = ("no_oppose",), g._value_outcome(cb.a, cb.d, cb.react, None)
            for act in acts[1:]:
                v = g._value_outcome(cb.a, cb.d, cb.react, act[1]) + 0.01
                if v < best_v:
                    best, best_v = act, v
            return best
        if ph == "impeto":
            return ("gems", self._impeto(s))
        if ph == "risposta":
            return self._risposta(s, acts)
        return self._main(s, acts)

    # ------------------------------------------------ V2 control: face-up single answer
    def _risposta_values(self, s, a_gems):
        out = []
        g = PugnoGame(s, self.lam, opposer=None)
        for act in s.legal_actions() if s.phase == "risposta" else [("parry", 0, None)] + \
                [("oppose", u.uid) for u in s.p[1 - s.active].units if u.ready] + s._parry_options(1 - s.active)[1:]:
            if act[0] == "oppose":
                v = g._value_outcome(a_gems, 0, None, act[1]) + g.lam * (g.B - a_gems) - g.lam * g.G + 0.01
            else:
                v = g.cell(a_gems, act, "fixed")
            out.append((v, act))
        return out

    def _impeto(self, s):
        best, best_v = 0, None
        hand = sample_hand(s, s.active, self.rng)
        c = s.clone()
        c.p[1 - s.active].hand = hand
        for a_gems in range(s.p[s.active].brace + 1):
            v = min(x for x, _ in self._risposta_values(c, a_gems))
            if best_v is None or v > best_v:
                best, best_v = a_gems, v
        return best

    def _risposta(self, s, acts):
        return min(self._risposta_values(s, s.combat.a), key=lambda t: t[0])[1]

    # ------------------------------------------------ main phase heuristics
    def _main(self, s, acts):
        a = s.active
        pl, op = s.p[a], s.p[1 - a]
        by_kind = {}
        for act in acts:
            by_kind.setdefault(act[0], []).append(act)
        reserve = 0 if s.round <= 2 else 1
        # 1. leader / unit abilities with a target
        for act in by_kind.get("ability", []):
            if act[3] is not None:
                return act
        # 2. cards: most expensive first, keeping a small reserve for the pugno
        plays = []
        for act in by_kind.get("play", []):
            c = CARDS[act[1]]
            if c.type == "tactic":
                if not self._tactic_ok(s, act):
                    continue
            if pl.brace - c.cost < reserve and c.cost > 1:
                continue
            plays.append((c.cost, self._target_score(s, act), act))
        if plays:
            plays.sort(key=lambda t: (t[0], t[1]), reverse=True)
            return plays[0][2]
        # 3. attacks: units first, then the Leader
        attacks = by_kind.get("attack", [])
        units = [act for act in attacks if act[1] != "L"]
        units.sort(key=lambda act: -s.unit_power(a, s.unit(a, act[1])))
        for act in units:
            # attack only with a credible threat: an attacker that cannot reach Tempra stays home to oppose
            pw = s.unit_power(a, s.unit(a, act[1]))
            if pw + pl.brace >= s.r.tempra + 2 * min(op.guard, 1) or (s.alle_corde(1 - a) and pw + pl.brace >= s.r.tempra):
                return act
        rim = by_kind.get("rim", [])
        lead = [act for act in attacks if act[1] == "L"]
        if lead:
            threat = s.leader_power(a) + pl.brace >= s.r.tempra + 2 * op.guard - 1
            if threat or s.alle_corde(1 - a) or not rim or len(pl.life) >= 4:
                return lead[0]
        if rim and len(pl.life) >= 1:
            rim.sort(key=lambda act: (CARDS[act[1]].type == "reaction", CARDS[act[1]].cost), reverse=True)
            return rim[0]
        return ("end",)

    def _tactic_ok(self, s, act):
        c = CARDS[act[1]]
        a = s.active
        if any("lose_life" in x for x in (c.play or {}).get("costs", []) or ()):
            return len(s.p[a].hand) <= 3 and len(s.p[a].life) >= 3
        if act[2] is None:
            return True
        side = a if (c.play or {}).get("target", {}).get("side", "own") == "own" else 1 - a
        u = s.unit(side, act[2])
        return u is not None and s.unit_power(side, u) >= 2

    def _target_score(self, s, act):
        if act[2] is None:
            return 0
        c = CARDS[act[1]]
        side = s.active if (c.play or {}).get("target", {}).get("side", "own") == "own" else 1 - s.active
        u = s.unit(side, act[2])
        return s.unit_power(side, u) if u else 0


class BestResponseAgent(RuleAgent2):
    """Exploitability probe: knows the opponent's pugno distribution (computed on the true
    state) and plays the pure best response to it. opponent='eq' or 'det'."""
    name = "br"

    def __init__(self, seed=None, lam=LAMBDA, opponent="eq", **kw):
        super().__init__(seed, lam, **kw)
        self.opponent = opponent

    def act(self, s):
        if s.phase == "pugno_att" and s.r.pugno == "simultaneo":
            g = PugnoGame(s, self.lam)
            M = g.matrix(_opposer_mode(s))
            if self.opponent == "det":
                y = np.zeros(M.shape[1]); y[int(np.argmin(M.max(axis=0)))] = 1
            else:
                _, y = regret_matching(M, self.iters)
            return ("gems", int(np.argmax(M @ y)))
        if s.phase == "pugno_def" and s.r.pugno == "simultaneo":
            g = PugnoGame(s, self.lam)
            M = g.matrix(_opposer_mode(s))
            if self.opponent == "det":
                x = np.zeros(M.shape[0]); x[int(np.argmax(M.min(axis=1)))] = 1
            else:
                x, _ = regret_matching(M, self.iters)
            return g.cols[int(np.argmin(x @ M))]
        return super().act(s)


class MCTSAgent2:
    """IA forte: determinized UCT over main-phase and opposition decisions; pugno nodes are
    played with the equilibrium strategy (never by peeking at the hidden pugno)."""
    name = "forte"

    def __init__(self, iterations=100, c=0.9, seed=None, lam=LAMBDA):
        self.iterations = iterations
        self.c = c
        self.rng = random.Random((seed or 0) * 104729 + 3)
        self.base = RuleAgent2(seed=seed, lam=lam)
        self.fast = RuleAgent2(seed=(seed or 0) + 99991, lam=lam, iters=150, k_det=1)

    def act(self, s):
        acts = s.legal_actions()
        if len(acts) == 1:
            return acts[0]
        if s.phase not in ("main", "oppose", "oppose_after"):
            return self.base.act(s)
        me = s.decider()
        stats = {a: [0, 0.0] for a in acts}
        for it in range(self.iterations):
            total = sum(n for n, _ in stats.values()) + 1
            act = max(acts, key=lambda a: (stats[a][1] / stats[a][0] + self.c * math.sqrt(math.log(total) / stats[a][0]))
                      if stats[a][0] else float("inf"))
            c = determinize(s, me, self.rng)
            c.step(act)
            steps = 0
            while not c.over and steps < 400:
                c.step(self.fast.act(c))
                steps += 1
            v = evaluate(c, me)
            stats[act][0] += 1
            stats[act][1] += v
        return max(acts, key=lambda a: stats[a][0])


def make_agent(spec, seed=None):
    """'semplice', 'semplice@0.08' (lam), 'det', 'br', 'br:det', 'forte', 'forte:200'."""
    name, _, rest = spec.partition(":")
    name, _, lam = name.partition("@")
    lam = float(lam) if lam else LAMBDA
    if name == "semplice":
        return RuleAgent2(seed=seed, lam=lam)
    if name == "det":
        return RuleAgent2(seed=seed, lam=lam, det=True)
    if name == "br":
        return BestResponseAgent(seed=seed, lam=lam, opponent=rest or "eq")
    if name == "forte":
        return MCTSAgent2(iterations=int(rest) if rest else 100, seed=seed, lam=lam)
    raise ValueError(spec)
