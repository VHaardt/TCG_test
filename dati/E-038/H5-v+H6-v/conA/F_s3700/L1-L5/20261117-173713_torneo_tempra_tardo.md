# Torneo v0.2 — /root/in38/dati/E-038-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in38/dati/E-038-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1785s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 31.3% [30.1–32.6] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 10.96) | 8–11 | ✅ |
| Partite al round 13+ | 29.5% [23.6–36.2] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–1.9] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=85) | 25.9% [17.8–36.1] | 20–35% | ✅ |
| Attacchi con opposizione | 38.2% [36.9–39.5] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 68.0% [66.6–69.4] (con ≥3: 30.3% [28.9–31.7]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 38.2% [36.9–39.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 5.7% [3.8–8.6] (n=368) / 87.9% [83.8–91.1] (n=314) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.1% [12.6–15.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 73.3% [48.0–89.1] (n=15), LDR-01 Risvegliato 65.0% [56.1–72.9] (n=120), LDR-05 Base 33.3% [9.7–70.0] (n=6), LDR-05 Risvegliato 76.9% [69.7–82.8] (n=156) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 29.6% [23.6–36.5] (n=189) | | |
| Attacchi per partita | 25.6 | | |
| Pugno attaccante vuoto / pieno | 49.0% [47.6–50.5] / 13.0% [12.1–14.0] (gemme medie 0.85) | non >90% | |
| Pugno difensore vuoto / pieno | 55.1% [53.0–57.1] / 26.3% [24.6–28.2] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1381, 1: 1706, 2: 1422, 3: 393, 4: 146, 5: 63, 6: 11} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 188, 'crepuscolo': 12} | | |
| G1 vince fra le partite finite al Crepuscolo | 75.0% [46.8–91.1] | | |
| G1 vince fra le partite arrivate al round 15 | 71.4% [45.4–88.3] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 57.1% [32.6–78.6] / 25.0% [7.1–59.1] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 75.0% [40.9–92.9]; 0.0% [0.0–21.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 6, '2-0': 2, '0-0': 2, '2-1': 1, '2-2': 1, '2-3': 1, '1-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=8) | 57.1% [32.6–78.6] / 25.0% [7.1–59.1] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 8}; 25.0% [7.1–59.1] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 75.0% [40.9–92.9] / 62.5% [30.6–86.3]; 2.38 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–32.4] / 87.5% [52.9–97.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 83.3% [43.6–97.0]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.0% [0.3–3.6] / 14.3% [4.0–39.9]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 1, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=9) / turno di G2 (n=7) | 0.0% [0.0–29.9] / 0.0% [0.0–35.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=9) | 0.0% [0.0–29.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 71.4% [45.4–88.3] (7.1% [1.3–31.5]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 5, 'rif_LDR05_scudi_armati': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 71% (n=14) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 46.0% [39.2–52.9], rif_LDR05_scudi_armati 54.0% [47.1–60.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.373 / 0.089 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.087 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.09 (0.00), rif_LDR05_scudi_armati 0.15 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 31.1% [29.9–32.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.80 (127 / 233); 56.7% [55.3–58.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.4% [49.4–51.3]; rif_LDR01_puntata_e_preda 47.5%, rif_LDR05_scudi_armati 53.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.295 (942) / 0.302 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 92 vittorie), LDR-05 R: 18.0 (49%, 108 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 4.24, LDR-01 1.67, ROS-016 1.48, VER-011 0.81, VER-001 0.80, BLU-015 0.68, ROS-018 0.66, BLU-021 0.54, VER-019 0.53, BLU-001 0.51, ROS-005 0.51, ROS-001 0.49 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.85, rif_LDR05_scudi_armati 0.14 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.06, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 16% (n=25), rif_LDR05_scudi_armati 30% (n=60) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.0% [12.1–14.0] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, ROS-020 54%, BLU-010 54%, BLU-021 54%, NEU-013 54%, BLU-008 54%, collante 54%, NEU-009 54%, VER-011 46%, ROS-016 46%, VER-008 46%, caccia 46%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 46.0 [39–53] (200) |
| rif_LDR05_scudi_armati | 54.0 [47–61] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.65 | 0.00 | 1.67 / 0.00 | 0.00 | 0.00 | 4.0 (199) | 13 | G 41%, R 59% | 2.26 | 0.57 |
| rif_LDR05_scudi_armati | 4.05 | 0.00 | 4.24 / 0.00 | 0.00 | 0.76 | 3.6 (200) | 13 | B 47%, R 53% | 1.69 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR01_puntata_e_preda | 1.67 | 0.00 |
| rif_LDR05_scudi_armati | 1.02 | 3.21 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.67/1.50/0.67 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.35/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.37/0.17/0.07 | 0.68/0.16/0.47/0.44 | 0.80/0.53/0.26/0.11 | 0.00/0.33/0.00/0.00 | 0.64/0.00/0.26/0.17 | 0.57/0.20/0.26/0.17 | 0.62/1.48/0.04/0.51 | 0.80/0.98/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.25/0.14/0.10 | 0.26/0.14/0.09/0.20 | 0.00/0.00/0.00/0.00 | 0.68/0.80/0.06/0.54 | 0.66/0.00/0.00/0.00 | 0.72/0.00/0.13/0.04 | 0.61/0.81/0.25/0.18 | 0.64/0.53/0.39/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.06/0.03 | 0.39/0.04/0.06/0.01 | 0.34/0.15/0.17/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.04/0.03 | 0.33/0.47/0.01/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/4.24/1.92/0.92 | 0.58/0.51/0.21/0.16 | 0.47/0.00/0.12/0.08 | 0.55/0.39/0.24/0.13 | 0.56/0.23/0.28/0.20 | 0.56/0.00/0.24/0.14 | 0.56/0.68/0.28/0.27 | 0.00/0.54/0.00/0.00 | 0.00/0.46/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.47/0.32/0.36 | 0.67/0.61/0.24/0.16 | 0.00/0.00/0.00/0.00 | 0.71/0.48/0.21/0.12 | 0.00/0.28/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.23/0.29/0.26 | 0.00/0.00/0.00/0.00 | 0.29/0.33/0.00/0.00 | 0.53/0.36/0.33/0.29 | 0.39/0.24/0.18/0.24 | 0.19/0.04/0.14/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.00/0.09/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.23/0.04/0.06/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.00/0.03/0.03 | 0.29/0.03/0.03/0.03 | 0.32/0.11/0.07/0.10 | 0.35/0.39/0.17/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.06 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.18 | 0.01 | 0.00 | 0.01 | 0.14 | 0.09 | 0.00 | 0.00 | 0.10 | 0.12 | 0.00 | 0.06 | 0.00 | 0.01 | 0.10 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 0.88 | 0.00 | 0.09 | 0.01 | 0.00 | 0.01 | 0.03 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.03 | 0.00 | 0.01 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.18 | 0.14 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.81 | 0.01 | 0.04 | 0.07 | 0.12 | 0.15 | 0.17 | 0.09 | 0.09 | 0.01 | 0.03 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.85 | 0.03 | 0.04 | 0.08 | 0.08 | 0.20 | 0.16 | 0.12 | 0.07 | 0.02 | 0.03 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 1 | 0 | 0 | 1 |
| 6 | 0 | 1 | 0 | 1 |
| 7 | 3 | 4 | 0 | 7 |
| 8 | 9 | 9 | 0 | 18 |
| 9 | 16 | 15 | 0 | 31 |
| 10 | 19 | 14 | 0 | 33 |
| 11 | 18 | 16 | 0 | 34 |
| 12 | 11 | 5 | 0 | 16 |
| 13 | 15 | 12 | 0 | 27 |
| 14 | 4 | 14 | 0 | 18 |
| 15 | 10 | 4 | 0 | 14 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 47.5% | 0.066 | 0.00 | 0.85 | 0.00 | 0.00 | 3.85 | 0.00 | 0.00 | 0.328 |
| rif_LDR05_scudi_armati | 200 | 53.1% | 0.113 | 0.14 | 0.00 | 0.00 | 0.00 | 3.96 | 0.00 | 0.00 | 0.417 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 421 | 0.876 | 0.850 | 0.819 | 0.354 | 2116 | 0.793 | 0.200 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 421 | 0.176 | 0.162 | 0.126 | 0.043 | 2116 | 0.164 | 0.058 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 603 | 0.907 | 0.882 | 0.871 | 0.431 | 1982 | 0.817 | 0.251 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 603 | 0.177 | 0.172 | 0.164 | 0.051 | 1982 | 0.126 | 0.052 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 6.0% | 2.23 | 2.11 | 30.5% | 0.5% | 14.7% | 27.3% | 6.7% | 0.00 | 17.2% | 47.5% | 0.18 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 6.0% | 2.23 | 2.11 | 41.1% | 0.5% | 13.7% | 31.9% | 17.0% | 0.00 | 16.6% | 53.1% | 0.08 | 0.00 |
| Totale | 400 | 6.0% | 2.23 | 2.11 | 35.8% | 0.5% | 14.2% | 29.6% | 12.2% | 0.00 | 16.9% | 50.4% | 0.13 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.391 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.34 |
| rif_LDR05_scudi_armati | 200 | 0.373 | 0.189 | 0.0% | 0.0% | 1.48 | 0.35 | 0.49 | 0.00 | 0.00 | 0.00 | 5.45 |

