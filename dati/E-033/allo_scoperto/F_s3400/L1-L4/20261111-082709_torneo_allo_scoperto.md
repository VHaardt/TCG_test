# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 915s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 35.3% [33.5–37.1] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.0–13.0] (media 11.85) | 8–11 | ❌ |
| Partite al round 13+ | 48.0% [38.5–57.7] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=38) | 21.1% [11.1–36.3] | 20–35% | ✅ |
| Attacchi con opposizione | 30.7% [29.0–32.5] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 67.4% [65.4–69.3] (con ≥3: 27.4% [25.6–29.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.6% [35.8–39.4] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.4% [4.1–9.9] (n=281) / 83.0% [76.1–88.2] (n=147) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.3% [10.4–14.5] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 57.1% [32.6–78.6] (n=14), LDR-01 Risvegliato 74.6% [63.1–83.5] (n=67), LDR-04 Base 0.0% [0.0–49.0] (n=4), LDR-04 Risvegliato 70.9% [57.9–81.2] (n=55) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 52.4% [41.8–62.9] (n=82) | | |
| Attacchi per partita | 26.4 | | |
| Pugno attaccante vuoto / pieno | 45.1% [43.1–47.1] / 14.6% [13.2–16.1] (gemme medie 0.98) | non >90% | |
| Pugno difensore vuoto / pieno | 61.7% [58.9–64.4] / 22.4% [20.1–24.9] (gemme medie 0.22) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 816, 1: 951, 2: 523, 3: 222, 4: 99, 5: 22, 6: 9} | | |
| Azioni legali per decisione | 5.4 | <60 | ✅ |
| Fine partita | {'colpo_finale': 89, 'crepuscolo': 11} | | |
| G1 vince fra le partite finite al Crepuscolo | 81.8% [52.3–94.9] | | |
| G1 vince fra le partite arrivate al round 15 | 64.3% [38.8–83.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 21.4% [7.6–47.6] / 66.7% [20.8–93.9] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [6.1–79.2]; 7.1% [1.3–31.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-1': 3, '2-0': 2, '0-0': 2, '2-2': 2, '4-3': 1, '3-4': 1, '1-0': 1, '4-0': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=3) | 21.4% [7.6–47.6] / 66.7% [20.8–93.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 3}; 66.7% [20.8–93.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 66.7% [20.8–93.9] / 33.3% [6.1–79.2]; 1.67 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–56.2] / 100.0% [43.8–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 100.0% [20.7–100.0]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 14.3% [4.0–39.9]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=8) / turno di G2 (n=11) | 0.0% [0.0–32.4] / 0.0% [0.0–25.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=8) | 0.0% [0.0–32.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 42.9% [21.4–67.4] (7.1% [1.3–31.5]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR04_stanca_e_smonta 64% (n=14) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 54.0% [44.3–63.4], rif_LDR04_stanca_e_smonta 46.0% [36.6–55.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.313 / 0.065 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.065 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.04 (0.00), rif_LDR04_stanca_e_smonta 0.05 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 30.7% [28.9–32.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.23 (116 / 207); 60.7% [58.8–62.5] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 53.3% [52.0–54.7]; rif_LDR01_puntata_e_preda 53.3%, rif_LDR04_stanca_e_smonta 53.4% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.327 (242) / 0.317 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 54 vittorie), LDR-04 B: 14.0 (40%, 46 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 6.33, LDR-01 1.83, ROS-016 1.32, ROS-018 1.17, BLU-015 0.92, VER-001 0.81, VER-011 0.76, BLU-001 0.67, VER-008 0.66, VER-014 0.66, BLU-023 0.58, ROS-021 0.50 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.90, rif_LDR04_stanca_e_smonta 2.76 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.08, rif_LDR04_stanca_e_smonta 0.38 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 20% (n=15), rif_LDR04_stanca_e_smonta 22% (n=23) | 20–35% |
| M13 | Pugno d'attacco pieno | 14.6% [13.2–16.1] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, caccia 100%, VER-001 100%, VER-008 100%, ROS-016 54%, VER-011 54%, BLU-010 46%, NEU-009 46%, NEU-003 46%, VER-014 46%, VER-023 46%, collante 46%; oltre il 60%: VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 54.0 [44–63] (100) |
| rif_LDR04_stanca_e_smonta | 46.0 [37–56] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.80 | 0.00 | 1.83 / 0.00 | 0.00 | 0.00 | 4.2 (100) | 13 | G 41%, R 59% | 2.49 | 0.38 |
| rif_LDR04_stanca_e_smonta | 5.41 | 2.31 | 6.33 / 0.00 | 0.00 | 1.06 | 4.0 (100) | 9 | B 41%, G 59% | 1.94 | 0.82 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.83/2.09/0.52 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.33/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.32/0.07/0.12 | 0.82/0.17/0.67/0.25 | 0.94/0.36/0.17/0.06 | 0.00/0.26/0.00/0.00 | 0.75/0.00/0.29/0.18 | 0.69/0.25/0.38/0.18 | 0.76/1.32/0.02/0.41 | 0.80/1.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.50/0.28/0.32 | 0.29/0.15/0.25/0.37 | 0.00/0.00/0.00/0.00 | 0.78/0.82/0.05/0.61 | 0.77/0.00/0.00/0.00 | 0.86/0.00/0.21/0.07 | 0.76/0.76/0.21/0.20 | 0.77/0.49/0.42/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.05/0.00 | 0.40/0.02/0.05/0.00 | 0.46/0.08/0.20/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.04/0.01 | 0.33/0.49/0.02/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.16/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.67/0.15/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.23/0.25/0.19 | 0.34/0.00/0.14/0.11 | 0.72/0.92/0.44/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.58/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.81/0.10/0.76 | 0.68/0.00/0.00/0.00 | 0.63/0.00/0.25/0.16 | 0.00/0.00/0.00/0.00 | 0.33/0.24/0.21/0.21 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/6.33/2.19/0.74 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.19/0.22/0.02/0.10 | 0.00/0.00/0.00/0.00 | 0.41/0.27/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.12/0.19/0.10 | 0.25/0.00/0.00/0.04 | 0.29/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.83/0.04/0.32 | 0.32/0.02/0.03/0.01 | 0.32/0.00/0.15/0.11 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.26 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.19 | 0.01 | 0.00 | 0.00 | 0.17 | 0.10 | 0.00 | 0.00 | 0.31 | 0.15 | 0.00 | 0.02 | 0.00 | 0.00 | 0.04 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.49 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.04 | 0.01 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.01 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 1.00 | 0.01 | 0.01 | 0.07 | 0.10 | 0.16 | 0.13 | 0.06 | 0.13 | 0.09 | 0.07 | 0.08 | 0.05 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 1.08 | 0.01 | 0.04 | 0.06 | 0.08 | 0.20 | 0.15 | 0.18 | 0.12 | 0.05 | 0.11 | 0.06 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 3 | 0 | 3 |
| 8 | 6 | 3 | 0 | 9 |
| 9 | 4 | 6 | 0 | 10 |
| 10 | 6 | 3 | 0 | 9 |
| 11 | 7 | 7 | 0 | 14 |
| 12 | 2 | 5 | 0 | 7 |
| 13 | 9 | 4 | 0 | 13 |
| 14 | 5 | 16 | 0 | 21 |
| 15 | 8 | 5 | 0 | 13 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 53.3% | 0.057 | 0.00 | 0.90 | 0.00 | 0.00 | 3.81 | 0.00 | 0.00 | 0.348 |
| rif_LDR04_stanca_e_smonta | 100 | 53.4% | 0.074 | 1.95 | 0.81 | 0.00 | 0.00 | 3.36 | 0.00 | 0.00 | 0.278 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 249 | 0.855 | 0.783 | 0.723 | 0.285 | 1066 | 0.779 | 0.223 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 249 | 0.209 | 0.197 | 0.181 | 0.016 | 1066 | 0.163 | 0.053 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 203 | 0.842 | 0.788 | 0.744 | 0.458 | 1124 | 0.693 | 0.163 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 203 | 0.158 | 0.128 | 0.103 | 0.025 | 1124 | 0.125 | 0.045 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 11.0% | 2.22 | 1.92 | 31.8% | 0.0% | 19.3% | 24.2% | 5.6% | 0.00 | 13.0% | 53.3% | 0.10 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 11.0% | 2.22 | 1.92 | 28.8% | 0.0% | 20.7% | 29.3% | 9.8% | 0.00 | 15.5% | 53.4% | 0.02 | 0.00 |
| Totale | 200 | 11.0% | 2.22 | 1.92 | 30.0% | 0.0% | 20.0% | 26.7% | 8.1% | 0.00 | 14.2% | 53.3% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

