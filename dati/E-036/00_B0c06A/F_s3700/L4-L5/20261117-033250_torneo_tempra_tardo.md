# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2589s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 39.3% [38.0–40.6] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [11.0–12.0] (media 11.70) | 8–11 | ✅ |
| Partite al round 13+ | 40.0% [33.5–46.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=48) | 27.1% [16.6–41.0] | 20–35% | ✅ |
| Attacchi con opposizione | 33.4% [32.1–34.6] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 67.6% [66.3–69.0] (con ≥3: 28.6% [27.3–29.9]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 35.6% [34.4–36.9] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 12.0% [9.3–15.4] (n=441) / 84.4% [79.4–88.3] (n=256) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.1% [9.8–12.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 36.8% [19.1–59.0] (n=19), LDR-04 Risvegliato 71.1% [62.1–78.6] (n=114), LDR-05 Base 55.9% [39.5–71.1] (n=34), LDR-05 Risvegliato 82.4% [73.8–88.5] (n=102) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 44.8% [37.2–52.7] (n=154) | | |
| Attacchi per partita | 27.4 | | |
| Pugno attaccante vuoto / pieno | 52.8% [51.4–54.2] / 11.5% [10.6–12.4] (gemme medie 0.78) | non >90% | |
| Pugno difensore vuoto / pieno | 69.4% [67.6–71.1] / 18.0% [16.6–19.5] (gemme medie 0.21) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1843, 1: 1885, 2: 1086, 3: 452, 4: 156, 5: 44, 6: 5} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'crepuscolo': 23, 'colpo_finale': 177} | | |
| G1 vince fra le partite finite al Crepuscolo | 82.6% [62.9–93.0] | | |
| G1 vince fra le partite arrivate al round 15 | 71.4% [52.9–84.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 32.1% [17.9–50.7] / 22.2% [6.3–54.7] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 66.7% [35.4–87.9]; 10.7% [3.7–27.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 6, '2-1': 5, '2-0': 4, '3-2': 3, '2-2': 3, '1-2': 1, '3-0': 1, '1-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=11) | 39.3% [23.6–57.6] / 18.2% [5.1–47.7] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 9, 17: 1, 16: 1}; 27.3% [9.7–56.6] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 72.7% [43.4–90.3] / 63.6% [35.4–84.8]; 2.36 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–25.9] / 90.9% [62.3–98.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 77.8% [45.3–93.7]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.0% [0.3–3.6] / 7.1% [2.0–22.6]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:pronto': 1, 'perd:rim': 1, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=5) | 0.0% [0.0–43.4] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 64.3% [45.8–79.3] (3.6% [0.6–17.7]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 11} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR05_scudi_armati 71% (n=28) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 33.0% [26.9–39.8], rif_LDR05_scudi_armati 67.0% [60.2–73.1]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.529 / 0.077 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.075 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.10 (0.00), rif_LDR05_scudi_armati 0.17 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 30.7% [29.5–32.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.56 (102 / 211); 62.4% [61.1–63.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.4% [50.5–52.3]; rif_LDR04_stanca_e_smonta 47.1%, rif_LDR05_scudi_armati 55.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.303 (353) / 0.320 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 12.0 (36%, 66 vittorie), LDR-05 R: 18.0 (49%, 134 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 6.35, LDR-05 3.87, BLU-015 1.03, VER-008 1.03, VER-014 0.79, ROS-018 0.64, VER-001 0.64, ROS-020 0.61, NEW-I04 0.56, VER-023 0.56, NEU-013 0.51, BLU-001 0.50 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.67, rif_LDR05_scudi_armati 0.14 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.36, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 12% (n=17), rif_LDR05_scudi_armati 35% (n=31) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.5% [10.6–12.4] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-009 100%, BLU-010 100%, ROS-020 67%, NEU-013 67%, BLU-021 67%, BLU-008 67%, VER-014 33%, caccia 33%, VER-008 33%, VER-023 33%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 33.0 [27–40] (200) |
| rif_LDR05_scudi_armati | 67.0 [60–73] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.67 | 2.75 | 6.35 / 0.00 | 0.00 | 0.68 | 4.6 (195) | 10 | B 39%, G 61% | 2.11 | 0.53 |
| rif_LDR05_scudi_armati | 4.16 | 0.00 | 3.87 / 0.00 | 0.00 | 0.89 | 4.9 (197) | 13 | B 47%, R 53% | 1.86 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.66/0.16/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.39/0.33/0.27 | 0.32/0.00/0.14/0.09 | 0.76/1.09/0.45/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.64/0.04/0.44 | 0.75/0.00/0.00/0.00 | 0.59/0.00/0.20/0.10 | 0.00/0.00/0.00/0.00 | 0.43/0.28/0.26/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/6.35/1.82/0.58 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.56/0.03/0.18 | 0.00/0.00/0.00/0.00 | 0.38/0.30/0.02/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.00/0.21/0.09 | 0.33/0.00/0.04/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/1.03/0.01/0.39 | 0.30/0.04/0.03/0.03 | 0.38/0.00/0.14/0.08 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.00/0.00 | 0.53/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.56/0.00/0.00 | 0.00/0.05/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.87/1.67/0.51 | 0.62/0.35/0.12/0.07 | 0.65/0.00/0.17/0.07 | 0.62/0.39/0.23/0.14 | 0.77/0.28/0.35/0.20 | 0.63/0.00/0.30/0.20 | 0.70/0.97/0.43/0.38 | 0.00/0.40/0.00/0.00 | 0.00/0.40/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.51/0.31/0.28 | 0.67/0.30/0.10/0.09 | 0.00/0.00/0.00/0.00 | 0.70/0.34/0.10/0.08 | 0.00/0.32/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.25/0.29/0.25 | 0.00/0.00/0.00/0.00 | 0.41/0.64/0.00/0.00 | 0.69/0.61/0.44/0.56 | 0.49/0.45/0.36/0.46 | 0.24/0.06/0.15/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.00/0.07/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.04/0.10/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.03/0.01 | 0.31/0.02/0.03/0.02 | 0.34/0.17/0.19/0.14 | 0.31/0.40/0.20/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.45 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.02 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.16 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.36 | 0.00 | 0.07 | 0.01 | 0.00 | 0.00 | 0.03 | 0.05 | 0.16 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | 0.27 | 0.32 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.80 | 0.00 | 0.01 | 0.04 | 0.05 | 0.14 | 0.15 | 0.15 | 0.10 | 0.06 | 0.04 | 0.03 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.70 | 0.01 | 0.00 | 0.06 | 0.07 | 0.14 | 0.11 | 0.10 | 0.07 | 0.07 | 0.04 | 0.02 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 3 | 0 | 4 |
| 8 | 2 | 4 | 0 | 6 |
| 9 | 12 | 9 | 0 | 21 |
| 10 | 22 | 19 | 0 | 41 |
| 11 | 22 | 10 | 0 | 32 |
| 12 | 8 | 8 | 0 | 16 |
| 13 | 9 | 23 | 0 | 32 |
| 14 | 8 | 12 | 0 | 20 |
| 15 | 17 | 8 | 0 | 25 |
| 16 | 2 | 0 | 0 | 2 |
| 17 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 47.1% | 0.058 | 1.94 | 0.73 | 0.00 | 0.00 | 2.88 | 0.00 | 0.00 | 0.469 |
| rif_LDR05_scudi_armati | 200 | 55.3% | 0.097 | 0.14 | 0.00 | 0.00 | 0.00 | 3.98 | 0.00 | 0.00 | 0.422 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 229 | 0.869 | 0.773 | 0.742 | 0.170 | 2611 | 0.825 | 0.411 | 0.149 | 0.041 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 229 | 0.197 | 0.135 | 0.092 | 0.052 | 2611 | 0.140 | 0.068 | 0.026 | 0.003 |
| rif_LDR05_scudi_armati | mano | 603 | 0.919 | 0.896 | 0.881 | 0.370 | 2028 | 0.849 | 0.266 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 603 | 0.191 | 0.184 | 0.176 | 0.055 | 2028 | 0.117 | 0.041 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 11.5% | 2.38 | 1.65 | 16.8% | 0.0% | 25.2% | 27.3% | 6.9% | 0.00 | 19.9% | 47.1% | 0.05 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 11.5% | 2.38 | 1.65 | 39.3% | 0.0% | 23.5% | 30.0% | 14.1% | 0.00 | 12.2% | 55.3% | 0.07 | 0.00 |
| Totale | 400 | 11.5% | 2.38 | 1.65 | 25.7% | 0.0% | 24.3% | 28.7% | 10.1% | 0.00 | 15.8% | 51.4% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.392 | 0.186 | 0.0% | 0.0% | 1.52 | 0.00 | 0.41 | 0.04 | 0.00 | 0.00 | 4.08 |
| rif_LDR05_scudi_armati | 200 | 0.271 | 0.123 | 0.0% | 0.0% | 0.90 | 0.32 | 0.67 | 1.12 | 0.00 | 0.00 | 5.66 |

