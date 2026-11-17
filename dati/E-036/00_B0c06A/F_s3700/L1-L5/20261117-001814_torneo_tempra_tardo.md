# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2158s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 30.6% [29.3–31.8] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 11.02) | 8–11 | ✅ |
| Partite al round 13+ | 29.5% [23.6–36.2] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.3–3.6] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=62) | 25.8% [16.6–37.9] | 20–35% | ✅ |
| Attacchi con opposizione | 36.4% [35.1–37.7] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 67.2% [65.8–68.6] (con ≥3: 28.4% [27.0–29.7]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.2% [37.9–40.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.5% [4.6–9.3] (n=428) / 89.7% [85.8–92.5] (n=319) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 13.3% [11.9–14.8] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 43.8% [23.1–66.8] (n=16), LDR-01 Risvegliato 62.7% [54.3–70.4] (n=134), LDR-05 Base 58.3% [32.0–80.7] (n=12), LDR-05 Risvegliato 83.6% [76.8–88.6] (n=152) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 31.2% [25.0–38.2] (n=186) | | |
| Attacchi per partita | 27.4 | | |
| Pugno attaccante vuoto / pieno | 49.4% [48.0–50.8] / 12.6% [11.7–13.6] (gemme medie 0.84) | non >90% | |
| Pugno difensore vuoto / pieno | 57.4% [55.4–59.3] / 25.5% [23.8–27.2] (gemme medie 0.25) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1562, 1: 1823, 2: 1466, 3: 402, 4: 159, 5: 68, 6: 6} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 186, 'crepuscolo': 14} | | |
| G1 vince fra le partite finite al Crepuscolo | 64.3% [38.8–83.7] | | |
| G1 vince fra le partite arrivate al round 15 | 57.9% [36.3–76.9] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 47.4% [27.3–68.3] / 33.3% [12.1–64.6] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 66.7% [35.4–87.9]; 10.5% [2.9–31.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 6, '0-0': 3, '3-2': 2, '2-1': 2, '2-3': 2, '3-4': 1, '2-2': 1, '4-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=11) | 57.9% [36.3–76.9] / 36.4% [15.2–64.6] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 9, 16: 2}; 45.5% [21.3–72.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 72.7% [43.4–90.3] / 45.5% [21.3–72.0]; 1.55 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–25.9] / 81.8% [52.3–94.9] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=4) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–49.0] / 71.4% [35.9–91.8]; 0.0% [0.0–49.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.8–5.0] / 21.1% [8.5–43.3]; 100.0% [51.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 2, 'perd:rim': 1, 'vinc:atk': 4} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=8) | 0.0% [0.0–43.4] / 0.0% [0.0–32.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 57.9% [36.3–76.9] (10.5% [2.9–31.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 7, 'rif_LDR05_scudi_armati': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 58% (n=19) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 41.0% [34.4–47.9], rif_LDR05_scudi_armati 59.0% [52.1–65.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.367 / 0.084 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.083 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.06 (0.00), rif_LDR05_scudi_armati 0.20 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 31.5% [30.3–32.7] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.87 (130 / 244); 59.2% [57.9–60.5] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 46.9% [46.0–47.9]; rif_LDR01_puntata_e_preda 44.4%, rif_LDR05_scudi_armati 49.4% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.318 (973) / 0.315 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 82 vittorie), LDR-05 R: 18.0 (49%, 118 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 4.34, LDR-01 1.87, ROS-016 1.56, VER-011 0.84, BLU-015 0.74, VER-001 0.73, ROS-018 0.71, VER-008 0.63, BLU-021 0.56, BLU-001 0.53, ROS-019 0.52, ROS-020 0.52 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.85, rif_LDR05_scudi_armati 0.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.09, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 16% (n=32), rif_LDR05_scudi_armati 37% (n=30) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.6% [11.7–13.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, ROS-020 59%, BLU-021 59%, BLU-010 59%, collante 59%, NEU-013 59%, NEU-009 59%, BLU-008 59%, VER-008 41%, VER-001 41%, VER-011 41%, ROS-016 41%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 41.0 [34–48] (200) |
| rif_LDR05_scudi_armati | 59.0 [52–66] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.01 | 0.00 | 1.87 / 0.00 | 0.00 | 0.00 | 3.9 (200) | 13 | G 41%, R 59% | 2.21 | 0.55 |
| rif_LDR05_scudi_armati | 4.06 | 0.00 | 4.34 / 0.00 | 0.00 | 0.91 | 4.1 (200) | 13 | B 46%, R 54% | 1.83 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.87/1.83/0.71 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.40/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.52/0.26/0.08 | 0.70/0.14/0.53/0.41 | 0.80/0.42/0.17/0.12 | 0.00/0.34/0.00/0.00 | 0.65/0.00/0.27/0.15 | 0.56/0.20/0.22/0.16 | 0.64/1.56/0.03/0.54 | 0.80/1.05/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.32/0.20/0.17 | 0.30/0.08/0.18/0.16 | 0.00/0.00/0.00/0.00 | 0.67/0.73/0.04/0.48 | 0.62/0.00/0.00/0.00 | 0.73/0.00/0.14/0.13 | 0.68/0.84/0.28/0.20 | 0.69/0.42/0.45/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.05/0.03 | 0.41/0.08/0.09/0.07 | 0.33/0.13/0.15/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.10/0.03 | 0.34/0.63/0.01/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/4.34/1.91/0.77 | 0.61/0.53/0.20/0.14 | 0.49/0.00/0.21/0.09 | 0.61/0.39/0.20/0.20 | 0.59/0.25/0.30/0.22 | 0.55/0.00/0.21/0.23 | 0.57/0.74/0.28/0.33 | 0.00/0.56/0.00/0.00 | 0.00/0.46/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.49/0.42/0.29 | 0.69/0.41/0.14/0.12 | 0.00/0.00/0.00/0.00 | 0.71/0.36/0.17/0.10 | 0.00/0.26/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.51/0.23/0.36/0.28 | 0.00/0.00/0.00/0.00 | 0.35/0.36/0.00/0.00 | 0.65/0.52/0.44/0.52 | 0.40/0.29/0.20/0.26 | 0.21/0.07/0.13/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.00/0.08/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.21/0.04/0.07/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.00/0.01/0.03 | 0.31/0.03/0.03/0.03 | 0.33/0.15/0.17/0.14 | 0.36/0.52/0.24/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.02 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.14 | 0.01 | 0.00 | 0.01 | 0.12 | 0.10 | 0.00 | 0.00 | 0.17 | 0.08 | 0.00 | 0.04 | 0.00 | 0.01 | 0.06 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.08 | 0.00 | 0.06 | 0.01 | 0.01 | 0.02 | 0.01 | 0.03 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.29 | 0.17 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.77 | 0.01 | 0.06 | 0.07 | 0.09 | 0.14 | 0.15 | 0.10 | 0.06 | 0.06 | 0.01 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.83 | 0.01 | 0.04 | 0.10 | 0.15 | 0.10 | 0.12 | 0.09 | 0.11 | 0.04 | 0.03 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 0 | 0 | 1 |
| 7 | 2 | 4 | 0 | 6 |
| 8 | 16 | 5 | 0 | 21 |
| 9 | 19 | 11 | 0 | 30 |
| 10 | 17 | 18 | 0 | 35 |
| 11 | 20 | 15 | 0 | 35 |
| 12 | 5 | 8 | 0 | 13 |
| 13 | 10 | 10 | 0 | 20 |
| 14 | 3 | 17 | 0 | 20 |
| 15 | 11 | 6 | 0 | 17 |
| 16 | 0 | 2 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 44.4% | 0.066 | 0.00 | 0.85 | 0.00 | 0.00 | 4.08 | 0.00 | 0.00 | 0.353 |
| rif_LDR05_scudi_armati | 200 | 49.4% | 0.101 | 0.12 | 0.00 | 0.00 | 0.00 | 4.21 | 0.00 | 0.00 | 0.380 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 400 | 0.917 | 0.885 | 0.830 | 0.417 | 2313 | 0.834 | 0.243 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 400 | 0.168 | 0.138 | 0.120 | 0.030 | 2313 | 0.185 | 0.070 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 628 | 0.842 | 0.825 | 0.806 | 0.382 | 2145 | 0.771 | 0.213 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 628 | 0.252 | 0.240 | 0.231 | 0.065 | 2145 | 0.186 | 0.064 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 7.0% | 2.00 | 1.57 | 28.9% | 0.0% | 16.2% | 24.8% | 5.7% | 0.00 | 18.2% | 44.4% | 0.14 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 7.0% | 2.00 | 1.57 | 40.8% | 0.0% | 13.5% | 30.7% | 16.9% | 0.00 | 17.3% | 49.4% | 0.12 | 0.00 |
| Totale | 400 | 7.0% | 2.00 | 1.57 | 34.2% | 0.0% | 14.8% | 27.7% | 11.4% | 0.00 | 17.7% | 46.9% | 0.13 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.377 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.99 |
| rif_LDR05_scudi_armati | 200 | 0.351 | 0.173 | 0.0% | 0.0% | 1.48 | 0.39 | 0.39 | 0.00 | 0.00 | 0.00 | 5.77 |

