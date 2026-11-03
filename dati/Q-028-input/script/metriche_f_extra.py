"""Q-028, misure aggiuntive chieste dall'analista, dai log già salvati del torneo 3600+k (partite.pkl di metriche_f.py).
Nessuna partita nuova, motore non toccato (si leggono solo le carte per i costi).

  python3 -B metriche_f_extra.py <radice_sim> <carte.json> <partite.pkl>   → stampa la sezione Markdown

1. Scontri senza possibilità. Dal log: gemme del turno = min(round, 8), +1 per P2 nei round 1 e 3 (V027);
   meno i costi delle carte giocate, di Rimarginare (1, 0 per LDR-03 Risvegliato), delle ⟳ e delle gemme già messe negli
   attacchi precedenti del turno. Forza massima = X + gemme rimaste (1 Forza a gemma).
   Difesa minima = Y − 2·d (3·d per LDR-02 Risvegliata) e, se il difensore è LDR-02 e ha messo gemme, X torna su di 2.
   Senza possibilità = Forza massima < difesa minima (non arriva nemmeno al pareggio). Gli scontri con una Reazione si
   lasciano fuori (l'effetto della Reazione non si ricava dal log): contano come scontri con possibilità.
2. Round deciso: da quale round il vincitore resta avanti nelle Vite (strettamente) fino alla fine. Il motore non dà una stima
   di vittoria, quindi si usa la regola di riserva.
3. Turni vuoti nei round 1–3: turno senza «gioca», attacchi, Rimarginare o ⟳.
4. A 0 Vite: primo inizio di turno in cui un giocatore ha 0 Vite e l'altro ≥1.
"""
import pickle, re, statistics, sys
from collections import Counter, defaultdict
sys.path.insert(0, sys.argv[1])
from sim.v02 import engine, run  # noqa: E402
run.use_cards(sys.argv[2])
C = engine.CARDS
DECKS = ["rif_LDR01_puntata_e_preda", "rif_LDR02_muro_di_parata", "rif_LDR03_sanguinare_per_accendere",
         "rif_LDR04_stanca_e_smonta", "rif_LDR05_scudi_armati", "rif_LDR06_ferite_e_caccia"]
LDR = {d: f"LDR-0{i + 1}" for i, d in enumerate(DECKS)}
RE_R = re.compile(r"^--- Round (\d+), P(\d) \| Vite (\d+)-(\d+)")
RE_G = re.compile(r"^  P(\d) gioca (\S+)")
RE_RIM = re.compile(r"^  P(\d) Rimargina ")
RE_AB = re.compile(r"^  P(\d) usa ⟳ di (\S+)")
RE_ABL = re.compile(r"^  P(\d) usa ⟳ del Leader")
RE_ATT = re.compile(r"^  P(\d) attacca con (Leader \S+|\S+?)(#\d+)?( |$)")
RE_PU = re.compile(r"^    pugni: attaccante (\d+), difensore (\d+)( \+ (\S+))? -> (-?\d+) contro (-?\d+)")
RE_RISV = re.compile(r"^    P(\d): il Leader si Risveglia")


def ab_cost(cid):
    for ab in C[cid].abilities:
        if ab.get("activated"):
            return ab.get("cost", 0)
    return 0


recs = []
with open(sys.argv[3], "rb") as f:
    while True:
        try:
            recs.append(pickle.load(f)[1])
        except Exception:
            break

H = defaultdict(Counter)       # per lista: scontri, senza possibilità, reazioni
empty = defaultdict(Counter)   # per lista: turni R1–3, vuoti
dec_r, zero = [], Counter()
zero_rounds = []
for r in recs:
    dk = [run.D.label(x) for x in r["decks"]]
    st, log, w = r["stats"], r["log"], r["winner"]
    for q in (0, 1):
        H[dk[q]]["idle"] += st["unit_idle"][q]; H[dk[q]]["ut"] += st["unit_turns"][q]
    aw = [False, False]
    rd = q = None
    brace = 0
    acts = 0
    vite = []
    last_att = None
    for l in log + ["--- Round 99, P1 | Vite 0-0"]:
        m = RE_R.match(l)
        if m:
            if rd is not None and rd <= 3:
                empty[dk[q]]["turni"] += 1; empty[dk[q]]["vuoti"] += acts == 0
            rd, q = int(m[1]), int(m[2]) - 1
            if rd == 99:
                break
            vite.append((rd, q, int(m[3]), int(m[4])))
            brace = min(rd, 8) + (1 if q == 1 and rd in (1, 3) else 0)
            acts = 0
            continue
        if (m := RE_RISV.match(l)):
            aw[int(m[1]) - 1] = True
        elif (m := RE_G.match(l)) and int(m[1]) - 1 == q:
            brace -= C[m[2]].cost; acts += 1
        elif (m := RE_RIM.match(l)) and int(m[1]) - 1 == q:
            brace -= 0 if (LDR[dk[q]] == "LDR-03" and aw[q]) else 1; acts += 1
        elif (m := RE_AB.match(l)) and int(m[1]) - 1 == q:
            brace -= ab_cost(m[2]); acts += 1
        elif RE_ABL.match(l):
            acts += 1
        elif (m := RE_ATT.match(l)) and int(m[1]) - 1 == q:
            acts += 1; last_att = "L" if m[2].startswith("Leader") else "U"
        elif (m := RE_PU.match(l)) and rd is not None:
            a, d, react, X, Y = int(m[1]), int(m[2]), m[4], int(m[5]), int(m[6])
            dq = 1 - q
            x = H[dk[dq]]
            x["scontri"] += 1
            if react:
                x["react"] += 1
            else:
                ppg = 3 if (LDR[dk[dq]] == "LDR-02" and aw[dq]) else 2
                ymin = Y - ppg * d
                xmax = X + max(brace - a, 0) + (2 if LDR[dk[dq]] == "LDR-02" and d >= 1 else 0)
                if xmax < ymin:
                    x["senza"] += 1
                    H[dk[q]]["senza_att"] += 1
                    if last_att == "U":
                        H[dk[q]]["senza_unit"] += 1
            brace -= a
    # 2. round deciso
    if w is not None:
        s = 1 if w == 0 else -1
        not_ahead = [rr for (rr, _, p1, p2) in vite if s * (p1 - p2) <= 0]
        dec_r.append((max(not_ahead) + 1) if not_ahead else 1)
    # 4. a 0 Vite
    first = next(((rr, 0 if p1 == 0 else 1) for (rr, _, p1, p2) in vite if (p1 == 0) != (p2 == 0)), None)
    if first:
        zero["casi"] += 1
        zero_rounds.append(r["rounds"] - first[0])
        zero["ribalta"] += w == first[1]

L = ["", "## Misure aggiuntive per l'analista (dagli stessi 300 log, nessuna partita nuova)", "",
     "**Come sono calcolate:** script `script/metriche_f_extra.py`; definizioni e approssimazioni sono in testa allo script.", "",
     "### 1. Scontri senza possibilità",
     "Un attacco è senza possibilità quando l'attaccante, mettendo tutte le gemme che gli restano, non arriva nemmeno a pareggiare la difesa con 0 gemme di Parata.",
     "Gli scontri con una Reazione restano fuori dal conto.", "",
     "| Leader (difende) | Scontri difesi | Senza possibilità | Reazioni per scontro difeso | … senza quelli | Unità ferme (M6) | … contando ferme le Unità che attaccano senza possibilità |",
     "|---|---|---|---|---|---|---|"]
tot = Counter()
for d in DECKS:
    x = H[d]
    for k in ("scontri", "senza", "react", "idle", "ut", "senza_unit", "senza_att"):
        tot[k] += x[k]
for d in DECKS + ["Totale"]:
    x = tot if d == "Totale" else H[d]
    L.append(f"| {d[4:9] if d != 'Totale' else d} | {x['scontri']} | {x['senza']} ({100 * x['senza'] / max(x['scontri'], 1):.1f}%) | "
             f"{x['react'] / max(x['scontri'], 1):.3f} | {x['react'] / max(x['scontri'] - x['senza'], 1):.3f} | "
             f"{100 * x['idle'] / max(x['ut'], 1):.1f}% | {100 * (x['idle'] + x['senza_unit']) / max(x['ut'], 1):.1f}% |")
L += ["", "Le ultime due colonne sono le Unità ferme dell'attaccante: la riga di un Leader conta le sue Unità e i suoi attacchi senza possibilità. "
      "Nell'ultima colonna un'Unità che attacca senza possibilità conta come ferma (limite superiore).",
      "Attacchi senza possibilità per Leader attaccante: " + ", ".join(f"{d[4:9]} {H[d]['senza_att']} (di Unità {H[d]['senza_unit']})" for d in DECKS) + ".", ""]
dc = Counter(dec_r)
L += ["### 2. Round in cui la partita è decisa",
      "Il motore non dà una stima di vittoria. Uso la regola di riserva: il round da cui il vincitore resta avanti nelle Vite (strettamente) fino alla fine, misurato a ogni inizio di turno.", "",
      f"- Media **{statistics.mean(dec_r):.1f}**, mediana {statistics.median(dec_r)}, su {len(dec_r)} partite con un vincitore.",
      f"- Decise entro il round 6: {100 * sum(1 for x in dec_r if x <= 6) / len(dec_r):.1f}%. Dal round 10 in poi: {100 * sum(1 for x in dec_r if x >= 10) / len(dec_r):.1f}%.",
      "- Distribuzione: " + ", ".join(f"R{k}: {v}" for k, v in sorted(dc.items())) + ".", "",
      "### 3. Turni vuoti nei round 1–3 (nessuna carta, attacco, Rimarginare o ⟳)", "",
      "| Leader | Turni R1–3 | Vuoti |", "|---|---|---|"]
te = Counter()
for d in DECKS:
    e = empty[d]; te["turni"] += e["turni"]; te["vuoti"] += e["vuoti"]
    L.append(f"| {d[4:9]} | {e['turni']} | {100 * e['vuoti'] / max(e['turni'], 1):.1f}% |")
L.append(f"| Totale | {te['turni']} | {100 * te['vuoti'] / max(te['turni'], 1):.1f}% |")
zc = Counter(zero_rounds)
L += ["", "### 4. A 0 Vite senza esito",
      "Caso contato: un giocatore inizia un turno con 0 Vite mentre l'altro ne ha almeno 1. Si conta la prima volta in cui succede.", "",
      f"- Partite con questo caso: **{zero['casi']} su {len(recs)}** ({100 * zero['casi'] / len(recs):.1f}%).",
      f"- Round che restano dopo: media **{statistics.mean(zero_rounds):.1f}**, mediana {statistics.median(zero_rounds)}; distribuzione "
      + ", ".join(f"{k}: {v}" for k, v in sorted(zc.items())) + ".",
      f"- Il giocatore a 0 Vite ribalta e vince: **{zero['ribalta']}** ({100 * zero['ribalta'] / max(zero['casi'], 1):.1f}%)."]
print("\n".join(L))
