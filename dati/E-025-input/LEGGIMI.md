# E-025_B0c02 — ciclo 02, gruppo (b): riferimento B0c02 e diagnostica di LDR-05

- **Preset:** V024 con P6 = [1,3], cioè G2 +1 gemma nei round 1 e 3 (opzione B di Vittorio, che Q-022 chiude). Il nome esatto del preset nel motore lo decide il thread principale. Fino ad allora si usa il file `variante_V024_P13.json` (`{"base": "V024", "set": {"scintilla_extra_rounds": [1]}}`), predefinito in `lancia_e025.sh`. Il preset si cambia con `E025_VARIANTE=<nome>`.
- **Motore:** 934a469 (origin/claude/regolamento-v0.1). Tutti i file sono validati su una copia temporanea: 0 errori. Le prove di fumo con la semplice confermano che la variante dà `scintilla_extra_rounds [1]` con `scintilla_extra_round 3`.
- **Lancio:** `bash tcg/set/esperimenti/E-025_B0c02/lancia_e025.sh <braccio> <ia> <N> <seed> <protagonisti> [mix]`, dalla radice della repo. Seed: F 3000+k, S 2000+k, mix 20+o.

## Bracci
| Braccio | Cosa | IA e partite | Ore circa |
|---|---|---|---|
| `00_B0c02` | set finale attuale (`tcg/set/finale`, Thorn T1+V2 di Q-020), 6 rif più `mazzi_mix_M3.json` | F: 15 incroci × 100 più mix_M3 contro i 5 rif non-Thorn × 100 = 2.000. S: completa, 15 × 400 più mix × 400 = 8.000 | 8.0 F + 0.3 S |
| `D05b_c02` | Scudo neutralizzato solo in `rif_LDR05`: copie `D05B-*` senza la parola chiave `scudo` di BLU-001 ×2, BLU-007 ×3, BLU-008 ×3, BLU-010 ×2, BLU-012 ×2, NEU-013 ×3 (come D_05b di E-020). Protagonista LDR-05 | F: 60 per incrocio sui 5 incroci di LDR-05 = 300, appaiato con 00_B0c02 (stessi seed) | 1.2 |

**Comandi:**
- B0c02 con la forte: `E025_TRACCIA=LDR-05,BLU-001,BLU-007,BLU-008,BLU-010,BLU-012,BLU-015,BLU-021,BLU-023,BLU-025,NEU-013,ROS-001,ROS-005,ROS-007,ROS-015,ROS-018,ROS-020,ROS-021,ROS-023 bash lancia_e025.sh 00_B0c02 forte:30 100 3000 tutti mix`
- B0c02 con la semplice: lo stesso comando con `semplice 400 2000`.
- D05b_c02: `E025_TRACCIA=LDR-05,D05B-BLU-001,D05B-BLU-007,D05B-BLU-008,D05B-BLU-010,D05B-BLU-012,BLU-015,BLU-021,BLU-023,BLU-025,D05B-NEU-013,ROS-001,ROS-005,ROS-007,ROS-015,ROS-018,ROS-020,ROS-021,ROS-023 bash lancia_e025.sh D05b_c02 forte:30 60 3000 5`

Per il confronto appaiato di D05b, la cella di B0c02 si legge sulle sue prime 60 partite per incrocio.

## Traccia di rif_LDR05
- Gli ID sono quelli dei comandi sopra: le 18 carte di `rif_LDR05` più LDR-05; in D05b_c02 con gli ID `D05B-*`.
- Il report R-012 dà, per carta e per partita del mazzo: giocate, attivazioni, colpi a segno sul Leader e Unità sconfitte.
- **Il contatore "scontri vinti con Fa ≥8" non esiste nel motore 934a469.** Nel codice non c'è nessuna metrica sulla Forza d'attacco per scontro. Va chiesto al programmatore come contatore R-012, per esempio una colonna "colpi con Fa ≥8" per carta tracciata, prima di lanciare la forte di B0c02. Se non arriva, la traccia gira senza.

## Dopo E-024: rimisura delle leve vincenti su B0c02 (piano §1)
- **A:** la lista vincente fra A-FV e A-IF, ed eventualmente A-LB, costruita sul set finale. F, 100 per incrocio su LDR-06 = 500 (2 ore); con A-LB anche M6 × 60 (1.2 ore).
- **B:** la leva B vincente secondo la regola di combinazione: B-U o B-3g su LDR-01 = 500 (2 ore); B-R15 o la coppia su LDR-01 e LDR-05 = 900 (3.6 ore).
- **Combinato del voto** (A più B insieme): 15 × 100 = 1.500 (6 ore), se le leve sono due o più.
- I bracci di rimisura si generano quando E-024 ha dato il vincitore, con lo stesso formato e la stessa base (`00_B0c02`).

## Ore stimate (F a 0.4 ore ogni 100 partite)
| Voce | Ore |
|---|---|
| B0c02, forte più mix | 8.0 |
| B0c02, semplice | 0.3 |
| D05b_c02 | 1.2 |
| Rimisure | da 4 a 7 |
| Combinato | 6 |
| **Totale** | **da 13 a 22** |
