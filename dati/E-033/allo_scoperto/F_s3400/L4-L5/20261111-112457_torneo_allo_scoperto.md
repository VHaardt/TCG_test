# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 1050s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 38.9% [37.0–40.7] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [11.0–12.0] (media 11.57) | 8–11 | ✅ |
| Partite al round 13+ | 34.0% [25.5–43.7] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=26) | 23.1% [11.0–42.1] | 20–35% | ✅ |
| Attacchi con opposizione | 34.7% [32.9–36.5] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 66.7% [64.7–68.6] (con ≥3: 27.5% [25.7–29.4]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 35.4% [33.7–37.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 11.2% [7.9–15.6] (n=260) / 94.5% [88.5–97.5] (n=109) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.8% [9.0–13.0] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 33.3% [9.7–70.0] (n=6), LDR-04 Risvegliato 71.7% [58.4–82.0] (n=53), LDR-05 Base 60.9% [40.8–77.8] (n=23), LDR-05 Risvegliato 78.0% [64.8–87.2] (n=50) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 40.5% [30.1–51.9] (n=74) | | |
| Attacchi per partita | 26.8 | | |
| Pugno attaccante vuoto / pieno | 49.5% [47.5–51.5] / 12.1% [10.9–13.5] (gemme medie 0.83) | non >90% | |
| Pugno difensore vuoto / pieno | 61.6% [58.8–64.3] / 22.5% [20.2–24.9] (gemme medie 0.22) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 869, 1: 885, 2: 564, 3: 239, 4: 87, 5: 33, 6: 6} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 86, 'crepuscolo': 14} | | |
| G1 vince fra le partite finite al Crepuscolo | 78.6% [52.4–92.4] | | |
| G1 vince fra le partite arrivate al round 15 | 70.6% [46.9–86.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 17.6% [6.2–41.0] / 33.3% [6.1–79.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 66.7% [20.8–93.9]; 5.9% [1.0–27.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-1': 5, '2-2': 3, '3-1': 2, '2-0': 2, '1-0': 2, '4-4': 1, '1-1': 1, '1-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=4) | 23.5% [9.6–47.3] / 50.0% [15.0–85.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 3, 16: 1}; 50.0% [15.0–85.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 50.0% [15.0–85.0] / 50.0% [15.0–85.0]; 1.75 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–49.0] / 100.0% [51.0–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 100.0% [34.2–100.0]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 11.8% [3.3–34.3]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:pronto': 2, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=4) | 0.0% [0.0–43.4] / 0.0% [0.0–49.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 70.6% [46.9–86.7] (5.9% [1.0–27.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 3, 'rif_LDR04_stanca_e_smonta': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR05_scudi_armati 71% (n=17) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 30.0% [21.9–39.6], rif_LDR05_scudi_armati 70.0% [60.4–78.1]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.342 / 0.076 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.075 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.06 (0.00), rif_LDR05_scudi_armati 0.09 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 30.4% [28.7–32.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.37 (47 / 90); 61.8% [60.0–63.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 49.9% [48.6–51.3]; rif_LDR04_stanca_e_smonta 44.4%, rif_LDR05_scudi_armati 54.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.273 (178) / 0.329 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 14.0 (40%, 30 vittorie), LDR-05 R: 18.0 (49%, 70 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 6.68, LDR-05 4.36, BLU-015 1.05, VER-008 0.84, VER-014 0.79, ROS-018 0.78, NEU-013 0.68, VER-001 0.62, BLU-001 0.55, ROS-019 0.54, ROS-020 0.50, BLU-008 0.50 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.93, rif_LDR05_scudi_armati 0.06 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.30, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 25% (n=12), rif_LDR05_scudi_armati 21% (n=14) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.1% [10.9–13.5] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | BLU-010 100%, ponte 100%, NEU-009 100%, collante 100%, BLU-008 70%, NEU-013 70%, BLU-021 70%, ROS-020 70%, caccia 30%, NEU-003 30%, NEU-011 30%, VER-014 30%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 30.0 [22–40] (100) |
| rif_LDR05_scudi_armati | 70.0 [60–78] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.61 | 2.76 | 6.68 / 0.00 | 0.00 | 0.69 | 4.3 (100) | 10 | B 40%, G 60% | 2.40 | 0.50 |
| rif_LDR05_scudi_armati | 4.02 | 0.00 | 4.36 / 0.00 | 0.00 | 1.06 | 4.8 (99) | 12 | B 48%, R 52% | 1.89 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.69/0.12/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.28/0.45/0.19 | 0.33/0.00/0.13/0.06 | 0.75/1.15/0.43/0.35 | 0.00/0.00/0.00/0.00 | 0.00/0.68/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.62/0.07/0.39 | 0.70/0.00/0.00/0.00 | 0.65/0.00/0.10/0.06 | 0.00/0.00/0.00/0.00 | 0.39/0.32/0.21/0.22 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/6.68/1.84/0.71 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.25/0.40/0.01/0.15 | 0.00/0.00/0.00/0.00 | 0.37/0.25/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.00/0.09/0.08 | 0.29/0.00/0.02/0.01 | 0.25/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.84/0.03/0.31 | 0.42/0.03/0.00/0.01 | 0.45/0.00/0.12/0.08 | 0.00/0.26/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/4.36/1.85/0.48 | 0.64/0.40/0.17/0.07 | 0.62/0.00/0.22/0.08 | 0.72/0.50/0.30/0.15 | 0.57/0.28/0.28/0.23 | 0.66/0.00/0.25/0.19 | 0.81/0.96/0.32/0.42 | 0.00/0.26/0.00/0.00 | 0.00/0.31/0.00/0.00 | 0.00/0.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.68/0.36/0.34 | 0.80/0.34/0.14/0.08 | 0.00/0.00/0.00/0.00 | 0.73/0.40/0.22/0.02 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.20/0.32/0.24 | 0.00/0.00/0.00/0.00 | 0.38/0.78/0.00/0.00 | 0.66/0.50/0.32/0.43 | 0.43/0.41/0.26/0.51 | 0.22/0.13/0.12/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.00/0.11/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.00/0.09/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.03/0.05 | 0.35/0.01/0.00/0.01 | 0.28/0.06/0.11/0.05 | 0.39/0.54/0.24/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.57 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.08 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.29 | 0.00 | 0.06 | 0.00 | 0.00 | 0.04 | 0.07 | 0.03 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.12 | 0.32 | 0.16 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.16 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 1.05 | 0.01 | 0.02 | 0.05 | 0.08 | 0.17 | 0.11 | 0.14 | 0.17 | 0.15 | 0.09 | 0.04 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.75 | 0.02 | 0.03 | 0.07 | 0.07 | 0.08 | 0.12 | 0.07 | 0.10 | 0.09 | 0.04 | 0.03 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 1 | 0 | 2 |
| 8 | 2 | 3 | 0 | 5 |
| 9 | 12 | 5 | 0 | 17 |
| 10 | 2 | 11 | 0 | 13 |
| 11 | 11 | 6 | 0 | 17 |
| 12 | 7 | 5 | 0 | 12 |
| 13 | 2 | 3 | 0 | 5 |
| 14 | 3 | 9 | 0 | 12 |
| 15 | 12 | 4 | 0 | 16 |
| 16 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 44.4% | 0.083 | 2.36 | 0.57 | 0.00 | 0.00 | 2.82 | 0.00 | 0.00 | 0.298 |
| rif_LDR05_scudi_armati | 100 | 54.5% | 0.069 | 0.06 | 0.00 | 0.00 | 0.00 | 4.07 | 0.00 | 0.00 | 0.392 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 217 | 0.889 | 0.802 | 0.765 | 0.516 | 1212 | 0.751 | 0.175 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 217 | 0.207 | 0.166 | 0.129 | 0.028 | 1212 | 0.151 | 0.046 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 251 | 0.865 | 0.857 | 0.857 | 0.307 | 1003 | 0.797 | 0.267 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 251 | 0.171 | 0.159 | 0.155 | 0.036 | 1003 | 0.144 | 0.041 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 14.0% | 2.44 | 1.44 | 13.5% | 0.0% | 23.7% | 26.5% | 7.1% | 0.00 | 21.9% | 44.4% | 0.07 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 14.0% | 2.44 | 1.44 | 25.9% | 0.0% | 20.3% | 28.7% | 15.9% | 0.00 | 12.2% | 54.5% | 0.08 | 0.00 |
| Totale | 200 | 14.0% | 2.44 | 1.44 | 16.8% | 0.0% | 22.0% | 27.6% | 11.0% | 0.00 | 16.6% | 49.9% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

