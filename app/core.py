"""Logica dell'app online di CICATRICI: dati, costruzione del mazzo, draft, stanze e viste.

Il motore è sim/v02 usato come libreria: l'app non contiene regole del gioco.
- Carte e Leader: il file del set (CICATRICI_SET, poi la cartella condivisa, poi app/dati).
- Regole: un preset di sim/v02/config.py o un file json di variante (CICATRICI_REGOLE).
- Costruzione: sim/v02/decks.problems (40 carte, 3 copie per ID, colori del Leader o Neutrali).
Ogni azione mostrata al giocatore è un elemento di GameState.legal_actions()."""
import json
import os
import random
import re
import secrets
import string
import threading
import time

from sim.v02 import engine, decks
from sim.v02.config import PRESETS, rules_from
from sim.v02.engine import CARDS, LEADERS, G1, G2

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = "/mnt/project-files/tcg/set/finale"
COLORI = {"R": "Rosso", "B": "Blu", "K": "Nero", "G": "Verde"}
TIPI = {"unit": "Unità", "tactic": "Tattica", "reaction": "Reazione", "relic": "Reliquia"}
FASI = {
    "main": "Fase principale",
    "impeto": "L'attaccante impegna le gemme a vista",
    "risposta": "Il difensore risponde",
    "oppose": "Il difensore può opporre un'Unità Pronta",
    "pugno_att": "L'attaccante impegna le gemme (Brace)",
    "pugno_def": "Il difensore impegna la Guardia (Parata e Reazione)",
    "oppose_after": "Il difensore può opporre un'Unità",
}
FINE = {"colpo_finale": "colpo finale", "crepuscolo": "Crepuscolo", "non_conclusa": "partita non conclusa",
        "mazzo_vuoto": "mazzo finito", "resa": "resa"}
DRAFT_OFFERTA = 3
DRAFT_RARITA = (("C", 0.6), ("NC", 0.3), ("R", 0.1))     # come l'Arena: le 3 carte di una scelta hanno la stessa rarità


def _first(*paths):
    for p in paths:
        if p and os.path.exists(p):
            return p
    return None


class Dati:
    """Set, regole e mazzi di riferimento caricati all'avvio del server."""

    def __init__(self):
        self.set_path = _first(os.environ.get("CICATRICI_SET"), os.path.join(SHARED, "set_v02.json"),
                               os.path.join(HERE, "dati", "set_v02.json"))
        self.mazzi_path = _first(os.environ.get("CICATRICI_MAZZI"), os.path.join(SHARED, "mazzi_v02.json"),
                                 os.path.join(HERE, "dati", "mazzi_v02.json"))
        spec = os.environ.get("CICATRICI_REGOLE")
        if not spec:
            spec = "V026" if "V026" in PRESETS else os.path.join(HERE, "dati", "regole_V026.json")
        self.regole_spec = spec
        self.rules = rules_from(spec)
        engine.load_cards(self.set_path)
        with open(self.set_path, encoding="utf-8") as f:
            raw = json.load(f)
        self.set_info = {k: raw.get(k) for k in ("version", "rules", "data")}
        self.rarity = {c["id"]: c.get("rarity") for c in raw["cards"]}
        self.riferimento = []
        if self.mazzi_path:
            with open(self.mazzi_path, encoding="utf-8") as f:
                for m in json.load(f).get("mazzi", []):
                    cards = {}
                    for cid in m["cards"]:
                        cards[cid] = cards.get(cid, 0) + 1
                    if not decks.problems(m["leader"], cards):
                        self.riferimento.append({"nome": m["name"], "leader": m["leader"], "carte": cards,
                                                 "note": m.get("note", "")})

    def catalogo(self):
        r = self.rules
        return {
            "set": self.set_info, "set_file": os.path.relpath(self.set_path, HERE) if self.set_path.startswith(HERE)
            else self.set_path, "regole": os.path.basename(str(self.regole_spec)),
            "costruzione": {"carte": decks.DECK_SIZE, "copie": decks.MAX_COPIES},
            "colori": COLORI,
            "leader": [leader_dict(l) for l in LEADERS.values()],
            "carte": [card_dict(c, self.rarity.get(c.id)) for c in sorted(CARDS.values(), key=sort_key)],
            "mazzi": self.riferimento,
            "valori_leader": {"forza": r.leader_power, "forza_risvegliato": r.leader_power_awakened,
                              "tempra": r.tempra, "vite": r.life, "guardia_max": r.guard_max,
                              "guardia_max_risvegliato": r.guard_max_awakened, "risveglio_a_vite": r.awaken_at_life},
        }


def sort_key(c):
    return (c.colors[0] if c.colors else "Z", c.id)


def card_dict(c, rarity=None):
    return {"id": c.id, "nome": c.name, "tipo": TIPI.get(c.type, c.type), "costo": c.cost,
            "colori": list(c.colors), "forza": c.power if c.type == "unit" else None,
            "parole": sorted(c.keywords), "testo": c.text, "rarita": rarity}


def leader_dict(l):
    def texts(side):
        return [ab.get("text", "") for ab in side if ab.get("text")]
    return {"id": l.id, "nome": l.name, "colori": list(l.colors), "base": texts(l.base),
            "risvegliato": texts(l.awakened)}


def legale_per(leader, cid):
    cols = CARDS[cid].colors
    return not cols or bool(set(cols) & set(LEADERS[leader].colors))


# ---------------------------------------------------------------------------- draft
class Draft:
    """Arena: 3 Leader fra cui sceglierne uno, poi 40 scelte di 1 carta su 3 fra le carte legali."""

    def __init__(self, rng):
        self.rng = rng
        ids = sorted(LEADERS)
        self.leader_offerta = rng.sample(ids, min(DRAFT_OFFERTA, len(ids)))
        self.leader = None
        self.carte = {}
        self.offerta = []

    def scegli_leader(self, lid):
        if self.leader or lid not in self.leader_offerta:
            raise ValueError("Leader non offerto")
        self.leader = lid
        self._nuova_offerta()

    def _nuova_offerta(self):
        if self.completo:
            self.offerta = []
            return
        pool = [cid for cid in sorted(CARDS) if legale_per(self.leader, cid)
                and self.carte.get(cid, 0) < decks.MAX_COPIES]
        rarities = [r for r, _ in DRAFT_RARITA]
        rar = self.rng.choices(rarities, weights=[w for _, w in DRAFT_RARITA])[0]
        same = [cid for cid in pool if dati().rarity.get(cid) == rar]
        src = same if len(same) >= DRAFT_OFFERTA else pool
        self.offerta = self.rng.sample(src, min(DRAFT_OFFERTA, len(src)))

    def scegli(self, cid):
        if cid not in self.offerta:
            raise ValueError("carta non offerta")
        self.carte[cid] = self.carte.get(cid, 0) + 1
        self._nuova_offerta()

    @property
    def scelte(self):
        return sum(self.carte.values())

    @property
    def completo(self):
        return self.scelte >= decks.DECK_SIZE

    def auto(self):
        """Draft dell'IA: scelte a caso."""
        if not self.leader:
            self.scegli_leader(self.rng.choice(self.leader_offerta))
        while not self.completo:
            self.scegli(self.rng.choice(self.offerta))

    def vista(self):
        return {"leader_offerta": self.leader_offerta, "leader": self.leader, "carte": self.carte,
                "offerta": self.offerta, "scelte": self.scelte, "totale": decks.DECK_SIZE}


# ---------------------------------------------------------------------------- stanze
class Posto:
    def __init__(self, nome, ia=False):
        self.nome = nome
        self.token = secrets.token_urlsafe(16)
        self.ia = ia
        self.leader = None
        self.carte = None
        self.pronto = False
        self.draft = None


class Stanza:
    def __init__(self, modalita, nome, contro_ia=False):
        if modalita not in ("costruito", "draft"):
            raise ValueError("modalità sconosciuta")
        dati()
        self.codice = None
        self.modalita = modalita
        self.lock = threading.RLock()
        self.rng = random.Random(secrets.randbits(64))
        self.posti = [Posto(nome)]
        self.partita = None
        self.agente = None
        self.n_partita = 0
        self.ultimo = time.time()
        if contro_ia:
            ia = Posto("IA", ia=True)
            self.posti.append(ia)
        self._prepara()

    # preparation -------------------------------------------------------
    def _prepara(self):
        for p in self.posti:
            p.pronto = False
            if self.modalita == "draft":
                p.draft = Draft(random.Random(self.rng.random()))
                p.leader, p.carte = None, None
            if p.ia:
                self._prepara_ia(p)

    def _prepara_ia(self, p):
        if self.modalita == "draft":
            p.draft.auto()
            p.leader, p.carte = p.draft.leader, dict(p.draft.carte)
        else:
            m = self.rng.choice(dati().riferimento)
            p.leader, p.carte = m["leader"], dict(m["carte"])
        p.pronto = True

    def entra(self, nome):
        if len(self.posti) >= 2:
            raise ValueError("la stanza è piena")
        p = Posto(nome)
        if self.modalita == "draft":
            p.draft = Draft(random.Random(self.rng.random()))
        self.posti.append(p)
        return p

    def posto(self, token):
        for i, p in enumerate(self.posti):
            if p.token == token:
                return i, p
        raise PermissionError("giocatore sconosciuto in questa stanza")

    def imposta_mazzo(self, i, leader, carte):
        if self.partita:
            raise ValueError("partita in corso")
        if self.modalita != "costruito":
            raise ValueError("in modalità draft il mazzo nasce dal draft")
        carte = {cid: int(k) for cid, k in (carte or {}).items() if int(k) > 0}
        pr = decks.problems(leader, carte)
        if pr:
            raise ValueError("mazzo illegale: " + "; ".join(pr))
        p = self.posti[i]
        p.leader, p.carte, p.pronto = leader, carte, True
        self._forse_inizia()

    def annulla_pronto(self, i):
        if not self.partita and self.modalita == "costruito":
            self.posti[i].pronto = False

    def draft_leader(self, i, lid):
        self.posti[i].draft.scegli_leader(lid)

    def draft_scelta(self, i, cid):
        p = self.posti[i]
        p.draft.scegli(cid)
        if p.draft.completo:
            p.leader, p.carte, p.pronto = p.draft.leader, dict(p.draft.carte), True
            self._forse_inizia()

    def _forse_inizia(self):
        if len(self.posti) == 2 and all(p.pronto for p in self.posti) and not self.partita:
            self.inizia()

    def inizia(self):
        first = self.rng.randrange(2)                       # chi è G1 si tira a sorte
        seats = [first, 1 - first]                          # seats[q] = indice del posto che gioca come q
        mazzi = [(self.posti[i].leader, [cid for cid, k in self.posti[i].carte.items() for _ in range(k)])
                 for i in seats]
        s = engine.new_game(mazzi[0][0], mazzi[0][1], mazzi[1][0], mazzi[1][1], rules=dati().rules,
                            seed=self.rng.randrange(1 << 30), log=True)
        self.partita = {"s": s, "seats": seats, "versione": 0}
        self.n_partita += 1
        if any(p.ia for p in self.posti):
            from sim.v02.agents import RuleAgent2
            self.agente = RuleAgent2(seed=self.rng.randrange(1 << 30))
        self._turni_ia()

    def q_di(self, i):
        return self.partita["seats"].index(i)

    def azione(self, i, versione, indice):
        m = self.partita
        if not m:
            raise ValueError("nessuna partita in corso")
        if versione != m["versione"]:
            raise ValueError("stato cambiato, aggiorna")
        s = m["s"]
        if s.over or s.decider() != self.q_di(i):
            raise ValueError("non è il tuo turno di decidere")
        acts = s.legal_actions()
        if not 0 <= indice < len(acts):
            raise ValueError("azione non valida")
        s.step(acts[indice])
        m["versione"] += 1
        self._turni_ia()

    def _turni_ia(self):
        m = self.partita
        s = m["s"]
        for _ in range(2000):
            if s.over:
                return
            q = s.decider()
            if not self.posti[m["seats"][q]].ia:
                return
            s.step(self.agente.act(s))
            m["versione"] += 1

    def resa(self, i):
        s = self.partita["s"]
        if not s.over:
            s.lose(self.q_di(i), "resa")
            self.partita["versione"] += 1

    def rivincita(self):
        if self.partita and not self.partita["s"].over:
            raise ValueError("la partita non è finita")
        self.partita = None
        self._prepara()

    # views -------------------------------------------------------------
    def vista(self, i):
        self.ultimo = time.time()
        me = self.posti[i]
        out = {"codice": self.codice, "modalita": self.modalita, "io": i,
               "giocatori": [{"nome": p.nome, "ia": p.ia, "pronto": p.pronto} for p in self.posti],
               "fase": "partita" if self.partita else "preparazione", "n_partita": self.n_partita}
        if me.draft and not self.partita:
            out["draft"] = me.draft.vista()
        if not self.partita and self.modalita == "costruito" and me.carte:
            out["mio_mazzo"] = {"leader": me.leader, "carte": me.carte}
        if self.partita:
            out["partita"] = vista_partita(self, i)
        return out


def _nomi(stanza):
    seats = stanza.partita["seats"]
    return [stanza.posti[seats[q]].nome for q in (G1, G2)]


def vista_partita(stanza, i):
    m = stanza.partita
    s = m["s"]
    q = stanza.q_di(i)
    nomi = _nomi(stanza)
    dec = s.decider()
    out = {
        "versione": m["versione"], "round": s.round, "fase": s.phase, "fase_testo": FASI.get(s.phase, s.phase),
        "sei": "G1" if q == G1 else "G2", "attivo_sei_tu": s.active == q, "tocca_a_te": dec == q,
        "decide": nomi[dec] if dec is not None else None,
        "io": vista_giocatore(s, q, True), "avversario": vista_giocatore(s, 1 - q, False),
        "nomi": {"io": nomi[q], "avversario": nomi[1 - q]},
        "combattimento": vista_scontro(s, q), "azioni": [], "log": tradotto(s.log[-80:], nomi),
        "regole": {"saldo": s.saldo_cap(), "crepuscolo": s.r.crepuscolo_round, "round_max": s.r.max_rounds},
    }
    if s.over:
        out["fine"] = {"vincitore": None if s.winner is None else nomi[s.winner],
                       "hai_vinto": s.winner == q, "motivo": FINE.get(s.end_reason, s.end_reason)}
    elif dec == q:
        out["azioni"] = [{"i": k, **etichetta(s, q, a)} for k, a in enumerate(s.legal_actions())]
    return out


def tradotto(lines, nomi):
    return [re.sub(r"\bP([12])\b", lambda mm: nomi[int(mm.group(1)) - 1], ln) for ln in lines]


def vista_giocatore(s, q, mio):
    pl = s.p[q]
    lid = pl.leader
    out = {
        "leader": {"id": lid, "colori": list(LEADERS[lid].colors), "risvegliato": pl.awakened,
                   "pronto": pl.l_ready, "forza": s.leader_power(q), "tempra": s.tempra(q)},
        "vite": len(pl.life), "alle_corde": s.alle_corde(q), "brace": pl.brace, "guardia": pl.guard,
        "guardia_max": s.guard_max(q), "mazzo": len(pl.deck), "mano_n": len(pl.hand),
        "cicatrici": [{"id": sc[0], "fresca": bool(sc[1])} for sc in pl.scars],
        "unita": [{"uid": u.uid, "id": u.cid, "pronta": u.ready, "forza": s.unit_power(q, u, outside=True),
                   "forza_stampata": CARDS[u.cid].power} for u in pl.units],
        "reliquie": list(pl.relics), "scarti": list(pl.discard),
    }
    if mio:
        out["mano"] = list(pl.hand)
    return out


def vista_scontro(s, q):
    cb = s.combat
    if cb is None or s.phase == "main":
        return None
    a = s.active
    tgt = cb.target()
    visibile = cb.a is not None and (cb.a_visible or q == a)
    return {"attaccante": s.describe(a, cb.att), "attacca_tu": q == a,
            "bersaglio": s.describe(1 - a, tgt) if tgt is not None else "Leader",
            "opposta_da": s.describe(1 - a, cb.opposer) if cb.opposer is not None else None,
            "gemme_attacco": cb.a if visibile else None}


def _forza_su(s, a_gems, d_gems=0, react=None):
    try:
        fa, db, _ = s.compute(a_gems, d_gems, react, "current")
        return fa, db
    except Exception:           # anteprima: mai bloccare l'azione
        return None, None


def etichetta(s, q, act):
    """Testo leggibile di un'azione legale, con il gruppo per l'interfaccia."""
    k = act[0]
    a = s.active
    if k == "end":
        return {"gruppo": "turno", "testo": "Fine del turno"}
    if k == "play":
        c = CARDS[act[1]]
        t = ""
        if act[2] is not None:
            sel = (c.play or {}).get("target") or {}
            owner = q if sel.get("side", "own") == "own" else 1 - q
            t = f" → {'tua' if owner == q else 'avversaria'} {s.describe(owner, act[2])}"
        return {"gruppo": "gioca", "testo": f"Gioca {c.name} ({c.cost} Brace){t}", "carta": c.id}
    if k == "rim":
        return {"gruppo": "rimargina", "testo": f"Rimargina {act[1]}: ruota il Leader, {s.modifier(q, 'rim_cost', 1)} Brace, la carta torna in mano",
                "carta": act[1]}
    if k == "ability":
        src, idx, t = act[1], act[2], act[3]
        if src == "L":
            ab = s.leader_abilities(q)[idx]
            who = "Leader"
        else:
            u = s.unit(q, src)
            ab = CARDS[u.cid].abilities[idx]
            who = s.describe(q, src)
        tt = ""
        if t is not None:
            sel = ab.get("target") or {}
            owner = q if sel.get("side", "own") == "own" else 1 - q
            tt = f" → {'tua' if owner == q else 'avversaria'} {s.describe(owner, t)}"
        return {"gruppo": "abilita", "testo": f"⟳ {who} ({ab.get('cost', 0)} Brace){tt}"
                + (f": {ab['text']}" if ab.get("text") else "")}
    if k == "attack":
        t = f" (Caccia: {s.describe(1 - q, act[2])})" if len(act) > 2 else " il Leader avversario"
        return {"gruppo": "attacca", "testo": f"Attacca con {s.describe(q, act[1])}{t}"}
    if k == "gems":
        fa, db = _forza_su(s, act[1])
        extra = f" → Forza d'attacco {fa} contro difesa {db} senza Parata" if fa is not None else ""
        return {"gruppo": "gemme", "testo": f"Impegna {act[1]} gemme{extra}"}
    if k == "no_oppose":
        return {"gruppo": "opposizione", "testo": "Non opporti"}
    if k == "oppose":
        u = s.unit(q, act[1])
        return {"gruppo": "opposizione",
                "testo": f"Opponi {s.describe(q, act[1])} (Forza {s.unit_power(q, u, outside=True)})"}
    if k == "parry":
        gems, react = act[1], act[2]
        txt = f"Impegna {gems} gemme di Guardia"
        if react:
            cid, src = react
            txt += f" con la Reazione {cid} {'dalla mano' if src == 'hand' else 'dalle Cicatrici'} (costo {max(CARDS[cid].cost, 1)})"
        cb = s.combat
        if cb.a is not None and (cb.a_visible or q == a):
            fa, db = _forza_su(s, cb.a, gems, react)
            if fa is not None:
                txt += f" → attacco {fa} contro difesa {db}"
        return {"gruppo": "parata", "testo": txt, "carta": react[0] if react else None}
    return {"gruppo": "altro", "testo": str(act)}


# ---------------------------------------------------------------------------- registry
class Registro:
    DURATA = 6 * 3600

    def __init__(self):
        self.stanze = {}
        self.lock = threading.Lock()

    def crea(self, modalita, nome, contro_ia=False):
        st = Stanza(modalita, nome, contro_ia)
        with self.lock:
            self._pulisci()
            while True:
                code = "".join(random.choice(string.ascii_uppercase) for _ in range(5))
                if code not in self.stanze:
                    break
            st.codice = code
            self.stanze[code] = st
        return st

    def get(self, code):
        st = self.stanze.get((code or "").strip().upper())
        if not st:
            raise KeyError("stanza inesistente o scaduta")
        return st

    def _pulisci(self):
        now = time.time()
        for c in [c for c, st in self.stanze.items() if now - st.ultimo > self.DURATA]:
            del self.stanze[c]


_DATI = []


def dati():
    """Set, regole e mazzi, caricati alla prima chiamata (carica le carte nel motore)."""
    if not _DATI:
        _DATI.append(Dati())
    return _DATI[0]
