# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 868s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 31.3% [29.5–33.3] | 30–45% | ✅ |
| Durata mediana (round) | 10.0 [9.0–10.5] (media 10.21) | 8–11 | ✅ |
| Partite al round 13+ | 29.0% [21.0–38.5] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=42) | 21.4% [11.7–35.9] | 20–35% | ✅ |
| Attacchi con opposizione | 35.4% [33.5–37.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 63.9% [61.7–65.9] (con ≥3: 24.6% [22.7–26.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 41.4% [39.4–43.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 9.1% [5.8–14.1] (n=186) / 87.4% [81.4–91.7] (n=159) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.5% [12.4–16.9] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 100.0% [34.2–100.0] (n=2), LDR-03 Risvegliato 100.0% [96.3–100.0] (n=99), LDR-05 Base 60.0% [35.7–80.2] (n=15), LDR-05 Risvegliato 62.5% [47.0–75.8] (n=40) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 26.4% [18.3–36.6] (n=87) | | |
| Attacchi per partita | 23.1 | | |
| Pugno attaccante vuoto / pieno | 51.8% [49.7–53.9] / 12.5% [11.1–13.9] (gemme medie 0.87) | non >90% | |
| Pugno difensore vuoto / pieno | 54.1% [51.0–57.0] / 26.6% [24.0–29.4] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 574, 1: 905, 2: 568, 3: 188, 4: 54, 5: 18} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 91, 'crepuscolo': 9} | | |
| G1 vince fra le partite finite al Crepuscolo | 88.9% [56.5–98.0] | | |
| G1 vince fra le partite arrivate al round 15 | 80.0% [49.0–94.3] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 40.0% [16.8–68.7] / 0.0% [0.0–49.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 100.0% [51.0–100.0]; 10.0% [1.8–40.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 4, '3-0': 2, '3-2': 2, '2-0': 1, '1-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=5) | 50.0% [23.7–76.3] / 0.0% [0.0–43.4] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 4, 16: 1}; 0.0% [0.0–43.4] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 80.0% [37.6–96.4] / 80.0% [37.6–96.4]; 3.20 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–43.4] / 100.0% [56.6–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=0) / a Vite diverse; nessuno attacca a Vite pari | nan% [nan–nan] / 80.0% [37.6–96.4]; nan% [nan–nan] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 0.0% [0.0–3.7] / 0.0% [0.0–27.8]; nan% [nan–nan] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=5) | 0.0% [0.0–43.4] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 80.0% [49.0–94.3] (10.0% [1.8–40.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 3, 'rif_LDR03_sanguinare_per_accendere': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR05_scudi_armati 80% (n=10) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 32.0% [23.7–41.7], rif_LDR05_scudi_armati 68.0% [58.3–76.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.379 / 0.092 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.091 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.13 (0.02), rif_LDR05_scudi_armati 0.16 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 32.1% [30.2–34.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.28 (57 / 71); 60.9% [58.9–62.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 47.9% [46.4–49.4]; rif_LDR03_sanguinare_per_accendere 44.8%, rif_LDR05_scudi_armati 51.2% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.302 (171) / 0.315 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 32 vittorie), LDR-05 R: 18.0 (49%, 68 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 2.80, NER-017 1.44, NER-001 1.09, NER-008 1.01, NER-006 0.98, NER-013 0.94, ROS-011 0.88, NER-009 0.62, BLU-015 0.60, NER-010 0.58, ROS-019 0.55, BLU-001 0.47 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.34, rif_LDR05_scudi_armati 0.10 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 24% (n=38), rif_LDR05_scudi_armati 0% (n=4) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.5% [11.1–13.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.36, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, NEU-013 68%, BLU-008 68%, ROS-020 68%, BLU-021 68%, BLU-010 68%, NEU-009 68%, collante 68%, NER-010 32%, NER-017 32%, NER-009 32%, ROS-011 32%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 32.0 [24–42] (100) |
| rif_LDR05_scudi_armati | 68.0 [58–76] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.12 | 0.00 | 0.00 / 0.00 | 2.11 | 0.00 | 4.2 (100) | 10 | K 60%, R 40% | 1.98 | 0.36 |
| rif_LDR05_scudi_armati | 3.82 | 0.00 | 2.80 / 0.00 | 0.00 | 0.89 | 4.2 (100) | 12 | B 48%, R 52% | 2.08 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.00/0.09/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.55/0.73 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/1.09/0.37/0.32 | 0.73/0.98/0.14/0.05 | 0.00/0.00/0.00/0.00 | 0.02/0.00/0.00/0.00 | 0.29/0.22/0.36/0.22 | 0.00/0.21/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.00/0.04/0.04 | 0.00/0.00/0.00/0.00 | 0.31/0.12/0.15/0.10 | 0.60/0.92/0.27/0.24 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.13/0.04 | 0.26/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.80/1.90/0.47 | 0.59/0.47/0.12/0.07 | 0.46/0.00/0.12/0.12 | 0.57/0.40/0.14/0.21 | 0.52/0.17/0.25/0.12 | 0.56/0.00/0.16/0.09 | 0.59/0.60/0.27/0.13 | 0.00/0.42/0.00/0.00 | 0.00/0.38/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.34/0.16/0.17 | 0.59/0.28/0.10/0.08 | 0.00/0.00/0.00/0.00 | 0.70/0.31/0.09/0.11 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.17/0.20/0.13 | 0.00/0.00/0.00/0.00 | 0.24/0.38/0.00/0.00 | 0.58/0.39/0.31/0.28 | 0.40/0.31/0.21/0.17 | 0.18/0.07/0.16/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.00/0.12/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.01/0.06/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.01/0.01 | 0.34/0.02/0.04/0.01 | 0.18/0.06/0.04/0.03 | 0.31/0.18/0.08/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.70 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.01 | 0.00 | 0.13 | 0.00 | 0.02 | 0.01 | 0.04 | 0.02 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.20 | 0.20 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 1.02 | 0.00 | 0.02 | 0.12 | 0.19 | 0.21 | 0.14 | 0.13 | 0.12 | 0.01 | 0.04 | 0.02 | 0.01 | 0.01 | 0.00 | 1.36 | 0.32 | 0.30 | 0.35 | 0.15 | 0.10 | 0.04 | 0.02 | 0.02 | 0.03 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.57 | 0.00 | 0.02 | 0.03 | 0.04 | 0.06 | 0.08 | 0.08 | 0.04 | 0.05 | 0.06 | 0.04 | 0.01 | 0.04 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 1 | 4 | 0 | 5 |
| 6 | 2 | 2 | 0 | 4 |
| 7 | 5 | 3 | 0 | 8 |
| 8 | 8 | 9 | 0 | 17 |
| 9 | 11 | 4 | 0 | 15 |
| 10 | 5 | 5 | 0 | 10 |
| 11 | 1 | 5 | 0 | 6 |
| 12 | 3 | 3 | 0 | 6 |
| 13 | 8 | 2 | 0 | 10 |
| 14 | 2 | 7 | 0 | 9 |
| 15 | 7 | 2 | 0 | 9 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 44.8% | 0.087 | 0.74 | 0.60 | 0.00 | 0.00 | 3.72 | 0.00 | 0.00 | 0.470 |
| rif_LDR05_scudi_armati | 100 | 51.2% | 0.097 | 0.10 | 0.00 | 0.00 | 0.00 | 2.56 | 0.00 | 0.00 | 0.298 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 232 | 0.909 | 0.892 | 0.888 | 0.349 | 852 | 0.797 | 0.303 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 232 | 0.358 | 0.306 | 0.293 | 0.056 | 852 | 0.306 | 0.122 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 250 | 0.840 | 0.816 | 0.800 | 0.412 | 973 | 0.691 | 0.141 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 250 | 0.196 | 0.176 | 0.172 | 0.064 | 973 | 0.133 | 0.030 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 9.0% | 2.04 | 1.88 | 23.4% | 5.0% | 16.7% | 30.5% | 10.1% | 0.00 | 16.0% | 44.8% | 0.08 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 9.0% | 2.04 | 1.88 | 44.2% | 5.0% | 16.3% | 30.2% | 10.3% | 0.00 | 18.8% | 51.2% | 0.03 | 0.00 |
| Totale | 200 | 9.0% | 2.04 | 1.88 | 31.8% | 5.0% | 16.5% | 30.4% | 10.2% | 0.00 | 17.4% | 47.9% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

