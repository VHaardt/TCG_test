"""Play one side of a game against an AI, one decision per command (for playtester agents).

  python -m sim.gioca nuova --mazzo maera_blu_nero --contro arden_rosso_verde --ia semplice --seed 3 --file partita.json
  python -m sim.gioca mossa --file partita.json 4      # choose action number 4
  python -m sim.gioca stato --file partita.json        # print the state again

The file stores the seed and every action taken, so the game is rebuilt exactly each
time and the whole log can be read at the end (`--log`). The human/agent side is P1
unless --secondo is given. Only information visible to that player is printed."""
import argparse
import json

from .agents import make_agent
from .cards import CARDS, LEADERS
from .config import rules_from
from .engine import new_game
from .run import load_deck


def rebuild(g):
    me_first = not g.get("secondo")
    decks = [g["mazzo"], g["contro"]] if me_first else [g["contro"], g["mazzo"]]
    (l1, d1), (l2, d2) = load_deck(decks[0]), load_deck(decks[1])
    s = new_game(l1, d1, l2, d2, rules=rules_from(g.get("variante", "default")), seed=g["seed"], log=True)
    for act in g["azioni"]:
        s.step(tuple(act))
    return s, (0 if me_first else 1)


def advance(g, s, me):
    ai = make_agent(g["ia"], seed=g["seed"] + len(g["azioni"]))
    while not s.over and s.decider() != me:
        act = ai.act(s)
        g["azioni"].append(list(act))
        s.step(act)


def describe_action(s, act):
    a = s.decider()
    k = act[0]
    if k == "end":
        return "Termina il turno"
    if k == "play":
        c = CARDS[act[1]]
        t = f" → {s.describe(1 - a if (c.play or {}).get('target', {}).get('side') == 'opp' else a, act[2])}" if act[2] else ""
        return f"Gioca {c.name} ({c.cost}){t}"
    if k == "infuse":
        return f"Infondi 1 Brace in {s.describe(a, act[1])}"
    if k == "attack":
        return f"Attacca con {s.describe(a, act[1])} → {s.describe(1 - a, act[2])}"
    if k == "rim":
        return f"Rimargina: {CARDS[act[1]].name} in mano"
    if k == "spark":
        return "Usa la Scintilla (+1 Brace)"
    if k == "leader_ability":
        return f"Abilità del Leader → {s.describe(1 - a, act[2]) if act[2] else ''}"
    if k == "no_intercept":
        return "Non intercettare"
    if k == "intercept":
        return f"Intercetta con {s.describe(a, act[1])}"
    if k == "no_react":
        return "Nessuna reazione"
    if k == "parry":
        return f"Parata spendendo {act[1]} Guardia (+{s.parry_per_guard(a) * act[1]})"
    if k == "reaction":
        return f"Reazione: {CARDS[act[1]].name}" + (" dalle Cicatrici" if act[2] == "scar" else " dalla mano")
    if k == "leader_reaction":
        return "Reazione del Leader"
    return str(act)


def show(s, me):
    out = []
    for q, label in ((1 - me, "AVVERSARIO"), (me, "TU")):
        p = s.p[q]
        lead = LEADERS[p.leader].name + (" (Risvegliato)" if p.awakened else "")
        out.append(f"[{label}] {lead} | Vite {len(p.life)} | Fornace {p.furnace} | Brace {p.brace} | "
                   f"Guardia {p.guard} | mano {len(p.hand)} | mazzo {len(p.deck)} | turno {p.turn_no}"
                   + (" | Leader Esposto" if p.l_exposed else ""))
        if p.scars:
            out.append("   Cicatrici: " + ", ".join(CARDS[c].name for c in p.scars))
        for u in p.units:
            out.append(f"   - {CARDS[u.cid].name} Forza {s.unit_power(q, u)}"
                       + (" Esposta" if u.exposed else " Pronta"))
        if p.relics:
            out.append("   Reliquie: " + ", ".join(CARDS[c].name for c in p.relics))
    out.append("La tua mano: " + ", ".join(f"{CARDS[c].name} ({CARDS[c].cost})" for c in s.p[me].hand))
    if s.combat:
        out.append(f"Combattimento: {s.describe(s.active, s.combat.att)} (Forza {s.att_power()}) → "
                   f"{s.describe(1 - s.active, s.combat.tgt)} (difesa {s.def_value()})")
    if s.over:
        out.append(f"PARTITA FINITA: {'hai vinto' if s.winner == me else 'hai perso'} ({s.end_reason})")
    else:
        out.append("Azioni legali:")
        for i, act in enumerate(s.legal_actions()):
            out.append(f"  {i}. {describe_action(s, act)}")
    return "\n".join(out)


def main(argv=None):
    p = argparse.ArgumentParser(prog="python -m sim.gioca")
    sub = p.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("nuova")
    n.add_argument("--mazzo", required=True)
    n.add_argument("--contro", required=True)
    n.add_argument("--ia", default="semplice")
    n.add_argument("--seed", type=int, default=0)
    n.add_argument("--variante", default="default")
    n.add_argument("--secondo", action="store_true")
    n.add_argument("--file", required=True)
    m = sub.add_parser("mossa")
    m.add_argument("--file", required=True)
    m.add_argument("numero", type=int)
    st = sub.add_parser("stato")
    st.add_argument("--file", required=True)
    st.add_argument("--log", action="store_true")
    a = p.parse_args(argv)
    if a.cmd == "nuova":
        g = {"mazzo": a.mazzo, "contro": a.contro, "ia": a.ia, "seed": a.seed, "variante": a.variante,
             "secondo": a.secondo, "azioni": []}
        s, me = rebuild(g)
        advance(g, s, me)
    else:
        with open(a.file, encoding="utf-8") as f:
            g = json.load(f)
        s, me = rebuild(g)
        if a.cmd == "mossa":
            acts = s.legal_actions()
            act = acts[a.numero]
            g["azioni"].append(list(act))
            s.step(act)
            advance(g, s, me)
    with open(a.file, "w", encoding="utf-8") as f:
        json.dump(g, f)
    if getattr(a, "log", False):
        print("\n".join(s.log))
        print()
    print(show(s, me))


if __name__ == "__main__":
    main()
