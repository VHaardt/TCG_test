# E-031 (Q-027, interattività): piano di misura

Autore: programmatore (swarm), 2026-11-02. Esito dei voti: `tcg/swarm/questioni/Q-027_interattivita/esito_passata2.md`. Testi: `round1/proposta_unificata.md`, con l'emendamento "Pronta" su I03. I07 è fuori.

## Quando parte
- E-031 parte **dopo E-030**, sul thread principale.
- Serve il motore con le primitive di R-026 (`tcg/set/richieste/R-026_primitive_Q027.md`). Oggi, su ab6f2dd, solo R1-2c passa `valida`. A, B e C si fermano sulle bozze: `NEW-I04.react.play_if`, `sacrifice`, `bounce`, `recover` e `on_rim`.
- Il confronto usa i riferimenti di E-030 sugli stessi semi (3400+k). Vale solo se il motore di R-026 lascia identici i replay V026/V027 di ab6f2dd. Se non è così, prima vanno rigiocate su quel motore le celle di riferimento:
  - 00_B0c05 sui protagonisti 2, 4 e 6: 12 incroci, ~8.7 h;
  - R5-2c sulle celle 2-5, 4-5 e 5-6: 3 incroci, ~2.2 h.

## Carte (`carte_q027.json`)
| ID | Stato | JSON |
|---|---|---|
| NEW-I01 | finale | `play.costs: [{stanca_own: 1}]`, bersaglio avversario Pronto con costo ≤3, `defeat` |
| NEW-I05 | finale | `react.do: att_mod −2`; `do_from_scars: att_mod −2 + draw 1` |
| NEW-I06 | finale | `react.do: att_mod −2`; `do_from_scars: att_mod −2 + defeat attacker (sel cost_le 2)`, dopo lo scontro come BLU-025 |
| NEW-I02 | bozza | costo `sacrifice: 1` |
| NEW-I03 | bozza | `stanca_own` + op `bounce` |
| NEW-I04 | bozza | costo 0, `react.play_if: [target_is_unit, no_own_gems]` |
| NEW-I08 | bozza | op `recover` dagli Scarti, campo di selettore `without_trigger: on_enter` |
| NEW-I09 | bozza | evento `on_rim` |
| NEW-I10 | bozza | evento `on_rim` |

**Verifiche fatte su ab6f2dd con V027:**
- `valida` accetta I01, I05 e I06.
- 320 partite di prova con l'IA semplice, Maera contro Arden e LDR-06 contro L5:
  - **I01:** giocata 46 volte, con 46 Stanca di una propria Unità per pagare il costo.
  - **I05 da Cicatrice:** 7 volte, 7 pescate.
  - **I06 da Cicatrice:** 10 volte. L'attaccante viene sconfitto nelle 9 volte in cui ha costo ≤2, e non viene sconfitto nell'unica volta in cui ha costo 5.
  - **Dalla mano:** l'IA semplice non ha mai giocato I05 né I06; il ramo `do` è la forma già usata da NEU-019.

## Bracci (2 copie per carta, liste B0c05 corrette dal critico)
| Braccio | Carte e liste | Celle | Partite | Ore |
|---|---|---|---|---|
| R1-2c | riferimento: `rott_LDR01_2c` al posto di rif_LDR01, nessuna carta nuova | 1-2, 1-4, 1-6 | 600 | ~2.2 |
| A | I04 e I05 in Thorn e Maera; I06 solo in Maera | protagonisti 2, 4 (9 incroci) | 1.800 | ~6.5 |
| A-r5 / A-r1 | A con la rottura di L5 / di L1 | 2-5, 4-5 / 1-2, 1-4 | 400 + 400 | ~2.9 |
| B | I01 e I02 in LDR-06 e Maera; I03 solo in Maera | protagonisti 2, 6 (9 incroci) | 1.800 | ~6.5 |
| B-r5 / B-r1 | B con la rottura di L5 / di L1 | 2-5, 5-6 / 1-2, 1-6 | 400 + 400 | ~2.9 |
| C | I08 e I09 in Maera; I08 e I10 in LDR-06 | protagonisti 2, 6 (9 incroci) | 1.800 | ~6.5 |
| C-r5 / C-r1 | C con la rottura di L5 / di L1 | 2-5, 5-6 / 1-2, 1-6 | 400 + 400 | ~2.9 |

**Totale:** 8.400 partite, **circa 30.3 h** su 4 core (forte:30, circa 13 s a partita). Le celle di rottura aggiungono circa 2.9 h a braccio, in linea con le "+2–4 ore" dell'esito.

**Riferimenti:**
- per A, B e C: `E-030_q026/00_B0c05/F_s3400`;
- per le celle r5: `E-030_q026/R5-2c/F_s3400`;
- per le celle r1: `E-031_q027/R1-2c/F_s3400`.

## Scambi (escono carte dello stesso tipo o con lo stesso compito, a costo vicino)
| Braccio | Lista | Escono | Entrano | Costo medio (B0c05 → braccio) |
|---|---|---|---|---|
| A | Thorn | BLU-023 ×2; VER-024, VER-025 | I04 ×2; I05 ×2 | 2.50 → 2.42 |
| A | Maera | BLU-023 ×2; BLU-009, NER-023; NER-003 ×2 | I04 ×2; I05 ×2; I06 ×2 | 2.58 → 2.52 |
| B | LDR-06 | NER-011 ×2; VER-013 ×2 | I01 ×2; I02 ×2 | 2.70 → 2.75 |
| B | Maera | NEU-003, NER-021; NEU-002 ×2; BLU-017 ×2 | I01 ×2; I02 ×2; I03 ×2 | 2.58 → 2.48 |
| C | Maera | NER-014 ×2; BLU-016 ×2 | I09 ×2; I08 ×2 | 2.58 → 2.52 |
| C | LDR-06 | NER-001, NER-013; VER-010, VER-008 | I08 ×2; I10 ×2 | 2.70 → 2.70 |

- **A:** le Reazioni restano tante quante prima (17 in Maera, 5 in Thorn). Cambia solo quale Reazione si gioca. I04 costa 0, per questo il costo medio scende.
- **B:** escono Stanca, Reliquie e una rimozione su Ruotata; entrano rimozioni su Pronta, sacrificio e rimbalzo. Le Unità restano 17 in Maera e 27 in LDR-06, perché I01 e I03 Stancano una propria Unità.
- **C:** in Maera gli Scudo scendono da 11 a 9 (NER-014).
- Il dettaglio carta per carta, con il perché, è nel `LEGGIMI.md` di ogni braccio.

**Colori:**
- In Maera il Nero sale nei bracci B e C (K 12 e 11 su 37 e 34). In A il Nero scende a 8 su 30 (27%), sotto il 35% come già in B0c05.
- Thorn passa da B 14 / G 22 a B 12 / G 19, perché entrano carte neutrali.
- LDR-06 in B passa a G 15 / K 20.

## File
- `genera_e031.py`: rigenera tutti i bracci. Rilanciarlo se cambiano `carte_q027.json` (bozze rese finali) o le liste B0c05.
- `lancia_e031.sh <braccio> <ia> <N> <seed_base> <celle>`. Celle: `tutti`, `p:2,4` oppure `2-5,4-5`.
- `esegui_e031.sh`: corsa sequenziale; prima di ogni braccio esegue `valida`.
