# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 1658s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 42.4% [40.5–44.3] | 30–45% | ✅ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 12.92) | 8–11 | ❌ |
| Partite al round 13+ | 64.0% [54.2–72.7] | ≤12% | ❌ |
| Partite oltre il 15 | 7.0% [3.4–13.7] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=28) | 32.1% [17.9–50.7] | 20–35% | ✅ |
| Attacchi con opposizione | 38.9% [37.1–40.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 65.5% [63.6–67.4] (con ≥3: 25.0% [23.3–26.7]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.5% [32.7–36.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 9.0% [5.9–13.6] (n=221) / 87.6% [80.3–92.5] (n=113) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.9% [9.0–13.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 66.7% [20.8–93.9] (n=3), LDR-02 Risvegliato 84.5% [73.1–91.6] (n=58), LDR-05 Base 52.9% [31.0–73.8] (n=17), LDR-05 Risvegliato 78.0% [63.3–88.0] (n=41) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 69.8% [59.4–78.5] (n=86) | | |
| Attacchi per partita | 26.4 | | |
| Pugno attaccante vuoto / pieno | 49.1% [47.2–51.1] / 10.3% [9.1–11.5] (gemme medie 1.04) | non >90% | |
| Pugno difensore vuoto / pieno | 47.2% [44.6–49.9] / 25.3% [23.0–27.6] (gemme medie 0.38) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 846, 1: 912, 2: 561, 3: 204, 4: 86, 5: 29, 6: 2} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 78, 'crepuscolo': 22} | | |
| G1 vince fra le partite finite al Crepuscolo | 54.5% [34.7–73.1] | | |
| G1 vince fra le partite arrivate al round 15 | 60.0% [43.6–74.4] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 20.0% [10.0–35.9] / 57.1% [25.0–84.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 14.3% [2.6–51.3]; 20.0% [10.0–35.9] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 7, '3-2': 6, '2-3': 4, '2-1': 3, '1-1': 3, '0-2': 2, '0-1': 2, '1-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=12) | 34.3% [20.8–50.8] / 41.7% [19.3–68.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 7, 16: 5}; 58.3% [32.0–80.7] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 58.3% [32.0–80.7] / 33.3% [13.8–60.9]; 2.17 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–24.3] / 91.7% [64.6–98.5] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 57.1% [25.0–84.2]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.0% [2.2–11.2] / 14.3% [6.3–29.4]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 3, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=10) / turno di G2 (n=4) | 0.0% [0.0–27.8] / 0.0% [0.0–49.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=10) | 0.0% [0.0–27.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 40.0% [25.6–56.4] (8.6% [3.0–22.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 7, 'rif_LDR02_muro_di_parata': 5} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 60% (n=35) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 40.0% [30.9–49.8], rif_LDR05_scudi_armati 60.0% [50.2–69.1]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.495 / 0.091 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.086 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.19 (0.00), rif_LDR05_scudi_armati 0.15 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 22.6% [21.0–24.2] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 61.1% [59.2–62.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.6% [49.3–52.0]; rif_LDR02_muro_di_parata 45.7%, rif_LDR05_scudi_armati 54.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.295 (241) / 0.335 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 40 vittorie), LDR-05 R: 18.0 (49%, 60 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.89, LDR-02 1.55, BLU-015 0.89, ROS-020 0.74, ROS-018 0.68, BLU-001 0.67, ROS-021 0.57, BLU-008 0.53, ROS-001 0.45, NEU-013 0.37, BLU-023 0.36, ROS-005 0.35 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.70, rif_LDR05_scudi_armati 0.15 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 22% (n=18), rif_LDR05_scudi_armati 50% (n=10) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.3% [9.1–11.5] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, BLU-021 100%, ponte 100%, NEU-009 100%, BLU-008 60%, NEU-013 60%, BLU-010 60%, ROS-020 60%, NEU-003 40%, 11.1 40%, BLU-022 40%, NER-014 40%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 40.0 [31–50] (100) |
| rif_LDR05_scudi_armati | 60.0 [50–69] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.75 | 0.00 | 1.55 / 0.00 | 0.00 | 1.62 | 4.9 (100) | 8 | B 77%, K 23% | 2.84 | 0.00 |
| rif_LDR05_scudi_armati | 4.46 | 0.00 | 3.89 / 0.00 | 0.00 | 0.90 | 4.3 (100) | 13 | B 48%, R 52% | 2.14 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.93/0.22/0.23 | 0.93/0.00/0.27/0.31 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.00/0.29/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.19/0.00/0.00 | 0.00/0.21/0.00/0.00 | 0.00/0.46/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.55/1.61/1.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.11/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.16/0.16/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.89/1.73/0.40 | 0.66/0.41/0.08/0.07 | 0.80/0.00/0.18/0.06 | 0.74/0.53/0.29/0.08 | 0.67/0.18/0.16/0.10 | 0.79/0.00/0.17/0.16 | 0.72/0.89/0.29/0.17 | 0.00/0.47/0.00/0.00 | 0.00/0.51/0.00/0.00 | 0.00/0.16/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.37/0.22/0.11 | 0.83/0.45/0.20/0.04 | 0.00/0.00/0.00/0.00 | 0.82/0.35/0.08/0.03 | 0.00/0.25/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.21/0.29/0.16 | 0.00/0.00/0.00/0.00 | 0.37/0.68/0.00/0.00 | 0.82/0.74/0.46/0.26 | 0.50/0.57/0.40/0.19 | 0.25/0.14/0.09/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.00/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.08/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.01/0.00 | 0.38/0.05/0.02/0.02 | 0.29/0.07/0.14/0.03 | 0.38/0.33/0.11/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.57 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.42 | 0.00 | 0.13 | 0.01 | 0.02 | 0.05 | 0.06 | 0.01 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.35 | 0.36 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 1.36 | 0.00 | 0.06 | 0.07 | 0.17 | 0.22 | 0.18 | 0.15 | 0.12 | 0.06 | 0.11 | 0.11 | 0.07 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 1.06 | 0.02 | 0.02 | 0.07 | 0.11 | 0.09 | 0.13 | 0.17 | 0.09 | 0.09 | 0.08 | 0.09 | 0.07 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 8 | 4 | 2 | 0 | 6 |
| 9 | 4 | 3 | 0 | 7 |
| 10 | 5 | 0 | 0 | 5 |
| 11 | 8 | 2 | 0 | 10 |
| 12 | 6 | 2 | 0 | 8 |
| 13 | 7 | 6 | 0 | 13 |
| 14 | 9 | 7 | 0 | 16 |
| 15 | 15 | 13 | 0 | 28 |
| 16 | 6 | 1 | 0 | 7 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 45.7% | 0.072 | 1.70 | 0.00 | 0.00 | 0.00 | 3.96 | 0.00 | 0.00 | 0.592 |
| rif_LDR05_scudi_armati | 100 | 54.0% | 0.112 | 0.15 | 0.00 | 0.00 | 0.00 | 2.14 | 0.00 | 0.00 | 0.385 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 414 | 1.000 | 1.000 | 0.998 | 0.198 | 988 | 1.000 | 0.421 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 414 | 0.481 | 0.442 | 0.399 | 0.046 | 988 | 0.353 | 0.151 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 313 | 0.911 | 0.898 | 0.872 | 0.396 | 925 | 0.805 | 0.179 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 313 | 0.208 | 0.198 | 0.195 | 0.048 | 925 | 0.158 | 0.048 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 22.0% | 2.61 | 1.54 | 26.2% | 0.0% | 32.7% | 43.4% | 16.5% | 0.00 | 19.4% | 45.7% | 0.08 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 22.0% | 2.61 | 1.54 | 43.9% | 0.0% | 18.3% | 31.2% | 15.3% | 0.00 | 17.4% | 54.0% | 0.08 | 0.00 |
| Totale | 200 | 22.0% | 2.61 | 1.54 | 33.3% | 0.0% | 25.5% | 37.3% | 16.1% | 0.00 | 18.2% | 50.6% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

