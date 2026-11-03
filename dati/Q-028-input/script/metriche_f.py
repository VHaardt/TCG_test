"""Q-028: metriche del divertimento (F1–F6) su un torneo con l'IA forte. Il motore non si modifica.

Uso (dalla radice di una copia del simulatore, es. main ad77242):
  python3 -B metriche_f.py <radice_sim> <carte.json> <mazzi.json> <out_dir> [--partite 20] [--seed 3600] [--ia forte:30]

- Gioca i 15 incroci delle 6 liste rif_ (`--partite` partite per incrocio, posti alternati), seme dell'incrocio k = seed+k
  (k = 1 per 1-2 … 15 per 5-6), come i lanciatori di E-030; dentro l'incrocio i semi sono quelli di `cross_jobs`.
- Le partite finite si salvano in <out_dir>/partite.pkl (con i log): un rilancio gioca solo quelle mancanti.
- Fonti: il log della partita (righe "--- Round", "gioca", "Rimargina", "attacca con Leader"), i contatori del motore
  (`stats`) e, per F1/F6, un involucro di GameState.step che legge le azioni legali della fase principale senza cambiarle
  (stessa lista che il motore già conta in `stats["legal_actions"]`).
- Scrive <out_dir>/metriche_F.md e <out_dir>/metriche_F.json.
"""
import argparse, json, os, pickle, re, statistics, sys
from collections import Counter, defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("sim"); ap.add_argument("carte"); ap.add_argument("mazzi"); ap.add_argument("out")
ap.add_argument("--partite", type=int, default=20); ap.add_argument("--seed", type=int, default=3600)
ap.add_argument("--ia", default="forte:30"); ap.add_argument("--variante", default="V027")
a = ap.parse_args()
sys.path.insert(0, os.path.abspath(a.sim))
from multiprocessing import Pool
from sim.v02 import run, engine  # noqa: E402

DECKS = ["rif_LDR01_puntata_e_preda", "rif_LDR02_muro_di_parata", "rif_LDR03_sanguinare_per_accendere",
         "rif_LDR04_stanca_e_smonta", "rif_LDR05_scudi_armati", "rif_LDR06_ferite_e_caccia"]
LBL = {d: d[4:9] for d in DECKS}

# ------------------------------------------------------------------ involucro di step (sola lettura)
_step = engine.GameState.step


def step(self, act):
    if self.stats is not None and self.phase == "main":
        f = self.stats.setdefault("_f", {})
        key = f"{self.round}-{self.active}"
        t = f.get(key)
        legal = self.legal_actions()
        if t is None:
            pl = self.p[self.active]
            t = f[key] = {"first": len(legal), "first_play": sum(1 for x in legal if x[0] == "play"),
                          "hand": len(pl.hand), "dec": 0, "sum": 0, "one": 0, "played": 0}
        t["dec"] += 1; t["sum"] += len(legal); t["one"] += len(legal) == 1
        t["played"] += act[0] == "play"
    return _step(self, act)


engine.GameState.step = step


def job_list():
    jobs, k = [], 0
    for i in range(6):
        for j in range(i + 1, 6):
            k += 1
            x, y = f"{a.mazzi}#{DECKS[i]}", f"{a.mazzi}#{DECKS[j]}"
            for jb in run.cross_jobs(a.variante, a.ia, a.partite, [x, y], seed0=a.seed + k):
                jobs.append(jb[:4] + (True, os.path.abspath(a.carte)))
    return jobs


def play(item):
    return item[0], run.play_game(item[1])


def main():
    os.makedirs(a.out, exist_ok=True)
    run.CARTE[0] = os.path.abspath(a.carte)
    run.use_cards(run.CARTE[0])
    jobs = job_list()
    ck = os.path.join(a.out, "partite.pkl")
    done = {}
    if os.path.exists(ck):
        with open(ck, "rb") as f:
            while True:
                try:
                    i, r = pickle.load(f); done[i] = r
                except Exception:
                    break
    todo = [(i, j) for i, j in enumerate(jobs) if i not in done]
    if todo:
        with open(ck, "ab") as f, Pool(os.cpu_count() or 2) as pool:
            for i, r in pool.imap_unordered(play, todo):
                pickle.dump((i, r), f); f.flush(); done[i] = r
                if len(done) % 25 == 0:
                    print(f"{len(done)}/{len(jobs)}", flush=True)
    recs = [done[i] for i in range(len(jobs))]
    analizza(recs)


# ------------------------------------------------------------------ analisi
RE_R = re.compile(r"^--- Round (\d+), P(\d) \| Vite (\d+)-(\d+)")


def vite(log):
    """[(round, giocatore attivo, vite P1, vite P2)] all'inizio di ogni turno."""
    return [(int(m[1]), int(m[2]) - 1, int(m[3]), int(m[4])) for m in map(RE_R.match, log) if m]


def turni(log):
    """{(round, giocatore): righe del turno}."""
    out, cur = defaultdict(list), None
    for l in log:
        m = RE_R.match(l)
        if m:
            cur = (int(m[1]), int(m[2]) - 1)
        elif cur:
            out[cur].append(l)
    return out


def pct(x, n):
    return f"{100 * x / n:.1f}%" if n else "—"


def analizza(recs):
    C = engine.CARDS
    lista = {d["name"]: d["cards"] for d in json.load(open(a.mazzi, encoding="utf-8"))["mazzi"]}
    P = defaultdict(lambda: defaultdict(float))       # per Leader (lista), somme
    T = defaultdict(float)                            # totali
    rounds, ends, margini, decide_r, run_max, run_mean = [], Counter(), [], [], [], []
    played = {d: Counter() for d in DECKS}
    for r in recs:
        st, log = r["stats"], r["log"]
        dk = [run.D.label(x) for x in r["decks"]]
        w = r["winner"]
        rounds.append(r["rounds"]); ends[r["end_reason"]] += 1
        T["n"] += 1
        # F1 e F6 (involucro)
        for key, t in st.get("_f", {}).items():
            rd, q = map(int, key.split("-"))
            x = P[dk[q]]
            for tgt in (x, T):
                tgt["turni"] += 1; tgt["first"] += t["first"]; tgt["dec"] += t["dec"]; tgt["sum"] += t["sum"]
                tgt["solo"] += t["first"] == 1
                tgt["nogioca"] += t["played"] == 0
                tgt["piena"] += t["hand"] >= 6; tgt["piena_blocc"] += t["hand"] >= 6 and t["first_play"] == 0
                tgt["blocc"] += t["first_play"] == 0
        # F3 / F4 dalle Vite all'inizio dei turni
        v = vite(log)
        lead = [(p1 > p2) - (p1 < p2) for _, _, p1, p2 in v]
        nz = [s for s in lead if s]
        cambi = sum(1 for s0, s1 in zip(nz, nz[1:]) if s0 != s1)
        T["cambi"] += cambi
        for q in (0, 1):
            P[dk[q]]["n"] += 1; P[dk[q]]["cambi"] += cambi
        if w is not None:
            sign = 1 if w == 0 else -1
            dietro = [rd for (rd, _, p1, p2) in v if sign * (p1 - p2) <= -2]
            T["vinte"] += 1
            if dietro:
                T["rimonte"] += 1; P[dk[w]]["rimonte"] += 1
            P[dk[w]]["vinte"] += 1
            le = r["life_end"]; margini.append(abs(le[0] - le[1]))
            behind = [rd for (rd, _, p1, p2) in v if sign * (p1 - p2) < 0]
            decide_r.append((max(behind) + 1) if behind else 1)
            l6 = st.get("life_at_round6")
            if l6 and l6[0] != l6[1]:
                T["r6_n"] += 1; T["r6_ok"] += (l6[0] > l6[1]) == (w == 0)
        # round senza Vite perse (totale delle due Vite all'inizio di ogni round, turno di P1)
        tot = [p1 + p2 for (rd, q, p1, p2) in v if q == 0] + [sum(r["life_end"])]
        runs, cur = [], 0
        for t0, t1 in zip(tot, tot[1:]):
            if t1 == t0:
                cur += 1
            else:
                if cur: runs.append(cur)
                cur = 0
        if cur: runs.append(cur)
        run_max.append(max(runs) if runs else 0); run_mean.extend(runs)
        T["colpi"] += sum(st["attacks_leader_hit"]); T["rounds"] += r["rounds"]
        # F5: profilo e carte giocate
        tu = turni(log)
        for q in (0, 1):
            x = P[dk[q]]
            for cid, k in st["cards_played"][q].items():
                played[dk[q]][cid] += k
                x["gioca_" + C[cid].type] += k
            x["reazioni"] += st["reactions"][q]
            x["att_leader"] += st["leader_attacks"][q]
            x["rim"] += st["rim_used"][q]
            x["attacchi"] += st["attacks"][q]
            x["vinte_tot"] += w == q
            x["colpi"] += st["attacks_leader_hit"][q]
    n = int(T["n"])
    out = {"partite": n, "ia": a.ia, "variante": a.variante, "semi": f"{a.seed}+k"}
    L = [f"# Q-028: metriche del divertimento (F1–F6)\n",
         f"Torneo: 6 liste rif_ di B0c05 (corrette dal critico), 15 incroci × {a.partite} partite = {n}, IA {a.ia}, preset {a.variante}, "
         f"semi {a.seed}+k (k = indice dell'incrocio). Motore: main ad77242, non modificato. Script: `script/metriche_f.py`.\n",
         "Per Leader i valori sono per partita della lista (ogni partita conta per entrambe le liste).\n"]
    # F1
    L += ["## F1. Decisioni", "",
          "| Leader | Azioni legali alla prima scelta del turno | Azioni legali per scelta (fase principale) | Scelte per turno | Turni con una sola azione legale (solo «fine») | Turni senza giocare carte |",
          "|---|---|---|---|---|---|"]
    for d in DECKS + ["Totale"]:
        x = T if d == "Totale" else P[d]
        tt = max(x["turni"], 1)
        L.append(f"| {LBL.get(d, d)} | {x['first'] / tt:.1f} | {x['sum'] / max(x['dec'], 1):.1f} | {x['dec'] / tt:.1f} | "
                 f"{pct(x['solo'], tt)} | {pct(x['nogioca'], tt)} |")
    L += ["", "Turno = turno del giocatore attivo, fase principale (attacchi, carte, ⟳). Le scelte di gemme, opposizioni e Reazioni non sono contate qui. "
          "\"Passo forzato\" = alla prima scelta del turno l'unica azione legale è «fine».", ""]
    # F2
    L += ["## F2. Interazione (tabella R-026 del report del motore)"] + run.render_q027(recs)[1:] + [""]
    # F3
    rim = T["rimonte"] / max(T["vinte"], 1)
    L += ["## F3. Tensione", "",
          f"- Cambi di comando nelle Vite (chi è avanti, all'inizio di ogni turno; i pareggi non contano): **{T['cambi'] / n:.2f} a partita**.",
          f"- Rimonte (il vincitore è stato sotto di ≥2 Vite): **{pct(T['rimonte'], T['vinte'])}** delle partite vinte.",
          f"- Margine finale di Vite: media **{statistics.mean(margini):.2f}**, mediana {statistics.median(margini)}; distribuzione "
          + ", ".join(f"{k}: {v}" for k, v in sorted(Counter(margini).items())) + ".",
          f"- Round da cui il vincitore non è più dietro: media **{statistics.mean(decide_r):.1f}**, mediana {statistics.median(decide_r)}; "
          f"mai dietro (round 1): {pct(sum(1 for x in decide_r if x == 1), len(decide_r))}.", "",
          "| Leader | Partite | Vittorie | Rimonte (sul totale delle sue vittorie) | Cambi di comando a partita |", "|---|---|---|---|---|"]
    for d in DECKS:
        x = P[d]
        L.append(f"| {LBL[d]} | {int(x['n'])} | {pct(x['vinte_tot'], x['n'])} | {pct(x['rimonte'], x['vinte'])} | {x['cambi'] / max(x['n'], 1):.2f} |")
    # F4
    rc = Counter(rounds)
    L += ["", "## F4. Ritmo", "",
          f"- Round finale: media **{statistics.mean(rounds):.1f}**, mediana {statistics.median(rounds)}; "
          f"round 13+ **{pct(sum(1 for x in rounds if x >= 13), n)}**; oltre il 15 {pct(sum(1 for x in rounds if x > 15), n)}.",
          "- Distribuzione: " + ", ".join(f"R{k}: {v}" for k, v in sorted(rc.items())) + ".",
          "- Fine partita: " + ", ".join(f"{k} {pct(v, n)}" for k, v in ends.most_common()) + ".",
          f"- Round consecutivi senza Vite perse (da nessuno dei due): serie più lunga per partita media **{statistics.mean(run_max):.1f}** "
          f"(massimo {max(run_max)}); lunghezza media di una serie {statistics.mean(run_mean) if run_mean else 0:.1f}.",
          f"- Colpi a segno sul Leader per round (somma dei due giocatori): **{T['colpi'] / T['rounds']:.2f}**.", ""]
    # F5
    L += ["## F5. Varietà", "",
          "| Leader | Unità giocate | Tattiche | Reliquie | Reazioni | Attacchi del Leader | Rimarginare | Attacchi totali | Colpi al Leader avversario |",
          "|---|---|---|---|---|---|---|---|---|"]
    for d in DECKS:
        x = P[d]; k = max(x["n"], 1)
        L.append(f"| {LBL[d]} | {x['gioca_unit'] / k:.1f} | {x['gioca_tactic'] / k:.1f} | {x['gioca_relic'] / k:.1f} | {x['reazioni'] / k:.1f} | "
                 f"{x['att_leader'] / k:.1f} | {x['rim'] / k:.2f} | {x['attacchi'] / k:.1f} | {x['colpi'] / k:.1f} |")
    L += ["", "Reazioni = Reazioni giocate in difesa (contatore `reactions`); le altre colonne contano le carte giocate nella fase principale.", "",
          "**Carte delle liste giocate meno di 0.1 volte a partita (copie nella lista):**", ""]
    for d in DECKS:
        k = max(P[d]["n"], 1)
        cnt = Counter(lista[d])
        rare = [f"{c} ×{cnt[c]} ({played[d][c] / k:.2f})" for c in sorted(cnt) if C[c].type != "reaction" and played[d][c] / k < 0.1]
        L.append(f"- {LBL[d]}: " + (", ".join(rare) or "nessuna"))
    L += ["", "Le Reazioni sono escluse: si giocano in difesa e `cards_played` non le conta.", ""]
    # F6
    L += ["## F6. Frustrazione", "",
          "| Leader | Turni senza nessuna carta giocabile alla prima scelta | Turni con mano ≥6 | … e nessuna carta giocabile |", "|---|---|---|---|"]
    for d in DECKS + ["Totale"]:
        x = T if d == "Totale" else P[d]
        tt = max(x["turni"], 1)
        L.append(f"| {LBL.get(d, d)} | {pct(x['blocc'], tt)} | {pct(x['piena'], tt)} | {pct(x['piena_blocc'], max(x['piena'], 1))} |")
    L += ["", f"- Partite decise presto: chi è avanti nelle Vite all'inizio del round 7 (fine del round 6) vince **{pct(T['r6_ok'], T['r6_n'])}** "
          f"(su {int(T['r6_n'])} partite non in parità a quel punto).",
          "- \"Mano piena\" = almeno 6 carte (il limite di mano è 8). \"Nessuna carta giocabile\" = nessuna azione «gioca» legale alla prima scelta "
          "(gemme insufficienti, nessun bersaglio, costo non pagabile).",
          "- Minacce senza risposta: non si ricava dai log senza una definizione di minaccia; non misurata.", ""]
    open(os.path.join(a.out, "metriche_F.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    out.update({"T": dict(T), "P": {d: dict(P[d]) for d in DECKS}, "rounds": rounds, "margini": margini, "decide_r": decide_r})
    json.dump(out, open(os.path.join(a.out, "metriche_F.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print("\n".join(L))


if __name__ == "__main__":
    main()
