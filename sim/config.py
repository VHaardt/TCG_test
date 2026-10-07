"""Rule configuration for CICATRICI.

Two layers, both meant to be edited freely while the game is being designed:
  * `modules`: which rule modules (sim/rules.py) are switched on. Removing a name
    removes that rule from the game; adding a new module class adds a rule.
  * numeric parameters (regolamento §15), read by the engine, the modules and the
    cards (a card value written as "@name" in the card data reads `name` from here).
Variants and control tests of regolamento §16 are named presets at the bottom."""
from dataclasses import dataclass, asdict, replace

DEFAULT_MODULES = (
    "primo_turno",           # §11: nobody attacks on own turn 1, G1 skips first draw
    "scintilla",             # §5.5
    "saldo",                 # §9.2
    "clessidra",             # §9.6: Saldo 3 from turn 10, Alle Corde at 1 Vita from turn 13
    "crepuscolo_terminale",  # §9.6: hard limit from turn 15
    "risveglio",             # §9.8
    "rimarginare",           # §10.2
    "ultimo_respiro",        # §8 step 5
)


@dataclass(frozen=True)
class Rules:
    modules: tuple = DEFAULT_MODULES

    # Leader (§2.2)
    leader_power: int = 3
    leader_power_awakened: int = 4
    leader_tempra: int = 5
    life: int = 5
    leader_hit_strict: bool = False      # T1: hit only if Forza > Tempra

    # setup (§4)
    hand_g1: int = 5
    hand_g2: int = 5                     # V2: 6
    mulligan_max: int = 3
    deck_size: int = 40

    # resources (§5)
    furnace_max: int = 8
    guard_max: int = 2
    guard_max_awakened: int = 3
    parry_per_guard: int = 2
    parry_max_guard: int = 0             # 0 = Parata scalabile; 1 = Parata fissa della bozza
    infusion_cap: int = 0                # §16.4 reserve lever (0 = no cap)

    # reactions (§8)
    reactions_per_turn: int = 1          # used when module reazione_per_attacco is off

    # Saldo / Clessidra / Crepuscolo (§9)
    saldo: int = 2
    saldo_late: int = 3
    saldo_late_turn: int = 10
    corde_one_life_turn: int = 13
    crepuscolo_turn: int = 15
    crepuscolo_loss: int = 2
    clessidra_counter: str = "active"    # V4: "round" = G1's turn number for both players
    bozza_crepuscolo_turn: int = 10      # module crepuscolo_bozza (T2)

    # Risveglio (§9.8)
    awaken_after_lost: int = 3
    awaken_on_turn: int = 7              # module risveglio_a_tempo (§16.4 lever)

    # Rimarginare (§10.2): "exhaust" = ⟳ ability of the Leader, "base" = no ⟳
    rimarginare_mode: str = "exhaust"
    rimarginare_cost: int = 1

    # Scintilla (§5.5)
    spark_gives_guard: int = 0

    # card values referenced as @name in the card data (V6 etc.)
    grido_hand: int = 3
    grido_scars: int = 5
    muro_bonus: int = 4

    # limits
    max_units: int = 5
    max_relics: int = 2
    hand_limit: int = 8
    max_turns: int = 17                  # §16.5 simulator safety cut

    def with_(self, **kw):
        return replace(self, **kw)

    def with_modules(self, add=(), remove=()):
        mods = [m for m in self.modules if m not in remove]
        mods += [m for m in add if m not in mods]
        return replace(self, modules=tuple(mods))

    def as_dict(self):
        return asdict(self)


DEFAULT = Rules()

# Presets for the variants (V) and control tests (T) of regolamento §16.
# Each preset is {"set": {param: value}, "add": [modules], "remove": [modules]}.
VARIANTS = {
    "default": {},
    "V1b_per_attack": {"add": ["reazione_per_attacco"], "remove": ["ultimo_respiro"]},
    "V2_g2_six": {"set": {"hand_g2": 6}},
    "V2_g2_six_nospark": {"set": {"hand_g2": 6}, "remove": ["scintilla"]},
    "V3_loss1": {"set": {"crepuscolo_loss": 1}},
    "V3_turn14": {"set": {"crepuscolo_turn": 14}},
    "V4_round_counter": {"set": {"clessidra_counter": "round"}},
    "V6_grido_4_6": {"set": {"grido_hand": 4, "grido_scars": 6}},
    "T1_power4_strict": {"set": {"leader_power": 4, "leader_power_awakened": 5, "leader_tempra": 4,
                                 "leader_hit_strict": True}},
    "T2_bozza_crepuscolo": {"add": ["crepuscolo_bozza"], "remove": ["clessidra", "crepuscolo_terminale"]},
    "T3_riscossa": {"add": ["riscossa"], "remove": ["rimarginare"]},
    "T3_rim_base": {"set": {"rimarginare_mode": "base"}},
    "T4_no_ultimo_respiro": {"remove": ["ultimo_respiro"]},
    "L_risveglio_turno7": {"add": ["risveglio_a_tempo"]},
    # introduzione in sequenza (regolamento §16.3)
    "I1_solo_tempra5": {"set": {"parry_max_guard": 1}, "remove": ["ultimo_respiro"]},
    "I2_parata_scalabile": {"remove": ["ultimo_respiro"]},
}


def rules_for(name, base=DEFAULT):
    v = VARIANTS[name]
    r = base.with_(**v.get("set", {}))
    return r.with_modules(add=v.get("add", ()), remove=v.get("remove", ()))


def rules_from(spec, base=DEFAULT):
    """A rule configuration from a preset name, a JSON file path or a dict.
    JSON / dict format: {"base": "<preset>", "set": {param: value}, "add": [modules], "remove": [modules]}.
    This is how the swarm proposes a variant without touching the code."""
    import json
    import os
    if isinstance(spec, str) and spec in VARIANTS:
        return rules_for(spec, base)
    if isinstance(spec, str):
        if not os.path.exists(spec):
            raise ValueError(f"variante sconosciuta: {spec} (né preset né file)")
        with open(spec, encoding="utf-8") as f:
            spec = json.load(f)
    r = rules_for(spec["base"], base) if spec.get("base") else base
    unknown = set(spec.get("set", {})) - set(Rules.__dataclass_fields__)
    if unknown:
        raise ValueError(f"parametri sconosciuti: {sorted(unknown)}")
    r = r.with_(**spec.get("set", {}))
    return r.with_modules(add=spec.get("add", ()), remove=spec.get("remove", ()))
