# Torneo v0.2 — /home/claude/e037_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e037_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 556s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.6% [27.7–31.6] | 30–45% | ❌ |
| Durata mediana (round) | 8.0 [7.0–8.0] (media 8.69) | 8–11 | ✅ |
| Partite al round 13+ | 20.0% [13.3–28.9] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=34) | 11.8% [4.7–26.6] | 20–35% | ❌ |
| Attacchi con opposizione | 29.3% [27.4–31.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 53.6% [51.2–56.0] (con ≥3: 19.7% [17.9–21.7]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 48.1% [46.0–50.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 56.2% [49.8–62.4] (n=235) / 93.7% [89.0–96.4] (n=174) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.9% [13.8–18.3] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 34.6% [27.0–43.1] (n=130), LDR-03 Risvegliato 100.0% [96.2–100.0] (n=96), LDR-05 Base 100.0% [34.2–100.0] (n=2), LDR-05 Risvegliato 68.7% [56.8–78.5] (n=67) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 20.0% [13.2–29.1] (n=95) | | |
| Attacchi per partita | 21.3 | | |
| Pugno attaccante vuoto / pieno | 65.6% [63.3–67.8] / 12.0% [10.6–13.6] (gemme medie 0.51) | non >90% | |
| Pugno difensore vuoto / pieno | 40.0% [36.7–43.4] / 34.8% [31.6–38.1] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 627, 1: 961, 2: 380, 3: 108, 4: 42, 5: 12} | | |
| Azioni legali per decisione | 4.7 | <60 | ✅ |
| Fine partita | {'colpo_finale': 98, 'crepuscolo': 2} | | |
| G1 vince fra le partite finite al Crepuscolo | 100.0% [34.2–100.0] | | |
| G1 vince fra le partite arrivate al round 15 | 66.7% [20.8–93.9] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 33.3% [6.1–79.2] / 0.0% [0.0–79.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 100.0% [20.7–100.0]; 0.0% [0.0–56.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'3-1': 1, '1-0': 1, '2-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=1) | 33.3% [6.1–79.2] / 0.0% [0.0–79.3] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 1}; 0.0% [0.0–79.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 100.0% [20.7–100.0] / 100.0% [20.7–100.0]; 3.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–79.3] / 100.0% [20.7–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=0) / a Vite diverse; nessuno attacca a Vite pari | nan% [nan–nan] / 100.0% [20.7–100.0]; nan% [nan–nan] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 0.0% [0.0–3.7] / 0.0% [0.0–56.2]; nan% [nan–nan] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=7) / turno di G2 (n=6) | 0.0% [0.0–35.4] / 0.0% [0.0–39.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=7) | 0.0% [0.0–35.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 66.7% [20.8–93.9] (0.0% [0.0–56.2]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR05_scudi_armati 67% (n=3) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 72.0% [62.5–79.9], rif_LDR05_scudi_armati 28.0% [20.1–37.5]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.325 / 0.081 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.079 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.12 (0.05), rif_LDR05_scudi_armati 0.28 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 47.2% [45.1–49.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.05 (37 / 68); 66.8% [64.7–68.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 42.9% [41.2–44.7]; rif_LDR03_sanguinare_per_accendere 40.7%, rif_LDR05_scudi_armati 45.7% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.438 (186) / 0.394 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 72 vittorie), LDR-05 R: 18.0 (49%, 28 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 1.78, NER-006 1.21, NER-008 1.09, NER-010 0.99, ROS-011 0.98, NER-017 0.86, NER-001 0.80, NER-009 0.72, NER-013 0.67, ROS-019 0.57, BLU-001 0.49, BLU-015 0.43 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.10, rif_LDR05_scudi_armati 0.19 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 17% (n=12), rif_LDR05_scudi_armati 9% (n=22) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.0% [10.6–13.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.16, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, ROS-011 72%, NER-017 72%, NER-010 72%, NER-009 72%, caccia 72%, BLU-010 28%, NEU-013 28%, NEU-009 28%, ROS-020 28%, collante 28%, BLU-021 28%; oltre il 60%: NER-009, NER-017 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 72.0 [63–80] (100) |
| rif_LDR05_scudi_armati | 28.0 [20–37] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 4.20 | 0.00 | 0.00 / 0.00 | 3.53 | 0.00 | 3.0 (100) | 10 | K 63%, R 37% | 1.35 | 0.49 |
| rif_LDR05_scudi_armati | 3.27 | 0.00 | 1.78 / 0.00 | 0.00 | 0.34 | 3.4 (97) | 10 | B 44%, R 56% | 2.50 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 0.47 | 1.31 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.00/0.17/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/2.32/0.53 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.80/0.29/0.23 | 0.73/1.21/0.46/0.08 | 0.00/0.00/0.00/0.00 | 0.02/0.00/0.00/0.00 | 0.19/0.13/0.16/0.13 | 0.00/0.19/0.00/0.00 | 0.00/0.03/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.08/0.01 | 0.00/0.00/0.00/0.00 | 0.18/0.11/0.21/0.10 | 0.56/0.93/0.27/0.29 | 0.00/0.06/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.00/0.22/0.06 | 0.59/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/1.78/1.77/0.43 | 0.54/0.49/0.09/0.01 | 0.38/0.00/0.09/0.06 | 0.44/0.24/0.10/0.03 | 0.31/0.04/0.10/0.03 | 0.33/0.00/0.14/0.04 | 0.48/0.43/0.20/0.12 | 0.00/0.40/0.00/0.00 | 0.00/0.36/0.00/0.00 | 0.00/0.19/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.18/0.11/0.05 | 0.64/0.33/0.09/0.09 | 0.00/0.00/0.00/0.00 | 0.40/0.23/0.13/0.03 | 0.00/0.30/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.08/0.11/0.11 | 0.00/0.00/0.00/0.00 | 0.21/0.16/0.00/0.00 | 0.52/0.20/0.19/0.08 | 0.40/0.15/0.11/0.05 | 0.14/0.02/0.11/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.00/0.03/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.19/0.01/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.00/0.02/0.00 | 0.33/0.02/0.04/0.01 | 0.16/0.05/0.02/0.04 | 0.20/0.22/0.11/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.45 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 0.35 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.09 | 0.02 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 0.55 | 0.00 | 0.01 | 0.05 | 0.08 | 0.08 | 0.09 | 0.09 | 0.05 | 0.02 | 0.01 | 0.05 | 0.02 | 1.16 | 0.25 | 0.23 | 0.31 | 0.19 | 0.10 | 0.04 | 0.00 | 0.02 | 0.00 | 0.02 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.53 | 0.00 | 0.00 | 0.12 | 0.06 | 0.11 | 0.11 | 0.07 | 0.03 | 0.02 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | NER-002 stanca | NER-002 vita |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.45 | 0.14 |
| rif_LDR05_scudi_armati | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 1 | 3 | 0 | 4 |
| 6 | 10 | 11 | 0 | 21 |
| 7 | 11 | 12 | 0 | 23 |
| 8 | 11 | 5 | 0 | 16 |
| 9 | 4 | 3 | 0 | 7 |
| 10 | 2 | 1 | 0 | 3 |
| 11 | 1 | 3 | 0 | 4 |
| 12 | 0 | 2 | 0 | 2 |
| 13 | 5 | 5 | 0 | 10 |
| 14 | 1 | 6 | 0 | 7 |
| 15 | 2 | 1 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 40.7% | 0.066 | 0.49 | 0.61 | 0.00 | 0.00 | 3.48 | 0.00 | 0.00 | 0.400 |
| rif_LDR05_scudi_armati | 100 | 45.7% | 0.088 | 0.19 | 0.00 | 0.00 | 0.00 | 1.27 | 0.00 | 0.00 | 0.288 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 151 | 0.947 | 0.927 | 0.907 | 0.232 | 559 | 0.896 | 0.224 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 151 | 0.344 | 0.344 | 0.325 | 0.079 | 559 | 0.283 | 0.073 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 334 | 0.847 | 0.829 | 0.826 | 0.290 | 1086 | 0.759 | 0.101 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 334 | 0.216 | 0.204 | 0.201 | 0.084 | 1086 | 0.229 | 0.042 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 2.0% | 1.59 | 2.18 | 57.9% | 4.0% | 14.0% | 28.2% | 12.0% | 0.00 | 9.8% | 40.7% | 0.08 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 2.0% | 1.59 | 2.18 | 17.9% | 4.0% | 15.3% | 29.9% | 5.7% | 0.00 | 25.3% | 45.7% | 0.05 | 0.00 |
| Totale | 200 | 2.0% | 1.59 | 2.18 | 34.0% | 4.0% | 14.7% | 29.0% | 9.1% | 0.00 | 16.7% | 42.9% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 0.272 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 6.65 |
| rif_LDR05_scudi_armati | 100 | 0.304 | 0.138 | 0.0% | 0.0% | 1.17 | 0.32 | 0.18 | 0.34 | 0.00 | 0.00 | 3.59 |

