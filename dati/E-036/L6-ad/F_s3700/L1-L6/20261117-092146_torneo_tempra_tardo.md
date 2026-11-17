# Torneo v0.2 — /root/in/dati/E-036-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in/dati/E-036-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1502s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.5% [28.3–30.8] | 30–45% | ❌ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 10.85) | 8–11 | ✅ |
| Partite al round 13+ | 26.5% [20.9–33.0] | ≤12% | ❌ |
| Partite oltre il 15 | 0.5% [0.1–2.8] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=94) | 20.2% [13.3–29.4] | 20–35% | ✅ |
| Attacchi con opposizione | 27.8% [26.5–29.0] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 58.8% [57.3–60.3] (con ≥3: 19.5% [18.4–20.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.8% [35.5–38.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 7.1% [5.0–10.1] (n=394) / 87.4% [83.3–90.6] (n=317) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.4% [13.8–17.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 64.0% [44.5–79.8] (n=25), LDR-01 Risvegliato 74.7% [64.9–82.5] (n=91), LDR-06 Base 66.7% [20.8–93.9] (n=3), LDR-06 Risvegliato 79.0% [72.6–84.3] (n=186) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 31.6% [24.8–39.3] (n=155) | | |
| Attacchi per partita | 24.5 | | |
| Pugno attaccante vuoto / pieno | 53.1% [51.6–54.6] / 12.6% [11.7–13.6] (gemme medie 0.83) | non >90% | |
| Pugno difensore vuoto / pieno | 60.3% [58.3–62.3] / 24.9% [23.1–26.7] (gemme medie 0.24) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1678, 1: 1576, 2: 1113, 3: 353, 4: 122, 5: 49, 6: 3} | | |
| Azioni legali per decisione | 5.4 | <60 | ✅ |
| Fine partita | {'colpo_finale': 185, 'crepuscolo': 15} | | |
| G1 vince fra le partite finite al Crepuscolo | 46.7% [24.8–69.9] | | |
| G1 vince fra le partite arrivate al round 15 | 52.9% [31.0–73.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 58.8% [36.0–78.4] / 70.0% [39.7–89.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 30.0% [10.8–60.3]; 5.9% [1.0–27.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-0': 4, '1-1': 3, '1-0': 3, '1-2': 1, '5-2': 1, '2-0': 1, '3-0': 1, '2-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=11) | 64.7% [41.3–82.7] / 63.6% [35.4–84.8] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 10, 16: 1}; 63.6% [35.4–84.8] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 36.4% [15.2–64.6] / 27.3% [9.7–56.6]; 1.73 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–25.9] / 72.7% [43.4–90.3] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=7) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–35.4] / 75.0% [30.1–95.4]; 0.0% [0.0–35.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.5% [1.7–7.0] / 41.2% [21.6–64.0]; 100.0% [64.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 3, 'vinc:atk': 7} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=7) / turno di G2 (n=4) | 0.0% [0.0–35.4] / 0.0% [0.0–49.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=7) | 0.0% [0.0–35.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 41.2% [21.6–64.0] (0.0% [0.0–18.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 6, 'rif_LDR06_ferite_e_caccia': 5} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR06_ferite_e_caccia 53% (n=17) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 71.0% [64.4–76.8], rif_LDR06_ferite_e_caccia 29.0% [23.2–35.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.347 / 0.077 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.077 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.07 (0.00), rif_LDR06_ferite_e_caccia 0.15 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 35.1% [33.7–36.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.32 (337 / 727); 56.6% [55.2–57.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 45.7% [44.7–46.8]; rif_LDR01_puntata_e_preda 48.9%, rif_LDR06_ferite_e_caccia 42.6% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.351 (410) / 0.333 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 142 vittorie), LDR-06 G: 19.0 (54%, 58 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.54, LDR-01 2.15, VER-020 2.08, ROS-016 1.65, NER-017 1.14, ROS-018 0.99, VER-001 0.66, NER-009 0.62, VER-011 0.60, NER-013 0.59, VER-008 0.53, NEW-P31 0.51 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 1.12, rif_LDR06_ferite_e_caccia 2.87 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR06_ferite_e_caccia 0.12 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 31% (n=16), rif_LDR06_ferite_e_caccia 18% (n=78) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.6% [11.7–13.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR06_ferite_e_caccia 0.86; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-001 100%, ponte 100%, caccia 100%, VER-008 71%, VER-011 71%, ROS-016 71%, NEW-B06 29%, NEU-001 29%, VER-020 29%, NER-017 29%, collante 29%, NER-009 29%; oltre il 60%: ROS-016, VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 71.0 [64–77] (200) |
| rif_LDR06_ferite_e_caccia | 29.0 [23–36] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.85 | 0.00 | 2.15 / 0.00 | 0.00 | 0.00 | 4.5 (199) | 13 | G 39%, R 61% | 2.49 | 0.40 |
| rif_LDR06_ferite_e_caccia | 3.62 | 0.00 | 3.54 / 0.14 | 0.00 | 0.14 | 4.6 (197) | 9 | G 51%, K 49% | 2.03 | 1.46 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR01_puntata_e_preda | 2.15 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.93 | 2.62 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/2.15/1.79/0.42 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.39/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.41/0.20/0.05 | 0.77/0.12/0.61/0.22 | 0.71/0.36/0.10/0.07 | 0.00/0.38/0.00/0.00 | 0.66/0.00/0.17/0.08 | 0.75/0.30/0.30/0.16 | 0.80/1.65/0.05/0.70 | 0.67/0.99/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.47/0.41/0.27 | 0.23/0.10/0.15/0.13 | 0.00/0.00/0.00/0.00 | 0.67/0.56/0.02/0.49 | 0.60/0.00/0.00/0.00 | 0.77/0.00/0.14/0.09 | 0.76/0.60/0.23/0.12 | 0.69/0.29/0.45/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.06/0.01 | 0.40/0.01/0.03/0.01 | 0.32/0.09/0.11/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.04/0.04 | 0.34/0.53/0.03/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.20/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.76/0.05/0.62 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.29/0.43/0.18 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.54/1.76/0.80 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.35/0.12/0.06 | 0.35/0.34/0.06/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.12/0.27/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.24/0.03/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.38/0.04/0.31 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.02/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.51/0.11/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.20/0.28/0.04/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.00/0.12/0.04 | 0.22/0.45/0.13/0.08 | 0.00/0.00/0.00/0.00 | 0.58/0.51/0.10/0.46 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.18 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.16 | 0.01 | 0.00 | 0.01 | 0.18 | 0.12 | 0.00 | 0.00 | 0.29 | 0.10 | 0.00 | 0.03 | 0.00 | 0.03 | 0.04 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.56 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.04 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.69 | 0.00 | 0.03 | 0.04 | 0.07 | 0.08 | 0.07 | 0.09 | 0.12 | 0.07 | 0.02 | 0.04 | 0.04 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.86 | 0.00 | 0.04 | 0.07 | 0.08 | 0.15 | 0.10 | 0.09 | 0.07 | 0.12 | 0.04 | 0.07 | 0.02 | 0.01 | 0.00 | 0.01 | 0.86 | 0.12 | 0.14 | 0.14 | 0.12 | 0.12 | 0.12 | 0.06 | 0.01 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR01_puntata_e_preda | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.47 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 1 | 0 | 0 | 1 |
| 7 | 6 | 3 | 0 | 9 |
| 8 | 11 | 10 | 0 | 21 |
| 9 | 21 | 10 | 0 | 31 |
| 10 | 23 | 13 | 0 | 36 |
| 11 | 12 | 16 | 0 | 28 |
| 12 | 10 | 11 | 0 | 21 |
| 13 | 8 | 17 | 0 | 25 |
| 14 | 3 | 8 | 0 | 11 |
| 15 | 8 | 8 | 0 | 16 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 48.9% | 0.083 | 0.00 | 1.12 | 0.00 | 0.00 | 3.30 | 0.00 | 0.00 | 0.329 |
| rif_LDR06_ferite_e_caccia | 200 | 42.6% | 0.072 | 0.77 | 2.10 | 0.00 | 0.00 | 4.93 | 0.00 | 0.00 | 0.365 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 506 | 0.893 | 0.848 | 0.796 | 0.383 | 1983 | 0.792 | 0.181 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 506 | 0.160 | 0.142 | 0.117 | 0.026 | 1983 | 0.100 | 0.035 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 388 | 0.884 | 0.812 | 0.740 | 0.366 | 2017 | 0.787 | 0.246 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 388 | 0.265 | 0.224 | 0.188 | 0.077 | 2017 | 0.189 | 0.067 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 7.5% | 2.13 | 1.76 | 37.2% | 0.5% | 20.2% | 23.9% | 3.1% | 0.00 | 16.4% | 48.9% | 0.09 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 7.5% | 2.13 | 1.76 | 18.2% | 0.5% | 23.2% | 31.3% | 12.8% | 0.00 | 13.1% | 42.6% | 0.04 | 0.00 |
| Totale | 400 | 7.5% | 2.13 | 1.76 | 24.6% | 0.5% | 21.7% | 27.5% | 8.9% | 0.00 | 14.8% | 45.7% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.292 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.88 |
| rif_LDR06_ferite_e_caccia | 200 | 0.263 | 0.038 | 0.0% | 0.0% | 0.35 | 0.10 | 0.06 | 0.00 | 0.00 | 0.00 | 4.12 |

