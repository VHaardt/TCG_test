"""E-035 (Q-031): mix_ a 2 copie contro i 6 rif_ di B0c06. Legge i partite.pkl delle celle di E-035 e di E-034 00_B0c06.
Uso: python3 -B agg_e035.py <E-035/F_s3600> <E-034/00_B0c06/F_s3500> [out.md]"""
import glob, math, os, pickle, re, sys


def recs_of(cell):
    out = []
    with open(os.path.join(cell, "partite.pkl"), "rb") as fh:
        while True:
            try:
                out.append(pickle.load(fh)[1])
            except Exception:
                break
    return out


def wilson(k, n, z=1.96):
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    p = k / n; den = 1 + z * z / n; c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return p, c - h, c + h


F = lambda w: f"{100*w[0]:.1f} [{100*w[1]:.1f}–{100*w[2]:.1f}]"
name = lambda d: d.split("#")[-1]
LEAD = {"M1": "L2", "M2": "L3", "M3": "L4", "M4": "L1"}
FULL = {}


def wins_of(recs, key):
    """vittorie, partite, round13+, vinte <R5, ≤R5, ≤R7 del mazzo che contiene key."""
    w = e5 = le5 = le7 = r13 = 0
    for r in recs:
        i = next(j for j, d in enumerate(r["decks"]) if key in name(d))
        FULL[key] = name(r["decks"][i])
        r13 += r["rounds"] >= 13
        if r["winner"] == i:
            w += 1; e5 += r["rounds"] < 5; le5 += r["rounds"] <= 5; le7 += r["rounds"] <= 7
    return w, len(recs), r13, e5, le5, le7


e35, e34 = sys.argv[1], sys.argv[2]
L = ["# E-035 (Q-031): le 4 mix_ a 2 copie contro i 6 rif_ di B0c06", "",
     "V027, forte:30, 200 partite per incrocio, semi 3600+k, motore main 8ff53fc, input 7ed91c5. "
     "Riferimento: E-034 braccio 00_B0c06 (stesso motore e preset, semi 3500+k). Percentuali con IC di Wilson al 95%.", ""]
cells = {os.path.basename(c): recs_of(c) for c in sorted(glob.glob(f"{e35}/M?-L?"))}
ref = {os.path.basename(c): recs_of(c) for c in sorted(glob.glob(f"{e34}/L?-L?"))}

# rif_ dello stesso Leader in E-034: media sui suoi 5 incroci
def rif_mean(lab):
    w = n = 0
    for k, rs in ref.items():
        if lab in k.split("-"):
            a, b, *_ = wins_of(rs, "rif_LDR0" + lab[1]); w += a; n += b
    return wilson(w, n)

L += ["## Vittorie della mix_ per incrocio", "", "| mix_ | " + " | ".join(f"contro L{i}" for i in range(1, 7)) + " | media | rif_ stesso Leader (E-034) |", "|---|" + "---|" * 8]
summ = {}
for m in ("M1", "M2", "M3", "M4"):
    row, W, N = [], 0, 0
    agg = [0] * 6
    for i in range(1, 7):
        rs = cells[f"{m}-L{i}"]
        t = wins_of(rs, f"mix_{m}_")
        agg = [a + b for a, b in zip(agg, t)]
        row.append(F(wilson(t[0], t[1])))
    summ[m] = agg
    L.append(f"| {m} ({LEAD[m]}) | " + " | ".join(row) + f" | **{F(wilson(agg[0], agg[1]))}** | {F(rif_mean(LEAD[m]))} |")
L += ["", "Nomi: " + ", ".join(f"{m} = `{FULL[f'mix_{m}_']}`" for m in summ) + ". Lo specchio M-L dello stesso Leader è incluso nella media della mix_.", ""]

L += ["## Ritmo e vittorie veloci della mix_ (sui 6 incroci, 1200 partite)", "",
      "| mix_ | round 13+ | vinte prima del R5 (<5) | vinte entro il R5 (≤5) | vinte entro il R7 (≤7) |", "|---|---|---|---|---|"]
for m, a in summ.items():
    w, n, r13, e5, le5, le7 = a
    L.append(f"| {m} | {F(wilson(r13, n))} | {F(wilson(e5, n))} | {F(wilson(le5, n))} | {F(wilson(le7, n))} |")
allr = [r for rs in cells.values() for r in rs]
L += ["", f"Tutte le 4800 partite: round 13+ {F(wilson(sum(r['rounds'] >= 13 for r in allr), len(allr)))}; "
      f"B0c06 (E-034, 3000 partite): {F(wilson(sum(r['rounds'] >= 13 for rs in ref.values() for r in rs), sum(len(rs) for rs in ref.values())))}.", ""]

# R9-5 di M2 dai report delle celle
L += ["## R9-5 per M2 (Unità Stancate da Pronte e rimosse nello stesso turno, per partita)", "", "| incrocio | M2 | avversario |", "|---|---|---|"]
for i in range(1, 7):
    md = [f for f in glob.glob(f"{e35}/M2-L{i}/*_torneo_*.md")][0]
    line = next(l for l in open(md, encoding="utf-8") if l.startswith("| R9-5 |"))
    v = dict(re.findall(r"(\w+_\w+) ([\d.]+)", line.split("|")[3]))
    m2 = next(x for k, x in v.items() if k.startswith("mix_M2"))
    opp = next(x for k, x in v.items() if not k.startswith("mix_M2"))
    L.append(f"| M2-L{i} | {m2} | {opp} |")
txt = "\n".join(L) + "\n"
if len(sys.argv) > 3:
    open(sys.argv[3], "w", encoding="utf-8").write(txt)
print(txt)
