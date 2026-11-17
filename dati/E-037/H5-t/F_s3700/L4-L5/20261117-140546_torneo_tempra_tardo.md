# Torneo v0.2 — /home/claude/e037_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e037_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 721s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 33.4% [31.5–35.3] | 30–45% | ✅ |
| Durata mediana (round) | 10.5 [10.0–11.0] (media 10.65) | 8–11 | ✅ |
| Partite al round 13+ | 34.0% [25.5–43.7] | ≤12% | ❌ |
| Partite oltre il 15 | 2.0% [0.6–7.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=50) | 16.0% [8.3–28.5] | 20–35% | ❌ |
| Attacchi con opposizione | 31.2% [29.3–33.1] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 65.6% [63.5–67.6] (con ≥3: 28.6% [26.7–30.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 43.7% [41.7–45.7] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 74.3% [69.0–79.0] (n=288) / 80.0% [73.0–85.5] (n=155) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.4% [10.5–14.5] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 22.5% [17.4–28.6] (n=213), LDR-04 Risvegliato 58.1% [43.3–71.6] (n=43), LDR-05 Base 0.0% [0.0–79.3] (n=1), LDR-05 Risvegliato 71.6% [61.0–80.3] (n=81) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 38.5% [28.4–49.6] (n=78) | | |
| Attacchi per partita | 22.9 | | |
| Pugno attaccante vuoto / pieno | 58.8% [56.6–61.0] / 13.3% [11.8–14.9] (gemme medie 0.66) | non >90% | |
| Pugno difensore vuoto / pieno | 51.1% [47.9–54.2] / 27.5% [24.8–30.4] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 772, 1: 926, 2: 373, 3: 142, 4: 65, 5: 15, 6: 2} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'crepuscolo': 16, 'colpo_finale': 84} | | |
| G1 vince fra le partite finite al Crepuscolo | 62.5% [38.6–81.5] | | |
| G1 vince fra le partite arrivate al round 15 | 58.8% [36.0–78.4] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 35.3% [17.3–58.7] / 50.0% [18.8–81.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [18.8–81.2]; 11.8% [3.3–34.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-0': 3, '1-0': 3, '1-2': 2, '0-0': 2, '3-1': 2, '5-2': 1, '2-2': 1, '1-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=8) | 47.1% [26.2–69.0] / 50.0% [21.5–78.5] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 2, 15: 6}; 50.0% [21.5–78.5] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 62.5% [30.6–86.3] / 50.0% [21.5–78.5]; 2.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–32.4] / 62.5% [30.6–86.3] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=4) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–49.0] / 100.0% [51.0–100.0]; 0.0% [0.0–49.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.0% [1.6–9.8] / 23.5% [9.6–47.3]; 100.0% [51.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 3, 'vinc:atk': 4} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=3) / turno di G2 (n=3) | 0.0% [0.0–56.2] / 0.0% [0.0–56.2] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=3) | 0.0% [0.0–56.2] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 76.5% [52.7–90.4] (17.6% [6.2–41.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 5, 'rif_LDR04_stanca_e_smonta': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR05_scudi_armati 59% (n=17) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 69.0% [59.4–77.2], rif_LDR05_scudi_armati 31.0% [22.8–40.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.461 / 0.077 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.076 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.14 (0.00), rif_LDR05_scudi_armati 0.16 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 39.0% [37.1–41.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.20 (36 / 84); 64.8% [62.8–66.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 55.0% [53.6–56.5]; rif_LDR04_stanca_e_smonta 50.3%, rif_LDR05_scudi_armati 59.6% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.379 (172) / 0.341 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 12.0 (36%, 69 vittorie), LDR-05 R: 18.0 (49%, 31 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 4.74, LDR-05 3.00, BLU-015 0.87, VER-008 0.85, VER-014 0.58, VER-001 0.56, BLU-023 0.43, NEW-I04 0.43, ROS-001 0.39, BLU-001 0.35, ROS-019 0.34, VER-023 0.33 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.22, rif_LDR05_scudi_armati 0.14 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.31, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 50% (n=2), rif_LDR05_scudi_armati 15% (n=48) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.3% [11.8–14.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, NEU-009 100%, collante 100%, BLU-010 100%, VER-023 69%, caccia 69%, VER-014 69%, VER-001 69%, VER-008 69%, BLU-008 31%, NEU-013 31%, ROS-020 31%; oltre il 60%: VER-001, VER-008, VER-023 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 69.0 [59–77] (100) |
| rif_LDR05_scudi_armati | 31.0 [23–41] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.04 | 1.85 | 4.74 / 0.00 | 0.00 | 0.29 | 2.9 (100) | 10 | B 41%, G 59% | 1.68 | 0.53 |
| rif_LDR05_scudi_armati | 3.48 | 0.00 | 3.00 / 0.00 | 0.00 | 0.59 | 4.4 (100) | 13 | B 44%, R 56% | 2.13 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR04_stanca_e_smonta | 1.85 | 2.89 |
| rif_LDR05_scudi_armati | 0.50 | 2.50 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.44/0.31/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.39/0.38/0.25 | 0.36/0.00/0.25/0.10 | 0.81/1.27/0.52/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.56/0.13/0.40 | 0.72/0.00/0.00/0.00 | 0.47/0.00/0.24/0.07 | 0.00/0.00/0.00/0.00 | 0.31/0.31/0.16/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/4.74/2.65/0.45 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.16/0.33/0.01/0.11 | 0.00/0.00/0.00/0.00 | 0.31/0.19/0.06/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.00/0.27/0.13 | 0.29/0.00/0.04/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.50/0.85/0.03/0.39 | 0.27/0.05/0.06/0.03 | 0.34/0.00/0.25/0.13 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.00/0.00 | 0.55/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.43/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.00/1.78/0.64 | 0.58/0.26/0.12/0.06 | 0.45/0.00/0.06/0.07 | 0.39/0.31/0.16/0.10 | 0.50/0.23/0.20/0.17 | 0.52/0.00/0.06/0.09 | 0.55/0.47/0.17/0.16 | 0.00/0.32/0.00/0.00 | 0.00/0.43/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.22/0.17/0.14 | 0.70/0.39/0.22/0.07 | 0.00/0.00/0.00/0.00 | 0.65/0.26/0.11/0.04 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.17/0.25/0.14 | 0.00/0.00/0.00/0.00 | 0.27/0.28/0.00/0.00 | 0.52/0.29/0.20/0.27 | 0.40/0.21/0.18/0.20 | 0.20/0.04/0.16/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.00/0.04/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.03/0.12/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.00/0.02/0.03 | 0.32/0.06/0.04/0.04 | 0.28/0.09/0.10/0.07 | 0.29/0.34/0.18/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.32 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 0.76 | 0.00 | 0.09 | 0.01 | 0.00 | 0.03 | 0.05 | 0.02 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.18 | 0.09 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 0.43 | 0.00 | 0.01 | 0.02 | 0.04 | 0.07 | 0.10 | 0.09 | 0.04 | 0.00 | 0.03 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.99 | 0.01 | 0.09 | 0.14 | 0.18 | 0.16 | 0.12 | 0.10 | 0.06 | 0.03 | 0.06 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 3 | 5 | 0 | 8 |
| 7 | 13 | 1 | 0 | 14 |
| 8 | 6 | 4 | 0 | 10 |
| 9 | 3 | 4 | 0 | 7 |
| 10 | 7 | 4 | 0 | 11 |
| 11 | 7 | 4 | 0 | 11 |
| 12 | 2 | 3 | 0 | 5 |
| 13 | 5 | 5 | 0 | 10 |
| 14 | 1 | 6 | 0 | 7 |
| 15 | 9 | 6 | 0 | 15 |
| 16 | 1 | 1 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 50.3% | 0.067 | 1.56 | 0.66 | 0.00 | 0.00 | 2.70 | 0.00 | 0.00 | 0.422 |
| rif_LDR05_scudi_armati | 100 | 59.6% | 0.084 | 0.14 | 0.00 | 0.00 | 0.00 | 2.56 | 0.00 | 0.00 | 0.360 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 100 | 0.840 | 0.770 | 0.730 | 0.100 | 869 | 0.789 | 0.339 | 0.159 | 0.047 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 100 | 0.260 | 0.200 | 0.180 | 0.120 | 869 | 0.204 | 0.087 | 0.024 | 0.002 |
| rif_LDR05_scudi_armati | mano | 375 | 0.883 | 0.856 | 0.837 | 0.256 | 951 | 0.821 | 0.143 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 375 | 0.165 | 0.157 | 0.155 | 0.043 | 951 | 0.184 | 0.030 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 16.0% | 2.02 | 2.24 | 43.8% | 0.0% | 20.0% | 27.6% | 7.5% | 0.00 | 15.8% | 50.3% | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 16.0% | 2.02 | 2.24 | 24.4% | 0.0% | 22.0% | 33.7% | 14.3% | 0.00 | 12.2% | 59.6% | 0.07 | 0.00 |
| Totale | 200 | 16.0% | 2.02 | 2.24 | 31.7% | 0.0% | 21.0% | 30.6% | 10.8% | 0.00 | 14.0% | 55.0% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 0.388 | 0.163 | 0.0% | 0.0% | 0.80 | 0.00 | 0.51 | 0.05 | 0.00 | 0.00 | 5.69 |
| rif_LDR05_scudi_armati | 100 | 0.256 | 0.109 | 0.0% | 0.0% | 0.85 | 0.40 | 0.50 | 0.81 | 0.00 | 0.00 | 4.34 |

