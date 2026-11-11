# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 1241s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 38.4% [36.6–40.3] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.0–13.0] (media 12.00) | 8–11 | ❌ |
| Partite al round 13+ | 47.0% [37.5–56.7] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=38) | 26.3% [15.0–42.0] | 20–35% | ✅ |
| Attacchi con opposizione | 31.6% [29.8–33.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 58.9% [56.9–60.8] (con ≥3: 21.6% [19.9–23.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.4% [35.6–39.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 10.2% [7.0–14.6] (n=246) / 77.6% [69.5–84.0] (n=125) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.1% [8.3–12.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 45.0% [25.8–65.8] (n=20), LDR-01 Risvegliato 68.5% [55.3–79.3] (n=54), LDR-02 Base 40.0% [11.8–76.9] (n=5), LDR-02 Risvegliato 93.0% [81.4–97.6] (n=43) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 53.0% [42.4–63.4] (n=83) | | |
| Attacchi per partita | 25.7 | | |
| Pugno attaccante vuoto / pieno | 48.8% [46.8–50.8] / 11.4% [10.2–12.7] (gemme medie 0.97) | non >90% | |
| Pugno difensore vuoto / pieno | 52.5% [49.8–55.2] / 25.1% [22.8–27.6] (gemme medie 0.32) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 908, 1: 896, 2: 496, 3: 176, 4: 78, 5: 16, 6: 1, 7: 1} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 89, 'crepuscolo': 11} | | |
| G1 vince fra le partite finite al Crepuscolo | 72.7% [43.4–90.3] | | |
| G1 vince fra le partite arrivate al round 15 | 62.5% [42.7–78.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 25.0% [12.0–44.9] / 33.3% [9.7–70.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 66.7% [30.0–90.3]; 4.2% [0.7–20.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 5, '1-0': 4, '3-3': 3, '2-3': 2, '2-0': 2, '3-2': 2, '1-1': 2, '2-4': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=6) | 25.0% [12.0–44.9] / 33.3% [9.7–70.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 6}; 33.3% [9.7–70.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 100.0% [61.0–100.0] / 50.0% [18.8–81.2]; 3.17 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–39.0] / 100.0% [61.0–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 75.0% [30.1–95.4]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 8.3% [2.3–25.8]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=15) / turno di G2 (n=10) | 0.0% [0.0–20.4] / 0.0% [0.0–27.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=15) | 0.0% [0.0–20.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 37.5% [21.2–57.3] (8.3% [2.3–25.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 4, 'rif_LDR02_muro_di_parata': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR02_muro_di_parata 62% (n=24) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 58.0% [48.2–67.2], rif_LDR02_muro_di_parata 42.0% [32.8–51.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.444 / 0.078 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.074 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.10 (0.00), rif_LDR02_muro_di_parata 0.15 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 24.7% [23.0–26.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.40 (37 / 103); 63.9% [62.0–65.8] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 48.8% [47.4–50.3]; rif_LDR01_puntata_e_preda 49.9%, rif_LDR02_muro_di_parata 47.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.370 (273) / 0.343 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 58 vittorie), LDR-02 K: 9.0 (26%, 42 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-01 1.75, ROS-016 1.32, LDR-02 1.28, ROS-018 1.08, ROS-021 0.70, BLU-001 0.63, VER-011 0.60, VER-001 0.50, BLU-025 0.49, VER-019 0.49, VER-008 0.42, NEU-006 0.42 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.80, rif_LDR02_muro_di_parata 1.55 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.03, rif_LDR02_muro_di_parata 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 38% (n=13), rif_LDR02_muro_di_parata 20% (n=25) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.4% [10.2–12.7] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR02_muro_di_parata 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, caccia 58%, VER-008 58%, VER-011 58%, VER-001 58%, ROS-016 58%, NEU-015 42%, 11.1 42%, BLU-021 42%, NEU-003 42%, BLU-022 42%, NER-014 42%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR02_muro_di_parata |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 58.0 [48–67] (100) |
| rif_LDR02_muro_di_parata | 42.0 [33–52] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.36 | 0.00 | 1.75 / 0.00 | 0.00 | 0.00 | 3.9 (100) | 13 | G 41%, R 59% | 2.24 | 0.75 |
| rif_LDR02_muro_di_parata | 4.65 | 0.00 | 1.28 / 0.00 | 0.00 | 1.59 | 4.4 (99) | 8 | B 77%, K 23% | 2.65 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.75/1.90/0.33 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.42/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.38/0.16/0.04 | 0.78/0.23/0.50/0.10 | 0.78/0.29/0.11/0.03 | 0.00/0.35/0.00/0.00 | 0.79/0.00/0.36/0.00 | 0.71/0.22/0.34/0.09 | 0.83/1.32/0.07/0.47 | 0.67/1.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.70/0.33/0.14 | 0.27/0.14/0.21/0.12 | 0.00/0.00/0.00/0.00 | 0.81/0.50/0.08/0.36 | 0.74/0.00/0.00/0.00 | 0.85/0.00/0.14/0.03 | 0.74/0.60/0.29/0.06 | 0.81/0.49/0.66/0.19 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.00/0.05/0.00 | 0.41/0.05/0.08/0.01 | 0.35/0.02/0.16/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.31/0.42/0.02/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.63/0.31/0.24 | 0.69/0.00/0.18/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.00/0.32/0.35 | 0.00/0.00/0.00/0.00 | 0.00/0.23/0.00/0.00 | 0.00/0.22/0.00/0.00 | 0.00/0.49/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.28/1.81/1.56 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.02/0.00/0.00 | 0.30/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.02/0.10/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.51/0.11/0.14/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.37 | 0.15 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.16 | 0.00 | 0.00 | 0.03 | 0.10 | 0.17 | 0.00 | 0.00 | 0.31 | 0.13 | 0.00 | 0.09 | 0.00 | 0.00 | 0.07 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 0.48 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.98 | 0.03 | 0.07 | 0.04 | 0.09 | 0.11 | 0.11 | 0.13 | 0.12 | 0.11 | 0.04 | 0.05 | 0.05 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 100 | 1.35 | 0.02 | 0.07 | 0.08 | 0.20 | 0.20 | 0.17 | 0.20 | 0.12 | 0.09 | 0.07 | 0.05 | 0.04 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 2 | 0 | 3 |
| 8 | 1 | 6 | 0 | 7 |
| 9 | 3 | 8 | 0 | 11 |
| 10 | 8 | 1 | 0 | 9 |
| 11 | 9 | 4 | 0 | 13 |
| 12 | 5 | 5 | 0 | 10 |
| 13 | 6 | 6 | 0 | 12 |
| 14 | 4 | 7 | 0 | 11 |
| 15 | 14 | 9 | 0 | 23 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 49.9% | 0.082 | 0.00 | 0.80 | 0.00 | 0.00 | 2.13 | 0.00 | 0.00 | 0.332 |
| rif_LDR02_muro_di_parata | 100 | 47.0% | 0.075 | 1.55 | 0.00 | 0.00 | 0.00 | 4.08 | 0.00 | 0.00 | 0.537 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 256 | 0.824 | 0.766 | 0.727 | 0.332 | 905 | 0.709 | 0.176 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 256 | 0.242 | 0.215 | 0.172 | 0.039 | 905 | 0.191 | 0.066 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | mano | 356 | 1.000 | 0.997 | 0.994 | 0.256 | 1055 | 1.000 | 0.382 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 356 | 0.480 | 0.438 | 0.379 | 0.042 | 1055 | 0.366 | 0.124 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 11.0% | 2.32 | 1.31 | 34.8% | 0.0% | 17.7% | 26.6% | 6.7% | 0.00 | 17.4% | 49.9% | 0.12 | 0.00 |
| rif_LDR02_muro_di_parata | 100 | 11.0% | 2.32 | 1.31 | 30.9% | 0.0% | 31.3% | 42.4% | 16.0% | 0.00 | 14.5% | 47.0% | 0.01 | 0.00 |
| Totale | 200 | 11.0% | 2.32 | 1.31 | 32.5% | 0.0% | 24.5% | 34.5% | 12.6% | 0.00 | 16.3% | 48.8% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

