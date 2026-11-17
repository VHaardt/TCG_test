"""E-038 (ciclo 05, voto_lampo.md V2): combinazione finale. Ogni cartella H5-x+H6-y prende LDR-05 dal braccio H5-x e LDR-06
dal braccio H6-y di E-037 (carte.json); il resto del set e le liste rif_ di B0c06 sono identici. Solo dati.
Uso: python3 -B genera_e038.py  (legge ../E-037-input, che va generata prima con genera_e037.py)."""
import copy, json, os
D = os.path.dirname(os.path.abspath(__file__))
E37 = os.path.join(D, "..", "E-037-input")
ld = lambda b: json.load(open(os.path.join(E37, b, "carte.json")))
NOTA = "Ciclo 05, E-038 (voto_lampo.md V2): combinazione finale {}; Leader presi da E-037. Solo in questo esperimento."
COMBO = [(h5, h6) for h5 in ("H5-t", "H5-v", "H5-r") for h6 in ("H6-v", "H6-c")] + [("L5ref", "H6-v")]
for h5, h6 in COMBO:                # L5ref: LDR-05 come in B0c06 (preso dal braccio H6-y, che non lo tocca)
    if True:
        a, b = ld(h6 if h5 == "L5ref" else h5), ld(h6)
        s = copy.deepcopy(a)
        s["leaders"] = [copy.deepcopy(next(x for x in b["leaders"] if x["id"] == "LDR-06")) if l["id"] == "LDR-06" else l
                        for l in s["leaders"]]
        assert s["cards"] == b["cards"]
        s["note"] = s["note"].split(" Ciclo 05, E-037")[0] + " " + NOTA.format(f"{h5}+{h6}")
        c = f"{h5}+{h6}"
        os.makedirs(os.path.join(D, c), exist_ok=True)
        json.dump(s, open(os.path.join(D, c, "carte.json"), "w"), ensure_ascii=False, indent=1)
        m = json.load(open(os.path.join(E37, h6, "mazzi.json"))); m["nota"] = m["nota"].replace("E-037", "E-038")
        json.dump(m, open(os.path.join(D, c, "mazzi.json"), "w"), ensure_ascii=False, indent=1)
        L = {l["id"]: l for l in s["leaders"]}
        print(c, {k: L["LDR-05"].get(k) for k in ("life", "tempra", "tempra_fissa") if k in L["LDR-05"]},
              {k: L["LDR-06"].get(k) for k in ("life",) if k in L["LDR-06"]}, len(L["LDR-05"]["base"]), len(L["LDR-06"]["base"]))
