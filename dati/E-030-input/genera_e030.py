"""E-030 (Q-026, esito della passata 2: questioni/Q-026_feedback_playtest/esito_passata2.md). Solo dati, nessuna regola nel codice.
Carte: B0c03 = tcg/set/esperimenti/E-025_B0c02/A-FV_c02/carte.json (non si tocca; identica a E-028_c04/00_B0c03).
Liste: B0c05 = tcg/swarm/questioni/Q-026_feedback_playtest/liste_B0c05/mazzi.json (6 liste rif_, 2 copie per nome; non si tocca).
Bracci: 00_B0c05 (riferimento), M2 (NEW-V05), M3 (NEW-B06), P-2c (leve di P, condizionale).
Se il critico corregge le liste B0c05: rilanciare  python3 -B genera_e030.py  e rivalidare.
"""
import copy, json, os
from collections import Counter
EXP = "/mnt/project-files/tcg/set/esperimenti"
CARTE = f"{EXP}/E-025_B0c02/A-FV_c02/carte.json"
LISTE = "/mnt/project-files/tcg/swarm/questioni/Q-026_feedback_playtest/liste_B0c05/mazzi.json"
LISTE_B0C03 = f"{EXP}/E-025_B0c02/A-FV_c02/mazzi.json"
OUT = os.path.dirname(os.path.abspath(__file__))
SET = json.load(open(CARTE, encoding="utf-8"))
MAZ = json.load(open(LISTE, encoding="utf-8"))
OLD = json.load(open(LISTE_B0C03, encoding="utf-8"))
L1, L4, L5, L6 = ("rif_LDR01_puntata_e_preda", "rif_LDR04_stanca_e_smonta", "rif_LDR05_scudi_armati",
                  "rif_LDR06_ferite_e_caccia")
CACCIA = ("Caccia *(quando attacca, puoi scegliere come bersaglio un'Unità avversaria, anche Ruotata, invece del Leader; "
          "l'avversario può ancora opporsi con un'altra Unità, che diventa il bersaglio)*.")

NEW_V05 = {
    "id": "NEW-V05", "name": "NEW-V05", "type": "tactic", "cost": 2, "colors": ["G"], "rarity": "R",
    "play": {"target": {"side": "opp", "ready": True, "keyword": "scudo"}, "do": [{"op": "stanca", "target": "chosen"}]},
    "text": "Stanca *(ruota)* un'Unità avversaria Pronta con Scudo.",
    "intent": "Q-026 M2: risposta verde allo Scudo senza tetto di costo (Thorn e LDR-06; misurata anche in LDR-01).",
    "_note": "E-030 M2 (Q-026, esito_passata2.md, 8/8). Rarità R dal voto; scala delle rarità di B0c03 non ancora rietichettata.",
}
NEW_B06 = {
    "id": "NEW-B06", "name": "NEW-B06", "type": "unit", "cost": 6, "colors": ["K", "G"], "rarity": "L", "power": 5,
    "keywords": ["caccia"],
    "abilities": [{"static": "power", "if": [{"attacking": True}, {"scars_ge": 3}], "value": 2}],
    "text": CACCIA + " Quando attacca, se hai almeno 3 Cicatrici, +2 in questo scontro.",
    "intent": "Q-026 M3: Leggendaria ponte N/V, chiusura a F7 per chi ha pagato Cicatrici.",
    "_note": "E-030 M3 (Q-026, esito_passata2.md, 8/8; variante a costo 7 respinta). Stessa forma di BLU-015 + VER-020.",
}


def card(s, cid):
    return next(c for c in s["cards"] if c["id"] == cid)


def deck(m, name):
    return next(d for d in m["mazzi"] if d["name"] == name)


def swap(m, name, out, inn):
    d = deck(m, name)
    for c in out:
        d["cards"].remove(c)          # ValueError se la lista corretta dal critico non ha più la carta: si riguarda la scelta
    d["cards"] += inn
    d["note"] = d.get("note", "") + f" E-030: −{', −'.join(out)}; +{', +'.join(inn)}."


# ------------------------------------------------------------------ leve
def M2(s, m):
    s["cards"].append(copy.deepcopy(NEW_V05))
    swap(m, L4, ["VER-012", "VER-002"], ["NEW-V05", "NEW-V05"])
    swap(m, L6, ["VER-013", "VER-013"], ["NEW-V05", "NEW-V05"])
    swap(m, L1, ["VER-013", "VER-013"], ["NEW-V05", "NEW-V05"])
    return ["Nuova carta `NEW-V05` (Tattica verde, costo 2, rarità R): `play` con bersaglio `{side: opp, ready: true, keyword: scudo}`, "
            "`stanca` sul bersaglio; nessun `cost_le`.",
            f"`{L4}`: −1 VER-012, −1 VER-002, +2 NEW-V05. Escono le due Stanca verdi più simili (Tattiche a bersaglio Pronta): "
            "VER-012 è la sola altra Stanca da 2; resta 1 VER-002 per la curva bassa.",
            f"`{L6}`: −2 VER-013, +2 NEW-V05. VER-013 (Stanca ≤3 da 2) è la sola Tattica di Stanca della lista ed è entrata in B0c05 al posto di NER-015.",
            f"`{L1}`: −2 VER-013, +2 NEW-V05. VER-013 ×2 sono entrate in B0c05 come riempitivi (sostituti di Reazioni gemelle G2) "
            "e sono le carte più simili; restano le 2 VER-002.",
            "Colori invariati in tutte e tre le liste (verde per verde); copie per nome ≤2."]


def M3(s, m):
    s["cards"].append(copy.deepcopy(NEW_B06))
    swap(m, L6, ["VER-023"], ["NEW-B06"])
    return ["Nuova carta `NEW-B06` (Unità N/V, costo 6, F5, Caccia, rarità L): statica `power +2` con `if: [attacking, scars_ge 3]` "
            "(stessa forma di BLU-015 e VER-020, il +2 vale solo quando attacca).",
            f"`{L6}`: −1 VER-023, +1 NEW-B06 (costo 6 per costo 6, come proposto dal designer ponti in round1). "
            "Colori: V −1, N/V +1 (la carta bicolore conta per entrambi)."]


def P(s, m):
    card(s, "NEU-013")["power"] = 2
    card(s, "NEU-013")["_note"] = (card(s, "NEU-013").get("_note", "") + " E-030 P-2c: Forza 3 → 2 (testo invariato).").strip()
    card(s, "BLU-008")["power"] = 1
    card(s, "BLU-008")["_note"] = (card(s, "BLU-008").get("_note", "") + " E-030 P-2c: Forza 2 → 1 (testo invariato).").strip()
    next(l for l in s["leaders"] if l["id"] == "LDR-05")["base"] = []
    d = deck(m, L5)
    return ["Le leve di P di E-029, identiche: NEU-013 Forza 3 → 2, BLU-008 Forza 2 → 1 (`power`, testo invariato); "
            "LDR-05 Base senza testo (`base: []`), Risvegliato invariato.",
            f"`{L5}` è quella di B0c05: NEU-013 ×{d['cards'].count('NEU-013')}, BLU-008 ×{d['cards'].count('BLU-008')} (in B0c03 erano ×3 e ×3)."]


# ------------------------------------------------------------------ traccia: quella di E-029 + Leader + carte nuove di B0c05 + NEW-*
BASETR = ("LDR-01,LDR-05,BLU-001,BLU-007,BLU-008,BLU-010,BLU-012,BLU-015,BLU-021,BLU-023,BLU-025,NEU-006,NEU-013,ROS-001,ROS-003,"
          "ROS-005,ROS-007,ROS-010,ROS-015,ROS-016,ROS-018,ROS-020,ROS-021,ROS-023,ROS-025,VER-001,VER-002,VER-009,VER-011,VER-019,VER-024")
base_ids = BASETR.split(",")
# carte entrate in B0c05: per ogni lista, gli ID che la stessa lista di B0c03 non aveva
entrate = sorted({c for d in MAZ["mazzi"] for c in d["cards"] if c not in deck(OLD, d["name"])["cards"]})
TRACCIA = ",".join(dict.fromkeys(base_ids + ["LDR-02", "LDR-03", "LDR-04", "LDR-06", "VER-012", "VER-013", "VER-023"] + entrate
                                 + ["NEW-V05", "NEW-B06"]))

ARMS = {  # nome: (leve, voto, protagonisti, incroci, ore, riferimento)
    "00_B0c05": ([], "riferimento B0c05 (V1, 2 copie per nome)", "tutti", 15, 10.8,
                 "—; anche IA semplice, 400 per incrocio, semi 2000+k (uscita S, ~0.2 h)"),
    "M2": ([M2], "M2, 8/8; LDR-01 su richiesta del critico (round1/discussione_critico.md)", "1,4,6", 12, 8.7,
           "E-030_q026/00_B0c05 F_s3400"),
    "M3": ([M3], "M3, 8/8 (costo 6, F5)", "6", 5, 3.6, "E-030_q026/00_B0c05 F_s3400"),
    "P-2c": ([P], "C: P rimisurata su B0c05 solo se lo screening di E-029 dà Δ05 ≤ −1.5 (condizionale)", "1,5", 9, 6.5,
             "E-030_q026/00_B0c05 F_s3400"),
}
for name, (levers, who, prot, inc, ore, ref) in ARMS.items():
    s, m = copy.deepcopy(SET), copy.deepcopy(MAZ)
    ch = [x for f in levers for x in f(s, m)]
    s["version"] = m["set"] = f"set_v02+E-030_{name}"
    s["note"] = SET["note"] + f" E-030 {name}: carte di B0c03 (E-025 A-FV_c02) con le sole leve del braccio (vedi LEGGIMI.md)."
    m["autore"], m["data"] = "programmatore (swarm)", "2026-10-26"
    m["nota"] = MAZ["nota"] + f" E-030 {name}: liste B0c05" + (" invariate." if name in ("00_B0c05", "P-2c") else ", modificate come in LEGGIMI.md.")
    p = os.path.join(OUT, name)
    os.makedirs(p, exist_ok=True)
    json.dump(s, open(f"{p}/carte.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(m, open(f"{p}/mazzi.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(f"{p}/traccia.txt", "w", encoding="utf-8").write(TRACCIA + "\n")
    cards = {c["id"]: c for c in s["cards"]}
    righe = []
    for d in m["mazzi"]:
        cnt = Counter(d["cards"])
        col = Counter(x for c, k in cnt.items() for x in cards[c]["colors"] for _ in range(k))
        righe.append(f"  - `{d['name']}`: {len(d['cards'])} carte, {sum(k for c, k in cnt.items() if cards[c]['type'] == 'unit')} Unità, "
                     f"{sum(k for c, k in cnt.items() if 'scudo' in cards[c].get('keywords', []))} Scudo, colori "
                     + " ".join(f"{x} {v}" for x, v in sorted(col.items())) + f", massimo copie {max(cnt.values())}.")
    sb = 3400
    open(f"{p}/LEGGIMI.md", "w", encoding="utf-8").write(
        f"# E-030_q026 / {name}\n\n- **Cosa cambia rispetto a B0c05 (carte B0c03 + liste B0c05):**\n"
        + "".join(f"  - {x}\n" for x in ch or ["nulla (riferimento)."])
        + f"- **Voto / ruolo:** {who}.\n- **Liste nel braccio:**\n" + "\n".join(righe) + "\n"
        + f"- **Si misura:** IA forte, 200 partite per incrocio, protagonisti `{prot}` ({inc} incroci), semi {sb}+k; contro {ref}.\n"
        + f"- **Comando:** `E030_TRACCIA=$(cat traccia.txt) bash ../lancia_e030.sh {name} forte:30 200 {sb} {prot}` "
        + f"(uscita `tcg/swarm/esperimenti/E-030_q026/{name}/F_s{sb}`), stima {ore} h su 4 core.\n"
        + "- **Regole:** `tcg/swarm/questioni/Q-026_feedback_playtest/esito_passata2.md`.\n")
    print(name, ch and ch[0][:60])
print("traccia:", TRACCIA)
