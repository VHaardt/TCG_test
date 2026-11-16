"""E-036 (ciclo 05, esito_piano.md P2): genera carte.json, mazzi.json e traccia.txt di ogni braccio dal set finale (B0c06).
Solo dati, nessuna regola nel codice. Uso: python3 -B genera_e036.py <tcg/set> (default /mnt/project-files/tcg/set)."""
import copy, json, os, sys
SET = sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/tcg/set"
D = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(SET, "finale/set_v02.json")))
M = json.load(open(os.path.join(SET, "finale/mazzi_v02.json")))
R52 = next(m for m in json.load(open(os.path.join(SET, "esperimenti/E-030_q026/R5-2c/mazzi.json")))["mazzi"]
           if m["name"] == "rif_LDR05_scudi_armati")
RIF = [m for m in M["mazzi"] if m["name"].startswith("rif_")]
ROTT = dict(copy.deepcopy(R52), name="rott_LDR05_2c", tipo="rottura",
            note="Lista di rottura R5-2c del critico (E-030 R5-2c, ciclo 04), per le celle 1-5 e 2-5 di L5-b.")
NOTA = "Ciclo 05, E-036 (esito_piano.md P2). Carta o testo provvisorio: solo in questo braccio, non in set/finale."

L5C = [{"static": "power", "applies_to": {"side": "own", "attacker": True, "keyword": "scudo"},
        "if": [{"pugno_ge": 1}, {"first_attack_kw": "scudo"}], "value": 1,
        "text": "La prima delle tue Unità con Scudo che attacca in ogni turno ha +1 in questo scontro, se nell'impegno hai almeno 1 gemma.",
        "_note": NOTA + " La condizione first_attack_kw è la primitiva chiesta con R-031 (n.1)."}]
L6A_TXT = ("⟳, il tuo Leader perde 1 Vita *(rispetta il Saldo)* oppure Stanca una tua Unità Pronta: Stanca un'Unità avversaria "
           "Pronta con Forza attuale inferiore alle tue Cicatrici. Non puoi pagare in Vita se il tuo Leader ha 2 Vite o meno.")
L6A = [{"activated": True, "cost": 0, "costs": [{"lose_life": 1, "floor": 2}],
        "target": {"side": "opp", "ready": True, "power_le": {"scars": "own"}},
        "do": [{"op": "stanca", "target": "chosen"}], "text": L6A_TXT,
        "_note": NOTA + " Modo 'perdi 1 Vita' (floor 2): le Cicatrici si contano prima di pagare con ≤, come oggi."},
       {"activated": True, "cost": 0, "costs": [{"stanca_own": 1}],
        "target": {"side": "opp", "ready": True, "power_le": {"n": {"scars": "own"}, "plus": -1}},
        "do": [{"op": "stanca", "target": "chosen"}], "text": "",
        "_note": NOTA + " Modo 'Stanca una tua Unità Pronta' della stessa ⟳: il pagamento non aggiunge Cicatrici, quindi "
                 "'inferiore alle tue Cicatrici' è ≤ Cicatrici − 1. Due abilità con la stessa ⟳ del Leader = un costo 'any' "
                 "in cui il bersaglio dipende dal modo scelto."}]
P31 = {"id": "NEW-P31", "name": "NEW-P31", "type": "unit", "cost": 3, "colors": ["K", "G"], "rarity": "R", "power": 3,
       "keywords": ["caccia"],
       "abilities": [{"static": "power", "if": [{"attacking": True}, {"target_has": "scudo"}], "value": 2}],
       "text": "Caccia *(quando attacca, puoi scegliere come bersaglio un'Unità avversaria, anche Ruotata, invece del Leader; "
               "l'avversario può ancora opporsi con un'altra Unità, che diventa il bersaglio)*. Quando attacca, se il bersaglio ha Scudo, +2 in questo scontro.",
       "intent": "Ciclo 05 L6-d (ponti, r1_ponti.md leva 1): Caccia che rompe i muri Scudo per LDR-06.",
       "vanilla_delta": "vanilla 3/4, Caccia −1; +2 condizionato giustifica la Rara bicolore",
       "_note": NOTA + " La condizione target_has è la primitiva chiesta con R-031 (n.2)."}
P32 = {"id": "NEW-P32", "name": "NEW-P32", "type": "tactic", "cost": 3, "colors": ["K", "G"], "rarity": "R",
       "play": {"costs": [{"stanca_own": 1}], "target": {"side": "opp", "ready": True, "keyword": "scudo", "cost_le": 3},
                "do": [{"op": "defeat", "target": "chosen"}]},
       "text": "Costo aggiuntivo: Stanca *(ruota)* una tua Unità Pronta. Sconfiggi un'Unità avversaria Pronta con Scudo e costo ≤3.",
       "intent": "Ciclo 05 L6-d (ponti, r1_ponti.md leva 2): rimozione degli Scudo che apre un varco nella propria difesa.",
       "vanilla_delta": "Tattica 3 = rimozione ristretta (Scudo, Pronta, costo ≤3) più costo Stanca",
       "_note": NOTA}

def carte(leader=None, base=None, extra=()):
    s = copy.deepcopy(S)
    if leader:
        next(l for l in s["leaders"] if l["id"] == leader)["base"] = copy.deepcopy(base)
    s["cards"] += copy.deepcopy(list(extra))
    s["note"] += " " + NOTA
    return s

def swap(deck, out, inn):
    d = copy.deepcopy(next(m for m in RIF if m["name"] == deck))
    for o, n in zip(out, inn):
        d["cards"][d["cards"].index(o)] = n
    d["note"] += f" E-036: −{', −'.join(out)}; +{', +'.join(inn)}."
    return d

def mazzi(changes=(), rott=False):
    m = {k: v for k, v in M.items() if k != "mazzi"}
    ch = {d["name"]: d for d in changes}
    m["mazzi"] = [ch.get(d["name"], d) for d in RIF] + ([ROTT] if rott else [])
    m["nota"] = "Liste rif_ di B0c06 (set/finale/mazzi_v02.json, senza le mix_)" + (" più rott_LDR05_2c" if rott else "") + "; E-036."
    return m

L5B = swap("rif_LDR05_scudi_armati", ["BLU-004", "BLU-004", "BLU-012", "BLU-012"], ["ROS-004", "ROS-006", "ROS-014", "ROS-019"])
L6B = swap("rif_LDR06_ferite_e_caccia", ["VER-008", "VER-003"], ["VER-002", "VER-002"])
L6D = swap("rif_LDR06_ferite_e_caccia", ["VER-008", "VER-008", "NER-011", "NER-011"], ["NEW-P31", "NEW-P31", "NEW-P32", "NEW-P32"])
BRACCI = {
    "00_B0c06A": (carte(), mazzi(rott=True)),
    "L5-c": (carte("LDR-05", L5C), mazzi()),
    "L5-b": (carte(), mazzi([L5B], rott=True)),
    "L6-a": (carte("LDR-06", L6A), mazzi()),
    "L6-ab": (carte("LDR-06", L6A), mazzi([L6B])),
    "L6-ad": (carte("LDR-06", L6A, [P31, P32]), mazzi([L6D])),
}
tr = open(os.path.join(D, "..", "E-034-input", "traccia.txt")).read().strip().split(",") \
    if os.path.exists(os.path.join(D, "..", "E-034-input", "traccia.txt")) else []
tr += [x for x in ["ROS-020", "ROS-021", "VER-002", "VER-008", "VER-003", "NER-011", "BLU-004", "BLU-012",
                   "ROS-004", "ROS-006", "ROS-014", "ROS-019", "NEW-P31", "NEW-P32"] if x not in tr]
for b, (c, m) in BRACCI.items():
    os.makedirs(os.path.join(D, b), exist_ok=True)
    json.dump(c, open(os.path.join(D, b, "carte.json"), "w"), ensure_ascii=False, indent=1)
    json.dump(m, open(os.path.join(D, b, "mazzi.json"), "w"), ensure_ascii=False, indent=1)
    open(os.path.join(D, b, "traccia.txt"), "w").write(",".join(tr) + "\n")
    print(b, len(c["cards"]), "carte,", [d["name"] for d in m["mazzi"]][-1])
