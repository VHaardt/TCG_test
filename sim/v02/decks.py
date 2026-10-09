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

DECK_SIZE, MAX_COPIES = 40, 3


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


def problems(leader, cards, card_colors=None, leader_colors=None):
    """Deck-building rules (regolamento §2.3) against a card database: {id: colors}, {leader: colors}."""
    card_colors = card_colors if card_colors is not None else {cid: c.colors for cid, c in engine.CARDS.items()}
    leader_colors = leader_colors if leader_colors is not None else {lid: l.colors for lid, l in engine.LEADERS.items()}
    out = []
    if leader not in leader_colors:
        return [f"Leader sconosciuto '{leader}'"]
    unknown = sorted(cid for cid in cards if cid not in card_colors)
    if unknown:
        out.append("id sconosciuti: " + ", ".join(unknown))
    n = sum(cards.values())
    if n != DECK_SIZE:
        out.append(f"{n} carte invece di {DECK_SIZE}")
    lcol = set(leader_colors[leader])
    for cid, k in cards.items():
        if cid not in card_colors:
            continue
        if k > MAX_COPIES:
            out.append(f"{cid}: {k} copie")
        if card_colors[cid] and not set(card_colors[cid]) & lcol:
            out.append(f"{cid}: colore fuori dal Leader")
    return out


def load(ref):
    """(leader, list of card ids) of a legal deck; ValueError naming the deck otherwise."""
    leader, cards = raw_deck(ref)
    pr = problems(leader, cards)
    if pr:
        raise ValueError(f"mazzo {ref} illegale per {engine.LOADED[0]}: " + "; ".join(pr))
    return leader, [cid for cid, k in cards.items() for _ in range(k)]
