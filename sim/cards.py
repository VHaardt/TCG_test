"""Card database: loads cards and Leaders from sim/data/*.json.

Cards are pure data. Their effects are written in the small effect language that
sim/effects.py interprets (see sim/README.md). Adding or changing a card never
requires touching the engine."""
import json
import os
from dataclasses import dataclass, field

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


@dataclass(frozen=True)
class Card:
    id: str
    name: str
    type: str                     # unit | tactic | reaction | relic
    cost: int
    colors: tuple
    power: int = 0
    keywords: frozenset = field(default_factory=frozenset)
    kw_params: dict = field(default_factory=dict, hash=False, compare=False)
    abilities: tuple = ()         # triggers / statics (dicts)
    play: dict = field(default=None, hash=False, compare=False)    # tactics
    react: dict = field(default=None, hash=False, compare=False)   # reactions
    costs: tuple = field(default=(), hash=False, compare=False)    # extra costs on any card type (R-002 #1)
    text: str = ""
    test: bool = False

    def has(self, kw):
        return kw in self.keywords

    def kw(self, name, default=0):
        return self.kw_params.get(name, default)


@dataclass(frozen=True)
class LeaderCard:
    id: str
    name: str
    colors: tuple
    base: tuple = ()
    awakened: tuple = ()

    def side(self, awakened):
        return self.awakened if awakened else self.base


def _tuple(x):
    return tuple(x or ())


def load(path=None):
    path = path or os.path.join(DATA_DIR, "cards_v0.json")
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    cards = {}
    for c in raw["cards"]:
        cards[c["id"]] = Card(
            id=c["id"], name=c["name"], type=c["type"], cost=c["cost"],
            colors=_tuple(c.get("colors")), power=c.get("power", 0),
            keywords=frozenset(c.get("keywords", [])), kw_params=c.get("kw_params", {}),
            abilities=_tuple(c.get("abilities")), play=c.get("play"), react=c.get("react"),
            costs=_tuple(c.get("costs")),
            text=c.get("text", ""), test=c.get("test", False))
    leaders = {}
    for l in raw["leaders"]:
        leaders[l["id"]] = LeaderCard(id=l["id"], name=l["name"], colors=_tuple(l["colors"]),
                                      base=_tuple(l.get("base")), awakened=_tuple(l.get("awakened")))
    return cards, leaders


CARDS, LEADERS = load()


def use_database(path):
    """Swap the active card database in place (e.g. a new set written by the swarm)."""
    c, l = load(path)
    CARDS.clear()
    CARDS.update(c)
    LEADERS.clear()
    LEADERS.update(l)


def check_deck(leader_id, deck):
    """Deck-building rules of regolamento §2.3. Returns a list of problems (empty = legal)."""
    problems = []
    if len(deck) != 40:
        problems.append(f"{len(deck)} carte invece di 40")
    lcol = set(LEADERS[leader_id].colors)
    counts = {}
    for cid in deck:
        counts[cid] = counts.get(cid, 0) + 1
        c = CARDS[cid]
        if c.colors and not (set(c.colors) & lcol):
            problems.append(f"{c.name}: colore fuori dal Leader")
    for cid, n in counts.items():
        if n > 3:
            problems.append(f"{CARDS[cid].name}: {n} copie")
    return problems
