"""Paired A/B experiment between a base rule set and one or more variants.

  python -m sim.esperimento --base default --variante V1b=V1b_per_attack \
         --partite 200 --ia semplice --seed 1 --out ../tcg/swarm/esperimenti/E-004

Base and every variant play exactly the same games (same matchups, seats and seeds),
so differences come from the rules, not from luck. A variant is a preset name from
sim/config.py or a JSON file (see sim/varianti/esempio_parata_fissa.json).
Output: one standard report per configuration plus `confronto.md` with the
difference on every metric (95% CI) and a verdict against each target."""
import argparse
import json
import math
import os
import random
import statistics
import time

from .config import rules_from
from .run import all_decks, deck_winrates, match_jobs, metrics, render, run_jobs, save, cards_version, wilson

# metric key, label, target (lo, hi) as fractions or turns
TARGETS = [
    ("rounds_median", "Durata mediana (turni)", (8, 10)),
    ("rounds_in_5_15", "Partite tra 5 e 15 turni", (0.90, 1.0)),
    ("rounds_ge13", "Partite al turno 13", (0.0, 0.10)),
    ("clessidra_active", "Clessidra attiva a fine partita", (0.0, 0.15)),
    ("rounds_over_15", "Partite oltre il turno 15", (0.0, 0.02)),
    ("g1_win", "Vittorie del primo giocatore", (0.48, 0.52)),
    ("comeback", "Rimonte", (0.20, 0.35)),
    ("stopped_by_reaction", "Attacchi al Leader fermati da reazione", (0.30, 0.45)),
    ("closed_by_stall", "Partite chiuse dal Crepuscolo", (0.0, 0.15)),
    ("rim_rate", "Rimarginare usato quando possibile", (0.0, 0.70)),
]


def verdict(t, target):
    v, lo, hi = t
    if any(x != x for x in (v, lo, hi)):
        return "n/d"
    a, b = target
    if a <= lo and hi <= b:
        return "dentro"
    if hi < a or lo > b:
        return "fuori"
    return "incerto"


def fmt(key, t):
    v, lo, hi = t
    if key == "rounds_median":
        return f"{v:.1f} [{lo:.1f}–{hi:.1f}]"
    return f"{100*v:.1f}% [{100*lo:.1f}–{100*hi:.1f}]"


def diff(key, base_m, var_m, base_recs, var_recs):
    """Difference variant - base with a 95% CI (normal approximation for proportions,
    paired bootstrap for the median length)."""
    if key == "rounds_median":
        rng = random.Random(0)
        pairs = list(zip([r["rounds"] for r in base_recs], [r["rounds"] for r in var_recs]))
        boots = []
        for _ in range(400):
            sample = rng.choices(pairs, k=len(pairs))
            boots.append(statistics.median(p[1] for p in sample) - statistics.median(p[0] for p in sample))
        boots.sort()
        d = var_m[key][0] - base_m[key][0]
        return f"{d:+.1f} [{boots[10]:+.1f}, {boots[389]:+.1f}]"
    p1, p2 = base_m[key][0], var_m[key][0]
    n1, n2 = _n(key, base_m), _n(key, var_m)
    if not n1 or not n2 or p1 != p1 or p2 != p2:
        return "n/d"
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    d = p2 - p1
    return f"{100*d:+.1f} [{100*(d-1.96*se):+.1f}, {100*(d+1.96*se):+.1f}] punti"


def _n(key, m):
    if key == "comeback":
        return m["comeback_n"]
    if key == "stopped_by_reaction":
        return m["threats"]
    if key == "rim_rate":
        return m.get("rim_n") or m["n"]
    return m["n"]


def main(argv=None):
    p = argparse.ArgumentParser(prog="python -m sim.esperimento")
    p.add_argument("--base", default="default")
    p.add_argument("--variante", action="append", default=[], help="NOME=preset_o_file.json (ripetibile)")
    p.add_argument("--mazzi", nargs="*", help="mazzi (default: tutti i mazzi di riferimento)")
    p.add_argument("--partite", type=int, default=200, help="partite per abbinamento")
    p.add_argument("--ia", default="semplice")
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--out", default=None)
    p.add_argument("--workers", type=int)
    a = p.parse_args(argv)

    decks = a.mazzi or all_decks()
    configs = [("base", a.base)] + [tuple(v.split("=", 1)) if "=" in v else (v, v) for v in a.variante]
    jobs_template = []
    k = 0
    for i, x in enumerate(decks):
        for y in decks[i:]:
            jobs_template.append((x, y, a.seed * 1_000_000 + 10_000 * k))
            k += 1
    results = {}
    t0 = time.time()
    for name, spec in configs:
        rules = rules_from(spec)
        jobs = []
        for x, y, s0 in jobs_template:
            jobs += match_jobs(x, y, a.ia, a.ia, rules, a.partite, seed0=s0)
        t = time.time()
        recs = run_jobs(jobs, a.workers)
        text, m = render(f"{name} ({spec})", recs, rules, agents=a.ia, elapsed=time.time() - t)
        save(name, text, recs, {"name": name, "spec": spec, "ia": a.ia, "seed": a.seed}, out_dir=a.out)
        dw = deck_winrates(recs)
        m["deck_spread"] = (max(x[0] for x in dw.values()) - min(x[0] for x in dw.values())) if dw else float("nan")
        m["rim_n"] = sum(sum(r["stats"]["rim_possible"]) for r in recs)
        results[name] = (rules, recs, m)

    base_rules, base_recs, base_m = results["base"]
    lines = ["# Esperimento A/B appaiato", "",
             f"- Base: `{a.base}`; varianti: " + ", ".join(f"`{n}` = `{s}`" for n, s in configs[1:]),
             f"- IA: {a.ia}; mazzi: {', '.join(decks)}; {a.partite} partite per abbinamento, posti alternati",
             f"- Partite per configurazione: {len(base_recs)}; seed base {a.seed}; versione carte `{cards_version()}`",
             "- Stesse partite (abbinamenti, posti, seed) per base e varianti. Tra parentesi: IC 95%.",
             "- Verdetto rispetto all'obiettivo: **dentro** (tutto l'IC nell'obiettivo), **fuori** (tutto l'IC fuori), **incerto**.",
             ""]
    for name, _ in configs[1:]:
        _, recs, m = results[name]
        lines += [f"## {name} contro base", "",
                  "| Metrica | Obiettivo | Base | Variante | Differenza | Verdetto base | Verdetto variante |",
                  "|---|---|---|---|---|---|---|"]
        for key, label, target in TARGETS:
            tgt = f"{target[0]}–{target[1]}" if key == "rounds_median" else f"{100*target[0]:.0f}–{100*target[1]:.0f}%"
            lines.append(f"| {label} | {tgt} | {fmt(key, base_m[key])} | {fmt(key, m[key])} | "
                         f"{diff(key, base_m, m, base_recs, recs)} | {verdict(base_m[key], target)} | {verdict(m[key], target)} |")
        lines.append(f"| Scarto di vittorie tra mazzi | piccolo | {100*base_m['deck_spread']:.0f} punti | "
                     f"{100*m['deck_spread']:.0f} punti | | | |")
        lines.append(f"| Vite perse da attacchi del Leader | <40% | {100*base_m['leader_attack_share']:.0f}% | "
                     f"{100*m['leader_attack_share']:.0f}% | | | |")
        lines.append("")
    lines.append(f"Tempo totale: {time.time()-t0:.0f}s.")
    text = "\n".join(lines) + "\n"
    out = a.out or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "confronto.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print("confronto:", path)


if __name__ == "__main__":
    main()
