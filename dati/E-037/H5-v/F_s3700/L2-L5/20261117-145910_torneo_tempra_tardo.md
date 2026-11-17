# Torneo v0.2 — /home/claude/e037_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e037_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 1440s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 42.8% [40.9–44.8] | 30–45% | ✅ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 12.89) | 8–11 | ❌ |
| Partite al round 13+ | 65.0% [55.3–73.6] | ≤12% | ❌ |
| Partite oltre il 15 | 7.0% [3.4–13.7] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=43) | 27.9% [16.7–42.7] | 20–35% | ✅ |
| Attacchi con opposizione | 45.7% [43.8–47.7] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 74.0% [72.3–75.7] (con ≥3: 37.2% [35.3–39.1]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 31.7% [29.9–33.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 12.0% [8.1–17.5] (n=183) / 94.4% [87.5–97.6] (n=89) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.8% [8.8–13.2] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 58.3% [32.0–80.7] (n=12), LDR-02 Risvegliato 75.0% [55.1–88.0] (n=24), LDR-05 Base 40.0% [16.8–68.7] (n=10), LDR-05 Risvegliato 73.3% [61.0–82.9] (n=60) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 69.5% [58.9–78.4] (n=82) | | |
| Attacchi per partita | 24.6 | | |
| Pugno attaccante vuoto / pieno | 50.6% [48.6–52.7] / 11.1% [9.9–12.5] (gemme medie 0.96) | non >90% | |
| Pugno difensore vuoto / pieno | 49.0% [46.3–51.8] / 26.4% [24.1–29.0] (gemme medie 0.35) | non >90% | |
| Reazioni per scontro | 0.12 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 776, 1: 861, 2: 498, 3: 226, 4: 73, 5: 20, 6: 6} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'crepuscolo': 27, 'colpo_finale': 73} | | |
| G1 vince fra le partite finite al Crepuscolo | 92.6% [76.6–97.9] | | |
| G1 vince fra le partite arrivate al round 15 | 74.4% [58.9–85.4] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 7.7% [2.7–20.3] / 0.0% [0.0–56.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 100.0% [43.8–100.0]; 17.9% [9.0–32.7] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-1': 7, '2-0': 6, '2-3': 5, '2-2': 5, '1-0': 3, '4-2': 3, '3-2': 2, '4-3': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=6) | 15.4% [7.2–29.7] / 0.0% [0.0–39.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 3, 15: 3}; 16.7% [3.0–56.4] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 100.0% [61.0–100.0] / 50.0% [18.8–81.2]; 2.33 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–39.0] / 100.0% [61.0–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=0) / a Vite diverse; nessuno attacca a Vite pari | nan% [nan–nan] / 50.0% [18.8–81.2]; nan% [nan–nan] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 0.0% [0.0–3.7] / 0.0% [0.0–9.0]; nan% [nan–nan] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=11) / turno di G2 (n=11) | 0.0% [0.0–25.9] / 0.0% [0.0–25.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=11) | 0.0% [0.0–25.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 64.1% [48.4–77.3] (5.1% [1.4–16.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 3, 'rif_LDR05_scudi_armati': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 74% (n=39) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 55.0% [45.2–64.4], rif_LDR05_scudi_armati 45.0% [35.6–54.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.545 / 0.116 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.114 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.14 (0.00), rif_LDR05_scudi_armati 0.13 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 25.8% [24.1–27.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 54.3% [52.3–56.2] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 58.6% [57.4–59.8]; rif_LDR02_muro_di_parata 57.7%, rif_LDR05_scudi_armati 59.4% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.1% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.292 (242) / 0.312 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 55 vittorie), LDR-05 R: 18.0 (49%, 45 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.76, LDR-02 1.58, BLU-005 0.89, BLU-001 0.73, BLU-015 0.70, NEW-I04 0.69, BLU-008 0.58, ROS-020 0.55, BLU-023 0.52, ROS-018 0.48, NEU-013 0.47, ROS-005 0.45 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.47, rif_LDR05_scudi_armati 0.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 29% (n=7), rif_LDR05_scudi_armati 28% (n=36) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.1% [9.9–12.5] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, BLU-021 100%, NEU-009 100%, NEU-015 55%, NER-014 55%, RS 55%, NEU-003 55%, ROS-020 45%, BLU-010 45%, BLU-008 45%, NEU-013 45%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 55.0 [45–64] (100) |
| rif_LDR05_scudi_armati | 45.0 [36–55] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.06 | 0.00 | 1.58 / 0.00 | 0.00 | 1.40 | 4.8 (96) | 8 | B 84%, K 16% | 1.93 | 0.00 |
| rif_LDR05_scudi_armati | 4.45 | 0.00 | 3.76 / 0.00 | 0.00 | 0.83 | 4.6 (100) | 13 | B 46%, R 54% | 1.87 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR02_muro_di_parata | 1.58 | 0.00 |
| rif_LDR05_scudi_armati | 1.18 | 2.58 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/1.06/0.33/0.19 | 0.78/0.00/0.15/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.00/0.29/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.50/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.26/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.58/1.24/1.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.99/0.00/0.09/0.03 | 0.89/0.89/0.04/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.02/0.00/0.00 | 0.38/0.00/0.00/0.00 | 0.39/0.44/0.03/0.03 | 0.46/0.00/0.12/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.14/0.17/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.69/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.76/1.48/0.79 | 0.68/0.40/0.12/0.04 | 0.63/0.00/0.07/0.06 | 0.66/0.58/0.32/0.16 | 0.61/0.24/0.16/0.14 | 0.62/0.00/0.21/0.07 | 0.63/0.70/0.18/0.15 | 0.00/0.37/0.00/0.00 | 0.00/0.52/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.47/0.28/0.15 | 0.75/0.35/0.13/0.06 | 0.00/0.00/0.00/0.00 | 0.71/0.45/0.13/0.09 | 0.00/0.22/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.11/0.13/0.13 | 0.00/0.00/0.00/0.00 | 0.31/0.48/0.00/0.00 | 0.71/0.55/0.30/0.38 | 0.49/0.38/0.17/0.26 | 0.27/0.14/0.18/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.00/0.08/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.10/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.00/0.02/0.00 | 0.52/0.07/0.09/0.03 | 0.35/0.16/0.09/0.08 | 0.40/0.33/0.16/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.39 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 0.94 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.02 | 0.00 | 0.02 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.28 | 0.19 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 0.92 | 0.04 | 0.06 | 0.08 | 0.08 | 0.12 | 0.15 | 0.13 | 0.12 | 0.03 | 0.05 | 0.02 | 0.01 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.72 | 0.00 | 0.04 | 0.09 | 0.08 | 0.15 | 0.09 | 0.08 | 0.07 | 0.02 | 0.01 | 0.05 | 0.02 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 3 | 0 | 3 |
| 8 | 1 | 4 | 0 | 5 |
| 9 | 5 | 4 | 0 | 9 |
| 10 | 1 | 4 | 0 | 5 |
| 11 | 6 | 1 | 0 | 7 |
| 12 | 4 | 2 | 0 | 6 |
| 13 | 4 | 4 | 0 | 8 |
| 14 | 7 | 11 | 0 | 18 |
| 15 | 23 | 9 | 0 | 32 |
| 16 | 6 | 1 | 0 | 7 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 57.7% | 0.120 | 1.47 | 0.00 | 0.00 | 0.00 | 3.36 | 0.00 | 0.00 | 0.512 |
| rif_LDR05_scudi_armati | 100 | 59.4% | 0.111 | 0.12 | 0.00 | 0.00 | 0.00 | 2.92 | 0.00 | 0.00 | 0.451 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 320 | 0.997 | 0.928 | 0.869 | 0.253 | 1005 | 0.986 | 0.363 | 0.142 | 0.064 |
| rif_LDR02_muro_di_parata | Cicatrice | 320 | 0.344 | 0.247 | 0.209 | 0.028 | 1005 | 0.269 | 0.083 | 0.023 | 0.005 |
| rif_LDR05_scudi_armati | mano | 316 | 0.905 | 0.896 | 0.873 | 0.358 | 819 | 0.866 | 0.260 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 316 | 0.196 | 0.190 | 0.180 | 0.041 | 819 | 0.155 | 0.070 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 27.0% | 2.80 | 1.95 | 28.0% | 0.0% | 18.3% | 35.6% | 12.2% | 0.00 | 18.5% | 57.7% | 0.01 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 27.0% | 2.80 | 1.95 | 20.8% | 0.0% | 22.7% | 35.5% | 18.9% | 0.00 | 14.8% | 59.4% | 0.11 | 0.00 |
| Totale | 200 | 27.0% | 2.80 | 1.95 | 24.5% | 0.0% | 20.5% | 35.6% | 15.2% | 0.00 | 16.5% | 58.6% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 0.445 | 0.288 | 0.2% | 0.3% | 1.78 | 0.00 | 0.89 | 0.03 | 0.00 | 0.00 | 3.39 |
| rif_LDR05_scudi_armati | 100 | 0.472 | 0.233 | 0.0% | 0.0% | 1.51 | 0.00 | 1.03 | 0.88 | 0.00 | 0.00 | 4.40 |

