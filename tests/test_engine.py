"""Basic checks of the engine, the rule modules and the card language.
Run: python -m pytest -q   (or python tests/test_engine.py)"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sim.agents import RandomAgent, RuleAgent
from sim.config import DEFAULT, VARIANTS, rules_for
from sim.engine import Unit, new_game
from sim.run import all_decks, load_deck


def _game(rules=DEFAULT, seed=0):
    (l1, d1), (l2, d2) = load_deck("arden_rosso_verde"), load_deck("maera_blu_nero")
    return new_game(l1, d1, l2, d2, rules=rules, seed=seed)


def _play(s, agents):
    while not s.over:
        s.step(agents[s.decider()].act(s))
    return s


def test_decks_are_legal():
    for d in all_decks():
        load_deck(d)


def test_games_terminate_under_every_variant():
    for name in VARIANTS:
        for seed in range(5):
            s = _play(_game(rules_for(name), seed), [RuleAgent(), RandomAgent(seed)])
            assert s.end_reason in ("colpo_finale", "crepuscolo", "mazzo_vuoto"), (name, s.end_reason)
            assert s.p[0].turn_no <= 17


def test_saldo_module_caps_life_loss_and_can_be_removed():
    s = _game()
    s.lose_life(1, 4, "test")
    assert len(s.p[1].life) == 3
    s2 = _game(DEFAULT.with_modules(remove=["saldo"]))
    s2.lose_life(1, 4, "test")
    assert len(s2.p[1].life) == 1


def test_risveglio_after_three_lives():
    s = _game(DEFAULT.with_modules(remove=["saldo"]))
    s.lose_life(1, 3, "test")
    s.state_checks()
    assert s.p[1].awakened


def test_colpo_finale_needs_snapshot():
    s = _game(DEFAULT.with_modules(remove=["saldo"]))
    s.lose_life(1, 5, "test")
    assert not s.snapshot            # Alle Corde only during this turn: no snapshot yet
    s.p[0].turn_no = 2
    s.p[0].brace = 5
    s.step(("infuse", "L"))
    s.step(("infuse", "L"))
    s.step(("attack", "L", "L"))
    while s.phase != "main":
        s.step(s.legal_actions()[0])
    assert not s.over                 # hit on a Leader that was not Alle Corde at turn start


def test_scudiera_infuso_from_card_data():
    s = _game()
    pl = s.p[0]
    u = Unit(999, "scudiera", 0)
    pl.units.append(u)
    pl.brace = 2
    s.step(("infuse", 999))
    assert u.temp == 2               # +1 infusion, +1 Infuso (first infusion)
    s.step(("infuse", 999))
    assert u.temp == 4               # +1 infusion, +1 Arden (second infusion)


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
