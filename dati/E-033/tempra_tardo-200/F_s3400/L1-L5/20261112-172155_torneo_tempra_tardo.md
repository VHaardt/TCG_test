# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1117s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.8% [28.6–31.1] | 30–45% | ❌ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 10.92) | 8–11 | ✅ |
| Partite al round 13+ | 28.5% [22.7–35.1] | ≤12% | ❌ |
| Partite oltre il 15 | 2.0% [0.8–5.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=68) | 25.0% [16.2–36.4] | 20–35% | ✅ |
| Attacchi con opposizione | 37.2% [35.9–38.5] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 68.4% [67.0–69.8] (con ≥3: 29.7% [28.3–31.1]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.6% [38.3–40.9] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.9% [4.8–9.7] (n=423) / 90.3% [86.4–93.2] (n=290) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.4% [11.1–13.9] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 60.0% [31.3–83.2] (n=10), LDR-01 Risvegliato 61.2% [52.9–68.8] (n=139), LDR-05 Base 63.2% [41.0–80.9] (n=19), LDR-05 Risvegliato 73.2% [64.7–80.2] (n=123) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 30.6% [24.5–37.6] (n=186) | | |
| Attacchi per partita | 26.6 | | |
| Pugno attaccante vuoto / pieno | 48.4% [47.0–49.8] / 13.2% [12.3–14.2] (gemme medie 0.84) | non >90% | |
| Pugno difensore vuoto / pieno | 58.6% [56.6–60.6] / 24.8% [23.1–26.6] (gemme medie 0.24) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1586, 1: 1641, 2: 1464, 3: 415, 4: 133, 5: 68, 6: 11} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 185, 'crepuscolo': 15} | | |
| G1 vince fra le partite finite al Crepuscolo | 60.0% [35.7–80.2] | | |
| G1 vince fra le partite arrivate al round 15 | 60.0% [38.7–78.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 40.0% [21.9–61.3] / 62.5% [30.6–86.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 25.0% [7.1–59.1]; 20.0% [8.1–41.6] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 3, '3-2': 3, '0-0': 3, '2-1': 2, '1-1': 2, '2-3': 2, '1-0': 2, '2-0': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=11) | 55.0% [34.2–74.2] / 45.5% [21.3–72.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 8, 16: 3}; 54.5% [28.0–78.7] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 45.5% [21.3–72.0] / 27.3% [9.7–56.6]; 1.64 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–25.9] / 72.7% [43.4–90.3] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 50.0% [18.8–81.2]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.5% [1.1–5.7] / 25.0% [11.2–46.9]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 3, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=9) / turno di G2 (n=8) | 0.0% [0.0–29.9] / 0.0% [0.0–32.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=9) | 0.0% [0.0–29.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 35.0% [18.1–56.7] (5.0% [0.9–23.6]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 7, 'rif_LDR01_puntata_e_preda': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 60% (n=20) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 39.5% [33.0–46.4], rif_LDR05_scudi_armati 60.5% [53.6–67.0]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.364 / 0.084 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.082 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.08 (0.00), rif_LDR05_scudi_armati 0.20 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 30.0% [28.8–31.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.69 (104 / 233); 58.7% [57.3–60.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 48.7% [47.7–49.6]; rif_LDR01_puntata_e_preda 47.0%, rif_LDR05_scudi_armati 50.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.319 (963) / 0.320 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 79 vittorie), LDR-05 R: 18.0 (49%, 121 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.98, LDR-01 1.83, ROS-016 1.62, ROS-018 0.81, VER-011 0.80, BLU-015 0.75, VER-001 0.64, BLU-001 0.59, BLU-023 0.49, BLU-008 0.48, BLU-021 0.47, VER-008 0.43 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.70, rif_LDR05_scudi_armati 0.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.05, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 12% (n=32), rif_LDR05_scudi_armati 36% (n=36) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.2% [12.3–14.2] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, BLU-008 60%, BLU-010 60%, NEU-009 60%, collante 60%, NEU-013 60%, BLU-021 60%, ROS-020 60%, ROS-016 40%, VER-011 40%, VER-008 40%, VER-001 40%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 39.5 [33–46] (200) |
| rif_LDR05_scudi_armati | 60.5 [54–67] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.21 | 0.00 | 1.83 / 0.00 | 0.00 | 0.00 | 4.0 (200) | 13 | G 39%, R 61% | 1.97 | 0.48 |
| rif_LDR05_scudi_armati | 3.91 | 0.00 | 3.98 / 0.00 | 0.00 | 0.94 | 4.0 (200) | 13 | B 48%, R 52% | 1.77 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.83/1.77/0.86 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.38/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.52/0.27/0.12 | 0.67/0.15/0.57/0.38 | 0.85/0.53/0.27/0.13 | 0.00/0.28/0.00/0.00 | 0.68/0.00/0.22/0.10 | 0.67/0.26/0.24/0.23 | 0.62/1.62/0.05/0.58 | 0.76/1.02/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.35/0.26/0.22 | 0.23/0.07/0.12/0.10 | 0.00/0.00/0.00/0.00 | 0.64/0.64/0.03/0.40 | 0.67/0.00/0.00/0.00 | 0.67/0.00/0.14/0.15 | 0.60/0.80/0.22/0.18 | 0.60/0.34/0.39/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.08/0.03 | 0.43/0.07/0.10/0.05 | 0.34/0.10/0.17/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.05/0.04 | 0.34/0.43/0.03/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.98/1.79/0.74 | 0.68/0.59/0.23/0.17 | 0.57/0.00/0.23/0.15 | 0.56/0.48/0.28/0.17 | 0.58/0.32/0.40/0.27 | 0.49/0.00/0.25/0.23 | 0.60/0.75/0.26/0.32 | 0.00/0.47/0.00/0.00 | 0.00/0.49/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.41/0.30/0.27 | 0.69/0.33/0.12/0.10 | 0.00/0.00/0.00/0.00 | 0.62/0.30/0.11/0.10 | 0.00/0.30/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.29/0.32/0.30 | 0.00/0.00/0.00/0.00 | 0.40/0.60/0.00/0.00 | 0.57/0.38/0.34/0.36 | 0.41/0.28/0.28/0.23 | 0.25/0.05/0.15/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.00/0.07/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.06/0.12/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.00/0.03/0.01 | 0.34/0.04/0.02/0.03 | 0.27/0.17/0.15/0.15 | 0.20/0.31/0.10/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.97 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.14 | 0.01 | 0.00 | 0.01 | 0.17 | 0.07 | 0.00 | 0.00 | 0.19 | 0.07 | 0.00 | 0.04 | 0.00 | 0.01 | 0.04 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.03 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.00 | 0.00 | 0.10 | 0.01 | 0.01 | 0.01 | 0.05 | 0.03 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.25 | 0.00 | 0.00 | 0.16 | 0.18 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.76 | 0.01 | 0.02 | 0.04 | 0.10 | 0.12 | 0.15 | 0.13 | 0.10 | 0.04 | 0.01 | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.79 | 0.03 | 0.07 | 0.09 | 0.10 | 0.12 | 0.12 | 0.10 | 0.06 | 0.04 | 0.04 | 0.01 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 2 | 0 | 3 |
| 7 | 4 | 8 | 0 | 12 |
| 8 | 8 | 11 | 0 | 19 |
| 9 | 23 | 8 | 0 | 31 |
| 10 | 15 | 15 | 0 | 30 |
| 11 | 16 | 15 | 0 | 31 |
| 12 | 12 | 5 | 0 | 17 |
| 13 | 13 | 3 | 0 | 16 |
| 14 | 5 | 16 | 0 | 21 |
| 15 | 8 | 8 | 0 | 16 |
| 16 | 4 | 0 | 0 | 4 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 47.0% | 0.063 | 0.00 | 0.70 | 0.00 | 0.00 | 4.08 | 0.00 | 0.00 | 0.349 |
| rif_LDR05_scudi_armati | 200 | 50.3% | 0.104 | 0.12 | 0.00 | 0.00 | 0.00 | 4.04 | 0.00 | 0.00 | 0.379 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 400 | 0.902 | 0.855 | 0.810 | 0.370 | 2219 | 0.820 | 0.234 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 400 | 0.245 | 0.215 | 0.188 | 0.040 | 2219 | 0.183 | 0.059 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 569 | 0.856 | 0.842 | 0.830 | 0.427 | 2130 | 0.779 | 0.231 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 569 | 0.200 | 0.181 | 0.165 | 0.069 | 2130 | 0.160 | 0.062 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 7.5% | 2.04 | 1.52 | 23.3% | 0.0% | 15.2% | 26.4% | 4.6% | 0.00 | 17.9% | 47.0% | 0.12 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 7.5% | 2.04 | 1.52 | 39.1% | 0.0% | 15.3% | 29.5% | 20.7% | 0.00 | 17.2% | 50.3% | 0.05 | 0.00 |
| Totale | 400 | 7.5% | 2.04 | 1.52 | 30.3% | 0.0% | 15.2% | 28.0% | 12.9% | 0.00 | 17.6% | 48.7% | 0.09 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

