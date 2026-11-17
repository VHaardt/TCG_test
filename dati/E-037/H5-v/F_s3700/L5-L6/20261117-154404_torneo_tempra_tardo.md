# Torneo v0.2 — /home/claude/e037_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e037_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 795s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 34.3% [32.3–36.2] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–12.0] (media 11.37) | 8–11 | ✅ |
| Partite al round 13+ | 40.0% [30.9–49.8] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=33) | 45.5% [29.8–62.0] | 20–35% | ❌ |
| Attacchi con opposizione | 32.9% [31.0–34.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 65.5% [63.5–67.4] (con ≥3: 28.3% [26.5–30.2]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.3% [34.3–38.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.3% [2.2–8.2] (n=187) / 91.2% [85.8–94.7] (n=160) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 17.6% [15.2–20.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-05 Base 33.3% [6.1–79.2] (n=3), LDR-05 Risvegliato 73.7% [62.8–82.3] (n=76), LDR-06 Base 40.0% [11.8–76.9] (n=5), LDR-06 Risvegliato 61.4% [49.7–72.0] (n=70) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 45.9% [35.7–56.4] (n=85) | | |
| Attacchi per partita | 22.8 | | |
| Pugno attaccante vuoto / pieno | 55.0% [52.9–57.2] / 11.0% [9.7–12.4] (gemme medie 0.75) | non >90% | |
| Pugno difensore vuoto / pieno | 50.5% [47.4–53.6] / 30.1% [27.4–33.0] (gemme medie 0.28) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 682, 1: 839, 2: 526, 3: 153, 4: 61, 5: 21} | | |
| Azioni legali per decisione | 5.6 | <60 | ✅ |
| Fine partita | {'colpo_finale': 91, 'crepuscolo': 9} | | |
| G1 vince fra le partite finite al Crepuscolo | 66.7% [35.4–87.9] | | |
| G1 vince fra le partite arrivate al round 15 | 58.3% [32.0–80.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 41.7% [19.3–68.0] / 40.0% [11.8–76.9] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 60.0% [23.1–88.2]; 8.3% [1.5–35.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-3': 3, '1-0': 3, '0-0': 2, '2-0': 1, '2-1': 1, '3-3': 1, '3-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=6) | 50.0% [25.4–74.6] / 33.3% [9.7–70.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 1, 15: 5}; 50.0% [18.8–81.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 66.7% [30.0–90.3] / 50.0% [18.8–81.2]; 2.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–39.0] / 100.0% [61.0–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 75.0% [30.1–95.4]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 16.7% [4.7–44.8]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=7) / turno di G2 (n=4) | 0.0% [0.0–35.4] / 0.0% [0.0–49.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=7) | 0.0% [0.0–35.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 58.3% [32.0–80.7] (8.3% [1.5–35.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 4, 'rif_LDR05_scudi_armati': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR05_scudi_armati vs rif_LDR06_ferite_e_caccia 58% (n=12) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR05_scudi_armati 56.0% [46.2–65.3], rif_LDR06_ferite_e_caccia 44.0% [34.7–53.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.359 / 0.100 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.098 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR05_scudi_armati 0.10 (0.00), rif_LDR06_ferite_e_caccia 0.10 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 37.4% [35.5–39.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.87 (144 / 243); 54.7% [52.7–56.8] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 56.2% [54.8–57.6]; rif_LDR05_scudi_armati 60.8%, rif_LDR06_ferite_e_caccia 51.8% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.318 (210) / 0.305 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-05 R: 18.0 (49%, 56 vittorie), LDR-06 G: 17.0 (49%, 44 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 2.99, LDR-05 2.77, VER-020 2.66, NER-017 1.03, VER-008 0.87, VER-001 0.74, NER-009 0.64, NER-013 0.62, BLU-015 0.56, NER-015 0.53, BLU-021 0.53, NEU-001 0.53 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR05_scudi_armati 0.14, rif_LDR06_ferite_e_caccia 2.89 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.19 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR05_scudi_armati 65% (n=17), rif_LDR06_ferite_e_caccia 25% (n=16) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.0% [9.7–12.4] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.95; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-013 56%, ROS-020 56%, BLU-021 56%, NEU-009 56%, BLU-010 56%, BLU-008 56%, NEU-012 44%, NER-017 44%, NER-015 44%, VER-020 44%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR05_scudi_armati | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR05_scudi_armati | — | 56.0 [46–65] (100) |
| rif_LDR06_ferite_e_caccia | 44.0 [35–54] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 3.89 | 0.00 | 2.77 / 0.00 | 0.00 | 0.70 | 4.7 (100) | 11 | B 45%, R 55% | 2.26 | 0.00 |
| rif_LDR06_ferite_e_caccia | 3.50 | 0.00 | 2.99 / 0.06 | 0.00 | 0.14 | 4.5 (97) | 9 | G 54%, K 46% | 1.91 | 1.22 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR05_scudi_armati | 0.76 | 2.01 |
| rif_LDR06_ferite_e_caccia | 0.52 | 2.47 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.77/1.89/0.56 | 0.56/0.36/0.13/0.09 | 0.65/0.00/0.08/0.08 | 0.59/0.24/0.13/0.08 | 0.64/0.28/0.18/0.22 | 0.46/0.00/0.13/0.10 | 0.60/0.56/0.26/0.17 | 0.00/0.53/0.00/0.00 | 0.00/0.38/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.31/0.27/0.10 | 0.71/0.35/0.14/0.07 | 0.00/0.00/0.00/0.00 | 0.72/0.48/0.22/0.05 | 0.00/0.37/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.22/0.24/0.15 | 0.00/0.00/0.00/0.00 | 0.33/0.27/0.00/0.00 | 0.59/0.27/0.19/0.24 | 0.51/0.35/0.21/0.36 | 0.22/0.01/0.10/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.00/0.12/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.26/0.09/0.07/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.03/0.01 | 0.33/0.03/0.04/0.01 | 0.29/0.03/0.04/0.03 | 0.37/0.17/0.15/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.74/0.05/0.53 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.34/0.43/0.22 | 0.00/0.19/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.99/1.58/0.58 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.46/0.11/0.11 | 0.46/0.40/0.11/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.15/0.30/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.35/0.02/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.46/0.01/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.87/0.03/0.31 | 0.28/0.02/0.03/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.53/0.15/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.00/0.00/0.00 | 0.45/0.00/0.00/0.00 | 0.22/0.24/0.03/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.06/0.00 | 0.26/0.52/0.11/0.06 | 0.32/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.64 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.06 | 0.20 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.63 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 0.59 | 0.00 | 0.04 | 0.07 | 0.07 | 0.07 | 0.09 | 0.11 | 0.06 | 0.03 | 0.03 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.91 | 0.00 | 0.00 | 0.05 | 0.09 | 0.15 | 0.10 | 0.19 | 0.18 | 0.07 | 0.05 | 0.00 | 0.01 | 0.02 | 0.95 | 0.10 | 0.18 | 0.14 | 0.14 | 0.12 | 0.12 | 0.07 | 0.06 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 1 | 1 | 0 | 2 |
| 7 | 4 | 1 | 0 | 5 |
| 8 | 2 | 4 | 0 | 6 |
| 9 | 5 | 5 | 0 | 10 |
| 10 | 9 | 7 | 0 | 16 |
| 11 | 7 | 5 | 0 | 12 |
| 12 | 5 | 3 | 0 | 8 |
| 13 | 11 | 3 | 0 | 14 |
| 14 | 3 | 11 | 0 | 14 |
| 15 | 7 | 4 | 0 | 11 |
| 16 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 60.8% | 0.117 | 0.14 | 0.00 | 0.00 | 0.00 | 2.51 | 0.00 | 0.00 | 0.400 |
| rif_LDR06_ferite_e_caccia | 100 | 51.8% | 0.079 | 0.92 | 1.97 | 0.00 | 0.00 | 4.21 | 0.00 | 0.00 | 0.311 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | mano | 324 | 0.923 | 0.910 | 0.910 | 0.420 | 922 | 0.828 | 0.206 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 324 | 0.130 | 0.123 | 0.120 | 0.031 | 922 | 0.098 | 0.025 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 179 | 0.821 | 0.765 | 0.709 | 0.402 | 857 | 0.702 | 0.191 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 179 | 0.268 | 0.212 | 0.168 | 0.056 | 857 | 0.225 | 0.058 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 9.0% | 2.16 | 1.84 | 33.3% | 1.0% | 23.3% | 34.6% | 11.6% | 0.00 | 14.8% | 60.8% | 0.06 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 9.0% | 2.16 | 1.84 | 28.2% | 1.0% | 24.3% | 32.3% | 8.1% | 0.00 | 12.8% | 51.8% | 0.07 | 0.00 |
| Totale | 200 | 9.0% | 2.16 | 1.84 | 30.3% | 1.0% | 23.8% | 33.5% | 9.7% | 0.00 | 13.8% | 56.2% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 0.307 | 0.140 | 0.0% | 0.0% | 0.95 | 0.97 | 0.40 | 0.48 | 0.00 | 0.00 | 4.62 |
| rif_LDR06_ferite_e_caccia | 100 | 0.354 | 0.059 | 0.0% | 0.0% | 0.49 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 3.66 |

