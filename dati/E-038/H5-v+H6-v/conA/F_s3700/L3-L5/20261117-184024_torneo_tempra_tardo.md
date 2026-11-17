# Torneo v0.2 — /root/in38/dati/E-038-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in38/dati/E-038-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1446s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 31.1% [29.7–32.4] | 30–45% | ✅ |
| Durata mediana (round) | 10.5 [10.0–11.0] (media 10.53) | 8–11 | ✅ |
| Partite al round 13+ | 29.5% [23.6–36.2] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–1.9] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=63) | 12.7% [6.6–23.1] | 20–35% | ❌ |
| Attacchi con opposizione | 39.4% [37.9–40.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 66.3% [64.8–67.7] (con ≥3: 28.5% [27.1–29.9]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.1% [37.6–40.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.5% [2.7–7.6] (n=286) / 90.5% [86.9–93.2] (n=338) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 17.8% [16.1–19.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 75.0% [30.1–95.4] (n=4), LDR-03 Risvegliato 100.0% [97.7–100.0] (n=164), LDR-05 Base 22.2% [6.3–54.7] (n=9), LDR-05 Risvegliato 71.8% [63.9–78.6] (n=142) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 29.4% [23.4–36.1] (n=194) | | |
| Attacchi per partita | 22.0 | | |
| Pugno attaccante vuoto / pieno | 55.3% [53.7–56.8] / 12.2% [11.2–13.2] (gemme medie 0.82) | non >90% | |
| Pugno difensore vuoto / pieno | 52.6% [50.3–54.8] / 26.9% [25.0–28.9] (gemme medie 0.28) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1139, 1: 1737, 2: 1048, 3: 316, 4: 132, 5: 29, 6: 1} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 188, 'crepuscolo': 12} | | |
| G1 vince fra le partite finite al Crepuscolo | 58.3% [32.0–80.7] | | |
| G1 vince fra le partite arrivate al round 15 | 66.7% [41.7–84.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 46.7% [24.8–69.9] / 42.9% [15.8–75.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 42.9% [15.8–75.0]; 0.0% [0.0–20.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-1': 3, '1-0': 3, '0-0': 2, '2-2': 2, '1-1': 1, '0-1': 1, '1-2': 1, '3-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=7) | 46.7% [24.8–69.9] / 42.9% [15.8–75.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 7}; 57.1% [25.0–84.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 71.4% [35.9–91.8] / 42.9% [15.8–75.0]; 2.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–35.4] / 85.7% [48.7–97.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 75.0% [30.1–95.4]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.5% [0.5–4.3] / 20.0% [7.0–45.2]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 1, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=12) / turno di G2 (n=9) | 0.0% [0.0–24.3] / 0.0% [0.0–29.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=12) | 0.0% [0.0–24.3] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 60.0% [35.7–80.2] (13.3% [3.7–37.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 4, 'rif_LDR03_sanguinare_per_accendere': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR05_scudi_armati 67% (n=15) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 43.0% [36.3–49.9], rif_LDR05_scudi_armati 57.0% [50.1–63.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.388 / 0.105 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.103 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.12 (0.07), rif_LDR05_scudi_armati 0.09 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 36.4% [35.0–37.9] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.25 (122 / 127); 57.1% [55.6–58.6] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.3% [50.3–52.3]; rif_LDR03_sanguinare_per_accendere 49.6%, rif_LDR05_scudi_armati 53.2% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.333 (390) / 0.327 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 86 vittorie), LDR-05 R: 18.0 (49%, 114 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.13, NER-017 1.27, NER-001 1.21, NER-006 1.03, NER-013 0.86, ROS-011 0.77, NER-008 0.73, BLU-015 0.68, NER-009 0.67, ROS-019 0.60, NER-010 0.54, BLU-021 0.50 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.21, rif_LDR05_scudi_armati 0.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 10% (n=40), rif_LDR05_scudi_armati 17% (n=23) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.2% [11.2–13.2] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.34, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, NEU-013 57%, ROS-020 57%, BLU-010 57%, collante 57%, NEU-009 57%, BLU-008 57%, BLU-021 57%, NER-009 43%, NER-010 43%, NER-017 43%, ROS-011 43%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 43.0 [36–50] (200) |
| rif_LDR05_scudi_armati | 57.0 [50–64] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.09 | 0.00 | 0.00 / 0.00 | 2.19 | 0.00 | 4.4 (199) | 10 | K 63%, R 37% | 1.89 | 0.42 |
| rif_LDR05_scudi_armati | 3.67 | 0.00 | 3.13 / 0.00 | 0.00 | 0.56 | 4.4 (199) | 13 | B 45%, R 55% | 2.16 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 0.84 | 2.29 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.39/0.72 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/1.21/0.33/0.38 | 0.83/1.03/0.17/0.10 | 0.00/0.00/0.00/0.00 | 0.01/0.00/0.00/0.00 | 0.29/0.14/0.19/0.14 | 0.00/0.25/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.28/0.10/0.14/0.07 | 0.64/0.93/0.24/0.29 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.09/0.03 | 0.72/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.13/1.74/0.58 | 0.50/0.39/0.06/0.09 | 0.52/0.00/0.07/0.12 | 0.62/0.37/0.19/0.12 | 0.48/0.17/0.14/0.13 | 0.48/0.00/0.12/0.06 | 0.56/0.68/0.32/0.23 | 0.00/0.50/0.00/0.00 | 0.00/0.40/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.28/0.23/0.17 | 0.65/0.38/0.15/0.11 | 0.00/0.00/0.00/0.00 | 0.52/0.28/0.07/0.12 | 0.00/0.35/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.21/0.24/0.18 | 0.00/0.00/0.00/0.00 | 0.36/0.33/0.00/0.00 | 0.56/0.33/0.23/0.20 | 0.49/0.35/0.27/0.27 | 0.23/0.10/0.17/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.00/0.06/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.26/0.03/0.04/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.00/0.03/0.02 | 0.34/0.04/0.01/0.04 | 0.28/0.09/0.09/0.07 | 0.33/0.27/0.10/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.59 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 0.93 | 0.00 | 0.07 | 0.01 | 0.01 | 0.01 | 0.04 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.12 | 0.21 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 1.16 | 0.00 | 0.03 | 0.07 | 0.17 | 0.18 | 0.17 | 0.18 | 0.12 | 0.15 | 0.03 | 0.04 | 0.00 | 0.01 | 0.00 | 1.34 | 0.31 | 0.25 | 0.32 | 0.17 | 0.11 | 0.07 | 0.01 | 0.04 | 0.03 | 0.03 | 0.00 | 0.01 | 0.00 | 0.01 |
| rif_LDR05_scudi_armati | 200 | 0.64 | 0.00 | 0.01 | 0.04 | 0.04 | 0.07 | 0.13 | 0.13 | 0.07 | 0.07 | 0.03 | 0.02 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | NER-002 stanca | NER-002 vita |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.56 | 0.17 |
| rif_LDR05_scudi_armati | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 2 | 1 | 0 | 3 |
| 6 | 4 | 7 | 0 | 11 |
| 7 | 11 | 7 | 0 | 18 |
| 8 | 5 | 8 | 0 | 13 |
| 9 | 17 | 13 | 0 | 30 |
| 10 | 11 | 14 | 0 | 25 |
| 11 | 18 | 14 | 0 | 32 |
| 12 | 3 | 6 | 0 | 9 |
| 13 | 15 | 12 | 0 | 27 |
| 14 | 4 | 13 | 0 | 17 |
| 15 | 10 | 5 | 0 | 15 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 49.6% | 0.089 | 0.66 | 0.56 | 0.00 | 0.00 | 3.76 | 0.00 | 0.00 | 0.460 |
| rif_LDR05_scudi_armati | 200 | 53.2% | 0.119 | 0.12 | 0.00 | 0.00 | 0.00 | 2.82 | 0.00 | 0.00 | 0.322 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 413 | 0.939 | 0.935 | 0.930 | 0.390 | 1672 | 0.855 | 0.318 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 413 | 0.329 | 0.317 | 0.308 | 0.058 | 1672 | 0.234 | 0.078 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 517 | 0.903 | 0.886 | 0.882 | 0.499 | 1800 | 0.757 | 0.147 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 517 | 0.141 | 0.135 | 0.133 | 0.035 | 1800 | 0.096 | 0.024 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 6.0% | 2.21 | 2.06 | 34.4% | 1.5% | 17.7% | 30.8% | 11.0% | 0.00 | 15.3% | 49.6% | 0.07 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 6.0% | 2.21 | 2.06 | 40.5% | 1.5% | 17.8% | 31.5% | 10.7% | 0.00 | 18.8% | 53.2% | 0.05 | 0.00 |
| Totale | 400 | 6.0% | 2.21 | 2.06 | 37.2% | 1.5% | 17.8% | 31.1% | 10.9% | 0.00 | 17.0% | 51.3% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 0.387 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.28 |
| rif_LDR05_scudi_armati | 200 | 0.400 | 0.193 | 0.0% | 0.0% | 1.39 | 0.24 | 0.44 | 0.47 | 0.00 | 0.00 | 4.32 |

