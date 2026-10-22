"""E-028 (ciclo 04, Q-024 parte A): riferimento B0c03 e braccio dichiarato RB = R21 + B5. Solo dati.
Base B0c03 = tcg/set/esperimenti/E-025_B0c02/A-FV_c02/ (non si tocca). Leve identiche ai bracci R21 e B5 di E-027_c03.
  python3 -B genera_e028.py
"""
import copy, json, os
BASE = "/mnt/project-files/tcg/set/esperimenti/E-025_B0c02/A-FV_c02"
OUT = os.path.dirname(os.path.abspath(__file__))
SET = json.load(open(f"{BASE}/carte.json", encoding="utf-8"))
MAZ = json.load(open(f"{BASE}/mazzi.json", encoding="utf-8"))


def R21(s):
    c = next(c for c in s["cards"] if c["id"] == "ROS-021")
    c["abilities"][0]["if"] = [{"pugno_ge": 2}]
    c["text"] = ("Impeto 2: +3 *(se nell'impegno hai almeno 2 gemme, +3 in questo scontro; "
                 "quando è il bersaglio contano solo le gemme di Parata)*.")
    c["_note"] = "Q-023 (E-027 R21): Impeto 1: +3 → Impeto 2: +3. A 0/1/2 gemme 5/6/10 (prima 5/9/10)."
    return "ROS-021: \"Impeto 1: +3\" → \"Impeto 2: +3\" (`abilities[0].if = [{\"pugno_ge\": 2}]`, `text`, `_note`), come E-027_c03/R21."


def B5(s):
    b = next(l for l in s["leaders"] if l["id"] == "LDR-05")["base"][0]
    b["if"] = [{"pugno_ge": 2}]
    b["text"] = "Le tue Unità con Scudo hanno +1 in questo scontro quando attaccano, se nell'impegno hai almeno 2 gemme."
    return "LDR-05, Base: `base[0].if`: `pugno_ge 1` → `pugno_ge 2`, più `text`, come E-027_c03/B5."


ARMS = {"00_B0c03": ([], "riferimento: copia di E-025_B0c02/A-FV_c02 (B0c03), da rigiocare sui semi 3200+k"),
        "RB": ([R21, B5], "braccio dichiarato di Q-024 parte A (R21 + B5), deciso prima dei dati")}
for name, (levers, who) in ARMS.items():
    s, m = copy.deepcopy(SET), copy.deepcopy(MAZ)
    ch = [f(s) for f in levers]
    s["version"] = m["set"] = f"set_v02+E-028_{name}"
    s["note"] = SET["note"] + f" E-028 {name}: B0c03 (E-025 A-FV_c02) con le sole leve del braccio (vedi LEGGIMI.md)."
    m["autore"], m["data"] = "programmatore (swarm)", "2026-10-22"
    m["nota"] = MAZ["nota"] + f" E-028 {name}: liste di B0c03 invariate."
    p = os.path.join(OUT, name)
    os.makedirs(p, exist_ok=True)
    json.dump(s, open(f"{p}/carte.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(m, open(f"{p}/mazzi.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(f"{p}/LEGGIMI.md", "w", encoding="utf-8").write(
        f"# E-028_c04 / {name}\n\n- **Cosa cambia rispetto a B0c03:**\n" + "".join(f"  - {x}\n" for x in ch or ["nulla (riferimento)."])
        + f"- **Ruolo:** {who}.\n- **Si misura:** IA forte, 200 partite per incrocio, protagonisti 1 e 5, semi 3200+k "
        + "(`bash ../lancia_e028.sh " + name + " forte:30 200 3200 1,5`), appaiato con l'altro braccio.\n"
        + "- **Regole d'uscita:** `tcg/swarm/questioni/Q-024_ciclo04_rossi_ridondanza_RB.md` §A (regole 1–9 e 11 del ciclo 03, tetto di LDR-01 relativo: Δ01 ≤ 0 a cella inclusa; regola 7 senza deroghe).\n")
    print(name, ch)
