"""E-029 (ciclo 04, misura X votata 8/8: round1/punti_passata2.md punto 1). Solo dati, nessuna regola nel codice.
Base B0c03 = tcg/set/esperimenti/E-025_B0c02/A-FV_c02/ (non si tocca). Bracci: 00_B0c03, P, P-rott, D05b-200, D-2M.
  python3 -B genera_e029.py
"""
import copy, json, os, re
from collections import Counter
EXP = "/mnt/project-files/tcg/set/esperimenti"
BASE = f"{EXP}/E-025_B0c02/A-FV_c02"
D05B_SRC = f"{EXP}/E-025_B0c02/D05b_c02/carte.json"          # copie D05B-* già usate in E-025 (stesse carte di B0c03)
OUT = os.path.dirname(os.path.abspath(__file__))
SET = json.load(open(f"{BASE}/carte.json", encoding="utf-8"))
MAZ = json.load(open(f"{BASE}/mazzi.json", encoding="utf-8"))
L05 = "rif_LDR05_scudi_armati"
RE_SCUDO = re.compile(r"Scudo \*\([^)]*\)\*\.\s*")
RE_IMPETO = re.compile(r"Impeto \d+: \+\d+ \*\([^)]*\)\*\.\s*")


def card(s, cid):
    return next(c for c in s["cards"] if c["id"] == cid)


def deck(m):
    return next(d for d in m["mazzi"] if d["name"] == L05)


def is_impeto_ab(ab):
    """L'abilità di Impeto: statica di Forza sulla carta stessa, condizionata solo dalle gemme (pugno_ge)."""
    return (ab.get("static") == "power" and "applies_to" not in ab
            and [list(x) for x in ab.get("if", [])] == [["pugno_ge"]])


# ------------------------------------------------------------------ leve e diagnostici
def P(s, m):
    card(s, "NEU-013")["power"] = 2
    card(s, "NEU-013")["_note"] = (card(s, "NEU-013").get("_note", "") + " E-029 P: Forza 3 → 2 (testo invariato).").strip()
    card(s, "BLU-008")["power"] = 1
    card(s, "BLU-008")["_note"] = (card(s, "BLU-008").get("_note", "") + " E-029 P: Forza 2 → 1 (testo invariato).").strip()
    next(l for l in s["leaders"] if l["id"] == "LDR-05")["base"] = []
    return ["NEU-013: Forza 3 → 2 (`power`), testo invariato.",
            "BLU-008: Forza 2 → 1 (`power`), testo invariato.",
            "LDR-05: Base senza testo (`base: []`); Risvegliato invariato."]


def PROTT(s, m):
    d = deck(m)
    for cid in ["NEU-013"] * 3 + ["BLU-008"] * 3:
        d["cards"].remove(cid)
    d["cards"] += ["ROS-003", "ROS-003", "ROS-021", "BLU-012", "BLU-010", "BLU-001"]
    return [f"Lista `{L05}` (rottura del competitivo): −3 NEU-013, −3 BLU-008, +2 ROS-003 (0 → 2), +1 ROS-021 (2 → 3), "
            "+1 BLU-012 (2 → 3), +1 BLU-010 (2 → 3), +1 BLU-001 (2 → 3). Le carte nerfate da P escono dalla lista: "
            "di P in questa lista conta solo la Base vuota di LDR-05."]


def D05B(s, m):
    src = [c for c in json.load(open(D05B_SRC, encoding="utf-8"))["cards"] if c["id"].startswith("D05B-")]
    s["cards"] += copy.deepcopy(src)
    d = deck(m)
    rows = []
    for c in src:
        o = c["id"][5:]
        rows.append(f"{o} ×{d['cards'].count(o)}")
        d["cards"] = [c["id"] if x == o else x for x in d["cards"]]
    return ["Scudo tolto alle Unità di `rif_LDR05`: copie `D05B-*` (identiche a quelle di E-025 D05b_c02: senza la parola chiave "
            "`scudo`, Forza e resto invariati) al posto di " + ", ".join(rows) + ". Gli originali restano nel set e nelle altre liste."]


def D2M(s, m):
    d = deck(m)
    rows = []
    for o in sorted(set(d["cards"])):
        c0 = card(s, o)
        if c0["type"] != "unit" or not ({"scudo", "impeto"} & set(c0.get("keywords", []))):
            continue
        c = copy.deepcopy(c0)
        c["id"] = c["name"] = f"D2M-{o}"
        c["keywords"] = [k for k in c["keywords"] if k not in ("scudo", "impeto")]
        if "impeto" in c0["keywords"]:
            imp = [ab for ab in c["abilities"] if is_impeto_ab(ab)]
            assert len(imp) == 1, o
            c["abilities"] = [ab for ab in c["abilities"] if not is_impeto_ab(ab)]
        c["text"] = RE_IMPETO.sub("", RE_SCUDO.sub("", c["text"])).strip()
        c.pop("tags", None)
        c["_note"] = f"E-029 D-2M: copia diagnostica di {o} senza Scudo e senza Impeto (costo, Forza, colore invariati). Solo in rif_LDR05."
        s["cards"].append(c)
        rows.append(f"{o} ×{d['cards'].count(o)}")
        d["cards"] = [c["id"] if x == o else x for x in d["cards"]]
    return ["Scudo e Impeto tolti insieme alle Unità di `rif_LDR05`: copie `D2M-*` (senza le parole chiave `scudo` e `impeto` e senza "
            "la statica di Forza dell'Impeto; altre abilità, Forza, costo e colore invariati) al posto di " + ", ".join(rows)
            + ". Di conseguenza la Base di LDR-05 (Scudo) e il Risvegliato (Impeto) non trovano più bersagli nella lista."]


BASETR = ("LDR-01,LDR-05,BLU-001,BLU-007,BLU-008,BLU-010,BLU-012,BLU-015,BLU-021,BLU-023,BLU-025,NEU-006,NEU-013,ROS-001,ROS-003,"
          "ROS-005,ROS-007,ROS-010,ROS-015,ROS-016,ROS-018,ROS-020,ROS-021,ROS-023,ROS-025,VER-001,VER-002,VER-009,VER-011,VER-019,VER-024")
ARMS = {  # nome: (leve, chi, protagonisti, seed_base, riferimento, ore stimate)
    "00_B0c03": ([], "riferimento: copia di B0c03; su 3300+k va portato a 200 per incrocio (protagonista 5)", "5", 3300,
                 "— (su 3200+k esiste già da E-028 A e non si rigioca)", 3.6),
    "P": ([P], "competitivo, nero, critico, analista (3 modifiche)", "1,5", 3200, "E-028_c04/00_B0c03 F_s3200 (200 per incrocio, già giocato)", 6.5),
    "P-rott": ([P, PROTT], "competitivo (lista di rottura); P si vota solo se anche qui Δ05 ≤ −3 (critico)", "5", 3300,
               "E-029_c04/00_B0c03 F_s3300 (200 per incrocio)", 3.6),
    "D05b-200": ([D05B], "diagnosi dello Scudo (D05b a 200 partite)", "5", 3300, "E-029_c04/00_B0c03 F_s3300", 3.6),
    "D-2M": ([D2M], "diagnosi di Scudo e Impeto insieme (ponti)", "5", 3300, "E-029_c04/00_B0c03 F_s3300", 3.6),
}
TR = {}
for name, (levers, who, prot, sb, ref, ore) in ARMS.items():
    s, m = copy.deepcopy(SET), copy.deepcopy(MAZ)
    ch = [x for f in levers for x in f(s, m)]
    s["version"] = m["set"] = f"set_v02+E-029_{name}"
    s["note"] = SET["note"] + f" E-029 {name}: B0c03 (E-025 A-FV_c02) con le sole leve del braccio (vedi LEGGIMI.md)."
    m["autore"], m["data"] = "programmatore (swarm)", "2026-10-26"
    m["nota"] = MAZ["nota"] + f" E-029 {name}: liste di B0c03" + (", rif_LDR05 modificata (vedi LEGGIMI.md)." if name != "00_B0c03" and name != "P" else " invariate.")
    tr = BASETR + "".join("," + c["id"] for c in s["cards"] if c["id"].startswith(("D05B-", "D2M-")))
    TR[name] = tr
    p = os.path.join(OUT, name)
    os.makedirs(p, exist_ok=True)
    json.dump(s, open(f"{p}/carte.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(m, open(f"{p}/mazzi.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(f"{p}/traccia.txt", "w", encoding="utf-8").write(tr + "\n")
    d = deck(m)
    cards = {c["id"]: c for c in s["cards"]}
    cnt = Counter(d["cards"])
    units = sum(k for c, k in cnt.items() if cards[c]["type"] == "unit")
    scudo = sum(k for c, k in cnt.items() if "scudo" in cards[c].get("keywords", []))
    col = Counter(x for c, k in cnt.items() for x in cards[c]["colors"] for _ in range(k))
    open(f"{p}/LEGGIMI.md", "w", encoding="utf-8").write(
        f"# E-029_c04 / {name}\n\n- **Cosa cambia rispetto a B0c03:**\n" + "".join(f"  - {x}\n" for x in ch or ["nulla (riferimento)."])
        + f"- **Proponenti / ruolo:** {who}.\n"
        + f"- **`rif_LDR05` nel braccio:** {len(d['cards'])} carte, {units} Unità, {sum(cnt.values()) - units} non Unità, {scudo} copie con Scudo, "
        + f"colori R {col['R']} B {col['B']} N {len(d['cards']) - col['R'] - col['B']}; massimo copie per ID {max(cnt.values())}.\n"
        + f"- **Si misura:** IA forte, 200 partite per incrocio, protagonisti `{prot}`, semi {sb}+k; contro {ref}.\n"
        + f"- **Comando:** `E029_TRACCIA=$(cat traccia.txt) bash ../lancia_e029.sh {name} forte:30 200 {sb} {prot}` "
        + f"(uscita `tcg/swarm/esperimenti/E-029_c04/{name}/F_s{sb}`), stima {ore} h su 4 core.\n"
        + "- **Regole:** `tcg/swarm/cicli/ciclo-04/round1/punti_passata2.md` (punti 1–3, esito della passata 2).\n")
    print(name, f"Unità {units}, Scudo {scudo}, carte {len(d['cards'])}", ch)
