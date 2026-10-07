"""Rule configuration for the v0.2 candidate core (B0 of Q-013).

Every rule choice still open in the debate is a parameter here, so each variant of
tcg/swarm/questioni/Q-013_rework_nucleo_v0.2/esperimento.md is a preset, not code."""
from dataclasses import dataclass, asdict, replace


@dataclass(frozen=True)
class Rules2:
    # open choices (esperimento.md §4)
    pugno: str = "simultaneo"          # "sequenziale" (V1-B) | "nessuno" (V2-B: risposta unica a carte scoperte)
    opposizione: str = "prima"         # "dopo" (V3-B: dopo l'apertura del pugno)
    raddrizzo: str = "ripristino"      # "fine" (V4-B)
    scudo: str = "oppone_senza_ruotarsi"   # "vince_pareggi"

    forza_per_gemma: int = 1
    parata_per_gemma: int = 2

    # Leader
    leader_power: int = 3
    leader_power_awakened: int = 4
    tempra: int = 5
    life: int = 5
    awaken_at_life: int = 2
    guard_max: int = 2
    guard_max_awakened: int = 3
    guard_alle_corde_bonus: int = 1    # ex Ultimo respiro

    # setup and turn
    hand: int = 5
    mulligan_max: int = 3
    brace_max: int = 8                 # Brace = min(round, brace_max)
    scintilla_g2_gems: int = 1         # G2 +1 gemma nel round 1
    g2_hand_extra: int = 0             # carte in più nella mano iniziale di G2 (dopo il mulligan)
    no_attack_round: int = 1

    # Vita, Saldo, Clessidra, Crepuscolo
    saldo: int = 2
    saldo_late: int = 3
    saldo_late_round: int = 10
    corde_one_life_round: int = 13
    crepuscolo_round: int = 15
    crepuscolo_loss: int = 2

    # limits
    max_units: int = 5
    max_relics: int = 2
    hand_limit: int = 8
    max_rounds: int = 17

    # card values referenced as @name
    grido_hand: int = 3
    grido_scars: int = 5
    muro_bonus: int = 4

    def with_(self, **kw):
        return replace(self, **kw)

    def as_dict(self):
        return asdict(self)


B0 = Rules2()

PRESETS = {
    "B0": {},
    "V1B_sequenziale": {"pugno": "sequenziale"},
    "V2B_scoperto": {"pugno": "nessuno"},
    "V3B_opposizione_dopo": {"opposizione": "dopo"},
    "V4B_raddrizzo_fine": {"raddrizzo": "fine"},
    "S_scudo_pareggi": {"scudo": "vince_pareggi"},
}


def rules_from(spec, base=B0):
    """A preset name, a JSON file {"base": preset, "set": {...}} or a dict."""
    import json
    import os
    if isinstance(spec, str) and spec in PRESETS:
        return base.with_(**PRESETS[spec])
    if isinstance(spec, str):
        if not os.path.exists(spec):
            raise ValueError(f"variante sconosciuta: {spec}")
        with open(spec, encoding="utf-8") as f:
            spec = json.load(f)
    r = rules_from(spec["base"], base) if spec.get("base") else base
    unknown = set(spec.get("set", {})) - set(Rules2.__dataclass_fields__)
    if unknown:
        raise ValueError(f"parametri sconosciuti: {sorted(unknown)}")
    return r.with_(**spec.get("set", {}))
