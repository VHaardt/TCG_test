# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2723s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 41.3% [40.0–42.7] | 30–45% | ✅ |
| Durata mediana (round) | 14.0 [14.0–14.5] (media 13.32) | 8–11 | ❌ |
| Partite al round 13+ | 71.0% [64.4–76.8] | ≤12% | ❌ |
| Partite oltre il 15 | 10.0% [6.6–14.9] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=48) | 25.0% [14.9–38.8] | 20–35% | ✅ |
| Attacchi con opposizione | 44.8% [43.4–46.2] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 74.6% [73.4–75.8] (con ≥3: 38.0% [36.6–39.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.2% [32.9–35.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 12.9% [10.1–16.4] (n=434) / 89.4% [84.6–92.8] (n=217) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.0% [9.7–12.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 50.0% [33.2–66.8] (n=30), LDR-02 Risvegliato 70.6% [61.1–78.6] (n=102), LDR-05 Base 57.7% [38.9–74.5] (n=26), LDR-05 Risvegliato 70.7% [60.7–79.0] (n=92) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 74.7% [67.7–80.6] (n=170) | | |
| Attacchi per partita | 25.7 | | |
| Pugno attaccante vuoto / pieno | 50.6% [49.2–52.0] / 10.7% [9.8–11.6] (gemme medie 0.97) | non >90% | |
| Pugno difensore vuoto / pieno | 50.5% [48.6–52.5] / 25.8% [24.2–27.6] (gemme medie 0.33) | non >90% | |
| Reazioni per scontro | 0.12 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1731, 1: 1762, 2: 1001, 3: 401, 4: 164, 5: 71, 6: 6, 7: 1} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 138, 'crepuscolo': 62} | | |
| G1 vince fra le partite finite al Crepuscolo | 66.1% [53.7–76.7] | | |
| G1 vince fra le partite arrivate al round 15 | 54.5% [44.2–64.5] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 25.0% [17.1–35.0] / 40.9% [23.3–61.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [30.7–69.3]; 22.7% [15.2–32.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 11, '3-2': 10, '2-3': 9, '2-2': 9, '0-0': 6, '2-1': 5, '3-1': 4, '3-3': 4} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=33) | 37.5% [28.1–47.9] / 27.3% [15.1–44.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 11, 15: 22}; 39.4% [24.7–56.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 81.8% [65.6–91.4] / 57.6% [40.8–72.8]; 2.73 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–10.4] / 93.9% [80.4–98.3] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=9) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–29.9] / 79.2% [59.5–90.8]; 0.0% [0.0–29.9] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.5% [2.4–8.3] / 10.2% [5.5–18.3]; 100.0% [70.1–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 7, 'perd:pronto': 2, 'vinc:atk': 9} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=26) / turno di G2 (n=28) | 0.0% [0.0–12.9] / 0.0% [0.0–12.1] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=26) | 0.0% [0.0–12.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 56.8% [46.4–66.7] (13.6% [8.0–22.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 18, 'rif_LDR05_scudi_armati': 15} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 55% (n=88) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 47.5% [40.7–54.4], rif_LDR05_scudi_armati 52.5% [45.6–59.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.535 / 0.117 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.113 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.12 (0.00), rif_LDR05_scudi_armati 0.15 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 26.2% [25.0–27.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 55.2% [53.8–56.6] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 58.8% [58.0–59.7]; rif_LDR02_muro_di_parata 58.1%, rif_LDR05_scudi_armati 59.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.3% [0.1–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.289 (492) / 0.317 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 95 vittorie), LDR-05 R: 18.0 (49%, 105 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.37, LDR-02 1.55, BLU-015 0.98, BLU-005 0.80, BLU-001 0.71, ROS-020 0.69, NEW-I04 0.67, ROS-018 0.60, ROS-021 0.58, BLU-021 0.51, BLU-023 0.49, BLU-008 0.47 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.51, rif_LDR05_scudi_armati 0.10 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 20% (n=25), rif_LDR05_scudi_armati 30% (n=23) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.7% [9.8–11.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, NEU-009 100%, collante 100%, BLU-021 100%, ROS-020 52%, NEU-013 52%, BLU-010 52%, BLU-008 52%, NEU-015 48%, RS 48%, NEU-003 48%, NER-014 48%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 47.5 [41–54] (200) |
| rif_LDR05_scudi_armati | 52.5 [46–59] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.34 | 0.00 | 1.55 / 0.00 | 0.00 | 1.25 | 4.5 (196) | 8 | B 84%, K 16% | 1.98 | 0.00 |
| rif_LDR05_scudi_armati | 4.08 | 0.00 | 3.37 / 0.00 | 0.00 | 0.78 | 4.6 (199) | 13 | B 47%, R 53% | 1.83 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.89/0.25/0.15 | 0.80/0.00/0.33/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.00/0.36/0.25 | 0.00/0.00/0.00/0.00 | 0.00/0.56/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.55/1.77/1.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.98/0.00/0.10/0.06 | 0.92/0.80/0.10/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.38/0.00/0.00/0.00 | 0.46/0.43/0.04/0.05 | 0.39/0.00/0.10/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.15/0.09/0.27 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.67/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.37/1.48/0.54 | 0.64/0.54/0.10/0.05 | 0.70/0.00/0.14/0.06 | 0.68/0.47/0.20/0.12 | 0.65/0.23/0.23/0.12 | 0.65/0.00/0.18/0.09 | 0.73/0.98/0.28/0.26 | 0.00/0.47/0.00/0.00 | 0.00/0.49/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.36/0.20/0.15 | 0.81/0.39/0.19/0.06 | 0.00/0.00/0.00/0.00 | 0.77/0.41/0.12/0.06 | 0.00/0.28/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.16/0.25/0.12 | 0.00/0.00/0.00/0.00 | 0.34/0.60/0.00/0.00 | 0.69/0.69/0.41/0.35 | 0.50/0.58/0.23/0.31 | 0.24/0.10/0.11/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.82/0.00/0.07/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.00/0.09/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.04/0.01 | 0.46/0.07/0.06/0.01 | 0.38/0.12/0.09/0.07 | 0.34/0.35/0.12/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.39 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.28 | 0.00 | 0.12 | 0.01 | 0.01 | 0.01 | 0.03 | 0.01 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.00 | 0.02 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.27 | 0.34 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.02 | 0.03 | 0.04 | 0.09 | 0.14 | 0.14 | 0.19 | 0.13 | 0.12 | 0.04 | 0.08 | 0.02 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.88 | 0.01 | 0.05 | 0.09 | 0.12 | 0.12 | 0.12 | 0.12 | 0.07 | 0.04 | 0.03 | 0.06 | 0.04 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 2 | 0 | 2 |
| 8 | 1 | 4 | 0 | 5 |
| 9 | 7 | 4 | 0 | 11 |
| 10 | 4 | 6 | 0 | 10 |
| 11 | 15 | 6 | 0 | 21 |
| 12 | 5 | 4 | 0 | 9 |
| 13 | 13 | 10 | 0 | 23 |
| 14 | 6 | 25 | 0 | 31 |
| 15 | 33 | 35 | 0 | 68 |
| 16 | 15 | 5 | 0 | 20 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 58.1% | 0.123 | 1.51 | 0.00 | 0.00 | 0.00 | 3.52 | 0.00 | 0.00 | 0.559 |
| rif_LDR05_scudi_armati | 200 | 59.5% | 0.110 | 0.10 | 0.00 | 0.00 | 0.00 | 2.76 | 0.00 | 0.00 | 0.395 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 612 | 0.993 | 0.923 | 0.873 | 0.281 | 2025 | 0.986 | 0.429 | 0.172 | 0.063 |
| rif_LDR02_muro_di_parata | Cicatrice | 612 | 0.319 | 0.261 | 0.193 | 0.031 | 2025 | 0.276 | 0.094 | 0.025 | 0.003 |
| rif_LDR05_scudi_armati | mano | 626 | 0.911 | 0.895 | 0.885 | 0.391 | 1874 | 0.814 | 0.204 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 626 | 0.222 | 0.204 | 0.185 | 0.048 | 1874 | 0.178 | 0.060 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 31.0% | 2.79 | 1.88 | 25.5% | 0.0% | 21.0% | 37.8% | 13.3% | 0.00 | 16.8% | 58.1% | 0.01 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 31.0% | 2.79 | 1.88 | 33.0% | 0.0% | 18.3% | 36.1% | 18.4% | 0.00 | 15.2% | 59.5% | 0.13 | 0.00 |
| Totale | 400 | 31.0% | 2.79 | 1.88 | 29.1% | 0.0% | 19.7% | 36.9% | 15.5% | 0.00 | 16.0% | 58.8% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.436 | 0.284 | 0.6% | 0.8% | 1.68 | 0.00 | 1.08 | 0.04 | 0.00 | 0.00 | 4.22 |
| rif_LDR05_scudi_armati | 200 | 0.460 | 0.229 | 0.0% | 0.0% | 1.64 | 0.00 | 0.97 | 0.83 | 0.00 | 0.00 | 4.57 |

