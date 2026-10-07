"""Checks of the v0.2 candidate core (sim/v02, Q-013 B0)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from sim.run import load_deck
from sim.v02.agents import RuleAgent2, regret_matching
from sim.v02.config import B0, PRESETS, rules_from
from sim.v02.engine import Unit, new_game


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


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
