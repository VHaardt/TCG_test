# Torneo v0.2 — /home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json

- Regole `v0.2`, configurazione `/home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json`; differenze da B0: {'pugno': 'sequenziale', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L')}
- IA: forte:30; partite: 200; tempo 1579s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 31.3% [29.9–32.6] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.5–12.0] (media 11.05) | 8–11 | ✅ |
| Partite al round 13+ | 38.0% [31.6–44.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.3–3.6] | <2% | ✅ |
| Vittorie prima del round 5 | 0.5% [0.1–2.8] | 0 | ❌ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=71) | 19.7% [12.1–30.4] | 20–35% | ❌ |
| Attacchi con opposizione | 39.9% [38.5–41.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 67.4% [66.0–68.8] (con ≥3: 27.8% [26.5–29.2]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.6% [36.2–39.0] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–1.3] (n=302) / 87.9% [83.9–91.1] (n=315) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.8% [14.2–17.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Risvegliato 97.7% [94.2–99.1] (n=174), LDR-05 Risvegliato 73.8% [64.5–81.3] (n=103) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 38.2% [31.4–45.5] (n=178) | | |
| Attacchi per partita | 23.3 | | |
| Pugno attaccante vuoto / pieno | 53.4% [51.9–54.9] / 12.3% [11.4–13.4] (gemme medie 0.86) | non >90% | |
| Pugno difensore vuoto / pieno | 50.7% [48.5–52.8] / 28.6% [26.6–30.5] (gemme medie 0.29) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1215, 1: 1771, 2: 1135, 3: 390, 4: 113, 5: 38, 6: 2} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 173, 'crepuscolo': 27} | | |
| G1 vince fra le partite finite al Crepuscolo | 59.3% [40.7–75.5] | | |
| G1 vince fra le partite arrivate al round 15 | 54.8% [37.8–70.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 48.4% [32.0–65.2] / 33.3% [15.2–58.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 53.3% [30.1–75.2]; 6.5% [1.8–20.7] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 8, '2-1': 5, '0-0': 3, '2-2': 3, '1-1': 2, '1-3': 2, '0-1': 2, '3-1': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=17) | 54.8% [37.8–70.8] / 35.3% [17.3–58.7] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15, 16: 2}; 47.1% [26.2–69.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 64.7% [41.3–82.7] / 35.3% [17.3–58.7]; 2.06 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–18.4] / 88.2% [65.7–96.7] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=6) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–39.0] / 54.5% [28.0–78.7]; 0.0% [0.0–39.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.4–6.4] / 19.4% [9.2–36.3]; 100.0% [61.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 1, 'perd:rim': 1, 'vinc:atk': 5, 'vinc:rim': 1} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=16) / turno di G2 (n=14) | 0.0% [0.0–19.4] / 0.0% [0.0–21.5] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=16) | 0.0% [0.0–19.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 61.3% [43.8–76.3] (16.1% [7.1–32.6]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 9, 'rif_LDR03_sanguinare_per_accendere': 8} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR05_scudi_armati 55% (n=31) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 39.0% [32.5–45.9], rif_LDR05_scudi_armati 61.0% [54.1–67.5]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.388 / 0.099 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.097 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.12 (0.07), rif_LDR05_scudi_armati 0.19 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 33.3% [31.9–34.6] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.18 (102 / 133); 56.8% [55.4–58.2] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.0% [51.0–53.0]; rif_LDR03_sanguinare_per_accendere 51.1%, rif_LDR05_scudi_armati 53.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 3.2% [2.5–4.1] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.323 (460) / 0.325 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 78 vittorie), LDR-05 R: 18.0 (49%, 122 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 2.79, NER-001 1.27, NER-017 1.08, NER-006 1.01, NER-013 0.94, ROS-011 0.86, NER-008 0.83, BLU-015 0.71, NER-009 0.69, ROS-019 0.58, BLU-001 0.58, NER-010 0.56 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.36, rif_LDR05_scudi_armati 0.16 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 21% (n=63), rif_LDR05_scudi_armati 12% (n=8) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.3% [11.4–13.4] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.52, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, BLU-021 61%, ROS-020 61%, NEU-013 61%, BLU-008 61%, NEU-009 61%, BLU-010 61%, collante 61%, NER-009 39%, ROS-011 39%, NER-017 39%, NER-010 39%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 39.0 [33–46] (200) |
| rif_LDR05_scudi_armati | 61.0 [54–67] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.64 | 0.00 | 0.00 / 0.00 | 2.56 | 0.00 | 3.7 (198) | 10 | K 60%, R 40% | 1.84 | 0.36 |
| rif_LDR05_scudi_armati | 3.54 | 0.00 | 2.79 / 0.00 | 0.00 | 0.66 | 4.3 (198) | 13 | B 48%, R 52% | 2.31 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.00/0.03/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.52/0.93 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/1.27/0.39/0.39 | 0.82/1.01/0.17/0.14 | 0.00/0.00/0.00/0.00 | 0.03/0.00/0.00/0.00 | 0.36/0.28/0.42/0.28 | 0.00/0.24/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.02/0.03 | 0.00/0.00/0.00/0.00 | 0.35/0.14/0.14/0.12 | 0.56/0.96/0.27/0.33 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.14/0.07 | 0.24/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.79/1.56/0.55 | 0.70/0.58/0.09/0.09 | 0.57/0.00/0.09/0.10 | 0.65/0.34/0.14/0.12 | 0.61/0.16/0.14/0.10 | 0.54/0.00/0.08/0.09 | 0.61/0.71/0.23/0.28 | 0.00/0.54/0.00/0.00 | 0.00/0.43/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.20/0.11/0.09 | 0.61/0.44/0.18/0.09 | 0.00/0.00/0.00/0.00 | 0.76/0.35/0.08/0.10 | 0.00/0.30/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.19/0.18/0.16 | 0.00/0.00/0.00/0.00 | 0.32/0.47/0.00/0.00 | 0.62/0.56/0.38/0.38 | 0.47/0.43/0.23/0.24 | 0.20/0.10/0.15/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.00/0.08/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.03/0.04/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.01/0.01 | 0.38/0.00/0.04/0.00 | 0.23/0.08/0.09/0.07 | 0.27/0.21/0.04/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.69 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.01 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.03 | 0.00 | 0.10 | 0.00 | 0.00 | 0.03 | 0.03 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.23 | 0.30 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 1.29 | 0.00 | 0.04 | 0.11 | 0.18 | 0.23 | 0.19 | 0.15 | 0.09 | 0.11 | 0.06 | 0.05 | 0.04 | 0.03 | 0.02 | 1.52 | 0.31 | 0.34 | 0.30 | 0.18 | 0.15 | 0.07 | 0.06 | 0.01 | 0.03 | 0.01 | 0.03 | 0.01 | 0.01 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.79 | 0.00 | 0.03 | 0.03 | 0.09 | 0.09 | 0.12 | 0.14 | 0.10 | 0.07 | 0.05 | 0.02 | 0.04 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 4 | 0 | 1 | 0 | 1 |
| 5 | 1 | 0 | 0 | 1 |
| 6 | 3 | 3 | 0 | 6 |
| 7 | 10 | 8 | 0 | 18 |
| 8 | 12 | 9 | 0 | 21 |
| 9 | 18 | 5 | 0 | 23 |
| 10 | 10 | 8 | 0 | 18 |
| 11 | 15 | 6 | 0 | 21 |
| 12 | 9 | 6 | 0 | 15 |
| 13 | 7 | 16 | 0 | 23 |
| 14 | 8 | 14 | 0 | 22 |
| 15 | 16 | 13 | 0 | 29 |
| 16 | 1 | 1 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 51.1% | 0.087 | 0.81 | 0.56 | 0.00 | 0.00 | 4.53 | 0.00 | 0.00 | 0.482 |
| rif_LDR05_scudi_armati | 200 | 53.0% | 0.109 | 0.16 | 0.00 | 0.00 | 0.00 | 2.74 | 0.00 | 0.00 | 0.315 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 432 | 0.935 | 0.928 | 0.914 | 0.352 | 1609 | 0.869 | 0.334 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 432 | 0.303 | 0.285 | 0.262 | 0.058 | 1609 | 0.234 | 0.100 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 579 | 0.883 | 0.857 | 0.829 | 0.430 | 2044 | 0.762 | 0.143 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 579 | 0.216 | 0.209 | 0.202 | 0.066 | 2044 | 0.162 | 0.038 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 13.5% | 2.29 | 2.34 | 26.0% | 1.0% | 16.7% | 33.8% | 10.8% | 0.00 | 13.9% | 51.1% | 0.09 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 13.5% | 2.29 | 2.34 | 42.0% | 1.0% | 16.7% | 31.7% | 10.5% | 0.00 | 20.2% | 53.0% | 0.09 | 0.00 |
| Totale | 400 | 13.5% | 2.29 | 2.34 | 32.8% | 1.0% | 16.7% | 32.7% | 10.7% | 0.00 | 16.9% | 52.0% | 0.09 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 0.383 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.82 |
| rif_LDR05_scudi_armati | 200 | 0.412 | 0.209 | 5.5% | 10.8% | 2.07 | 0.26 | 0.47 | 0.49 | 0.00 | 0.00 | 3.94 |

