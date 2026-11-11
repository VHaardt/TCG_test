# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 561s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 34.2% [32.3–36.2] | 30–45% | ✅ |
| Durata mediana (round) | 10.0 [10.0–11.0] (media 10.54) | 8–11 | ✅ |
| Partite al round 13+ | 21.0% [14.2–30.0] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=36) | 30.6% [18.0–46.9] | 20–35% | ✅ |
| Attacchi con opposizione | 23.5% [21.7–25.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 56.6% [54.5–58.8] (con ≥3: 18.5% [16.9–20.2]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 40.5% [38.4–42.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.9% [3.8–12.2] (n=145) / 87.7% [82.5–91.5] (n=203) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 20.3% [17.8–23.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 83.3% [43.6–97.0] (n=6), LDR-03 Risvegliato 99.1% [95.1–99.8] (n=111), LDR-06 Base 25.0% [4.6–69.9] (n=4), LDR-06 Risvegliato 83.6% [72.9–90.6] (n=67) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 21.3% [14.2–30.6] (n=94) | | |
| Attacchi per partita | 21.7 | | |
| Pugno attaccante vuoto / pieno | 62.3% [60.1–64.4] / 11.5% [10.1–12.9] (gemme medie 0.73) | non >90% | |
| Pugno difensore vuoto / pieno | 58.7% [55.7–61.7] / 24.2% [21.7–26.9] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 673, 1: 880, 2: 430, 3: 138, 4: 37, 5: 7, 6: 3} | | |
| Azioni legali per decisione | 5.6 | <60 | ✅ |
| Fine partita | {'colpo_finale': 93, 'crepuscolo': 7} | | |
| G1 vince fra le partite finite al Crepuscolo | 57.1% [25.0–84.2] | | |
| G1 vince fra le partite arrivate al round 15 | 66.7% [35.4–87.9] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 55.6% [26.7–81.1] / 60.0% [23.1–88.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 40.0% [11.8–76.9]; 11.1% [2.0–43.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-1': 2, '1-0': 2, '2-2': 1, '3-1': 1, '2-1': 1, '4-5': 1, '0-0': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=5) | 55.6% [26.7–81.1] / 60.0% [23.1–88.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 5}; 60.0% [23.1–88.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 20.0% [3.6–62.4] / 20.0% [3.6–62.4]; 1.40 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–43.4] / 60.0% [23.1–88.2] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 50.0% [9.5–90.5]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.0–8.5] / 33.3% [12.1–64.6]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:pronto': 3, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=4) / turno di G2 (n=3) | 0.0% [0.0–49.0] / 0.0% [0.0–56.2] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=4) | 0.0% [0.0–49.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 44.4% [18.9–73.3] (0.0% [0.0–29.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR03_sanguinare_per_accendere': 3, 'rif_LDR06_ferite_e_caccia': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR06_ferite_e_caccia 67% (n=9) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 71.0% [61.5–79.0], rif_LDR06_ferite_e_caccia 29.0% [21.0–38.5]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.409 / 0.091 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.091 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.05 (0.02), rif_LDR06_ferite_e_caccia 0.13 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 35.2% [33.3–37.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.44 (135 / 209); 64.7% [62.7–66.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.6% [49.0–52.1]; rif_LDR03_sanguinare_per_accendere 53.2%, rif_LDR06_ferite_e_caccia 47.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.7] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.429 (30) / 0.328 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 71 vittorie), LDR-06 G: 17.0 (49%, 29 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 1.56, VER-020 1.22, NER-008 1.13, NER-017 1.09, ROS-019 1.01, NER-001 0.83, NER-006 0.82, ROS-011 0.71, VER-008 0.70, NER-013 0.60, NER-010 0.60, NEU-001 0.45 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.44, rif_LDR06_ferite_e_caccia 2.09 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR06_ferite_e_caccia 0.13 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 39% (n=23), rif_LDR06_ferite_e_caccia 15% (n=13) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.5% [10.1–12.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.59, rif_LDR06_ferite_e_caccia 0.65; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | caccia 100%, ponte 100%, NER-017 100%, NER-009 100%, ROS-011 71%, NER-010 71%, NEU-001 29%, NEU-012 29%, VER-008 29%, collante 29%, VER-020 29%, VER-001 29%; oltre il 60%: NER-009, NER-017 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 71.0 [61–79] (100) |
| rif_LDR06_ferite_e_caccia | 29.0 [21–39] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.18 | 0.00 | 0.00 / 0.00 | 2.95 | 0.00 | 5.3 (100) | 10 | K 61%, R 39% | 1.93 | 0.44 |
| rif_LDR06_ferite_e_caccia | 3.61 | 0.00 | 1.56 / 0.04 | 0.00 | 0.09 | 5.1 (96) | 10 | G 56%, K 44% | 2.70 | 0.94 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.02/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.80/0.33 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/1.47/0.72/0.32 | 0.75/0.82/0.13/0.06 | 0.00/0.00/0.00/0.00 | 0.05/0.00/0.00/0.00 | 0.38/0.12/0.38/0.12 | 0.00/0.20/0.00/0.00 | 0.00/0.06/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.00/0.01/0.02 | 0.00/0.00/0.00/0.00 | 0.35/0.03/0.13/0.01 | 0.67/1.01/0.42/0.18 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.50/0.00/0.10/0.04 | 0.31/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.35/0.02/0.27 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.33/0.31/0.19 | 0.00/0.36/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.56/1.68/0.43 | 0.00/0.00/0.00/0.00 | 0.32/0.00/0.00/0.00 | 0.22/0.24/0.02/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.25/0.20/0.09/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.00/0.14/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.26/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.30/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.31/0.00/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.70/0.01/0.22 | 0.29/0.00/0.05/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.45/0.08/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.77 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.54 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 0.77 | 0.00 | 0.01 | 0.06 | 0.15 | 0.09 | 0.17 | 0.11 | 0.04 | 0.06 | 0.03 | 0.01 | 0.02 | 0.02 | 0.00 | 0.00 | 1.59 | 0.28 | 0.29 | 0.24 | 0.24 | 0.22 | 0.19 | 0.04 | 0.03 | 0.02 | 0.01 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.62 | 0.00 | 0.02 | 0.02 | 0.07 | 0.06 | 0.07 | 0.17 | 0.06 | 0.06 | 0.03 | 0.02 | 0.03 | 0.00 | 0.00 | 0.01 | 0.65 | 0.11 | 0.11 | 0.12 | 0.04 | 0.08 | 0.08 | 0.01 | 0.05 | 0.02 | 0.00 | 0.01 | 0.00 | 0.01 | 0.01 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 5 | 5 | 0 | 10 |
| 8 | 6 | 6 | 0 | 12 |
| 9 | 3 | 10 | 0 | 13 |
| 10 | 11 | 6 | 0 | 17 |
| 11 | 13 | 8 | 0 | 21 |
| 12 | 5 | 1 | 0 | 6 |
| 13 | 2 | 4 | 0 | 6 |
| 14 | 2 | 4 | 0 | 6 |
| 15 | 5 | 3 | 0 | 8 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 53.2% | 0.085 | 0.69 | 0.75 | 0.00 | 0.00 | 2.83 | 0.00 | 0.00 | 0.453 |
| rif_LDR06_ferite_e_caccia | 100 | 47.0% | 0.096 | 0.86 | 1.23 | 0.00 | 0.00 | 2.66 | 0.00 | 0.00 | 0.375 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 212 | 0.868 | 0.854 | 0.854 | 0.349 | 721 | 0.786 | 0.307 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 212 | 0.311 | 0.311 | 0.292 | 0.024 | 721 | 0.268 | 0.087 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 215 | 0.940 | 0.902 | 0.874 | 0.493 | 1020 | 0.878 | 0.246 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 215 | 0.247 | 0.219 | 0.219 | 0.060 | 1020 | 0.234 | 0.072 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 7.0% | 2.10 | 1.65 | 44.4% | 0.0% | 28.0% | 30.8% | 8.6% | 0.00 | 10.1% | 53.2% | 0.07 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 7.0% | 2.10 | 1.65 | 16.7% | 0.0% | 29.0% | 32.5% | 5.4% | 0.00 | 15.5% | 47.0% | 0.03 | 0.00 |
| Totale | 200 | 7.0% | 2.10 | 1.65 | 26.8% | 0.0% | 28.5% | 31.6% | 6.9% | 0.00 | 12.4% | 50.6% | 0.05 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

