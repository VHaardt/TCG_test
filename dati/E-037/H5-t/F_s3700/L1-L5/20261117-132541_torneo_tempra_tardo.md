# Torneo v0.2 — /home/claude/e037_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e037_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 712s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 27.9% [26.1–29.7] | 30–45% | ❌ |
| Durata mediana (round) | 8.0 [8.0–9.0] (media 9.39) | 8–11 | ✅ |
| Partite al round 13+ | 20.0% [13.3–28.9] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=41) | 9.8% [3.9–22.5] | 20–35% | ❌ |
| Attacchi con opposizione | 31.6% [29.7–33.5] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 63.3% [61.0–65.5] (con ≥3: 24.1% [22.2–26.1]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 44.8% [42.8–46.8] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 60.3% [54.7–65.7] (n=305) / 90.6% [85.1–94.2] (n=160) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 13.5% [11.6–15.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 23.5% [17.9–30.1] (n=183), LDR-01 Risvegliato 57.1% [44.9–68.6] (n=63), LDR-05 Base 100.0% [20.7–100.0] (n=1), LDR-05 Risvegliato 81.7% [72.0–88.6] (n=82) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 22.2% [14.9–31.8] (n=90) | | |
| Attacchi per partita | 24.0 | | |
| Pugno attaccante vuoto / pieno | 55.9% [53.7–58.1] / 14.2% [12.8–15.8] (gemme medie 0.62) | non >90% | |
| Pugno difensore vuoto / pieno | 44.7% [41.3–48.0] / 35.3% [32.1–38.5] (gemme medie 0.25) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 858, 1: 816, 2: 524, 3: 121, 4: 52, 5: 28, 6: 2} | | |
| Azioni legali per decisione | 4.8 | <60 | ✅ |
| Fine partita | {'colpo_finale': 95, 'crepuscolo': 5} | | |
| G1 vince fra le partite finite al Crepuscolo | 40.0% [11.8–76.9] | | |
| G1 vince fra le partite arrivate al round 15 | 57.1% [25.0–84.2] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 28.6% [8.2–64.1] / 100.0% [34.2–100.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 0.0% [0.0–65.8]; 0.0% [0.0–35.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-0': 2, '2-2': 2, '1-1': 2, '0-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=2) | 28.6% [8.2–64.1] / 100.0% [34.2–100.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 2}; 100.0% [34.2–100.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 50.0% [9.5–90.5] / 0.0% [0.0–65.8]; 0.50 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–65.8] / 50.0% [9.5–90.5] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / nan% [nan–nan]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 28.6% [8.2–64.1]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 1, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=4) / turno di G2 (n=2) | 0.0% [0.0–49.0] / 0.0% [0.0–65.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=4) | 0.0% [0.0–49.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 42.9% [15.8–75.0] (14.3% [2.6–51.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 1, 'rif_LDR05_scudi_armati': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 57% (n=7) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 72.0% [62.5–79.9], rif_LDR05_scudi_armati 28.0% [20.1–37.5]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.293 / 0.077 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.076 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.04 (0.00), rif_LDR05_scudi_armati 0.24 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 42.2% [40.3–44.2] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.67 (41 / 126); 63.1% [61.2–65.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 46.3% [44.8–47.9]; rif_LDR01_puntata_e_preda 44.0%, rif_LDR05_scudi_armati 48.9% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.342 (350) / 0.336 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 72 vittorie), LDR-05 R: 18.0 (49%, 28 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 2.65, LDR-01 1.20, ROS-016 0.88, VER-001 0.85, VER-011 0.73, VER-008 0.72, BLU-001 0.56, BLU-021 0.49, ROS-005 0.47, ROS-019 0.46, BLU-015 0.46, ROS-018 0.45 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 1.00, rif_LDR05_scudi_armati 0.13 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.12, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 20% (n=5), rif_LDR05_scudi_armati 8% (n=36) | 20–35% |
| M13 | Pugno d'attacco pieno | 14.2% [12.8–15.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, VER-008 72%, caccia 72%, VER-001 72%, ROS-016 72%, VER-011 72%, NEU-013 28%, ROS-020 28%, BLU-021 28%, BLU-010 28%, BLU-008 28%, collante 28%; oltre il 60%: ROS-016, VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 72.0 [63–80] (100) |
| rif_LDR05_scudi_armati | 28.0 [20–37] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.88 | 0.00 | 1.20 / 0.00 | 0.00 | 0.00 | 2.8 (100) | 12 | G 41%, R 59% | 1.80 | 0.42 |
| rif_LDR05_scudi_armati | 3.85 | 0.00 | 2.65 / 0.00 | 0.00 | 0.52 | 3.5 (98) | 9 | B 48%, R 52% | 2.25 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR01_puntata_e_preda | 1.20 | 0.00 |
| rif_LDR05_scudi_armati | 0.60 | 2.05 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.20/2.56/0.76 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.22/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.45/0.25/0.07 | 0.64/0.07/0.42/0.26 | 0.78/0.46/0.18/0.15 | 0.00/0.21/0.00/0.00 | 0.52/0.00/0.44/0.16 | 0.57/0.20/0.52/0.19 | 0.52/0.88/0.05/0.31 | 0.61/0.79/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.22/0.11/0.12 | 0.19/0.02/0.11/0.08 | 0.00/0.00/0.00/0.00 | 0.63/0.85/0.03/0.65 | 0.56/0.00/0.00/0.00 | 0.65/0.00/0.36/0.17 | 0.46/0.73/0.38/0.15 | 0.50/0.35/0.36/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.20/0.00/0.06/0.01 | 0.39/0.06/0.07/0.04 | 0.32/0.19/0.30/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.06/0.01 | 0.27/0.72/0.01/0.34 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.65/2.09/0.83 | 0.55/0.56/0.13/0.13 | 0.35/0.00/0.13/0.09 | 0.52/0.42/0.24/0.09 | 0.42/0.06/0.15/0.05 | 0.51/0.00/0.16/0.15 | 0.56/0.46/0.13/0.20 | 0.00/0.49/0.00/0.00 | 0.00/0.42/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.21/0.20/0.13 | 0.71/0.40/0.17/0.05 | 0.00/0.00/0.00/0.00 | 0.65/0.47/0.19/0.11 | 0.00/0.28/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.05/0.14/0.20 | 0.00/0.00/0.00/0.00 | 0.26/0.11/0.00/0.00 | 0.51/0.11/0.22/0.34 | 0.32/0.04/0.13/0.05 | 0.07/0.00/0.06/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.00/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.20/0.04/0.06/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.00/0.01/0.00 | 0.26/0.03/0.03/0.02 | 0.26/0.11/0.07/0.10 | 0.24/0.46/0.12/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.61 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.02 | 0.00 | 0.01 | 0.13 | 0.02 | 0.00 | 0.00 | 0.12 | 0.02 | 0.00 | 0.03 | 0.00 | 0.00 | 0.02 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 0.37 | 0.00 | 0.05 | 0.02 | 0.00 | 0.02 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.03 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.07 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.43 | 0.00 | 0.02 | 0.04 | 0.11 | 0.11 | 0.05 | 0.02 | 0.02 | 0.04 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.76 | 0.03 | 0.07 | 0.13 | 0.09 | 0.16 | 0.09 | 0.08 | 0.04 | 0.04 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 3 | 5 | 0 | 8 |
| 7 | 12 | 13 | 0 | 25 |
| 8 | 13 | 5 | 0 | 18 |
| 9 | 7 | 3 | 0 | 10 |
| 10 | 6 | 1 | 0 | 7 |
| 11 | 4 | 4 | 0 | 8 |
| 12 | 2 | 2 | 0 | 4 |
| 13 | 5 | 6 | 0 | 11 |
| 14 | 0 | 2 | 0 | 2 |
| 15 | 4 | 3 | 0 | 7 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 44.0% | 0.052 | 0.00 | 1.00 | 0.00 | 0.00 | 3.71 | 0.00 | 0.00 | 0.237 |
| rif_LDR05_scudi_armati | 100 | 48.9% | 0.093 | 0.13 | 0.00 | 0.00 | 0.00 | 2.85 | 0.00 | 0.00 | 0.330 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 144 | 0.847 | 0.785 | 0.757 | 0.319 | 810 | 0.770 | 0.132 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 144 | 0.194 | 0.146 | 0.139 | 0.028 | 810 | 0.185 | 0.036 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 327 | 0.875 | 0.856 | 0.850 | 0.336 | 1120 | 0.750 | 0.152 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 327 | 0.226 | 0.211 | 0.205 | 0.073 | 1120 | 0.218 | 0.065 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 5.0% | 1.80 | 1.68 | 46.5% | 0.0% | 10.7% | 21.4% | 4.6% | 0.00 | 15.3% | 44.0% | 0.13 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 5.0% | 1.80 | 1.68 | 21.6% | 0.0% | 14.3% | 29.7% | 13.6% | 0.00 | 19.6% | 48.9% | 0.03 | 0.00 |
| Totale | 200 | 5.0% | 1.80 | 1.68 | 29.8% | 0.0% | 12.5% | 25.5% | 9.5% | 0.00 | 17.4% | 46.3% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.351 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 6.27 |
| rif_LDR05_scudi_armati | 100 | 0.292 | 0.157 | 0.0% | 0.0% | 1.36 | 0.53 | 0.21 | 0.00 | 0.00 | 0.00 | 4.48 |

