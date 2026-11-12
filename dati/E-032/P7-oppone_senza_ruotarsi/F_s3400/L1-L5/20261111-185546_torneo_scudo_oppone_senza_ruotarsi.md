# Torneo v0.2 — /home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json

- Regole `v0.2`, configurazione `/home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json`; differenze da B0: {'pugno': 'sequenziale', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L')}
- IA: forte:30; partite: 200; tempo 2347s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.2% [28.0–30.4] | 30–45% | ❌ |
| Durata mediana (round) | 12.0 [11.0–13.0] (media 11.68) | 8–11 | ❌ |
| Partite al round 13+ | 45.0% [38.3–51.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=77) | 22.1% [14.3–32.5] | 20–35% | ✅ |
| Attacchi con opposizione | 39.7% [38.4–41.0] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 71.0% [69.6–72.3] (con ≥3: 31.3% [30.0–32.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.9% [35.6–38.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–0.9] (n=412) / 90.1% [86.2–93.0] (n=302) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 13.5% [12.0–15.0] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Risvegliato 68.8% [60.7–76.0] (n=138), LDR-05 Risvegliato 78.4% [70.6–84.5] (n=134) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 48.4% [41.2–55.6] (n=182) | | |
| Attacchi per partita | 27.4 | | |
| Pugno attaccante vuoto / pieno | 46.9% [45.5–48.2] / 12.8% [11.9–13.8] (gemme medie 0.91) | non >90% | |
| Pugno difensore vuoto / pieno | 56.6% [54.6–58.6] / 25.5% [23.8–27.3] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1478, 1: 1678, 2: 1625, 3: 442, 4: 169, 5: 75, 6: 11} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'crepuscolo': 19, 'colpo_finale': 181} | | |
| G1 vince fra le partite finite al Crepuscolo | 52.6% [31.7–72.7] | | |
| G1 vince fra le partite arrivate al round 15 | 54.2% [35.1–72.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 37.5% [21.2–57.3] / 44.4% [18.9–73.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 22.2% [6.3–54.7]; 12.5% [4.3–31.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-1': 5, '2-2': 4, '0-0': 3, '0-1': 3, '2-0': 2, '1-0': 2, '3-3': 1, '1-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=12) | 50.0% [31.4–68.6] / 50.0% [25.4–74.6] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 3, 15: 9}; 75.0% [46.8–91.1] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 91.7% [64.6–98.5] / 16.7% [4.7–44.8]; 1.42 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–24.3] / 91.7% [64.6–98.5] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=6) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–39.0] / 33.3% [9.7–70.0]; 0.0% [0.0–39.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.4–6.4] / 25.0% [12.0–44.9]; 100.0% [61.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 5, 'perd:pronto': 1, 'vinc:atk': 6} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=21) / turno di G2 (n=14) | 0.0% [0.0–15.5] / 0.0% [0.0–21.5] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=21) | 0.0% [0.0–15.5] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 62.5% [42.7–78.8] (33.3% [18.0–53.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 9, 'rif_LDR01_puntata_e_preda': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 54% (n=24) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 37.0% [30.6–43.9], rif_LDR05_scudi_armati 63.0% [56.1–69.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.366 / 0.087 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.086 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.07 (0.00), rif_LDR05_scudi_armati 0.18 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 28.3% [27.1–29.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.67 (141 / 192); 56.3% [55.0–57.6] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.7% [49.8–51.6]; rif_LDR01_puntata_e_preda 47.2%, rif_LDR05_scudi_armati 53.9% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 2.3% [1.7–3.0] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.306 (1060) / 0.304 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 74 vittorie), LDR-05 R: 18.0 (49%, 126 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 4.58, LDR-01 1.85, ROS-016 1.48, ROS-018 1.04, VER-011 0.76, BLU-015 0.73, VER-001 0.67, BLU-001 0.63, BLU-023 0.57, ROS-001 0.54, BLU-021 0.53, BLU-008 0.52 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.79, rif_LDR05_scudi_armati 0.08 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.02, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 6% (n=31), rif_LDR05_scudi_armati 33% (n=46) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.8% [11.9–13.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, BLU-008 63%, BLU-010 63%, ROS-020 63%, BLU-021 63%, collante 63%, NEU-013 63%, NEU-009 63%, ROS-016 37%, VER-008 37%, VER-011 37%, caccia 37%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 37.0 [31–44] (200) |
| rif_LDR05_scudi_armati | 63.0 [56–69] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.26 | 0.00 | 1.85 / 0.00 | 0.00 | 0.00 | 3.7 (198) | 13 | G 40%, R 60% | 2.15 | 0.43 |
| rif_LDR05_scudi_armati | 3.92 | 0.00 | 4.58 / 0.00 | 0.00 | 1.04 | 4.0 (199) | 13 | B 47%, R 53% | 1.74 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.85/1.95/0.90 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.36/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.58/0.23/0.18 | 0.74/0.18/0.49/0.51 | 0.86/0.59/0.24/0.18 | 0.00/0.34/0.00/0.00 | 0.70/0.00/0.19/0.15 | 0.67/0.28/0.24/0.24 | 0.66/1.48/0.02/0.56 | 0.82/1.30/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.35/0.21/0.24 | 0.24/0.09/0.09/0.20 | 0.00/0.00/0.00/0.00 | 0.68/0.67/0.02/0.49 | 0.65/0.00/0.00/0.00 | 0.66/0.00/0.12/0.07 | 0.60/0.76/0.24/0.23 | 0.69/0.46/0.36/0.40 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.04/0.04 | 0.46/0.07/0.13/0.05 | 0.36/0.12/0.14/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.04/0.04 | 0.37/0.44/0.03/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/4.58/1.62/0.86 | 0.70/0.63/0.24/0.11 | 0.65/0.00/0.20/0.11 | 0.60/0.52/0.27/0.21 | 0.56/0.36/0.28/0.33 | 0.56/0.00/0.20/0.18 | 0.63/0.73/0.20/0.39 | 0.00/0.53/0.00/0.00 | 0.00/0.57/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.51/0.34/0.34 | 0.76/0.49/0.20/0.12 | 0.00/0.00/0.00/0.00 | 0.66/0.43/0.20/0.11 | 0.00/0.30/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.23/0.27/0.20 | 0.00/0.00/0.00/0.00 | 0.43/0.78/0.00/0.00 | 0.60/0.48/0.33/0.46 | 0.46/0.39/0.27/0.29 | 0.27/0.12/0.17/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.00/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.04/0.10/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.03/0.01 | 0.34/0.03/0.04/0.02 | 0.29/0.15/0.17/0.14 | 0.23/0.36/0.10/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.13 | 0.16 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.16 | 0.02 | 0.00 | 0.01 | 0.17 | 0.09 | 0.00 | 0.00 | 0.18 | 0.07 | 0.00 | 0.03 | 0.00 | 0.01 | 0.04 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.21 | 0.00 | 0.06 | 0.00 | 0.01 | 0.03 | 0.05 | 0.02 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.01 | 0.00 | 0.03 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.25 | 0.29 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.94 | 0.00 | 0.04 | 0.10 | 0.11 | 0.13 | 0.10 | 0.10 | 0.10 | 0.08 | 0.09 | 0.06 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 1.19 | 0.03 | 0.07 | 0.07 | 0.15 | 0.19 | 0.20 | 0.14 | 0.10 | 0.10 | 0.08 | 0.04 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 2 | 1 | 0 | 3 |
| 7 | 2 | 3 | 0 | 5 |
| 8 | 8 | 7 | 0 | 15 |
| 9 | 16 | 6 | 0 | 22 |
| 10 | 10 | 13 | 0 | 23 |
| 11 | 16 | 9 | 0 | 25 |
| 12 | 9 | 8 | 0 | 17 |
| 13 | 16 | 16 | 0 | 32 |
| 14 | 14 | 20 | 0 | 34 |
| 15 | 12 | 9 | 0 | 21 |
| 16 | 1 | 2 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 47.2% | 0.065 | 0.00 | 0.79 | 0.00 | 0.00 | 4.76 | 0.00 | 0.00 | 0.351 |
| rif_LDR05_scudi_armati | 200 | 53.9% | 0.109 | 0.08 | 0.00 | 0.00 | 0.00 | 4.53 | 0.00 | 0.00 | 0.382 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 445 | 0.888 | 0.845 | 0.811 | 0.360 | 2256 | 0.812 | 0.235 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 445 | 0.187 | 0.164 | 0.135 | 0.034 | 2256 | 0.188 | 0.066 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 609 | 0.895 | 0.874 | 0.862 | 0.437 | 2168 | 0.810 | 0.220 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 609 | 0.222 | 0.213 | 0.190 | 0.059 | 2168 | 0.174 | 0.058 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 9.5% | 2.13 | 2.15 | 18.4% | 0.0% | 15.3% | 27.6% | 6.5% | 0.00 | 18.0% | 47.2% | 0.14 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 9.5% | 2.13 | 2.15 | 47.7% | 0.0% | 14.3% | 30.3% | 18.1% | 0.00 | 15.9% | 53.9% | 0.07 | 0.00 |
| Totale | 400 | 9.5% | 2.13 | 2.15 | 31.9% | 0.0% | 14.8% | 29.0% | 12.4% | 0.00 | 16.9% | 50.7% | 0.11 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.409 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.79 |
| rif_LDR05_scudi_armati | 200 | 0.385 | 0.202 | 4.7% | 8.9% | 2.10 | 0.41 | 0.38 | 0.00 | 0.00 | 0.00 | 5.32 |

