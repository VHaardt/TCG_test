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
            if "mulligan" in v:
                if not v["mulligan"]["fatto"]:
                    _api("/api/mulligan", {"codice": code, "token": t, "carte": v["mulligan"]["mano"][:2]})
                continue
            if v.get("bersaglio"):
                if v["bersaglio"]["tuo"]:
                    _api("/api/bersaglio", {"codice": code, "token": t, "versione": v["versione"],
                                            "uid": v["bersaglio"]["cands"][-1]["uid"]})
                    break
                continue
            if v["tocca_a_te"]:
                acts = v["azioni"]
                pick = next((a for a in acts if a["gruppo"] != "turno"), acts[0])
                _api("/api/azione", {"codice": code, "token": t, "versione": v["versione"], "indice": pick["i"]})
                break
    raise AssertionError("partita non finita")


def test_catalogo_and_reference_decks_are_legal():
    cat = _api("/api/catalogo", method="GET")
    lim = decks.limits(core.dati().rules)
    assert cat["costruzione"]["carte"] == lim["deck_size"] and cat["costruzione"]["copie"] == lim["max_copies"]
    assert len(cat["leader"]) >= 2 and len(cat["carte"]) >= 40 and cat["mazzi"]
    for m in cat["mazzi"]:
        assert not core.dati().problemi(m["leader"], m["carte"])


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
    assert v["fase"] == "partita" and len(v["partita"]["mulligan"]["mano"]) == 5
    code, out = server.api("POST", "/api/mulligan", {}, {**a, "carte": ["XXX-999"]})
    assert code == 400
    _api("/api/mulligan", {**a, "carte": _api("/api/stato", a, "GET")["partita"]["mulligan"]["mano"][:3]})
    v = _api("/api/mulligan", {**b, "carte": []})
    # hidden information: no opponent hand, no Life cards
    assert "mano" in v["partita"]["io"] and "mano" not in v["partita"]["avversario"]
    p = _play_out(a["codice"], [a["token"], b["token"]])
    assert p[0]["fine"]["hai_vinto"] != p[1]["fine"]["hai_vinto"]
    v = _api("/api/rivincita", a)
    assert v["fase"] == "preparazione"


def test_v027_limits_two_copies_and_rarity():
    D = core.dati()
    assert D.limiti["max_copies"] == 2 and D.limiti["max_copies_rarity"].get("L") == 1
    assert len(D.riferimento) == 6 and all(max(m["carte"].values()) <= 2 for m in D.riferimento)
    m = D.riferimento[0]
    tre = dict(m["carte"]); cid = next(iter(tre)); tre[cid] = 3
    tre[next(c for c in tre if c != cid)] -= 1
    a = _api("/api/stanza", {"nome": "A", "modalita": "costruito"})
    code, out = server.api("POST", "/api/mazzo", {}, {**a, "leader": m["leader"], "carte": tre})
    assert code == 400 and "massimo 2" in out["errore"]
    # una Leggendaria vale 1 copia, anche nel draft
    D.info[cid] = (D.info[cid][0], "L")
    try:
        assert D.copie_max(cid) == 1
    finally:
        D.info[cid] = (D.info[cid][0], D.rarity.get(cid))


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
    assert not core.dati().problemi(me.leader, me.carte)
    assert max(me.carte.values()) <= core.dati().limiti["max_copies"]
    assert "partita" in v and v["giocatori"][1]["ia"]


def test_wrong_turn_and_stale_version_are_rejected():
    a = _api("/api/stanza", {"nome": "A", "modalita": "costruito", "contro_ia": True})
    m = core.dati().catalogo()["mazzi"][0]
    _api("/api/mazzo", {**a, "leader": m["leader"], "carte": m["carte"]})
    v = _api("/api/mulligan", {**a, "carte": []})["partita"]
    code, _ = server.api("POST", "/api/azione", {}, {**a, "versione": v["versione"] + 1, "indice": 0})
    assert code == 400


def test_mulligan_puts_cards_at_the_bottom_and_redraws():
    a = _api("/api/stanza", {"nome": "A", "modalita": "costruito", "contro_ia": True})
    m = core.dati().catalogo()["mazzi"][0]
    mano = _api("/api/mazzo", {**a, "leader": m["leader"], "carte": m["carte"]})["partita"]["mulligan"]["mano"]
    _api("/api/mulligan", {**a, "carte": mano[:3]})
    st = server.REG.get(a["codice"])
    s, q = st.partita["s"], st.q_di(0)
    assert s.p[q].deck[:3] == list(reversed(mano[:3]))         # in fondo al mazzo
    assert all(c in s.p[q].hand for c in mano[3:])


def test_trigger_targets_are_asked_and_applied():
    """Players answer every trigger with several targets; the chosen Unit is the one affected."""
    import random
    rng = random.Random(7)
    asked = 0
    for g in range(40):
        a = _api("/api/stanza", {"nome": "A", "modalita": "costruito", "contro_ia": True})
        mz = core.dati().catalogo()["mazzi"]
        m = mz[g % len(mz)]
        _api("/api/mazzo", {**a, "leader": m["leader"], "carte": m["carte"]})
        _api("/api/mulligan", {**a, "carte": []})
        st = server.REG.get(a["codice"])
        for _ in range(3000):
            v = _api("/api/stato", a, "GET")["partita"]
            if "fine" in v:
                break
            if v.get("bersaglio"):
                d = st.partita["attesa"]["domanda"]
                alt = next(u for u in d["cands"] if u != d["default"])
                cid = st.partita["s"].unit(d["side"], alt).cid
                n0 = len(st.partita["s"].log)
                _api("/api/bersaglio", {**a, "versione": v["versione"], "uid": alt})
                assert any(ln.strip().startswith(f"{cid} di P{d['side'] + 1}") for ln in st.partita["s"].log[n0:]), cid
                asked += 1
                continue
            _api("/api/azione", {**a, "versione": v["versione"], "indice": rng.choice(v["azioni"])["i"]})
        if asked >= 3:
            break
    assert asked >= 3


def test_premade_decks_mode():
    a = _api("/api/stanza", {"nome": "A", "modalita": "pronti"})
    b = _api("/api/entra", {"nome": "B", "codice": a["codice"]})
    mz = core.dati().catalogo()["mazzi"]
    code, out = server.api("POST", "/api/mazzo", {}, {**a, "leader": mz[0]["leader"], "carte": mz[0]["carte"]})
    assert code == 400
    code, out = server.api("POST", "/api/mazzo/pronto", {}, {**a, "nome": "non esiste"})
    assert code == 400
    _api("/api/mazzo/pronto", {**a, "nome": mz[0]["nome"]})
    _api("/api/mazzo/annulla", a)
    _api("/api/mazzo/pronto", {**a, "nome": mz[2]["nome"]})
    v = _api("/api/mazzo/pronto", {**b, "nome": mz[1]["nome"]})
    assert v["fase"] == "partita"
    st = server.REG.get(a["codice"])
    assert st.posti[0].carte == mz[2]["carte"] and st.posti[1].leader == mz[1]["leader"]
    ia = _api("/api/stanza", {"nome": "C", "modalita": "pronti", "contro_ia": True})
    v = _api("/api/mazzo/pronto", {**ia, "nome": mz[3]["nome"]})
    assert v["fase"] == "partita"


def test_hits_that_take_no_life_say_why():
    """§9.2-9.5: every attack on the Leader with Fa >= Db takes a Life, wins, or the log says why not."""
    import random, re
    rx = re.compile(r"-> (-?\d+) contro (-?\d+)")
    told = 0
    for seed in range(60):
        rng = random.Random(seed)
        L = lambda m: [c for c, k in m["carte"].items() for _ in range(k)]
        a, b = rng.choice(core.dati().riferimento), rng.choice(core.dati().riferimento)
        s = E.new_game(a["leader"], L(a), b["leader"], L(b), rules=core.dati().rules, seed=seed, log=True)
        for _ in range(4000):
            if s.over:
                break
            acts = s.legal_actions()
            pool = [x for x in acts if x[0] != "end_turn"] if rng.random() < .85 else acts
            core.passo(s, rng.choice(pool or acts))
        log = s.log
        for n, ln in enumerate(log):
            m = rx.search(ln)
            if not m or int(m[1]) < int(m[2]) or "oppone" in log[n - 1] or "(Caccia" in log[n - 1]:
                continue
            nxt = log[n + 1] if n + 1 < len(log) else ""
            assert "perde 1 Vita" in nxt or "non perde Vite" in nxt or nxt.startswith("***"), (seed, ln, nxt)
            told += "non perde Vite" in nxt
    assert told > 0


def test_undo_own_choice_until_something_is_revealed():
    import random
    rng = random.Random(3)
    undone = 0
    for g in range(30):
        a = _api("/api/stanza", {"nome": "A", "modalita": "pronti", "contro_ia": True})
        mz = core.dati().catalogo()["mazzi"]
        _api("/api/mazzo/pronto", {**a, "nome": mz[g % len(mz)]["nome"]})
        _api("/api/mulligan", {**a, "carte": []})
        st = server.REG.get(a["codice"])
        for _ in range(400):
            v = _api("/api/stato", a, "GET")["partita"]
            if "fine" in v or undone >= 5:
                break
            if v.get("bersaglio"):
                _api("/api/bersaglio", {**a, "versione": v["versione"], "uid": v["bersaglio"]["cands"][0]["uid"]})
                continue
            s0 = st.partita["s"]
            before = (list(s0.p[0].hand), list(s0.p[1].hand), [u.uid for p in s0.p for u in p.units],
                      [p.brace for p in s0.p], s0.phase)
            act = rng.choice(v["azioni"])
            v2 = _api("/api/azione", {**a, "versione": v["versione"], "indice": act["i"]})["partita"]
            if v2.get("puoi_annullare") and rng.random() < .5:
                v3 = _api("/api/annulla", a)["partita"]
                s1 = st.partita["s"]
                assert (list(s1.p[0].hand), list(s1.p[1].hand), [u.uid for p in s1.p for u in p.units],
                        [p.brace for p in s1.p], s1.phase) == before
                assert v3["versione"] > v2["versione"] and "torna indietro" in s1.log[-1]
                undone += 1
    assert undone >= 5
    # contro un umano: dopo una sua scelta non si torna indietro
    a = _api("/api/stanza", {"nome": "A", "modalita": "pronti"})
    b = _api("/api/entra", {"nome": "B", "codice": a["codice"]})
    _api("/api/mazzo/pronto", {**a, "nome": mz[0]["nome"]})
    _api("/api/mazzo/pronto", {**b, "nome": mz[1]["nome"]})
    _api("/api/mulligan", {**a, "carte": []})
    _api("/api/mulligan", {**b, "carte": []})
    st = server.REG.get(a["codice"])
    for _ in range(200):
        va, vb = (_api("/api/stato", t, "GET")["partita"] for t in (a, b))
        me, other, v = (a, b, va) if va["tocca_a_te"] else (b, a, vb)
        if st.annullabile(st.posti.index(next(p for p in st.posti if p.token == other["token"]))):
            break
        if v.get("bersaglio"):
            _api("/api/bersaglio", {**me, "versione": v["versione"], "uid": v["bersaglio"]["cands"][0]["uid"]})
        else:
            pick = next((x for x in v["azioni"] if x["gruppo"] != "turno"), v["azioni"][0])
            _api("/api/azione", {**me, "versione": v["versione"], "indice": pick["i"]})
    i_other = next(k for k, p in enumerate(st.posti) if p.token == other["token"])
    assert st.annullabile(i_other)
    v = _api("/api/stato", me, "GET")["partita"]
    if v["tocca_a_te"] and not v.get("bersaglio"):
        _api("/api/azione", {**me, "versione": v["versione"], "indice": v["azioni"][0]["i"]})
        assert not st.annullabile(i_other)


def test_live_modifiers_add_up():
    import random
    rng = random.Random(5)
    seen = combats = 0
    for g in range(25):
        a = _api("/api/stanza", {"nome": "A", "modalita": "pronti", "contro_ia": True})
        mz = core.dati().catalogo()["mazzi"]
        _api("/api/mazzo/pronto", {**a, "nome": mz[g % len(mz)]["nome"]})
        _api("/api/mulligan", {**a, "carte": []})
        for _ in range(500):
            v = _api("/api/stato", a, "GET")["partita"]
            if "fine" in v:
                break
            for side in ("io", "avversario"):
                for u in v[side]["unita"]:
                    assert u["forza_stampata"] + sum(m["v"] for m in u["mod"] if not m.get("scontro")) == u["forza"]
                    seen += bool(u["mod"])
            c = (v["combattimento"] or {}).get("conto")
            if c:
                combats += 1
                assert sum(x["v"] for x in c["att"]) == c["fa"]
                assert sum(x["v"] or 0 for x in c["dif"]) == c["db"]
            if v.get("bersaglio"):
                _api("/api/bersaglio", {**a, "versione": v["versione"], "uid": v["bersaglio"]["cands"][0]["uid"]})
            elif v["tocca_a_te"]:
                pool = [x for x in v["azioni"] if x["gruppo"] != "turno"] if rng.random() < .8 else v["azioni"]
                _api("/api/azione", {**a, "versione": v["versione"], "indice": rng.choice(pool or v["azioni"])["i"]})
    assert seen > 0 and combats > 0


def teardown_module():
    E.load_cards()          # the app loads the set into the engine: restore the default for the other tests


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
    teardown_module()
