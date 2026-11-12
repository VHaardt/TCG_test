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
                assert any(ln.strip().startswith(f"{E.CARDS[cid].name} di P{d['side'] + 1}") for ln in st.partita["s"].log[n0:]), cid
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


# ---------------------------------------------------------------- R-026 (Q-027) nell'app
def _r026():
    """Carte di prova di Q-027 sul set del motore di test (l'app lo ricarica dopo, vedi _set_app)."""
    from tests import test_v02 as T
    E.load_cards()
    return T, T._q027_cards()


def _set_app():
    core._DATI.clear()
    core.dati()


def test_r026_each_way_to_pay_is_its_own_labelled_action():
    T, k = _r026()
    try:
        s = T._arena()
        s.p[0].brace, s.p[0].hand = 3, [k["I03"], k["I02"]]
        s.p[0].units = [E.Unit(900, "t_r6", True), E.Unit(901, "t_r6", True)]
        s.p[1].units = [E.Unit(910, T._card("_u2", cost=2, power=2), True)]
        lab = [core.etichetta(s, 0, a) for a in s.legal_actions() if a[0] == "play"]
        assert sorted(x["pagamento"] for x in lab if x["carta"] == k["I03"]) == \
            sorted(f"Stanca {s.describe(0, u)}" for u in (900, 901))
        sac = [x for x in lab if x["carta"] == k["I02"]]
        assert len(sac) == 2 and all(x["pagamento"].startswith("sacrifica ") for x in sac)
        assert all(x["paga"][0]["come"] == "sacrifica" and "paghi: sacrifica" in x["testo"] for x in sac)
        assert all(x["bersaglio"] == {"lato": "avv", "uid": 910} for x in lab)
    finally:
        _set_app()


def test_r026_recover_is_a_question_when_more_cards_qualify():
    T, k = _r026()
    try:
        a2, b2 = T._card("_a2", cost=2, power=2), T._card("_b2", cost=2, power=1)
        s = T._arena()
        s.log = []
        pl = s.p[0]
        pl.brace, pl.hand = 3, [k["I08"]]
        pl.discard = [a2, b2, T._card("_big5", cost=5, power=5)]
        pl.scars = [[c, False, "test"] for c in pl.life[:2]]
        act = ("play", k["I08"], None)
        extra, need = core.prova(s, act, [])
        assert need["tipo"] == "recupero" and sorted(need["cands"]) == sorted([a2, b2]) and need["default"] == a2
        assert need["fonte"] == k["I08"] and need["q"] == 0
        assert core.prova(s, act, [b2]) == ([], None)
        core.esegui_con_scelte(s, act, [b2])                    # non la scelta del motore: decide il giocatore
        assert pl.hand == [b2] and a2 in pl.discard and "riprende _b2" in " ".join(s.log)
        assert "trigger_target" not in vars(s) and "recover_choice" not in vars(s)
        assert any(e["t"] == "riprende" and e["carta"] == b2 and e["chi"] == "io" for e in core.eventi(s.log, 0, 0))
        pl.brace, pl.hand, pl.discard = 3, [k["I08"]], [a2, T._card("_big5", cost=5, power=5)]
        assert core.prova(s, act, []) == ([a2], None)            # una sola carta valida: niente domanda
    finally:
        _set_app()


def test_r026_free_reaction_shows_cost_0_and_counts():
    T, k = _r026()
    try:
        s = T._arena()
        s.p[0].units = [E.Unit(900, "t_r6", True)]
        s.p[1].units = [E.Unit(901, "t_r6", True)]
        s.p[1].guard, s.p[1].hand = 2, [k["I04"]]
        for a in (("attack", 900), ("oppose", 901), ("gems", 0)):
            s.step(a)
        lab = [core.etichetta(s, 1, a) for a in s.legal_actions() if a[2]]
        assert len(lab) == 1 and "(costo 0)" in lab[0]["testo"] and lab[0]["db"] == 9
        s.combat.d, s.combat.react = 0, (k["I04"], "hand")
        conto = core.conto_scontro(s, s.combat, 0, 0)
        assert conto["db"] == 9 and any(x["t"] == f"Reazione {k['I04']} (gratis)" for x in conto["dif"])
        assert sum(x["v"] for x in conto["dif"] if x["v"]) == conto["db"]
    finally:
        _set_app()


def test_q030_names_replace_ids_and_twins_share_the_copy_limit():
    d = core.dati()
    if not d.nomi:
        return                                      # nessuna mappa dei nomi: l'app mostra gli ID
    cat = d.catalogo()
    nomi = {c["id"]: c["nome"] for c in cat["carte"]}
    assert all(nomi[i] == d.nomi["carte"][i] for i in nomi if i in d.nomi["carte"])
    assert all(l["nome"] != l["id"] for l in cat["leader"])
    # gemelle Q-026 (gruppo 1: ROS-004, NER-005, VER-005): stesso nome, quindi stesso gruppo del limite di copie
    gem = [c for c in cat["carte"] if c["id"] in ("ROS-004", "NER-005", "VER-005")]
    if len(gem) == 3 and d.limiti["copies_by_name"]:
        assert len({c["gruppo"] for c in gem}) == 1
    # un nome diverso per ogni carta che non è gemella
    per_nome = {}
    for c in cat["carte"]:
        per_nome.setdefault(c["nome"], set()).add(c["testo"])
    assert all(len(t) == 1 for t in per_nome.values()), [n for n, t in per_nome.items() if len(t) > 1]
    # i problemi di costruzione nominano la carta, non l'ID
    probs = d.problemi("LDR-01", {"NER-001": 1})
    assert any(p.startswith(nomi["NER-001"] + ":") for p in probs), probs


def test_any_cost_menu_on_ner002_ner019_and_cycle04_names():
    """Ciclo 04: NER-002/NER-019 si pagano perdendo 1 Vita oppure Stancando una tua Unità Pronta (una voce per modo);
    le carte nuove hanno il nome di Q-029 e i mazzi di riferimento sono le liste rif_ a 2 copie del set."""
    d = core.dati()
    C = {c["id"]: c for c in d.catalogo()["carte"]}
    assert C["NEW-V05"]["nome"] != "NEW-V05" and C["NEW-B06"]["nome"] != "NEW-B06" and C["NEW-B06"]["max"] == 1
    assert all(m["nome"].startswith("rif_") for m in d.riferimento) and any("NEW-B06" in m["carte"] for m in d.riferimento)
    r0, r1 = d.riferimento[0], d.riferimento[1]
    L = lambda m: [c for c, k in m["carte"].items() for _ in range(k)]
    s = E.new_game(r0["leader"], L(r0), r1["leader"], L(r1), rules=d.rules, seed=1, log=True)
    s.round = 3
    q = s.active
    s.p[q].hand, s.p[q].brace = ["NER-002", "NER-019"], 6
    s.p[q].units = [E.Unit(950, "NEW-V05", True), E.Unit(951, "NEW-B06", False)]
    s.p[1 - q].units = [E.Unit(960, "NEW-V05", False)]
    for cid in ("NER-002", "NER-019"):
        pag = sorted(core.etichetta(s, q, a)["pagamento"] for a in s.legal_actions() if a[0] == "play" and a[1] == cid)
        assert pag == ["Stanca " + s.describe(q, 950), "perdi 1 Vita"], (cid, pag)    # solo le Unità Pronte


def test_q027_new_i04_free_reaction_only_with_no_gems_on_own_unit():
    """Q-027: NEW-I04 (costo 0) si offre solo quando il bersaglio è una tua Unità e impegni 0 gemme;
    nell'app risulta "costo 0" e il conto dello scontro la conta (gratis)."""
    d = core.dati()
    C = {c["id"]: c for c in d.catalogo()["carte"]}
    assert C["NEW-I04"]["nome"] != "NEW-I04" and C["NEW-I04"]["costo"] == 0
    r0, r1 = d.riferimento[0], d.riferimento[1]
    L = lambda m: [c for c, k in m["carte"].items() for _ in range(k)]

    def scontro(bersaglio):
        s = E.new_game(r0["leader"], L(r0), r1["leader"], L(r1), rules=d.rules, seed=3, log=True)
        s.round = 3
        a = s.active
        s.p[a].units = [E.Unit(900, "NEW-V05", True)]
        s.p[1 - a].units = [E.Unit(901, "NEW-V05", True)]
        s.p[1 - a].guard, s.p[1 - a].hand = 2, ["NEW-I04"]
        s.step(("attack", 900))
        if s.phase == "oppose":
            s.step(("oppose", 901) if bersaglio == "unita" else ("no_oppose",))
        s.step(("gems", 0))
        return s, 1 - a
    s, q = scontro("leader")
    assert not [x for x in s.legal_actions() if x[0] == "parry" and x[2]]          # bersaglio il Leader
    s, q = scontro("unita")
    con = [x for x in s.legal_actions() if x[0] == "parry" and x[2]]
    assert [x[1] for x in con] == [0]                                              # solo con 0 gemme
    lab = core.etichetta(s, q, con[0])
    assert "(costo 0)" in lab["testo"] and lab["carta"] == "NEW-I04"
    s.combat.d, s.combat.react = 0, None
    senza = core.conto_scontro(s, s.combat, 0, 0)
    s.combat.react = con[0][2]
    conto = core.conto_scontro(s, s.combat, 0, 0)
    assert any(x["t"] == "Reazione NEW-I04 (gratis)" for x in conto["dif"]) and conto["db"] == senza["db"] + 2


def test_log_events_find_cards_by_their_q029_names():
    """Il registro scrive i nomi (anche di più parole): ogni giocata, opposizione e Reazione diventa un evento
    con l'ID della carta, così il client può animarla."""
    import random
    d = core.dati()
    r0, r1 = d.riferimento[1], d.riferimento[3]
    L = lambda m: [c for c, k in m["carte"].items() for _ in range(k)]
    seen = {"gioca": 0, "scontro": 0}
    for seed in range(6):
        rng = random.Random(seed)
        s = E.new_game(r0["leader"], L(r0), r1["leader"], L(r1), rules=d.rules, seed=seed, log=True)
        for _ in range(3000):
            if s.over:
                break
            acts = s.legal_actions()
            core.passo(s, rng.choice([x for x in acts if x[0] != "end"] or acts))
        ev = {e["n"]: e for e in core.eventi(s.log, 0, 0)}
        for n, ln in enumerate(s.log):
            if " gioca " in ln and ln.startswith("  P"):
                assert ev[n]["t"] == "gioca" and ev[n]["carta"] in E.CARDS, ln
                seen["gioca"] += 1
            if "pugni:" in ln and " + " in ln:
                assert ev[n]["t"] == "scontro" and ev[n]["carta"] in E.CARDS, ln
                seen["scontro"] += 1
    assert seen["gioca"] and seen["scontro"], seen


def teardown_module():
    E.load_cards()          # the app loads the set into the engine: restore the default for the other tests


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
    teardown_module()
