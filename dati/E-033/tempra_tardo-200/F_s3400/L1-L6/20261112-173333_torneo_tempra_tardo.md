# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 698s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.4% [28.2–30.8] | 30–45% | ❌ |
| Durata mediana (round) | 10.0 [10.0–11.0] (media 10.46) | 8–11 | ✅ |
| Partite al round 13+ | 20.0% [15.0–26.1] | ≤12% | ❌ |
| Partite oltre il 15 | 0.5% [0.1–2.8] | <2% | ✅ |
| Vittorie prima del round 5 | 0.5% [0.1–2.8] | 0 | ❌ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=87) | 20.7% [13.5–30.4] | 20–35% | ✅ |
| Attacchi con opposizione | 23.9% [22.7–25.2] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 56.6% [55.1–58.1] (con ≥3: 18.0% [16.8–19.2]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.9% [38.5–41.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.3% [4.4–9.1] (n=411) / 88.0% [84.3–91.0] (n=359) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 16.8% [15.2–18.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 52.2% [33.0–70.8] (n=23), LDR-01 Risvegliato 67.2% [58.3–75.1] (n=116), LDR-06 Base 33.3% [6.1–79.2] (n=3), LDR-06 Risvegliato 74.5% [68.0–80.0] (n=200) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 23.3% [17.5–30.4] (n=163) | | |
| Attacchi per partita | 23.5 | | |
| Pugno attaccante vuoto / pieno | 52.7% [51.1–54.2] / 13.3% [12.3–14.4] (gemme medie 0.82) | non >90% | |
| Pugno difensore vuoto / pieno | 60.3% [58.2–62.3] / 24.9% [23.1–26.7] (gemme medie 0.23) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1596, 1: 1559, 2: 1067, 3: 358, 4: 95, 5: 26, 6: 3} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 187, 'crepuscolo': 13} | | |
| G1 vince fra le partite finite al Crepuscolo | 69.2% [42.4–87.3] | | |
| G1 vince fra le partite arrivate al round 15 | 64.7% [41.3–82.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 47.1% [26.2–69.0] / 25.0% [7.1–59.1] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [21.5–78.5]; 5.9% [1.0–27.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 4, '0-1': 2, '3-0': 2, '0-0': 2, '2-2': 2, '2-4': 1, '3-2': 1, '2-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=9) | 52.9% [31.0–73.8] / 22.2% [6.3–54.7] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 8, 16: 1}; 44.4% [18.9–73.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 55.6% [26.7–81.1] / 44.4% [18.9–73.3]; 2.44 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–29.9] / 77.8% [45.3–93.7] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 57.1% [25.0–84.2]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.0% [0.3–3.6] / 11.8% [3.3–34.3]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 1, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=6) / turno di G2 (n=6) | 0.0% [0.0–39.0] / 0.0% [0.0–39.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=6) | 0.0% [0.0–39.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 47.1% [26.2–69.0] (5.9% [1.0–27.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 7, 'rif_LDR06_ferite_e_caccia': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR06_ferite_e_caccia 65% (n=17) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 71.5% [64.9–77.3], rif_LDR06_ferite_e_caccia 28.5% [22.7–35.1]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.376 / 0.072 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.072 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.10 (0.00), rif_LDR06_ferite_e_caccia 0.14 (0.05) | |
| M4 | Scontri decisi prima dell'impegno | 35.6% [34.2–36.9] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.07 (300 / 714); 60.0% [58.6–61.4] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 46.8% [45.7–47.9]; rif_LDR01_puntata_e_preda 50.8%, rif_LDR06_ferite_e_caccia 42.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.342 (420) / 0.326 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 143 vittorie), LDR-06 G: 17.0 (49%, 57 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 2.79, LDR-01 1.83, VER-020 1.77, ROS-016 1.35, NER-017 0.93, ROS-018 0.92, VER-008 0.72, NER-009 0.65, VER-001 0.62, NEU-001 0.54, NER-013 0.53, VER-003 0.53 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 1.18, rif_LDR06_ferite_e_caccia 2.92 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR06_ferite_e_caccia 0.21 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 53% (n=15), rif_LDR06_ferite_e_caccia 14% (n=72) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.3% [12.3–14.4] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR06_ferite_e_caccia 0.90; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, VER-001 100%, VER-008 100%, caccia 100%, VER-011 72%, ROS-016 72%, VER-020 28%, NER-009 28%, VER-023 28%, NER-015 28%, collante 28%, NEU-001 28%; oltre il 60%: ROS-016, VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 71.5 [65–77] (200) |
| rif_LDR06_ferite_e_caccia | 28.5 [23–35] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.56 | 0.00 | 1.83 / 0.00 | 0.00 | 0.00 | 4.6 (200) | 13 | G 40%, R 60% | 2.36 | 0.37 |
| rif_LDR06_ferite_e_caccia | 3.90 | 0.00 | 2.79 / 0.04 | 0.00 | 0.17 | 4.3 (191) | 10 | G 56%, K 44% | 2.42 | 1.47 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.83/1.83/0.36 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.38/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.43/0.19/0.05 | 0.80/0.11/0.74/0.23 | 0.69/0.33/0.14/0.04 | 0.00/0.27/0.00/0.00 | 0.69/0.00/0.21/0.05 | 0.68/0.20/0.30/0.10 | 0.69/1.35/0.06/0.60 | 0.69/0.92/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.38/0.34/0.18 | 0.20/0.07/0.20/0.08 | 0.00/0.00/0.00/0.00 | 0.74/0.67/0.06/0.57 | 0.56/0.00/0.00/0.00 | 0.71/0.00/0.12/0.03 | 0.66/0.41/0.16/0.05 | 0.67/0.43/0.46/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.09/0.01 | 0.39/0.01/0.03/0.01 | 0.31/0.01/0.11/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.00/0.04/0.01 | 0.38/0.68/0.01/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.61/0.58/0.09/0.45 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.32/0.43/0.19 | 0.00/0.25/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.79/2.02/0.69 | 0.00/0.00/0.00/0.00 | 0.45/0.00/0.00/0.00 | 0.18/0.23/0.03/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.47/0.22/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.08/0.26/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.30/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.47/0.07/0.38 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.76/0.01/0.40 | 0.32/0.03/0.02/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.54/0.17/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.19 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.15 | 0.01 | 0.00 | 0.01 | 0.14 | 0.18 | 0.00 | 0.00 | 0.29 | 0.06 | 0.00 | 0.03 | 0.00 | 0.01 | 0.03 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.52 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.56 | 0.00 | 0.03 | 0.07 | 0.05 | 0.04 | 0.06 | 0.11 | 0.10 | 0.05 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.91 | 0.00 | 0.03 | 0.06 | 0.06 | 0.14 | 0.12 | 0.14 | 0.14 | 0.12 | 0.04 | 0.04 | 0.01 | 0.01 | 0.01 | 0.90 | 0.10 | 0.20 | 0.12 | 0.11 | 0.14 | 0.10 | 0.04 | 0.04 | 0.03 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 4 | 0 | 1 | 0 | 1 |
| 5 | 2 | 1 | 0 | 3 |
| 6 | 0 | 1 | 0 | 1 |
| 7 | 4 | 10 | 0 | 14 |
| 8 | 11 | 14 | 0 | 25 |
| 9 | 10 | 14 | 0 | 24 |
| 10 | 12 | 25 | 0 | 37 |
| 11 | 20 | 20 | 0 | 40 |
| 12 | 8 | 7 | 0 | 15 |
| 13 | 6 | 8 | 0 | 14 |
| 14 | 1 | 8 | 0 | 9 |
| 15 | 10 | 6 | 0 | 16 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 50.8% | 0.066 | 0.00 | 1.18 | 0.00 | 0.00 | 2.85 | 0.00 | 0.00 | 0.331 |
| rif_LDR06_ferite_e_caccia | 200 | 42.3% | 0.078 | 0.89 | 2.03 | 0.00 | 0.00 | 4.36 | 0.00 | 0.00 | 0.424 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 482 | 0.855 | 0.799 | 0.759 | 0.293 | 1947 | 0.762 | 0.193 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 482 | 0.199 | 0.176 | 0.145 | 0.041 | 1947 | 0.161 | 0.051 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 384 | 0.938 | 0.896 | 0.872 | 0.391 | 1891 | 0.835 | 0.313 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 384 | 0.250 | 0.214 | 0.203 | 0.070 | 1891 | 0.230 | 0.088 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 6.5% | 1.80 | 1.50 | 47.9% | 2.0% | 20.7% | 24.1% | 4.1% | 0.00 | 14.9% | 50.8% | 0.09 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 6.5% | 1.80 | 1.50 | 21.0% | 2.0% | 22.3% | 28.4% | 7.3% | 0.00 | 11.6% | 42.3% | 0.05 | 0.00 |
| Totale | 400 | 6.5% | 1.80 | 1.50 | 30.4% | 2.0% | 21.5% | 26.2% | 6.0% | 0.00 | 13.3% | 46.8% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

