# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1866s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 38.0% [36.7–39.4] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.0–12.0] (media 11.95) | 8–11 | ❌ |
| Partite al round 13+ | 41.5% [34.9–48.4] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=80) | 41.2% [31.1–52.2] | 20–35% | ❌ |
| Attacchi con opposizione | 23.1% [21.9–24.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 60.7% [59.3–62.1] (con ≥3: 20.6% [19.5–21.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.3% [35.0–37.7] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 13.5% [10.7–16.9] (n=467) / 76.0% [71.3–80.1] (n=358) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.9% [13.4–16.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 42.6% [30.3–55.8] (n=54), LDR-04 Risvegliato 64.9% [54.8–73.8] (n=94), LDR-06 Base 33.3% [12.1–64.6] (n=9), LDR-06 Risvegliato 79.8% [73.3–85.0] (n=178) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 44.5% [37.3–52.0] (n=173) | | |
| Attacchi per partita | 25.1 | | |
| Pugno attaccante vuoto / pieno | 52.8% [51.3–54.3] / 12.2% [11.2–13.2] (gemme medie 0.85) | non >90% | |
| Pugno difensore vuoto / pieno | 67.5% [65.7–69.4] / 18.5% [17.1–20.1] (gemme medie 0.22) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1744, 1: 1973, 2: 918, 3: 278, 4: 78, 5: 20, 6: 1} | | |
| Azioni legali per decisione | 5.7 | <60 | ✅ |
| Fine partita | {'colpo_finale': 170, 'crepuscolo': 30} | | |
| G1 vince fra le partite finite al Crepuscolo | 56.7% [39.2–72.6] | | |
| G1 vince fra le partite arrivate al round 15 | 56.2% [39.3–71.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 46.9% [30.9–63.6] / 40.0% [19.8–64.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [15.2–58.3]; 9.4% [3.2–24.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 5, '2-1': 5, '0-1': 4, '2-0': 4, '0-0': 4, '1-1': 2, '1-2': 2, '2-3': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=17) | 53.1% [36.4–69.1] / 41.2% [21.6–64.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15, 17: 1, 16: 1}; 64.7% [41.3–82.7] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 52.9% [31.0–73.8] / 29.4% [13.3–53.1]; 1.94 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–18.4] / 76.5% [52.7–90.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=7) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–35.4] / 50.0% [23.7–76.3]; 0.0% [0.0–35.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.5% [1.7–7.0] / 21.9% [11.0–38.8]; 100.0% [64.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:abil': 1, 'perd:atk': 3, 'perd:pronto': 3, 'vinc:atk': 7} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=1) | 0.0% [0.0–43.4] / 0.0% [0.0–79.3] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 59.4% [42.3–74.5] (12.5% [5.0–28.1]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 9, 'rif_LDR06_ferite_e_caccia': 8} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR06_ferite_e_caccia 56% (n=32) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 64.5% [57.7–70.8], rif_LDR06_ferite_e_caccia 35.5% [29.2–42.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.484 / 0.072 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.072 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.07 (0.00), rif_LDR06_ferite_e_caccia 0.12 (0.02) | |
| M4 | Scontri decisi prima dell'impegno | 35.7% [34.4–37.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.12 (306 / 718); 61.4% [60.1–62.8] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.7% [50.7–52.7]; rif_LDR04_stanca_e_smonta 55.9%, rif_LDR06_ferite_e_caccia 47.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.419 (80) / 0.337 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 12.0 (36%, 129 vittorie), LDR-06 G: 17.0 (49%, 71 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 3.54, LDR-06 3.08, VER-020 2.25, NER-017 1.23, VER-008 0.96, BLU-015 0.91, NEW-I04 0.64, VER-014 0.60, NER-009 0.56, VER-001 0.55, VER-023 0.54, NER-003 0.53 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.71, rif_LDR06_ferite_e_caccia 3.06 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.27, rif_LDR06_ferite_e_caccia 0.27 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 64% (n=22), rif_LDR06_ferite_e_caccia 33% (n=58) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.2% [11.2–13.2] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR06_ferite_e_caccia 0.87; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, caccia 100%, ponte 100%, VER-008 100%, VER-001 100%, BLU-010 64%, NEU-009 64%, VER-023 64%, VER-014 64%, NEU-012 36%, NEW-B06 36%, NEU-001 36%; oltre il 60%: VER-001, VER-008, VER-023 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 64.5 [58–71] (200) |
| rif_LDR06_ferite_e_caccia | 35.5 [29–42] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.07 | 1.67 | 3.54 / 0.00 | 0.00 | 0.65 | 5.4 (199) | 9 | B 41%, G 59% | 2.20 | 0.50 |
| rif_LDR06_ferite_e_caccia | 3.69 | 0.00 | 3.08 / 0.17 | 0.00 | 0.15 | 4.6 (198) | 10 | G 54%, K 46% | 2.47 | 1.33 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.41/0.17/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.18/0.41/0.12 | 0.41/0.00/0.20/0.05 | 0.80/0.91/0.41/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.58/0.04/0.45 | 0.61/0.00/0.00/0.00 | 0.73/0.00/0.21/0.06 | 0.00/0.00/0.00/0.00 | 0.39/0.25/0.28/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.54/2.04/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.54/0.06/0.28 | 0.00/0.00/0.00/0.00 | 0.41/0.24/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.14/0.17/0.03 | 0.41/0.00/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.96/0.01/0.43 | 0.31/0.01/0.02/0.01 | 0.33/0.00/0.12/0.02 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.14/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.64/0.00/0.00 | 0.00/0.04/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.51/0.06/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.47/0.54/0.23 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.08/2.08/0.55 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.41/0.23/0.07 | 0.41/0.28/0.09/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.07/0.19/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.17/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.42/0.04/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.96/0.01/0.36 | 0.41/0.04/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.88/0.41/0.17/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.00/0.00/0.00 | 0.53/0.00/0.00/0.00 | 0.27/0.46/0.07/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.00/0.10/0.04 | 0.23/0.50/0.14/0.07 | 0.47/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.56 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.06 | 0.01 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.72 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.18 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.97 | 0.00 | 0.02 | 0.12 | 0.07 | 0.10 | 0.10 | 0.15 | 0.17 | 0.10 | 0.04 | 0.04 | 0.04 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.85 | 0.00 | 0.02 | 0.06 | 0.06 | 0.04 | 0.10 | 0.13 | 0.12 | 0.12 | 0.09 | 0.05 | 0.04 | 0.02 | 0.00 | 0.87 | 0.10 | 0.12 | 0.11 | 0.12 | 0.12 | 0.07 | 0.09 | 0.04 | 0.04 | 0.04 | 0.01 | 0.01 | 0.02 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR04_stanca_e_smonta | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.49 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 1 | 0 | 1 |
| 7 | 1 | 2 | 0 | 3 |
| 8 | 1 | 5 | 0 | 6 |
| 9 | 10 | 7 | 0 | 17 |
| 10 | 13 | 10 | 0 | 23 |
| 11 | 26 | 14 | 0 | 40 |
| 12 | 12 | 15 | 0 | 27 |
| 13 | 18 | 12 | 0 | 30 |
| 14 | 10 | 11 | 0 | 21 |
| 15 | 16 | 13 | 0 | 29 |
| 16 | 1 | 1 | 0 | 2 |
| 17 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 55.9% | 0.068 | 1.83 | 0.89 | 0.00 | 0.00 | 2.23 | 0.00 | 0.00 | 0.452 |
| rif_LDR06_ferite_e_caccia | 200 | 47.3% | 0.077 | 0.97 | 2.09 | 0.00 | 0.00 | 4.18 | 0.00 | 0.00 | 0.385 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 336 | 0.798 | 0.729 | 0.673 | 0.113 | 2261 | 0.765 | 0.388 | 0.181 | 0.055 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 336 | 0.107 | 0.068 | 0.057 | 0.033 | 2261 | 0.081 | 0.039 | 0.017 | 0.001 |
| rif_LDR06_ferite_e_caccia | mano | 476 | 0.895 | 0.832 | 0.763 | 0.340 | 1939 | 0.759 | 0.243 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 476 | 0.223 | 0.181 | 0.160 | 0.053 | 1939 | 0.171 | 0.057 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 15.0% | 2.27 | 1.66 | 39.1% | 0.0% | 24.5% | 29.0% | 7.1% | 0.00 | 13.9% | 55.9% | 0.02 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 15.0% | 2.27 | 1.66 | 18.5% | 0.0% | 23.0% | 28.2% | 7.4% | 0.00 | 9.4% | 47.3% | 0.03 | 0.00 |
| Totale | 400 | 15.0% | 2.27 | 1.66 | 27.0% | 0.0% | 23.8% | 28.6% | 7.3% | 0.00 | 11.7% | 51.7% | 0.03 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.265 | 0.118 | 0.0% | 0.0% | 0.60 | 0.81 | 0.28 | 0.47 | 0.00 | 0.00 | 4.43 |
| rif_LDR06_ferite_e_caccia | 200 | 0.195 | 0.026 | 0.0% | 0.0% | 0.23 | 0.06 | 0.06 | 0.32 | 0.00 | 0.00 | 4.67 |

