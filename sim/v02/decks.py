"""Deck files for the v0.2 core, checked against the v0.2 card database (engine.CARDS).

A deck reference is one of:
  name               sim/decks/<name>.json (reference decks)
  path.json          a file with one deck: {"leader": id, "cards": {id: copies} or [id, id, ...]}
  path.json#name     one deck of a file with several: {"mazzi": [{"name", "leader", "cards"}, ...]}
A file with "mazzi" given without #name stands for all its decks (expand())."""
import glob
import json
import os

from ..run import DECK_DIR
from . import engine

DECK_SIZE, MAX_COPIES = 40, 3            # valori di B0 (V026); i limiti in vigore sono regole: limits(rules)


def limits(rules=None):
    """Deck-building limits of a rule set (config.Rules2), as a plain dict (also for the app)."""
    if rules is None:
        return {"deck_size": DECK_SIZE, "max_copies": MAX_COPIES, "copies_by_name": False,
                "max_copies_rarity": {}, "multicolor_all": False, "rarity_scale": []}
    return {"deck_size": rules.deck_size, "max_copies": rules.max_copies, "copies_by_name": rules.copies_by_name,
            "max_copies_rarity": dict(rules.max_copies_rarity), "multicolor_all": rules.multicolor_all,
            "rarity_scale": list(rules.rarity_scale)}


def card_info():
    """{id: (name, rarity)} of the loaded card database."""
    return {cid: (c.name or cid, engine.META.get(cid, {}).get("rarity")) for cid, c in engine.CARDS.items()}


def _read(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def expand(refs):
    out = []
    for ref in refs:
        if ref.endswith(".json") and os.path.exists(ref) and "mazzi" in _read(ref):
            out += [f"{ref}#{d['name']}" for d in _read(ref)["mazzi"]]
        else:
            out.append(ref)
    return out


def label(ref):
    """Short name of a deck reference for reports."""
    path, _, name = ref.partition("#")
    if name:
        return name
    return os.path.splitext(os.path.basename(path))[0] if path.endswith(".json") else ref


def reference_decks():
    """Reference decks of sim/decks (files starting with '_' excluded)."""
    names = (os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(DECK_DIR, "*.json")))
    return sorted(n for n in names if not n.startswith("_"))


def raw_deck(ref):
    """(leader, {cid: copies}) in file order, without checks."""
    path, _, name = ref.partition("#")
    if not path.endswith(".json"):
        path = os.path.join(DECK_DIR, path + ".json")
    if not os.path.exists(path):
        raise ValueError(f"mazzo {ref}: file {path} inesistente")
    d = _read(path)
    if name or "mazzi" in d:
        found = [x for x in d.get("mazzi", []) if x.get("name") == name]
        if not found:
            raise ValueError(f"mazzo {ref}: nessun mazzo '{name}' in {path}")
        d = found[0]
    cards = d["cards"]
    if isinstance(cards, list):
        counts = {}
        for cid in cards:
            counts[cid] = counts.get(cid, 0) + 1
        cards = counts
    return d["leader"], cards


def problems(leader, cards, card_colors=None, leader_colors=None, rules=None, info=None):
    """Deck-building rules (regolamento §2.3) against a card database: {id: colors}, {leader: colors},
    info {id: (name, rarity)}. rules: config.Rules2 (None = limits of B0: 40 cards, 3 copies per ID)."""
    lim = limits(rules)
    card_colors = card_colors if card_colors is not None else {cid: c.colors for cid, c in engine.CARDS.items()}
    leader_colors = leader_colors if leader_colors is not None else {lid: l.colors for lid, l in engine.LEADERS.items()}
    info = info if info is not None else card_info()
    out = []
    if leader not in leader_colors:
        return [f"Leader sconosciuto '{leader}'"]
    unknown = sorted(cid for cid in cards if cid not in card_colors)
    if unknown:
        out.append("id sconosciuti: " + ", ".join(unknown))
    n = sum(cards.values())
    if n != lim["deck_size"]:
        out.append(f"{n} carte invece di {lim['deck_size']}")
    lcol = set(leader_colors[leader])
    by_name = {}
    for cid, k in cards.items():
        if cid not in card_colors:
            continue
        name, rar = info.get(cid, (cid, None))
        key = name if lim["copies_by_name"] else cid
        by_name.setdefault(key, [0, set(), lim["max_copies"]])
        g = by_name[key]
        g[0] += k
        g[1].add(cid)
        g[2] = min(g[2], lim["max_copies_rarity"].get(rar, lim["max_copies"]))
        col = set(card_colors[cid] or ())
        if col and not (col <= lcol if lim["multicolor_all"] else col & lcol):
            out.append(f"{cid}: colore fuori dal Leader" if not col & lcol or len(col) == 1
                       else f"{cid}: carta multicolore, il Leader non ha tutti i suoi colori")
    for key, (k, ids, cap) in by_name.items():
        if k > cap:
            who = key if ids == {key} else f"{key} ({', '.join(sorted(ids))})"
            out.append(f"{who}: {k} copie (massimo {cap})")
    return out


def rarity_warnings(rules, info):
    """Rarities outside the scale of the rules: a warning, never an error (rarity does not change games)."""
    scale = set(limits(rules)["rarity_scale"])
    if not scale:
        return []
    off = sorted(cid for cid, (_, rar) in info.items() if rar not in scale)
    return [f"{len(off)} carte con rarità fuori dalla scala {'/'.join(limits(rules)['rarity_scale'])}: "
            + ", ".join(off[:12]) + (" …" if len(off) > 12 else "")] if off else []


def load(ref, rules=None):
    """(leader, list of card ids) of a legal deck under rules (§2.3); ValueError naming the deck otherwise."""
    leader, cards = raw_deck(ref)
    pr = problems(leader, cards, rules=rules)
    if pr:
        raise ValueError(f"mazzo {ref} illegale per {engine.LOADED[0]}: " + "; ".join(pr))
    return leader, [cid for cid, k in cards.items() for _ in range(k)]
