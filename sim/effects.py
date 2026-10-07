"""Interpreter for the card effect language (see sim/README.md).

A card or Leader side carries a list of abilities. Each ability is one of:
  {"trigger": EVENT, "if": [COND...], "once_per_turn": bool, "do": [OP...]}
  {"static": "power" | "guard_max", "if": [COND...], "applies_to": SELECTOR, "value": N}
  {"modifier": NAME, "value": N}                       (Leader rule tweaks)
  {"activated": true, "exhaust": bool, "cost": N, "target": SELECTOR, "do": [OP...]}
  {"reaction": true, "guard_cost": N, "do": [OP...]}  (Leader reaction ability)
Tactics carry "play": {"target": SELECTOR, "costs": [...], "do": [OP...]}.
Reactions carry "react": {"do": [...], "do_from_scars": [...]}.

Numbers may be written as "@param" or "-@param" to read a value from the rule config.
"""
from .cards import CARDS, LEADERS

# Events fired only on the card that caused them (the "self" of the ability).
SELF_EVENTS = {"on_enter", "on_attack", "on_intercept", "on_defeats_attacker"}


def num(s, v):
    if isinstance(v, str):
        neg = v.startswith("-")
        name = v.lstrip("-@")
        v = getattr(s.r, name)
        return -v if neg else v
    return v


# --------------------------------------------------------------------- conditions
def cond_ok(s, owner, conds, ctx):
    for c in conds or ():
        (k, v), = c.items()
        if k == "furia" and s.furia_count(owner) < v:
            return False
        if k == "scars_ge" and len(s.p[owner].scars) < v:
            return False
        if k == "infusion_count" and ctx.get("count") != v:
            return False
        if k == "awakened" and s.p[owner].awakened != v:
            return False
    return True


# --------------------------------------------------------------------- selectors
def matches(s, owner_of_unit, u, sel):
    c = CARDS[u.cid]
    if "cost_le" in sel and c.cost > sel["cost_le"]:
        return False
    if "exposed" in sel and u.exposed != sel["exposed"]:
        return False
    if "power_le" in sel and s.unit_power(owner_of_unit, u) > sel["power_le"]:
        return False
    if "inf_ge" in sel and u.inf < sel["inf_ge"]:
        return False
    if "keyword" in sel and not c.has(sel["keyword"]):
        return False
    return True


def select(s, owner, sel):
    side = owner if sel.get("side", "own") == "own" else 1 - owner
    return [u.uid for u in s.p[side].units if matches(s, side, u, sel)]


# --------------------------------------------------------------------- abilities lookup
def leader_abilities(s, q):
    pl = s.p[q]
    return LEADERS[pl.leader].side(pl.awakened)


def leader_modifier(s, q, name, default=None):
    for ab in leader_abilities(s, q):
        if ab.get("modifier") == name:
            return ab.get("value", True)
    return default


def static_power(s, owner, u):
    """Sum of static power bonuses applying to unit u (its own + Leader/relic auras)."""
    bonus = 0
    c = CARDS[u.cid]
    for ab in c.abilities:
        if ab.get("static") == "power" and "applies_to" not in ab and cond_ok(s, owner, ab.get("if"), {}):
            bonus += num(s, ab["value"])
    sources = list(leader_abilities(s, owner))
    for rid in s.p[owner].relics:
        sources += CARDS[rid].abilities
    for ou in s.p[owner].units:
        sources += [ab for ab in CARDS[ou.cid].abilities if "applies_to" in ab]
    for ab in sources:
        if ab.get("static") == "power" and "applies_to" in ab:
            sel = ab["applies_to"]
            if sel.get("side", "own") == "own" and matches(s, owner, u, sel) and cond_ok(s, owner, ab.get("if"), {}):
                bonus += num(s, ab["value"])
    return bonus


def static_total(s, owner, stat):
    """Static bonuses to a player-level stat (e.g. guard_max) from Leader and relics."""
    total = 0
    sources = list(leader_abilities(s, owner))
    for rid in s.p[owner].relics:
        sources += CARDS[rid].abilities
    for ab in sources:
        if ab.get("static") == stat and cond_ok(s, owner, ab.get("if"), {}):
            total += num(s, ab["value"])
    return total


# --------------------------------------------------------------------- triggers
def fire(s, event, owner, ctx):
    """Fire `event` for player `owner`. ctx may hold: self (uid), infused, count,
    defeated (list of (owner, Unit)) for look-back triggers."""
    if s.over:
        return
    pl = s.p[owner]
    if event in SELF_EVENTS:
        uid = ctx.get("self")
        u = s.unit(owner, uid) or ctx.get("self_unit")
        if u is None:
            return
        _run_triggers(s, owner, CARDS[u.cid].abilities, event, dict(ctx, self=u.uid))
        return
    if event == "on_infuse":
        who = ctx["infused"]
        if who != "L":
            u = s.unit(owner, who)
            _run_triggers(s, owner, CARDS[u.cid].abilities, event, dict(ctx, self=who))
        _run_triggers(s, owner, leader_abilities(s, owner), event, dict(ctx, self="L"))
        return
    # global listeners: every unit of the owner (plus look-back defeated units), Leader, relics
    units = list(pl.units) + [u for o, u in ctx.get("defeated", ()) if o == owner]
    for u in units:
        _run_triggers(s, owner, CARDS[u.cid].abilities, event, dict(ctx, self=u.uid), key=u.cid)
    _run_triggers(s, owner, leader_abilities(s, owner), event, dict(ctx, self="L"), key="leader")
    for rid in pl.relics:
        _run_triggers(s, owner, CARDS[rid].abilities, event, ctx, key=rid)


def _run_triggers(s, owner, abilities, event, ctx, key=None):
    for i, ab in enumerate(abilities):
        if ab.get("trigger") != event:
            continue
        if not cond_ok(s, owner, ab.get("if"), ctx):
            continue
        if ab.get("once_per_turn"):
            # once per turn per printed card (key identifies the source card)
            tag = (event, key)
            if tag in s.p[owner].once_flags:
                continue
            s.p[owner].once_flags.add(tag)
        run_ops(s, owner, ab["do"], ctx)


# --------------------------------------------------------------------- operations
def _target(s, owner, ref, ctx):
    """Resolve a target reference to (owner, uid_or_L)."""
    if ref in ("self", "infused"):
        return owner, ctx["self"] if ref == "self" else ctx["infused"]
    if ref == "chosen":
        return ctx["chosen_owner"], ctx["chosen"]
    raise ValueError(ref)


def run_ops(s, owner, ops, ctx):
    for op in ops:
        if s.over:
            return
        kind = op["op"]
        n = num(s, op.get("n", 0))
        if kind == "draw":
            s.draw(owner, n)
        elif kind == "gain_guard":
            s.p[owner].guard = min(s.p[owner].guard + n, s.guard_max(owner))
        elif kind in ("temp_power", "perm_power"):
            q, ref = _target(s, owner, op.get("target", "self"), ctx)
            if ref == "L":
                if kind == "temp_power":
                    s.p[q].l_temp += n
            else:
                u = s.unit(q, ref)
                if u:
                    if kind == "temp_power":
                        u.temp += n
                    else:
                        u.perm += n
        elif kind == "expose":
            q, ref = _target(s, owner, op["target"], ctx)
            u = s.unit(q, ref)
            if u:
                u.exposed = True
        elif kind == "defeat":
            q, ref = _target(s, owner, op["target"], ctx)
            u = s.unit(q, ref)
            if u:
                s.p[q].units.remove(u)
                s.p[q].discard.append(u.cid)
        elif kind == "give_renew":
            q, ref = _target(s, owner, op["target"], ctx)
            u = s.unit(q, ref)
            if u:
                u.renew = True
        elif kind == "att_mod":
            s.combat.att_mod += n
        elif kind == "def_mod":
            s.combat.def_mod += n
        elif kind == "after_combat_ready_interceptor":
            s.combat.ready_interceptor_after = True
        elif kind == "steal_infusion":
            me = s.unit(owner, ctx["self"])
            donors = [v for v in s.p[owner].units if v.uid != me.uid and v.inf > 0]
            if donors:
                v = max(donors, key=lambda x: x.inf)
                me.inf += v.inf
                me.temp += v.inf
                v.temp -= v.inf
                v.inf = 0
        else:
            raise ValueError(f"operazione sconosciuta: {kind}")


def pay_costs(s, owner, costs, check_only=False):
    for c in costs or ():
        if "lose_life" in c:
            if not s.can_pay_life(owner, c["lose_life"], c.get("floor", 0)):
                return False
    if check_only:
        return True
    for c in costs or ():
        if "lose_life" in c:
            s.lose_life(owner, c["lose_life"], "costo")
    return True
