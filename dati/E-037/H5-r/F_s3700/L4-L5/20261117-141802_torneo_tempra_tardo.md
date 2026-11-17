# Torneo v0.2 — /root/in37/dati/E-037-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in37/dati/E-037-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 1554s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 38.0% [36.2–39.9] | 30–45% | ✅ |
| Durata mediana (round) | 12.5 [12.0–13.0] (media 12.47) | 8–11 | ❌ |
| Partite al round 13+ | 50.0% [40.4–59.6] | ≤12% | ❌ |
| Partite oltre il 15 | 3.0% [1.0–8.5] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=26) | 34.6% [19.4–53.8] | 20–35% | ✅ |
| Attacchi con opposizione | 36.6% [34.8–38.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 72.4% [70.6–74.2] (con ≥3: 32.3% [30.5–34.2]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 35.4% [33.6–37.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 12.6% [9.0–17.4] (n=238) / 78.1% [70.5–84.2] (n=137) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.1% [9.2–13.2] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 46.2% [23.2–70.9] (n=13), LDR-04 Risvegliato 55.6% [42.4–68.0] (n=54), LDR-05 Base 35.3% [17.3–58.7] (n=17), LDR-05 Risvegliato 79.2% [66.5–88.0] (n=53) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 54.2% [43.5–64.5] (n=83) | | |
| Attacchi per partita | 27.3 | | |
| Pugno attaccante vuoto / pieno | 50.4% [48.4–52.4] / 12.2% [11.0–13.6] (gemme medie 0.87) | non >90% | |
| Pugno difensore vuoto / pieno | 67.8% [65.2–70.2] / 18.0% [16.1–20.2] (gemme medie 0.21) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 902, 1: 1000, 2: 502, 3: 206, 4: 88, 5: 28, 6: 4} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 81, 'crepuscolo': 19} | | |
| G1 vince fra le partite finite al Crepuscolo | 63.2% [41.0–80.9] | | |
| G1 vince fra le partite arrivate al round 15 | 60.0% [40.7–76.6] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 24.0% [11.5–43.4] / 33.3% [9.7–70.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [9.7–70.0]; 12.0% [4.2–30.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-1': 6, '2-3': 4, '2-2': 3, '2-0': 2, '0-1': 2, '1-0': 2, '4-2': 1, '0-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=8) | 32.0% [17.2–51.6] / 37.5% [13.7–69.4] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 6, 16: 2}; 62.5% [30.6–86.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 62.5% [30.6–86.3] / 37.5% [13.7–69.4]; 2.50 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–32.4] / 87.5% [52.9–97.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 60.0% [23.1–88.2]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.0–8.5] / 12.0% [4.2–30.0]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 2, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=7) / turno di G2 (n=6) | 0.0% [0.0–35.4] / 0.0% [0.0–39.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=7) | 0.0% [0.0–35.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 48.0% [30.0–66.5] (8.0% [2.2–25.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 5, 'rif_LDR05_scudi_armati': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR05_scudi_armati 60% (n=25) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 36.0% [27.3–45.8], rif_LDR05_scudi_armati 64.0% [54.2–72.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.512 / 0.079 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.077 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.11 (0.00), rif_LDR05_scudi_armati 0.13 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 32.3% [30.6–34.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.44 (47 / 97); 60.0% [58.2–61.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 55.4% [54.1–56.6]; rif_LDR04_stanca_e_smonta 52.0%, rif_LDR05_scudi_armati 58.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.298 (201) / 0.309 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 12.0 (36%, 36 vittorie), LDR-05 R: 18.0 (49%, 64 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 7.18, BLU-015 1.23, LDR-05 1.04, ROS-018 0.85, VER-008 0.77, VER-014 0.67, VER-001 0.65, ROS-021 0.63, BLU-001 0.60, ROS-020 0.60, NEW-I04 0.55, VER-023 0.54 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.58, rif_LDR05_scudi_armati 0.16 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.36, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 15% (n=13), rif_LDR05_scudi_armati 54% (n=13) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.2% [11.0–13.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | BLU-010 100%, collante 100%, ponte 100%, NEU-009 100%, BLU-008 64%, NEU-013 64%, ROS-020 64%, BLU-021 64%, VER-001 36%, caccia 36%, VER-014 36%, VER-008 36%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 36.0 [27–46] (100) |
| rif_LDR05_scudi_armati | 64.0 [54–73] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.86 | 2.83 | 7.18 / 0.00 | 0.00 | 0.81 | 4.6 (98) | 10 | B 41%, G 59% | 1.87 | 0.68 |
| rif_LDR05_scudi_armati | 3.94 | 0.00 | 1.04 / 0.00 | 0.00 | 1.08 | 5.1 (99) | 13 | B 46%, R 54% | 1.82 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR04_stanca_e_smonta | 2.83 | 4.35 |
| rif_LDR05_scudi_armati | 0.00 | 1.04 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.75/0.76/0.21/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.45/0.37/0.28 | 0.33/0.00/0.13/0.10 | 0.92/1.43/0.48/0.49 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.65/0.05/0.53 | 0.81/0.00/0.00/0.00 | 0.62/0.00/0.19/0.08 | 0.00/0.00/0.00/0.00 | 0.37/0.26/0.19/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/7.18/1.87/0.72 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.25/0.54/0.02/0.22 | 0.00/0.00/0.00/0.00 | 0.38/0.26/0.05/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.00/0.19/0.13 | 0.37/0.00/0.03/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.77/0.02/0.31 | 0.35/0.04/0.02/0.00 | 0.37/0.00/0.22/0.07 | 0.00/0.22/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.00/0.00 | 0.75/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.55/0.00/0.00 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/1.04/1.88/0.51 | 0.67/0.45/0.07/0.07 | 0.63/0.00/0.11/0.06 | 0.63/0.31/0.15/0.12 | 0.67/0.30/0.39/0.26 | 0.64/0.00/0.27/0.11 | 0.68/1.02/0.37/0.50 | 0.00/0.36/0.00/0.00 | 0.00/0.48/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.33/0.18/0.19 | 0.78/0.26/0.11/0.07 | 0.00/0.00/0.00/0.00 | 0.76/0.24/0.08/0.06 | 0.00/0.29/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.34/0.31/0.27 | 0.00/0.00/0.00/0.00 | 0.43/0.85/0.00/0.00 | 0.72/0.60/0.39/0.43 | 0.46/0.63/0.36/0.47 | 0.26/0.12/0.23/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.00/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.05/0.13/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.02/0.03 | 0.28/0.01/0.01/0.01 | 0.41/0.22/0.15/0.19 | 0.37/0.43/0.19/0.25 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.52 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.02 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.01 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.60 | 0.00 | 0.15 | 0.02 | 0.00 | 0.02 | 0.07 | 0.03 | 0.16 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.29 | 0.00 | 0.00 | 0.16 | 0.45 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 0.81 | 0.02 | 0.01 | 0.05 | 0.08 | 0.08 | 0.08 | 0.13 | 0.18 | 0.04 | 0.06 | 0.03 | 0.02 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.84 | 0.02 | 0.02 | 0.06 | 0.11 | 0.14 | 0.13 | 0.19 | 0.02 | 0.02 | 0.04 | 0.04 | 0.03 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 8 | 3 | 1 | 0 | 4 |
| 9 | 4 | 1 | 0 | 5 |
| 10 | 4 | 4 | 0 | 8 |
| 11 | 11 | 11 | 0 | 22 |
| 12 | 8 | 3 | 0 | 11 |
| 13 | 3 | 9 | 0 | 12 |
| 14 | 2 | 11 | 0 | 13 |
| 15 | 13 | 9 | 0 | 22 |
| 16 | 2 | 1 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 52.0% | 0.063 | 1.89 | 0.69 | 0.00 | 0.00 | 3.32 | 0.00 | 0.00 | 0.499 |
| rif_LDR05_scudi_armati | 100 | 58.5% | 0.094 | 0.16 | 0.00 | 0.00 | 0.00 | 3.93 | 0.00 | 0.00 | 0.384 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 128 | 0.844 | 0.820 | 0.719 | 0.164 | 1205 | 0.844 | 0.429 | 0.175 | 0.043 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 128 | 0.242 | 0.195 | 0.133 | 0.062 | 1205 | 0.206 | 0.085 | 0.036 | 0.002 |
| rif_LDR05_scudi_armati | mano | 306 | 0.899 | 0.876 | 0.853 | 0.386 | 1091 | 0.781 | 0.236 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 306 | 0.186 | 0.176 | 0.160 | 0.042 | 1091 | 0.122 | 0.048 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 19.0% | 2.53 | 1.67 | 18.5% | 0.0% | 26.3% | 30.6% | 9.3% | 0.00 | 17.4% | 52.0% | 0.03 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 19.0% | 2.53 | 1.67 | 40.0% | 0.0% | 24.7% | 32.7% | 15.5% | 0.00 | 13.5% | 58.5% | 0.09 | 0.00 |
| Totale | 200 | 19.0% | 2.53 | 1.67 | 27.3% | 0.0% | 25.5% | 31.6% | 12.1% | 0.00 | 15.4% | 55.4% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 0.419 | 0.195 | 0.0% | 0.0% | 1.49 | 0.00 | 0.54 | 0.04 | 0.00 | 0.00 | 4.24 |
| rif_LDR05_scudi_armati | 100 | 0.316 | 0.165 | 0.0% | 0.0% | 1.28 | 0.33 | 0.51 | 1.01 | 0.00 | 0.00 | 5.43 |

