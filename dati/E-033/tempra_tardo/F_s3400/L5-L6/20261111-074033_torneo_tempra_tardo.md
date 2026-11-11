# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 837s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 36.5% [34.6–38.4] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.5] (media 11.04) | 8–11 | ✅ |
| Partite al round 13+ | 34.0% [25.5–43.7] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=43) | 20.9% [11.4–35.2] | 20–35% | ✅ |
| Attacchi con opposizione | 26.8% [25.1–28.6] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 58.3% [56.2–60.4] (con ≥3: 21.8% [20.1–23.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.3% [34.5–38.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 8.8% [5.5–13.8] (n=182) / 90.7% [84.9–94.4] (n=150) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.8% [12.7–17.3] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-05 Base 53.8% [29.1–76.8] (n=13), LDR-05 Risvegliato 78.6% [60.5–89.8] (n=28), LDR-06 Base 100.0% [43.8–100.0] (n=3), LDR-06 Risvegliato 70.4% [61.2–78.2] (n=108) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 41.6% [31.2–52.7] (n=77) | | |
| Attacchi per partita | 25.2 | | |
| Pugno attaccante vuoto / pieno | 56.1% [54.0–58.1] / 11.9% [10.6–13.3] (gemme medie 0.72) | non >90% | |
| Pugno difensore vuoto / pieno | 58.3% [55.5–61.1] / 23.6% [21.3–26.1] (gemme medie 0.25) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 838, 1: 866, 2: 579, 3: 167, 4: 51, 5: 16, 6: 6} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 91, 'crepuscolo': 9} | | |
| G1 vince fra le partite finite al Crepuscolo | 66.7% [35.4–87.9] | | |
| G1 vince fra le partite arrivate al round 15 | 58.3% [32.0–80.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 25.0% [8.9–53.2] / 33.3% [6.1–79.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 66.7% [20.8–93.9]; 0.0% [0.0–24.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 2, '3-1': 2, '2-2': 2, '2-0': 1, '1-2': 1, '0-2': 1, '4-2': 1, '2-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=3) | 25.0% [8.9–53.2] / 33.3% [6.1–79.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 3}; 33.3% [6.1–79.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 33.3% [6.1–79.2] / 33.3% [6.1–79.2]; 2.33 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–56.2] / 100.0% [43.8–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=1) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–79.3] / 50.0% [9.5–90.5]; 0.0% [0.0–79.3] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.0% [0.2–5.4] / 8.3% [1.5–35.4]; 100.0% [20.7–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'vinc:atk': 1} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=3) / turno di G2 (n=6) | 0.0% [0.0–56.2] / 0.0% [0.0–39.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=3) | 0.0% [0.0–56.2] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 50.0% [25.4–74.6] (8.3% [1.5–35.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR05_scudi_armati vs rif_LDR06_ferite_e_caccia 58% (n=12) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR05_scudi_armati 70.0% [60.4–78.1], rif_LDR06_ferite_e_caccia 30.0% [21.9–39.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.402 / 0.090 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.088 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR05_scudi_armati 0.20 (0.00), rif_LDR06_ferite_e_caccia 0.09 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 33.6% [31.8–35.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 4.30 (138 / 292); 60.2% [58.3–62.1] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 47.3% [45.8–48.8]; rif_LDR05_scudi_armati 53.7%, rif_LDR06_ferite_e_caccia 41.2% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.327 (167) / 0.322 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-05 R: 18.0 (49%, 70 vittorie), LDR-06 G: 17.0 (49%, 30 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.39, LDR-05 2.88, VER-020 2.30, NER-017 1.48, VER-008 0.91, NER-009 0.82, VER-001 0.72, NER-013 0.72, BLU-015 0.70, NER-015 0.68, NEU-001 0.66, BLU-023 0.57 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR05_scudi_armati 0.12, rif_LDR06_ferite_e_caccia 3.14 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.24 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR05_scudi_armati 33% (n=3), rif_LDR06_ferite_e_caccia 20% (n=40) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.9% [10.6–13.3] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.96; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-013 70%, BLU-010 70%, NEU-009 70%, BLU-008 70%, ROS-020 70%, BLU-021 70%, VER-023 30%, caccia 30%, NER-017 30%, NER-009 30%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR05_scudi_armati | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR05_scudi_armati | — | 70.0 [60–78] (100) |
| rif_LDR06_ferite_e_caccia | 30.0 [22–40] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 3.96 | 0.00 | 2.88 / 0.00 | 0.00 | 0.58 | 5.1 (100) | 12 | B 48%, R 52% | 2.30 | 0.00 |
| rif_LDR06_ferite_e_caccia | 3.74 | 0.00 | 3.39 / 0.08 | 0.00 | 0.15 | 5.0 (98) | 10 | G 56%, K 44% | 2.08 | 1.49 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.88/1.57/0.51 | 0.69/0.39/0.13/0.08 | 0.60/0.00/0.09/0.01 | 0.53/0.20/0.09/0.05 | 0.63/0.12/0.31/0.10 | 0.72/0.00/0.30/0.16 | 0.67/0.70/0.33/0.24 | 0.00/0.55/0.00/0.00 | 0.00/0.57/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.41/0.32/0.14 | 0.64/0.27/0.11/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.26/0.07/0.06 | 0.00/0.33/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.19/0.27/0.14 | 0.00/0.00/0.00/0.00 | 0.36/0.51/0.00/0.00 | 0.61/0.38/0.38/0.23 | 0.48/0.43/0.41/0.25 | 0.25/0.06/0.17/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.00/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.05/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.02/0.02 | 0.35/0.01/0.02/0.00 | 0.27/0.08/0.11/0.06 | 0.32/0.20/0.09/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.72/0.07/0.54 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.47/0.71/0.19 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.39/1.75/0.58 | 0.00/0.00/0.00/0.00 | 0.52/0.00/0.00/0.00 | 0.22/0.39/0.00/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.52/0.21/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.06/0.15/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.32/0.04/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.52/0.04/0.38 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.91/0.01/0.38 | 0.40/0.06/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.66/0.20/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.61/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 1.12 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.15 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.15 | 0.37 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.71 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 0.38 | 0.00 | 0.01 | 0.01 | 0.03 | 0.03 | 0.05 | 0.05 | 0.08 | 0.05 | 0.02 | 0.04 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.84 | 0.00 | 0.02 | 0.04 | 0.08 | 0.08 | 0.14 | 0.12 | 0.13 | 0.08 | 0.06 | 0.05 | 0.02 | 0.02 | 0.00 | 0.96 | 0.11 | 0.16 | 0.16 | 0.15 | 0.17 | 0.09 | 0.07 | 0.03 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 1 | 0 | 0 | 1 |
| 6 | 0 | 1 | 0 | 1 |
| 7 | 3 | 1 | 0 | 4 |
| 8 | 5 | 7 | 0 | 12 |
| 9 | 6 | 6 | 0 | 12 |
| 10 | 10 | 4 | 0 | 14 |
| 11 | 10 | 6 | 0 | 16 |
| 12 | 2 | 4 | 0 | 6 |
| 13 | 7 | 8 | 0 | 15 |
| 14 | 1 | 6 | 0 | 7 |
| 15 | 7 | 5 | 0 | 12 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 53.7% | 0.117 | 0.12 | 0.00 | 0.00 | 0.00 | 2.29 | 0.00 | 0.00 | 0.369 |
| rif_LDR06_ferite_e_caccia | 100 | 41.2% | 0.057 | 0.82 | 2.32 | 0.00 | 0.00 | 4.58 | 0.00 | 0.00 | 0.442 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | mano | 332 | 0.828 | 0.825 | 0.819 | 0.428 | 1054 | 0.746 | 0.207 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 332 | 0.157 | 0.151 | 0.145 | 0.060 | 1054 | 0.128 | 0.036 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 167 | 0.922 | 0.892 | 0.856 | 0.335 | 970 | 0.936 | 0.343 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 167 | 0.281 | 0.246 | 0.240 | 0.054 | 970 | 0.203 | 0.098 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 9.0% | 2.23 | 1.54 | 48.8% | 1.0% | 29.0% | 29.5% | 9.4% | 0.00 | 15.7% | 53.7% | 0.04 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 9.0% | 2.23 | 1.54 | 17.1% | 1.0% | 24.7% | 29.5% | 9.0% | 0.00 | 13.2% | 41.2% | 0.07 | 0.00 |
| Totale | 200 | 9.0% | 2.23 | 1.54 | 28.6% | 1.0% | 26.8% | 29.5% | 9.2% | 0.00 | 14.5% | 47.3% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

