"""E-036: confronto appaiato per seme di un braccio con il riferimento 00_B0c06A, per il Leader protagonista.
Uso (dalla radice di una copia del simulatore): python3 -B agg_e036.py <E-036> <braccio> [out.md]
Riferimento: AGG_REF_DIR (default <E-036>/00_B0c06A) e AGG_REF (nome nel report). Con 100 partite nel braccio si appaiano le prime 100 del riferimento."""
import glob, math, os, pickle, re, sys

ROOT, ARM = sys.argv[1], sys.argv[2]
REF = os.environ.get("AGG_REF", "00_B0c06A")
REF_DIR = os.environ.get("AGG_REF_DIR", f"{ROOT}/00_B0c06A")
PROT = "L6" if ARM[1] == "6" else "L5"
LID = {"L5": "LDR-05", "L6": "LDR-06"}[PROT]
lab = lambda d: (lambda n: re.sub(r"rif_LDR0(\d)_\w+", r"L\1", n).replace("rott_LDR05_2c", "R5"))(d.split("#")[-1])


def load(d):
    out = {}
    for c in sorted(glob.glob(f"{d}/F_s3700/*/partite.pkl")):
        rs = []
        with open(c, "rb") as fh:
            while True:
                try:
                    rs.append(pickle.load(fh)[1])
                except Exception:
                    break
        out[c.split("/")[-2]] = {r["seed"]: r for r in rs}
    return out


def wilson(k, n, z=1.96):
    p = k / n; den = 1 + z * z / n; c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return f"{100*p:.1f} [{100*(c-h):.1f}–{100*(c+h):.1f}]"


def paired(ds):
    n = len(ds); m = sum(ds) / n
    sd = math.sqrt(sum((d - m) ** 2 for d in ds) / (n - 1)) if n > 1 else 0
    h = 1.96 * sd / math.sqrt(n)
    return f"{100*m:+.1f} [{100*(m-h):+.1f} … {100*(m+h):+.1f}]"


def seat(r, who):
    return next((i for i, d in enumerate(r["decks"]) if lab(d) == who), None)


A, R = load(f"{ROOT}/{ARM}"), load(REF_DIR)
cells = [c for c in A if PROT in c.split("-") and c in R]
L = [f"# E-036 / {ARM}: {PROT} appaiato per seme con {REF}", "",
     f"Celle di {PROT} comuni ai due bracci: {len(cells)}; partite appaiate per seme. Δ = vittorie di {PROT} nel braccio meno nel riferimento, IC 95% sulle differenze appaiate.", "",
     f"| Cella | {PROT} in {ARM} | {PROT} in {REF} | Δ appaiato |", "|---|---|---|---|"]
allD, kA, kR, nA = [], 0, 0, 0
for c in cells:
    ds, ka, kr = [], 0, 0
    for s, ra in A[c].items():
        rr = R[c].get(s)
        if rr is None:
            continue
        wa = ra["winner"] == seat(ra, PROT); wr = rr["winner"] == seat(rr, PROT)
        ds.append(wa - wr); ka += wa; kr += wr
    n = len(ds); allD += ds; kA += ka; kR += kr; nA += n
    L.append(f"| {c} | {wilson(ka, n)} | {wilson(kr, n)} | {paired(ds)} |")
L.append(f"| **Totale** | **{wilson(kA, nA)}** | {wilson(kR, nA)} | **{paired(allD)}** |")


def prof(data, cs, other):
    p = {"n": 0, "act": 0, "act_b": 0, "act_a": 0, "side": False, "life": 0, "scudo2": 0, "w5": 0, "wlt5": 0, "r13": 0, "f20": 0, "f21": 0, "opp20": 0, "opp21": 0}
    for c in cs:
        for sd, r in data[c].items():
            if sd not in other[c]:
                continue
            i = seat(r, PROT); s = r["stats"]
            p["n"] += 1
            p["act"] += s["activations"][i].get(LID, 0)
            if "leader_act_side" in s:
                p["side"] = True; p["act_b"] += s["leader_act_side"][i]["base"]; p["act_a"] += s["leader_act_side"][i]["awakened"]
            p["life"] += s["life_costs"][i]; p["scudo2"] += s["scudo_atk2"][i]
            p["w5"] += r["winner"] == i and r["rounds"] <= 5; p["wlt5"] += r["winner"] == i and r["rounds"] < 5
            p["r13"] += r["rounds"] >= 13
            p["f20"] += s["fa_alta_by"][i].get("ROS-020", 0); p["f21"] += s["fa_alta_by"][i].get("ROS-021", 0)
            p["opp20"] += s["fa_alta_by"][1 - i].get("ROS-020", 0); p["opp21"] += s["fa_alta_by"][1 - i].get("ROS-021", 0)
    return p


pa, pr = prof(A, cells, R), prof(R, cells, A)
row = lambda name, f: f"| {name} | {f(pa)} | {f(pr)} |"
per = lambda k: (lambda p: f"{p[k]/p['n']:.2f}")
L += ["", f"## {PROT}: misure per partita del protagonista (stesse celle)", "", f"| Misura | {ARM} | {REF} |", "|---|---|---|",
      row(f"Attivazioni di {LID} (Base + Risvegliato)", per("act"))]
if pa["side"]:
    L.append(row(f"di cui Base / Risvegliato (R-031)", lambda p: f"{p['act_b']/p['n']:.2f} / {p['act_a']/p['n']:.2f}" if p["side"] else "— (motore senza R-031)"))
L += [row("Costi in Vita pagati", per("life")), row("Attacchi con Scudo a ≥2 gemme", per("scudo2")),
      row(f"Scontri vinti con Forza ≥8 da ROS-020 / ROS-021 di {PROT}", lambda p: f"{p['f20']/p['n']:.2f} / {p['f21']/p['n']:.2f}"),
      row("Scontri vinti con Forza ≥8 da ROS-020 / ROS-021 degli avversari", lambda p: f"{p['opp20']/p['n']:.2f} / {p['opp21']/p['n']:.2f}"),
      row(f"Vittorie di {PROT} entro il R5 (≤5) / prima del R5 (<5)", lambda p: f"{wilson(p['w5'], p['n'])} / {wilson(p['wlt5'], p['n'])}"),
      row("Partite al round 13+", lambda p: wilson(p["r13"], p["n"])), ""]
txt = "\n".join(L) + "\n"
if len(sys.argv) > 3:
    open(sys.argv[3], "w", encoding="utf-8").write(txt)
print(txt)
