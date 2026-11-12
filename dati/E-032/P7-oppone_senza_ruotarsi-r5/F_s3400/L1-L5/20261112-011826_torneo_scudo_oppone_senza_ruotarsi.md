# Torneo v0.2 — /home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json

- Regole `v0.2`, configurazione `/home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json`; differenze da B0: {'pugno': 'sequenziale', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L')}
- IA: forte:30; partite: 200; tempo 1929s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.2% [28.0–30.4] | 30–45% | ❌ |
| Durata mediana (round) | 11.0 [11.0–12.0] (media 11.31) | 8–11 | ✅ |
| Partite al round 13+ | 37.0% [30.6–43.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.3–3.6] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=76) | 30.3% [21.1–41.3] | 20–35% | ✅ |
| Attacchi con opposizione | 40.7% [39.4–42.0] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 70.1% [68.8–71.5] (con ≥3: 32.1% [30.8–33.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.5% [36.2–38.8] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–0.9] (n=407) / 89.6% [85.6–92.6] (n=289) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 13.3% [11.8–14.9] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Risvegliato 66.4% [57.6–74.2] (n=122), LDR-05 Risvegliato 81.8% [74.4–87.3] (n=137) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 39.0% [32.2–46.3] (n=182) | | |
| Attacchi per partita | 26.0 | | |
| Pugno attaccante vuoto / pieno | 47.9% [46.4–49.3] / 12.9% [11.9–13.8] (gemme medie 0.90) | non >90% | |
| Pugno difensore vuoto / pieno | 54.0% [51.9–56.0] / 26.8% [25.0–28.7] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1366, 1: 1705, 2: 1466, 3: 434, 4: 163, 5: 55, 6: 9} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 179, 'crepuscolo': 21} | | |
| G1 vince fra le partite finite al Crepuscolo | 57.1% [36.5–75.5] | | |
| G1 vince fra le partite arrivate al round 15 | 54.2% [35.1–72.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 54.2% [35.1–72.1] / 38.5% [17.7–64.5] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 61.5% [35.5–82.3]; 8.3% [2.3–25.8] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 8, '0-0': 3, '2-2': 3, '2-1': 3, '1-1': 2, '0-2': 1, '2-3': 1, '3-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=15) | 62.5% [42.7–78.8] / 46.7% [24.8–69.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 13, 16: 2}; 46.7% [24.8–69.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 66.7% [41.7–84.8] / 46.7% [24.8–69.9]; 2.33 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–20.4] / 80.0% [54.8–93.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=7) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–35.4] / 87.5% [52.9–97.8]; 0.0% [0.0–35.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.5% [1.7–7.0] / 29.2% [14.9–49.2]; 100.0% [64.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 3, 'vinc:atk': 7} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=12) / turno di G2 (n=14) | 0.0% [0.0–24.3] / 0.0% [0.0–21.5] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=12) | 0.0% [0.0–24.3] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 62.5% [42.7–78.8] (16.7% [6.7–35.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 9, 'rif_LDR05_scudi_armati': 6} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 54% (n=24) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 41.0% [34.4–47.9], rif_LDR05_scudi_armati 59.0% [52.1–65.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.366 / 0.083 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.081 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.07 (0.00), rif_LDR05_scudi_armati 0.13 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 30.2% [29.0–31.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.46 (132 / 159); 55.9% [54.5–57.2] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.3% [50.4–52.3]; rif_LDR01_puntata_e_preda 49.6%, rif_LDR05_scudi_armati 52.9% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 2.0% [1.5–2.7] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.313 (1106) / 0.305 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 82 vittorie), LDR-05 R: 18.0 (50%, 118 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 4.88, LDR-01 1.66, ROS-016 1.26, ROS-018 0.74, BLU-015 0.72, VER-011 0.65, ROS-005 0.56, VER-001 0.53, NEU-001 0.50, ROS-020 0.49, BLU-023 0.48, BLU-001 0.48 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.60, rif_LDR05_scudi_armati 0.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 9% (n=32), rif_LDR05_scudi_armati 45% (n=44) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.9% [11.9–13.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR05_scudi_armati 0.52; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, ROS-020 59%, BLU-008 59%, BLU-010 59%, NEU-001 59%, NEU-013 59%, collante 59%, BLU-021 59%, VER-008 41%, ROS-016 41%, VER-011 41%, caccia 41%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 41.0 [34–48] (200) |
| rif_LDR05_scudi_armati | 59.0 [52–66] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.98 | 0.00 | 1.66 / 0.00 | 0.00 | 0.00 | 3.7 (200) | 13 | G 40%, R 60% | 2.25 | 0.49 |
| rif_LDR05_scudi_armati | 3.80 | 0.00 | 4.88 / 0.00 | 0.00 | 0.85 | 3.8 (200) | 13 | B 44%, R 56% | 1.72 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.66/1.72/0.91 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.35/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.46/0.20/0.14 | 0.65/0.15/0.38/0.53 | 0.83/0.64/0.28/0.17 | 0.00/0.32/0.00/0.00 | 0.67/0.00/0.20/0.08 | 0.57/0.24/0.20/0.17 | 0.60/1.26/0.04/0.45 | 0.78/0.95/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.41/0.19/0.28 | 0.24/0.07/0.09/0.16 | 0.00/0.00/0.00/0.00 | 0.69/0.53/0.03/0.41 | 0.62/0.00/0.00/0.00 | 0.60/0.00/0.07/0.06 | 0.60/0.65/0.21/0.17 | 0.65/0.43/0.31/0.36 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.61/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.05/0.04 | 0.42/0.05/0.05/0.04 | 0.34/0.12/0.21/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.05/0.04 | 0.35/0.47/0.04/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/4.88/1.76/0.84 | 0.63/0.48/0.21/0.05 | 0.56/0.00/0.14/0.15 | 0.57/0.36/0.18/0.17 | 0.54/0.29/0.20/0.24 | 0.51/0.00/0.16/0.17 | 0.62/0.72/0.24/0.28 | 0.00/0.45/0.00/0.00 | 0.00/0.48/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.36/0.28/0.28 | 0.73/0.47/0.20/0.13 | 0.61/0.13/0.46/0.41 | 0.78/0.49/0.20/0.10 | 0.00/0.28/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.23/0.36/0.29 | 0.00/0.00/0.00/0.00 | 0.29/0.54/0.00/0.00 | 0.55/0.49/0.33/0.42 | 0.38/0.38/0.23/0.33 | 0.28/0.12/0.17/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.22/0.08/0.07/0.12 | 0.73/0.50/0.12/0.06 | 0.52/0.00/0.15/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.08 | 0.15 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.12 | 0.03 | 0.00 | 0.01 | 0.12 | 0.09 | 0.00 | 0.00 | 0.26 | 0.07 | 0.00 | 0.03 | 0.00 | 0.01 | 0.03 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.21 | 0.00 | 0.07 | 0.00 | 0.01 | 0.01 | 0.02 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.01 | 0.12 | 0.01 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.23 | 0.27 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.98 | 0.00 | 0.03 | 0.06 | 0.07 | 0.17 | 0.17 | 0.09 | 0.09 | 0.12 | 0.10 | 0.06 | 0.04 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 1.16 | 0.00 | 0.04 | 0.06 | 0.10 | 0.13 | 0.21 | 0.22 | 0.12 | 0.10 | 0.07 | 0.05 | 0.04 | 0.01 | 0.01 | 0.52 | 0.20 | 0.12 | 0.09 | 0.06 | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 1 | 0 | 0 | 1 |
| 7 | 4 | 7 | 0 | 11 |
| 8 | 14 | 5 | 0 | 19 |
| 9 | 11 | 13 | 0 | 24 |
| 10 | 12 | 16 | 0 | 28 |
| 11 | 12 | 6 | 0 | 18 |
| 12 | 13 | 11 | 0 | 24 |
| 13 | 7 | 15 | 0 | 22 |
| 14 | 9 | 19 | 0 | 28 |
| 15 | 13 | 9 | 0 | 22 |
| 16 | 0 | 2 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 49.6% | 0.061 | 0.00 | 0.60 | 0.00 | 0.00 | 4.28 | 0.00 | 0.00 | 0.356 |
| rif_LDR05_scudi_armati | 200 | 52.9% | 0.107 | 0.12 | 0.00 | 0.00 | 0.00 | 4.38 | 0.00 | 0.00 | 0.376 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 462 | 0.885 | 0.840 | 0.786 | 0.323 | 2219 | 0.822 | 0.222 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 462 | 0.271 | 0.247 | 0.208 | 0.032 | 2219 | 0.210 | 0.069 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 563 | 0.869 | 0.849 | 0.840 | 0.433 | 1954 | 0.821 | 0.213 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 563 | 0.227 | 0.215 | 0.211 | 0.046 | 1954 | 0.175 | 0.052 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 10.5% | 2.21 | 2.24 | 23.4% | 0.5% | 15.7% | 28.3% | 5.6% | 0.00 | 18.2% | 49.6% | 0.10 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 10.5% | 2.21 | 2.24 | 45.2% | 0.5% | 14.3% | 31.8% | 19.2% | 0.00 | 15.7% | 52.9% | 0.09 | 0.00 |
| Totale | 400 | 10.5% | 2.21 | 2.24 | 33.6% | 0.5% | 15.0% | 30.0% | 12.6% | 0.00 | 16.9% | 51.3% | 0.09 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.407 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.30 |
| rif_LDR05_scudi_armati | 200 | 0.408 | 0.200 | 4.2% | 8.5% | 1.92 | 0.32 | 0.43 | 0.00 | 0.00 | 0.00 | 5.45 |

