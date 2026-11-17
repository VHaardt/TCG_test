# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2244s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 30.3% [29.1–31.6] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 10.77) | 8–11 | ✅ |
| Partite al round 13+ | 26.0% [20.4–32.5] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–1.9] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=65) | 23.1% [14.5–34.6] | 20–35% | ✅ |
| Attacchi con opposizione | 36.7% [35.4–38.0] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 66.2% [64.8–67.7] (con ≥3: 27.9% [26.5–29.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.7% [38.4–41.1] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.8% [3.1–7.4] (n=396) / 91.7% [88.2–94.2] (n=336) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.7% [13.3–16.3] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 88.9% [56.5–98.0] (n=9), LDR-01 Risvegliato 60.6% [52.3–68.2] (n=142), LDR-05 Base 50.0% [23.7–76.3] (n=10), LDR-05 Risvegliato 76.5% [69.5–82.3] (n=166) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 26.7% [20.9–33.5] (n=187) | | |
| Attacchi per partita | 26.3 | | |
| Pugno attaccante vuoto / pieno | 50.4% [49.0–51.8] / 12.6% [11.7–13.6] (gemme medie 0.79) | non >90% | |
| Pugno difensore vuoto / pieno | 54.9% [52.9–57.0] / 25.8% [24.1–27.7] (gemme medie 0.25) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1549, 1: 1679, 2: 1427, 3: 391, 4: 153, 5: 52, 6: 9} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 189, 'crepuscolo': 11} | | |
| G1 vince fra le partite finite al Crepuscolo | 63.6% [35.4–84.8] | | |
| G1 vince fra le partite arrivate al round 15 | 50.0% [26.8–73.2] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 50.0% [26.8–73.2] / 28.6% [8.2–64.1] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 57.1% [25.0–84.2]; 0.0% [0.0–21.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 4, '1-1': 2, '2-1': 1, '0-1': 1, '2-2': 1, '2-4': 1, '3-1': 1, '1-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=7) | 50.0% [26.8–73.2] / 28.6% [8.2–64.1] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 7}; 42.9% [15.8–75.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 42.9% [15.8–75.0] / 28.6% [8.2–64.1]; 2.57 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–35.4] / 71.4% [35.9–91.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 40.0% [11.8–76.9]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.0% [0.3–3.6] / 14.3% [4.0–39.9]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:pronto': 2, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=6) / turno di G2 (n=5) | 0.0% [0.0–39.0] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=6) | 0.0% [0.0–39.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 50.0% [26.8–73.2] (7.1% [1.3–31.5]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rott_LDR05_2c': 5, 'rif_LDR01_puntata_e_preda': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rott_LDR05_2c 50% (n=14) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 41.0% [34.4–47.9], rott_LDR05_2c 59.0% [52.1–65.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.361 / 0.082 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.079 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.09 (0.00), rott_LDR05_2c 0.17 (0.01) | |
| M4 | Scontri decisi prima dell'impegno | 31.7% [30.4–32.9] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.54 (118 / 190); 58.8% [57.5–60.1] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 46.7% [45.7–47.7]; rif_LDR01_puntata_e_preda 44.0%, rott_LDR05_2c 49.2% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.327 (1042) / 0.317 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 82 vittorie), LDR-05 R: 18.0 (50%, 118 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 4.51, LDR-01 1.56, ROS-016 1.25, ROS-018 0.75, VER-011 0.74, BLU-015 0.65, VER-001 0.59, VER-008 0.58, NEU-001 0.51, ROS-005 0.48, BLU-021 0.47, ROS-020 0.47 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.79, rott_LDR05_2c 0.16 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.07, rott_LDR05_2c 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 4% (n=24), rott_LDR05_2c 34% (n=41) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.6% [11.7–13.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rott_LDR05_2c 0.43; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, BLU-021 59%, NEU-001 59%, BLU-010 59%, collante 59%, ROS-020 59%, NEU-013 59%, BLU-008 59%, ROS-016 41%, VER-001 41%, caccia 41%, VER-011 41%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rott_LDR05_2c |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 41.0 [34–48] (200) |
| rott_LDR05_2c | 59.0 [52–66] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.89 | 0.00 | 1.56 / 0.00 | 0.00 | 0.00 | 3.9 (200) | 13 | G 41%, R 59% | 2.42 | 0.48 |
| rott_LDR05_2c | 3.81 | 0.00 | 4.51 / 0.00 | 0.00 | 0.82 | 3.9 (200) | 13 | B 44%, R 56% | 1.83 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.56/1.82/0.73 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.35/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.53/0.20/0.12 | 0.73/0.16/0.50/0.34 | 0.78/0.50/0.19/0.14 | 0.00/0.29/0.00/0.00 | 0.60/0.00/0.23/0.12 | 0.57/0.15/0.24/0.17 | 0.64/1.25/0.04/0.44 | 0.76/0.95/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.35/0.20/0.17 | 0.24/0.10/0.17/0.12 | 0.00/0.00/0.00/0.00 | 0.63/0.59/0.04/0.42 | 0.62/0.00/0.00/0.00 | 0.64/0.00/0.17/0.11 | 0.66/0.74/0.28/0.15 | 0.68/0.43/0.32/0.34 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.04/0.02 | 0.41/0.10/0.04/0.07 | 0.32/0.18/0.18/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.11/0.05 | 0.34/0.58/0.01/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rott_LDR05_2c | 0.00/0.00/0.00/0.00 | 0.00/4.51/1.84/0.71 | 0.64/0.46/0.21/0.12 | 0.64/0.00/0.19/0.14 | 0.56/0.34/0.20/0.14 | 0.54/0.26/0.35/0.22 | 0.57/0.00/0.21/0.17 | 0.53/0.65/0.20/0.30 | 0.00/0.47/0.00/0.00 | 0.00/0.39/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.30/0.26/0.20 | 0.71/0.41/0.20/0.10 | 0.65/0.16/0.54/0.58 | 0.78/0.46/0.17/0.12 | 0.00/0.30/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.21/0.29/0.27 | 0.00/0.00/0.00/0.00 | 0.44/0.55/0.00/0.00 | 0.58/0.47/0.36/0.38 | 0.35/0.28/0.24/0.20 | 0.20/0.05/0.12/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.20/0.03/0.06/0.10 | 0.69/0.51/0.10/0.06 | 0.43/0.00/0.11/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.92 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.14 | 0.01 | 0.00 | 0.01 | 0.10 | 0.10 | 0.00 | 0.00 | 0.14 | 0.09 | 0.00 | 0.01 | 0.00 | 0.03 | 0.06 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rott_LDR05_2c | 1.08 | 0.00 | 0.07 | 0.01 | 0.01 | 0.01 | 0.04 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.01 | 0.17 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.21 | 0.20 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.82 | 0.00 | 0.01 | 0.06 | 0.08 | 0.10 | 0.10 | 0.14 | 0.14 | 0.12 | 0.03 | 0.03 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rott_LDR05_2c | 200 | 1.09 | 0.00 | 0.03 | 0.10 | 0.15 | 0.14 | 0.21 | 0.16 | 0.10 | 0.12 | 0.03 | 0.01 | 0.03 | 0.01 | 0.43 | 0.13 | 0.08 | 0.06 | 0.07 | 0.01 | 0.06 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 0 | 5 | 0 | 5 |
| 7 | 5 | 4 | 0 | 9 |
| 8 | 11 | 6 | 0 | 17 |
| 9 | 18 | 11 | 0 | 29 |
| 10 | 17 | 19 | 0 | 36 |
| 11 | 23 | 9 | 0 | 32 |
| 12 | 11 | 8 | 0 | 19 |
| 13 | 10 | 13 | 0 | 23 |
| 14 | 8 | 7 | 0 | 15 |
| 15 | 7 | 7 | 0 | 14 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 44.0% | 0.061 | 0.00 | 0.79 | 0.00 | 0.00 | 3.86 | 0.00 | 0.00 | 0.349 |
| rott_LDR05_2c | 200 | 49.2% | 0.103 | 0.16 | 0.00 | 0.00 | 0.00 | 4.02 | 0.00 | 0.00 | 0.372 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 455 | 0.897 | 0.857 | 0.824 | 0.316 | 2209 | 0.844 | 0.225 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 455 | 0.171 | 0.147 | 0.127 | 0.040 | 2209 | 0.177 | 0.065 | 0.000 | 0.000 |
| rott_LDR05_2c | mano | 561 | 0.877 | 0.861 | 0.847 | 0.415 | 2035 | 0.812 | 0.214 | 0.000 | 0.000 |
| rott_LDR05_2c | Cicatrice | 561 | 0.239 | 0.234 | 0.230 | 0.061 | 2035 | 0.176 | 0.061 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 5.5% | 1.95 | 1.94 | 32.5% | 0.5% | 17.2% | 26.4% | 5.7% | 0.00 | 19.4% | 44.0% | 0.14 | 0.00 |
| rott_LDR05_2c | 200 | 5.5% | 1.95 | 1.94 | 48.1% | 0.5% | 14.8% | 29.1% | 16.4% | 0.00 | 16.2% | 49.2% | 0.10 | 0.00 |
| Totale | 400 | 5.5% | 1.95 | 1.94 | 39.9% | 0.5% | 16.0% | 27.8% | 11.3% | 0.00 | 17.7% | 46.7% | 0.12 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.381 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.78 |
| rott_LDR05_2c | 200 | 0.354 | 0.176 | 0.0% | 0.0% | 1.48 | 0.36 | 0.54 | 0.00 | 0.00 | 0.00 | 5.67 |

