"""E-031 (Q-027, interattività: questioni/Q-027_interattivita/esito_passata2.md). Solo dati, nessuna regola nel codice.
Carte: B0c03 (E-025_B0c02/A-FV_c02/carte.json) + carte_q027.json (cards: finali; bozze: da validare con le primitive di R-026).
Liste: B0c05 corrette dal critico (questioni/Q-026_feedback_playtest/liste_B0c05/mazzi.json); rotture rott_LDR05_2c e
rott_LDR01_2c dal blocco JSON di liste_B0c05/verifica_critico.md. Preset V027.
Bracci: A, B, C (celle dei protagonisti), A-r5/A-r1, B-r5/B-r1, C-r5/C-r1 (celle sulle liste di rottura), R1-2c (riferimento delle celle r1).
  python3 -B genera_e031.py
"""
import copy, json, os, re
from collections import Counter
EXP = "/mnt/project-files/tcg/set/esperimenti"
Q26 = "/mnt/project-files/tcg/swarm/questioni/Q-026_feedback_playtest/liste_B0c05"
OUT = os.path.dirname(os.path.abspath(__file__))
SET = json.load(open(f"{EXP}/E-025_B0c02/A-FV_c02/carte.json", encoding="utf-8"))
MAZ = json.load(open(f"{Q26}/mazzi.json", encoding="utf-8"))
NEW = json.load(open(f"{OUT}/carte_q027.json", encoding="utf-8"))
ROTT = {d["name"]: d for d in json.loads(re.search(r"```json\n(.*?)```", open(f"{Q26}/verifica_critico.md", encoding="utf-8").read(), re.S)
                                         .group(1))["mazzi"]}
NUOVE = {c["id"]: c for c in NEW["cards"] + NEW["bozze"]}
L1, L2, L4, L5, L6 = ("rif_LDR01_puntata_e_preda", "rif_LDR02_muro_di_parata", "rif_LDR04_stanca_e_smonta",
                      "rif_LDR05_scudi_armati", "rif_LDR06_ferite_e_caccia")
C0 = {c["id"]: c for c in SET["cards"]} | NUOVE

# braccio: (carte nuove, scambi [(lista, esce, entra, perché)], protagonisti, voto)
SCAMBI = {
    "A": (["NEW-I04", "NEW-I05", "NEW-I06"], [
        (L4, ["BLU-023", "BLU-023"], ["NEW-I04", "NEW-I04"], "Reazione 'il bersaglio ha +X' per Reazione 'il bersaglio ha +2' (costo 1 → 0)"),
        (L4, ["VER-024", "VER-025"], ["NEW-I05", "NEW-I05"], "Reazioni 'l'attaccante ha −X' (−3 da 1, −5 e pesca da 2) per −2 e pesca da Cicatrice (costo 1)"),
        (L2, ["BLU-023", "BLU-023"], ["NEW-I04", "NEW-I04"], "come in Thorn: +4 al bersaglio da 1 → +2 alla propria Unità da 0"),
        (L2, ["BLU-009", "NER-023"], ["NEW-I05", "NEW-I05"], "le due 'l'attaccante ha −3' semplici da 1 (gemelle G2) per la −2 da 1 con pesca da Cicatrice"),
        (L2, ["NER-003", "NER-003"], ["NEW-I06", "NEW-I06"], "Reazione nera da 1 con bonus da Cicatrice per Reazione nera da 1 con bonus da Cicatrice"),
    ], "2,4", "A, Reazioni (8/8): I04 e I05 in Thorn e Maera, I06 solo in Maera"),
    "B": (["NEW-I01", "NEW-I02", "NEW-I03"], [
        (L6, ["NER-011", "NER-011"], ["NEW-I01", "NEW-I01"], "Tattica nera che toglie un'Unità Pronta dallo scontro (Stanca, costo 2) per Tattica nera che la sconfigge (costo 3)"),
        (L6, ["VER-013", "VER-013"], ["NEW-I02", "NEW-I02"], "Tattica da 2 di Stanca per Tattica da 2 di rimozione: le rimozioni crescono, la curva no"),
        (L2, ["NEU-003", "NER-021"], ["NEW-I01", "NEW-I01"], "rimozione da 3 su Ruotata e Reliquia nera da 5 per la rimozione nera da 3 su Pronta"),
        (L2, ["NEU-002", "NEU-002"], ["NEW-I02", "NEW-I02"], "Reliquia da 2 (massimo di Guardia) per Tattica da 2: le Unità (17) restano tutte"),
        (L2, ["BLU-017", "BLU-017"], ["NEW-I03", "NEW-I03"], "Tattica blu di risposta da 4 per la Tattica blu di risposta da 3 (rimbalzo)"),
    ], "2,6", "B, rimozioni e sacrificio (8/8): I01 e I02 in LDR-06 e Maera, I03 solo in Maera"),
    "C": (["NEW-I08", "NEW-I09", "NEW-I10"], [
        (L2, ["NER-014", "NER-014"], ["NEW-I09", "NEW-I09"], "Unità nera da 3 per Unità nera da 3 (F3 Scudo → F2 con Stanca al Rimarginare; gli Scudo della lista scendono da 11 a 9)"),
        (L2, ["BLU-016", "BLU-016"], ["NEW-I08", "NEW-I08"], "Unità da 4 che fa carte (⟳ pesca 1) per Unità da 3 che fa carte (recupero)"),
        (L6, ["NER-001", "NER-013"], ["NEW-I08", "NEW-I08"], "due Unità nere da 3 a Furia per l'Unità nera da 3 con recupero"),
        (L6, ["VER-010", "VER-008"], ["NEW-I10", "NEW-I10"], "le due Unità verdi da 2 a F1 più deboli per l'Unità verde da 2 a F2"),
    ], "2,6", "C, cimitero e Rimarginare (8/8, senza I07): I08 e I09 in Maera, I08 e I10 in LDR-06"),
}
CELLE = {"A": ("2-5,4-5", "1-2,1-4"), "B": ("2-5,5-6", "1-2,1-6"), "C": ("2-5,5-6", "1-2,1-6")}
ORE = 13 / 3600


def deck(m, name):
    return next(d for d in m["mazzi"] if d["name"] == name)


def ncelle(spec):
    if spec.startswith("p:"):
        p = set(spec[2:].split(","))
        return sum(1 for i in range(1, 7) for j in range(i + 1, 7) if str(i) in p or str(j) in p)
    return len(spec.split(","))


def stats(d, cards):
    cnt = Counter(d["cards"])
    col = Counter(x for c, k in cnt.items() for x in cards[c]["colors"] for _ in range(k))
    cm = sum(cards[c]["cost"] * k for c, k in cnt.items()) / len(d["cards"])
    return (f"{len(d['cards'])} carte, {sum(k for c, k in cnt.items() if cards[c]['type'] == 'unit')} Unità, "
            f"{sum(k for c, k in cnt.items() if cards[c]['type'] == 'reaction')} Reazioni, "
            f"{sum(k for c, k in cnt.items() if 'scudo' in cards[c].get('keywords', []))} Scudo, costo medio {cm:.2f}, colori "
            + " ".join(f"{x} {v}" for x, v in sorted(col.items())) + f", massimo copie {max(cnt.values())}")


def scrivi(name, nuove, scambi, rott, celle, rif, voto):
    s, m = copy.deepcopy(SET), copy.deepcopy(MAZ)
    for cid in nuove:
        c = copy.deepcopy(NUOVE[cid])
        s["cards"].append(c)
    righe = []
    for lista, out, inn, perche in scambi:
        d = deck(m, lista)
        for c in out:
            d["cards"].remove(c)
        d["cards"] += inn
        d["note"] = d.get("note", "") + f" E-031 {name}: −{', −'.join(out)}; +{', +'.join(inn)}."
        righe.append((lista, out, inn, perche))
    for slot, rname in rott:
        d = deck(m, slot)
        d["cards"] = list(ROTT[rname]["cards"])
        d["note"] = f"E-031 {name}: carte di {rname} (critico, liste_B0c05/verifica_critico.md); nome della rif_ lasciato per il lanciatore."
    s["version"] = m["set"] = f"set_v02+E-031_{name}"
    s["note"] = SET["note"] + f" E-031 {name}: carte di B0c03 più le carte di Q-027 del braccio (carte_q027.json)."
    m["autore"], m["data"] = "programmatore (swarm)", "2026-11-02"
    m["nota"] = MAZ["nota"] + f" E-031 {name}: liste B0c05 (corrette dal critico), modificate come in LEGGIMI.md."
    p = os.path.join(OUT, name)
    os.makedirs(p, exist_ok=True)
    json.dump(s, open(f"{p}/carte.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(m, open(f"{p}/mazzi.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tr = ",".join(dict.fromkeys(["LDR-01", "LDR-02", "LDR-04", "LDR-05", "LDR-06"] + nuove
                                + sorted({c for _, out, _, _ in righe for c in out}) + ["NER-003", "NER-025", "BLU-025", "VER-025", "NEU-019"]))
    open(f"{p}/traccia.txt", "w", encoding="utf-8").write(tr + "\n")
    cards = {c["id"]: c for c in s["cards"]}
    bozze = [c for c in nuove if c in {b["id"] for b in NEW["bozze"]}]
    n = ncelle(celle)
    txt = [f"# E-031_q027 / {name}\n", f"- **Voto:** {voto}."]
    if nuove:
        txt.append("- **Carte nuove:** " + ", ".join(f"`{c}`" + (" (bozza: da validare quando c'è la primitiva di R-026)" if c in bozze else " (finale)")
                                                    for c in nuove) + ". Testi e JSON in `../carte_q027.json`.")
    if righe:
        txt.append("- **Scambi (2 copie per carta; la carta che esce ha lo stesso tipo o lo stesso compito e costo vicino, così la curva resta):**")
        txt += [f"  - `{l}`: −{', −'.join(o)} → +{', +'.join(i)}. {why}." for l, o, i, why in righe]
    if rott:
        txt.append("- **Liste di rottura:** " + "; ".join(f"`{slot}` sostituita da `{r}` (nome della rif_ lasciato per il lanciatore)" for slot, r in rott) + ".")
    txt.append("- **Liste toccate, dopo gli scambi:**")
    txt += [f"  - `{d['name']}`: {stats(d, cards)} (in B0c05: {stats(deck(MAZ, d['name']), C0).split(', ', 4)[4].split(', colori')[0]})." for d in m["mazzi"] if any(d["name"] == x[0] for x in righe) or any(d["name"] == x[0] for x in rott)]
    txt.append(f"- **Si misura:** IA forte:30, 200 partite per incrocio, celle `{celle}` ({n} incroci, {200 * n} partite, ~{200 * n * ORE:.1f} h su 4 core), "
               f"semi 3400+k; contro {rif}.")
    txt.append(f"- **Comando:** `E031_TRACCIA=$(cat traccia.txt) bash ../lancia_e031.sh {name} forte:30 200 3400 {celle}`.")
    open(f"{p}/LEGGIMI.md", "w", encoding="utf-8").write("\n".join(txt) + "\n")
    return n


TOT = {}
for b, (nuove, scambi, prot, voto) in SCAMBI.items():
    TOT[b] = scrivi(b, nuove, scambi, [], f"p:{prot}", "E-030_q026/00_B0c05 F_s3400 (stesse celle e semi)", voto)
    r5, r1 = CELLE[b]
    TOT[b + "-r5"] = scrivi(b + "-r5", nuove, scambi, [(L5, "rott_LDR05_2c")], r5, "E-030_q026/R5-2c F_s3400 (stesse celle e semi)",
                            voto + "; celle extra sulla rottura di L5")
    TOT[b + "-r1"] = scrivi(b + "-r1", nuove, scambi, [(L1, "rott_LDR01_2c")], r1, "E-031_q027/R1-2c F_s3400 (stesse celle e semi)",
                            voto + "; celle extra sulla rottura di L1")
TOT["R1-2c"] = scrivi("R1-2c", [], [], [(L1, "rott_LDR01_2c")], "1-2,1-4,1-6", "— (riferimento delle celle r1: B0c05 senza carte nuove)",
                      "riferimento: rottura di L1 contro le liste B0c05 dei protagonisti 2, 4, 6")
for k, n in TOT.items():
    print(f"{k}: {n} incroci, {200 * n} partite, ~{200 * n * ORE:.1f} h")
print(f"totale: {sum(TOT.values()) * 200} partite, ~{sum(TOT.values()) * 200 * ORE:.1f} h")
