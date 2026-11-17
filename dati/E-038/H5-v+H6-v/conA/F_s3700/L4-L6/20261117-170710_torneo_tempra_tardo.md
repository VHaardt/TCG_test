# Torneo v0.2 — /root/in38/dati/E-038-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in38/dati/E-038-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1566s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 39.0% [37.7–40.3] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [12.0–13.0] (media 11.93) | 8–11 | ❌ |
| Partite al round 13+ | 44.0% [37.3–50.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.3–3.6] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=99) | 40.4% [31.3–50.3] | 20–35% | ❌ |
| Attacchi con opposizione | 22.4% [21.3–23.5] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 60.5% [59.1–61.9] (con ≥3: 20.9% [19.8–22.1]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 35.9% [34.6–37.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 14.3% [11.5–17.8] (n=481) / 76.5% [71.4–80.9] (n=302) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.4% [11.0–14.0] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 42.9% [30.0–56.7] (n=49), LDR-04 Risvegliato 66.3% [56.7–74.8] (n=101), LDR-06 Base 65.0% [43.3–81.9] (n=20), LDR-06 Risvegliato 78.5% [70.6–84.7] (n=130) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 47.9% [40.5–55.4] (n=167) | | |
| Attacchi per partita | 25.9 | | |
| Pugno attaccante vuoto / pieno | 53.6% [52.2–55.1] / 12.2% [11.3–13.2] (gemme medie 0.84) | non >90% | |
| Pugno difensore vuoto / pieno | 68.6% [66.8–70.3] / 17.6% [16.2–19.1] (gemme medie 0.22) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1754, 1: 2066, 2: 957, 3: 285, 4: 95, 5: 24, 6: 5} | | |
| Azioni legali per decisione | 5.9 | <60 | ✅ |
| Fine partita | {'crepuscolo': 20, 'colpo_finale': 180} | | |
| G1 vince fra le partite finite al Crepuscolo | 20.0% [8.1–41.6] | | |
| G1 vince fra le partite arrivate al round 15 | 29.0% [16.1–46.6] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 48.4% [32.0–65.2] / 60.0% [35.7–80.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 13.3% [3.7–37.9]; 6.5% [1.8–20.7] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-1': 5, '2-3': 5, '0-1': 4, '0-0': 4, '3-3': 2, '2-2': 2, '1-0': 2, '4-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=15) | 48.4% [32.0–65.2] / 60.0% [35.7–80.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15}; 86.7% [62.1–96.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 60.0% [35.7–80.2] / 6.7% [1.2–29.8]; 1.73 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–20.4] / 93.3% [70.2–98.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=9) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–29.9] / 16.7% [3.0–56.4]; 0.0% [0.0–29.9] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.5% [2.4–8.3] / 29.0% [16.1–46.6]; 100.0% [70.1–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 7, 'perd:pronto': 2, 'vinc:atk': 9} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=12) / turno di G2 (n=10) | 0.0% [0.0–24.3] / 0.0% [0.0–27.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=12) | 0.0% [0.0–24.3] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 41.9% [26.4–59.2] (32.3% [18.6–49.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 10, 'rif_LDR06_ferite_e_caccia': 5} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR06_ferite_e_caccia 29% (n=31) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 55.0% [48.1–61.7], rif_LDR06_ferite_e_caccia 45.0% [38.3–51.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.490 / 0.077 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.077 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.07 (0.00), rif_LDR06_ferite_e_caccia 0.16 (0.05) | |
| M4 | Scontri decisi prima dell'impegno | 33.5% [32.3–34.8] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.21 (267 / 774); 62.5% [61.1–63.8] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.6% [49.6–51.6]; rif_LDR04_stanca_e_smonta 55.1%, rif_LDR06_ferite_e_caccia 45.9% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.372 (70) / 0.332 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 12.0 (36%, 110 vittorie), LDR-06 G: 17.0 (49%, 90 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 3.87, LDR-06 3.44, VER-020 2.58, NER-017 1.56, VER-008 0.93, BLU-015 0.87, NEW-I04 0.67, NER-013 0.63, NEW-B06 0.58, VER-023 0.54, VER-001 0.53, VER-014 0.52 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.69, rif_LDR06_ferite_e_caccia 3.25 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.32, rif_LDR06_ferite_e_caccia 0.39 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 48% (n=65), rif_LDR06_ferite_e_caccia 26% (n=34) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.2% [11.3–13.2] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR06_ferite_e_caccia 1.38; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, VER-001 100%, ponte 100%, VER-008 100%, caccia 100%, NEU-009 55%, BLU-010 55%, VER-014 55%, VER-023 55%, VER-020 45%, NER-017 45%, NEU-012 45%; oltre il 60%: VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 55.0 [48–62] (200) |
| rif_LDR06_ferite_e_caccia | 45.0 [38–52] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.26 | 1.64 | 3.87 / 0.00 | 0.00 | 0.84 | 5.3 (200) | 10 | B 41%, G 59% | 2.12 | 0.67 |
| rif_LDR06_ferite_e_caccia | 3.46 | 0.00 | 3.44 / 0.38 | 0.00 | 0.14 | 4.4 (199) | 10 | G 55%, K 45% | 2.43 | 1.50 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR04_stanca_e_smonta | 1.64 | 2.23 |
| rif_LDR06_ferite_e_caccia | 1.70 | 1.74 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.46/0.21/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.18/0.30/0.13 | 0.40/0.00/0.21/0.10 | 0.78/0.87/0.49/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.58/0.07/0.45 | 0.71/0.00/0.00/0.00 | 0.74/0.00/0.28/0.07 | 0.00/0.00/0.00/0.00 | 0.39/0.24/0.21/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.87/1.98/0.33 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.54/0.05/0.24 | 0.00/0.00/0.00/0.00 | 0.43/0.24/0.04/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.12/0.19/0.06 | 0.45/0.00/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.99/0.01/0.40 | 0.32/0.02/0.02/0.01 | 0.36/0.00/0.14/0.09 | 0.00/0.25/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.00/0.00 | 0.17/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.67/0.00/0.00 | 0.00/0.02/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.48/0.04/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.55/0.56/0.23 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.44/1.94/0.41 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.45/0.24/0.09 | 0.41/0.26/0.07/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.07/0.28/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.28/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.19/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.44/0.04/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.86/0.03/0.36 | 0.39/0.04/0.04/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.89/0.51/0.12/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.00/0.00/0.00 | 0.49/0.00/0.00/0.00 | 0.27/0.58/0.07/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.14/0.03 | 0.23/0.45/0.12/0.04 | 0.46/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.56 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.04 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.01 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.80 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 1.03 | 0.00 | 0.01 | 0.09 | 0.10 | 0.15 | 0.10 | 0.15 | 0.14 | 0.08 | 0.06 | 0.07 | 0.05 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.67 | 0.00 | 0.01 | 0.03 | 0.04 | 0.06 | 0.09 | 0.06 | 0.12 | 0.09 | 0.06 | 0.05 | 0.02 | 0.04 | 0.01 | 1.38 | 0.08 | 0.17 | 0.12 | 0.11 | 0.14 | 0.18 | 0.20 | 0.15 | 0.11 | 0.06 | 0.03 | 0.04 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR04_stanca_e_smonta | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.79 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 0 | 0 | 1 |
| 7 | 1 | 2 | 0 | 3 |
| 8 | 4 | 6 | 0 | 10 |
| 9 | 10 | 6 | 0 | 16 |
| 10 | 8 | 18 | 0 | 26 |
| 11 | 15 | 13 | 0 | 28 |
| 12 | 15 | 13 | 0 | 28 |
| 13 | 16 | 18 | 0 | 34 |
| 14 | 13 | 10 | 0 | 23 |
| 15 | 8 | 21 | 0 | 29 |
| 16 | 1 | 1 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 55.1% | 0.072 | 1.81 | 0.88 | 0.00 | 0.00 | 2.29 | 0.00 | 0.00 | 0.478 |
| rif_LDR06_ferite_e_caccia | 200 | 45.9% | 0.081 | 1.03 | 2.23 | 0.00 | 0.00 | 4.22 | 0.00 | 0.00 | 0.389 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 297 | 0.825 | 0.788 | 0.754 | 0.162 | 2316 | 0.778 | 0.421 | 0.174 | 0.054 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 297 | 0.088 | 0.071 | 0.040 | 0.020 | 2316 | 0.088 | 0.040 | 0.017 | 0.003 |
| rif_LDR06_ferite_e_caccia | mano | 553 | 0.835 | 0.787 | 0.740 | 0.320 | 2020 | 0.718 | 0.243 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 553 | 0.253 | 0.226 | 0.175 | 0.058 | 2020 | 0.190 | 0.065 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 10.0% | 2.15 | 1.57 | 31.4% | 0.0% | 22.7% | 27.1% | 7.1% | 0.00 | 12.7% | 55.1% | 0.02 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 10.0% | 2.15 | 1.57 | 24.6% | 0.0% | 23.8% | 29.2% | 7.6% | 0.00 | 9.8% | 45.9% | 0.02 | 0.00 |
| Totale | 400 | 10.0% | 2.15 | 1.57 | 27.8% | 0.0% | 23.2% | 28.1% | 7.3% | 0.00 | 11.3% | 50.6% | 0.02 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.253 | 0.113 | 0.0% | 0.0% | 0.61 | 0.76 | 0.33 | 0.57 | 0.00 | 0.00 | 4.50 |
| rif_LDR06_ferite_e_caccia | 200 | 0.194 | 0.029 | 0.0% | 0.0% | 0.24 | 0.05 | 0.05 | 0.33 | 0.00 | 0.00 | 4.82 |

