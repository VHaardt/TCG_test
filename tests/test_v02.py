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


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
