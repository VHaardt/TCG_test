"""Experiments for the v0.2 core (Q-013, esperimento.md).

  python -m sim.v02.run partita arden_rosso_verde maera_blu_nero --seed 3
  python -m sim.v02.run torneo --variante B0 --partite 100
  python -m sim.v02.run ab --base B0 --variante V1B_sequenziale --partite 2500 --out <cartella>
  python -m sim.v02.run lambda --partite 400            # taratura del prezzo-ombra
  python -m sim.v02.run collaudo --partite 1000         # sfruttabilita del pugno
  python -m sim.v02.run forte --variante B0 --partite 100 --forte forte:60
  python -m sim.v02.run vita --partite 200              # M14: IA che paga sempre i costi in Vita
  python -m sim.v02.run valida set.json --mazzi mazzi.json   # controllo stretto di carte e mazzi
  python -m sim.v02.run torneo --carte set.json --mazzi mazzi.json   # un altro file di carte

Every arm plays the same jobs (decks, seats, seeds): differences come from the rules."""
import argparse
import json
import os
import statistics
import time
from multiprocessing import Pool

from ..run import wilson, median_ci, pct, check
from . import decks as D
from . import engine
from .agents import make_agent
from .config import rules_from, B0
from .engine import new_game, RULES_VERSION, CARDS, LEADERS, META
from .validate import validate

CARTE = [None]                      # --carte: file di carte usato da questo processo e dai worker

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORT_DIR = os.path.join(ROOT, "reports", "v02")


def use_cards(path):
    """Loads a card file (validated) in this process if it is not the current one."""
    path = os.path.abspath(path or engine.DATA)
    if engine.LOADED[0] != path:
        engine.load_cards(path)


def play_game(job):
    decks, agents_spec, spec, seed, keep_log = job[:5]
    use_cards(job[5] if len(job) > 5 else CARTE[0])
    rules = rules_from(spec)
    (l1, d1), (l2, d2) = D.load(decks[0]), D.load(decks[1])
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


def all_decks():
    return D.reference_decks()


def run_jobs(jobs, workers=None):
    jobs = [j[:5] + (CARTE[0],) for j in jobs]
    for ref in {d for j in jobs for d in j[0]}:          # errori chiari prima di partire
        D.load(ref)
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
    lh = [sum(r["stats"].get("leader_hits", [[0] * 4] * 2)[q][i] for r in recs for q in (0, 1)) for i in range(4)]
    m["leader_free"] = (wilson(lh[1], lh[0]), lh[0], wilson(lh[3], lh[2]), lh[2])     # Q-017
    m["leader_drain"] = wilson(lh[3], sum(sum(r["stats"]["attacks_leader_hit"]) for r in recs))   # Q-017 (Cr)
    both = [r for r in recs if all(x is not None for x in r["stats"]["awaken_round"])]
    m["r13_both_awak"] = (wilson(sum(r["rounds"] >= 13 for r in both), len(both)), len(both))    # Q-017 (Ne)
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
    m.update(r005_metrics(recs, att))
    return m


# ---------------------------------------------------------------------------- R-005, M1-M15
def deck_list(name):
    """(leader, {cid: copies}) read from the deck file, without the legality check."""
    return D.raw_deck(name)


def minor_colour(name):
    """(colour, cards of that colour, coloured cards): the Leader's colour with fewer cards in the deck."""
    lid, cards = deck_list(name)
    cols = LEADERS[lid].colors
    count = {c: sum(n for cid, n in cards.items() if c in CARDS[cid].colors) for c in cols}
    tot = sum(n for cid, n in cards.items() if set(CARDS[cid].colors) & set(cols))
    minor = min(cols, key=lambda c: count[c])
    return minor, count[minor], tot


def slots_of(cid):
    """Slot labels of a card for M15: the card id, plus "slot" from the card file, plus "caccia"."""
    tags = []
    for k in ("slot", "tags"):
        v = META.get(cid, {}).get(k) or []
        tags += [v] if isinstance(v, str) else list(v)
    if cid in CARDS and CARDS[cid].has("caccia"):
        tags.append("caccia")
    return tags


def r005_metrics(recs, att):
    m = {}
    tot = lambda key: sum(sum(r["stats"][key]) for r in recs)
    per_deck = lambda key: _per_deck(recs, key)
    att = max(att, 1)
    m["react_avail"] = tot("react_avail") / att                               # M1
    m["react_decisive"] = tot("react_decisive") / att                         # M2
    m["react_scar"] = per_deck("react_scar")                                  # M3 (per partita)
    m["react_scar_life"] = per_deck("react_scar_life")
    m["decided_pre"] = wilson(tot("decided_pre"), att)                        # M4
    hunt = tot("hunt")                                                        # M5
    m["hunt"] = (hunt / max(len(recs), 1), tot("hunt_ready"), tot("hunt_rotated"))
    m["target_leader"] = wilson(tot("target_leader"), att)
    idle = {}                                                                 # M6
    for r in recs:
        for q in (0, 1):
            x = idle.setdefault(r["decks"][q], [0, 0])
            x[0] += r["stats"]["unit_idle"][q]
            x[1] += r["stats"]["unit_turns"][q]
    m["unit_idle"] = wilson(sum(x[0] for x in idle.values()), sum(x[1] for x in idle.values()))
    m["unit_idle_deck"] = {d: wilson(*x) for d, x in idle.items()}
    m["opp_repeat"] = wilson(tot("opp_repeat"), max(tot("opposed"), 1))     # M7
    m["double_gems"] = tot("double_gems")                                     # M8
    m["opp_rate"] = tot("opposed") / max(tot("opp_elig"), 1)                  # M9
    m["opp_rate_impeto"] = tot("opp_impeto") / max(tot("opp_elig_impeto"), 1)
    m["opp_impeto"] = tot("opp_impeto")
    minor = {}                                                                # M10, per Leader
    for r in recs:
        if r["winner"] is None:
            continue
        name = r["decks"][r["winner"]]
        col, k, n_col = minor_colour(name)
        x = minor.setdefault(deck_list(name)[0], [0, 0, 0, col])
        x[0] += k; x[1] += n_col; x[2] += 1
    m["minor"] = {lid: (x[3], x[0] / max(x[2], 1), x[0] / max(x[1], 1), x[2]) for lid, x in minor.items()}
    acts, seats = {}, {}                                                      # M11: per partita giocata dal mazzo
    for r in recs:
        for q in (0, 1):
            lid, cards = deck_list(r["decks"][q])
            for cid in list(cards) + [lid]:
                seats[cid] = seats.get(cid, 0) + 1
            for cid, k in r["stats"]["activations"][q].items():
                acts[cid] = acts.get(cid, 0) + k
    per_game = {cid: k / max(seats.get(cid, 1), 1) for cid, k in acts.items()}
    m["activations"] = dict(sorted(per_game.items(), key=lambda t: -t[1]))
    m["removals"] = per_deck("removals")                                      # M12
    m["life_costs"] = per_deck("life_costs")                                  # M14 (costi pagati)
    wins = [r for r in recs if r["winner"] is not None]                       # M15
    pres = {}
    for r in wins:
        _, cards = deck_list(r["decks"][r["winner"]])
        for tag in {t for cid in cards for t in [cid] + slots_of(cid)}:
            pres[tag] = pres.get(tag, 0) + 1
    m["slot_presence"] = {t: k / max(len(wins), 1) for t, k in sorted(pres.items(), key=lambda t: -t[1])}
    m["slot_alarm"] = sorted(cid for cid in pres if cid in CARDS and ("caccia" in slots_of(cid) or "11.1" in slots_of(cid))
                             and m["slot_presence"][cid] > 0.60)
    by_agent = {}                                                             # M14: vittorie per IA (partite miste)
    for r in recs:
        if r["agents"][0] != r["agents"][1]:
            for q in (0, 1):
                x = by_agent.setdefault(r["agents"][q], [0, 0])
                x[0] += r["winner"] == q; x[1] += 1
    m["agent_win"] = {k: wilson(*x) for k, x in by_agent.items()}
    return m


def _per_deck(recs, key):
    """{deck: per-game average of stats[key] for the side that played the deck}."""
    out = {}
    for r in recs:
        for q in (0, 1):
            x = out.setdefault(r["decks"][q], [0, 0])
            x[0] += r["stats"][key][q]; x[1] += 1
    return {d: k / max(n_, 1) for d, (k, n_) in sorted(out.items())}


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
         f"| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | {pct(m['leader_free'][0])} (n={m['leader_free'][1]}) / {pct(m['leader_free'][2])} (n={m['leader_free'][3]}) | | |",
         f"| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | {pct(m['leader_drain'])} | <35% (Cr) | |",
         f"| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | {pct(m['r13_both_awak'][0])} (n={m['r13_both_awak'][1]}) | | |",
         f"| Attacchi per partita | {m['attacks_per_game']:.1f} | | |",
         f"| Pugno attaccante vuoto / pieno | {pct(m['pugno_att_empty'])} / {pct(m['pugno_att_full'])} (gemme medie {m['pugno_att_gems']:.2f}) | non >90% | |",
         f"| Pugno difensore vuoto / pieno | {pct(m['pugno_def_empty'])} / {pct(m['pugno_def_full'])} (gemme medie {m['pugno_def_gems']:.2f}) | non >90% | |",
         f"| Reazioni per scontro | {m['reactions_per_combat']:.2f} | | |",
         f"| Modificatori per scontro (max; distribuzione) | {m['mods_max']}; {m['mods_dist']} | | |",
         f"| Azioni legali per decisione | {m['legal_per_decision']:.1f} | <60 | {check(m['legal_per_decision'] < 60)} |",
         f"| Fine partita | {m['end_reasons']} | | |",
         f"| Nelle fasce comuni | {'sì' if in_bands(m) else 'no'} | | |", "",
         "Vittorie per mazzo: " + ", ".join(f"{D.label(d)} {pct(w)}" for d, w in sorted(m["deck_win"].items())), ""]
    L += render_r005(m)
    return "\n".join(L) + "\n"


def render_r005(m):
    fmt = lambda d, f="{:.2f}": ", ".join(f"{D.label(k)} " + f.format(v) for k, v in d.items()) or "—"
    top = list(m["activations"].items())[:12]
    pres = [(t, v) for t, v in m["slot_presence"].items() if t not in CARDS or "caccia" in slots_of(t) or slots_of(t)]
    return [
        "## Metriche diagnostiche R-005 (M1–M15)", "",
        "| # | Metrica | Valore | Obiettivo |", "|---|---|---|---|",
        f"| M1 | Reazioni disponibili / giocate per scontro | {m['react_avail']:.3f} / {m['reactions_per_combat']:.3f} | giocate ≥0.10 |",
        f"| M2 | Reazioni decisive per scontro | {m['react_decisive']:.3f} | ≥0.05 |",
        f"| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | "
        + ", ".join(f"{D.label(d)} {v:.2f} ({m['react_scar_life'][d]:.2f})" for d, v in m["react_scar"].items()) + " | |",
        f"| M4 | Scontri decisi prima dell'impegno | {pct(m['decided_pre'])} | |",
        f"| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | {m['hunt'][0]:.2f} ({m['hunt'][1]} / {m['hunt'][2]}); {pct(m['target_leader'])} | |",
        f"| M6 | Unità ferme (né attaccano né si oppongono) | {pct(m['unit_idle'])}; " + fmt({d: v[0] for d, v in m['unit_idle_deck'].items()}, "{:.1%}") + " | ≤38%, verdi ≤35% |",
        f"| M7 | Opposizioni ripetute della stessa Unità nel turno | {pct(m['opp_repeat'])} | ≤3% |",
        f"| M8 | Gemme contate sia per la Reazione sia per Impeto | {m['double_gems']} | 0 |",
        f"| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | {m['opp_rate_impeto']:.3f} ({m['opp_impeto']}) / {m['opp_rate']:.3f} | |",
        f"| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | "
        + ", ".join(f"{l} {c}: {k:.1f} ({100*q:.0f}%, {n} vittorie)" for l, (c, k, q, n) in sorted(m["minor"].items())) + " | ≥35% |",
        f"| M11 | Attivazioni per partita (prime 12) | " + fmt(dict(top)) + " | |",
        f"| M12 | Rimozioni per partita (effetti e Caccia) | " + fmt(m["removals"]) + " | |",
        f"| M13 | Pugno d'attacco pieno | {pct(m['pugno_att_full'])} | |",
        f"| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | " + fmt(m["life_costs"])
        + "; " + (", ".join(f"{k} {pct(v)}" for k, v in m["agent_win"].items()) or "nessuna partita mista (comando `vita`)") + " | |",
        f"| M15 | Presenza nei mazzi vincenti (slot e Caccia) | " + (fmt(dict(pres[:12]), "{:.0%}") if pres else "nessuno slot nei file")
        + f"; oltre il 60%: {', '.join(m['slot_alarm']) or 'nessuno'} | nessuno slot di Caccia o 11.1 >60% |", ""]


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
        save(f"{name}_{os.path.splitext(os.path.basename(spec))[0]}", render(f"Braccio {name}: {spec}", m, spec, a.ia, el), recs, out)
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
    res, recs = head_to_head(a.variante, a.forte, a.ia, a.partite, a.mazzi)
    text = (f"# IA forte contro semplice ({a.variante})\n\n`{a.forte}` contro `{a.ia}`, mirror, {len(recs)} partite.\n\n"
            f"- Vittorie dell'IA forte: {pct(res)}; margine {100*(res[0]-0.5):+.1f} punti "
            f"[{100*(res[1]-0.5):+.1f}, {100*(res[2]-0.5):+.1f}]\n")
    print(text)
    print("report:", save(f"forte_{os.path.splitext(os.path.basename(a.variante))[0]}", text, recs, a.out))


def cmd_vita(a):
    """M14: an AI that always pays its costs in Vita against the plain AI, mirror."""
    res, recs = head_to_head(a.variante, "vita", a.ia, a.partite, a.mazzi)
    m = metrics(recs)
    text = (f"# M14: IA che paga sempre i costi in Vita ({a.variante})\n\n`vita` contro `{a.ia}`, mirror, {len(recs)} partite.\n\n"
            f"- Vittorie dell'IA `vita`: {pct(res)}\n- Costi in Vita pagati per partita: "
            + ", ".join(f"{d} {v:.2f}" for d, v in m["life_costs"].items()) + "\n")
    print(text)
    print("report:", save(f"vita_{os.path.splitext(os.path.basename(a.variante))[0]}", text, recs, a.out))


def cmd_valida(a):
    """Strict check of a card file and, optionally, of decks against it. Exit code 1 on errors."""
    import sys
    with open(a.file, encoding="utf-8") as f:
        raw = json.load(f)
    errors = validate(raw)
    colors = {c["id"]: tuple(c.get("colors") or ()) for c in raw.get("cards", [])}
    lcolors = {l["id"]: tuple(l.get("colors") or ()) for l in raw.get("leaders", [])}
    for ref in D.expand(a.mazzi or []):
        try:
            leader, cards = D.raw_deck(ref)
            errors += [f"mazzo {ref}: {p}" for p in D.problems(leader, cards, colors, lcolors)]
        except (ValueError, KeyError) as e:
            errors.append(f"mazzo {ref}: {e}")
    print("\n".join(errors) if errors else "nessun errore")
    print(f"{a.file}: {len(raw.get('cards', []))} carte, {len(raw.get('leaders', []))} Leader, {len(errors)} errori")
    sys.exit(1 if errors else 0)


def cmd_partita(a):
    r = play_game(((a.mazzo1, a.mazzo2), (a.ia, a.ia), a.variante, a.seed, True))
    print("\n".join(r["log"]))
    print(f"\nVincitore: P{(r['winner'] or 0) + 1} ({r['end_reason']}), round {r['rounds']}")


def main(argv=None):
    p = argparse.ArgumentParser(prog="python -m sim.v02.run")
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(x, partite=100):
        x.add_argument("--variante", default="V02")
        x.add_argument("--ia", default="semplice")
        x.add_argument("--partite", type=int, default=partite)
        x.add_argument("--mazzi", nargs="*", help="nomi in sim/decks, file .json o file.json#nome")
        x.add_argument("--carte", help="file di carte v0.2 (default sim/v02/cards_v02.json)")
        x.add_argument("--incroci", type=int, default=0)
        x.add_argument("--seed", type=int, default=1)
        x.add_argument("--out")
    t = sub.add_parser("torneo"); common(t)
    ab = sub.add_parser("ab"); common(ab); ab.add_argument("--base", default="V02")
    lm = sub.add_parser("lambda"); common(lm, 200)
    co = sub.add_parser("collaudo"); common(co, 250)
    fo = sub.add_parser("forte"); common(fo, 25); fo.add_argument("--forte", default="forte:60")
    vi = sub.add_parser("vita"); common(vi, 100)
    pa = sub.add_parser("partita"); common(pa); pa.add_argument("mazzo1"); pa.add_argument("mazzo2")
    va = sub.add_parser("valida"); va.add_argument("file"); va.add_argument("--mazzi", nargs="*")
    a = p.parse_args(argv)
    if a.cmd == "valida":
        return cmd_valida(a)
    CARTE[0] = os.path.abspath(a.carte) if a.carte else None
    try:
        use_cards(CARTE[0])
        if a.mazzi:
            a.mazzi = D.expand(a.mazzi)
        for ref in a.mazzi or [] if a.cmd != "partita" else (a.mazzo1, a.mazzo2):
            D.load(ref)
    except ValueError as e:                             # carte o mazzi non validi: messaggio, niente traceback
        raise SystemExit(f"errore: {e}")
    {"torneo": cmd_torneo, "ab": cmd_ab, "lambda": cmd_lambda, "collaudo": cmd_collaudo,
     "forte": cmd_forte, "vita": cmd_vita, "partita": cmd_partita, "valida": cmd_valida}[a.cmd](a)


if __name__ == "__main__":
    main()
