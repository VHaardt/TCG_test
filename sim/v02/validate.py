"""Strict schema of the v0.2 card language (R-006 §0).

Every key, condition, event, op and selector field the engine reads is listed here; anything
else is an error naming the card. Keys starting with "_" and descriptive fields are free.
Used by engine.load_cards() and by `python3 -m sim.v02.run valida <file>`."""
import numbers

DESCRIPTIVE = {"text", "name", "rarity", "slot", "tags", "intent", "vanilla_delta", "note", "notes", "test"}
CARD_KEYS = {"id", "type", "cost", "colors", "power", "keywords", "kw_params", "abilities", "play", "react", "costs"}
LEADER_KEYS = {"id", "colors", "base", "awakened"}
TYPES = {"unit", "tactic", "reaction", "relic"}
KEYWORDS = {"assalto", "scudo", "bracconiere", "caccia", "impeto", "infuso", "furia", "rinnovo"}
KW_PARAMS = {"bracconiere"}
EVENTS = {"on_enter", "on_attack", "on_oppose", "on_defeats_attacker", "on_own_unit_defeats_unit",
          "on_attack_defeats_unit", "on_own_unit_attack_defeats_unit", "on_own_reaction"}
COMBAT_EVENTS = {"on_attack", "on_oppose"}           # where att_mod / def_mod are read
STATICS = {"power": {"value", "if", "applies_to", "stack"},
           "guard_max": {"value", "cap", "if", "stack"},
           "furia_bonus": {"value", "if", "stack"},
           "combat": {"role", "if", "att_mod", "def_mod", "stack"},
           "parata_per_gemma": {"value"}}
MODIFIERS = {"rim_cost"}
# condition -> type of its value
CONDITIONS = {"furia": int, "scars_ge": int, "awakened": bool, "attacking": bool, "pugno_ge": int,
              "deck_nonempty": bool, "target_is_unit": bool, "opposing": bool, "attacker_has": str,
              "react_from_scars": bool, "hunted_ready": bool, "survived": bool}
SELECTOR = {"side", "cost_le", "ready", "power_le", "keyword", "attacker", "kind", "any", "if"}
OPS = {"draw": {"n"}, "att_mod": {"n"}, "def_mod": {"n"},
       "stanca": {"target", "sel"}, "defeat": {"target", "sel"}, "raddrizza": {"target", "sel"}}
OP_TARGETS = {"chosen", "self", "opposer", "attacker"}


def _free(k):
    return k.startswith("_") or k in DESCRIPTIVE


class _V:
    def __init__(self):
        self.errors = []

    def err(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def keys(self, where, d, allowed):
        if not isinstance(d, dict):
            self.err(where, f"atteso un oggetto, trovato {d!r}")
            return False
        for k in d:
            if k not in allowed and not _free(k):
                self.err(where, f"chiave sconosciuta '{k}'")
        return True

    def num(self, where, v, dyn=True):
        if isinstance(v, bool) or v is None:
            self.err(where, f"valore non numerico {v!r}")
        elif isinstance(v, numbers.Number):
            return
        elif isinstance(v, str):
            if not v.lstrip("-").startswith("@"):
                self.err(where, f"valore '{v}' (atteso numero o '@parametro')")
        elif isinstance(v, dict) and dyn:
            if "scars" in v:
                if set(v) != {"scars"} or v["scars"] not in ("own", "opp"):
                    self.err(where, f"valore dinamico {v!r} (atteso {{\"scars\": \"own\"|\"opp\"}})")
            elif "n" in v:
                self.keys(where, v, {"n", "plus", "if"})
                self.num(where + ".n", v["n"])
                self.num(where + ".plus", v.get("plus", 0))
                self.conds(where + ".if", v.get("if"))
            else:
                self.err(where, f"valore dinamico sconosciuto {v!r}")
        else:
            self.err(where, f"valore {v!r}")

    def conds(self, where, conds):
        if conds is None:
            return
        if not isinstance(conds, list):
            self.err(where, "'if' deve essere una lista")
            return
        for c in conds:
            if not isinstance(c, dict) or len(c) != 1:
                self.err(where, f"condizione {c!r} (una chiave per condizione)")
                continue
            (k, v), = c.items()
            t = CONDITIONS.get(k)
            if t is None:
                self.err(where, f"condizione sconosciuta '{k}'")
            elif t is int and (isinstance(v, bool) or not isinstance(v, int)):
                self.err(where, f"condizione '{k}' vuole un intero")
            elif t is not int and not isinstance(v, t):
                self.err(where, f"condizione '{k}' vuole {t.__name__}")
            elif k == "attacker_has" and v not in KEYWORDS:
                self.err(where, f"parola chiave sconosciuta '{v}'")

    def selector(self, where, sel):
        if not self.keys(where, sel, SELECTOR):
            return
        if sel.get("side", "own") not in ("own", "opp"):
            self.err(where, f"side '{sel['side']}'")
        for k in ("cost_le", "power_le"):
            if k in sel:
                self.num(f"{where}.{k}", sel[k])
        if "ready" in sel and not isinstance(sel["ready"], bool):
            self.err(where, "'ready' vuole true/false")
        if "keyword" in sel and sel["keyword"] not in KEYWORDS:
            self.err(where, f"parola chiave sconosciuta '{sel['keyword']}'")
        if "kind" in sel and sel["kind"] != "unit":
            self.err(where, f"kind '{sel['kind']}' (solo \"unit\")")
        self.conds(where + ".if", sel.get("if"))
        for i, s2 in enumerate(sel.get("any", [])):
            self.selector(f"{where}.any[{i}]", s2)

    def ops(self, where, ops, has_target, mods_ok):
        if not isinstance(ops, list):
            self.err(where, "'do' deve essere una lista")
            return
        for i, o in enumerate(ops):
            w = f"{where}[{i}]"
            if not isinstance(o, dict) or "op" not in o:
                self.err(w, "op senza 'op'")
                continue
            allowed = OPS.get(o["op"])
            if allowed is None:
                self.err(w, f"op sconosciuta '{o['op']}'")
                continue
            self.keys(w, o, allowed | {"op", "if"})
            self.conds(w + ".if", o.get("if"))
            if "n" in allowed:
                self.num(w + ".n", o.get("n", 0), dyn=False)
            if o["op"] in ("att_mod", "def_mod") and not mods_ok:
                self.err(w, f"'{o['op']}' vale solo in Reazioni e trigger on_attack/on_oppose")
            if "target" in allowed:
                t = o.get("target", "chosen")
                if t not in OP_TARGETS:
                    self.err(w, f"target '{t}' (ammessi: {sorted(OP_TARGETS)})")
                elif t == "chosen" and not has_target:
                    self.err(w, "target 'chosen' senza un selettore 'target' nell'abilità")
                if "sel" in o:
                    self.selector(w + ".sel", o["sel"])

    def costs(self, where, costs):
        if costs is None:
            return
        if not isinstance(costs, list):
            self.err(where, "'costs' deve essere una lista")
            return
        for i, c in enumerate(costs):
            if self.keys(f"{where}[{i}]", c, {"lose_life", "floor"}):
                if not isinstance(c.get("lose_life"), int):
                    self.err(f"{where}[{i}]", "'lose_life' vuole un intero")

    def ability(self, where, ab):
        if not isinstance(ab, dict):
            self.err(where, "abilità non è un oggetto")
            return
        kinds = [k for k in ("static", "trigger", "activated", "modifier") if k in ab]
        if len(kinds) != 1:
            self.err(where, f"un'abilità ha esattamente uno fra static/trigger/activated/modifier (trovati {kinds})")
            return
        kind = kinds[0]
        if kind == "static":
            allowed = STATICS.get(ab["static"])
            if allowed is None:
                self.err(where, f"statica sconosciuta '{ab['static']}'")
                return
            self.keys(where, ab, allowed | {"static"})
            if "value" in allowed:
                self.num(where + ".value", ab.get("value"))
            if "cap" in ab:
                self.num(where + ".cap", ab["cap"], dyn=False)
            if ab["static"] == "combat" and ab.get("role") != "defense":
                self.err(where, f"statica combat: role '{ab.get('role')}' (solo \"defense\")")
            if "stack" in ab and not isinstance(ab["stack"], bool):
                self.err(where, "'stack' vuole true/false")
            if "applies_to" in ab:
                self.selector(where + ".applies_to", ab["applies_to"])
            self.conds(where + ".if", ab.get("if"))
        elif kind == "trigger":
            self.keys(where, ab, {"trigger", "if", "target", "do"})
            if ab["trigger"] not in EVENTS:
                self.err(where, f"evento sconosciuto '{ab['trigger']}'")
            self.conds(where + ".if", ab.get("if"))
            if "target" in ab:
                self.selector(where + ".target", ab["target"])
            self.ops(where + ".do", ab.get("do", []), "target" in ab, ab["trigger"] in COMBAT_EVENTS)
        elif kind == "activated":
            self.keys(where, ab, {"activated", "cost", "costs", "target", "do"})
            self.num(where + ".cost", ab.get("cost", 0), dyn=False)
            self.costs(where + ".costs", ab.get("costs"))
            if "target" in ab:
                self.selector(where + ".target", ab["target"])
            self.ops(where + ".do", ab.get("do", []), "target" in ab, False)
        else:
            self.keys(where, ab, {"modifier", "value"})
            if ab["modifier"] not in MODIFIERS:
                self.err(where, f"modificatore sconosciuto '{ab['modifier']}'")

    def card(self, c):
        cid = c.get("id", "?")
        self.keys(cid, c, CARD_KEYS)
        if c.get("type") not in TYPES:
            self.err(cid, f"type '{c.get('type')}'")
        self.num(cid + ".cost", c.get("cost"), dyn=False)
        for k in c.get("keywords", []):
            if k not in KEYWORDS:
                self.err(cid, f"parola chiave sconosciuta '{k}'")
        for k, v in (c.get("kw_params") or {}).items():
            if k not in KW_PARAMS:
                self.err(cid, f"kw_params: chiave sconosciuta '{k}'")
            self.num(f"{cid}.kw_params.{k}", v, dyn=False)
        for i, ab in enumerate(c.get("abilities") or []):
            self.ability(f"{cid}.abilities[{i}]", ab)
        self.costs(cid + ".costs", c.get("costs"))
        if c.get("play") is not None:
            p = c["play"]
            if self.keys(cid + ".play", p, {"target", "do", "costs"}):
                if "target" in p:
                    self.selector(cid + ".play.target", p["target"])
                self.costs(cid + ".play.costs", p.get("costs"))
                self.ops(cid + ".play.do", p.get("do", []), "target" in p, False)
        if c.get("react") is not None:
            r = c["react"]
            if self.keys(cid + ".react", r, {"do", "do_from_scars"}):
                for k in ("do", "do_from_scars"):
                    if k in r:
                        self.ops(f"{cid}.react.{k}", r[k], False, True)
        if c.get("type") == "reaction" and not c.get("react"):
            self.err(cid, "Reazione senza 'react'")

    def leader(self, l):
        lid = l.get("id", "?")
        self.keys(lid, l, LEADER_KEYS)
        for side in ("base", "awakened"):
            for i, ab in enumerate(l.get(side) or []):
                self.ability(f"{lid}.{side}[{i}]", ab)


def validate(raw):
    """List of error strings for a card file already parsed from JSON (empty = valid)."""
    v = _V()
    seen = set()
    for c in raw.get("cards", []):
        if c.get("id") in seen:
            v.err(c.get("id"), "id duplicato")
        seen.add(c.get("id"))
        v.card(c)
    for l in raw.get("leaders", []):
        v.leader(l)
    return v.errors
