# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1885s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 35.2% [33.9–36.6] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [11.0–11.0] (media 11.12) | 8–11 | ✅ |
| Partite al round 13+ | 30.5% [24.5–37.2] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=104) | 20.2% [13.6–28.9] | 20–35% | ✅ |
| Attacchi con opposizione | 30.1% [28.9–31.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 63.3% [61.9–64.8] (con ≥3: 23.7% [22.5–25.0]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.1% [34.7–37.4] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 8.5% [6.0–11.8] (n=355) / 88.4% [84.3–91.6] (n=294) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.5% [13.0–16.2] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-05 Base 58.3% [38.8–75.5] (n=24), LDR-05 Risvegliato 79.4% [67.8–87.5] (n=63), LDR-06 Base 50.0% [18.8–81.2] (n=6), LDR-06 Risvegliato 64.5% [57.6–70.8] (n=197) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 35.0% [28.0–42.7] (n=160) | | |
| Attacchi per partita | 24.8 | | |
| Pugno attaccante vuoto / pieno | 54.9% [53.4–56.4] / 10.9% [10.0–11.8] (gemme medie 0.75) | non >90% | |
| Pugno difensore vuoto / pieno | 56.1% [54.1–58.1] / 25.2% [23.5–27.0] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1682, 1: 1600, 2: 1135, 3: 373, 4: 138, 5: 34, 6: 6} | | |
| Azioni legali per decisione | 5.6 | <60 | ✅ |
| Fine partita | {'colpo_finale': 184, 'crepuscolo': 16} | | |
| G1 vince fra le partite finite al Crepuscolo | 68.8% [44.4–85.8] | | |
| G1 vince fra le partite arrivate al round 15 | 68.2% [47.3–83.6] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 27.3% [13.2–48.2] / 50.0% [18.8–81.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [18.8–81.2]; 13.6% [4.7–33.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 3, '2-2': 3, '2-1': 3, '2-3': 3, '0-0': 2, '3-2': 2, '0-4': 1, '3-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=9) | 40.9% [23.3–61.3] / 33.3% [12.1–64.6] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 6, 16: 3}; 44.4% [18.9–73.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 66.7% [35.4–87.9] / 33.3% [12.1–64.6]; 1.78 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–29.9] / 77.8% [45.3–93.7] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 50.0% [18.8–81.2]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.5% [0.5–4.3] / 13.6% [4.7–33.3]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 2, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=10) / turno di G2 (n=8) | 0.0% [0.0–27.8] / 0.0% [0.0–32.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=10) | 0.0% [0.0–27.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 45.5% [26.9–65.3] (4.5% [0.8–21.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 6, 'rif_LDR06_ferite_e_caccia': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR05_scudi_armati vs rif_LDR06_ferite_e_caccia 68% (n=22) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR05_scudi_armati 69.0% [62.3–75.0], rif_LDR06_ferite_e_caccia 31.0% [25.0–37.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.365 / 0.091 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.090 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR05_scudi_armati 0.10 (0.00), rif_LDR06_ferite_e_caccia 0.15 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 33.0% [31.7–34.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.75 (239 / 512); 58.5% [57.1–59.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 49.2% [48.2–50.2]; rif_LDR05_scudi_armati 55.2%, rif_LDR06_ferite_e_caccia 43.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.325 (367) / 0.332 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-05 R: 18.0 (49%, 138 vittorie), LDR-06 G: 17.0 (49%, 62 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.50, LDR-05 3.23, VER-020 2.19, NER-017 1.17, NER-009 0.74, VER-001 0.72, NEU-001 0.67, NER-013 0.63, BLU-015 0.58, VER-008 0.57, NEU-012 0.49, BLU-021 0.47 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR05_scudi_armati 0.12, rif_LDR06_ferite_e_caccia 2.85 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.28 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR05_scudi_armati 38% (n=24), rif_LDR06_ferite_e_caccia 15% (n=80) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.9% [10.0–11.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.86; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, collante 100%, NEU-009 69%, BLU-021 69%, BLU-010 69%, ROS-020 69%, NEU-013 69%, BLU-008 69%, NER-009 31%, caccia 31%, NER-015 31%, NEU-012 31%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR05_scudi_armati | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR05_scudi_armati | — | 69.0 [62–75] (200) |
| rif_LDR06_ferite_e_caccia | 31.0 [25–38] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 3.79 | 0.00 | 3.23 / 0.00 | 0.00 | 0.76 | 5.0 (198) | 13 | B 48%, R 52% | 2.23 | 0.00 |
| rif_LDR06_ferite_e_caccia | 3.72 | 0.00 | 3.50 / 0.12 | 0.00 | 0.16 | 4.8 (195) | 9 | G 53%, K 47% | 1.96 | 1.30 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.23/1.44/0.58 | 0.56/0.32/0.14/0.09 | 0.66/0.00/0.21/0.10 | 0.63/0.41/0.20/0.12 | 0.66/0.24/0.30/0.18 | 0.56/0.00/0.14/0.10 | 0.74/0.58/0.30/0.17 | 0.00/0.47/0.00/0.00 | 0.00/0.43/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.41/0.28/0.17 | 0.63/0.36/0.14/0.07 | 0.00/0.00/0.00/0.00 | 0.69/0.36/0.12/0.07 | 0.00/0.40/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.18/0.28/0.15 | 0.00/0.00/0.00/0.00 | 0.30/0.36/0.00/0.00 | 0.68/0.41/0.38/0.21 | 0.48/0.32/0.28/0.24 | 0.21/0.07/0.17/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.00/0.07/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.06/0.11/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.02/0.02 | 0.40/0.02/0.01/0.01 | 0.28/0.09/0.12/0.07 | 0.33/0.22/0.12/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.72/0.04/0.51 | 0.62/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.41/0.51/0.27 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.50/1.81/0.70 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.36/0.14/0.07 | 0.41/0.41/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.23/0.41/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.35/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.49/0.04/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.57/0.01/0.26 | 0.28/0.01/0.01/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.67/0.14/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.00/0.00/0.00 | 0.45/0.00/0.00/0.00 | 0.22/0.35/0.06/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.11/0.03 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.89 | 0.00 | 0.04 | 0.00 | 0.01 | 0.03 | 0.07 | 0.03 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.14 | 0.22 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.47 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 0.69 | 0.00 | 0.02 | 0.05 | 0.05 | 0.08 | 0.08 | 0.14 | 0.08 | 0.07 | 0.06 | 0.03 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.82 | 0.00 | 0.03 | 0.04 | 0.07 | 0.12 | 0.12 | 0.14 | 0.13 | 0.07 | 0.04 | 0.02 | 0.04 | 0.00 | 0.86 | 0.11 | 0.17 | 0.17 | 0.10 | 0.07 | 0.10 | 0.07 | 0.04 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR05_scudi_armati | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.44 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 0 | 2 | 0 | 2 |
| 7 | 2 | 6 | 0 | 8 |
| 8 | 8 | 7 | 0 | 15 |
| 9 | 19 | 9 | 0 | 28 |
| 10 | 19 | 13 | 0 | 32 |
| 11 | 16 | 16 | 0 | 32 |
| 12 | 12 | 9 | 0 | 21 |
| 13 | 17 | 8 | 0 | 25 |
| 14 | 4 | 10 | 0 | 14 |
| 15 | 13 | 6 | 0 | 19 |
| 16 | 2 | 1 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 55.2% | 0.110 | 0.12 | 0.00 | 0.00 | 0.00 | 2.65 | 0.00 | 0.00 | 0.366 |
| rif_LDR06_ferite_e_caccia | 200 | 43.0% | 0.070 | 0.94 | 1.91 | 0.00 | 0.00 | 4.49 | 0.00 | 0.00 | 0.364 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | mano | 625 | 0.867 | 0.842 | 0.830 | 0.430 | 2006 | 0.773 | 0.195 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 625 | 0.130 | 0.123 | 0.120 | 0.034 | 2006 | 0.108 | 0.038 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 387 | 0.879 | 0.822 | 0.765 | 0.344 | 1950 | 0.739 | 0.237 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 387 | 0.274 | 0.253 | 0.207 | 0.080 | 1950 | 0.215 | 0.069 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 8.0% | 2.25 | 1.68 | 42.5% | 0.5% | 23.7% | 29.0% | 14.0% | 0.00 | 14.8% | 55.2% | 0.03 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 8.0% | 2.25 | 1.68 | 20.4% | 0.5% | 25.7% | 28.5% | 5.4% | 0.00 | 14.6% | 43.0% | 0.04 | 0.00 |
| Totale | 400 | 8.0% | 2.25 | 1.68 | 27.2% | 0.5% | 24.7% | 28.7% | 9.2% | 0.00 | 14.7% | 49.2% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 0.286 | 0.138 | 0.0% | 0.0% | 1.11 | 0.97 | 0.42 | 0.41 | 0.00 | 0.00 | 4.84 |
| rif_LDR06_ferite_e_caccia | 200 | 0.318 | 0.056 | 0.0% | 0.0% | 0.55 | 0.00 | 0.06 | 0.01 | 0.00 | 0.00 | 4.11 |

