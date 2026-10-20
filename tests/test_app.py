"""Checks of the online app (app/): rooms, deck building, draft and full games through the API."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import core, server
from sim.v02 import decks, engine as E


def _api(path, body=None, method="POST"):
    code, out = server.api(method, path, {}, body or {})
    assert code == 200, (path, out)
    return out


def _play_out(code, tokens, limit=3000):
    """Both humans pick the first legal action until the game ends."""
    for _ in range(limit):
        views = [_api("/api/stato", {"codice": code, "token": t}, "GET") for t in tokens]
        p = [v["partita"] for v in views]
        if "fine" in p[0]:
            return p
        for t, v in zip(tokens, p):
            if v["tocca_a_te"]:
                acts = v["azioni"]
                pick = next((a for a in acts if a["gruppo"] != "turno"), acts[0])
                _api("/api/azione", {"codice": code, "token": t, "versione": v["versione"], "indice": pick["i"]})
                break
    raise AssertionError("partita non finita")


def test_catalogo_and_reference_decks_are_legal():
    cat = _api("/api/catalogo", method="GET")
    assert cat["costruzione"] == {"carte": decks.DECK_SIZE, "copie": decks.MAX_COPIES}
    assert len(cat["leader"]) >= 2 and len(cat["carte"]) >= 40 and cat["mazzi"]
    for m in cat["mazzi"]:
        assert not decks.problems(m["leader"], m["carte"])


def test_constructed_room_two_humans():
    cat = core.dati().catalogo()
    a = _api("/api/stanza", {"nome": "A", "modalita": "costruito"})
    b = _api("/api/entra", {"nome": "B", "codice": a["codice"]})
    m = cat["mazzi"][0]
    bad = dict(m["carte"]); bad[next(iter(bad))] += 5
    code, out = server.api("POST", "/api/mazzo", {}, {**a, "leader": m["leader"], "carte": bad})
    assert code == 400 and "illegale" in out["errore"]
    _api("/api/mazzo", {**a, "leader": m["leader"], "carte": m["carte"]})
    v = _api("/api/mazzo", {**b, "leader": cat["mazzi"][1]["leader"], "carte": cat["mazzi"][1]["carte"]})
    assert v["fase"] == "partita"
    # hidden information: no opponent hand, no Life cards
    assert "mano" in v["partita"]["io"] and "mano" not in v["partita"]["avversario"]
    p = _play_out(a["codice"], [a["token"], b["token"]])
    assert p[0]["fine"]["hai_vinto"] != p[1]["fine"]["hai_vinto"]
    v = _api("/api/rivincita", a)
    assert v["fase"] == "preparazione"


def test_draft_respects_leader_colours_and_copies():
    a = _api("/api/stanza", {"nome": "A", "modalita": "draft", "contro_ia": True})
    v = _api("/api/stato", a, "GET")
    assert len(v["draft"]["leader_offerta"]) == 3
    v = _api("/api/draft/leader", {**a, "leader": v["draft"]["leader_offerta"][0]})
    leader = v["draft"]["leader"]
    while v["fase"] == "preparazione":
        offer = v["draft"]["offerta"]
        assert 1 <= len(offer) <= 3 and all(core.legale_per(leader, c) for c in offer)
        v = _api("/api/draft/scelta", {**a, "carta": offer[0]})
    st = server.REG.get(a["codice"])
    me = st.posti[0]
    assert not decks.problems(me.leader, me.carte)
    assert "partita" in v and v["giocatori"][1]["ia"]


def test_wrong_turn_and_stale_version_are_rejected():
    a = _api("/api/stanza", {"nome": "A", "modalita": "costruito", "contro_ia": True})
    m = core.dati().catalogo()["mazzi"][0]
    v = _api("/api/mazzo", {**a, "leader": m["leader"], "carte": m["carte"]})["partita"]
    code, _ = server.api("POST", "/api/azione", {}, {**a, "versione": v["versione"] + 1, "indice": 0})
    assert code == 400


def teardown_module():
    E.load_cards()          # the app loads the set into the engine: restore the default for the other tests


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
    teardown_module()
