# E-037-input — vaglio delle leve dure su L5 e L6 (ciclo 05, voto_lampo.md V1)

Autore: programmatore (swarm), 2026-11-17. Voto: `tcg/swarm/cicli/ciclo-05/voto_lampo.md` (V1, 8/8 con emendamenti).

## Base e regole
La forma è quella di E-036:
- carte e liste `rif_` di B0c06 da `tcg/set/finale/`;
- regole `varianti/tempra_tardo.json` (V027 + A);
- forte:30, **100 partite** per incrocio, solo i 5 incroci del protagonista, semi 3700+k;
- record per partita in `partite.pkl`.

**Appaiamento con E-036:** i semi sono quelli di E-036, quindi le 100 partite di ogni cella sono appaiate seme per seme con le prime 100 della stessa cella di E-036 `00_B0c06A`. Per H6-v sono appaiate anche con quelle di `L6-a`.

Le cartelle si rigenerano con `python3 -B genera_e037.py [tcg/set]` (solo dati). Testi e valori nuovi stanno solo nel braccio, non in `set/finale`.

| Braccio | Leader | Cosa cambia | Nel JSON | `valida` (main e3b31b0) |
|---|---|---|---|---|
| **H5-t** | LDR-05 | Tempra 3 **per tutta la partita: A non la abbassa a 2** (Esito del voto) | `"tempra": 3, "tempra_fissa": true` | 1 errore: chiave sconosciuta `tempra` (R-032) |
| **H5-v** | LDR-05 | 4 Vite | `"life": 4` | 1 errore: chiave sconosciuta `life` (R-032) |
| **H5-r** | LDR-05 | Base senza testo; Risvegliato "Le tue Unità con Impeto hanno +1 in questo scontro quando attaccano e il loro bersaglio è un'Unità." | `"base": []`; Risvegliato come quello di LDR-06 oggi (`applies_to` impeto/unit, `if` attacking + target_is_unit) | **0 errori** |
| **H6-v** | LDR-06 | 6 Vite, sopra L6-a (la Base di E-036) | `"life": 6` e la Base di L6-a | 1 errore: chiave sconosciuta `life` (R-032) |
| **H6-c** | LDR-06 | Base "… con Forza attuale **pari o inferiore** alle tue Cicatrici. Non puoi pagare in Vita se il tuo Leader ha 2 Vite o meno." (costo: perdi 1 Vita oppure Stanca una tua Unità Pronta); Risvegliato "Le tue Unità con Caccia hanno +2 in questo scontro quando attaccano e il loro bersaglio è un'Unità." | due abilità ⟳, come in L6-a (vedi sotto); Risvegliato con `value` 2 | **0 errori** |

**Base di H6-c come dati.** Si usano le due abilità ⟳ della forma di L6-a in E-036, una per ogni modo di pagare:
- paga in Vita (floor 2): bersaglio con Forza ≤ Cicatrici + 1, perché le Cicatrici si contano prima di pagare e la Vita pagata ne aggiunge una;
- Stanca una tua Unità: bersaglio con Forza ≤ Cicatrici.

Con L6-a i due modi davano ≤ Cicatrici e ≤ Cicatrici − 1.

**R-032 (in preparazione nel thread principale).** Riguarda i campi facoltativi `life` e `tempra` del Leader nel set JSON, con A che toglie 1 dal R10 al valore del Leader. **H5-t ha bisogno in più di `tempra_fissa`** (o di una forma equivalente): è il valore del Leader che A non abbassa. Senza questa chiave, H5-t giocherebbe con Tempra 2 dal R10, contro il voto. Se R-032 sceglie un nome diverso, basta cambiarlo in `genera_e037.py` e rigenerare.

## Lancio
Dalla radice della repo:

    nohup bash dati/E-037-input/lancia_e037.sh tutti > /dev/null 2>&1 &

- Prima di ogni braccio il launcher lancia `valida` sul motore in uso. Se non passa, salta il braccio e lo scrive nel registro. Oggi partono H5-r e H6-c (circa 3.6 h); H5-t, H5-v e H6-v partono dopo R-032, rilanciando lo stesso comando.
- Le uscite vanno in `tcg/swarm/esperimenti/E-037_leve_dure/<braccio>/F_s3700/Li-Lj/`.

## Da leggere (regole d'uscita del voto)
- **Uscita:** L5 ≤ 58; L6 ≥ 42.
- **Guardie:** L1 ≤ 58, vittorie entro il R5 ≤ 1%, R9-5 di L6 ≤ 0.35, Vey ≥ 43.
- **Celle e contatori:**
  - cella L5-L6 per H6-v e H6-c;
  - round 13+ negli incroci di L6 per H6-v;
  - attivazioni del Leader e costi in Vita, letti come in E-036. Le attivazioni sono ancora sommate fra Base e Risvegliato finché non arriva R-031 n.3.
