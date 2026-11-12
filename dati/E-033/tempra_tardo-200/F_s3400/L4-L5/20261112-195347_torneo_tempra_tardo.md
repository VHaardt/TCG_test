# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1080s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 39.2% [37.9–40.5] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [12.0–13.0] (media 12.24) | 8–11 | ❌ |
| Partite al round 13+ | 47.0% [40.2–53.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=62) | 24.2% [15.2–36.2] | 20–35% | ✅ |
| Attacchi con opposizione | 35.8% [34.6–37.1] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 70.3% [69.0–71.6] (con ≥3: 30.7% [29.4–32.0]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.8% [33.6–36.1] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 13.5% [10.7–16.9] (n=459) / 85.9% [80.9–89.8] (n=234) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.6% [9.3–12.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 33.3% [16.3–56.3] (n=18), LDR-04 Risvegliato 66.3% [56.5–74.9] (n=98), LDR-05 Base 61.4% [46.6–74.3] (n=44), LDR-05 Risvegliato 81.6% [73.0–87.9] (n=103) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 56.6% [48.5–64.5] (n=143) | | |
| Attacchi per partita | 27.1 | | |
| Pugno attaccante vuoto / pieno | 51.6% [50.2–53.0] / 12.0% [11.1–12.9] (gemme medie 0.83) | non >90% | |
| Pugno difensore vuoto / pieno | 59.8% [57.9–61.7] / 23.3% [21.7–25.0] (gemme medie 0.24) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1750, 1: 1795, 2: 1156, 3: 469, 4: 198, 5: 47, 6: 15} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'crepuscolo': 35, 'colpo_finale': 165} | | |
| G1 vince fra le partite finite al Crepuscolo | 57.1% [40.9–72.0] | | |
| G1 vince fra le partite arrivate al round 15 | 55.1% [41.3–68.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 30.6% [19.5–44.5] / 73.3% [48.0–89.1] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 20.0% [7.0–45.2]; 6.1% [2.1–16.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 10, '0-0': 7, '2-0': 5, '2-1': 4, '1-1': 4, '1-0': 3, '3-0': 3, '4-2': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=16) | 32.7% [21.2–46.6] / 68.8% [44.4–85.8] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15, 16: 1}; 75.0% [50.5–89.8] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 43.8% [23.1–66.8] / 18.8% [6.6–43.0]; 1.69 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–19.4] / 68.8% [44.4–85.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=11) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–25.9] / 60.0% [23.1–88.2]; 0.0% [0.0–25.9] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.5% [3.1–9.6] / 22.4% [13.0–35.9]; 100.0% [74.1–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 5, 'perd:pronto': 5, 'perd:rim': 1, 'vinc:atk': 11} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=19) / turno di G2 (n=15) | 0.0% [0.0–16.8] / 0.0% [0.0–20.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=19) | 0.0% [0.0–16.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 44.9% [31.9–58.7] (8.2% [3.2–19.2]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 10, 'rif_LDR05_scudi_armati': 6} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR05_scudi_armati 55% (n=49) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 38.0% [31.6–44.9], rif_LDR05_scudi_armati 62.0% [55.1–68.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.349 / 0.087 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.086 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.12 (0.00), rif_LDR05_scudi_armati 0.18 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 31.8% [30.6–33.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.41 (101 / 180); 60.6% [59.3–61.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 53.8% [52.9–54.7]; rif_LDR04_stanca_e_smonta 49.7%, rif_LDR05_scudi_armati 57.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.283 (365) / 0.315 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 14.0 (40%, 76 vittorie), LDR-05 R: 18.0 (49%, 124 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 7.11, LDR-05 4.03, BLU-015 1.10, VER-008 0.85, VER-014 0.84, ROS-018 0.74, VER-001 0.62, ROS-021 0.59, BLU-001 0.57, BLU-023 0.57, BLU-008 0.55, NEU-013 0.47 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.94, rif_LDR05_scudi_armati 0.16 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.30, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 15% (n=27), rif_LDR05_scudi_armati 31% (n=35) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.0% [11.1–12.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | NEU-009 100%, ponte 100%, BLU-010 100%, collante 100%, NEU-013 62%, BLU-008 62%, ROS-020 62%, BLU-021 62%, VER-008 38%, VER-014 38%, VER-023 38%, caccia 38%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 38.0 [32–45] (200) |
| rif_LDR05_scudi_armati | 62.0 [55–68] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.49 | 2.60 | 7.11 / 0.00 | 0.00 | 0.57 | 4.6 (197) | 10 | B 42%, G 58% | 2.19 | 0.47 |
| rif_LDR05_scudi_armati | 4.15 | 0.00 | 4.03 / 0.00 | 0.00 | 0.97 | 4.8 (199) | 13 | B 47%, R 53% | 1.84 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.83/0.20/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.27/0.37/0.21 | 0.34/0.00/0.15/0.05 | 0.77/1.04/0.40/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.75/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.62/0.02/0.38 | 0.74/0.00/0.00/0.00 | 0.67/0.00/0.14/0.07 | 0.00/0.00/0.00/0.00 | 0.41/0.24/0.21/0.20 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/7.11/1.78/0.69 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.23/0.45/0.03/0.20 | 0.00/0.00/0.00/0.00 | 0.40/0.33/0.06/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.00/0.14/0.10 | 0.28/0.00/0.03/0.01 | 0.30/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.85/0.01/0.32 | 0.37/0.04/0.06/0.02 | 0.40/0.00/0.14/0.09 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/4.03/1.69/0.55 | 0.65/0.32/0.18/0.13 | 0.69/0.00/0.24/0.10 | 0.66/0.55/0.28/0.23 | 0.58/0.29/0.26/0.23 | 0.60/0.00/0.28/0.18 | 0.80/1.17/0.39/0.50 | 0.00/0.38/0.00/0.00 | 0.00/0.39/0.00/0.00 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.47/0.27/0.28 | 0.76/0.43/0.17/0.10 | 0.00/0.00/0.00/0.00 | 0.70/0.35/0.17/0.05 | 0.00/0.26/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.61/0.20/0.27/0.23 | 0.00/0.00/0.00/0.00 | 0.47/0.74/0.00/0.00 | 0.65/0.44/0.29/0.38 | 0.53/0.59/0.38/0.54 | 0.24/0.08/0.12/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.75/0.00/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.05/0.07/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.04/0.01 | 0.42/0.04/0.02/0.01 | 0.33/0.14/0.14/0.12 | 0.37/0.33/0.14/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.51 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.03 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.18 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.39 | 0.00 | 0.07 | 0.04 | 0.01 | 0.03 | 0.02 | 0.03 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.17 | 0.45 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.03 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.97 | 0.01 | 0.04 | 0.07 | 0.10 | 0.11 | 0.13 | 0.14 | 0.18 | 0.06 | 0.06 | 0.05 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.76 | 0.01 | 0.04 | 0.06 | 0.07 | 0.10 | 0.12 | 0.12 | 0.10 | 0.06 | 0.03 | 0.03 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 8 | 6 | 2 | 0 | 8 |
| 9 | 13 | 4 | 0 | 17 |
| 10 | 15 | 12 | 0 | 27 |
| 11 | 15 | 16 | 0 | 31 |
| 12 | 12 | 11 | 0 | 23 |
| 13 | 9 | 15 | 0 | 24 |
| 14 | 5 | 16 | 0 | 21 |
| 15 | 24 | 22 | 0 | 46 |
| 16 | 3 | 0 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 49.7% | 0.080 | 2.34 | 0.59 | 0.00 | 0.00 | 2.87 | 0.00 | 0.00 | 0.310 |
| rif_LDR05_scudi_armati | 200 | 57.3% | 0.096 | 0.16 | 0.00 | 0.00 | 0.00 | 4.20 | 0.00 | 0.00 | 0.393 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 429 | 0.865 | 0.797 | 0.732 | 0.483 | 2473 | 0.745 | 0.190 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 429 | 0.212 | 0.184 | 0.135 | 0.056 | 2473 | 0.169 | 0.055 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 573 | 0.876 | 0.873 | 0.871 | 0.360 | 1955 | 0.792 | 0.235 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 573 | 0.176 | 0.171 | 0.164 | 0.065 | 1955 | 0.108 | 0.037 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 17.5% | 2.54 | 1.77 | 22.1% | 0.0% | 23.5% | 28.1% | 7.5% | 0.00 | 21.0% | 49.7% | 0.02 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 17.5% | 2.54 | 1.77 | 31.4% | 0.0% | 22.2% | 31.9% | 14.9% | 0.00 | 11.2% | 57.3% | 0.07 | 0.00 |
| Totale | 400 | 17.5% | 2.54 | 1.77 | 25.5% | 0.0% | 22.8% | 30.0% | 10.7% | 0.00 | 15.7% | 53.8% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

