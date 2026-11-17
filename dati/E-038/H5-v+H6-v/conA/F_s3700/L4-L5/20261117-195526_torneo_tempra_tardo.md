# Torneo v0.2 — /home/claude/e038_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e038_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1919s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 37.9% [36.6–39.3] | 30–45% | ✅ |
| Durata mediana (round) | 11.5 [11.0–13.0] (media 11.47) | 8–11 | ❌ |
| Partite al round 13+ | 43.5% [36.8–50.4] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=86) | 23.3% [15.6–33.2] | 20–35% | ✅ |
| Attacchi con opposizione | 34.8% [33.5–36.2] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 68.8% [67.5–70.2] (con ≥3: 30.1% [28.8–31.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.2% [35.8–38.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.8% [4.7–9.6] (n=413) / 80.7% [76.0–84.6] (n=326) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.3% [12.8–16.0] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 29.4% [13.3–53.1] (n=17), LDR-04 Risvegliato 60.8% [51.1–69.7] (n=102), LDR-05 Base 45.5% [21.3–72.0] (n=11), LDR-05 Risvegliato 75.2% [67.9–81.2] (n=161) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 45.8% [38.6–53.1] (n=177) | | |
| Attacchi per partita | 24.7 | | |
| Pugno attaccante vuoto / pieno | 50.5% [49.0–52.0] / 13.4% [12.4–14.4] (gemme medie 0.82) | non >90% | |
| Pugno difensore vuoto / pieno | 65.5% [63.6–67.4] / 18.4% [16.9–20.0] (gemme medie 0.22) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1462, 1: 1882, 2: 996, 3: 380, 4: 182, 5: 38, 6: 8} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 178, 'crepuscolo': 22} | | |
| G1 vince fra le partite finite al Crepuscolo | 77.3% [56.6–89.9] | | |
| G1 vince fra le partite arrivate al round 15 | 67.9% [49.3–82.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 32.1% [17.9–50.7] / 33.3% [12.1–64.6] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 66.7% [35.4–87.9]; 10.7% [3.7–27.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 6, '2-0': 5, '2-1': 3, '2-3': 3, '2-2': 3, '1-1': 2, '3-2': 2, '0-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=12) | 42.9% [26.5–60.9] / 25.0% [8.9–53.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 9, 16: 3}; 25.0% [8.9–53.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 91.7% [64.6–98.5] / 66.7% [39.1–86.2]; 3.08 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–24.3] / 91.7% [64.6–98.5] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 88.9% [56.5–98.0]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.5% [0.5–4.3] / 10.7% [3.7–27.2]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 1, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=14) / turno di G2 (n=16) | 0.0% [0.0–21.5] / 0.0% [0.0–19.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=14) | 0.0% [0.0–21.5] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 67.9% [49.3–82.1] (10.7% [3.7–27.2]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 7, 'rif_LDR05_scudi_armati': 5} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR05_scudi_armati 68% (n=28) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 48.0% [41.2–54.9], rif_LDR05_scudi_armati 52.0% [45.1–58.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.499 / 0.078 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.078 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.07 (0.00), rif_LDR05_scudi_armati 0.12 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 32.1% [30.8–33.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.39 (91 / 186); 61.2% [59.8–62.5] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 55.4% [54.4–56.3]; rif_LDR04_stanca_e_smonta 51.3%, rif_LDR05_scudi_armati 59.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.293 (331) / 0.314 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 12.0 (36%, 96 vittorie), LDR-05 R: 18.0 (49%, 104 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 6.50, LDR-05 3.71, BLU-015 0.97, VER-008 0.91, VER-014 0.72, VER-001 0.67, ROS-018 0.55, ROS-020 0.54, BLU-001 0.53, NEW-I04 0.49, BLU-021 0.42, BLU-023 0.38 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.31, rif_LDR05_scudi_armati 0.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.30, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 13% (n=15), rif_LDR05_scudi_armati 25% (n=71) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.4% [12.4–14.4] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | BLU-010 100%, NEU-009 100%, ponte 100%, collante 100%, BLU-008 52%, BLU-021 52%, ROS-020 52%, NEU-013 52%, VER-014 48%, caccia 48%, VER-008 48%, VER-001 48%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 48.0 [41–55] (200) |
| rif_LDR05_scudi_armati | 52.0 [45–59] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.13 | 2.27 | 6.50 / 0.00 | 0.00 | 0.59 | 4.4 (199) | 10 | B 39%, G 61% | 2.14 | 0.61 |
| rif_LDR05_scudi_armati | 3.79 | 0.00 | 3.71 / 0.00 | 0.00 | 0.89 | 4.4 (197) | 13 | B 47%, R 53% | 1.92 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR04_stanca_e_smonta | 2.27 | 4.24 |
| rif_LDR05_scudi_armati | 0.85 | 2.85 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.69/0.13/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.34/0.40/0.23 | 0.34/0.00/0.21/0.10 | 0.72/1.11/0.38/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.67/0.02/0.48 | 0.72/0.00/0.00/0.00 | 0.56/0.00/0.10/0.05 | 0.00/0.00/0.00/0.00 | 0.40/0.28/0.17/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/6.50/1.79/0.54 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.35/0.02/0.14 | 0.00/0.00/0.00/0.00 | 0.36/0.26/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.00/0.13/0.04 | 0.32/0.00/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.91/0.01/0.35 | 0.28/0.04/0.02/0.04 | 0.34/0.00/0.21/0.11 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.59/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.49/0.00/0.00 | 0.00/0.04/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.71/1.91/0.65 | 0.62/0.35/0.14/0.06 | 0.61/0.00/0.19/0.07 | 0.56/0.29/0.20/0.06 | 0.61/0.28/0.32/0.21 | 0.57/0.00/0.16/0.14 | 0.70/0.83/0.41/0.28 | 0.00/0.42/0.00/0.00 | 0.00/0.38/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.26/0.20/0.15 | 0.67/0.38/0.14/0.12 | 0.00/0.00/0.00/0.00 | 0.69/0.33/0.14/0.07 | 0.00/0.26/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.21/0.35/0.24 | 0.00/0.00/0.00/0.00 | 0.38/0.55/0.00/0.00 | 0.62/0.54/0.35/0.43 | 0.39/0.36/0.27/0.40 | 0.20/0.06/0.12/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.00/0.05/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.04/0.10/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.04/0.01 | 0.33/0.04/0.04/0.03 | 0.28/0.13/0.11/0.10 | 0.31/0.34/0.12/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.43 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.01 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.41 | 0.00 | 0.12 | 0.01 | 0.01 | 0.02 | 0.06 | 0.03 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.03 | 0.00 | 0.01 | 0.00 | 0.00 | 0.19 | 0.00 | 0.00 | 0.31 | 0.28 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.89 | 0.01 | 0.03 | 0.07 | 0.15 | 0.14 | 0.14 | 0.14 | 0.07 | 0.06 | 0.05 | 0.02 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.90 | 0.04 | 0.04 | 0.07 | 0.14 | 0.17 | 0.16 | 0.10 | 0.10 | 0.03 | 0.01 | 0.02 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 1 | 0 | 1 |
| 7 | 7 | 7 | 0 | 14 |
| 8 | 11 | 6 | 0 | 17 |
| 9 | 12 | 11 | 0 | 23 |
| 10 | 12 | 11 | 0 | 23 |
| 11 | 11 | 11 | 0 | 22 |
| 12 | 5 | 8 | 0 | 13 |
| 13 | 13 | 17 | 0 | 30 |
| 14 | 4 | 25 | 0 | 29 |
| 15 | 16 | 9 | 0 | 25 |
| 16 | 3 | 0 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 51.3% | 0.061 | 1.62 | 0.69 | 0.00 | 0.00 | 2.79 | 0.00 | 0.00 | 0.450 |
| rif_LDR05_scudi_armati | 200 | 59.0% | 0.096 | 0.12 | 0.00 | 0.00 | 0.00 | 3.38 | 0.00 | 0.00 | 0.410 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 223 | 0.857 | 0.744 | 0.713 | 0.175 | 2216 | 0.796 | 0.386 | 0.157 | 0.043 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 223 | 0.211 | 0.166 | 0.157 | 0.049 | 2216 | 0.176 | 0.083 | 0.035 | 0.001 |
| rif_LDR05_scudi_armati | mano | 593 | 0.895 | 0.884 | 0.874 | 0.364 | 1916 | 0.846 | 0.244 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 593 | 0.189 | 0.185 | 0.165 | 0.040 | 1916 | 0.121 | 0.044 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 11.0% | 2.08 | 2.25 | 30.2% | 0.0% | 22.5% | 30.2% | 6.9% | 0.00 | 18.4% | 51.3% | 0.06 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 11.0% | 2.08 | 2.25 | 32.5% | 0.0% | 21.2% | 32.0% | 17.5% | 0.00 | 12.0% | 59.0% | 0.10 | 0.00 |
| Totale | 400 | 11.0% | 2.08 | 2.25 | 31.3% | 0.0% | 21.8% | 31.1% | 11.7% | 0.00 | 15.0% | 55.4% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.410 | 0.198 | 0.0% | 0.0% | 1.27 | 0.00 | 0.44 | 0.04 | 0.00 | 0.00 | 3.85 |
| rif_LDR05_scudi_armati | 200 | 0.289 | 0.137 | 0.0% | 0.0% | 0.87 | 0.34 | 0.64 | 0.91 | 0.00 | 0.00 | 5.34 |

