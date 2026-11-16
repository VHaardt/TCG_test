# Torneo v0.2 — /home/claude/e034_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e034_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2390s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 46.7% [45.3–48.0] | 30–45% | ❌ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 13.14) | 8–11 | ❌ |
| Partite al round 13+ | 67.5% [60.7–73.6] | ≤12% | ❌ |
| Partite oltre il 15 | 5.0% [2.7–9.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=49) | 30.6% [19.5–44.5] | 20–35% | ✅ |
| Attacchi con opposizione | 34.1% [32.8–35.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 68.2% [66.9–69.4] (con ≥3: 27.4% [26.2–28.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.3% [33.1–35.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 13.5% [10.9–16.6] (n=556) / 77.7% [72.4–82.3] (n=265) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.3% [9.9–12.8] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 48.1% [35.1–61.3] (n=52), LDR-02 Risvegliato 78.0% [68.5–85.3] (n=91), LDR-04 Base 39.1% [22.2–59.2] (n=23), LDR-04 Risvegliato 67.8% [58.8–75.7] (n=115) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 71.5% [64.0–78.0] (n=158) | | |
| Attacchi per partita | 26.5 | | |
| Pugno attaccante vuoto / pieno | 50.9% [49.5–52.3] / 11.9% [11.0–12.8] (gemme medie 0.92) | non >90% | |
| Pugno difensore vuoto / pieno | 62.9% [61.1–64.6] / 18.0% [16.6–19.5] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1755, 1: 2098, 2: 875, 3: 437, 4: 104, 5: 32, 6: 7, 7: 1} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 147, 'crepuscolo': 53} | | |
| G1 vince fra le partite finite al Crepuscolo | 52.8% [39.7–65.6] | | |
| G1 vince fra le partite arrivate al round 15 | 49.3% [37.7–60.9] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 38.8% [28.0–50.8] / 34.6% [19.4–53.8] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 42.3% [25.5–61.1]; 14.9% [8.3–25.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 11, '0-1': 6, '2-3': 6, '2-2': 5, '0-0': 5, '3-2': 4, '1-1': 4, '2-0': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=34) | 50.7% [39.1–62.3] / 32.4% [19.1–49.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 26, 16: 7, 17: 1}; 50.0% [34.1–65.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 70.6% [53.8–83.2] / 35.3% [21.5–52.1]; 2.03 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–10.2] / 91.2% [77.0–97.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=11) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–25.9] / 52.2% [33.0–70.8]; 0.0% [0.0–25.9] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.5% [3.1–9.6] / 16.4% [9.4–27.1]; 100.0% [74.1–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 8, 'perd:pronto': 3, 'vinc:atk': 11} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=20) / turno di G2 (n=16) | 0.0% [0.0–16.1] / 0.0% [0.0–19.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=20) | 0.0% [0.0–16.1] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 52.2% [40.5–63.7] (17.9% [10.6–28.7]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 25, 'rif_LDR02_muro_di_parata': 9} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR04_stanca_e_smonta 49% (n=67) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 50.0% [43.1–56.9], rif_LDR04_stanca_e_smonta 50.0% [43.1–56.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.675 / 0.092 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.089 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.15 (0.00), rif_LDR04_stanca_e_smonta 0.09 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 27.6% [26.4–28.8] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.16 (86 / 145); 62.7% [61.4–64.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 55.2% [54.3–56.1]; rif_LDR02_muro_di_parata 58.2%, rif_LDR04_stanca_e_smonta 52.6% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.1% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.411 (46) / 0.329 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 100 vittorie), LDR-04 B: 12.0 (36%, 100 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 6.46, LDR-02 1.71, BLU-015 1.30, VER-014 1.00, VER-008 0.69, VER-023 0.67, NEW-I04 0.64, BLU-001 0.60, VER-006 0.54, BLU-021 0.47, VER-001 0.43, BLU-011 0.42 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.60, rif_LDR04_stanca_e_smonta 2.44 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.26 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 20% (n=25), rif_LDR04_stanca_e_smonta 42% (n=24) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.9% [11.0–12.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-009 100%, BLU-010 50%, VER-014 50%, caccia 50%, VER-001 50%, VER-023 50%, VER-008 50%, NER-014 50%, NEU-003 50%, NEU-015 50%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 50.0 [43–57] (200) |
| rif_LDR04_stanca_e_smonta | 50.0 [43–57] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.58 | 0.00 | 1.71 / 0.00 | 0.00 | 1.52 | 4.4 (198) | 8 | B 83%, K 17% | 2.51 | 0.00 |
| rif_LDR04_stanca_e_smonta | 5.62 | 2.02 | 6.46 / 0.00 | 0.00 | 0.66 | 4.8 (197) | 10 | B 38%, G 62% | 2.29 | 0.86 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.86/0.51/0.20/0.12 | 0.97/0.00/0.22/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.85/0.00/0.32/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.47/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.36/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.71/2.20/0.88 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.94/0.00/0.07/0.04 | 0.93/0.47/0.09/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.35/0.00/0.00/0.00 | 0.54/0.28/0.04/0.02 | 0.48/0.05/0.13/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.12/0.32/0.36 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.60/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.70/0.18/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.26/0.28/0.14 | 0.41/0.00/0.16/0.04 | 0.80/1.30/0.51/0.27 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.43/0.04/0.17 | 0.69/0.00/0.00/0.00 | 0.84/0.00/0.23/0.07 | 0.00/0.00/0.00/0.00 | 0.39/0.35/0.23/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/6.46/1.91/0.43 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.67/0.04/0.24 | 0.00/0.00/0.00/0.00 | 0.46/0.28/0.06/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.00/0.23/0.03 | 0.39/0.00/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.69/0.01/0.15 | 0.37/0.04/0.01/0.02 | 0.39/0.00/0.09/0.07 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.00/0.00 | 0.80/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.68/0.00/0.00 | 0.00/0.04/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.58 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.67 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.03 | 0.01 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.01 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.23 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.22 | 0.01 | 0.07 | 0.09 | 0.10 | 0.18 | 0.16 | 0.17 | 0.17 | 0.09 | 0.10 | 0.05 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 1.23 | 0.02 | 0.06 | 0.10 | 0.10 | 0.14 | 0.17 | 0.18 | 0.14 | 0.07 | 0.11 | 0.07 | 0.03 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 8 | 3 | 1 | 0 | 4 |
| 9 | 2 | 6 | 0 | 8 |
| 10 | 6 | 8 | 0 | 14 |
| 11 | 13 | 10 | 0 | 23 |
| 12 | 11 | 5 | 0 | 16 |
| 13 | 12 | 17 | 0 | 29 |
| 14 | 16 | 23 | 0 | 39 |
| 15 | 27 | 30 | 0 | 57 |
| 16 | 5 | 4 | 0 | 9 |
| 17 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 58.2% | 0.106 | 1.60 | 0.00 | 0.00 | 0.00 | 3.17 | 0.00 | 0.00 | 0.558 |
| rif_LDR04_stanca_e_smonta | 200 | 52.6% | 0.076 | 2.06 | 0.39 | 0.00 | 0.00 | 1.87 | 0.00 | 0.00 | 0.514 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 700 | 0.993 | 0.957 | 0.914 | 0.224 | 2084 | 0.984 | 0.412 | 0.119 | 0.051 |
| rif_LDR02_muro_di_parata | Cicatrice | 700 | 0.266 | 0.210 | 0.136 | 0.024 | 2084 | 0.219 | 0.086 | 0.019 | 0.007 |
| rif_LDR04_stanca_e_smonta | mano | 352 | 0.909 | 0.866 | 0.790 | 0.131 | 2173 | 0.875 | 0.442 | 0.190 | 0.060 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 352 | 0.170 | 0.111 | 0.077 | 0.034 | 2173 | 0.108 | 0.045 | 0.021 | 0.002 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 26.5% | 2.60 | 2.14 | 23.5% | 0.0% | 28.0% | 34.0% | 9.7% | 0.00 | 12.5% | 58.2% | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 26.5% | 2.60 | 2.14 | 27.8% | 0.0% | 23.7% | 29.4% | 7.1% | 0.00 | 17.2% | 52.6% | 0.07 | 0.00 |
| Totale | 400 | 26.5% | 2.60 | 2.14 | 25.7% | 0.0% | 25.8% | 31.7% | 8.5% | 0.00 | 15.0% | 55.2% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.250 | 0.146 | 0.3% | 0.5% | 0.77 | 0.26 | 1.29 | 1.39 | 0.00 | 0.00 | 4.86 |
| rif_LDR04_stanca_e_smonta | 200 | 0.441 | 0.195 | 0.0% | 0.0% | 0.99 | 0.00 | 0.57 | 0.93 | 0.00 | 0.00 | 4.25 |

