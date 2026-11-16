# Torneo v0.2 — /home/claude/e034_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e034_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2210s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 36.3% [35.1–37.6] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [11.0–12.0] (media 11.50) | 8–11 | ✅ |
| Partite al round 13+ | 38.0% [31.6–44.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.3–3.6] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=72) | 27.8% [18.8–39.0] | 20–35% | ✅ |
| Attacchi con opposizione | 30.2% [28.9–31.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 67.4% [66.0–68.7] (con ≥3: 25.7% [24.4–27.0]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.3% [36.1–38.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.1% [4.3–8.5] (n=512) / 79.0% [74.1–83.1] (n=314) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.3% [11.0–13.8] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 52.4% [32.4–71.7] (n=21), LDR-01 Risvegliato 74.1% [65.3–81.3] (n=112), LDR-04 Base 40.0% [16.8–68.7] (n=10), LDR-04 Risvegliato 66.2% [57.9–73.6] (n=136) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 41.3% [34.2–48.7] (n=172) | | |
| Attacchi per partita | 26.9 | | |
| Pugno attaccante vuoto / pieno | 45.6% [44.2–47.1] / 14.7% [13.7–15.7] (gemme medie 0.90) | non >90% | |
| Pugno difensore vuoto / pieno | 66.7% [64.8–68.5] / 17.1% [15.7–18.6] (gemme medie 0.21) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1673, 1: 1802, 2: 1217, 3: 418, 4: 207, 5: 56, 6: 9} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 181, 'crepuscolo': 19} | | |
| G1 vince fra le partite finite al Crepuscolo | 26.3% [11.8–48.8] | | |
| G1 vince fra le partite arrivate al round 15 | 23.1% [11.0–42.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 38.5% [22.4–57.5] / 70.0% [39.7–89.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 0.0% [0.0–27.8]; 7.7% [2.1–24.1] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-0': 4, '1-1': 3, '0-1': 3, '3-2': 3, '0-3': 2, '2-2': 2, '2-3': 2, '0-2': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=11) | 42.3% [25.5–61.1] / 63.6% [35.4–84.8] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 10, 16: 1}; 90.9% [62.3–98.4] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 45.5% [21.3–72.0] / 9.1% [1.6–37.7]; 1.27 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–25.9] / 81.8% [52.3–94.9] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=7) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–35.4] / 25.0% [4.6–69.9]; 0.0% [0.0–35.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.5% [1.7–7.0] / 26.9% [13.7–46.1]; 100.0% [64.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 2, 'perd:rim': 1, 'vinc:atk': 7} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=13) / turno di G2 (n=12) | 0.0% [0.0–22.8] / 0.0% [0.0–24.3] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=13) | 0.0% [0.0–22.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 34.6% [19.4–53.8] (15.4% [6.1–33.5]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 7, 'rif_LDR01_puntata_e_preda': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR04_stanca_e_smonta 23% (n=26) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 62.0% [55.1–68.4], rif_LDR04_stanca_e_smonta 38.0% [31.6–44.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.467 / 0.071 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.071 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.10 (0.00), rif_LDR04_stanca_e_smonta 0.16 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 30.6% [29.3–31.8] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.23 (209 / 437); 61.7% [60.4–63.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.7% [49.7–51.7]; rif_LDR01_puntata_e_preda 52.5%, rif_LDR04_stanca_e_smonta 49.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.312 (405) / 0.310 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 124 vittorie), LDR-04 B: 12.0 (36%, 76 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 6.72, LDR-01 2.12, ROS-016 1.45, ROS-018 1.17, BLU-015 1.07, VER-014 0.78, VER-008 0.71, VER-001 0.71, NEW-I04 0.69, BLU-001 0.68, VER-011 0.62, ROS-021 0.54 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.65, rif_LDR04_stanca_e_smonta 3.02 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR04_stanca_e_smonta 0.30 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 38% (n=29), rif_LDR04_stanca_e_smonta 21% (n=43) | 20–35% |
| M13 | Pugno d'attacco pieno | 14.7% [13.7–15.7] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, caccia 100%, VER-008 100%, VER-001 100%, VER-011 62%, ROS-016 62%, VER-014 38%, collante 38%, VER-023 38%, NEU-009 38%, BLU-010 38%; oltre il 60%: ROS-016, VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 62.0 [55–68] (200) |
| rif_LDR04_stanca_e_smonta | 38.0 [32–45] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.91 | 0.00 | 2.12 / 0.00 | 0.00 | 0.00 | 4.3 (200) | 13 | G 39%, R 61% | 2.37 | 0.51 |
| rif_LDR04_stanca_e_smonta | 5.14 | 2.19 | 6.72 / 0.00 | 0.00 | 0.78 | 4.4 (195) | 9 | B 40%, G 60% | 1.83 | 0.77 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/2.12/2.18/0.52 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.41/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.88/0.51/0.26/0.09 | 0.81/0.12/0.60/0.42 | 0.85/0.40/0.21/0.04 | 0.00/0.37/0.00/0.00 | 0.79/0.00/0.28/0.14 | 0.64/0.20/0.23/0.15 | 0.82/1.45/0.04/0.59 | 0.72/1.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.54/0.33/0.35 | 0.22/0.07/0.14/0.21 | 0.00/0.00/0.00/0.00 | 0.73/0.56/0.04/0.37 | 0.71/0.00/0.00/0.00 | 0.77/0.00/0.19/0.06 | 0.65/0.62/0.24/0.13 | 0.66/0.61/0.43/0.31 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.00/0.10/0.04 | 0.41/0.04/0.05/0.04 | 0.41/0.14/0.14/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.07/0.01 | 0.36/0.36/0.00/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.68/0.20/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.24/0.41/0.18 | 0.34/0.00/0.14/0.07 | 0.69/1.07/0.46/0.33 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.85/0.10/0.71 | 0.71/0.00/0.00/0.00 | 0.64/0.00/0.16/0.09 | 0.00/0.00/0.00/0.00 | 0.34/0.25/0.20/0.22 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/6.72/1.95/0.59 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.21/0.39/0.04/0.20 | 0.00/0.00/0.00/0.00 | 0.33/0.23/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.10/0.28/0.08 | 0.27/0.00/0.02/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.61/1.06/0.01/0.55 | 0.38/0.08/0.03/0.04 | 0.34/0.00/0.20/0.07 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.69/0.00/0.00 | 0.00/0.09/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.39 | 0.16 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.20 | 0.01 | 0.00 | 0.01 | 0.16 | 0.17 | 0.00 | 0.00 | 0.34 | 0.09 | 0.00 | 0.03 | 0.00 | 0.01 | 0.08 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.03 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.55 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.03 | 0.01 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.01 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.81 | 0.01 | 0.04 | 0.05 | 0.10 | 0.08 | 0.15 | 0.10 | 0.11 | 0.10 | 0.04 | 0.02 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 1.14 | 0.01 | 0.05 | 0.08 | 0.12 | 0.11 | 0.17 | 0.24 | 0.17 | 0.06 | 0.06 | 0.04 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 1 | 0 | 1 |
| 7 | 1 | 3 | 0 | 4 |
| 8 | 9 | 6 | 0 | 15 |
| 9 | 12 | 16 | 0 | 28 |
| 10 | 7 | 17 | 0 | 24 |
| 11 | 20 | 14 | 0 | 34 |
| 12 | 9 | 9 | 0 | 18 |
| 13 | 16 | 12 | 0 | 28 |
| 14 | 8 | 14 | 0 | 22 |
| 15 | 4 | 20 | 0 | 24 |
| 16 | 2 | 0 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 52.5% | 0.067 | 0.00 | 0.65 | 0.00 | 0.00 | 3.70 | 0.00 | 0.00 | 0.353 |
| rif_LDR04_stanca_e_smonta | 200 | 49.1% | 0.076 | 1.99 | 1.03 | 0.00 | 0.00 | 3.38 | 0.00 | 0.00 | 0.440 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 564 | 0.881 | 0.817 | 0.738 | 0.291 | 2165 | 0.785 | 0.207 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 564 | 0.218 | 0.200 | 0.174 | 0.034 | 2165 | 0.161 | 0.053 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 282 | 0.816 | 0.730 | 0.677 | 0.142 | 2371 | 0.788 | 0.370 | 0.163 | 0.054 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 282 | 0.213 | 0.191 | 0.138 | 0.078 | 2371 | 0.168 | 0.073 | 0.028 | 0.004 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 9.5% | 2.12 | 1.70 | 38.5% | 0.0% | 18.2% | 24.2% | 4.1% | 0.00 | 13.0% | 52.5% | 0.07 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 9.5% | 2.12 | 1.70 | 23.1% | 0.0% | 21.2% | 28.7% | 11.8% | 0.00 | 15.8% | 49.1% | 0.01 | 0.00 |
| Totale | 400 | 9.5% | 2.12 | 1.70 | 29.5% | 0.0% | 19.7% | 26.4% | 8.8% | 0.00 | 14.4% | 50.7% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.249 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.55 |
| rif_LDR04_stanca_e_smonta | 200 | 0.356 | 0.161 | 0.0% | 0.0% | 0.99 | 0.21 | 0.33 | 0.00 | 0.00 | 0.00 | 4.50 |

