"""E-038: riepilogo della combinazione finale sui 15 incroci, con A (200 partite) e senza A (100), appaiati per seme.
Uso: python3 -B agg_e038.py <out.md> <radice>...   (ogni radice ha <conA|senzaA>/F_s3700/Li-Lj/partite.pkl; es. dati/E-038/comune dati/E-038/H5-v+H6-v)"""
import glob, math, os, pickle, random, re, sys

OUT, ROOTS = sys.argv[1], sys.argv[2:]
LAB = lambda d: re.sub(r"rif_LDR0(\d)_\w+", r"L\1", d.split("#")[-1])
LEAD = [f"L{i}" for i in range(1, 7)]


def load(v):
    cells = {}
    for root in ROOTS:
        for f in sorted(glob.glob(f"{root}/{v}/F_s3700/L?-L?/partite.pkl")):
            c = f.split("/")[-2]
            if c in cells:
                raise SystemExit(f"cella doppia {c} in {v}")
            rs = {}
            with open(f, "rb") as fh:
                while True:
                    try:
                        i, r = pickle.load(fh); rs[i] = r
                    except Exception:
                        break
            cells[c] = rs
    return cells


def wilson(k, n, z=1.96):
    if n == 0:
        return "—"
    p = k / n; den = 1 + z * z / n; c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return f"{100*p:.1f} [{100*(c-h):.1f}–{100*(c+h):.1f}]"


def wins(cells, sel=lambda i: True):
    """vittorie e partite per Leader."""
    w = {l: 0 for l in LEAD}; n = {l: 0 for l in LEAD}
    for c, rs in cells.items():
        for i, r in rs.items():
            if not sel(i):
                continue
            labs = [LAB(d) for d in r["decks"]]
            for q, l in enumerate(labs):
                n[l] += 1; w[l] += r["winner"] == q
    return w, n


def dist(w, n):
    return sum(max(0.0, 45 - 100 * w[l] / n[l], 100 * w[l] / n[l] - 55) for l in LEAD if n[l])


def boot_dist(cells, reps=2000, seed=1):
    rnd = random.Random(seed); keys = {c: list(rs) for c, rs in cells.items()}; out = []
    for _ in range(reps):
        w = {l: 0 for l in LEAD}; n = {l: 0 for l in LEAD}
        for c, rs in cells.items():
            ks = keys[c]
            for _ in ks:
                r = rs[rnd.choice(ks)]
                for q, d in enumerate(r["decks"]):
                    l = LAB(d); n[l] += 1; w[l] += r["winner"] == q
        out.append(dist(w, n))
    out.sort()
    return out[int(0.025 * reps)], out[int(0.975 * reps) - 1]


A, S = load("conA"), load("senzaA")
L = ["# E-038: combinazione finale H5-v+H6-v sui 15 incroci", "",
     f"Celle con A: {len(A)} ({sum(len(r) for r in A.values())} partite); senza A: {len(S)} ({sum(len(r) for r in S.values())} partite). "
     "Motore 612057d (R-031 + R-032), input d770cbf, forte:30, semi 3700+k; le 6 celle senza L5 e L6 sono giocate una volta (identiche in tutte le combinazioni). IC di Wilson al 95%.", ""]
wA, nA = wins(A); w1, n1 = wins(A, lambda i: i < 100); w2, n2 = wins(A, lambda i: i >= 100); wS, nS = wins(S)
L += ["## Vittorie per Leader", "", "| Leader | con A (200 per incrocio) | con A, partite 0–99 | con A, partite 100–199 | senza A (100 per incrocio) | Δ con A − senza A (prime 100, appaiato) |", "|---|---|---|---|---|---|"]
for l in LEAD:
    ds = []
    for c in A:
        if l not in c.split("-") or c not in S:
            continue
        for i, ra in A[c].items():
            rb = S[c].get(i)
            if rb is None:
                continue
            qa = [LAB(d) for d in ra["decks"]].index(l); qb = [LAB(d) for d in rb["decks"]].index(l)
            ds.append((ra["winner"] == qa) - (rb["winner"] == qb))
    if ds:
        m = sum(ds) / len(ds); sd = math.sqrt(sum((d - m) ** 2 for d in ds) / (len(ds) - 1)); h = 1.96 * sd / math.sqrt(len(ds))
        dtxt = f"{100*m:+.1f} [{100*(m-h):+.1f} … {100*(m+h):+.1f}] (n={len(ds)})"
    else:
        dtxt = "—"
    L.append(f"| {l} | **{wilson(wA[l], nA[l])}** | {wilson(w1[l], n1[l])} | {wilson(w2[l], n2[l])} | {wilson(wS[l], nS[l])} | {dtxt} |")
fuori = [l for l in LEAD if nA[l] and not 42 <= 100 * wA[l] / nA[l] <= 58]
L += ["", f"Con A, Leader fuori da 42–58: {', '.join(fuori) if fuori else 'nessuno'}. "
      f"Fuori da 45–55: {', '.join(l for l in LEAD if nA[l] and not 45 <= 100 * wA[l] / nA[l] <= 55) or 'nessuno'}.", ""]
lo, hi = boot_dist(A); slo, shi = boot_dist(S)
L += ["## Somma delle distanze dalla fascia 45–55 (punti; IC bootstrap 95% sulle partite)", "",
      f"- con A: **{dist(wA, nA):.1f}** [{lo:.1f}–{hi:.1f}]; partite 0–99 {dist(w1, n1):.1f}, partite 100–199 {dist(w2, n2):.1f}",
      f"- senza A: **{dist(wS, nS):.1f}** [{slo:.1f}–{shi:.1f}]", ""]


def ritmo(cells):
    rs = [r for c in cells.values() for r in c.values()]; n = len(rs)
    return (wilson(sum(r["rounds"] >= 13 for r in rs), n), wilson(sum(r["end_reason"] == "crepuscolo" for r in rs), n),
            wilson(sum(r["winner"] is not None and r["rounds"] <= 5 for r in rs), n), wilson(sum(r["winner"] is not None and r["rounds"] < 5 for r in rs), n))


L += ["## Ritmo (tutte le partite)", "", "| | Round 13+ | Chiuse dal Crepuscolo | Vittorie entro il R5 (≤5) | prima del R5 (<5) |", "|---|---|---|---|---|"]
for name, cs in (("con A", A), ("senza A", S)):
    L.append(f"| {name} | " + " | ".join(ritmo(cs)) + " |")


def r95(cells, l="L6"):
    t = k = 0
    for c in cells.values():
        for r in c.values():
            labs = [LAB(d) for d in r["decks"]]
            if l in labs:
                t += r["stats"]["stanca_removed"][labs.index(l)]; k += 1
    return t / k if k else float("nan")


L += ["", f"R9-5 di L6 (Unità Stancate da Pronte e rimosse nello stesso turno, per partita; allarme >1): con A {r95(A):.2f}, senza A {r95(S):.2f}.", ""]
cell = lambda cs: (lambda rs: wilson(sum(r["winner"] == [LAB(d) for d in r["decks"]].index("L5") for r in rs), len(rs)))(list(cs.get("L5-L6", {}).values())) if "L5-L6" in cs else "—"
L += [f"Cella L5-L6, vittorie di L5: con A {cell(A)}; senza A {cell(S)}.", ""]
L += ["## Matrice con A (vittorie della riga contro la colonna)", "", "| | " + " | ".join(LEAD) + " |", "|---|" + "---|" * 6]
for a in LEAD:
    row = []
    for b in LEAD:
        c = f"{min(a,b)}-{max(a,b)}"
        if a == b or c not in A:
            row.append("—"); continue
        rs = A[c].values(); row.append(f"{100*sum(r['winner'] == [LAB(d) for d in r['decks']].index(a) for r in rs)/len(rs):.1f}")
    L.append(f"| {a} | " + " | ".join(row) + " |")
txt = "\n".join(L) + "\n"
open(OUT, "w", encoding="utf-8").write(txt); print(txt)
