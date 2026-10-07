"""Checks of the card-language extensions asked in R-002 (tcg/set/richieste/R-002_estensioni_dsl.md).
Test cards are added to the database only for these tests."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sim import effects
from sim.cards import CARDS, Card
from sim.config import DEFAULT
from sim.engine import Unit, new_game
from sim.run import load_deck


def _card(**kw):
    kw.setdefault("colors", ())
    c = Card(**kw)
    CARDS[c.id] = c
    return c


_card(id="zz_costo_vita", name="Unità a costo Vita", type="unit", cost=1, power=4,
      costs=({"lose_life": 1, "floor": 2},))
_card(id="zz_reazione_vita", name="Reazione a costo Vita", type="reaction", cost=1,
      react={"costs": [{"lose_life": 1, "floor": 1}], "do": [{"op": "def_mod", "n": 3}]})
_card(id="zz_intercettata", name="Si vendica", type="unit", cost=2, power=3,
      abilities=({"trigger": "on_intercepted", "do": [{"op": "temp_power", "n": 2}]},))
_card(id="zz_inarrestabile", name="Inarrestabile", type="unit", cost=2, power=3,
      abilities=({"trigger": "on_attack", "do": [{"op": "unblockable", "target": "self"}]},))
_card(id="zz_scudo", name="Scudo", type="unit", cost=2, power=2, keywords=frozenset({"scudo"}))
_card(id="zz_esecuzione", name="Esecuzione", type="tactic", cost=1,
      play={"target": {"side": "opp", "power_le": "@scars"}, "do": [{"op": "defeat", "target": "chosen"}]})
_card(id="zz_lanterna", name="Lanterna", type="relic", cost=1,
      abilities=({"static": "guard_max", "value": 1, "cap": 3},))
_card(id="zz_scartata", name="Accumulatore", type="unit", cost=2, power=2,
      abilities=({"trigger": "on_guard_discarded", "do": [{"op": "draw", "n": "@n"}]},))
_card(id="zz_rincorsa", name="Rincorsa", type="unit", cost=2, power=2,
      abilities=({"static": "power", "if": [{"is_second_player": True}, {"life_behind_ge": 2}], "value": 3},))


def _game(rules=DEFAULT):
    (l1, d1), (l2, d2) = load_deck("arden_rosso_verde"), load_deck("maera_blu_nero")
    s = new_game(l1, d1, l2, d2, rules=rules, seed=0)
    s.p[0].turn_no = 2               # past the first-turn rule
    return s


def _unit(s, q, cid, uid):
    u = Unit(uid, cid, 0)
    s.p[q].units.append(u)
    return u


def test_life_cost_on_unit_is_paid_and_respects_floor():
    s = _game()
    pl = s.p[0]
    pl.hand.append("zz_costo_vita")
    pl.brace = 5
    assert ("play", "zz_costo_vita", None) in s.legal_actions()
    s.step(("play", "zz_costo_vita", None))
    assert len(pl.life) == 4 and pl.lost_this_turn == 1
    pl.life[:] = pl.life[:2]         # 2 Vite left: floor 2 forbids paying
    pl.hand.append("zz_costo_vita")
    assert ("play", "zz_costo_vita", None) not in s.legal_actions()


def test_life_cost_on_reaction():
    s = _game()
    d = s.p[1]
    d.hand.append("zz_reazione_vita")
    d.guard = 2
    s.step(("attack", "L", "L"))
    while s.phase == "intercept":
        s.step(("no_intercept",))
    assert ("reaction", "zz_reazione_vita", "hand") in s.legal_actions()
    s.step(("reaction", "zz_reazione_vita", "hand"))
    assert len(d.life) == 4          # paid 1 Vita, and the attack (3 vs 5+3) did not hit


def test_on_intercepted_fires_on_attacker():
    s = _game()
    att = _unit(s, 0, "zz_intercettata", 900)
    _unit(s, 1, "zz_scudo", 901)
    s.step(("attack", 900, "L"))
    assert s.phase == "intercept"
    s.step(("intercept", 901))
    assert att.temp == 2


def test_unblockable_skips_intercept():
    s = _game()
    _unit(s, 0, "zz_inarrestabile", 900)
    _unit(s, 1, "zz_scudo", 901)
    s.step(("attack", 900, "L"))
    assert s.phase != "intercept"


def test_power_le_scars_selector():
    s = _game()
    pl = s.p[0]
    _unit(s, 1, "zz_scudo", 901)     # Forza 2
    pl.hand.append("zz_esecuzione")
    pl.brace = 5
    acts = [a for a in s.legal_actions() if a[:2] == ("play", "zz_esecuzione")]
    assert acts == []                # 0 Cicatrici: no target
    pl.scars += [pl.life.pop(), pl.life.pop()]
    acts = [a for a in s.legal_actions() if a[:2] == ("play", "zz_esecuzione")]
    assert acts == [("play", "zz_esecuzione", 901)]


def test_guard_max_cap():
    s = _game()
    assert s.guard_max(0) == 2
    s.p[0].relics.append("zz_lanterna")
    assert s.guard_max(0) == 3
    s.p[0].awakened = True           # base 3 + 1 would be 4, cap 3
    assert s.guard_max(0) == 3


def test_on_guard_discarded_draws_n():
    s = _game()
    pl = s.p[1]
    _unit(s, 1, "zz_scartata", 900)
    pl.guard = 2
    hand = len(pl.hand)
    s.step(("end",))                 # P2's Ripristino discards 2 Guardia, then normal draw
    assert len(pl.hand) == hand + 2 + 1


def test_second_player_and_life_behind_conditions():
    s = _game()
    u = _unit(s, 1, "zz_rincorsa", 900)
    assert s.unit_power(1, u) == 2
    s.p[1].life[:] = s.p[1].life[:3]  # 3 vs 5: behind by 2
    assert s.unit_power(1, u) == 5
    v = _unit(s, 0, "zz_rincorsa", 901)
    s.p[0].life[:] = s.p[0].life[:1]
    assert s.unit_power(0, v) == 2    # G1 never gets the bonus


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
