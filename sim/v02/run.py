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
            "stats": s.stats, "log": s.log, "crep": dict(s.crep),
            "spareggio_word": s.r.crepuscolo_spareggio}


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
    fr = {}
    for r in recs:
        for q in (0, 1):
            for k, v in r["stats"].get("leader_free_rim", [{}, {}])[q].items():
                fr[k] = fr.get(k, 0) + v
    m["leader_free_rim"] = {k[:-4]: (wilson(fr.get(k[:-4] + "|rim", 0), v), v) for k, v in sorted(fr.items()) if k.endswith("|tot")}
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
    cr = [r for r in recs if r["end_reason"] == "crepuscolo"]
    m["g1_win_crep"] = wilson(sum(r["winner"] == 0 for r in cr), len(cr))     # R-011 #2
    r15 = [r for r in recs if r["rounds"] >= 15]
    m["g1_win_r15"] = wilson(sum(r["winner"] == 0 for r in r15), len(r15))    # Q-019
    c15 = [r for r in recs if r.get("crep", {}).get("r15_lives")]
    par = [r for r in c15 if r["crep"]["pareggio"]]
    m["crep_pareggi"] = wilson(len(par), len(c15))
    m["crep_pari"] = wilson(sum(r["crep"]["r15_lives"][0] == r["crep"]["r15_lives"][1] for r in par), len(par))
    m["crep_vivi_r16"] = wilson(sum(bool(r["crep"].get("vivo_r16")) for r in c15), len(c15))
    m["crep_g1_pareggi"] = wilson(sum(r["winner"] == 0 for r in par), len(par))
    lp = {}
    for r in c15:
        k = "%d-%d" % tuple(r["crep"]["r15_lives"])
        lp[k] = lp.get(k, 0) + 1
    m["crep_vite"] = dict(sorted(lp.items(), key=lambda x: -x[1])[:8])
    sp = [r for r in recs if r.get("crep", {}).get("spareggio")]          # Q-019 esito §6: spareggi a ogni controllo
    m["sp_n"], m["sp_rate"] = len(sp), wilson(len(sp), len(c15))
    m["sp_pari"] = wilson(sum(r["crep"]["spareggio"]["vite"][0] == r["crep"]["spareggio"]["vite"][1] for r in sp), len(sp))
    m["sp_round"] = {}
    for r in sp:
        k = r["crep"]["spareggio"]["round"]; m["sp_round"][k] = m["sp_round"].get(k, 0) + 1
    m["sp_g2"] = wilson(sum(r["winner"] == 1 for r in sp), len(sp))
    def no_hit(r, rounds):
        return not any(rd in rounds and q == r["winner"] for rd, q in r["crep"].get("hits", []))
    m["sp_stallo"] = wilson(sum(no_hit(r, {r["crep"]["spareggio"]["round"] - 1}) for r in sp), len(sp))
    m["sp_noatk"] = wilson(sum(not any(rd == r["crep"]["spareggio"]["round"] - 1 and q == r["winner"]
                                       for rd, q in r["crep"].get("atk", [])) for r in sp), len(sp))
    gw = [r["crep"].get("guard", {}).get(f"{r['crep']['spareggio']['round'] - 1}-{r['winner']}") for r in sp]
    gw = [g for g in gw if g is not None]
    m["sp_guard"] = (sum(gw) / len(gw)) if gw else float("nan")
    # Q-022: righe di stallo proposte nel round 1 (blu, architetto, critico, verde, ponti, analista, rosso, nero)
    def atk_in(r, q):
        return any(rd == r["crep"]["spareggio"]["round"] - 1 and qq == q for rd, qq in r["crep"].get("atk", []))
    loser = lambda r: r["crep"]["spareggio"]["perde"]
    pari = [r for r in sp if r["crep"]["spareggio"]["vite"][0] == r["crep"]["spareggio"]["vite"][1]]
    dis = [r for r in sp if r not in pari]
    m["sp_noatk_both"] = wilson(sum(not atk_in(r, 0) and not atk_in(r, 1) for r in sp), len(sp))
    m["sp_loser_atk"] = wilson(sum(atk_in(r, loser(r)) for r in sp), len(sp))
    m["sp_noatk_pari"] = wilson(sum(not atk_in(r, r["winner"]) for r in pari), len(pari))
    m["sp_noatk_dis"] = wilson(sum(not atk_in(r, r["winner"]) for r in dis), len(dis))
    m["sp_noatk_both_pari"] = wilson(sum(not atk_in(r, 0) and not atk_in(r, 1) for r in pari), len(pari))
    def ultima(r):                                       # spareggio chiuso dall'ultima clausola (il posto)
        c = r["crep"]["spareggio"]; pr = c.get("pronto"); gu = c.get("guardia")
        if c["vite"][0] != c["vite"][1]:
            return False
        if spec_sp in ("vite_leader", "vite_ruotato") and pr is not None:
            return pr[0] == pr[1]
        if spec_sp == "vite_guardia" and gu is not None:
            return gu[0] == gu[1]
        return True
    spec_sp = recs[0].get("spareggio_word") if recs else None
    m["posto_tutte"] = wilson(sum(ultima(r) for r in sp), n)
    m["posto_r15"] = wilson(sum(ultima(r) for r in sp), len(c15))
    m["sp_g2_pari"] = wilson(sum(r["winner"] == 1 for r in pari), len(pari))
    rot = {}
    for r in pari:
        for side, q in (("vinc", r["winner"]), ("perd", loser(r))):
            hs = r["crep"].get("lrot", {}).get(f"{r['crep']['spareggio']['round'] - 1}-{q}", [])
            k = side + ":" + (hs[0] if hs else "pronto")
            rot[k] = rot.get(k, 0) + 1
    m["sp_rot_pari"] = dict(sorted(rot.items()))
    tp = {0: [0, 0], 1: [0, 0]}                         # Q-022 riga del critico: turni iniziati con entrambi Alle Corde a Vite pari
    for r in recs:
        atk = set(r.get("crep", {}).get("atk", []))
        for rd, q in r.get("crep", {}).get("pari_inizio", []):
            tp[q][0] += 1; tp[q][1] += (rd, q) not in atk
    m["pari_noatk_g1"] = wilson(tp[0][1], tp[0][0]); m["pari_noatk_g2"] = wilson(tp[1][1], tp[1][0])
    m["pari_turni"] = (tp[0][0], tp[1][0])
    nb = [0, 0]                                          # Q-022 (blu, critico): nessuno dei due attacca nel round, popolazione fissata all'inizio del turno di G1
    for r in recs:
        atk = set(r.get("crep", {}).get("atk", []))
        for rd, q in r.get("crep", {}).get("pari_inizio", []):
            if q == 0:
                nb[0] += 1; nb[1] += (rd, 0) not in atk and (rd, 1) not in atk
    m["pari_noatk_both"] = wilson(nb[1], nb[0])
    pre = [r for r in mir if r["rounds"] < 15]
    m["g1_win_pre15"] = wilson(sum(r["winner"] == 0 for r in pre), len(pre))
    fin = [r for r in c15 if r["winner"] is not None and r["rounds"] >= 15]
    m["stallo_r15"] = wilson(sum(no_hit(r, {14, 15}) for r in fin), len(fin))
    m["stallo_r15_g2"] = wilson(sum(no_hit(r, {14, 15}) and r["winner"] == 1 for r in fin), len(fin))
    spd = {}
    for r in sp:
        d = D.label(r["decks"][r["winner"]]); spd[d] = spd.get(d, 0) + 1
    m["sp_deck"] = dict(sorted(spd.items(), key=lambda x: -x[1]))
    pair = {}
    for r in c15:
        k = " vs ".join(sorted(D.label(d) for d in r["decks"]))
        x = pair.setdefault(k, [0, 0]); x[0] += r["winner"] == 0; x[1] += 1
    m["g1_r15_pair"] = {k: (wilson(*v), v[1]) for k, v in sorted(pair.items())}
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
    m["stanca_removed"] = per_deck("stanca_removed")                          # R-009 #5
    tb = per_deck("turns_both022")
    ab = per_deck("atk_leader_both022")
    m["both022"] = {d: ab[d] / tb[d] for d in tb if tb[d] > 0}               # R-009 #6
    cb = {}                                                                   # R-009 #8: rimonte per mazzo
    for r in recs:
        lr = r["stats"]["life_at_round6"]
        if lr and abs(lr[0] - lr[1]) >= 2:
            q = 0 if lr[0] < lr[1] else 1
            x = cb.setdefault(r["decks"][q], [0, 0])
            x[0] += r["winner"] == q; x[1] += 1
    m["comeback_deck"] = {d: (k / n_, n_) for d, (k, n_) in sorted(cb.items())}
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
         f"| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | "
         + (", ".join(f"{k.replace('|', ' ')} {pct(v)} (n={n})" for k, (v, n) in m["leader_free_rim"].items()) or "—") + " | | |",
         f"| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | {pct(m['r13_both_awak'][0])} (n={m['r13_both_awak'][1]}) | | |",
         f"| Attacchi per partita | {m['attacks_per_game']:.1f} | | |",
         f"| Pugno attaccante vuoto / pieno | {pct(m['pugno_att_empty'])} / {pct(m['pugno_att_full'])} (gemme medie {m['pugno_att_gems']:.2f}) | non >90% | |",
         f"| Pugno difensore vuoto / pieno | {pct(m['pugno_def_empty'])} / {pct(m['pugno_def_full'])} (gemme medie {m['pugno_def_gems']:.2f}) | non >90% | |",
         f"| Reazioni per scontro | {m['reactions_per_combat']:.2f} | | |",
         f"| Modificatori per scontro (max; distribuzione) | {m['mods_max']}; {m['mods_dist']} | | |",
         f"| Azioni legali per decisione | {m['legal_per_decision']:.1f} | <60 | {check(m['legal_per_decision'] < 60)} |",
         f"| Fine partita | {m['end_reasons']} | | |",
         f"| G1 vince fra le partite finite al Crepuscolo | {pct(m['g1_win_crep'])} | | |",
         f"| G1 vince fra le partite arrivate al round 15 | {pct(m['g1_win_r15'])} | | |",
         f"| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | {pct(m['crep_pareggi'])} / {pct(m['crep_pari'])} | | |",
         f"| Q-019: G1 vince fra i pareggi; partite vive al round 16 | {pct(m['crep_g1_pareggi'])}; {pct(m['crep_vivi_r16'])} | | |",
         f"| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {m['crep_vite']} | | |",
         f"| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n={m['sp_n']}) | {pct(m['sp_rate'])} / {pct(m['sp_pari'])} | | |",
         f"| Q-019: spareggi per round; G2 vince lo spareggio | {m['sp_round']}; {pct(m['sp_g2'])} | | |",
         f"| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | {pct(m['sp_stallo'])} / {pct(m['sp_noatk'])}; {m['sp_guard']:.2f} | ≤50% (Cr) | |",
         f"| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | {pct(m['sp_noatk_both'])} / {pct(m['sp_loser_atk'])} | | |",
         f"| Q-022: il vincitore non attacca, spareggi a Vite pari (n={m['sp_pari'][0]*m['sp_n']:.0f}) / a Vite diverse; nessuno attacca a Vite pari | {pct(m['sp_noatk_pari'])} / {pct(m['sp_noatk_dis'])}; {pct(m['sp_noatk_both_pari'])} | | |",
         f"| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | {pct(m['posto_tutte'])} / {pct(m['posto_r15'])}; {pct(m['sp_g2_pari'])} | | |",
         f"| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {m['sp_rot_pari']} | | |",
         f"| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n={m['pari_turni'][0]}) / turno di G2 (n={m['pari_turni'][1]}) | {pct(m['pari_noatk_g1'])} / {pct(m['pari_noatk_g2'])} | ≤30% per chi perde la parità | |",
         f"| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n={m['pari_turni'][0]}) | {pct(m['pari_noatk_both'])} | ≤25–30% | |",
         f"| Q-022: G1 nei mirror fra le partite finite prima del R15 | {pct(m['g1_win_pre15'])} | | |",
         f"| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | {pct(m['stallo_r15'])} ({pct(m['stallo_r15_g2'])}) | | |",
         f"| Q-019: vincitori degli spareggi per mazzo | {m['sp_deck']} | | |",
         f"| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | " + ", ".join(f"{k} {100*w[0]:.0f}% (n={n})" for k, (w, n) in m["g1_r15_pair"].items()) + " | | |",
         f"| Nelle fasce comuni | {'sì' if in_bands(m) else 'no'} | | |", "",
         "Vittorie per mazzo: " + ", ".join(f"{D.label(d)} {pct(w)}" for d, w in sorted(m["deck_win"].items())), ""]
    L += render_r005(m)
    return "\n".join(L) + "\n"


def render_r012(recs, traccia=()):
    """R-012: matrice degli incroci, contatori per mazzo e uso delle carte tracciate."""
    decks = sorted({d for r in recs for d in r["decks"]})
    if not recs or "leader_attacks" not in recs[0]["stats"]:
        return []
    L = ["## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)", "",
         "| | " + " | ".join(D.label(d) for d in decks) + " |", "|---|" + "---|" * len(decks)]
    for x in decks:
        row = []
        for y in decks:
            g = [r for r in recs if set(r["decks"]) == {x, y} and x != y]
            if not g:
                row.append("—")
                continue
            w = wilson(sum(r["winner"] is not None and r["decks"][r["winner"]] == x for r in g), len(g))
            row.append(f"{100*w[0]:.1f} [{100*w[1]:.0f}–{100*w[2]:.0f}] ({len(g)})")
        L.append(f"| {D.label(x)} | " + " | ".join(row) + " |")
    per = {d: {"n": 0} for d in decks}
    for r in recs:
        st = r["stats"]
        for q in (0, 1):
            x = per[r["decks"][q]]
            x["n"] += 1
            for k in ("leader_attacks", "leader_on_attack", "furia_bonus_combats", "scudo_atk2", "solo_unit_turns", "caccia_leader_atk", "fa_alta_wins"):
                x[k] = x.get(k, 0) + st[k][q]
            x["act_then_hit"] = x.get("act_then_hit", 0) + sum(st["act_then_hit"][q].values())
            x["lead_act"] = x.get("lead_act", 0) + sum(v for c, v in st["activations"][q].items() if c in LEADERS or c.startswith("LDR"))
            fh = st["first_hit_round"][q]
            if fh is not None:
                x.setdefault("fh", []).append(fh)
            x["peak2"] = max(x.get("peak2", 0), st["peak2"][q])
            for cid, v in st["cards_played"][q].items():
                for c in CARDS[cid].colors if cid in CARDS else ():
                    col = x.setdefault("col", {})
                    col[c] = col.get(c, 0) + v
            for key, lab in (("cards_played", "g"), ("activations", "a"), ("hits_by", "h"), ("kills_by", "k"), ("fa_alta_by", "f")):
                for cid, v in st[key][q].items():
                    if cid in traccia:
                        t = x.setdefault("tr", {}).setdefault(cid, {})
                        t[lab] = t.get(lab, 0) + v
    L += ["", "## R-012: contatori per mazzo (per partita)", "",
          "| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for d in decks:
        x = per[d]; n = max(x["n"], 1)
        fh = x.get("fh", [])
        col = x.get("col", {}); ct = max(sum(col.values()), 1)
        L.append(f"| {D.label(d)} | {x.get('leader_attacks', 0)/n:.2f} | {x.get('leader_on_attack', 0)/n:.2f} | "
                 f"{x.get('lead_act', 0)/n:.2f} / {x.get('act_then_hit', 0)/n:.2f} | {x.get('furia_bonus_combats', 0)/n:.2f} | "
                 f"{x.get('scudo_atk2', 0)/n:.2f} | {(sum(fh)/len(fh)) if fh else float('nan'):.1f} ({len(fh)}) | {x.get('peak2', 0)} | "
                 + ", ".join(f"{c} {100*v/ct:.0f}%" for c, v in sorted(col.items()))
                 + f" | {x.get('solo_unit_turns', 0)/n:.2f} | {x.get('caccia_leader_atk', 0)/n:.2f} |")
    if traccia:
        L += ["", "## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)", "",
              "| Mazzo | " + " | ".join(traccia) + " |", "|---|" + "---|" * len(traccia)]
        for d in decks:
            x = per[d]; n = max(x["n"], 1); tr = x.get("tr", {})
            L.append(f"| {D.label(d)} | " + " | ".join(
                "/".join(f"{tr.get(c, {}).get(k, 0)/n:.2f}" for k in "gahk") for c in traccia) + " |")
    if recs and "fa_alta_wins" in recs[0]["stats"]:
        L += ["", f"## R-017: scontri vinti con Forza d'attacco ≥ {engine.FA_ALTA} (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)", "",
              "| Mazzo | Totale | " + " | ".join(traccia) + " |", "|---|---|" + "---|" * len(traccia)]
        for d in decks:
            x = per[d]; n = max(x["n"], 1); tr = x.get("tr", {})
            L.append(f"| {D.label(d)} | {x.get('fa_alta_wins', 0)/n:.2f} | " + " | ".join(f"{tr.get(c, {}).get('f', 0)/n:.2f}" for c in traccia) + " |")
    return L + [""]


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
        f"| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | " + fmt(m["stanca_removed"]) + " | allarme >1 con LDR-04/LDR-06 |",
        f"| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | " + (fmt(m["both022"]) if m["both022"] else "mai insieme") + " | |",
        f"| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | " + ", ".join(f"{D.label(d)} {100*v:.0f}% (n={n})" for d, (v, n) in m["comeback_deck"].items()) + " | 20–35% |",
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
    text += "\n".join(render_r012(recs, tuple(t for t in (a.traccia or "").split(",") if t))) + "\n"
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
        x.add_argument("--variante", default="V026")
        x.add_argument("--ia", default="semplice")
        x.add_argument("--partite", type=int, default=partite)
        x.add_argument("--mazzi", nargs="*", help="nomi in sim/decks, file .json o file.json#nome")
        x.add_argument("--carte", help="file di carte v0.2 (default sim/v02/cards_v02.json)")
        x.add_argument("--incroci", type=int, default=0)
        x.add_argument("--seed", type=int, default=1)
        x.add_argument("--out")
    t = sub.add_parser("torneo"); common(t)
    t.add_argument("--traccia", help="R-012: ID di carte e Leader da tracciare, separati da virgola")
    ab = sub.add_parser("ab"); common(ab); ab.add_argument("--base", default="V026")
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
