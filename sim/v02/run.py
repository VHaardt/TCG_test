"""Experiments for the v0.2 core (Q-013, esperimento.md).

  python -m sim.v02.run partita arden_rosso_verde maera_blu_nero --seed 3
  python -m sim.v02.run torneo --variante B0 --partite 100
  python -m sim.v02.run ab --base B0 --variante V1B_sequenziale --partite 2500 --out <cartella>
  python -m sim.v02.run lambda --partite 400            # taratura del prezzo-ombra
  python -m sim.v02.run collaudo --partite 1000         # sfruttabilita del pugno
  python -m sim.v02.run forte --variante B0 --partite 100 --forte forte:60

Every arm plays the same jobs (decks, seats, seeds): differences come from the rules."""
import argparse
import json
import os
import statistics
import time
from multiprocessing import Pool

from ..run import load_deck, all_decks, wilson, median_ci, pct, check
from .agents import make_agent
from .config import rules_from, B0
from .engine import new_game, RULES_VERSION

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORT_DIR = os.path.join(ROOT, "reports", "v02")


def play_game(job):
    decks, agents_spec, spec, seed, keep_log = job
    rules = rules_from(spec)
    (l1, d1), (l2, d2) = load_deck(decks[0]), load_deck(decks[1])
    agents = [make_agent(agents_spec[0], seed=seed * 2 + 1), make_agent(agents_spec[1], seed=seed * 2 + 2)]
    s = new_game(l1, d1, l2, d2, rules=rules, seed=seed, log=keep_log)
    steps = 0
    while not s.over and steps < 5000:
        s.step(agents[s.decider()].act(s))
        steps += 1
    if not s.over:
        s.end_reason = "loop"
    return {"decks": list(decks), "agents": list(agents_spec), "seed": seed, "winner": s.winner,
            "end_reason": s.end_reason, "rounds": s.round, "life_end": [len(s.p[0].life), len(s.p[1].life)],
            "stats": s.stats, "log": s.log}


def run_jobs(jobs, workers=None):
    workers = workers or os.cpu_count() or 2
    if workers == 1 or len(jobs) < 8:
        return [play_game(j) for j in jobs]
    with Pool(workers) as pool:
        return pool.map(play_game, jobs, chunksize=max(1, len(jobs) // (workers * 8)))


def mirror_jobs(spec, agent, games, decks=None, seed0=1, agent2=None):
    """Mirror matches (same deck both sides) for every reference deck, seats alternate."""
    jobs = []
    decks = decks or all_decks()
    for k, d in enumerate(decks):
        for g in range(games):
            s = seed0 * 1_000_000 + 10_000 * k + g
            if agent2 is None:
                jobs.append(((d, d), (agent, agent), spec, s, False))
            elif g % 2 == 0:
                jobs.append(((d, d), (agent, agent2), spec, s, False))
            else:
                jobs.append(((d, d), (agent2, agent), spec, s, False))
    return jobs


def cross_jobs(spec, agent, games, decks=None, seed0=1):
    jobs = []
    decks = decks or all_decks()
    k = 0
    for i, x in enumerate(decks):
        for y in decks[i + 1:]:
            for g in range(games):
                s = seed0 * 1_000_000 + 500_000 + 10_000 * k + g
                jobs.append((((x, y) if g % 2 == 0 else (y, x)), (agent, agent), spec, s, False))
            k += 1
    return jobs


# ---------------------------------------------------------------------------- metrics
def metrics(recs):
    n = len(recs)
    m = {"n": n}
    rounds = [r["rounds"] for r in recs]
    m["rounds_median"] = median_ci(rounds)
    m["rounds_mean"] = statistics.mean(rounds)
    m["rounds_ge13"] = wilson(sum(x >= 13 for x in rounds), n)
    m["rounds_over15"] = wilson(sum(x > 15 for x in rounds), n)
    m["rounds_out_5_15"] = wilson(sum(not 5 <= x <= 15 for x in rounds), n)
    m["early_win"] = wilson(sum(r["rounds"] < 5 and r["winner"] is not None for r in recs), n)
    mir = [r for r in recs if r["decks"][0] == r["decks"][1] and r["agents"][0] == r["agents"][1]]
    m["g1_win"] = wilson(sum(r["winner"] == 0 for r in mir), len(mir))
    att = sum(sum(r["stats"]["attacks"]) for r in recs)
    stopped = sum(sum(r["stats"]["stopped"]) for r in recs)
    m["attacks"] = att
    m["stopped"] = wilson(stopped, att)
    m["opposed"] = wilson(sum(sum(r["stats"]["opposed"]) for r in recs), att)
    m["leader_hit"] = wilson(sum(sum(r["stats"]["attacks_leader_hit"]) for r in recs), att)
    m["attacks_per_game"] = att / max(n, 1)
    cb = [r for r in recs if r["stats"]["life_at_round6"]]
    behind = [(r, 0 if r["stats"]["life_at_round6"][0] < r["stats"]["life_at_round6"][1] else 1)
              for r in cb if abs(r["stats"]["life_at_round6"][0] - r["stats"]["life_at_round6"][1]) >= 2]
    m["comeback"] = wilson(sum(r["winner"] == q for r, q in behind), len(behind))
    m["comeback_n"] = len(behind)
    turns = sum(sum(r["stats"]["turns"]) for r in recs)
    m["idle"] = wilson(sum(sum(r["stats"]["idle_turns"]) for r in recs), turns)
    m["idle3"] = wilson(sum(sum(r["stats"]["idle3_turns"]) for r in recs), turns)
    for key in ("pugno_att", "pugno_def"):
        tot = [0, 0, 0, 0]
        for r in recs:
            for side in r["stats"][key]:
                tot = [a + b for a, b in zip(tot, side)]
        m[key + "_empty"] = wilson(tot[1], tot[0])
        m[key + "_full"] = wilson(tot[2], tot[0])
        m[key + "_gems"] = tot[3] / max(att, 1)
    m["reactions_per_combat"] = sum(sum(r["stats"]["reactions"]) for r in recs) / max(att, 1)
    mods = {}
    for r in recs:
        for k, v in r["stats"]["mods"].items():
            mods[int(k)] = mods.get(int(k), 0) + v
    m["mods_max"] = max(mods) if mods else 0
    m["mods_dist"] = dict(sorted(mods.items()))
    dec = sum(sum(r["stats"]["decisions"]) for r in recs)
    m["legal_per_decision"] = sum(sum(r["stats"]["legal_actions"]) for r in recs) / max(dec, 1)
    m["end_reasons"] = {}
    for r in recs:
        m["end_reasons"][r["end_reason"]] = m["end_reasons"].get(r["end_reason"], 0) + 1
    dw = {}
    for r in recs:
        for q in (0, 1):
            w = dw.setdefault(r["decks"][q], [0, 0])
            w[1] += 1
            w[0] += r["winner"] == q
    m["deck_win"] = {d: wilson(w, n_) for d, (w, n_) in dw.items()}
    return m


BANDS = {"stopped": (0.30, 0.45), "rounds_median": (8, 11), "rounds_ge13": (0, 0.12), "early_win": (0, 0)}


def in_bands(m):
    return (BANDS["stopped"][0] <= m["stopped"][0] <= BANDS["stopped"][1]
            and BANDS["rounds_median"][0] <= m["rounds_median"][0] <= BANDS["rounds_median"][1]
            and m["rounds_ge13"][0] <= BANDS["rounds_ge13"][1]
            and m["early_win"][0] == 0)


def render(title, m, spec, agents, elapsed):
    r = rules_from(spec)
    diff = {k: v for k, v in r.as_dict().items() if B0.as_dict()[k] != v}
    L = [f"# {title}", "",
         f"- Regole `{RULES_VERSION}`, configurazione `{spec}`; differenze da B0: {diff or 'nessuna'}",
         f"- IA: {agents}; partite: {m['n']}; tempo {elapsed:.0f}s", "",
         "| Metrica | Valore [IC 95%] | Fascia | Esito |", "|---|---|---|---|",
         f"| Attacchi fermati | {pct(m['stopped'])} | 30–45% | {check(0.30 <= m['stopped'][0] <= 0.45)} |",
         f"| Durata mediana (round) | {m['rounds_median'][0]:.1f} [{m['rounds_median'][1]:.1f}–{m['rounds_median'][2]:.1f}] (media {m['rounds_mean']:.2f}) | 8–11 | {check(8 <= m['rounds_median'][0] <= 11)} |",
         f"| Partite al round 13+ | {pct(m['rounds_ge13'])} | ≤12% | {check(m['rounds_ge13'][0] <= 0.12)} |",
         f"| Partite oltre il 15 | {pct(m['rounds_over15'])} | <2% | {check(m['rounds_over15'][0] < 0.02)} |",
         f"| Vittorie prima del round 5 | {pct(m['early_win'])} | 0 | {check(m['early_win'][0] == 0)} |",
         f"| G1 vince (mirror) | {pct(m['g1_win'])} | 48–52% | {check(0.48 <= m['g1_win'][0] <= 0.52)} |",
         f"| Rimonte (n={m['comeback_n']}) | {pct(m['comeback'])} | 20–35% | {check(0.20 <= m['comeback'][0] <= 0.35)} |",
         f"| Attacchi con opposizione | {pct(m['opposed'])} | 15–35% (V4) | |",
         f"| Turni con Unità Pronte ferme | {pct(m['idle'])} (con ≥3: {pct(m['idle3'])}) | ≤35% (V4) | |",
         f"| Attacchi a segno sul Leader | {pct(m['leader_hit'])} | | |",
         f"| Attacchi per partita | {m['attacks_per_game']:.1f} | | |",
         f"| Pugno attaccante vuoto / pieno | {pct(m['pugno_att_empty'])} / {pct(m['pugno_att_full'])} (gemme medie {m['pugno_att_gems']:.2f}) | non >90% | |",
         f"| Pugno difensore vuoto / pieno | {pct(m['pugno_def_empty'])} / {pct(m['pugno_def_full'])} (gemme medie {m['pugno_def_gems']:.2f}) | non >90% | |",
         f"| Reazioni per scontro | {m['reactions_per_combat']:.2f} | | |",
         f"| Modificatori per scontro (max; distribuzione) | {m['mods_max']}; {m['mods_dist']} | | |",
         f"| Azioni legali per decisione | {m['legal_per_decision']:.1f} | <60 | {check(m['legal_per_decision'] < 60)} |",
         f"| Fine partita | {m['end_reasons']} | | |",
         f"| Nelle fasce comuni | {'sì' if in_bands(m) else 'no'} | | |", "",
         "Vittorie per mazzo: " + ", ".join(f"{d} {pct(w)}" for d, w in sorted(m["deck_win"].items())), ""]
    return "\n".join(L) + "\n"


def save(name, text, recs, out_dir=None):
    out = out_dir or REPORT_DIR
    os.makedirs(out, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    path = os.path.join(out, f"{stamp}_{name}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    sample = next((r for r in recs if r.get("log")), None)
    if sample:
        with open(path.replace(".md", "_replay.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(sample["log"]))
    return path


def arm(spec, agent, games, decks=None, seed0=1, cross=0):
    jobs = mirror_jobs(spec, agent, games, decks, seed0)
    if cross:
        jobs += cross_jobs(spec, agent, cross, decks, seed0)
    jobs[0] = jobs[0][:4] + (True,)
    t = time.time()
    recs = run_jobs(jobs)
    return recs, time.time() - t


def diff_line(label, key, ma, mb, scale=100, unit="punti"):
    (pa, la, ha), (pb, lb, hb) = ma[key], mb[key]
    d = pb - pa
    se = ((ha - la) ** 2 + (hb - lb) ** 2) ** 0.5 / (2 * 1.96)
    return f"| {label} | {scale*pa:.1f} | {scale*pb:.1f} | {scale*d:+.1f} [{scale*(d-1.96*se):+.1f}, {scale*(d+1.96*se):+.1f}] {unit} |"


def cmd_ab(a):
    out = a.out
    res = {}
    for name, spec in (("A", a.base), ("B", a.variante)):
        recs, el = arm(spec, a.ia, a.partite, a.mazzi, a.seed, a.incroci)
        m = metrics(recs)
        res[name] = (spec, m, recs)
        save(f"{name}_{spec.replace('/', '_')}", render(f"Braccio {name}: {spec}", m, spec, a.ia, el), recs, out)
    (sa, ma, ra), (sb, mb, rb) = res["A"], res["B"]
    rmean = lambda recs: statistics.mean(r["rounds"] for r in recs)
    import random as _r
    pairs = list(zip([r["rounds"] for r in ra], [r["rounds"] for r in rb]))
    rng = _r.Random(0)
    boots = sorted(statistics.mean(y - x for x, y in rng.choices(pairs, k=len(pairs))) for _ in range(400))
    L = [f"# Confronto A/B: `{sa}` (A) contro `{sb}` (B)", "",
         f"IA `{a.ia}`; {a.partite} partite mirror per mazzo"
         + (f" + {a.incroci} per incrocio" if a.incroci else "") + f"; seed {a.seed}; stesse partite nei due bracci.", "",
         "| Metrica | A | B | B − A [IC 95%] |", "|---|---|---|---|",
         diff_line("Attacchi fermati %", "stopped", ma, mb),
         diff_line("G1 vince %", "g1_win", ma, mb),
         diff_line("Round 13+ %", "rounds_ge13", ma, mb),
         diff_line("Rimonte %", "comeback", ma, mb),
         diff_line("Opposizioni %", "opposed", ma, mb),
         diff_line("Unità ferme %", "idle", ma, mb),
         f"| Durata media (round) | {rmean(ra):.2f} | {rmean(rb):.2f} | {rmean(rb)-rmean(ra):+.2f} [{boots[10]:+.2f}, {boots[389]:+.2f}] |",
         f"| Durata mediana | {ma['rounds_median'][0]:.1f} | {mb['rounds_median'][0]:.1f} | |",
         f"| Nelle fasce comuni | {'sì' if in_bands(ma) else 'no'} | {'sì' if in_bands(mb) else 'no'} | |", ""]
    text = "\n".join(L) + "\n"
    path = save("confronto", text, [], out)
    print(text)
    print("report:", path)


def cmd_torneo(a):
    recs, el = arm(a.variante, a.ia, a.partite, a.mazzi, a.seed, a.incroci)
    m = metrics(recs)
    text = render(f"Torneo v0.2 — {a.variante}", m, a.variante, a.ia, el)
    print(text)
    print("report:", save(f"torneo_{os.path.splitext(os.path.basename(a.variante))[0]}", text, recs, a.out))


def head_to_head(spec, x, y, games, decks=None, seed0=7):
    recs = run_jobs(mirror_jobs(spec, x, games, decks, seed0, agent2=y))
    w = sum(1 for r in recs if r["winner"] is not None and r["agents"][r["winner"]] == x)
    return wilson(w, len(recs)), recs


def cmd_lambda(a):
    L = [f"# Taratura del prezzo-ombra λ ({a.variante})", "",
         f"Ogni IA(λ) contro IA(0.012) (scala di evaluate() in probabilità di vittoria: la griglia 0.04–0.20 dello spec divisa per 10, vedi nota), mirror su tutti i mazzi, {a.partite} partite per mazzo.", "",
         "| λ | vittorie contro λ=0.012 | pugno attaccante vuoto / pieno | pugno difensore vuoto / pieno |", "|---|---|---|---|"]
    for lam in (0.004, 0.008, 0.016, 0.020):
        res, recs = head_to_head(a.variante, f"semplice@{lam}", "semplice@0.012", a.partite)
        m = metrics(recs)
        L.append(f"| {lam} | {pct(res)} | {pct(m['pugno_att_empty'])} / {pct(m['pugno_att_full'])} | "
                 f"{pct(m['pugno_def_empty'])} / {pct(m['pugno_def_full'])} |")
        print(L[-1], flush=True)
    text = "\n".join(L) + "\n"
    print("report:", save("taratura_lambda", text, [], a.out))


def cmd_collaudo(a):
    L = [f"# Collaudo del pugno ({a.variante}, IA `{a.ia}`)", "",
         "Sfruttabilità: un agente che conosce la distribuzione dell'IA e gioca la risposta pura migliore.", "",
         "| Prova | Vittorie dell'agente che sfrutta | Soglia | Esito |", "|---|---|---|---|"]
    lam = a.ia.partition("@")[2]
    br = "br" + (f"@{lam}" if lam else "")
    res, recs = head_to_head(a.variante, br, a.ia, a.partite)
    L.append(f"| contro IA in equilibrio | {pct(res)} | ≤52% | {check(res[0] <= 0.52)} |")
    det = "det" + (f"@{lam}" if lam else "")
    res2, _ = head_to_head(a.variante, br + ":det", det, a.partite)
    L.append(f"| contro IA deterministica (controllo del test) | {pct(res2)} | ≥60% | {check(res2[0] >= 0.60)} |")
    m = metrics(recs)
    L += ["", f"Degenerazione: pugno attaccante vuoto {pct(m['pugno_att_empty'])}, pieno {pct(m['pugno_att_full'])}; "
          f"difensore vuoto {pct(m['pugno_def_empty'])}, pieno {pct(m['pugno_def_full'])} (allarme oltre 90%)."]
    text = "\n".join(L) + "\n"
    print(text)
    print("report:", save("collaudo", text, recs, a.out))


def cmd_forte(a):
    res, recs = head_to_head(a.variante, a.forte, a.ia, a.partite)
    text = (f"# IA forte contro semplice ({a.variante})\n\n`{a.forte}` contro `{a.ia}`, mirror, {len(recs)} partite.\n\n"
            f"- Vittorie dell'IA forte: {pct(res)}; margine {100*(res[0]-0.5):+.1f} punti "
            f"[{100*(res[1]-0.5):+.1f}, {100*(res[2]-0.5):+.1f}]\n")
    print(text)
    print("report:", save(f"forte_{a.variante}", text, recs, a.out))


def cmd_partita(a):
    r = play_game(((a.mazzo1, a.mazzo2), (a.ia, a.ia), a.variante, a.seed, True))
    print("\n".join(r["log"]))
    print(f"\nVincitore: P{(r['winner'] or 0) + 1} ({r['end_reason']}), round {r['rounds']}")


def main(argv=None):
    p = argparse.ArgumentParser(prog="python -m sim.v02.run")
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(x, partite=100):
        x.add_argument("--variante", default="B0")
        x.add_argument("--ia", default="semplice")
        x.add_argument("--partite", type=int, default=partite)
        x.add_argument("--mazzi", nargs="*")
        x.add_argument("--incroci", type=int, default=0)
        x.add_argument("--seed", type=int, default=1)
        x.add_argument("--out")
    t = sub.add_parser("torneo"); common(t)
    ab = sub.add_parser("ab"); common(ab); ab.add_argument("--base", default="B0")
    lm = sub.add_parser("lambda"); common(lm, 200)
    co = sub.add_parser("collaudo"); common(co, 250)
    fo = sub.add_parser("forte"); common(fo, 25); fo.add_argument("--forte", default="forte:60")
    pa = sub.add_parser("partita"); common(pa); pa.add_argument("mazzo1"); pa.add_argument("mazzo2")
    a = p.parse_args(argv)
    {"torneo": cmd_torneo, "ab": cmd_ab, "lambda": cmd_lambda, "collaudo": cmd_collaudo,
     "forte": cmd_forte, "partita": cmd_partita}[a.cmd](a)


if __name__ == "__main__":
    main()
