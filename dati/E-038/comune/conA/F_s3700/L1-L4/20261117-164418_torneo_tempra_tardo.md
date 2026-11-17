# Torneo v0.2 — /root/in38/dati/E-038-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in38/dati/E-038-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2464s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 34.1% [32.9–35.4] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [11.0–11.0] (media 11.28) | 8–11 | ✅ |
| Partite al round 13+ | 31.5% [25.5–38.2] | ≤12% | ❌ |
| Partite oltre il 15 | 0.5% [0.1–2.8] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=73) | 30.1% [20.8–41.4] | 20–35% | ✅ |
| Attacchi con opposizione | 30.6% [29.4–31.9] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 66.5% [65.1–67.9] (con ≥3: 26.0% [24.7–27.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 38.7% [37.3–40.0] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 5.1% [3.5–7.3] (n=534) / 78.2% [73.3–82.5] (n=308) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.9% [10.5–13.3] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 55.6% [33.7–75.4] (n=18), LDR-01 Risvegliato 60.0% [50.4–68.9] (n=105), LDR-04 Base 44.4% [18.9–73.3] (n=9), LDR-04 Risvegliato 68.4% [60.2–75.6] (n=136) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 34.1% [27.4–41.5] (n=170) | | |
| Attacchi per partita | 26.3 | | |
| Pugno attaccante vuoto / pieno | 45.9% [44.4–47.3] / 14.4% [13.4–15.4] (gemme medie 0.90) | non >90% | |
| Pugno difensore vuoto / pieno | 68.9% [67.1–70.7] / 17.6% [16.2–19.2] (gemme medie 0.20) | non >90% | |
| Reazioni per scontro | 0.06 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1576, 1: 1849, 2: 1136, 3: 430, 4: 200, 5: 53, 6: 13} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 183, 'crepuscolo': 17} | | |
| G1 vince fra le partite finite al Crepuscolo | 47.1% [26.2–69.0] | | |
| G1 vince fra le partite arrivate al round 15 | 39.1% [22.2–59.2] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 34.8% [18.8–55.1] / 62.5% [30.6–86.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 25.0% [7.1–59.1]; 4.3% [0.8–21.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 4, '2-1': 3, '1-1': 3, '2-0': 2, '0-0': 2, '1-0': 2, '1-4': 1, '2-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=8) | 34.8% [18.8–55.1] / 62.5% [30.6–86.3] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 8}; 75.0% [40.9–92.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 37.5% [13.7–69.4] / 25.0% [7.1–59.1]; 1.62 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–32.4] / 75.0% [40.9–92.9] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 66.7% [20.8–93.9]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.5% [1.1–5.7] / 21.7% [9.7–41.9]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 2, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=10) / turno di G2 (n=14) | 0.0% [0.0–27.8] / 0.0% [0.0–21.5] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=10) | 0.0% [0.0–27.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 43.5% [25.6–63.2] (8.7% [2.4–26.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 5, 'rif_LDR04_stanca_e_smonta': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR04_stanca_e_smonta 39% (n=23) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 55.0% [48.1–61.7], rif_LDR04_stanca_e_smonta 45.0% [38.3–51.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.476 / 0.065 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.065 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.10 (0.00), rif_LDR04_stanca_e_smonta 0.09 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 30.0% [28.8–31.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.08 (210 / 405); 61.1% [59.8–62.4] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.5% [49.5–51.5]; rif_LDR01_puntata_e_preda 51.1%, rif_LDR04_stanca_e_smonta 50.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.336 (462) / 0.317 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 110 vittorie), LDR-04 B: 12.0 (36%, 90 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 6.82, LDR-01 1.86, ROS-016 1.53, ROS-018 1.16, BLU-015 1.16, VER-011 0.78, VER-008 0.71, VER-014 0.65, NEW-I04 0.62, VER-001 0.58, ROS-001 0.55, BLU-001 0.55 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.74, rif_LDR04_stanca_e_smonta 2.49 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.03, rif_LDR04_stanca_e_smonta 0.27 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 33% (n=27), rif_LDR04_stanca_e_smonta 28% (n=46) | 20–35% |
| M13 | Pugno d'attacco pieno | 14.4% [13.4–15.4] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-008 100%, VER-001 100%, caccia 100%, ponte 100%, ROS-016 55%, VER-011 55%, collante 45%, VER-014 45%, BLU-010 45%, VER-023 45%, NEU-009 45%; oltre il 60%: VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 55.0 [48–62] (200) |
| rif_LDR04_stanca_e_smonta | 45.0 [38–52] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.81 | 0.00 | 1.86 / 0.00 | 0.00 | 0.00 | 3.9 (200) | 13 | G 41%, R 59% | 2.38 | 0.43 |
| rif_LDR04_stanca_e_smonta | 5.16 | 2.08 | 6.82 / 0.00 | 0.00 | 0.85 | 4.1 (199) | 10 | B 39%, G 61% | 1.92 | 0.79 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR01_puntata_e_preda | 1.86 | 0.00 |
| rif_LDR04_stanca_e_smonta | 2.08 | 4.75 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.86/2.12/0.46 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.34/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.55/0.23/0.12 | 0.75/0.14/0.66/0.43 | 0.77/0.34/0.14/0.06 | 0.00/0.35/0.00/0.00 | 0.69/0.00/0.24/0.14 | 0.69/0.34/0.31/0.18 | 0.70/1.53/0.07/0.64 | 0.75/1.16/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.51/0.41/0.28/0.30 | 0.24/0.07/0.20/0.20 | 0.00/0.00/0.00/0.00 | 0.69/0.49/0.02/0.29 | 0.68/0.00/0.00/0.00 | 0.68/0.00/0.13/0.04 | 0.71/0.78/0.28/0.16 | 0.77/0.64/0.41/0.40 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.04/0.01 | 0.44/0.04/0.04/0.01 | 0.38/0.08/0.21/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.06/0.03 | 0.34/0.41/0.01/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.55/0.20/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.27/0.30/0.21 | 0.39/0.00/0.28/0.15 | 0.69/1.16/0.47/0.42 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.68/0.08/0.53 | 0.74/0.00/0.00/0.00 | 0.62/0.00/0.14/0.09 | 0.00/0.00/0.00/0.00 | 0.33/0.25/0.29/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/6.82/2.09/0.59 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.55/0.06/0.28 | 0.00/0.00/0.00/0.00 | 0.39/0.27/0.04/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.06/0.25/0.10 | 0.34/0.00/0.02/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/1.01/0.01/0.49 | 0.36/0.04/0.05/0.03 | 0.33/0.00/0.17/0.09 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.62/0.00/0.00 | 0.00/0.03/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.41 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.24 | 0.01 | 0.00 | 0.01 | 0.27 | 0.17 | 0.00 | 0.00 | 0.24 | 0.08 | 0.00 | 0.01 | 0.00 | 0.00 | 0.07 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.64 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.02 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.24 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.96 | 0.01 | 0.03 | 0.10 | 0.10 | 0.12 | 0.14 | 0.17 | 0.13 | 0.09 | 0.04 | 0.04 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 1.15 | 0.01 | 0.05 | 0.09 | 0.12 | 0.18 | 0.20 | 0.17 | 0.13 | 0.09 | 0.06 | 0.03 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 7 | 0 | 4 | 0 | 4 |
| 8 | 4 | 9 | 0 | 13 |
| 9 | 12 | 17 | 0 | 29 |
| 10 | 21 | 13 | 0 | 34 |
| 11 | 22 | 15 | 0 | 37 |
| 12 | 13 | 6 | 0 | 19 |
| 13 | 18 | 6 | 0 | 24 |
| 14 | 3 | 13 | 0 | 16 |
| 15 | 8 | 14 | 0 | 22 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 51.1% | 0.064 | 0.00 | 0.74 | 0.00 | 0.00 | 3.67 | 0.00 | 0.00 | 0.356 |
| rif_LDR04_stanca_e_smonta | 200 | 50.0% | 0.066 | 1.60 | 0.89 | 0.00 | 0.00 | 3.48 | 0.00 | 0.00 | 0.484 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 520 | 0.888 | 0.840 | 0.794 | 0.292 | 2187 | 0.800 | 0.222 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 520 | 0.225 | 0.206 | 0.169 | 0.038 | 2187 | 0.167 | 0.050 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 258 | 0.872 | 0.787 | 0.756 | 0.143 | 2292 | 0.812 | 0.421 | 0.164 | 0.050 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 258 | 0.151 | 0.105 | 0.070 | 0.027 | 2292 | 0.134 | 0.064 | 0.028 | 0.004 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 8.5% | 1.90 | 1.58 | 35.1% | 0.5% | 21.3% | 25.5% | 4.4% | 0.00 | 14.1% | 51.1% | 0.15 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 8.5% | 1.90 | 1.58 | 30.8% | 0.5% | 20.5% | 27.5% | 10.9% | 0.00 | 15.5% | 50.0% | 0.01 | 0.00 |
| Totale | 400 | 8.5% | 1.90 | 1.58 | 32.7% | 0.5% | 20.9% | 26.5% | 8.2% | 0.00 | 14.8% | 50.5% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.274 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.45 |
| rif_LDR04_stanca_e_smonta | 200 | 0.340 | 0.154 | 0.0% | 0.0% | 0.97 | 0.30 | 0.36 | 0.00 | 0.00 | 0.00 | 4.71 |

