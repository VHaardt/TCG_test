"""Aggregates the per-crossing reports of E-020 (R-012) into one esito.md per arm and AI."""
import glob, math, os, re, sys

ROOT = os.environ.get("E020_ROOT", "/mnt/project-files/tcg/swarm/esperimenti/E-020")
COMMIT = sys.argv[1] if len(sys.argv) > 1 else "feabc5c"
LAB = lambda d: re.sub(r"rif_LDR0(\d)_\w+", r"L\1", d).replace("mix_M3_thorn_lucchetto", "M3")
ORDER = ["L1", "L2", "L3", "L4", "L5", "L6", "M3"]


def wilson(k, n, z=1.96):
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return p, c - h, c + h


def fmt(w):
    return "—" if w[0] != w[0] else f"{100*w[0]:.1f} [{100*w[1]:.1f}–{100*w[2]:.1f}]"


def cell(path):
    t = open(path, encoding="utf-8").read()
    c = {"n": int(re.search(r"partite: (\d+)", t).group(1))}
    c["wins"] = {LAB(d): float(p) / 100 for d, p in re.findall(r"(rif_LDR0\d_\w+|mix_M3_\w+) ([\d.]+)% \[", t.split("Vittorie per mazzo:")[1].split("\n")[0])}
    num = lambda lab: float(re.search(re.escape(lab) + r" \| ([\d.]+)%", t).group(1)) / 100
    c["r13"], c["o15"], c["early"] = num("Partite al round 13+"), num("Partite oltre il 15"), num("Vittorie prima del round 5")
    c["med"] = float(re.search(r"Durata mediana \(round\) \| ([\d.]+)", t).group(1))
    c["end"] = {k: int(v) for k, v in re.findall(r"'(\w+)': (\d+)", re.search(r"Fine partita \| (\{.*?\})", t).group(1))}
    c["m13"] = num("| M13 | Pugno d'attacco pieno")

    def per_deck(row, pat=r"(rif_LDR0\d_\w+|mix_M3_\w+) ([\d.]+)"):
        line = next((l for l in t.splitlines() if l.startswith(row)), "")
        return {LAB(d): float(v) for d, v in re.findall(pat, line)}
    c["r95"] = per_deck("| R9-5 |")
    c["r98"] = {LAB(d): (float(p) / 100, int(n)) for d, p, n in
                re.findall(r"(rif_LDR0\d_\w+|mix_M3_\w+) ([\d.]+)% \(n=(\d+)\)", next((l for l in t.splitlines() if l.startswith("| R9-8 |")), ""))}
    c["m6"] = per_deck("| M6 |", r"(rif_LDR0\d_\w+|mix_M3_\w+) ([\d.]+)%")
    c["m14"] = per_deck("| M14 |")
    c["cnt"], c["trk"], hdr = {}, {}, None
    sec = None
    for l in t.splitlines():
        if l.startswith("## R-012: contatori"):
            sec = "cnt"
        elif l.startswith("## R-012: carte tracciate"):
            sec = "trk"
        elif l.startswith("## "):
            sec = None
        elif sec and l.startswith("| Mazzo"):
            hdr = [h.strip() for h in l.strip("|").split("|")][1:]
        elif sec and l.startswith("| ") and not l.startswith("|---"):
            f = [x.strip() for x in l.strip("|").split("|")]
            c[sec][LAB(f[0])] = dict(zip(hdr, f[1:]))
    return c


def nums(s):
    return [float(x) for x in re.findall(r"[\d.]+", s)]


def arm(arm_dir, ia):
    cells = {}
    for p in sorted(glob.glob(f"{arm_dir}/{ia}/*/*_torneo_*.md")):
        cells[os.path.basename(os.path.dirname(p))] = cell(p)
    if not cells:
        return None
    return cells


def leader_totals(cells, keep=None):
    tot = {}
    for k, c in cells.items():
        if keep is not None and k not in keep:
            continue
        for d, w in c["wins"].items():
            x = tot.setdefault(d, [0, 0])
            x[0] += round(w * c["n"]); x[1] += c["n"]
    return tot


def render(name, ia, cells, base, ref="00_B0"):
    rif = {k: c for k, c in cells.items() if not k.startswith("M3")}
    mix = {k: c for k, c in cells.items() if k.startswith("M3")}
    ngames = sum(c["n"] for c in cells.values())
    L = [f"# E-020 / {name} — dati con IA {'semplice' if ia == 'S' else 'forte:30 (v2)'}", "",
         f"Motore commit {COMMIT} (branch `claude/regolamento-v0.1`), preset V02, un torneo per incrocio (`lancia_e020.sh`), "
         f"partite appaiate per seme con B0. Incroci: {len(rif)} rif" + (f" + {len(mix)} mix_M3" if mix else "")
         + f"; partite: {ngames} ({next(iter(cells.values()))['n']} per incrocio). Solo dati: le regole d'uscita sono nel piano e nel LEGGIMI.", ""]
    tot = leader_totals(rif)
    btot = leader_totals(base, keep=set(rif)) if base else None
    L += ["## Vittorie per Leader (incroci rif)", "", f"| Leader | Vittorie [IC 95%] | n | {ref} sugli stessi incroci | Δ |", "|---|---|---|---|---|"]
    for d in [o for o in ORDER if o in tot]:
        w = wilson(*tot[d])
        b = wilson(*btot[d]) if btot and d in btot else (float("nan"),) * 3
        L.append(f"| {d} | {fmt(w)} | {tot[d][1]} | {fmt(b)} | {100*(w[0]-b[0]):+.1f} |" if b[0] == b[0] else f"| {d} | {fmt(w)} | {tot[d][1]} | — | — |")
    decks = [o for o in ORDER[:6] if o in tot]
    L += ["", "## Matrice degli incroci (vittorie della riga contro la colonna)", "", "| | " + " | ".join(decks) + " |", "|---|" + "---|" * len(decks)]
    for x in decks:
        row = []
        for y in decks:
            k = f"{min(x, y)}-{max(x, y)}"
            c = rif.get(k)
            row.append("—" if x == y or c is None else f"{100*c['wins'][x]:.1f}")
        L.append(f"| {x} | " + " | ".join(row) + " |")
    if mix:
        L += ["", "## mix_M3_thorn_lucchetto contro i 5 rif", "", "| Avversario | Vittorie di M3 | R9-5 di M3 per partita | n |", "|---|---|---|---|"]
        for k, c in sorted(mix.items()):
            L.append(f"| {k.split('-')[1]} | {100*c['wins'].get('M3', float('nan')):.1f} | {c['r95'].get('M3', float('nan')):.2f} | {c['n']} |")
        km = sum(round(c["wins"]["M3"] * c["n"]) for c in mix.values()); nm = sum(c["n"] for c in mix.values())
        r95m = sum(c["r95"].get("M3", 0) * c["n"] for c in mix.values()) / nm
        L.append(f"| **totale** | {fmt(wilson(km, nm))} | {r95m:.2f} | {nm} |")
    n = sum(c["n"] for c in rif.values())
    wavg = lambda key: sum(c[key] * c["n"] for c in rif.values()) / n
    ends = {}
    for c in rif.values():
        for k, v in c["end"].items():
            ends[k] = ends.get(k, 0) + v
    L += ["", "## Durata e fine (incroci rif)", "",
          f"- Round 13+: {100*wavg('r13'):.1f}%; oltre il 15: {100*wavg('o15'):.1f}%; vittorie prima del round 5: {100*wavg('early'):.1f}%; "
          f"mediana per incrocio da {min(c['med'] for c in rif.values()):.0f} a {max(c['med'] for c in rif.values()):.0f}; fine partita {ends}.",
          "- Round 13+ negli incroci di ciascun Leader: " + ", ".join(
              f"{d} {100*sum(c['r13']*c['n'] for k, c in rif.items() if d in k.split('-'))/max(sum(c['n'] for k, c in rif.items() if d in k.split('-')), 1):.1f}%" for d in decks),
          f"- M13 pugno d'attacco pieno: {100*wavg('m13'):.1f}%."]
    per = {}
    for k, c in cells.items():
        for d in c["wins"]:
            x = per.setdefault(d, {"n": 0, "r95": 0, "m6": 0, "m14": 0, "rk": 0, "rn": 0, "cnt": {}, "trk": {}, "peak": 0, "fh": 0, "fhn": 0})
            x["n"] += c["n"]
            x["r95"] += c["r95"].get(d, 0) * c["n"]; x["m6"] += c["m6"].get(d, 0) * c["n"]; x["m14"] += c["m14"].get(d, 0) * c["n"]
            if d in c["r98"]:
                p, rn = c["r98"][d]; x["rk"] += p * rn; x["rn"] += rn
            row = c["cnt"].get(d)
            if row:
                for h, v in row.items():
                    if h.startswith("Round del primo"):
                        a = nums(v)
                        if len(a) == 2 and a[0] == a[0]:
                            x["fh"] += a[0] * a[1]; x["fhn"] += a[1]
                    elif h.startswith("Forza max"):
                        x["peak"] = max(x["peak"], nums(v)[0] if nums(v) else 0)
                    elif h.startswith("Carte giocate"):
                        for col, pc in re.findall(r"(\w) (\d+)%", v):
                            x["cnt"].setdefault("col_" + col, 0); x["cnt"]["col_" + col] += float(pc) * c["n"]
                    else:
                        for i, val in enumerate(nums(v)):
                            key = h + ("" if i == 0 else " (2)")
                            x["cnt"][key] = x["cnt"].get(key, 0) + val * c["n"]
            for card, v in c["trk"].get(d, {}).items():
                a = nums(v)
                if a and any(a):
                    t = x["trk"].setdefault(card, [0, 0, 0, 0])
                    for i in range(4):
                        t[i] += a[i] * c["n"]
    L += ["", "## Per mazzo (tutte le partite del mazzo nell'arma, medie per partita)", "",
          "| Mazzo | n | R9-5 | Rimonte R9-8 (n) | M6 Unità ferme | M14 costi in Vita | Attacchi del Leader | on_attack del Leader | Attivazioni del Leader (⟳, trigger e statiche in scontro) / ⟳ seguite da colpo | furia_bonus | Scudo ≥2 gemme | Primo colpo al Leader (round) | Forza max a 2 gemme | Carte per colore | Turni con una sola Unità | Attacchi al Leader di Unità con Caccia |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for d in [o for o in ORDER if o in per]:
        x = per[d]; nn = x["n"]; g = lambda h: x["cnt"].get(h, 0) / nn
        cols = ", ".join(f"{k[4:]} {v/nn:.0f}%" for k, v in sorted(x["cnt"].items()) if k.startswith("col_"))
        L.append(f"| {d} | {nn} | {x['r95']/nn:.2f} | {100*x['rk']/max(x['rn'],1):.0f}% ({x['rn']}) | {x['m6']/nn:.1f}% | {x['m14']/nn:.2f} | "
                 f"{g('Attacchi del Leader'):.2f} | {g('on_attack del Leader eseguiti'):.2f} | "
                 f"{g('Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno'):.2f} / {g('Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno (2)'):.2f} | "
                 f"{g('Scontri con furia_bonus'):.2f} | {g('Scudo a ≥2 gemme'):.2f} | {x['fh']/max(x['fhn'],1):.1f} | {x['peak']:.0f} | {cols} | "
                 + (f"{g('Turni con una sola Unità in campo'):.2f} | {g('Attacchi al Leader di Unità con Caccia'):.2f} |" if 'Turni con una sola Unità in campo' in x['cnt'] else "non misurati | non misurati |"))
    cards = sorted({card for x in per.values() for card in x["trk"]})
    if cards:
        L += ["", "## Carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)", "",
              "| Mazzo | " + " | ".join(cards) + " |", "|---|" + "---|" * len(cards)]
        for d in [o for o in ORDER if o in per]:
            x = per[d]; nn = x["n"]
            L.append(f"| {d} | " + " | ".join("/".join(f"{v/nn:.2f}" for v in x["trk"][cd]) if cd in x["trk"] else "—" for cd in cards) + " |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    arms = sys.argv[2:] or sorted(os.path.basename(p) for p in glob.glob(f"{ROOT}/*") if os.path.isdir(p))
    for ia in os.environ.get("IA", "S F").split():
        REF = {"19_T1b": "08_T1", "20_T1b_PB": "09_T1_PB", "21_T1b_V2": "11_T1_V2"}
        for a in arms:
            cells = arm(f"{ROOT}/{a}", ia)
            if not cells:
                continue
            ref = REF.get(a, "00_B0")
            base = arm(f"{ROOT}/{ref}", ia)
            out = f"{ROOT}/{a}/esito_{ia}.md"
            open(out, "w", encoding="utf-8").write(render(a, ia, cells, None if a == "00_B0" else base, ref))
            print("scritto", out)
