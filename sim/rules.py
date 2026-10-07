"""Pluggable rule modules.

Each rule of the regolamento that is not part of the bare skeleton (turns, Brace,
cards, combat, colpo finale) is a module here. A module is switched on by listing
its name in `Rules.modules` (sim/config.py). To add a new rule, write a subclass of
RuleModule, override the hooks it needs and register it in MODULES; to remove a
rule, drop its name from the config. Section numbers refer to regolamento_v0.1.md.

Hooks (all optional; "chain" hooks receive the current value and return a new one):
  on_setup(s)                       after hands and Vita are dealt
  on_turn_start(s, a)               Ripristino, after turn number and snapshot, before readying
  is_alle_corde(s, q) -> bool       extra conditions for Alle Corde (OR-ed with Vita == 0)
  saldo_cap(s, cap) -> cap          chain; None = no cap
  on_life_lost(s, q, card) -> bool  return True if the module placed the card itself
  reaction_limit(s, d, lim) -> lim  chain
  can_attack(s, a) -> bool          AND-ed
  skip_draw(s, a) -> bool           OR-ed
  extra_actions(s, a) -> [actions]  main-phase actions owned by the module
  do_action(s, a, action) -> bool   apply one of its actions
  state_check(s)                    §7.4
"""
from . import effects


class RuleModule:
    name = ""

    def on_setup(self, s): pass
    def on_turn_start(self, s, a): pass
    def is_alle_corde(self, s, q): return False
    def saldo_cap(self, s, cap): return cap
    def on_life_lost(self, s, q, card): return False
    def reaction_limit(self, s, d, lim): return lim
    def can_attack(self, s, a): return True
    def skip_draw(self, s, a): return False
    def extra_actions(self, s, a): return []
    def do_action(self, s, a, action): return False
    def state_check(self, s): pass


class PrimoTurno(RuleModule):
    """§11: nobody attacks on their own turn 1; G1 does not draw on turn 1."""
    name = "primo_turno"

    def can_attack(self, s, a):
        return s.p[a].turn_no > 1

    def skip_draw(self, s, a):
        return a == 0 and s.p[a].turn_no == 1


class Scintilla(RuleModule):
    """§5.5: G2 has a one-shot +1 Brace."""
    name = "scintilla"

    def on_setup(self, s):
        s.p[1].spark = True

    def extra_actions(self, s, a):
        return [("spark",)] if s.p[a].spark else []

    def do_action(self, s, a, action):
        if action[0] != "spark":
            return False
        pl = s.p[a]
        pl.spark = False
        pl.brace += 1
        if s.r.spark_gives_guard:
            pl.guard = min(pl.guard + s.r.spark_gives_guard, s.guard_max(a))
        return True


class Saldo(RuleModule):
    """§9.2: a Leader loses at most `saldo` Vite per turn."""
    name = "saldo"

    def saldo_cap(self, s, cap):
        return s.r.saldo


class Clessidra(RuleModule):
    """§9.6 first two steps: Saldo 3 from turn 10, Alle Corde at 1 Vita from turn 13."""
    name = "clessidra"

    def saldo_cap(self, s, cap):
        if cap is not None and s.clock() >= s.r.saldo_late_turn:
            return max(cap, s.r.saldo_late)
        return cap

    def is_alle_corde(self, s, q):
        return s.clock() >= s.r.corde_one_life_turn and len(s.p[q].life) == 1


class CrepuscoloTerminale(RuleModule):
    """§9.6 hard limit: from turn 15, Alle Corde at Ripristino loses, else lose 2 Vite (no Saldo)."""
    name = "crepuscolo_terminale"

    def on_turn_start(self, s, a):
        if s.clock() >= s.r.crepuscolo_turn:
            if s.alle_corde(a):
                s.lose(a, "crepuscolo")
            else:
                s.lose_life(a, s.r.crepuscolo_loss, "crepuscolo", ignore_saldo=True)


class CrepuscoloBozza(RuleModule):
    """T2: the draft rule. From turn 10 the active Leader loses 1 Vita (Saldo applies); at 0 it loses."""
    name = "crepuscolo_bozza"

    def on_turn_start(self, s, a):
        if s.clock() >= s.r.bozza_crepuscolo_turn:
            if not s.p[a].life:
                s.lose(a, "crepuscolo")
            else:
                s.lose_life(a, 1, "crepuscolo")


class Risveglio(RuleModule):
    """§9.8: after `awaken_after_lost` Vite lost the Leader flips to its Awakened side."""
    name = "risveglio"

    def state_check(self, s):
        for q in (s.active, 1 - s.active):
            if not s.p[q].awakened and s.r.life - len(s.p[q].life) >= s.r.awaken_after_lost:
                s.awaken(q)


class RisveglioATempo(RuleModule):
    """§16.4 reserve lever: also awaken at the start of your turn `awaken_on_turn`."""
    name = "risveglio_a_tempo"

    def on_turn_start(self, s, a):
        if s.p[a].turn_no >= s.r.awaken_on_turn and not s.p[a].awakened:
            s.awaken(a)


class Rimarginare(RuleModule):
    """§10.2: once per turn, pay 1 Brace to put a Cicatrice in hand. Mode "exhaust"
    makes it a ⟳ ability of the Leader (Leader must be Pronto and becomes Esposto)."""
    name = "rimarginare"

    def _cost(self, s, a):
        pl = s.p[a]
        if effects.leader_modifier(s, a, "rim_free_once") and not pl.flag("rim_free_used"):
            return 0
        return s.r.rimarginare_cost

    def extra_actions(self, s, a):
        pl = s.p[a]
        if not pl.scars or pl.flag("rim_used"):
            return []
        if s.r.rimarginare_mode == "exhaust" and pl.l_exposed:
            return []
        if pl.brace < self._cost(s, a):
            return []
        s.mark_rim_possible(a)
        return [("rim", cid) for cid in sorted(set(pl.scars))]

    def do_action(self, s, a, action):
        if action[0] != "rim":
            return False
        pl = s.p[a]
        cost = self._cost(s, a)
        if cost == 0:
            pl.set_flag("rim_free_used")
        pl.brace -= cost
        pl.set_flag("rim_used")
        if s.r.rimarginare_mode == "exhaust":
            pl.l_exposed = True
        pl.scars.remove(action[1])
        pl.hand.append(action[1])
        if effects.leader_modifier(s, a, "rim_keeps_furia"):
            pl.furia_bonus += 1
        s.stat("rim_used", a)
        return True


class Riscossa(RuleModule):
    """T3 alternative: the first Vita you lose each turn goes to your hand instead of the Cicatrici."""
    name = "riscossa"

    def on_life_lost(self, s, q, card):
        pl = s.p[q]
        if pl.flag("riscossa_used"):
            return False
        pl.set_flag("riscossa_used")
        pl.hand.append(card)
        return True


class UltimoRespiro(RuleModule):
    """§8 step 5: a defender whose Leader was Alle Corde at the start of the turn gets 2 reactions."""
    name = "ultimo_respiro"

    def reaction_limit(self, s, d, lim):
        return lim + 1 if s.snapshot else lim


class ReazionePerAttacco(RuleModule):
    """V1-b: one reaction per attack instead of per turn (every reaction costs >= 1 Guardia)."""
    name = "reazione_per_attacco"

    def reaction_limit(self, s, d, lim):
        return 10 ** 6


MODULES = {cls.name: cls for cls in (
    PrimoTurno, Scintilla, Saldo, Clessidra, CrepuscoloTerminale, CrepuscoloBozza,
    Risveglio, RisveglioATempo, Rimarginare, Riscossa, UltimoRespiro, ReazionePerAttacco)}


def build(names):
    unknown = [n for n in names if n not in MODULES]
    if unknown:
        raise ValueError(f"moduli sconosciuti: {unknown}")
    return [MODULES[n]() for n in names]
