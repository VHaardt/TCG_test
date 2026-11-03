"""Q-028: una partita con il log di `sim.v02.run partita`, più una riga per turno con le opzioni della fase principale.
Il motore non si modifica: un involucro di GameState.step legge le azioni legali (le stesse che il motore conta).

  python3 -B partita_annotata.py <radice_sim> <carte.json> <mazzi.json> <lista1> <lista2> <seme> [--ia forte:30] [--variante V027]

Stampa il log; prima di ogni turno aggiunge:
  [opzioni] prima scelta: N azioni legali (G «gioca», A attacchi, R Rimarginare, ⟳ abilità) · mano H · gemme B · scelte nel turno S
La riga si scrive alla fine del turno, quindi descrive il turno che la precede nel file (il blocco "--- Round …" sopra di lei).
"""
import argparse, os, sys
ap = argparse.ArgumentParser()
for k in ("sim", "carte", "mazzi", "l1", "l2"):
    ap.add_argument(k)
ap.add_argument("seme", type=int); ap.add_argument("--ia", default="forte:30"); ap.add_argument("--variante", default="V027")
a = ap.parse_args()
sys.path.insert(0, os.path.abspath(a.sim))
from sim.v02 import run, engine  # noqa: E402

_step, _end = engine.GameState.step, engine.GameState.end_turn


def step(self, act):
    if self.stats is not None and self.phase == "main":
        legal = self.legal_actions()
        t = getattr(self, "_t", None)
        if t is None:
            pl = self.p[self.active]
            kinds = [x[0] for x in legal]
            t = self._t = {"n": len(legal), "G": kinds.count("play"), "A": kinds.count("attack"), "R": kinds.count("rim"),
                           "ab": kinds.count("ability"), "h": len(pl.hand), "b": pl.brace, "s": 0}
        t["s"] += 1
    return _step(self, act)


def end_turn(self):
    t = getattr(self, "_t", None)
    if self.stats is not None and t is not None:
        self.say(f"  [opzioni] prima scelta: {t['n']} azioni legali (G {t['G']}, A {t['A']}, R {t['R']}, ⟳ {t['ab']}) · mano {t['h']} · gemme {t['b']} · scelte nel turno {t['s']}")
    self._t = None
    return _end(self)


engine.GameState.step, engine.GameState.end_turn = step, end_turn
run.CARTE[0] = os.path.abspath(a.carte)
run.use_cards(run.CARTE[0])
r = run.play_game(((f"{a.mazzi}#{a.l1}", f"{a.mazzi}#{a.l2}"), (a.ia, a.ia), a.variante, a.seme, True, run.CARTE[0]))
print("\n".join(r["log"]))
print(f"\nVincitore: P{(r['winner'] or 0) + 1} ({r['end_reason']}), round {r['rounds']}")
