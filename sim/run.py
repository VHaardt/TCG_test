"""Mass simulation and standard report.

Examples
  python -m sim.run torneo --games 200                    # round robin of all decks, IA semplice
  python -m sim.run torneo --games 100 --agents forte:200 # same with the strong AI
  python -m sim.run varianti --games 200 --variants default V1b_per_attack V2_g2_six
  python -m sim.run ia --games 60                          # control test: forte vs semplice
  python -m sim.run partita arden_rosso_verde maera_blu_nero --seed 3   # readable replay
Reports (markdown + json) are written to reports/."""
import argparse
import glob
import json
import math
import os
import random
import statistics
import sys
import time
from multiprocessing import Pool

from .agents import make_agent
from .cards import CARDS, LEADERS, check_deck
from .config import DEFAULT, VARIANTS, rules_for
from .engine import RULES_VERSION, new_game

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DECK_DIR = os.path.join(ROOT, "sim", "decks")
REPORT_DIR = os.path.join(ROOT, "reports")


# ---------------------------------------------------------------------------- decks
def load_deck(name):
    with open(os.path.join(DECK_DIR, name + ".json"), encoding="utf-8") as f:
        d = json.load(f)
    cards = [cid for cid, n in d["cards"].items() for _ in range(n)]
    problems = check_deck(d["leader"], cards)
    if problems:
        raise ValueError(f"mazzo {name} illegale: {problems}")
    return d["leader"], cards


def all_decks():
    """Reference decks (files starting with '_' such as the trap deck are excluded)."""
    names = (os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(DECK_DIR, "*.json")))
    return sorted(n for n in names if not n.startswith("_"))


def cards_version():
    """Short hash of the card database, printed in every report."""
    import hashlib
    from .cards import DATA_DIR
    h = hashlib.sha1()
    for path in sorted(glob.glob(os.path.join(DATA_DIR, "*.json"))):
        with open(path, "rb") as f:
            h.update(f.read())
    return h.hexdigest()[:10]


# ---------------------------------------------------------------------------- games
def play_game(job):
    deck_names, agent_specs, rules, seed, keep_log = job
    (l1, d1), (l2, d2) = load_deck(deck_names[0]), load_deck(deck_names[1])
    agents = [make_agent(agent_specs[0], seed=seed * 2 + 1), make_agent(agent_specs[1], seed=seed * 2 + 2)]
    s = new_game(l1, d1, l2, d2, rules=rules, seed=seed, log=True)
    steps = 0
    while not s.over:
        s.step(agents[s.decider()].act(s))
        steps += 1
        if steps > 20000:
            s.end_reason = "loop"
            break
    return {
        "decks": list(deck_names), "agents": list(agent_specs), "seed": seed,
        "winner": s.winner, "end_reason": s.end_reason,
        "rounds": s.p[0].turn_no, "turns": [s.p[0].turn_no, s.p[1].turn_no],
        "life_end": [len(s.p[0].life), len(s.p[1].life)],
        "stats": s.stats,
        "log": s.log if (keep_log or seed % 1000 == 0 or s.end_reason not in ("colpo_finale", "crepuscolo", "mazzo_vuoto")
                         or not 5 <= s.p[0].turn_no <= 15) else None,
    }


def run_jobs(jobs, workers=None):
    workers = workers or max(1, (os.cpu_count() or 2))
    if workers == 1 or len(jobs) < 8:
        return [play_game(j) for j in jobs]
    with Pool(workers) as pool:
        return pool.map(play_game, jobs, chunksize=max(1, len(jobs) // (workers * 4)))


def match_jobs(deck_a, deck_b, agent_a, agent_b, rules, games, seed0=0):
    """Alternate seats so each deck/agent is G1 in half of the games."""
    jobs = []
    for g in range(games):
        if g % 2 == 0:
            jobs.append(((deck_a, deck_b), (agent_a, agent_b), rules, seed0 + g, False))
        else:
            jobs.append(((deck_b, deck_a), (agent_b, agent_a), rules, seed0 + g, False))
    return jobs


# ---------------------------------------------------------------------------- statistics
def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"), float("nan"))
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (p, max(0.0, c - h), min(1.0, c + h))


def median_ci(xs, reps=400, rng=random.Random(0)):
    if not xs:
        return (float("nan"),) * 3
    med = statistics.median(xs)
    boots = sorted(statistics.median(rng.choices(xs, k=len(xs))) for _ in range(reps))
    return (med, boots[int(0.025 * reps)], boots[int(0.975 * reps) - 1])


def pct(t):
    p, lo, hi = t
    return f"{100*p:.1f}% [{100*lo:.1f}–{100*hi:.1f}]"


def check(ok):
    return "✅" if ok else "❌"


def metrics(records):
    n = len(records)
    rounds = [r["rounds"] for r in records]
    in_range = sum(1 for x in rounds if 5 <= x <= 15)
    g1_wins = sum(1 for r in records if r["winner"] == 0)
    decided = sum(1 for r in records if r["winner"] is not None)
    # comebacks: someone >= 2 Vite behind at round 6 and still won
    behind, comeback = 0, 0
    for r in records:
        lf = r["stats"]["life_at_round6"]
        if lf is None:
            continue
        if abs(lf[0] - lf[1]) >= 2:
            behind += 1
            loser_then = 0 if lf[0] < lf[1] else 1
            if r["winner"] == loser_then:
                comeback += 1
    threats = sum(sum(r["stats"]["threats_at_reaction"]) for r in records)
    stopped = sum(sum(r["stats"]["stopped_by_reaction"]) for r in records)
    att_l = sum(sum(r["stats"]["attacks_leader"]) for r in records)
    hits = sum(sum(r["stats"]["hits_leader"]) for r in records)
    antistall = sum(1 for r in records if r["end_reason"] == "crepuscolo"
                    or sum(r["stats"]["lives_lost"][q].get("crepuscolo", 0) for q in (0, 1)) > 0)
    closed_by_stall = sum(1 for r in records if r["end_reason"] == "crepuscolo")
    rim_used = sum(sum(r["stats"]["rim_used"]) for r in records)
    rim_poss = sum(sum(r["stats"]["rim_possible"]) for r in records)
    lost_src = {}
    for r in records:
        for q in (0, 1):
            for k, v in r["stats"]["lives_lost"][q].items():
                lost_src[k] = lost_src.get(k, 0) + v
    lost_total = sum(lost_src.values()) or 1
    reactions = {}
    for r in records:
        for q in (0, 1):
            for k, v in r["stats"]["reactions"][q].items():
                reactions[k] = reactions.get(k, 0) + v
    guard = sum(sum(r["stats"]["guard_stored"]) for r in records)
    tend = sum(sum(r["stats"]["turns_ended"]) for r in records) or 1
    ends = {}
    for r in records:
        ends[r["end_reason"]] = ends.get(r["end_reason"], 0) + 1
    ge13 = sum(1 for x in rounds if x >= 13)
    clessidra = sum(1 for x in rounds if x >= DEFAULT.saldo_late_turn)
    ghist = {}
    for r in records:
        for q in (0, 1):
            for k, v in r["stats"]["guard_hist"][q].items():
                ghist[int(k)] = ghist.get(int(k), 0) + v
    return {
        "n": n,
        "rounds_ge13": wilson(ge13, n),
        "clessidra_active": wilson(clessidra, n),
        "guard_hist": dict(sorted(ghist.items())),
        "rounds_median": median_ci(rounds),
        "rounds_mean": statistics.mean(rounds) if rounds else float("nan"),
        "rounds_in_5_15": wilson(in_range, n),
        "rounds_over_15": wilson(sum(1 for x in rounds if x > 15), n),
        "rounds_hist": {x: rounds.count(x) for x in sorted(set(rounds))},
        "g1_win": wilson(g1_wins, decided),
        "comeback": wilson(comeback, behind), "comeback_n": behind,
        "stopped_by_reaction": wilson(stopped, threats), "threats": threats,
        "hit_rate": wilson(hits, att_l),
        "closed_by_stall": wilson(closed_by_stall, n),
        "touched_by_stall": wilson(antistall, n),
        "rim_rate": wilson(rim_used, rim_poss),
        "lives_lost_by_source": {k: v / lost_total for k, v in sorted(lost_src.items(), key=lambda x: -x[1])},
        "leader_attack_share": lost_src.get("attacco_leader", 0) / lost_total,
        "reactions": reactions,
        "guard_per_turn": guard / tend,
        "end_reasons": ends,
    }


def deck_winrates(records):
    out = {}
    for r in records:
        for seat in (0, 1):
            d = r["decks"][seat]
            if r["decks"][0] == r["decks"][1]:
                continue
            w, n = out.get(d, (0, 0))
            out[d] = (w + (1 if r["winner"] == seat else 0), n + 1)
    return {d: wilson(w, n) for d, (w, n) in out.items()}


def g1_by_deck(records):
    """First-player win rate in mirror matches, per deck."""
    out = {}
    for r in records:
        if r["decks"][0] != r["decks"][1] or r["winner"] is None:
            continue
        w, n = out.get(r["decks"][0], (0, 0))
        out[r["decks"][0]] = (w + (r["winner"] == 0), n + 1)
    return {d: wilson(w, n) for d, (w, n) in out.items()}


def matchup_matrix(records):
    m = {}
    for r in records:
        a, b = r["decks"]
        if a == b or r["winner"] is None:
            continue
        for row, col, seat in ((a, b, 0), (b, a, 1)):
            w, n = m.get((row, col), (0, 0))
            m[(row, col)] = (w + (r["winner"] == seat), n + 1)
    return m


def card_stats(records):
    """Per card: games in which it was drawn, % of those in which it was played,
    win rate when played, win rate when drawn but never played ("dead")."""
    acc = {}
    for r in records:
        for seat in (0, 1):
            drawn = r["stats"]["cards_drawn"][seat]
            played = r["stats"]["cards_played"][seat]
            won = r["winner"] == seat
            for cid in set(drawn) | set(played):
                a = acc.setdefault(cid, {"drawn": 0, "played": 0, "won_played": 0, "dead": 0, "won_dead": 0,
                                         "copies_played": 0})
                a["drawn"] += 1
                if played.get(cid):
                    a["played"] += 1
                    a["copies_played"] += played[cid]
                    a["won_played"] += won
                else:
                    a["dead"] += 1
                    a["won_dead"] += won
    rows = []
    for cid, a in acc.items():
        rows.append({
            "id": cid, "name": CARDS[cid].name, "games_drawn": a["drawn"],
            "play_rate": a["played"] / a["drawn"] if a["drawn"] else 0,
            "win_when_played": a["won_played"] / a["played"] if a["played"] else float("nan"),
            "win_when_dead": a["won_dead"] / a["dead"] if a["dead"] else float("nan"),
        })
    rows.sort(key=lambda x: -(x["win_when_played"] if x["win_when_played"] == x["win_when_played"] else 0))
    return rows


# ---------------------------------------------------------------------------- report
def rules_digest(rules):
    diff = {k: v for k, v in rules.as_dict().items() if DEFAULT.as_dict().get(k) != v}
    return diff


def render(title, records, rules, extra="", agents=None, elapsed=None):
    m = metrics(records)
    dw = deck_winrates(records)
    lines = [f"# {title}", ""]
    lines.append(f"- Regole: `{RULES_VERSION}`; moduli attivi: {', '.join(rules.modules)}")
    lines.append(f"- Versione carte: `{cards_version()}`; seed: {min(r['seed'] for r in records)}–{max(r['seed'] for r in records)}")
    diff = rules_digest(rules)
    lines.append(f"- Parametri diversi dal default: {json.dumps(diff, ensure_ascii=False) if diff else 'nessuno'}")
    lines.append(f"- Partite: {m['n']}; IA: {agents or '?'}" + (f"; tempo {elapsed:.0f}s" if elapsed else ""))
    lines.append("- Tra parentesi quadre: intervallo di confidenza al 95%.")
    lines.append("")
    lines.append("## Metriche dei pilastri")
    lines.append("| Metrica | Valore | Obiettivo | |")
    lines.append("|---|---|---|---|")
    med = m["rounds_median"]
    lines.append(f"| Durata mediana (turni per giocatore) | {med[0]:.1f} [{med[1]:.1f}–{med[2]:.1f}] (media {m['rounds_mean']:.1f}) | 8–10 | {check(8 <= med[0] <= 10)} |")
    lines.append(f"| Partite tra 5 e 15 turni | {pct(m['rounds_in_5_15'])} | ≥90% | {check(m['rounds_in_5_15'][0] >= 0.9)} |")
    lines.append(f"| Partite arrivate al turno 13 | {pct(m['rounds_ge13'])} | <10% | {check(m['rounds_ge13'][0] < 0.1)} |")
    lines.append(f"| Clessidra attiva a fine partita (turno ≥{DEFAULT.saldo_late_turn}) | {pct(m['clessidra_active'])} | <15% | {check(m['clessidra_active'][0] < 0.15)} |")
    lines.append(f"| Partite oltre il turno 15 | {pct(m['rounds_over_15'])} | <2% | {check(m['rounds_over_15'][0] < 0.02)} |")
    lines.append(f"| Vittorie del primo giocatore | {pct(m['g1_win'])} | 48–52% | {check(0.48 <= m['g1_win'][0] <= 0.52)} |")
    lines.append(f"| Rimonte (sotto di ≥2 Vite al turno 6, n={m['comeback_n']}) | {pct(m['comeback'])} | 20–35% | {check(0.2 <= m['comeback'][0] <= 0.35)} |")
    lines.append(f"| Attacchi al Leader fermati da una reazione (su {m['threats']} minacce) | {pct(m['stopped_by_reaction'])} | 30–45% | {check(0.3 <= m['stopped_by_reaction'][0] <= 0.45)} |")
    lines.append(f"| Partite chiuse dal Crepuscolo | {pct(m['closed_by_stall'])} | <15% | {check(m['closed_by_stall'][0] < 0.15)} |")
    lines.append(f"| Rimarginare usato quando possibile | {pct(m['rim_rate'])} | <70% | {check(m['rim_rate'][0] < 0.7)} |")
    lines.append(f"| Quota di Vite perse per attacchi del Leader | {100*m['leader_attack_share']:.1f}% | <40% | {check(m['leader_attack_share'] < 0.4)} |")
    if dw:
        lines.append("")
        lines.append("## Vittorie per mazzo (escluse le partite speculari)")
        lines.append("| Mazzo | Vittorie | Obiettivo 45–55% |")
        lines.append("|---|---|---|")
        for d, t in sorted(dw.items(), key=lambda x: -x[1][0]):
            lines.append(f"| {d} | {pct(t)} | {check(0.45 <= t[0] <= 0.55)} |")
    g1d = g1_by_deck(records)
    if g1d:
        lines.append("")
        lines.append("## Vittorie del primo giocatore nelle partite speculari")
        lines.append("| Mazzo | G1 vince | Obiettivo 48–52% |")
        lines.append("|---|---|---|")
        for d, t in sorted(g1d.items()):
            lines.append(f"| {d} | {pct(t)} | {check(0.48 <= t[0] <= 0.52)} |")
    mm = matchup_matrix(records)
    if mm:
        names = sorted({k[0] for k in mm})
        lines.append("")
        lines.append("## Matrice degli abbinamenti (% vittorie della riga)")
        lines.append("| | " + " | ".join(names) + " |")
        lines.append("|---" * (len(names) + 1) + "|")
        for a in names:
            cells = []
            for b in names:
                if (a, b) in mm:
                    w, n = mm[(a, b)]
                    cells.append(f"{100*w/n:.0f}%")
                else:
                    cells.append("–")
            lines.append(f"| {a} | " + " | ".join(cells) + " |")
    lines.append("")
    lines.append("## Dettagli")
    lines.append(f"- Fine partita: {json.dumps(m['end_reasons'])}")
    lines.append(f"- Durata (turni per giocatore → partite): {json.dumps(m['rounds_hist'])}")
    lines.append(f"- Attacchi al Leader andati a segno: {pct(m['hit_rate'])}")
    lines.append(f"- Partite toccate dal Crepuscolo terminale: {pct(m['touched_by_stall'])}")
    lines.append(f"- Vite perse per fonte: " + ", ".join(f"{k} {100*v:.0f}%" for k, v in m["lives_lost_by_source"].items()))
    lines.append(f"- Reazioni usate: {json.dumps(m['reactions'], ensure_ascii=False)}")
    lines.append(f"- Guardia accantonata in media per turno: {m['guard_per_turn']:.2f}; distribuzione (Guardia → turni): {json.dumps(m['guard_hist'])}")
    cs = card_stats(records)
    lines.append("")
    lines.append("## Statistiche per carta")
    lines.append("| Carta | Partite in cui pescata | Giocata quando pescata | Vittorie se giocata | Vittorie se rimasta in mano |")
    lines.append("|---|---|---|---|---|")
    for row in cs:
        wp = row["win_when_played"]
        wd = row["win_when_dead"]
        lines.append(f"| {row['name']} | {row['games_drawn']} | {100*row['play_rate']:.0f}% | "
                     f"{'–' if wp != wp else f'{100*wp:.0f}%'} | {'–' if wd != wd else f'{100*wd:.0f}%'} |")
    if extra:
        lines += ["", extra]
    return "\n".join(lines) + "\n", m


def save(name, text, records, meta, out_dir=None):
    out_dir = out_dir or REPORT_DIR
    os.makedirs(out_dir, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    base = os.path.join(out_dir, f"{stamp}_{name}")
    logs = [r for r in records if r.get("log")]
    if logs:
        with open(base + "_replay.txt", "w", encoding="utf-8") as f:
            for r in logs:
                f.write(f"===== seed {r['seed']} | {r['decks'][0]} (P1) vs {r['decks'][1]} (P2) | "
                        f"{r['end_reason']} | turni {r['turns']}\n")
                f.write("\n".join(r["log"]) + "\n\n")
    with open(base + ".md", "w", encoding="utf-8") as f:
        f.write(text)
    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump({"meta": meta, "records": [{k: v for k, v in r.items() if k != "log"} for r in records]}, f)
    return base + ".md"


# ---------------------------------------------------------------------------- commands
def tournament(rules, agents, games, decks=None, seed0=0, workers=None, mirrors=True):
    decks = decks or all_decks()
    jobs = []
    k = 0
    for i, a in enumerate(decks):
        for b in decks[i:]:
            if a == b and not mirrors:
                continue
            jobs += match_jobs(a, b, agents, agents, rules, games, seed0=seed0 + 100000 * k)
            k += 1
    return run_jobs(jobs, workers)


def cmd_torneo(args):
    rules = rules_for(args.variant)
    t = time.time()
    recs = tournament(rules, args.agents, args.games, args.decks, workers=args.workers)
    text, _ = render(f"Torneo — variante {args.variant}", recs, rules, agents=args.agents, elapsed=time.time() - t)
    path = save(f"torneo_{args.variant}", text, recs, {"variant": args.variant, "agents": args.agents})
    print(text)
    print("report:", path)


def cmd_varianti(args):
    rows = []
    t0 = time.time()
    all_text = ["# Confronto varianti", "",
                f"IA: {args.agents}; {args.games} partite per abbinamento (torneo completo con specchi).", ""]
    for v in args.variants:
        rules = rules_for(v)
        t = time.time()
        recs = tournament(rules, args.agents, args.games, args.decks, workers=args.workers)
        text, m = render(f"Variante {v}", recs, rules, agents=args.agents, elapsed=time.time() - t)
        save(f"variante_{v}", text, recs, {"variant": v, "agents": args.agents})
        dw = deck_winrates(recs)
        spread = max(x[0] for x in dw.values()) - min(x[0] for x in dw.values()) if dw else float("nan")
        rows.append((v, m, spread))
    all_text.append("| Variante | Durata mediana | 5–15 turni | G1 vince | Rimonte | Fermati da reazione | Chiuse dal Crepuscolo | Rimarginare | Scarto vittorie tra mazzi |")
    all_text.append("|---|---|---|---|---|---|---|---|---|")
    for v, m, spread in rows:
        all_text.append(f"| {v} | {m['rounds_median'][0]:.1f} | {pct(m['rounds_in_5_15'])} | {pct(m['g1_win'])} | "
                        f"{pct(m['comeback'])} | {pct(m['stopped_by_reaction'])} | {pct(m['closed_by_stall'])} | "
                        f"{pct(m['rim_rate'])} | {100*spread:.0f} punti |")
    text = "\n".join(all_text) + f"\n\nTempo totale {time.time()-t0:.0f}s.\n"
    path = save("confronto_varianti", text, [], {"variants": args.variants})
    print(text)
    print("report:", path)


def cmd_ia(args):
    """AI control (strategia §6): strong AI must beat the simple one >= 65%."""
    rules = rules_for(args.variant)
    decks = args.decks or all_decks()
    jobs = []
    k = 0
    for a in decks:
        for b in decks:
            jobs += match_jobs(a, b, args.strong, "semplice", rules, args.games, seed0=500000 + 1000 * k)
            k += 1
    t = time.time()
    recs = run_jobs(jobs, args.workers)
    wins = sum(1 for r in recs if r["winner"] is not None and r["agents"][r["winner"]] == args.strong)
    res = wilson(wins, len(recs))
    text = (f"# Controllo dell'IA\n\nIA forte `{args.strong}` contro IA semplice, {len(recs)} partite "
            f"(tutti gli abbinamenti, posti alternati).\n\n- Vittorie dell'IA forte: {pct(res)} "
            f"(obiettivo ≥65%: {check(res[0] >= 0.65)})\n- Tempo: {time.time()-t:.0f}s\n")
    path = save("controllo_ia", text, recs, {"strong": args.strong})
    print(text)
    print("report:", path)


def cmd_trappola(args):
    """Trap-deck check (strategia §6): the deck with the broken card must win > 80%
    against every reference deck, otherwise the AI does not see what is strong."""
    rules = rules_for(args.variant)
    decks = args.decks or all_decks()
    lines = [f"# Controllo mazzo trappola", "",
             f"IA `{args.agents}` per entrambi i lati, {args.games} partite per mazzo (posti alternati).", "",
             "| Avversario | Vittorie trappola | ≥80% | Vittorie se il Titano è stato giocato | Partite senza Titano |",
             "|---|---|---|---|---|"]
    t = time.time()
    all_recs = []
    for k, d in enumerate(decks):
        recs = run_jobs(match_jobs("_trappola", d, args.agents, args.agents, rules, args.games,
                                   seed0=700000 + 1000 * k), args.workers)
        all_recs += recs
        wins = sum(1 for r in recs if r["winner"] is not None and r["decks"][r["winner"]] == "_trappola")
        res = wilson(wins, len(recs))
        seat = [r["decks"].index("_trappola") for r in recs]
        played = [r for r, q in zip(recs, seat) if r["stats"]["cards_played"][q].get("x_titano")]
        pw = sum(1 for r in played if r["winner"] is not None and r["decks"][r["winner"]] == "_trappola") if played else 0
        lines.append(f"| {d} | {pct(res)} | {check(res[0] > 0.80)} | {pct(wilson(pw, len(played)))} | "
                     f"{100*(1-len(played)/len(recs)):.0f}% |")
    text = "\n".join(lines) + f"\n\nTempo: {time.time()-t:.0f}s\n"
    path = save(f"trappola_{args.agents.replace(':', '')}", text, all_recs, {"agents": args.agents})
    print(text)
    print("report:", path)


def cmd_partita(args):
    rules = rules_for(args.variant)
    r = play_game(((args.deck1, args.deck2), (args.agent1, args.agent2), rules, args.seed, True))
    print("\n".join(r["log"]))
    print(f"\nVincitore: P{r['winner']+1 if r['winner'] is not None else '-'} ({r['end_reason']}), turni {r['turns']}")


def main(argv=None):
    p = argparse.ArgumentParser(prog="python -m sim.run")
    sub = p.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("torneo")
    t.add_argument("--games", type=int, default=200)
    t.add_argument("--agents", default="semplice")
    t.add_argument("--variant", default="default", choices=sorted(VARIANTS))
    t.add_argument("--decks", nargs="*")
    t.add_argument("--workers", type=int)
    v = sub.add_parser("varianti")
    v.add_argument("--games", type=int, default=200)
    v.add_argument("--agents", default="semplice")
    v.add_argument("--variants", nargs="+", default=sorted(VARIANTS))
    v.add_argument("--decks", nargs="*")
    v.add_argument("--workers", type=int)
    i = sub.add_parser("ia")
    i.add_argument("--games", type=int, default=10)
    i.add_argument("--strong", default="forte:200")
    i.add_argument("--variant", default="default", choices=sorted(VARIANTS))
    i.add_argument("--decks", nargs="*")
    i.add_argument("--workers", type=int)
    tr = sub.add_parser("trappola")
    tr.add_argument("--games", type=int, default=50)
    tr.add_argument("--agents", default="semplice")
    tr.add_argument("--variant", default="default", choices=sorted(VARIANTS))
    tr.add_argument("--decks", nargs="*")
    tr.add_argument("--workers", type=int)
    g = sub.add_parser("partita")
    g.add_argument("deck1")
    g.add_argument("deck2")
    g.add_argument("--agent1", default="semplice")
    g.add_argument("--agent2", default="semplice")
    g.add_argument("--seed", type=int, default=0)
    g.add_argument("--variant", default="default", choices=sorted(VARIANTS))
    args = p.parse_args(argv)
    {"torneo": cmd_torneo, "varianti": cmd_varianti, "ia": cmd_ia, "trappola": cmd_trappola, "partita": cmd_partita}[args.cmd](args)


if __name__ == "__main__":
    main()
