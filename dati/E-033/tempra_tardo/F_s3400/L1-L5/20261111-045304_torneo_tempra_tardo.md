# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 1003s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.9% [28.2–31.7] | 30–45% | ❌ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 11.05) | 8–11 | ✅ |
| Partite al round 13+ | 30.0% [21.9–39.6] | ≤12% | ❌ |
| Partite oltre il 15 | 3.0% [1.0–8.5] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=34) | 29.4% [16.8–46.2] | 20–35% | ✅ |
| Attacchi con opposizione | 37.4% [35.6–39.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 69.1% [67.1–71.0] (con ≥3: 29.9% [28.0–31.9]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.7% [37.8–41.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.8% [2.6–8.5] (n=210) / 88.6% [82.5–92.8] (n=149) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.7% [10.8–14.8] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 33.3% [6.1–79.2] (n=3), LDR-01 Risvegliato 57.5% [46.1–68.2] (n=73), LDR-05 Base 85.7% [48.7–97.4] (n=7), LDR-05 Risvegliato 74.6% [62.2–83.9] (n=59) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 31.6% [23.1–41.5] (n=95) | | |
| Attacchi per partita | 26.2 | | |
| Pugno attaccante vuoto / pieno | 47.8% [45.8–49.8] / 13.4% [12.1–14.8] (gemme medie 0.85) | non >90% | |
| Pugno difensore vuoto / pieno | 57.3% [54.5–60.2] / 24.8% [22.4–27.4] (gemme medie 0.25) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 760, 1: 822, 2: 721, 3: 205, 4: 67, 5: 42, 6: 8} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 91, 'crepuscolo': 9} | | |
| G1 vince fra le partite finite al Crepuscolo | 66.7% [35.4–87.9] | | |
| G1 vince fra le partite arrivate al round 15 | 58.3% [32.0–80.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 25.0% [8.9–53.2] / 66.7% [20.8–93.9] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 0.0% [0.0–56.2]; 25.0% [8.9–53.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 2, '2-1': 2, '3-2': 2, '1-1': 2, '2-0': 1, '0-1': 1, '4-2': 1, '2-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=5) | 41.7% [19.3–68.0] / 40.0% [11.8–76.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 3, 16: 2}; 60.0% [23.1–88.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 40.0% [11.8–76.9] / 40.0% [11.8–76.9]; 1.60 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–43.4] / 60.0% [23.1–88.2] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 66.7% [20.8–93.9]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 16.7% [4.7–44.8]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:pronto': 2, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=6) | 0.0% [0.0–43.4] / 0.0% [0.0–39.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 33.3% [13.8–60.9] (0.0% [0.0–24.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 3, 'rif_LDR01_puntata_e_preda': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 58% (n=12) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 46.0% [36.6–55.7], rif_LDR05_scudi_armati 54.0% [44.3–63.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.358 / 0.085 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.083 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.07 (0.00), rif_LDR05_scudi_armati 0.21 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 29.6% [27.8–31.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.69 (51 / 118); 58.3% [56.4–60.2] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.3% [48.9–51.6]; rif_LDR01_puntata_e_preda 49.0%, rif_LDR05_scudi_armati 51.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.318 (480) / 0.314 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 46 vittorie), LDR-05 R: 18.0 (49%, 54 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.92, ROS-016 1.77, LDR-01 1.76, VER-011 1.03, ROS-018 0.73, BLU-015 0.65, VER-001 0.60, BLU-008 0.58, BLU-021 0.55, BLU-001 0.50, ROS-001 0.44, BLU-023 0.44 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.78, rif_LDR05_scudi_armati 0.11 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.08, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 25% (n=16), rif_LDR05_scudi_armati 33% (n=18) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.4% [12.1–14.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, ROS-020 54%, NEU-013 54%, BLU-021 54%, collante 54%, BLU-010 54%, NEU-009 54%, BLU-008 54%, caccia 46%, VER-011 46%, ROS-016 46%, VER-008 46%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 46.0 [37–56] (100) |
| rif_LDR05_scudi_armati | 54.0 [44–63] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.18 | 0.00 | 1.76 / 0.00 | 0.00 | 0.00 | 3.8 (100) | 13 | G 39%, R 61% | 2.09 | 0.61 |
| rif_LDR05_scudi_armati | 3.87 | 0.00 | 3.92 / 0.00 | 0.00 | 0.92 | 4.1 (100) | 13 | B 47%, R 53% | 1.88 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.76/1.87/0.80 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.37/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.54/0.28/0.12 | 0.64/0.17/0.57/0.37 | 0.78/0.47/0.22/0.12 | 0.00/0.27/0.00/0.00 | 0.70/0.00/0.22/0.08 | 0.68/0.25/0.19/0.22 | 0.64/1.77/0.06/0.64 | 0.77/0.96/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.44/0.24/0.26 | 0.26/0.04/0.15/0.09 | 0.00/0.00/0.00/0.00 | 0.60/0.60/0.03/0.43 | 0.68/0.00/0.00/0.00 | 0.65/0.00/0.09/0.14 | 0.71/1.03/0.24/0.22 | 0.50/0.28/0.37/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.10/0.00 | 0.49/0.08/0.13/0.05 | 0.37/0.13/0.20/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.04/0.04 | 0.32/0.43/0.05/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.92/1.72/0.87 | 0.65/0.50/0.19/0.14 | 0.51/0.00/0.23/0.16 | 0.54/0.58/0.27/0.21 | 0.55/0.30/0.35/0.22 | 0.51/0.00/0.24/0.17 | 0.61/0.65/0.16/0.28 | 0.00/0.55/0.00/0.00 | 0.00/0.44/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.31/0.25/0.16 | 0.68/0.34/0.10/0.12 | 0.00/0.00/0.00/0.00 | 0.58/0.37/0.13/0.14 | 0.00/0.31/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.28/0.34/0.27 | 0.00/0.00/0.00/0.00 | 0.37/0.51/0.00/0.00 | 0.57/0.30/0.30/0.31 | 0.47/0.28/0.31/0.27 | 0.21/0.06/0.11/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.00/0.11/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.08/0.19/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.00/0.04/0.01 | 0.36/0.04/0.03/0.02 | 0.33/0.15/0.17/0.11 | 0.22/0.35/0.13/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.94 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.19 | 0.00 | 0.00 | 0.00 | 0.13 | 0.04 | 0.00 | 0.00 | 0.20 | 0.04 | 0.00 | 0.02 | 0.00 | 0.01 | 0.07 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 0.95 | 0.00 | 0.13 | 0.02 | 0.01 | 0.01 | 0.07 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.21 | 0.00 | 0.00 | 0.12 | 0.21 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.79 | 0.00 | 0.02 | 0.04 | 0.12 | 0.10 | 0.15 | 0.15 | 0.11 | 0.05 | 0.02 | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.77 | 0.01 | 0.08 | 0.08 | 0.13 | 0.09 | 0.10 | 0.12 | 0.04 | 0.04 | 0.06 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 1 | 0 | 1 |
| 7 | 2 | 4 | 0 | 6 |
| 8 | 5 | 6 | 0 | 11 |
| 9 | 10 | 3 | 0 | 13 |
| 10 | 9 | 5 | 0 | 14 |
| 11 | 7 | 9 | 0 | 16 |
| 12 | 5 | 4 | 0 | 9 |
| 13 | 6 | 1 | 0 | 7 |
| 14 | 3 | 8 | 0 | 11 |
| 15 | 4 | 5 | 0 | 9 |
| 16 | 3 | 0 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 49.0% | 0.062 | 0.00 | 0.78 | 0.00 | 0.00 | 4.10 | 0.00 | 0.00 | 0.326 |
| rif_LDR05_scudi_armati | 100 | 51.5% | 0.107 | 0.11 | 0.00 | 0.00 | 0.00 | 3.87 | 0.00 | 0.00 | 0.388 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 203 | 0.916 | 0.872 | 0.823 | 0.350 | 1065 | 0.803 | 0.202 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 203 | 0.256 | 0.212 | 0.187 | 0.034 | 1065 | 0.202 | 0.056 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 285 | 0.853 | 0.839 | 0.821 | 0.435 | 1072 | 0.785 | 0.244 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 285 | 0.207 | 0.186 | 0.165 | 0.074 | 1072 | 0.174 | 0.067 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 9.0% | 2.06 | 1.54 | 29.4% | 0.0% | 13.3% | 27.0% | 6.2% | 0.00 | 17.7% | 49.0% | 0.14 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 9.0% | 2.06 | 1.54 | 33.9% | 0.0% | 13.0% | 29.6% | 21.5% | 0.00 | 16.7% | 51.5% | 0.02 | 0.00 |
| Totale | 200 | 9.0% | 2.06 | 1.54 | 31.5% | 0.0% | 13.2% | 28.3% | 14.2% | 0.00 | 17.2% | 50.3% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

