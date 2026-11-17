"""E-037 (ciclo 05, voto_lampo.md V1): genera carte.json e mazzi.json dei bracci delle leve dure dal set finale (B0c06).
Solo dati, nessuna regola nel codice. Uso: python3 -B genera_e037.py <tcg/set> (default /mnt/project-files/tcg/set)."""
import copy, json, os, sys
SET = sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/tcg/set"
D = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(SET, "finale/set_v02.json")))
M = json.load(open(os.path.join(SET, "finale/mazzi_v02.json")))
NOTA = "Ciclo 05, E-037 (voto_lampo.md V1). Testo o valore provvisorio: solo in questo braccio, non in set/finale."
R032 = (" Campi del Leader 'life'/'tempra' di R-032 (A toglie 1 dal R10 al valore del Leader); 'tempra_fissa': true = "
        "A non tocca la Tempra di questo Leader (voto lampo, Esito: H5-t), da aggiungere a R-032.")

def l6_base(plus_life, plus_stanca, txt):
    """Base di LDR-06 con costo 'perdi 1 Vita (floor 2) oppure Stanca una tua Unità Pronta': due abilità ⟳ (una per modo),
    perché il filtro sulle Cicatrici dipende dal modo (la Vita pagata aggiunge una Cicatrice, la Stanca no)."""
    pl = lambda n: {"scars": "own"} if n == 0 else {"n": {"scars": "own"}, "plus": n}
    return [{"activated": True, "cost": 0, "costs": [{"lose_life": 1, "floor": 2}],
             "target": {"side": "opp", "ready": True, "power_le": pl(plus_life)},
             "do": [{"op": "stanca", "target": "chosen"}], "text": txt,
             "_note": NOTA + " Modo 'perdi 1 Vita': Cicatrici contate prima di pagare."},
            {"activated": True, "cost": 0, "costs": [{"stanca_own": 1}],
             "target": {"side": "opp", "ready": True, "power_le": pl(plus_stanca)},
             "do": [{"op": "stanca", "target": "chosen"}], "text": "",
             "_note": NOTA + " Modo 'Stanca una tua Unità Pronta' della stessa ⟳: nessuna Cicatrice in più dal pagamento."}]

TXT_A = ("⟳, il tuo Leader perde 1 Vita *(rispetta il Saldo)* oppure Stanca una tua Unità Pronta: Stanca un'Unità avversaria "
         "Pronta con Forza attuale inferiore alle tue Cicatrici. Non puoi pagare in Vita se il tuo Leader ha 2 Vite o meno.")
TXT_C = TXT_A.replace("inferiore alle tue Cicatrici", "pari o inferiore alle tue Cicatrici")
L6A = l6_base(0, -1, TXT_A)          # L6-a (E-036): "inferiore" dopo il pagamento
L6C = l6_base(1, 0, TXT_C)           # H6-c: "pari o inferiore" dopo il pagamento
H6C_AW = [{"static": "power", "applies_to": {"side": "own", "keyword": "caccia", "kind": "unit"},
           "if": [{"attacking": True}, {"target_is_unit": True}], "value": 2,
           "text": "Le tue Unità con Caccia hanno +2 in questo scontro quando attaccano e il loro bersaglio è un'Unità.",
           "_note": NOTA}]
H5R_AW = [{"static": "power", "applies_to": {"side": "own", "keyword": "impeto", "kind": "unit"},
           "if": [{"attacking": True}, {"target_is_unit": True}], "value": 1,
           "text": "Le tue Unità con Impeto hanno +1 in questo scontro quando attaccano e il loro bersaglio è un'Unità.",
           "_note": NOTA}]

def carte(leader, **ch):
    s = copy.deepcopy(S)
    l = next(x for x in s["leaders"] if x["id"] == leader)
    for k, v in ch.items():
        l[k] = copy.deepcopy(v)
    l["_note"] = (l.get("_note", "") + " " + NOTA + (R032 if {"life", "tempra", "tempra_fissa"} & set(ch) else "")).strip()
    s["note"] += " " + NOTA
    return s

def mazzi():
    m = {k: v for k, v in M.items() if k != "mazzi"}
    m["mazzi"] = [d for d in M["mazzi"] if d["name"].startswith("rif_")]
    m["nota"] = "Liste rif_ di B0c06 (set/finale/mazzi_v02.json, senza le mix_); E-037."
    return m

BRACCI = {
    "H5-t": carte("LDR-05", tempra=3, tempra_fissa=True),   # voto lampo, Esito: Tempra 3 per tutta la partita, A non la abbassa
    "H5-v": carte("LDR-05", life=4),
    "H5-r": carte("LDR-05", base=[], awakened=H5R_AW),
    "H6-v": carte("LDR-06", base=L6A, life=6),
    "H6-c": carte("LDR-06", base=L6C, awakened=H6C_AW),
}
for b, c in BRACCI.items():
    os.makedirs(os.path.join(D, b), exist_ok=True)
    json.dump(c, open(os.path.join(D, b, "carte.json"), "w"), ensure_ascii=False, indent=1)
    json.dump(mazzi(), open(os.path.join(D, b, "mazzi.json"), "w"), ensure_ascii=False, indent=1)
    print(b, {k: v for k, v in next(x for x in c["leaders"] if x["id"] == ("LDR-05" if b[1] == "5" else "LDR-06")).items()
              if k in ("life", "tempra", "tempra_fissa")}, "base", len(next(x for x in c["leaders"] if x["id"] == ("LDR-05" if b[1] == "5" else "LDR-06"))["base"]))
