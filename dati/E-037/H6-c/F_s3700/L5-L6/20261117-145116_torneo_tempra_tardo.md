# Torneo v0.2 — /root/in37/dati/E-037-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in37/dati/E-037-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 738s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 36.3% [34.3–38.2] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–12.0] (media 10.89) | 8–11 | ✅ |
| Partite al round 13+ | 34.0% [25.5–43.7] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 1.0% [0.2–5.4] | 0 | ❌ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=43) | 34.9% [22.4–49.8] | 20–35% | ✅ |
| Attacchi con opposizione | 27.5% [25.7–29.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 61.4% [59.3–63.5] (con ≥3: 24.7% [22.9–26.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.6% [32.7–36.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.9% [2.5–9.4] (n=163) / 89.8% [83.4–94.0] (n=128) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.4% [12.1–17.0] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-05 Base 57.1% [25.0–84.2] (n=7), LDR-05 Risvegliato 87.0% [67.9–95.5] (n=23), LDR-06 Base 100.0% [20.7–100.0] (n=1), LDR-06 Risvegliato 71.7% [61.8–79.9] (n=92) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 45.8% [34.8–57.3] (n=72) | | |
| Attacchi per partita | 23.2 | | |
| Pugno attaccante vuoto / pieno | 55.9% [53.7–58.0] / 9.6% [8.4–10.9] (gemme medie 0.76) | non >90% | |
| Pugno difensore vuoto / pieno | 55.0% [52.1–58.0] / 27.7% [25.1–30.4] (gemme medie 0.28) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 720, 1: 792, 2: 528, 3: 189, 4: 63, 5: 17, 6: 8} | | |
| Azioni legali per decisione | 5.8 | <60 | ✅ |
| Fine partita | {'colpo_finale': 91, 'crepuscolo': 9} | | |
| G1 vince fra le partite finite al Crepuscolo | 66.7% [35.4–87.9] | | |
| G1 vince fra le partite arrivate al round 15 | 53.8% [29.1–76.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 30.8% [12.7–57.6] / 50.0% [15.0–85.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [15.0–85.0]; 7.7% [1.4–33.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-1': 3, '2-3': 2, '2-2': 2, '0-0': 2, '1-0': 2, '3-2': 1, '1-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=5) | 38.5% [17.7–64.5] / 40.0% [11.8–76.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 1, 15: 4}; 40.0% [11.8–76.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 60.0% [23.1–88.2] / 60.0% [23.1–88.2]; 3.20 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–43.4] / 60.0% [23.1–88.2] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 100.0% [43.8–100.0]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 15.4% [4.3–42.2]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:pronto': 1, 'perd:rim': 1, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=4) | 0.0% [0.0–43.4] / 0.0% [0.0–49.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 46.2% [23.2–70.9] (0.0% [0.0–22.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 3, 'rif_LDR05_scudi_armati': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR05_scudi_armati vs rif_LDR06_ferite_e_caccia 54% (n=13) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR05_scudi_armati 65.0% [55.3–73.6], rif_LDR06_ferite_e_caccia 35.0% [26.4–44.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.381 / 0.099 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.098 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR05_scudi_armati 0.11 (0.00), rif_LDR06_ferite_e_caccia 0.14 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 35.1% [33.2–37.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 4.58 (114 / 344); 57.4% [55.3–59.4] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.3% [48.9–51.8]; rif_LDR05_scudi_armati 59.1%, rif_LDR06_ferite_e_caccia 43.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.363 (158) / 0.318 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-05 R: 18.0 (49%, 65 vittorie), LDR-06 G: 17.0 (49%, 35 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 5.54, VER-020 2.91, LDR-05 2.47, NER-017 1.37, VER-008 1.23, NER-013 0.80, VER-001 0.72, NEU-012 0.68, NER-009 0.65, NEU-001 0.60, NER-001 0.54, NER-015 0.53 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR05_scudi_armati 0.12, rif_LDR06_ferite_e_caccia 3.58 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.51 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR06_ferite_e_caccia 35% (n=43) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.6% [8.4–10.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 1.34; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, BLU-008 65%, NEU-009 65%, NEU-013 65%, ROS-020 65%, BLU-010 65%, BLU-021 65%, NEW-B06 35%, NER-009 35%, VER-001 35%, NEU-012 35%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR05_scudi_armati | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR05_scudi_armati | — | 65.0 [55–74] (100) |
| rif_LDR06_ferite_e_caccia | 35.0 [26–45] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 3.76 | 0.00 | 2.47 / 0.00 | 0.00 | 0.72 | 4.8 (100) | 13 | B 47%, R 53% | 2.18 | 0.00 |
| rif_LDR06_ferite_e_caccia | 2.75 | 0.00 | 5.54 / 0.28 | 0.00 | 0.11 | 4.8 (93) | 10 | G 54%, K 46% | 1.61 | 1.42 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR05_scudi_armati | 1.40 | 1.07 |
| rif_LDR06_ferite_e_caccia | 2.13 | 3.41 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.47/1.54/0.56 | 0.54/0.20/0.11/0.04 | 0.69/0.00/0.24/0.10 | 0.58/0.39/0.21/0.07 | 0.64/0.13/0.19/0.08 | 0.46/0.00/0.11/0.04 | 0.64/0.45/0.17/0.15 | 0.00/0.46/0.00/0.00 | 0.00/0.45/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.29/0.13/0.14 | 0.62/0.40/0.15/0.08 | 0.00/0.00/0.00/0.00 | 0.70/0.32/0.13/0.06 | 0.00/0.41/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.12/0.14/0.10 | 0.00/0.00/0.00/0.00 | 0.30/0.52/0.00/0.00 | 0.64/0.28/0.24/0.10 | 0.53/0.43/0.31/0.22 | 0.20/0.02/0.15/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.00/0.09/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.02/0.01/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.01/0.00 | 0.33/0.03/0.07/0.01 | 0.27/0.08/0.05/0.07 | 0.35/0.18/0.07/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.72/0.05/0.53 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.34/0.49/0.10 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/5.54/1.37/0.34 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.54/0.20/0.10 | 0.41/0.47/0.12/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.14/0.32/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.16/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.38/0.01/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.68/0.01/0.48 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/1.23/0.03/0.55 | 0.32/0.08/0.01/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.60/0.08/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.22/0.37/0.08/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.12/0.05 | 0.17/0.42/0.08/0.03 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.64 | 0.00 | 0.07 | 0.00 | 0.01 | 0.01 | 0.01 | 0.03 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.06 | 0.21 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.62 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.16 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 0.50 | 0.00 | 0.00 | 0.02 | 0.05 | 0.02 | 0.08 | 0.03 | 0.08 | 0.11 | 0.03 | 0.04 | 0.03 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.87 | 0.00 | 0.00 | 0.02 | 0.11 | 0.08 | 0.15 | 0.12 | 0.15 | 0.08 | 0.05 | 0.06 | 0.03 | 0.02 | 0.00 | 1.34 | 0.15 | 0.33 | 0.34 | 0.25 | 0.06 | 0.11 | 0.03 | 0.04 | 0.00 | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR05_scudi_armati | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.21 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 4 | 1 | 0 | 0 | 1 |
| 5 | 1 | 2 | 0 | 3 |
| 6 | 3 | 1 | 0 | 4 |
| 7 | 3 | 2 | 0 | 5 |
| 8 | 3 | 5 | 0 | 8 |
| 9 | 5 | 7 | 0 | 12 |
| 10 | 9 | 3 | 0 | 12 |
| 11 | 6 | 7 | 0 | 13 |
| 12 | 4 | 4 | 0 | 8 |
| 13 | 3 | 7 | 0 | 10 |
| 14 | 8 | 3 | 0 | 11 |
| 15 | 6 | 6 | 0 | 12 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 59.1% | 0.114 | 0.12 | 0.00 | 0.00 | 0.00 | 2.15 | 0.00 | 0.00 | 0.396 |
| rif_LDR06_ferite_e_caccia | 100 | 43.0% | 0.081 | 0.81 | 2.77 | 0.00 | 0.00 | 4.61 | 0.00 | 0.00 | 0.362 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | mano | 293 | 0.925 | 0.911 | 0.911 | 0.464 | 1000 | 0.790 | 0.235 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 293 | 0.133 | 0.123 | 0.109 | 0.038 | 1000 | 0.095 | 0.036 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 199 | 0.849 | 0.804 | 0.719 | 0.347 | 825 | 0.726 | 0.213 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 199 | 0.286 | 0.266 | 0.216 | 0.070 | 825 | 0.217 | 0.074 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 9.0% | 2.18 | 1.86 | 39.0% | 4.0% | 25.3% | 31.8% | 11.6% | 0.00 | 13.1% | 59.1% | 0.02 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 9.0% | 2.18 | 1.86 | 21.8% | 4.0% | 23.3% | 30.4% | 8.6% | 0.00 | 12.2% | 43.0% | 0.29 | 0.00 |
| Totale | 200 | 9.0% | 2.18 | 1.86 | 27.7% | 4.0% | 24.3% | 31.1% | 9.9% | 0.00 | 12.6% | 50.3% | 0.15 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 0.234 | 0.107 | 0.0% | 0.0% | 0.81 | 1.32 | 0.44 | 0.43 | 0.00 | 0.00 | 4.12 |
| rif_LDR06_ferite_e_caccia | 100 | 0.327 | 0.049 | 0.0% | 0.0% | 0.40 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 3.89 |

