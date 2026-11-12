# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 937s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 35.9% [34.6–37.2] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.0–13.0] (media 11.87) | 8–11 | ❌ |
| Partite al round 13+ | 46.5% [39.7–53.4] | ≤12% | ❌ |
| Partite oltre il 15 | 2.0% [0.8–5.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=81) | 23.5% [15.6–33.8] | 20–35% | ✅ |
| Attacchi con opposizione | 30.5% [29.3–31.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 68.3% [66.9–69.6] (con ≥3: 28.2% [26.9–29.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.0% [35.7–38.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 7.4% [5.4–10.0] (n=502) / 83.9% [79.3–87.7] (n=292) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.6% [11.2–14.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 56.5% [36.8–74.4] (n=23), LDR-01 Risvegliato 67.2% [58.7–74.7] (n=128), LDR-04 Base 64.3% [38.8–83.7] (n=14), LDR-04 Risvegliato 64.1% [55.1–72.2] (n=117) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 50.9% [43.3–58.5] (n=163) | | |
| Attacchi per partita | 26.3 | | |
| Pugno attaccante vuoto / pieno | 47.6% [46.2–49.1] / 14.6% [13.6–15.6] (gemme medie 0.90) | non >90% | |
| Pugno difensore vuoto / pieno | 60.9% [58.9–62.8] / 21.9% [20.3–23.6] (gemme medie 0.23) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1715, 1: 1851, 2: 1023, 3: 408, 4: 208, 5: 55, 6: 8, 7: 1} | | |
| Azioni legali per decisione | 5.4 | <60 | ✅ |
| Fine partita | {'colpo_finale': 169, 'crepuscolo': 31} | | |
| G1 vince fra le partite finite al Crepuscolo | 58.1% [40.8–73.6] | | |
| G1 vince fra le partite arrivate al round 15 | 51.3% [36.2–66.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 38.5% [24.9–54.1] / 53.3% [30.1–75.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [15.2–58.3]; 10.3% [4.1–23.6] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 5, '0-0': 4, '2-2': 4, '2-3': 4, '2-0': 4, '1-1': 4, '3-2': 3, '2-1': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=18) | 46.2% [31.6–61.4] / 44.4% [24.6–66.3] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15, 16: 3}; 61.1% [38.6–79.7] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 61.1% [38.6–79.7] / 22.2% [9.0–45.2]; 1.72 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–17.6] / 94.4% [74.2–99.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=8) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–32.4] / 40.0% [16.8–68.7]; 0.0% [0.0–32.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.0% [2.0–7.7] / 20.5% [10.8–35.5]; 100.0% [67.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 5, 'perd:pronto': 3, 'vinc:atk': 7, 'vinc:rim': 1} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=17) / turno di G2 (n=13) | 0.0% [0.0–18.4] / 0.0% [0.0–22.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=17) | 0.0% [0.0–18.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 53.8% [38.6–68.4] (12.8% [5.6–26.7]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 12, 'rif_LDR01_puntata_e_preda': 6} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR04_stanca_e_smonta 51% (n=39) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 54.0% [47.1–60.8], rif_LDR04_stanca_e_smonta 46.0% [39.2–52.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.324 / 0.067 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.067 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.06 (0.00), rif_LDR04_stanca_e_smonta 0.06 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 31.8% [30.6–33.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.32 (230 / 434); 61.0% [59.7–62.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 54.0% [53.1–55.0]; rif_LDR01_puntata_e_preda 54.2%, rif_LDR04_stanca_e_smonta 53.8% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.331 (440) / 0.313 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 108 vittorie), LDR-04 B: 14.0 (40%, 92 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 6.27, LDR-01 1.78, ROS-016 1.54, ROS-018 1.05, BLU-015 0.95, VER-001 0.76, VER-011 0.72, VER-008 0.71, VER-014 0.71, BLU-023 0.56, BLU-001 0.53, VER-019 0.44 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.92, rif_LDR04_stanca_e_smonta 2.65 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.07, rif_LDR04_stanca_e_smonta 0.34 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 16% (n=32), rif_LDR04_stanca_e_smonta 29% (n=49) | 20–35% |
| M13 | Pugno d'attacco pieno | 14.6% [13.6–15.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-001 100%, ponte 100%, VER-008 100%, caccia 100%, VER-011 54%, ROS-016 54%, collante 46%, NEU-009 46%, BLU-010 46%, NEU-003 46%, NEU-011 46%, VER-023 46%; oltre il 60%: VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 54.0 [47–61] (200) |
| rif_LDR04_stanca_e_smonta | 46.0 [39–53] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.88 | 0.00 | 1.78 / 0.00 | 0.00 | 0.00 | 4.4 (200) | 13 | G 42%, R 58% | 2.34 | 0.41 |
| rif_LDR04_stanca_e_smonta | 5.31 | 2.27 | 6.27 / 0.00 | 0.00 | 0.66 | 4.7 (194) | 10 | B 39%, G 61% | 2.06 | 0.67 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.78/1.94/0.64 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.32/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.43/0.22/0.06 | 0.73/0.12/0.68/0.34 | 0.79/0.36/0.14/0.07 | 0.00/0.33/0.00/0.00 | 0.71/0.00/0.24/0.15 | 0.76/0.23/0.34/0.18 | 0.80/1.54/0.02/0.59 | 0.84/1.05/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.36/0.24/0.27 | 0.26/0.10/0.17/0.24 | 0.00/0.00/0.00/0.00 | 0.77/0.82/0.04/0.58 | 0.80/0.00/0.00/0.00 | 0.79/0.00/0.14/0.07 | 0.79/0.72/0.32/0.12 | 0.73/0.56/0.52/0.37 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.00/0.04/0.04 | 0.38/0.04/0.05/0.03 | 0.36/0.09/0.17/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.05/0.03 | 0.32/0.48/0.01/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.53/0.21/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.22/0.33/0.17 | 0.41/0.00/0.18/0.12 | 0.67/0.95/0.41/0.27 | 0.00/0.00/0.00/0.00 | 0.00/0.56/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.70/0.06/0.54 | 0.78/0.00/0.00/0.00 | 0.70/0.00/0.23/0.12 | 0.00/0.00/0.00/0.00 | 0.35/0.32/0.26/0.18 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/6.27/2.03/0.71 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.21/0.34/0.03/0.17 | 0.00/0.00/0.00/0.00 | 0.43/0.30/0.04/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.09/0.20/0.04 | 0.35/0.00/0.01/0.02 | 0.32/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.95/0.01/0.45 | 0.36/0.03/0.04/0.02 | 0.34/0.00/0.18/0.07 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.10 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.15 | 0.01 | 0.00 | 0.01 | 0.15 | 0.12 | 0.00 | 0.00 | 0.23 | 0.09 | 0.00 | 0.02 | 0.00 | 0.01 | 0.07 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.64 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.04 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.01 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.88 | 0.01 | 0.04 | 0.08 | 0.10 | 0.14 | 0.15 | 0.12 | 0.10 | 0.05 | 0.06 | 0.02 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 0.98 | 0.02 | 0.04 | 0.05 | 0.10 | 0.12 | 0.17 | 0.20 | 0.11 | 0.07 | 0.04 | 0.01 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 6 | 0 | 7 |
| 8 | 6 | 8 | 0 | 14 |
| 9 | 11 | 4 | 0 | 15 |
| 10 | 20 | 11 | 0 | 31 |
| 11 | 12 | 16 | 0 | 28 |
| 12 | 4 | 8 | 0 | 12 |
| 13 | 12 | 18 | 0 | 30 |
| 14 | 8 | 16 | 0 | 24 |
| 15 | 17 | 18 | 0 | 35 |
| 16 | 3 | 1 | 0 | 4 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 54.2% | 0.063 | 0.00 | 0.92 | 0.00 | 0.00 | 4.03 | 0.00 | 0.00 | 0.388 |
| rif_LDR04_stanca_e_smonta | 200 | 53.8% | 0.071 | 1.89 | 0.77 | 0.00 | 0.00 | 3.13 | 0.00 | 0.00 | 0.262 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 539 | 0.868 | 0.831 | 0.798 | 0.282 | 2055 | 0.786 | 0.242 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 539 | 0.217 | 0.197 | 0.152 | 0.020 | 2055 | 0.167 | 0.060 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 400 | 0.848 | 0.777 | 0.718 | 0.448 | 2275 | 0.698 | 0.153 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 400 | 0.152 | 0.140 | 0.105 | 0.028 | 2275 | 0.106 | 0.029 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 15.5% | 2.21 | 1.74 | 33.7% | 0.0% | 19.5% | 25.7% | 5.6% | 0.00 | 12.1% | 54.2% | 0.08 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 15.5% | 2.21 | 1.74 | 29.1% | 0.0% | 22.5% | 28.2% | 8.4% | 0.00 | 15.5% | 53.8% | 0.02 | 0.00 |
| Totale | 400 | 15.5% | 2.21 | 1.74 | 31.1% | 0.0% | 21.0% | 27.0% | 7.3% | 0.00 | 13.8% | 54.0% | 0.05 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

