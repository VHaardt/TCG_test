"""E-027 (ciclo 03, Q-023): bracci sui due Leader rossi. Solo dati, nessuna regola nel codice.
Base B0c03 = tcg/set/esperimenti/E-025_B0c02/A-FV_c02/ (carte.json, mazzi.json), che NON si tocca.
  python3 -B genera_e027.py
"""
import copy, json, os
BASE = "/mnt/project-files/tcg/set/esperimenti/E-025_B0c02/A-FV_c02"
OUT = os.path.dirname(os.path.abspath(__file__))
SET = json.load(open(f"{BASE}/carte.json", encoding="utf-8"))
MAZ = json.load(open(f"{BASE}/mazzi.json", encoding="utf-8"))
L05 = "rif_LDR05_scudi_armati"


def card(s, cid):
    return next(c for c in s["cards"] if c["id"] == cid)


def R20(s, m):
    c = card(s, "ROS-020")
    c["power"] = 3
    c["vanilla_delta"] = -1
    c["_note"] = "Q-023 (E-027 R20): F4 → F3, testo invariato. A 0/1/2 gemme 3/6/7 (prima 4/7/8); con il Risvegliato di LDR-05 4/7/8."
    return "ROS-020: Forza 4 → 3 (`power` 3, `vanilla_delta` −1, `_note`); testo e abilità invariati."


def R21(s, m):
    c = card(s, "ROS-021")
    c["abilities"][0]["if"] = [{"pugno_ge": 2}]
    c["text"] = ("Impeto 2: +3 *(se nell'impegno hai almeno 2 gemme, +3 in questo scontro; "
                 "quando è il bersaglio contano solo le gemme di Parata)*.")
    c["_note"] = "Q-023 (E-027 R21): Impeto 1: +3 → Impeto 2: +3. A 0/1/2 gemme 5/6/10 (prima 5/9/10)."
    return "ROS-021: \"Impeto 1: +3\" → \"Impeto 2: +3\" (`abilities[0].if = [{\"pugno_ge\": 2}]`, `text`, `_note`). Forza 5 invariata."


def B5(s, m):
    b = next(l for l in s["leaders"] if l["id"] == "LDR-05")["base"][0]
    b["if"] = [{"pugno_ge": 2}]
    b["text"] = "Le tue Unità con Scudo hanno +1 in questo scontro quando attaccano, se nell'impegno hai almeno 2 gemme."
    return "LDR-05, Base: `base[0].if`: `pugno_ge 1` → `pugno_ge 2`, più `text`. Condizione già nel motore (nessuna primitiva nuova)."


def KROTT(s, m):
    d = next(x for x in m["mazzi"] if x["name"] == L05)
    for _ in range(3):
        d["cards"].remove("ROS-020")
    d["cards"] += ["ROS-021", "ROS-003", "ROS-003"]
    return f"Lista `{L05}`: −3 ROS-020, +1 ROS-021 (2 → 3), +2 ROS-003 (0 → 2). Carte di B0c03 invariate."


ARMS = {
    "00_B0c03": ([], "riferimento: copia di E-025_B0c02/A-FV_c02 (B0c03), nessuna leva", "—"),
    "R20": ([R20], "critico, rosso, competitivo, ponti", "00_B0c03"),
    "R21": ([R21], "blu, rosso, verde", "00_B0c03"),
    "B5": ([B5], "blu (L2), rosso (leva 3)", "00_B0c03"),
    "K-rott": ([KROTT], "critico, competitivo (lista di rottura di LDR-05)", "00_B0c03 (e R20 per la regola di rottura)"),
    "C": ([R20, R21], "R20 + R21 (si lancia solo se lo dice la regola di combinazione)", "00_B0c03"),
}
for name, (levers, who, ref) in ARMS.items():
    s, m = copy.deepcopy(SET), copy.deepcopy(MAZ)
    ch = [f(s, m) for f in levers]
    s["version"] = m["set"] = f"set_v02+E-027_{name}"
    s["note"] = SET["note"] + f" E-027 {name}: B0c03 (E-025 A-FV_c02) con le sole leve del braccio (vedi LEGGIMI.md)."
    m["autore"], m["data"] = "programmatore (swarm)", "2026-10-19"
    m["nota"] = MAZ["nota"] + f" E-027 {name}: liste di B0c03 (E-025 A-FV_c02)" + (", lista di rottura di LDR-05." if levers == [KROTT] else ".")
    p = os.path.join(OUT, name)
    os.makedirs(p, exist_ok=True)
    json.dump(s, open(f"{p}/carte.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(m, open(f"{p}/mazzi.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(f"{p}/LEGGIMI.md", "w", encoding="utf-8").write(
        f"# E-027_c03 / {name}\n\n- **Cosa cambia rispetto a B0c03:**\n" + "".join(f"  - {x}\n" for x in ch or ["nulla (riferimento)."])
        + f"- **Proponenti:** {who}.\n- **Si misura contro:** {ref}, stessi seed.\n"
        + "- **Testi e regole d'uscita:** `tcg/swarm/cicli/ciclo-03/round1/r1_*.md` e `discussione_*.md`.\n")
    print(name, ch)
