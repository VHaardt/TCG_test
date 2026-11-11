"""Tabelle R-028 (serve main con la PR #22), R-026 (interattività) e R-027 P9b di un braccio, dai record per partita tenuti da tieni_pkl.sh.
Uso (dalla radice di una copia del simulatore): python3 -B agg_q028.py <semi_keep/E-03x/<braccio>/F_s3400> [out.md]"""
import glob, os, pickle, sys
sys.path.insert(0, os.getcwd())
from sim.v02 import run

recs = []
for f in sorted(glob.glob(os.path.join(sys.argv[1], "*", "partite.pkl"))):
    with open(f, "rb") as fh:
        while True:
            try:
                recs.append(pickle.load(fh)[1])
            except Exception:
                break
L = [f"# {sys.argv[1].rstrip('/').split('/')[-2]}: ritmo (R-028), interattività (R-026) e Reazioni (R-027 P9b)", "",
     f"Partite: {len(recs)}, dai record per partita di {len(glob.glob(os.path.join(sys.argv[1], '*', 'partite.pkl')))} incroci."]
L += run.render_q028(recs) + run.render_q027(recs) + run.render_p9b(recs)
for f in ("render_p7", "render_breccia"):          # solo sul branch dei contatori (PR #24)
    if hasattr(run, f):
        L += getattr(run, f)(recs)
txt = "\n".join(L).replace("rif_LDR0", "L").replace("/home/claude/e031_in/", "").replace("/home/claude/e033_in/", "") + "\n"
if len(sys.argv) > 2:
    open(sys.argv[2], "w", encoding="utf-8").write(txt)
print(txt)
