# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 1015s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 28.9% [27.2–30.7] | 30–45% | ❌ |
| Durata mediana (round) | 10.0 [9.0–11.0] (media 10.39) | 8–11 | ✅ |
| Partite al round 13+ | 24.0% [16.7–33.2] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=36) | 25.0% [13.8–41.1] | 20–35% | ✅ |
| Attacchi con opposizione | 35.0% [33.2–36.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 64.7% [62.6–66.7] (con ≥3: 24.2% [22.4–26.1]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 40.4% [38.5–42.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 10.3% [6.9–14.9] (n=224) / 92.3% [86.7–95.6] (n=142) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.3% [10.5–14.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 60.0% [23.1–88.2] (n=5), LDR-01 Risvegliato 61.0% [49.9–71.2] (n=77), LDR-05 Base 50.0% [29.0–71.0] (n=18), LDR-05 Risvegliato 87.0% [75.6–93.6] (n=54) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 26.4% [18.3–36.6] (n=87) | | |
| Attacchi per partita | 26.3 | | |
| Pugno attaccante vuoto / pieno | 49.0% [47.0–51.0] / 12.9% [11.6–14.2] (gemme medie 0.82) | non >90% | |
| Pugno difensore vuoto / pieno | 61.2% [58.3–64.0] / 25.4% [23.0–28.1] (gemme medie 0.22) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 773, 1: 844, 2: 722, 3: 193, 4: 65, 5: 28, 6: 4} | | |
| Azioni legali per decisione | 5.0 | <60 | ✅ |
| Fine partita | {'colpo_finale': 97, 'crepuscolo': 3} | | |
| G1 vince fra le partite finite al Crepuscolo | 33.3% [6.1–79.2] | | |
| G1 vince fra le partite arrivate al round 15 | 25.0% [7.1–59.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 12.5% [2.2–47.1] / 0.0% [0.0–79.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 0.0% [0.0–79.3]; 0.0% [0.0–32.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-3': 3, '0-1': 1, '3-2': 1, '2-1': 1, '1-2': 1, '2-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=1) | 12.5% [2.2–47.1] / 0.0% [0.0–79.3] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 1}; 100.0% [20.7–100.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 0.0% [0.0–79.3] / 0.0% [0.0–79.3]; 0.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–79.3] / 0.0% [0.0–79.3] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=0) / a Vite diverse; nessuno attacca a Vite pari | nan% [nan–nan] / 0.0% [0.0–79.3]; nan% [nan–nan] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 0.0% [0.0–3.7] / 0.0% [0.0–32.4]; nan% [nan–nan] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=4) / turno di G2 (n=3) | 0.0% [0.0–49.0] / 0.0% [0.0–56.2] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=4) | 0.0% [0.0–49.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 25.0% [7.1–59.1] (12.5% [2.2–47.1]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 25% (n=8) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 37.0% [28.2–46.8], rif_LDR05_scudi_armati 63.0% [53.2–71.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.357 / 0.076 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.075 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.05 (0.00), rif_LDR05_scudi_armati 0.15 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 29.3% [27.6–31.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.67 (57 / 110); 60.4% [58.5–62.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 44.1% [42.7–45.5]; rif_LDR01_puntata_e_preda 40.7%, rif_LDR05_scudi_armati 47.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.335 (436) / 0.336 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 37 vittorie), LDR-05 R: 18.0 (49%, 63 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 4.29, ROS-016 1.77, LDR-01 1.58, ROS-018 0.77, VER-011 0.66, BLU-015 0.59, BLU-008 0.57, VER-001 0.55, ROS-005 0.46, BLU-001 0.42, BLU-023 0.41, NEU-013 0.40 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.94, rif_LDR05_scudi_armati 0.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.08, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 17% (n=23), rif_LDR05_scudi_armati 38% (n=13) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.9% [11.6–14.2] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, NEU-013 63%, BLU-010 63%, BLU-021 63%, BLU-008 63%, collante 63%, ROS-020 63%, NEU-009 63%, ROS-016 37%, VER-011 37%, caccia 37%, VER-001 37%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 37.0 [28–47] (100) |
| rif_LDR05_scudi_armati | 63.0 [53–72] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.88 | 0.00 | 1.58 / 0.00 | 0.00 | 0.00 | 3.9 (99) | 13 | G 39%, R 61% | 2.43 | 0.54 |
| rif_LDR05_scudi_armati | 4.01 | 0.00 | 4.29 / 0.00 | 0.00 | 0.82 | 3.9 (100) | 12 | B 47%, R 53% | 1.76 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.58/1.76/0.73 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.38/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.36/0.16/0.13 | 0.68/0.11/0.50/0.33 | 0.79/0.47/0.17/0.13 | 0.00/0.29/0.00/0.00 | 0.65/0.00/0.40/0.14 | 0.65/0.24/0.37/0.14 | 0.61/1.77/0.07/0.70 | 0.70/0.89/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.40/0.28/0.18 | 0.21/0.07/0.13/0.11 | 0.00/0.00/0.00/0.00 | 0.62/0.55/0.04/0.39 | 0.60/0.00/0.00/0.00 | 0.58/0.00/0.07/0.05 | 0.68/0.66/0.18/0.16 | 0.59/0.38/0.22/0.31 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.05/0.00 | 0.49/0.06/0.09/0.06 | 0.34/0.13/0.25/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.04/0.06 | 0.28/0.40/0.02/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.11/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/4.29/1.90/0.84 | 0.63/0.42/0.24/0.15 | 0.50/0.00/0.14/0.07 | 0.64/0.57/0.38/0.26 | 0.52/0.30/0.41/0.27 | 0.49/0.00/0.22/0.21 | 0.53/0.59/0.31/0.20 | 0.00/0.38/0.00/0.00 | 0.00/0.41/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.40/0.28/0.33 | 0.60/0.32/0.16/0.06 | 0.00/0.00/0.00/0.00 | 0.60/0.44/0.14/0.15 | 0.00/0.29/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.23/0.45/0.25 | 0.00/0.00/0.00/0.00 | 0.38/0.65/0.00/0.00 | 0.52/0.35/0.27/0.37 | 0.47/0.36/0.23/0.38 | 0.18/0.03/0.11/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.00/0.12/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.06/0.17/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.01/0.02 | 0.29/0.01/0.04/0.01 | 0.35/0.22/0.18/0.21 | 0.28/0.30/0.06/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.07 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.12 | 0.00 | 0.00 | 0.01 | 0.18 | 0.12 | 0.00 | 0.00 | 0.23 | 0.11 | 0.00 | 0.01 | 0.00 | 0.01 | 0.07 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.06 | 0.00 | 0.04 | 0.01 | 0.00 | 0.01 | 0.08 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.02 | 0.00 | 0.04 | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | 0.19 | 0.26 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.85 | 0.01 | 0.05 | 0.11 | 0.16 | 0.09 | 0.18 | 0.06 | 0.10 | 0.05 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.79 | 0.03 | 0.05 | 0.09 | 0.04 | 0.15 | 0.14 | 0.09 | 0.05 | 0.06 | 0.03 | 0.01 | 0.03 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 1 | 0 | 1 |
| 7 | 3 | 9 | 0 | 12 |
| 8 | 11 | 9 | 0 | 20 |
| 9 | 8 | 1 | 0 | 9 |
| 10 | 10 | 2 | 0 | 12 |
| 11 | 8 | 7 | 0 | 15 |
| 12 | 4 | 3 | 0 | 7 |
| 13 | 3 | 2 | 0 | 5 |
| 14 | 2 | 9 | 0 | 11 |
| 15 | 2 | 6 | 0 | 8 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 40.7% | 0.058 | 0.00 | 0.94 | 0.00 | 0.00 | 3.93 | 0.00 | 0.00 | 0.328 |
| rif_LDR05_scudi_armati | 100 | 47.3% | 0.096 | 0.12 | 0.00 | 0.00 | 0.00 | 4.14 | 0.00 | 0.00 | 0.388 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 181 | 0.878 | 0.829 | 0.807 | 0.403 | 1163 | 0.798 | 0.231 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 181 | 0.144 | 0.116 | 0.110 | 0.028 | 1163 | 0.182 | 0.076 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 255 | 0.937 | 0.933 | 0.925 | 0.424 | 1030 | 0.824 | 0.227 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 255 | 0.180 | 0.176 | 0.173 | 0.059 | 1030 | 0.137 | 0.042 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 3.0% | 1.88 | 1.24 | 24.7% | 0.0% | 16.0% | 24.2% | 3.8% | 0.00 | 20.1% | 40.7% | 0.22 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 3.0% | 1.88 | 1.24 | 41.5% | 0.0% | 15.3% | 27.8% | 15.2% | 0.00 | 16.7% | 47.3% | 0.07 | 0.00 |
| Totale | 200 | 3.0% | 1.88 | 1.24 | 31.7% | 0.0% | 15.7% | 26.0% | 9.3% | 0.00 | 18.3% | 44.1% | 0.14 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

