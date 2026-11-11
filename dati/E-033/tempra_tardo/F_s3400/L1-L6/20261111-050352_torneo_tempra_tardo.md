# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 648s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.4% [27.6–31.3] | 30–45% | ❌ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 10.67) | 8–11 | ✅ |
| Partite al round 13+ | 22.0% [15.0–31.1] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 1.0% [0.2–5.4] | 0 | ❌ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=39) | 25.6% [14.6–41.1] | 20–35% | ✅ |
| Attacchi con opposizione | 23.5% [21.9–25.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 57.7% [55.6–59.8] (con ≥3: 19.7% [18.0–21.4]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 40.7% [38.7–42.7] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 8.0% [5.0–12.4] (n=213) / 85.5% [79.4–90.0] (n=172) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.2% [13.1–17.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 57.1% [32.6–78.6] (n=14), LDR-01 Risvegliato 71.4% [58.5–81.6] (n=56), LDR-06 Base 33.3% [6.1–79.2] (n=3), LDR-06 Risvegliato 73.6% [63.7–81.6] (n=91) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 24.1% [16.2–34.3] (n=83) | | |
| Attacchi per partita | 23.7 | | |
| Pugno attaccante vuoto / pieno | 51.6% [49.5–53.7] / 13.4% [12.0–14.9] (gemme medie 0.85) | non >90% | |
| Pugno difensore vuoto / pieno | 60.3% [57.4–63.1] / 24.5% [22.0–27.0] (gemme medie 0.24) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 777, 1: 802, 2: 543, 3: 185, 4: 45, 5: 18, 6: 1} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 93, 'crepuscolo': 7} | | |
| G1 vince fra le partite finite al Crepuscolo | 57.1% [25.0–84.2] | | |
| G1 vince fra le partite arrivate al round 15 | 50.0% [21.5–78.5] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 62.5% [30.6–86.3] / 20.0% [3.6–62.4] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 40.0% [11.8–76.9]; 0.0% [0.0–32.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 2, '0-1': 2, '3-0': 2, '0-0': 1, '2-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=5) | 62.5% [30.6–86.3] / 20.0% [3.6–62.4] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 5}; 60.0% [23.1–88.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 20.0% [3.6–62.4] / 20.0% [3.6–62.4]; 2.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–43.4] / 60.0% [23.1–88.2] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=1) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–79.3] / 25.0% [4.6–69.9]; 0.0% [0.0–79.3] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.0% [0.2–5.4] / 12.5% [2.2–47.1]; 100.0% [20.7–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:pronto': 1, 'vinc:atk': 1} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=4) / turno di G2 (n=5) | 0.0% [0.0–49.0] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=4) | 0.0% [0.0–49.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 25.0% [7.1–59.1] (0.0% [0.0–32.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 3, 'rif_LDR06_ferite_e_caccia': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR06_ferite_e_caccia 50% (n=8) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 70.0% [60.4–78.1], rif_LDR06_ferite_e_caccia 30.0% [21.9–39.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.384 / 0.077 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.077 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.06 (0.00), rif_LDR06_ferite_e_caccia 0.11 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 34.8% [32.9–36.7] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 4.91 (147 / 344); 60.8% [58.8–62.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 48.5% [47.0–50.0]; rif_LDR01_puntata_e_preda 52.5%, rif_LDR06_ferite_e_caccia 44.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.7] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.330 (206) / 0.308 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 70 vittorie), LDR-06 G: 17.0 (49%, 30 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 2.71, VER-020 2.14, LDR-01 1.82, ROS-016 1.28, NER-017 1.01, ROS-018 1.00, VER-008 0.70, VER-003 0.64, NER-009 0.61, NEU-001 0.60, VER-001 0.56, VER-011 0.54 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 1.01, rif_LDR06_ferite_e_caccia 2.93 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR06_ferite_e_caccia 0.20 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 60% (n=10), rif_LDR06_ferite_e_caccia 14% (n=29) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.4% [12.0–14.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR06_ferite_e_caccia 0.81; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, VER-001 100%, VER-008 100%, caccia 100%, ROS-016 70%, VER-011 70%, VER-020 30%, VER-023 30%, collante 30%, NER-009 30%, NEU-012 30%, NER-017 30%; oltre il 60%: ROS-016, VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 70.0 [60–78] (100) |
| rif_LDR06_ferite_e_caccia | 30.0 [22–40] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.55 | 0.00 | 1.82 / 0.00 | 0.00 | 0.00 | 4.6 (100) | 13 | G 40%, R 60% | 2.35 | 0.40 |
| rif_LDR06_ferite_e_caccia | 3.93 | 0.00 | 2.71 / 0.06 | 0.00 | 0.19 | 4.4 (97) | 9 | G 58%, K 42% | 2.25 | 1.54 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.82/1.88/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.45/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.43/0.22/0.08 | 0.87/0.06/0.67/0.27 | 0.64/0.27/0.12/0.02 | 0.00/0.27/0.00/0.00 | 0.69/0.00/0.17/0.07 | 0.71/0.22/0.29/0.12 | 0.64/1.28/0.08/0.53 | 0.75/1.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.35/0.31/0.17 | 0.20/0.07/0.26/0.09 | 0.00/0.00/0.00/0.00 | 0.69/0.54/0.08/0.44 | 0.63/0.00/0.00/0.00 | 0.74/0.00/0.11/0.03 | 0.69/0.54/0.20/0.08 | 0.70/0.55/0.52/0.19 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.00/0.10/0.01 | 0.35/0.03/0.05/0.02 | 0.33/0.03/0.09/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.27/0.00/0.03/0.00 | 0.42/0.64/0.03/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.59/0.10/0.48 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.40/0.50/0.18 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.71/1.97/0.67 | 0.00/0.00/0.00/0.00 | 0.45/0.00/0.00/0.00 | 0.15/0.15/0.03/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.46/0.24/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.10/0.30/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.28/0.05/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.37/0.07/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.76/0.01/0.39 | 0.36/0.02/0.02/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.84/0.60/0.17/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.23 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.12 | 0.00 | 0.00 | 0.00 | 0.17 | 0.13 | 0.00 | 0.00 | 0.28 | 0.07 | 0.00 | 0.02 | 0.00 | 0.01 | 0.05 | 0.18 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.03 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.51 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.67 | 0.00 | 0.04 | 0.05 | 0.07 | 0.06 | 0.07 | 0.11 | 0.14 | 0.06 | 0.02 | 0.03 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.97 | 0.00 | 0.02 | 0.07 | 0.07 | 0.14 | 0.09 | 0.15 | 0.16 | 0.12 | 0.07 | 0.04 | 0.02 | 0.01 | 0.01 | 0.81 | 0.08 | 0.18 | 0.08 | 0.09 | 0.15 | 0.09 | 0.07 | 0.04 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 4 | 0 | 1 | 0 | 1 |
| 5 | 0 | 1 | 0 | 1 |
| 7 | 1 | 3 | 0 | 4 |
| 8 | 3 | 8 | 0 | 11 |
| 9 | 5 | 7 | 0 | 12 |
| 10 | 6 | 14 | 0 | 20 |
| 11 | 13 | 10 | 0 | 23 |
| 12 | 4 | 2 | 0 | 6 |
| 13 | 3 | 4 | 0 | 7 |
| 14 | 1 | 6 | 0 | 7 |
| 15 | 4 | 4 | 0 | 8 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 52.5% | 0.069 | 0.00 | 1.01 | 0.00 | 0.00 | 2.75 | 0.00 | 0.00 | 0.346 |
| rif_LDR06_ferite_e_caccia | 100 | 44.3% | 0.085 | 0.87 | 2.06 | 0.00 | 0.00 | 4.34 | 0.00 | 0.00 | 0.426 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 251 | 0.857 | 0.805 | 0.769 | 0.319 | 989 | 0.781 | 0.201 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 251 | 0.207 | 0.187 | 0.139 | 0.024 | 989 | 0.183 | 0.054 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 202 | 0.906 | 0.891 | 0.871 | 0.421 | 929 | 0.806 | 0.318 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 202 | 0.223 | 0.183 | 0.168 | 0.054 | 929 | 0.207 | 0.067 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 7.0% | 1.82 | 1.53 | 44.7% | 2.0% | 22.7% | 24.3% | 3.6% | 0.00 | 13.9% | 52.5% | 0.08 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 7.0% | 1.82 | 1.53 | 23.6% | 2.0% | 21.0% | 30.6% | 8.4% | 0.00 | 11.6% | 44.3% | 0.07 | 0.00 |
| Totale | 200 | 7.0% | 1.82 | 1.53 | 30.9% | 2.0% | 21.8% | 27.4% | 6.4% | 0.00 | 12.8% | 48.5% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

