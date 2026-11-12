"""Checks of the v0.2 candidate core (sim/v02, Q-013 B0)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from sim.run import load_deck
from sim.v02.agents import RuleAgent2, regret_matching
from sim.v02.config import B0, PRESETS, rules_from
from sim.v02 import engine as E
from sim.v02.engine import Unit, new_game
from sim.cards import Card, LeaderCard


def _game(rules=B0, seed=0):
    (l1, d1), (l2, d2) = load_deck("arden_rosso_verde"), load_deck("maera_blu_nero")
    return new_game(l1, d1, l2, d2, rules=rules, seed=seed)


def _play(s, agents):
    n = 0
    while not s.over and n < 5000:
        s.step(agents[s.decider()].act(s))
        n += 1
    return s


def test_games_terminate_under_every_preset():
    for name in PRESETS:
        for seed in range(3):
            s = _play(_game(rules_from(name), seed), [RuleAgent2(seed), RuleAgent2(seed + 1)])
            assert s.end_reason in ("colpo_finale", "crepuscolo", "mazzo_vuoto"), (name, s.end_reason)
            assert s.round <= 17


def test_brace_follows_round_and_scintilla():
    s = _game()
    assert s.round == 1 and s.p[0].brace == 1
    s.step(("end",))
    assert s.p[1].brace == 1 + B0.scintilla_g2_gems
    assert s.p[0].guard == 1                     # unspent Brace became Guardia


def test_no_attack_in_round_one():
    s = _game()
    assert not any(a[0] == "attack" for a in s.legal_actions())


def test_fresh_scars_cap_and_colpo_finale():
    s = _game()
    s.round = 3
    d = s.p[1]
    assert s.lose_life(1, "test") and s.lose_life(1, "test")
    assert not s.lose_life(1, "test")            # Saldo: 2 fresh Scars
    for sc in d.scars:
        sc[1] = False
    d.life.clear()
    d.guard = 0
    s.p[0].brace = 4                             # Leader 3 + 4 gems beats Tempra 5
    s.combat = None
    s.step(("attack", "L"))
    while s.phase != "main" and not s.over:
        acts = s.legal_actions()
        if s.phase == "pugno_att":
            s.step(("gems", s.p[0].brace))
        else:
            s.step(acts[0])
    assert s.over and s.winner == 0              # Leader Alle Corde without fresh Scars: colpo finale


def test_opposer_takes_the_attack_and_scudo_does_not_rotate():
    s = _game()
    s.round = 3
    s.p[0].units.append(Unit(900, "t_r6", True))
    s.p[1].units.append(Unit(901, "sentinella", True))
    s.step(("attack", 900))
    assert s.phase == "oppose"
    s.step(("oppose", 901))
    assert s.unit(1, 901).ready                  # Scudo: opposes without rotating
    s.step(("gems", 0))
    s.step(("parry", 0, None))
    assert s.unit(1, 901) is None                # 6 vs 3+2: the opposer is defeated
    assert len(s.p[1].life) == 5                 # the Leader was not hit


def test_regret_matching_finds_matching_pennies():
    x, y = regret_matching(np.array([[1.0, 0.0], [0.0, 1.0]]), 2000)
    assert abs(x[0] - 0.5) < 0.05 and abs(y[0] - 0.5) < 0.05


# ---------------------------------------------------------------------------- R-005 primitives
def _card(cid, **kw):
    """Registers a throw-away test card in the v0.2 database."""
    c = dict(id=cid, name=cid, type="unit", cost=2, colors=("G",), power=2)
    c.update(kw)
    c["keywords"] = frozenset(c.get("keywords", ()))
    c["abilities"] = tuple(c.get("abilities", ()))
    c["costs"] = tuple(c.get("costs", ()))
    E.CARDS[cid] = Card(**c)
    return cid


def _arena(seed=0):
    """V02 game in round 3, no Units, no gems, defender's hand without Reactions."""
    s = _game(rules_from("V02"), seed)
    s.round = 3
    for pl in s.p:
        pl.units.clear()
        pl.guard = pl.brace = 0
        pl.hand = [c for c in pl.hand if E.CARDS[c].type != "reaction"]
    return s


def _fight(s, act, a_gems=0, parry=("parry", 0, None), oppose=None):
    s.step(act)
    if s.phase == "oppose":
        s.step(("oppose", oppose) if oppose else ("no_oppose",))
    s.step(("gems", a_gems))
    s.step(parry)


def test_caccia_targets_any_unit_and_opposer_must_differ():
    hunter = _card("_hunter", power=4, keywords=["caccia"])
    prey, other = _card("_prey", power=3, abilities=[{"trigger": "on_oppose", "do": [{"op": "def_mod", "n": 5}]}]), _card("_other", power=2)
    s = _arena()
    s.p[0].units = [Unit(900, hunter, True)]
    s.p[1].units = [Unit(901, prey, False), Unit(902, other, True)]
    acts = s.legal_actions()
    assert ("attack", 900, 901) in acts and ("attack", 900, 902) in acts and ("attack", 900) in acts
    s.step(("attack", 900, 901))
    assert s.legal_actions() == [("no_oppose",), ("oppose", 902)]       # the hunted Unit cannot oppose
    s.step(("no_oppose",))
    s.step(("gems", 0))
    s.step(("parry", 0, None))
    assert s.unit(1, 901) is None and len(s.p[1].life) == 5               # 4 vs 3, no on_oppose (+5)
    assert s.stats["hunt_rotated"][0] == 1 and s.stats["removals"][0] == 1 and s.stats["target_leader"][0] == 0
    # Parata defends the hunted Unit: 3 + 2 > 4, the hunter is defeated
    s = _arena()
    s.p[0].units = [Unit(900, hunter, True)]
    s.p[1].units = [Unit(901, prey, True)]
    s.p[1].guard = 1
    _fight(s, ("attack", 900, 901), parry=("parry", 1, None))
    assert s.unit(0, 900) is None and s.unit(1, 901) is not None and s.unit(1, 901).ready   # not rotated
    # opposition by another Unit: it becomes the target
    s = _arena()
    s.p[0].units = [Unit(900, hunter, True)]
    s.p[1].units = [Unit(901, prey, False), Unit(902, other, True)]
    _fight(s, ("attack", 900, 901), oppose=902)
    assert s.unit(1, 902) is None and s.unit(1, 901) is not None


def test_caccia_scudo_of_the_hunted_target_wins_ties():
    hunter = _card("_hunter", power=4, keywords=["caccia"])
    wall = _card("_wall", power=4, keywords=["scudo"])
    s = _arena()
    s.p[0].units = [Unit(900, hunter, True)]
    s.p[1].units = [Unit(901, wall, False)]
    _fight(s, ("attack", 900, 901))
    assert s.unit(0, 900) is None and s.unit(1, 901) is not None


def test_bracconiere_when_attacking_a_unit_never_when_opposing():
    poacher = _card("_poacher", power=2, keywords=["caccia", "bracconiere"], kw_params={"bracconiere": 2})
    prey, raider = _card("_prey3", power=3), _card("_raider", power=3)
    s = _arena()
    s.p[0].units = [Unit(900, poacher, True)]
    s.p[1].units = [Unit(901, prey, False)]
    _fight(s, ("attack", 900, 901))
    assert s.unit(1, 901) is None and s.unit(0, 900) is not None        # 2 + 2 > 3
    s = _arena()
    s.p[0].units = [Unit(900, raider, True)]
    s.p[1].units = [Unit(901, poacher, True)]
    _fight(s, ("attack", 900), oppose=901)
    assert s.unit(1, 901) is None                                        # opposing: no +2


def test_impeto_in_defence_counts_only_parata_and_alias():
    hunter = _card("_hunter6", power=6, keywords=["caccia"])
    ardent = _card("_ardent", power=3, keywords=["impeto"],
                   abilities=[{"static": "power", "if": [{"pugno_ge": 1}], "value": 2}])
    react = _card("_r0", type="reaction", cost=1, power=0, react={"do": [{"op": "def_mod", "n": 0}]})
    s = _arena()
    s.p[0].units = [Unit(900, hunter, True)]
    s.p[1].units = [Unit(901, ardent, False)]
    s.p[1].guard = 2
    s.p[1].hand.append(react)
    s.step(("attack", 900, 901))
    s.step(("gems", 0))
    assert s.compute(0, 1, (react, "hand"), None)[1] == 3               # the gem paid the Reaction
    assert s.compute(0, 2, (react, "hand"), None)[1] == 3 + 2 + 2       # 1 gem of Parata: Impeto on
    s.step(("parry", 2, (react, "hand")))
    assert s.unit(0, 900) is None and s.stats["double_gems"][1] == 0     # M8
    assert s.matches(1, Unit(1, ardent, True), {"keyword": "infuso"})    # old selector name


def test_infuso_keyword_is_read_as_impeto(tmp=None):
    import json
    import tempfile
    raw = {"cards": [{"id": "_old", "name": "old", "type": "unit", "cost": 1, "colors": ["R"], "power": 1,
                      "keywords": ["infuso"]}], "leaders": []}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(raw, f)
    try:
        E.load_cards(f.name)
        assert E.CARDS["_old"].has("impeto") and not E.CARDS["_old"].has("infuso")
    finally:
        E.load_cards()
        os.unlink(f.name)


def test_rinnovo_only_when_attacking_and_defeating_a_unit():
    renew = _card("_renew", power=5, cost=3, abilities=[
        {"trigger": "on_attack_defeats_unit", "do": [{"op": "raddrizza", "target": "self"}]}])
    small, hunter = _card("_small", power=2), _card("_hunter_r", power=3, keywords=["caccia"])
    s = _arena()
    s.p[0].units = [Unit(900, renew, True), Unit(902, hunter, True)]
    s.p[1].units = [Unit(901, small, True)]
    _fight(s, ("attack", 900), oppose=901)
    assert s.unit(1, 901) is None and s.unit(0, 900).ready               # defeated the opposer: straightens
    s.p[1].units = [Unit(903, small, False)]
    _fight(s, ("attack", 900))
    assert not s.unit(0, 900).ready                                      # hit the Leader: stays rotated
    # opposing and defeating the attacker: no Rinnovo
    s.p[0].units = [Unit(904, small, True)]
    s.p[1].units = [Unit(905, renew, True)]
    s.active, s.phase = 0, "main"
    _fight(s, ("attack", 904), oppose=905)
    assert s.unit(0, 904) is None and not s.unit(1, 905).ready


def _ldr06():
    E.LEADERS["_l06"] = LeaderCard(id="_l06", name="l06", colors=("K", "G"), base=(
        {"activated": True, "cost": 0, "costs": [{"lose_life": 1, "floor": 2}],
         "target": {"side": "opp", "ready": True, "power_le": {"scars": "own"}},
         "do": [{"op": "stanca", "target": "chosen"}]},), awakened=())
    return "_l06"


def test_life_cost_on_activated_and_dynamic_selector():
    s = _arena()
    s.p[0].leader = _ldr06()
    one, two = _card("_p1", power=1), _card("_p2", power=2)
    s.p[1].units = [Unit(901, one, True), Unit(902, two, True)]
    s.p[0].scars.append([s.p[0].life.pop(), False, "attacco"])            # 1 Scar, 4 Vite
    abil = [a for a in s.legal_actions() if a[0] == "ability"]
    assert abil == [("ability", "L", 0, 901)]                            # Forza <= 1 Cicatrice (counted before paying)
    s.step(abil[0])
    assert not s.unit(1, 901).ready and len(s.p[0].life) == 3 and s.p[0].fresh() == 1
    assert s.stats["life_costs"][0] == 1
    s.p[0].l_ready = True
    s.p[0].life = s.p[0].life[:2]                                        # 2 Vite: floor 2 makes it illegal
    assert not [a for a in s.legal_actions() if a[0] == "ability"]
    s.p[0].life = [s.p[0].deck.pop() for _ in range(4)]
    s.p[0].scars.append([s.p[0].deck.pop(), True, "attacco"])            # 2 fresh Scars: Saldo full
    assert not [a for a in s.legal_actions() if a[0] == "ability"]


def test_selector_any_and_if_for_conditional_thresholds():
    kill = _card("_ros013", type="tactic", cost=2, power=0, play={
        "target": {"side": "opp", "ready": False, "cost_le": 4,
                   "any": [{"power_le": 2}, {"power_le": 3, "if": [{"scars_ge": 1}]}]},
        "do": [{"op": "defeat", "target": "chosen"}]})
    three = _card("_p3", power=3)
    s = _arena()
    s.p[0].brace = 2
    s.p[0].hand.append(kill)
    s.p[1].units = [Unit(901, three, False)]
    assert not [a for a in s.legal_actions() if a[0] == "play" and a[1] == kill]
    s.p[0].scars.append([s.p[0].life.pop(), False, "attacco"])
    assert ("play", kill, 901) in s.legal_actions()
    s.step(("play", kill, 901))
    assert not s.p[1].units and s.stats["removals"][0] == 1


def test_reaction_draw_with_op_condition_and_raddrizza_opposer():
    draw = _card("_rdraw", type="reaction", cost=1, power=0, react={"do": [
        {"op": "def_mod", "n": 3}, {"op": "draw", "n": 1, "if": [{"deck_nonempty": True}]}]})
    for empty in (False, True):
        s = _arena()
        s.p[0].units = [Unit(900, _card("_a4", power=4), True)]
        s.p[1].guard = 1
        s.p[1].hand.append(draw)
        if empty:
            s.p[1].deck.clear()
        n_hand, n_life = len(s.p[1].hand), len(s.p[1].life)
        _fight(s, ("attack", 900), parry=("parry", 1, (draw, "hand")))
        assert len(s.p[1].hand) == n_hand - 1 + (0 if empty else 1)
        assert len(s.p[1].life) == n_life                               # 4 vs 4 + 3: stopped, no life lost to the empty deck
        assert s.stats["react_decisive"][1] == 1                         # without it 4 >= 4 hits
    up = _card("_blu002", type="reaction", cost=1, power=0, react={"do": [
        {"op": "def_mod", "n": 3}, {"op": "raddrizza", "target": "opposer"}]})
    s = _arena()
    s.p[0].units = [Unit(900, _card("_a3", power=3), True)]
    s.p[1].units = [Unit(901, _card("_d2", power=2), True)]
    s.p[1].guard = 1
    s.p[1].hand.append(up)
    _fight(s, ("attack", 900), oppose=901, parry=("parry", 1, (up, "hand")))
    assert s.unit(0, 900) is None and s.unit(1, 901).ready              # straightened after the combat


def test_op_condition_scars_ge_changes_a_value():
    bonus = _card("_blu022", type="reaction", cost=1, power=0, react={"do": [
        {"op": "def_mod", "n": 3}, {"op": "def_mod", "n": 1, "if": [{"scars_ge": 2}]}]})
    s = _arena()
    s.p[0].units = [Unit(900, _card("_a4", power=4), True)]
    s.step(("attack", 900))
    assert s.compute(0, 1, (bonus, "hand"), None)[1] == 4 + 3
    for _ in range(2):
        s.p[1].scars.append([s.p[1].life.pop(), False, "attacco"])
    assert s.compute(0, 1, (bonus, "hand"), None)[1] == 4 + 4


def test_guard_max_cap_applies_last():
    cap = _card("_neu002", type="relic", cost=2, power=0, colors=(), abilities=[{"static": "guard_max", "value": 1, "cap": 4}])
    s = _arena()
    s.p[0].relics = [cap, "lanterna"]
    assert s.guard_max(0) == 4                                           # 2 + 1 + 1
    s.p[0].awakened = True
    s.p[0].life = []                                                     # Alle Corde: 3 + 2 + 1 = 6 -> 4
    assert s.guard_max(0) == 4
    s.p[0].relics = ["lanterna"]
    assert s.guard_max(0) == 5


def test_combat_conditions_target_is_unit_opposing_attacker_has():
    E.LEADERS["_thorn"] = LeaderCard(id="_thorn", name="thorn", colors=("G", "B"), base=(
        {"static": "power", "applies_to": {"side": "own"}, "if": [{"attacking": True}, {"target_is_unit": True}], "value": 1},
        {"static": "power", "applies_to": {"side": "own"}, "if": [{"opposing": True}], "value": 1}), awakened=())
    neu009 = _card("_neu009", power=2, keywords=["scudo"],
                   abilities=[{"static": "power", "if": [{"opposing": True}, {"attacker_has": "caccia"}], "value": 2}])
    hunter, plain = _card("_hunter3", power=3, keywords=["caccia"]), _card("_plain3", power=3)
    s = _arena()
    s.p[0].leader = s.p[1].leader = "_thorn"
    s.p[0].units = [Unit(900, hunter, True), Unit(902, plain, True)]
    s.p[1].units = [Unit(901, neu009, True), Unit(903, plain, False)]
    s.step(("attack", 900, 903))
    fa, db, _ = s.compute(0, 0, None, None)
    assert (fa, db) == (3 + 1, 3)                                        # attacker +1 (target is a Unit); hunted: no "opposing"
    fa, db, _ = s.compute(0, 0, None, 901)
    assert (fa, db) == (3 + 1, 2 + 1 + 2)                                # opposer +1 (Thorn) +2 (attacker has Caccia)
    s.combat = E.Combat(902)
    fa, db, _ = s.compute(0, 0, None, None)
    assert fa == 3 and db == 4                                           # Leader target: no bonus
    fa, db, _ = s.compute(0, 0, None, 901)
    assert (fa, db) == (4, 2 + 1)                                        # attacker without Caccia: no +2


def _snap(s):
    return [(p.life[:], p.hand[:], p.deck[:], [x[:] for x in p.scars], [(u.uid, u.ready) for u in p.units],
             p.brace, p.guard, p.l_ready) for p in s.p] + [s.phase, tuple(getattr(s.combat, k) for k in E.Combat.__slots__)]


def test_ai_hunts_and_pugno_game_stays_pure():
    from sim.v02.agents import PugnoGame
    hunter = _card("_hunter5", power=5, keywords=["caccia"])
    s = _arena()
    s.p[0].units = [Unit(900, hunter, True)]
    s.p[1].units = [Unit(901, _card("_p2b", power=2, cost=3), False)]
    s.p[1].guard = 2                                     # Maera: -2 with a gem in the pugno; 5 - 2 < 2 + 4
    assert RuleAgent2(0).act(s) != ("attack", 900, 901)
    s.p[1].guard = 0
    act = RuleAgent2(0).act(s)
    assert act == ("attack", 900, 901)                                   # 5 > 2: hunts
    s.p[1].guard = 1
    s.step(act)
    s.step(("gems", 0))
    before = _snap(s)
    PugnoGame(s).matrix("after")
    RuleAgent2(1).act(s)
    assert _snap(s) == before


def test_games_with_caccia_cards_terminate():
    import dataclasses
    old = E.CARDS["t_g3"]
    E.CARDS["t_g3"] = dataclasses.replace(old, keywords=old.keywords | {"caccia"})
    try:
        hunts = 0
        for seed in range(12):                                          # hunting depends on the draw
            s = _play(_game(rules_from("V02"), seed), [RuleAgent2(seed), RuleAgent2(seed + 1)])
            assert s.end_reason in ("colpo_finale", "crepuscolo", "mazzo_vuoto")
            hunts += sum(s.stats["hunt"])
        assert hunts > 0
    finally:
        E.CARDS["t_g3"] = old


def test_decided_before_commitment_metric():
    s = _arena()
    s.p[0].units = [Unit(900, _card("_big", power=9), True)]
    _fight(s, ("attack", 900))
    assert s.stats["decided_pre"][0] == 1


def test_report_has_r005_metrics_and_slot_presence():
    from sim.v02 import run as R
    recs = [R.play_game((("arden_rosso_verde", "thorn_verde_blu"), ("semplice", "semplice"), "V02", k, False)) for k in range(2)]
    E.META["lince"] = {"slot": ["11.1"]}
    try:
        m = R.metrics(recs)
        text = R.render("t", m, "V02", "semplice", 0)
        assert "M1 " in text and "M15 " in text and m["double_gems"] == 0
        assert "11.1" in m["slot_presence"] and R.minor_colour("arden_rosso_verde")[0] in ("R", "G")
    finally:
        E.META["lince"] = {}


# ---------------------------------------------------------------------------- R-006
def test_validator_names_card_and_unknown_fields():
    from sim.v02.validate import validate
    raw = {"cards": [
        {"id": "A", "type": "unit", "cost": 1, "power": 1, "colors": [], "_pending": "x", "intent": "ok", "tags": ["11.1"],
         "abilities": [{"static": "power", "if": [{"opposed": True}], "value": 1}]},
        {"id": "B", "type": "tactic", "cost": 1, "colors": [], "play": {"target": {"side": "opp", "type": "unit"},
                                                                      "do": [{"op": "zap", "target": "chosen"}]}},
        {"id": "C", "type": "unit", "cost": 1, "power": 1, "colors": [], "abilities": [
            {"trigger": "on_fly", "do": [{"op": "stanca", "target": "chosen"}]},
            {"static": "power", "value": 1, "unique": True}]},
        {"id": "D", "type": "reaction", "cost": 1, "colors": [], "react": {"do": [{"op": "defeat", "target": "attacker",
                                                                                  "sel": {"cost_le": 4}}]}}],
        "leaders": [{"id": "L", "colors": ["R"], "base": [{"static": "power", "applies_to": {"side": "own", "kind": "unit"}, "value": 1}]}]}
    errs = validate(raw)
    want = ["A.abilities[0].if: condizione sconosciuta 'opposed'", "B.play.target: chiave sconosciuta 'type'",
            "B.play.do[0]: op sconosciuta 'zap'", "C.abilities[0]: evento sconosciuto 'on_fly'",
            "C.abilities[0].do[0]: target 'chosen' senza un selettore 'target' nell'abilità",
            "C.abilities[1]: chiave sconosciuta 'unique'"]
    assert sorted(errs) == sorted(want), errs
    s = _arena()
    try:
        s.cond_ok(0, [{"opposed": True}], {})
        assert False
    except ValueError:
        pass
    try:
        s.matches(0, Unit(1, "recluta", True), {"type": "unit"})
        assert False
    except ValueError:
        pass


def test_load_cards_rejects_invalid_file():
    import json
    import tempfile
    raw = {"cards": [{"id": "X1", "type": "unit", "cost": 1, "colors": [], "power": 1,
                      "abilities": [{"trigger": "on_enter", "do": [{"op": "draw", "n": 1, "if": [{"nope": 1}]}]}]}],
           "leaders": []}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(raw, f)
    try:
        E.load_cards(f.name)
        assert False
    except ValueError as e:
        assert "X1.abilities[0].do[0].if: condizione sconosciuta 'nope'" in str(e)
    finally:
        os.unlink(f.name)
    assert "recluta" in E.CARDS                                          # the old database is untouched


def test_trigger_target_chosen_by_engine():
    tirer = _card("_ver009", abilities=[{"trigger": "on_enter", "target": {"side": "opp", "ready": True, "cost_le": 3},
                                         "do": [{"op": "stanca", "target": "chosen"}]}])
    s = _arena()
    s.p[0].brace = 2
    s.p[0].hand.append(tirer)
    s.p[1].units = [Unit(901, _card("_s2", power=2, cost=2), True), Unit(902, _card("_s4", power=4, cost=3), True),
                    Unit(903, _card("_s9", power=9, cost=6), True)]
    s.step(("play", tirer, None))
    assert [u.ready for u in s.p[1].units] == [True, False, True]       # highest Forza among cost <= 3
    s = _arena()                                                         # no legal target: nothing happens
    s.p[0].brace = 2
    s.p[0].hand.append(tirer)
    s.step(("play", tirer, None))
    assert len(s.p[0].units) == 1
    raider = _card("_neu018", power=5, abilities=[{"trigger": "on_attack", "target": {"side": "opp", "ready": True},
                                                   "do": [{"op": "stanca", "target": "chosen"}]}])
    s = _arena()
    s.p[0].units = [Unit(900, raider, True)]
    s.p[1].units = [Unit(901, _card("_s2", power=2), True)]
    s.step(("attack", 900))
    assert not s.unit(1, 901).ready and s.phase == "pugno_att"           # nobody left to oppose


def test_stack_false_and_kind_unit():
    aura = _card("_ner016", type="relic", cost=3, power=0, colors=("K",), abilities=[
        {"static": "power", "applies_to": {"side": "own", "attacker": True}, "value": 1, "stack": False}])
    unit_only = _card("_ver018", type="relic", cost=3, power=0, colors=("G",), abilities=[
        {"static": "power", "applies_to": {"side": "own", "attacker": True, "kind": "unit"}, "value": 1}])
    s = _arena()
    s.p[0].units = [Unit(900, _card("_a3", power=3), True)]
    s.p[0].relics = [aura, aura]
    s.step(("attack", 900))
    assert s.compute(0, 0, None, None)[0] == 4                           # two copies: +1 once
    s = _arena()
    s.p[0].relics = [unit_only]
    s.step(("attack", "L"))
    assert s.compute(0, 0, None, None)[0] == 3                           # "kind": "unit": not the Leader
    s = _arena()
    s.p[0].relics = [aura]
    s.step(("attack", "L"))
    assert s.compute(0, 0, None, None)[0] == 4


def test_relic_triggers_on_own_reaction_and_attack_defeats_unit():
    blu018 = _card("_blu018", type="relic", cost=4, power=0, colors=("B",), abilities=[
        {"trigger": "on_own_reaction", "do": [{"op": "draw", "n": 1, "if": [{"deck_nonempty": True}]}]}])
    r = _card("_r3", type="reaction", cost=1, power=0, react={"do": [{"op": "def_mod", "n": 3}]})
    s = _arena()
    s.p[0].units = [Unit(900, _card("_a4", power=4), True)]
    s.p[1].relics = [blu018]
    s.p[1].guard = 1
    s.p[1].hand.append(r)
    n = len(s.p[1].hand)
    _fight(s, ("attack", 900), parry=("parry", 1, (r, "hand")))
    assert len(s.p[1].hand) == n                                         # -1 Reaction, +1 drawn after the combat
    ver022 = _card("_ver022", type="relic", cost=5, power=0, abilities=[
        {"trigger": "on_own_unit_attack_defeats_unit", "target": {"side": "opp", "ready": True, "cost_le": 4},
         "do": [{"op": "stanca", "target": "chosen"}]}])
    s = _arena()
    s.p[0].relics = [ver022]
    s.p[0].units = [Unit(900, _card("_hunter5", power=5, keywords=["caccia"]), True)]
    s.p[1].units = [Unit(901, _card("_s2", power=2), False), Unit(902, _card("_s1", power=1, cost=1), True)]
    _fight(s, ("attack", 900, 901), oppose=None)
    assert s.unit(1, 901) is None and not s.unit(1, 902).ready
    s = _arena()                                                         # opposing and defeating: no trigger
    s.active = 1
    s.p[0].relics = [ver022]
    s.p[0].units = [Unit(904, _card("_s9", power=9), True), Unit(906, _card("_s1", power=1, cost=1), True)]
    s.p[1].units = [Unit(905, _card("_a4", power=4), True)]
    _fight(s, ("attack", 905), oppose=904)
    assert s.unit(1, 905) is None and s.unit(1, 905) is None and s.unit(0, 906).ready


def test_dynamic_value_n_plus_if():
    s = _arena()
    sel = {"side": "opp", "ready": False, "power_le": {"n": 2, "plus": 1, "if": [{"scars_ge": 1}]}}
    s.p[1].units = [Unit(901, _card("_p3", power=3), False)]
    assert s._targets(0, sel) == []
    s.p[0].scars.append([s.p[0].life.pop(), False, "attacco"])
    assert s._targets(0, sel) == [901]


def test_reaction_defeats_attacker_with_sel():
    blu025 = _card("_blu025", type="reaction", cost=2, power=0, react={"do": [
        {"op": "att_mod", "n": -5}, {"op": "defeat", "target": "attacker", "sel": {"cost_le": 4}}]})
    for cost, gone in ((4, True), (5, False)):
        s = _arena()
        s.p[0].units = [Unit(900, _card(f"_a{cost}", power=6, cost=cost), True)]
        s.p[1].guard = 2
        s.p[1].hand.append(blu025)
        _fight(s, ("attack", 900), parry=("parry", 2, (blu025, "hand")))
        assert (s.unit(0, 900) is None) == gone
        assert s.stats["removals"][1] == (1 if gone else 0)


def test_combat_conditions_opposing_relic_react_from_scars_hunted_ready():
    neu014 = _card("_neu014", type="relic", cost=3, power=0, colors=(), abilities=[
        {"static": "combat", "role": "defense", "if": [{"opposing": True}], "def_mod": 1}])
    ner021 = _card("_ner021", type="relic", cost=5, power=0, colors=("K",), abilities=[
        {"static": "combat", "role": "defense", "if": [{"react_from_scars": True}], "att_mod": -2}])
    ver008 = _card("_ver008", power=1, keywords=["caccia"],
                   abilities=[{"static": "power", "if": [{"attacking": True}, {"hunted_ready": False}], "value": 2}])
    r = _card("_r0b", type="reaction", cost=1, power=0, react={"do": [{"op": "def_mod", "n": 0}]})
    E.LEADERS["_blank"] = LeaderCard(id="_blank", name="blank", colors=("R",), base=(), awakened=())
    s = _arena()
    s.p[1].leader = "_blank"
    s.p[0].units = [Unit(900, ver008, True)]
    s.p[1].relics = [neu014, ner021]
    s.p[1].units = [Unit(901, _card("_s2", power=2), False), Unit(902, _card("_s2", power=2), True)]
    s.step(("attack", 900, 901))
    assert s.compute(0, 0, None, None)[:2] == (1 + 2, 2)                 # hunted Rotated: +2; not opposing: no +1
    assert s.compute(0, 0, None, 902)[:2] == (1, 2 + 1)                  # replaced by an opposer: no +2; +1
    assert s.compute(0, 1, (r, "scar"), None)[0] == 3 - 2                # Reaction from a Scar: -2
    assert s.compute(0, 1, (r, "hand"), None)[0] == 3
    s = _arena()
    s.p[0].units = [Unit(900, ver008, True)]
    s.p[1].relics = [neu014]
    s.step(("attack", 900))
    assert s.compute(0, 0, None, None)[:2] == (1, 4)                     # Leader target: no +1, no +2


def test_hunted_target_fires_on_defeats_attacker():
    wall = _card("_blu003", power=5, keywords=["scudo"], abilities=[
        {"trigger": "on_defeats_attacker", "do": [{"op": "draw", "n": 1, "if": [{"deck_nonempty": True}]}]}])
    s = _arena()
    s.p[0].units = [Unit(900, _card("_hunter3", power=3, keywords=["caccia"]), True)]
    s.p[1].units = [Unit(901, wall, False)]
    n = len(s.p[1].hand)
    _fight(s, ("attack", 900, 901))
    assert s.unit(0, 900) is None and len(s.p[1].hand) == n + 1


def test_v02_decks_checked_against_v02_database():
    import json
    import tempfile
    from sim.v02 import decks as D
    leader, cards = D.load("arden_rosso_verde")
    assert leader == "arden" and len(cards) == 40
    multi = {"mazzi": [{"name": "ok", "leader": "arden", "cards": ["scudiera"] * 3 + ["t_r2"] * 3 + ["vesh"] * 3 + ["lince"] * 3
                        + ["esca"] * 3 + ["t_r3"] * 3 + ["t_g3"] * 3 + ["t_g4"] * 3 + ["t_n2"] * 3 + ["t_n4"] * 3
                        + ["carica"] * 2 + ["matriarca"] * 2 + ["colpo"] * 2 + ["recluta"] * 2 + ["t_r6"] * 2},
                       {"name": "bad", "leader": "arden", "cards": ["ROS-999"] * 40}]}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(multi, f)
    try:
        assert D.expand([f.name]) == [f.name + "#ok", f.name + "#bad"]
        assert len(D.load(f.name + "#ok")[1]) == 40
        try:
            D.load(f.name + "#bad")
            assert False
        except ValueError as e:
            assert "id sconosciuti: ROS-999" in str(e)
    finally:
        os.unlink(f.name)


def test_ai_uses_targetless_activated_ability():
    drawer = _card("_blu016", power=4, abilities=[{"activated": True, "cost": 1, "do": [{"op": "draw", "n": 1}]}])
    s = _arena()
    s.round = 2
    s.p[0].units = [Unit(900, drawer, True)]
    s.p[0].brace = 1
    s.p[0].hand = []
    s.p[1].guard = 3                                                     # 4 + 1 < 4 + 2: no credible attack
    assert RuleAgent2(0).act(s) == ("ability", 900, 0, None)


def test_defeat_triggers_look_back_on_mutual_defeat():
    """§7.5 (R-007 T-8): "quando sconfigge" fires even if its source died in the same combat;
    {"survived": true} restricts it to a source still in play."""
    drawer = _card("_drawer", power=3, abilities=[
        {"trigger": "on_own_unit_defeats_unit", "do": [{"op": "draw", "n": 1}]}])
    picky = _card("_picky", power=3, abilities=[
        {"trigger": "on_own_unit_defeats_unit", "if": [{"survived": True}], "do": [{"op": "draw", "n": 1}]}])
    for cid, drawn in ((drawer, 1), (picky, 0)):
        s = _arena()
        s.p[0].units = [Unit(900, cid, True)]
        s.p[1].units = [Unit(901, _card("_s3", power=3), True)]
        n = len(s.p[0].hand)
        _fight(s, ("attack", 900), oppose=901)
        assert s.unit(0, 900) is None and s.unit(1, 901) is None          # 3 contro 3: sconfitte entrambe
        assert len(s.p[0].hand) == n + drawn, cid
    guard = _card("_guard", power=3, abilities=[
        {"trigger": "on_defeats_attacker", "do": [{"op": "draw", "n": 1}]}])
    s = _arena()
    s.p[0].units = [Unit(900, _card("_s3", power=3), True)]
    s.p[1].units = [Unit(901, guard, True)]
    n = len(s.p[1].hand)
    _fight(s, ("attack", 900), oppose=901)
    assert len(s.p[1].hand) == n + 1


def test_global_trigger_stack_false_fires_once_per_id():
    """R-007: "stack": false on a global trigger = "Più copie non si sommano"."""
    for stack, drawn in ((True, 2), (False, 1)):
        payoff = _card(f"_payoff_{stack}", power=0, abilities=[
            {"trigger": "on_own_unit_defeats_unit", "stack": stack, "do": [{"op": "draw", "n": 1}]}])
        s = _arena()
        s.p[0].units = [Unit(900, _card("_s5", power=5), True), Unit(902, payoff, False), Unit(903, payoff, False)]
        s.p[1].units = [Unit(901, _card("_s1", power=1), True)]
        n = len(s.p[0].hand)
        _fight(s, ("attack", 900), oppose=901)
        assert len(s.p[0].hand) == n + drawn, stack


def test_q017_levers_tempra_awakened_and_leader_min_gems():
    """Q-017: tempra_awakened is the Db of an Awakened Leader; leader_min_gems stops a Leader
    hit with fewer gems than N."""
    s = _arena()
    s.r = s.r.with_(tempra_awakened=5)
    s.p[1].awakened = True
    assert s.tempra(1) == 5 and s.tempra(0) == 4
    s = _arena()
    s.p[0].awakened = True                                  # Risvegliato F4 contro Tempra 4
    assert s.preview("L", None, 0, 0)[2][0] is True
    s.r = s.r.with_(leader_min_gems=1)
    assert s.preview("L", None, 0, 0)[2][0] is False
    assert s.preview("L", None, 1, 0)[2][0] is True


def test_filters_read_forza_attuale_without_combat_bonuses():
    """R-009 T-9: "Forza ≤N" filters read printed Forza + auras; Furia and other conditional
    bonuses of the Unit itself are combat bonuses."""
    furioso = _card("_furioso", power=1, keywords=("furia",), abilities=[{"static": "power", "if": [{"furia": 1}], "value": 1}])
    s = _arena()
    s.p[1].units = [Unit(901, furioso, True)]
    s.p[1].scars = [("x", False), ("y", False)]
    u = s.unit(1, 901)
    assert s.unit_power(1, u) == 2                       # in uno scontro conta
    assert s.matches(1, u, {"side": "own", "power_le": 1}, {}, 1)



def test_q019_crepuscolo_simultaneo():
    """Q-019 B: one Crepuscolo check in G1's Ripristino for both players; only the one Alle Corde loses,
    with both Alle Corde nobody loses there."""
    s = _arena()
    s.r = s.r.with_(crepuscolo_simultaneo=True)
    s.round = 15
    n0, n1 = len(s.p[0].life), len(s.p[1].life)
    s._crepuscolo_both()
    assert len(s.p[0].life) == n0 - 2 and len(s.p[1].life) == n1 - 2 and not s.over
    s = _arena()
    s.r = s.r.with_(crepuscolo_simultaneo=True)
    s.round = 15
    s.p[1].life = s.p[1].life[:1]
    s._crepuscolo_both()
    assert s.over and s.winner == 0


def test_r012_leader_on_attack_trigger_and_att_mod():
    """R-012 primitiva 1: "quando il tuo Leader attacca" fires like a Unit's on_attack; an att_mod
    on the Leader counts in the combat."""
    E.LEADERS["_v2"] = LeaderCard(id="_v2", name="v2", colors=("G", "B"), base=(
        {"trigger": "on_attack", "target": {"side": "opp", "ready": True, "cost_le": 3},
         "do": [{"op": "stanca", "target": "chosen"}]},
        {"trigger": "on_attack", "do": [{"op": "att_mod", "n": 1}]}), awakened=())
    small = _card("_small2", power=2, cost=2)
    s = _arena()
    s.p[0].leader = "_v2"
    s.p[1].units = [Unit(901, small, True)]
    s.step(("attack", "L"))
    assert not s.unit(1, 901).ready                                      # Stancata quando il Leader attacca
    fa, _, _ = s.compute(0, 0, None, None)
    assert fa == s.r.leader_power + 1


def test_q019_v024_spareggio_vite_attivo():
    """Q-019 (V024): both Alle Corde in G1's Ripristino of round 15 -> fewer Lives loses, then the active player (G1)."""
    s = _arena()
    s.r = rules_from("V024")
    s.round, s.active = 15, 0
    s.p[0].life, s.p[1].life = s.p[0].life[:1], []
    s._crepuscolo_both()
    assert s.over and s.winner == 0                     # G2 a 0 Vite perde
    s = _arena()
    s.r = rules_from("V024")
    s.round, s.active = 15, 0
    s.p[0].life, s.p[1].life = s.p[0].life[:1], s.p[1].life[:1]
    s._crepuscolo_both()
    assert s.over and s.winner == 1                     # a Vite pari perde l'attivo (G1)


def test_q022_v026_p6_round_1_3():
    """Q-022 (V026): V024 with G2's extra gem in rounds 1 and 3 only, nothing else changed."""
    a, b = rules_from("V024"), rules_from("V026")
    assert b.scintilla_extra_rounds == () and a.scintilla_extra_rounds == (5,)
    assert b.with_(scintilla_extra_rounds=(5,)) == a
    extra = [r for r in range(1, 16) if r == b.scintilla_extra_round or r in b.scintilla_extra_rounds]
    assert b.scintilla_g2_gems == 1 and extra == [3]       # round 1 via scintilla_g2_gems, round 3 via extra_round


def test_q026_stanca_own_cost_and_choice():
    """Q-026 M1: "perdi 1 Vita oppure Stanca una tua Unità Pronta"; every way is its own action, none tried first."""
    t = _card("_ner019", type="tactic", cost=1, colors=("K",), power=0,
              play={"costs": [{"any": [{"lose_life": 1, "floor": 1}, {"stanca_own": 1}]}], "do": [{"op": "draw", "n": 1}]})
    only = _card("_ner002", type="tactic", cost=1, colors=("K",), power=0,
                 play={"costs": [{"stanca_own": 1}], "do": [{"op": "draw", "n": 1}]})
    s = _arena()
    s.p[0].brace = 2
    s.p[0].hand = [t]
    s.p[0].units = [Unit(900, "t_r6", True), Unit(901, "t_r6", False)]
    plays = [x for x in s.legal_actions() if x[0] == "play"]
    assert sorted(p[3] for p in plays) == [(("stanca", 900),), (("vita", 1, 1),)]
    life, hand = len(s.p[0].life), len(s.p[0].hand)
    s.step([p for p in plays if p[3][0][0] == "stanca"][0])
    assert not s.unit(0, 900).ready and len(s.p[0].life) == life and len(s.p[0].hand) == hand   # giocata -1, pescata +1
    assert s.stats["cost_paid"][0] == {f"{t} stanca": 1} and s.stats["life_costs"][0] == 0
    s.p[0].hand, s.p[0].brace = [only], 2
    assert not [x for x in s.legal_actions() if x[0] == "play"]       # nessuna Unità Pronta: non si paga
    s.p[0].hand = [t]
    plays = [x for x in s.legal_actions() if x[0] == "play"]
    assert [p[3] for p in plays] == [(("vita", 1, 1),)]
    s.step(plays[0])
    assert len(s.p[0].life) == life - 1 and s.stats["cost_paid"][0][f"{t} vita"] == 1
    assert s.stats["life_costs_round"][0] == {s.round: 1}


def test_q026_stanca_own_on_abilities_and_without_life():
    """A ⟳ with stanca_own never Stancas its own source; with Vita not payable only the Stanca ways remain."""
    src = _card("_ab", power=3, abilities=[{"activated": True, "cost": 0, "costs": [{"stanca_own": 1}],
                                            "do": [{"op": "draw", "n": 1}]}])
    t = _card("_any", type="tactic", cost=1, colors=("K",), power=0,
              play={"costs": [{"any": [{"lose_life": 1, "floor": 1}, {"stanca_own": 1}]}], "do": [{"op": "draw", "n": 1}]})
    s = _arena()
    s.p[0].brace = 1
    s.p[0].units = [Unit(900, src, True), Unit(901, "t_r6", True)]
    abil = [x for x in s.legal_actions() if x[0] == "ability" and x[1] == 900]
    assert [x[4] for x in abil] == [(("stanca", 901),)]
    s.step(abil[0])
    assert not s.unit(0, 900).ready and not s.unit(0, 901).ready
    assert not [x for x in s.legal_actions() if x[0] == "ability"]       # nessun'altra Unità Pronta
    s = _arena()
    s.p[0].brace, s.p[0].hand = 1, [t]
    s.p[0].units = [Unit(900, "t_r6", True)]
    s.p[0].life = s.p[0].life[:1]                                         # 1 Vita: floor 1, la Vita non si paga
    assert [x[3] for x in s.legal_actions() if x[0] == "play"] == [(("stanca", 900),)]


def test_q026_fixed_costs_keep_their_actions():
    """Cards with only a Vita cost keep the actions of before (3 elements): old results replay identically."""
    c = _card("_ros008", cost=1, colors=("R",), costs=[{"lose_life": 1, "floor": 1}])
    s = _arena()
    s.p[0].brace, s.p[0].hand = 2, [c]
    assert [x for x in s.legal_actions() if x[0] == "play"] == [("play", c, None)]


def test_q026_v027_deckbuilding():
    from sim.v02 import decks as D
    v26, v27 = rules_from("V026"), rules_from("V027")
    fill = {f"F{i}": 2 for i in range(17)}
    fill["F17"] = 1
    colors = dict({"A": ("R",), "B": ("R",), "T": ("R",), "LEG": ("R",), "RK": ("R", "K")}, **{f: () for f in fill})
    leaders = {"L": ("R", "G")}
    info = dict({"A": ("Gemella", "C"), "B": ("Gemella", "C"), "T": ("T", "C"), "LEG": ("LEG", "L"), "RK": ("RK", "R")},
                **{f: (f, "C") for f in fill})
    ok = dict({"A": 1, "B": 1, "T": 2, "LEG": 1}, **fill)                                   # 40 carte
    less = dict(ok, F17=0)

    def pr(rules, **kw):
        return D.problems("L", dict(less, **kw), colors, leaders, rules, info)
    assert D.problems("L", ok, colors, leaders, v27, info) == [] and D.problems("L", ok, colors, leaders, v26, info) == []
    assert pr(v27, B=2) == ["Gemella (A, B): 3 copie (massimo 2)"]
    assert pr(v27, T=3) == ["T: 3 copie (massimo 2)"] and pr(v26, T=3) == []               # V026: 3 per ID
    assert pr(v27, LEG=2) == ["LEG: 2 copie (massimo 1)"]
    assert pr(v27, RK=1) == ["RK: carta multicolore, il Leader non ha tutti i suoi colori"]
    assert pr(v26, RK=1) == []                                                              # V026: basta un colore
    assert D.limits(v27)["max_copies"] == 2 and D.limits(None)["max_copies"] == D.MAX_COPIES == 3
    assert D.rarity_warnings(v27, {"X": ("X", "NC")}) and not D.rarity_warnings(v26, {"X": ("X", "NC")})
    assert {k: v for k, v in v27.as_dict().items() if k not in D.limits(v27)} \
        == {k: v for k, v in v26.as_dict().items() if k not in D.limits(v26)}          # le partite sono quelle di V026


# ---------------------------------------------------------------- R-026 (Q-027): primitive
def _q027_cards():
    return {
        "I03": _card("_i03", type="tactic", cost=3, colors=("B",), power=0,
                     play={"costs": [{"stanca_own": 1}], "target": {"side": "opp", "ready": True, "cost_le": 4},
                           "do": [{"op": "bounce"}]}),
        "I02": _card("_i02", type="tactic", cost=2, colors=("K",), power=0,
                     play={"costs": [{"sacrifice": 1}], "target": {"side": "opp", "cost_le": 4}, "do": [{"op": "defeat"}]}),
        "I09": _card("_i09", cost=3, colors=("K",), power=2, abilities=[
            {"trigger": "on_rim", "target": {"side": "opp", "ready": True, "power_le": {"scars": "own"}}, "do": [{"op": "stanca"}]}]),
        "I10": _card("_i10", cost=2, colors=("G",), power=2, abilities=[
            {"trigger": "on_rim", "do": [{"op": "raddrizza", "target": "self", "sel": {"ready": False}}]}]),
        "I08": _card("_i08", cost=3, colors=("K",), power=2, abilities=[
            {"trigger": "on_enter", "if": [{"scars_ge": 2}],
             "do": [{"op": "recover", "from": "discard", "sel": {"kind": "unit", "cost_le": 2, "without_trigger": "on_enter"}}]}]),
        "I04": _card("_i04", type="reaction", cost=0, colors=(), power=0,
                     react={"play_if": [{"target_is_unit": True}, {"no_own_gems": True}], "do": [{"op": "def_mod", "n": 2}]}),
    }


def test_r026_bounce_ready_units_cost_le_4():
    k = _q027_cards()
    big = _card("_big5", cost=5, power=5)
    s = _arena()
    s.p[0].brace, s.p[0].hand = 3, [k["I03"]]
    s.p[0].units = [Unit(900, "t_r6", True)]
    u2 = _card("_u2", cost=2, power=2)
    s.p[1].units = [Unit(901, u2, True), Unit(902, u2, False), Unit(903, big, True)]
    plays = [x for x in s.legal_actions() if x[0] == "play"]
    assert [(x[2], x[3]) for x in plays] == [(901, (("stanca", 900),))]     # solo Pronta con costo ≤4
    s.step(plays[0])
    assert s.unit(1, 901) is None and s.p[1].hand[-1] == u2 and u2 not in s.p[1].discard
    assert s.stats["removals_src"][0] == {"rimbalzo": 1} and s.stats["removals"][0] == 1


def test_r026_on_rim_triggers_after_the_scar_returns():
    k = _q027_cards()
    weak, mid = _card("_w2", power=2), _card("_m3", power=3)
    s = _arena()
    pl = s.p[0]
    pl.brace, pl.l_ready = 1, True
    pl.scars = [[c, False, "test"] for c in pl.life[:3]]
    pl.life = pl.life[3:]
    pl.units = [Unit(900, k["I09"], True), Unit(901, k["I10"], False)]
    s.p[1].units = [Unit(910, mid, True), Unit(911, weak, True)]
    s.step([x for x in s.legal_actions() if x[0] == "rim"][0])
    assert len(pl.scars) == 2                                              # la soglia è letta dopo il Rimarginare
    assert s.unit(1, 911).ready is False and s.unit(1, 910).ready is True
    assert s.unit(0, 901).ready is True                                    # I10 raddrizza sé stessa
    assert ("attack", 901) in s.legal_actions()


def test_r026_sacrifice_g1():
    k = _q027_cards()
    rush = _card("_rush", power=3, keywords=["assalto"])
    s = _arena()
    s.p[0].brace, s.p[0].hand = 2, [k["I02"]]
    s.p[0].units = [Unit(900, "t_r6", True), Unit(901, rush, True), Unit(902, "t_r6", False)]
    s.p[1].units = [Unit(910, _card("_u2", cost=2, power=2), False)]
    plays = [x for x in s.legal_actions() if x[0] == "play"]
    assert [x[3] for x in plays] == [(("sacrifica", 900),)]               # Pronta e senza Assalto
    s.step(plays[0])
    assert s.unit(0, 900) is None and "t_r6" in s.p[0].discard and s.unit(1, 910) is None
    assert s.stats["sacrifices"][0] == 1 and s.stats["removals_src"][0] == {"sacrificio": 1, "sconfiggi": 1}
    s.p[0].hand, s.p[0].brace = [k["I02"]], 2
    s.p[1].units = [Unit(911, "t_r6", True)]
    s.p[0].units = [Unit(901, rush, True)]
    assert not [x for x in s.legal_actions() if x[0] == "play"]           # niente da sacrificare
    from sim.v02.validate import validate
    base = {"id": "X", "cost": 1, "colors": [], "power": 1}
    errs = validate({"cards": [dict(base, type="unit", costs=[{"sacrifice": 1}]),
                               dict(base, id="Y", type="unit", abilities=[{"activated": True, "costs": [{"sacrifice": 1}], "do": []}]),
                               dict(base, id="Z", type="tactic", play={"costs": [{"sacrifice": 1}], "do": [{"op": "draw", "n": 1}]}),
                               dict(base, id="W", type="tactic", play={"costs": [{"sacrifice": 1}], "do": []})]})
    assert [e.split(":")[0] for e in errs] == ["X.costs[0]", "Y.abilities[0].costs[0]", "Z"], errs


def test_r026_recover_and_g2():
    k = _q027_cards()
    cheap = _card("_c2", cost=2, power=2)
    enter = _card("_e2", cost=2, power=3, abilities=[{"trigger": "on_enter", "do": [{"op": "draw", "n": 1}]}])
    taker = _card("_t2", cost=2, power=4, abilities=[{"trigger": "on_attack", "do": [
        {"op": "recover", "sel": {"kind": "unit"}}]}])
    s = _arena()
    pl = s.p[0]
    pl.brace, pl.hand = 3, [k["I08"]]
    pl.discard = [cheap, enter, taker, "_big5", k["I03"]]
    pl.scars = [[c, False, "test"] for c in pl.life[:1]]
    s.step(("play", k["I08"], None))
    assert pl.hand == [] and s.stats["recovers"][0] == 0                   # 1 Cicatrice: niente
    pl.scars.append([pl.life[1], False, "test"])
    pl.brace, pl.hand = 3, [k["I08"]]
    s.step(("play", k["I08"], None))
    assert pl.hand == [cheap] and cheap not in pl.discard and s.stats["recovers"][0] == 1   # né "Quando entra" né G2
    s.r = s.r.with_(g2_recupero=False)
    pl.brace, pl.hand, pl.discard = 3, [k["I08"]], [cheap, taker]
    pl.units = []
    s.step(("play", k["I08"], None))
    assert pl.hand == [taker]


def test_r026_reaction_cost_0_with_play_if():
    k = _q027_cards()
    s = _arena()
    s.p[0].units = [Unit(900, "t_r6", True)]
    s.p[1].units = [Unit(901, "t_r6", True)]
    s.p[1].guard, s.p[1].hand = 2, [k["I04"]]
    s.step(("attack", 900))
    s.step(("no_oppose",))
    s.step(("gems", 0))
    assert not [x for x in s.legal_actions() if x[2]]                      # bersaglio il Leader: non si gioca
    s = _arena()
    s.p[0].units = [Unit(900, "t_r6", True)]
    s.p[1].units = [Unit(901, "t_r6", True)]
    s.p[1].guard, s.p[1].hand = 2, [k["I04"]]
    s.step(("attack", 900))
    s.step(("oppose", 901))
    s.step(("gems", 0))
    assert [x[1] for x in s.legal_actions() if x[2]] == [0]                # costo 0, e nessuna gemma nell'impegno
    assert s.compute(0, 0, (k["I04"], "hand"), 901)[:2] == (7, 9)
    s.step(("parry", 0, (k["I04"], "hand")))
    assert s.unit(0, 900) is None and k["I04"] in s.p[1].discard and s.stats["reactions"][1] == 1
    assert s.stats["react_legal"][1] == 1 and s.stats["react_avail"][1] == 1


def test_r027_reazione_da_cicatrice_costo():
    """P9b: con −1 una Reazione da 1 gemma giocata da una Cicatrice dritta costa 0; dalla mano costa sempre 1."""
    r = _card("_r027", type="reaction", cost=1, colors=(), power=0, react={"do": [{"op": "def_mod", "n": 3}]})
    for delta, from_scar, from_hand in ((0, 1, 1), (-1, 0, 1)):
        s = _arena()
        s.r = s.r.with_(reazione_da_cicatrice_costo=delta)
        s.p[0].units = [Unit(900, "t_r6", True)]
        s.p[1].guard, s.p[1].hand = 1, [r]
        s.p[1].scars = [[r, False, "test"]]
        s.step(("attack", 900))
        s.step(("gems", 0))
        acts = [x for x in s.legal_actions() if x[2]]
        assert min(x[1] for x in acts if x[2][1] == "scar") == from_scar
        assert min(x[1] for x in acts if x[2][1] == "hand") == from_hand
        assert s.react_cost(r, "scar") == from_scar


def test_r027_valida_set_laws():
    """§14, leggi 12, 13 e 15 (Q-029) in `valida`."""
    from sim.v02.validate import validate
    base = {"cost": 1, "colors": [], "power": 0}
    bad = [dict(base, id="V1", type="reaction", costs=[{"any": [{"lose_life": 1}, {"stanca_own": 1}]}],
                react={"do": [{"op": "def_mod", "n": 2}]}),
           dict(base, id="V2", type="reaction", react={"do": [{"op": "def_mod", "n": 2}], "do_from_scars": [{"op": "draw", "n": 1}]}),
           dict(base, id="V3", type="unit", abilities=[{"trigger": "on_oppose", "do": [{"op": "draw", "n": 1}]}]),
           dict(base, id="V4", type="reaction", cost=0, react={"do": [{"op": "def_mod", "n": 2}]}),
           dict(base, id="V5", type="reaction", cost=0, react={"play_if": [{"target_is_unit": True}],
                                                              "do": [{"op": "raddrizza", "target": "opposer"}]})]
    good = [dict(base, id="G1", type="reaction", react={"do": [{"op": "draw", "n": 1, "if": [{"deck_nonempty": True}]}]}),
            dict(base, id="G2", type="unit", abilities=[{"trigger": "on_oppose", "if": [{"deck_nonempty": True}],
                                                          "do": [{"op": "draw", "n": 1}]}]),
            dict(base, id="G3", type="unit", abilities=[{"trigger": "on_enter", "do": [{"op": "draw", "n": 1}]}]),
            dict(base, id="G4", type="unit", costs=[{"lose_life": 1}])]
    errs = validate({"cards": bad + good})
    assert sorted({e.split(":")[0].split(".")[0] for e in errs}) == ["V1", "V2", "V3", "V4", "V5"], errs


def test_r027_p9b_diagnostic():
    """La diagnostica conta per fonte: disponibile, giocabile con la Guardia, legale con l'impegno, giocata."""
    r = _card("_r027d", type="reaction", cost=1, colors=(), power=0, react={"do": [{"op": "def_mod", "n": 3}]})
    s = _arena()
    s.p[0].units = [Unit(900, "t_r6", True)]
    s.p[1].guard, s.p[1].hand = 1, [r]
    s.step(("attack", 900))
    s.step(("gems", 0))
    s.step(("parry", 0, None))                                            # la tiene in mano, nessuna gemma
    assert s.stats["react_diag"][1] == {"scontri|zero": 1, "hand|disp|zero": 1, "hand|guardia|zero": 1}


def test_r028_bruciare():
    """V1: la stessa giocata con 1 gemma in meno, scartando una carta scelta come azione a sé; una volta per turno."""
    big, a, b = _card("_r028u3", cost=3, power=3), _card("_r028a", cost=1, power=1), _card("_r028b", cost=2, power=2)
    s = _arena()
    s.p[0].brace, s.p[0].hand = 2, [big, a, b]
    assert not any(x[1] == big for x in s.legal_actions() if x[0] == "play")          # default: spento
    s.r = s.r.with_(bruciare=True)
    plays = [x for x in s.legal_actions() if x[0] == "play"]
    assert ("play", big, None, None, "brucia") in plays and ("play", big, None) not in plays
    assert ("play", a, None) in plays and ("play", a, None, None, "brucia") in plays
    s.step(("play", big, None, None, "brucia"))
    assert s.phase == "brucia" and s.decider() == 0
    assert s.legal_actions() == [("brucia", a), ("brucia", b)]
    s.step(("brucia", b))
    assert s.phase == "main" and s.p[0].brace == 0 and b in s.p[0].discard and s.p[0].hand == [a]
    assert [u.cid for u in s.p[0].units] == [big] and s.stats["ritmo"][0]["bruciate"] == 1
    s.p[0].brace, s.p[0].hand = 1, [a, b]
    assert not any(len(x) > 4 for x in s.legal_actions())                             # una volta per turno
    s2 = _arena()
    s2.r = s2.r.with_(bruciare=True, bruciare_min_mano=4)
    s2.p[0].brace, s2.p[0].hand = 2, [big, a, b]
    assert not any(len(x) > 4 for x in s2.legal_actions())                            # V1b: servono 4 carte in mano


def test_r028_tempra_tardo_e_allo_scoperto():
    s = _arena()
    s.r = s.r.with_(tempra_tardo=10)
    s.round = 9
    assert s.tempra(0) == s.tempra(1) == 4
    s.round = 10
    assert s.tempra(0) == s.tempra(1) == 3
    s = _arena()
    s.r = s.r.with_(allo_scoperto=True)
    s.p[1].life = []
    assert s.tempra(1) == 3 and s.tempra(0) == 4


def test_r028_breccia():
    """V3: se l'Unità con Breccia batte chi si oppone, il Leader avversario perde 1 Vita, nel rispetto del Saldo."""
    br, small = _card("_r028br", power=5, keywords=["breccia"]), _card("_r028sm", power=1)
    for fresh, lost in ((0, 1), (2, 0)):
        s = _arena()
        s.p[0].units = [Unit(900, br, True)]
        s.p[1].units = [Unit(901, small, True)]
        s.p[1].scars = [[c, True, "test"] for c in s.p[1].life[:fresh]]
        n = len(s.p[1].life)
        _fight(s, ("attack", 900), oppose=901)
        assert s.unit(1, 901) is None and n - len(s.p[1].life) == lost
        assert s.stats["breccia"][0] == lost
        assert s.stats["breccia_by"][0] == ({"_r028br|tent": 1, "_r028br|ok": 1} if lost else {"_r028br|tent": 1})
    s = _arena()                                                    # sconfitta reciproca: la Breccia scatta e si conta a parte
    eq = _card("_r028eq", power=5)
    s.p[0].units = [Unit(900, br, True)]
    s.p[1].units = [Unit(901, eq, True)]
    _fight(s, ("attack", 900), oppose=901)
    assert s.unit(0, 900) is None and s.unit(1, 901) is None
    assert s.stats["breccia_by"][0] == {"_r028br|tent": 1, "_r028br|ok": 1, "_r028br|ok_pari": 1}


def test_r028_partite_con_le_leve():
    """Partite intere con tutte le leve accese: finiscono e riempiono i contatori di ritmo."""
    rules = rules_from("V02").with_(bruciare=True, tempra_tardo=10, allo_scoperto=True)
    for seed in range(4):
        s = _play(_game(rules, seed), [RuleAgent2(seed=1), RuleAgent2(seed=2)])
        assert s.over and s.stats["ritmo"][0]["turni"] > 0 and len(s.stats["vite_round"]) == s.round
    assert any(sum(_play(_game(rules, k), [RuleAgent2(seed=1), RuleAgent2(seed=2)]).stats["ritmo"][q].get("bruciate", 0)
                   for q in (0, 1)) for k in range(4))


def test_r027_scudo_vince_pareggi_se_pronta():
    """P7 (c): lo Scudo vince i pareggi solo se è Pronto allo scontro: da bersaglio cacciato Pronto; chi si oppone si è ruotato."""
    hunter, shield = _card("_r027h", power=3, keywords=["caccia"]), _card("_r027s", power=3, keywords=["scudo"])
    for mode, ready, survives in (("vince_pareggi", False, True), ("vince_pareggi_se_pronta", True, True),
                                  ("vince_pareggi_se_pronta", False, False)):
        s = _arena()
        s.r = s.r.with_(scudo=mode)
        s.p[0].units = [Unit(900, hunter, True)]
        s.p[1].units = [Unit(901, shield, ready)]
        _fight(s, ("attack", 900, 901))
        assert (s.unit(1, 901) is not None) == survives and s.unit(0, 900) is None
    s = _arena()
    s.r = s.r.with_(scudo="vince_pareggi_se_pronta")
    s.p[0].units = [Unit(900, _card("_r027a", power=3), True)]
    s.p[1].units = [Unit(901, shield, True)]
    _fight(s, ("attack", 900), oppose=901)
    assert s.unit(1, 901) is None and s.unit(0, 900) is None                         # chi si oppone è Ruotato: pareggio senza Scudo

def test_r027_p7_contatori_scudo():
    """P7: i contatori dello Scudo (solo lettura) contano opposizioni, ripetute e rimozioni subite per fonte."""
    shield = _card("_r027c", power=3, keywords=["scudo"])
    s = _arena()
    assert s.stats is not None and s.track is not None
    s.p[0].units = [Unit(900, _card("_r027b", power=5), True)]
    s.p[1].units = [Unit(901, shield, True)]
    _fight(s, ("attack", 900), oppose=901)
    assert s.unit(1, 901) is None
    assert s.stats["scudo_opp"][1] == 1 and s.stats["scudo_opp_rep"][1] == 0
    assert s.stats["scudo_rimossa"][1] == {"scontro": 1}
    s = _arena()
    s.p[0].units = [Unit(900, _card("_r027d", power=5, keywords=["caccia"]), True)]
    s.p[1].units = [Unit(901, shield, False)]
    _fight(s, ("attack", 900, 901))
    assert s.unit(1, 901) is None and s.stats["scudo_rimossa"][1] == {"caccia": 1} and s.stats["scudo_opp"][1] == 0


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
