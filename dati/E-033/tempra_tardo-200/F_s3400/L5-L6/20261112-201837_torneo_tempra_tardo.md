# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 819s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 36.7% [35.4–38.0] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 10.99) | 8–11 | ✅ |
| Partite al round 13+ | 30.5% [24.5–37.2] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–1.9] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=89) | 23.6% [16.0–33.4] | 20–35% | ✅ |
| Attacchi con opposizione | 27.1% [25.9–28.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 59.2% [57.7–60.6] (con ≥3: 20.5% [19.3–21.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.0% [34.7–37.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 11.0% [8.2–14.7] (n=362) / 90.6% [86.8–93.4] (n=308) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.4% [13.8–17.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-05 Base 56.7% [39.2–72.6] (n=30), LDR-05 Risvegliato 83.3% [72.6–90.4] (n=66), LDR-06 Base 50.0% [23.7–76.3] (n=10), LDR-06 Risvegliato 70.0% [63.5–75.7] (n=213) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 36.5% [29.4–44.3] (n=156) | | |
| Attacchi per partita | 25.2 | | |
| Pugno attaccante vuoto / pieno | 56.1% [54.7–57.6] / 11.2% [10.3–12.1] (gemme medie 0.73) | non >90% | |
| Pugno difensore vuoto / pieno | 58.3% [56.3–60.3] / 24.9% [23.2–26.6] (gemme medie 0.25) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1731, 1: 1639, 2: 1178, 3: 338, 4: 118, 5: 34, 6: 7} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 184, 'crepuscolo': 16} | | |
| G1 vince fra le partite finite al Crepuscolo | 56.2% [33.2–76.9] | | |
| G1 vince fra le partite arrivate al round 15 | 52.4% [32.4–71.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 38.1% [20.8–59.1] / 37.5% [13.7–69.4] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [21.5–78.5]; 0.0% [0.0–15.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 4, '3-1': 3, '2-2': 3, '1-2': 2, '0-0': 2, '2-0': 1, '0-2': 1, '4-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=8) | 38.1% [20.8–59.1] / 37.5% [13.7–69.4] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 8}; 50.0% [21.5–78.5] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 37.5% [13.7–69.4] / 37.5% [13.7–69.4]; 2.12 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–32.4] / 87.5% [52.9–97.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 60.0% [23.1–88.2]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.5% [0.5–4.3] / 14.3% [5.0–34.6]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 1, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=6) / turno di G2 (n=9) | 0.0% [0.0–39.0] / 0.0% [0.0–29.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=6) | 0.0% [0.0–39.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 47.6% [28.3–67.6] (9.5% [2.7–28.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 7, 'rif_LDR05_scudi_armati': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR05_scudi_armati vs rif_LDR06_ferite_e_caccia 52% (n=21) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR05_scudi_armati 69.0% [62.3–75.0], rif_LDR06_ferite_e_caccia 31.0% [25.0–37.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.401 / 0.087 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.086 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR05_scudi_armati 0.15 (0.00), rif_LDR06_ferite_e_caccia 0.11 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 33.4% [32.1–34.7] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 4.38 (257 / 620); 59.6% [58.2–60.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 46.6% [45.5–47.6]; rif_LDR05_scudi_armati 53.3%, rif_LDR06_ferite_e_caccia 40.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.325 (356) / 0.325 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-05 R: 18.0 (49%, 138 vittorie), LDR-06 G: 17.0 (49%, 62 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.37, LDR-05 2.90, VER-020 2.46, NER-017 1.34, VER-008 1.03, VER-001 0.80, NEU-001 0.74, NER-009 0.73, BLU-015 0.68, NER-013 0.66, NER-015 0.59, NEU-012 0.54 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR05_scudi_armati 0.14, rif_LDR06_ferite_e_caccia 3.19 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.20 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR05_scudi_armati 43% (n=7), rif_LDR06_ferite_e_caccia 22% (n=82) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.2% [10.3–12.1] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.95; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-009 69%, BLU-010 69%, BLU-008 69%, BLU-021 69%, ROS-020 69%, NEU-013 69%, VER-008 31%, VER-001 31%, VER-020 31%, VER-023 31%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR05_scudi_armati | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR05_scudi_armati | — | 69.0 [62–75] (200) |
| rif_LDR06_ferite_e_caccia | 31.0 [25–38] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 3.94 | 0.00 | 2.90 / 0.00 | 0.00 | 0.71 | 5.0 (200) | 12 | B 46%, R 54% | 2.46 | 0.00 |
| rif_LDR06_ferite_e_caccia | 3.75 | 0.00 | 3.37 / 0.08 | 0.00 | 0.17 | 4.9 (197) | 10 | G 57%, K 43% | 2.05 | 1.46 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.90/1.54/0.49 | 0.62/0.34/0.12/0.07 | 0.54/0.00/0.12/0.03 | 0.56/0.32/0.14/0.07 | 0.64/0.14/0.31/0.10 | 0.65/0.00/0.23/0.17 | 0.68/0.68/0.33/0.22 | 0.00/0.50/0.00/0.00 | 0.00/0.47/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.44/0.32/0.18 | 0.71/0.32/0.12/0.04 | 0.00/0.00/0.00/0.00 | 0.65/0.25/0.09/0.05 | 0.00/0.36/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.17/0.29/0.14 | 0.00/0.00/0.00/0.00 | 0.36/0.43/0.00/0.00 | 0.64/0.39/0.33/0.24 | 0.53/0.45/0.38/0.27 | 0.23/0.06/0.16/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.61/0.00/0.07/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.05/0.09/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.01/0.01 | 0.33/0.01/0.02/0.01 | 0.32/0.08/0.11/0.06 | 0.28/0.16/0.07/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.80/0.05/0.53 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.36/0.59/0.20 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.37/1.80/0.63 | 0.00/0.00/0.00/0.00 | 0.53/0.00/0.00/0.00 | 0.23/0.41/0.01/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.41/0.18/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.12/0.28/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.39/0.04/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.54/0.03/0.38 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/1.03/0.01/0.43 | 0.36/0.04/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.84/0.74/0.23/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 1.10 | 0.00 | 0.10 | 0.00 | 0.01 | 0.01 | 0.04 | 0.02 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.15 | 0.36 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.66 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 0.52 | 0.00 | 0.02 | 0.02 | 0.04 | 0.03 | 0.09 | 0.10 | 0.09 | 0.07 | 0.03 | 0.03 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.81 | 0.00 | 0.01 | 0.04 | 0.09 | 0.10 | 0.12 | 0.14 | 0.12 | 0.07 | 0.04 | 0.05 | 0.04 | 0.01 | 0.00 | 0.95 | 0.10 | 0.19 | 0.17 | 0.12 | 0.15 | 0.09 | 0.04 | 0.06 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 1 | 0 | 0 | 1 |
| 6 | 0 | 1 | 0 | 1 |
| 7 | 4 | 4 | 0 | 8 |
| 8 | 9 | 12 | 0 | 21 |
| 9 | 15 | 12 | 0 | 27 |
| 10 | 20 | 13 | 0 | 33 |
| 11 | 22 | 11 | 0 | 33 |
| 12 | 8 | 7 | 0 | 15 |
| 13 | 15 | 12 | 0 | 27 |
| 14 | 1 | 12 | 0 | 13 |
| 15 | 11 | 10 | 0 | 21 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 53.3% | 0.110 | 0.14 | 0.00 | 0.00 | 0.00 | 2.35 | 0.00 | 0.00 | 0.360 |
| rif_LDR06_ferite_e_caccia | 200 | 40.1% | 0.060 | 0.88 | 2.31 | 0.00 | 0.00 | 4.54 | 0.00 | 0.00 | 0.451 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | mano | 667 | 0.832 | 0.820 | 0.814 | 0.411 | 2105 | 0.743 | 0.198 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 667 | 0.141 | 0.133 | 0.129 | 0.045 | 2105 | 0.108 | 0.034 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 336 | 0.938 | 0.914 | 0.881 | 0.342 | 1937 | 0.906 | 0.352 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 336 | 0.277 | 0.253 | 0.244 | 0.065 | 1937 | 0.214 | 0.092 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 8.0% | 2.20 | 1.53 | 42.9% | 0.5% | 27.2% | 29.6% | 9.7% | 0.00 | 15.6% | 53.3% | 0.06 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 8.0% | 2.20 | 1.53 | 18.7% | 0.5% | 24.3% | 28.6% | 8.5% | 0.00 | 13.7% | 40.1% | 0.07 | 0.00 |
| Totale | 400 | 8.0% | 2.20 | 1.53 | 27.4% | 0.5% | 25.8% | 29.1% | 9.1% | 0.00 | 14.6% | 46.6% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

