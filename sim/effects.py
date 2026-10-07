"""Interpreter for the card effect language (see sim/README.md).

A card or Leader side carries a list of abilities. Each ability is one of:
  {"trigger": EVENT, "if": [COND...], "once_per_turn": bool, "do": [OP...]}
  {"static": "power" | "guard_max", "if": [COND...], "applies_to": SELECTOR, "value": N}
  {"modifier": NAME, "value": N}                       (Leader rule tweaks)
  {"activated": true, "exhaust": bool, "cost": N, "target": SELECTOR, "do": [OP...]}
  {"reaction": true, "guard_cost": N, "do": [OP...]}  (Leader reaction ability)
Tactics carry "play": {"target": SELECTOR, "costs": [...], "do": [OP...]}.
Reactions carry "react": {"do": [...], "do_from_scars": [...]}.

Numbers may be written as "@name" or "-@name". Dynamic names are read from the game
(DYNAMIC below, from the point of view of the card's owner), "@n" reads the number
carried by the event (e.g. Guardia scartata), anything else reads the rule config.
"""
from .cards import CARDS, LEADERS

# Events fired only on the card that caused them (the "self" of the ability).
SELF_EVENTS = {"on_enter", "on_attack", "on_intercept", "on_intercepted", "on_defeats_attacker"}

# "@name" values computed from the game state, seen by player q
DYNAMIC = {
    "scars": lambda s, q: len(s.p[q].scars),
    "opp_scars": lambda s, q: len(s.p[1 - q].scars),
    "life": lambda s, q: len(s.p[q].life),
    "opp_life": lambda s, q: len(s.p[1 - q].life),
    "hand": lambda s, q: len(s.p[q].hand),
    "guard": lambda s, q: s.p[q].guard,
}


def num(s, v, owner=None, ctx=None):
    if isinstance(v, str):
        neg = v.startswith("-")
        name = v.lstrip("-@")
        if name in DYNAMIC:
            if owner is None:
                raise ValueError(f"@{name} richiede il proprietario della carta")
            v = DYNAMIC[name](s, owner)
        elif name == "n":
            v = (ctx or {}).get("n", 0)
        else:
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
        if k == "is_second_player" and (owner == 1) != v:
            return False
        if k == "life_behind_ge" and len(s.p[1 - owner].life) - len(s.p[owner].life) < num(s, v, owner, ctx):
            return False
        if k == "life_le" and len(s.p[owner].life) > num(s, v, owner, ctx):
            return False
    return True


# --------------------------------------------------------------------- selectors
def matches(s, owner_of_unit, u, sel, chooser=None):
    """chooser: the player whose card does the selecting (for "@scars" etc.);
    defaults to the unit's owner for auras on own units."""
    c = CARDS[u.cid]
    q = owner_of_unit if chooser is None else chooser
    if "cost_le" in sel and c.cost > num(s, sel["cost_le"], q):
        return False
    if "exposed" in sel and u.exposed != sel["exposed"]:
        return False
    if "power_le" in sel and s.unit_power(owner_of_unit, u) > num(s, sel["power_le"], q):
        return False
    if "inf_ge" in sel and u.inf < sel["inf_ge"]:
        return False
    if "keyword" in sel and not c.has(sel["keyword"]):
        return False
    return True


def select(s, owner, sel):
    side = owner if sel.get("side", "own") == "own" else 1 - owner
    return [u.uid for u in s.p[side].units if matches(s, side, u, sel, chooser=owner)]


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
            bonus += num(s, ab["value"], owner)
    sources = list(leader_abilities(s, owner))
    for rid in s.p[owner].relics:
        sources += CARDS[rid].abilities
    for ou in s.p[owner].units:
        sources += [ab for ab in CARDS[ou.cid].abilities if "applies_to" in ab]
    for ab in sources:
        if ab.get("static") == "power" and "applies_to" in ab:
            sel = ab["applies_to"]
            if sel.get("side", "own") == "own" and matches(s, owner, u, sel) and cond_ok(s, owner, ab.get("if"), {}):
                bonus += num(s, ab["value"], owner)
    return bonus


def static_total(s, owner, stat):
    """Static bonuses to a player-level stat (e.g. guard_max) from Leader, relics and units.
    Returns (total, cap): cap is the lowest "cap" among the applying abilities, or None
    ({"static": "guard_max", "value": 1, "cap": 4} = +1, but never above 4)."""
    total, cap = 0, None
    sources = list(leader_abilities(s, owner))
    for rid in s.p[owner].relics:
        sources += CARDS[rid].abilities
    for u in s.p[owner].units:
        sources += CARDS[u.cid].abilities
    for ab in sources:
        if ab.get("static") == stat and cond_ok(s, owner, ab.get("if"), {}):
            total += num(s, ab["value"], owner)
            if "cap" in ab:
                c = num(s, ab["cap"], owner)
                cap = c if cap is None else min(cap, c)
    return total, cap


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
        n = num(s, op.get("n", 0), owner, ctx)
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
        elif kind == "unblockable":
            # the target cannot be intercepted until end of turn (R-002 #3)
            q, ref = _target(s, owner, op.get("target", "self"), ctx)
            s.p[q].set_flag(("unblockable", ref))
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
    """Extra costs ({"lose_life": N, "floor": F}): legal only if the player keeps at least
    F Vite and the Saldo allows it; the lost Vite count in the Saldo."""
    for c in costs or ():
        if "lose_life" in c:
            if not s.can_pay_life(owner, num(s, c["lose_life"], owner), num(s, c.get("floor", 0), owner)):
                return False
    if check_only:
        return True
    for c in costs or ():
        if "lose_life" in c:
            s.lose_life(owner, num(s, c["lose_life"], owner), "costo")
    return True


def card_costs(c, spec=None):
    """All extra costs of a card: top-level "costs" plus those of its play/react spec."""
    return list(c.costs) + list((spec or {}).get("costs") or ())
