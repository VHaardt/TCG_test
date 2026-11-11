# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 605s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 28.7% [26.9–30.5] | 30–45% | ❌ |
| Durata mediana (round) | 10.0 [9.0–11.0] (media 10.19) | 8–11 | ✅ |
| Partite al round 13+ | 18.0% [11.7–26.7] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=48) | 20.8% [11.7–34.3] | 20–35% | ✅ |
| Attacchi con opposizione | 31.6% [29.8–33.6] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 61.6% [59.4–63.7] (con ≥3: 19.4% [17.7–21.2]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 40.9% [38.9–42.9] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.1% [2.0–8.3] (n=169) / 86.9% [81.2–91.0] (n=183) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 16.6% [14.4–19.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 80.0% [37.6–96.4] (n=5), LDR-01 Risvegliato 67.3% [53.4–78.8] (n=49), LDR-03 Base 50.0% [9.5–90.5] (n=2), LDR-03 Risvegliato 100.0% [96.6–100.0] (n=110) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 18.5% [11.9–27.6] (n=92) | | |
| Attacchi per partita | 23.4 | | |
| Pugno attaccante vuoto / pieno | 55.0% [52.9–57.1] / 13.4% [12.0–14.9] (gemme medie 0.77) | non >90% | |
| Pugno difensore vuoto / pieno | 57.3% [54.2–60.3] / 27.0% [24.3–29.8] (gemme medie 0.24) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 701, 1: 861, 2: 552, 3: 154, 4: 61, 5: 16} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 93, 'crepuscolo': 7} | | |
| G1 vince fra le partite finite al Crepuscolo | 42.9% [15.8–75.0] | | |
| G1 vince fra le partite arrivate al round 15 | 42.9% [15.8–75.0] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 71.4% [35.9–91.8] / 60.0% [23.1–88.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 40.0% [11.8–76.9]; 14.3% [2.6–51.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-0': 2, '1-0': 2, '5-2': 1, '3-1': 1, '1-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=6) | 85.7% [48.7–97.4] / 66.7% [30.0–90.3] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 5, 16: 1}; 66.7% [30.0–90.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 50.0% [18.8–81.2] / 33.3% [9.7–70.0]; 2.50 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–39.0] / 83.3% [43.6–97.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=4) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–49.0] / 100.0% [34.2–100.0]; 0.0% [0.0–49.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.0% [1.6–9.8] / 57.1% [25.0–84.2]; 100.0% [51.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 1, 'vinc:atk': 4} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=0) / turno di G2 (n=1) | nan% [nan–nan] / 0.0% [0.0–79.3] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=0) | nan% [nan–nan] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 57.1% [25.0–84.2] (14.3% [2.6–51.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR03_sanguinare_per_accendere': 4, 'rif_LDR01_puntata_e_preda': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR03_sanguinare_per_accendere 43% (n=7) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 54.0% [44.3–63.4], rif_LDR03_sanguinare_per_accendere 46.0% [36.6–55.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.362 / 0.076 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.076 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.12 (0.00), rif_LDR03_sanguinare_per_accendere 0.14 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 36.1% [34.2–38.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.54 (87 / 167); 61.0% [59.0–62.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 45.5% [43.9–47.0]; rif_LDR01_puntata_e_preda 42.0%, rif_LDR03_sanguinare_per_accendere 48.2% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.377 (218) / 0.350 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 54 vittorie), LDR-03 R: 14.0 (35%, 46 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | NER-017 1.60, LDR-01 1.59, NER-001 1.35, ROS-016 1.13, ROS-011 0.96, ROS-019 0.90, NER-008 0.85, NER-006 0.84, NER-013 0.77, ROS-018 0.70, NER-009 0.68, NEU-006 0.44 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.63, rif_LDR03_sanguinare_per_accendere 1.53 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.06, rif_LDR03_sanguinare_per_accendere 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 0% (n=3), rif_LDR03_sanguinare_per_accendere 22% (n=45) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.4% [12.0–14.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR03_sanguinare_per_accendere 1.34; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, caccia 100%, VER-008 54%, VER-001 54%, ROS-016 54%, VER-011 54%, NER-017 46%, ROS-011 46%, NER-009 46%, NER-010 46%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR03_sanguinare_per_accendere |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 54.0 [44–63] (100) |
| rif_LDR03_sanguinare_per_accendere | 46.0 [37–56] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.78 | 0.00 | 1.59 / 0.00 | 0.00 | 0.00 | 3.9 (100) | 13 | G 39%, R 61% | 2.74 | 0.55 |
| rif_LDR03_sanguinare_per_accendere | 3.47 | 0.00 | 0.00 / 0.00 | 2.33 | 0.00 | 4.2 (100) | 8 | K 61%, R 39% | 1.78 | 0.55 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.59/1.71/0.53 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.44/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.39/0.22/0.06 | 0.66/0.12/0.48/0.30 | 0.73/0.34/0.18/0.05 | 0.00/0.37/0.00/0.00 | 0.68/0.00/0.14/0.06 | 0.58/0.18/0.16/0.08 | 0.75/1.13/0.03/0.51 | 0.71/0.70/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.40/0.31/0.19 | 0.21/0.12/0.12/0.10 | 0.00/0.00/0.00/0.00 | 0.63/0.40/0.05/0.32 | 0.55/0.00/0.00/0.00 | 0.60/0.00/0.11/0.09 | 0.60/0.34/0.15/0.07 | 0.64/0.41/0.32/0.22 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.00/0.08/0.01 | 0.34/0.01/0.04/0.01 | 0.32/0.04/0.06/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.03/0.03 | 0.32/0.32/0.00/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.08/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.81/0.70 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/1.35/0.51/0.45 | 0.71/0.84/0.12/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.24/0.41/0.24 | 0.00/0.20/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.01/0.02 | 0.00/0.00/0.00/0.00 | 0.32/0.07/0.15/0.06 | 0.56/0.90/0.31/0.30 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.00/0.09/0.02 | 0.29/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.97 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.16 | 0.02 | 0.00 | 0.02 | 0.06 | 0.12 | 0.00 | 0.00 | 0.25 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.63 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.49 | 0.00 | 0.01 | 0.05 | 0.04 | 0.01 | 0.13 | 0.08 | 0.09 | 0.04 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 100 | 1.10 | 0.00 | 0.05 | 0.08 | 0.21 | 0.09 | 0.19 | 0.15 | 0.12 | 0.07 | 0.07 | 0.03 | 0.03 | 0.01 | 1.34 | 0.28 | 0.19 | 0.37 | 0.21 | 0.08 | 0.07 | 0.06 | 0.06 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 3 | 0 | 3 |
| 6 | 1 | 2 | 0 | 3 |
| 7 | 2 | 1 | 0 | 3 |
| 8 | 10 | 6 | 0 | 16 |
| 9 | 12 | 5 | 0 | 17 |
| 10 | 11 | 5 | 0 | 16 |
| 11 | 5 | 10 | 0 | 15 |
| 12 | 4 | 5 | 0 | 9 |
| 13 | 5 | 4 | 0 | 9 |
| 14 | 1 | 1 | 0 | 2 |
| 15 | 3 | 3 | 0 | 6 |
| 16 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 42.0% | 0.074 | 0.00 | 0.63 | 0.00 | 0.00 | 2.85 | 0.00 | 0.00 | 0.289 |
| rif_LDR03_sanguinare_per_accendere | 100 | 48.2% | 0.079 | 0.67 | 0.86 | 0.00 | 0.00 | 4.30 | 0.00 | 0.00 | 0.452 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 229 | 0.812 | 0.760 | 0.742 | 0.367 | 1063 | 0.763 | 0.158 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 229 | 0.205 | 0.175 | 0.157 | 0.052 | 1063 | 0.157 | 0.039 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | mano | 197 | 0.929 | 0.904 | 0.883 | 0.350 | 856 | 0.904 | 0.333 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 197 | 0.279 | 0.274 | 0.269 | 0.071 | 856 | 0.259 | 0.096 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 7.0% | 1.98 | 1.92 | 39.1% | 3.0% | 14.7% | 26.9% | 3.1% | 0.00 | 21.8% | 42.0% | 0.11 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 100 | 7.0% | 1.98 | 1.92 | 33.3% | 3.0% | 15.7% | 29.9% | 11.1% | 0.00 | 13.2% | 48.2% | 0.05 | 0.00 |
| Totale | 200 | 7.0% | 1.98 | 1.92 | 36.1% | 3.0% | 15.2% | 28.4% | 7.6% | 0.00 | 17.0% | 45.5% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

