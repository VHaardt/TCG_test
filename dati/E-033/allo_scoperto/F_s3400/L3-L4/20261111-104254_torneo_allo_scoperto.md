# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 744s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 40.6% [38.6–42.6] | 30–45% | ✅ |
| Durata mediana (round) | 11.5 [10.0–13.0] (media 11.29) | 8–11 | ❌ |
| Partite al round 13+ | 44.0% [34.7–53.8] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=48) | 35.4% [23.4–49.6] | 20–35% | ❌ |
| Attacchi con opposizione | 30.9% [29.1–32.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 66.1% [64.0–68.0] (con ≥3: 24.0% [22.2–25.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.9% [34.9–38.8] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 8.1% [5.0–12.7] (n=198) / 76.4% [68.9–82.5] (n=148) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 13.0% [11.0–15.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 71.4% [35.9–91.8] (n=7), LDR-03 Risvegliato 98.8% [93.4–99.8] (n=82), LDR-04 Base 33.3% [12.1–64.6] (n=9), LDR-04 Risvegliato 67.7% [50.1–81.4] (n=31) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 41.6% [31.9–52.0] (n=89) | | |
| Attacchi per partita | 23.5 | | |
| Pugno attaccante vuoto / pieno | 54.3% [52.1–56.4] / 11.6% [10.3–13.0] (gemme medie 0.88) | non >90% | |
| Pugno difensore vuoto / pieno | 56.3% [53.4–59.2] / 21.4% [19.1–23.9] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 691, 1: 938, 2: 472, 3: 167, 4: 63, 5: 19, 6: 2} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 87, 'crepuscolo': 13} | | |
| G1 vince fra le partite finite al Crepuscolo | 69.2% [42.4–87.3] | | |
| G1 vince fra le partite arrivate al round 15 | 66.7% [43.7–83.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 27.8% [12.5–50.9] / 40.0% [11.8–76.9] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 40.0% [11.8–76.9]; 0.0% [0.0–17.6] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 5, '2-0': 2, '1-1': 2, '4-1': 2, '1-0': 2, '0-1': 1, '2-1': 1, '3-0': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=5) | 27.8% [12.5–50.9] / 40.0% [11.8–76.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 5}; 60.0% [23.1–88.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 80.0% [37.6–96.4] / 0.0% [0.0–43.4]; 1.60 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–43.4] / 100.0% [56.6–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 0.0% [0.0–56.2]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 11.1% [3.1–32.8]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=9) / turno di G2 (n=5) | 0.0% [0.0–29.9] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=9) | 0.0% [0.0–29.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 61.1% [38.6–79.7] (16.7% [5.8–39.2]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 3, 'rif_LDR03_sanguinare_per_accendere': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR04_stanca_e_smonta 67% (n=18) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 44.0% [34.7–53.8], rif_LDR04_stanca_e_smonta 56.0% [46.2–65.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.381 / 0.090 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.090 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.16 (0.07), rif_LDR04_stanca_e_smonta 0.09 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 33.5% [31.7–35.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.87 (75 / 112); 63.8% [61.8–65.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.9% [51.4–54.3]; rif_LDR03_sanguinare_per_accendere 55.1%, rif_LDR04_stanca_e_smonta 50.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.245 (13) / 0.328 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 44 vittorie), LDR-04 B: 14.0 (40%, 56 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 5.36, BLU-015 1.27, ROS-019 1.08, NER-017 1.03, NER-008 0.96, NER-001 0.93, ROS-011 0.82, VER-014 0.81, BLU-023 0.74, NER-006 0.69, NER-010 0.69, NER-013 0.63 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.20, rif_LDR04_stanca_e_smonta 2.14 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR04_stanca_e_smonta 0.15 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 39% (n=41), rif_LDR04_stanca_e_smonta 14% (n=7) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.6% [10.3–13.0] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.59, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | caccia 100%, ponte 100%, collante 56%, VER-023 56%, NEU-009 56%, RS 56%, VER-001 56%, VER-014 56%, VER-008 56%, NEU-003 56%, NEU-011 56%, BLU-010 56%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 44.0 [35–54] (100) |
| rif_LDR04_stanca_e_smonta | 56.0 [46–65] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.25 | 0.00 | 0.00 / 0.00 | 2.78 | 0.00 | 4.9 (99) | 8 | K 60%, R 40% | 2.16 | 0.22 |
| rif_LDR04_stanca_e_smonta | 4.82 | 2.34 | 5.36 / 0.00 | 0.00 | 0.46 | 4.6 (99) | 9 | B 41%, G 59% | 2.48 | 0.58 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.00/0.06/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.64/0.60 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.93/0.37/0.25 | 0.80/0.69/0.10/0.03 | 0.00/0.00/0.00/0.00 | 0.02/0.00/0.00/0.00 | 0.41/0.19/0.36/0.19 | 0.00/0.24/0.00/0.00 | 0.00/0.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.03/0.03 | 0.00/0.00/0.00/0.00 | 0.32/0.04/0.18/0.04 | 0.74/1.08/0.30/0.38 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.50/0.00/0.20/0.06 | 0.26/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.50/0.06/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.19/0.24/0.13 | 0.27/0.00/0.11/0.06 | 0.74/1.27/0.49/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.74/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.37/0.02/0.31 | 0.68/0.00/0.00/0.00 | 0.70/0.00/0.10/0.08 | 0.00/0.00/0.00/0.00 | 0.39/0.27/0.22/0.12 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/5.36/1.82/0.42 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.24/0.04/0.10 | 0.00/0.00/0.00/0.00 | 0.44/0.34/0.01/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.08/0.08/0.01 | 0.32/0.00/0.01/0.00 | 0.31/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.55/0.00/0.18 | 0.30/0.02/0.01/0.01 | 0.30/0.00/0.09/0.07 | 0.00/0.29/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.70 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.02 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.58 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.03 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.16 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 1.20 | 0.00 | 0.01 | 0.10 | 0.14 | 0.22 | 0.09 | 0.17 | 0.10 | 0.14 | 0.10 | 0.02 | 0.05 | 0.06 | 0.00 | 1.59 | 0.24 | 0.20 | 0.39 | 0.18 | 0.18 | 0.13 | 0.13 | 0.03 | 0.08 | 0.02 | 0.00 | 0.01 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 0.88 | 0.00 | 0.01 | 0.04 | 0.10 | 0.05 | 0.09 | 0.12 | 0.14 | 0.11 | 0.08 | 0.03 | 0.06 | 0.03 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 3 | 1 | 0 | 4 |
| 7 | 3 | 7 | 0 | 10 |
| 8 | 4 | 5 | 0 | 9 |
| 9 | 4 | 3 | 0 | 7 |
| 10 | 8 | 4 | 0 | 12 |
| 11 | 4 | 4 | 0 | 8 |
| 12 | 3 | 3 | 0 | 6 |
| 13 | 7 | 7 | 0 | 14 |
| 14 | 4 | 8 | 0 | 12 |
| 15 | 12 | 6 | 0 | 18 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 55.1% | 0.080 | 0.74 | 0.46 | 0.00 | 0.00 | 3.40 | 0.00 | 0.00 | 0.523 |
| rif_LDR04_stanca_e_smonta | 100 | 50.1% | 0.099 | 1.71 | 0.43 | 0.00 | 0.00 | 1.91 | 0.00 | 0.00 | 0.263 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 244 | 0.939 | 0.939 | 0.939 | 0.283 | 822 | 0.888 | 0.378 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 244 | 0.254 | 0.250 | 0.234 | 0.066 | 822 | 0.200 | 0.082 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 249 | 0.835 | 0.767 | 0.719 | 0.474 | 1037 | 0.705 | 0.120 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 249 | 0.129 | 0.120 | 0.116 | 0.036 | 1037 | 0.117 | 0.023 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 13.0% | 2.01 | 2.11 | 28.8% | 0.0% | 20.0% | 31.1% | 7.7% | 0.00 | 9.6% | 55.1% | 0.10 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 13.0% | 2.01 | 2.11 | 36.8% | 0.0% | 24.3% | 31.1% | 5.6% | 0.00 | 20.5% | 50.1% | 0.05 | 0.00 |
| Totale | 200 | 13.0% | 2.01 | 2.11 | 32.5% | 0.0% | 22.2% | 31.1% | 6.7% | 0.00 | 14.5% | 52.9% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

