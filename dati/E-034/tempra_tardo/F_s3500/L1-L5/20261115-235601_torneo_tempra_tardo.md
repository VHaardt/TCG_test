# Torneo v0.2 — /home/claude/e034_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e034_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2299s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.9% [28.7–31.1] | 30–45% | ❌ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 11.00) | 8–11 | ✅ |
| Partite al round 13+ | 28.0% [22.2–34.6] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–1.9] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=73) | 30.1% [20.8–41.4] | 20–35% | ✅ |
| Attacchi con opposizione | 37.8% [36.6–39.2] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 68.0% [66.6–69.4] (con ≥3: 29.2% [27.9–30.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.7% [38.4–41.0] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 5.4% [3.6–7.9] (n=429) / 92.7% [89.1–95.2] (n=288) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.5% [11.2–14.0] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 50.0% [23.7–76.3] (n=10), LDR-01 Risvegliato 66.1% [57.5–73.8] (n=127), LDR-05 Base 61.5% [35.5–82.3] (n=13), LDR-05 Risvegliato 74.3% [66.5–80.8] (n=140) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 28.3% [22.4–35.2] (n=187) | | |
| Attacchi per partita | 26.8 | | |
| Pugno attaccante vuoto / pieno | 48.8% [47.4–50.2] / 13.0% [12.1–14.0] (gemme medie 0.83) | non >90% | |
| Pugno difensore vuoto / pieno | 59.4% [57.4–61.4] / 23.9% [22.2–25.6] (gemme medie 0.23) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1614, 1: 1666, 2: 1486, 3: 404, 4: 143, 5: 49, 6: 4} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 187, 'crepuscolo': 13} | | |
| G1 vince fra le partite finite al Crepuscolo | 38.5% [17.7–64.5] | | |
| G1 vince fra le partite arrivate al round 15 | 36.8% [19.1–59.0] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 42.1% [23.1–63.7] / 37.5% [13.7–69.4] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 25.0% [7.1–59.1]; 0.0% [0.0–16.8] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-1': 3, '0-0': 3, '2-3': 3, '1-0': 2, '2-2': 2, '2-1': 2, '1-2': 1, '3-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=8) | 42.1% [23.1–63.7] / 37.5% [13.7–69.4] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 8}; 75.0% [40.9–92.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 12.5% [2.2–47.1] / 12.5% [2.2–47.1]; 2.12 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–32.4] / 62.5% [30.6–86.3] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 20.0% [3.6–62.4]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.5% [0.5–4.3] / 15.8% [5.5–37.6]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 2, 'vinc:atk': 2, 'vinc:rim': 1} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=10) / turno di G2 (n=10) | 0.0% [0.0–27.8] / 0.0% [0.0–27.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=10) | 0.0% [0.0–27.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 15.8% [5.5–37.6] (0.0% [0.0–16.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 4, 'rif_LDR05_scudi_armati': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 37% (n=19) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 36.0% [29.7–42.9], rif_LDR05_scudi_armati 64.0% [57.1–70.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.352 / 0.082 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.079 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.08 (0.00), rif_LDR05_scudi_armati 0.15 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 31.2% [30.0–32.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.57 (124 / 191); 58.5% [57.1–59.8] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 47.9% [46.9–48.8]; rif_LDR01_puntata_e_preda 45.5%, rif_LDR05_scudi_armati 50.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.322 (972) / 0.320 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 72 vittorie), LDR-05 R: 18.0 (49%, 128 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.96, LDR-01 1.77, ROS-016 1.38, BLU-015 0.93, ROS-018 0.67, VER-011 0.67, VER-001 0.66, BLU-001 0.63, ROS-020 0.58, ROS-005 0.51, BLU-023 0.48, BLU-021 0.47 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.65, rif_LDR05_scudi_armati 0.15 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.02, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 12% (n=26), rif_LDR05_scudi_armati 40% (n=47) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.0% [12.1–14.0] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, ROS-020 64%, BLU-010 64%, BLU-008 64%, NEU-013 64%, collante 64%, NEU-009 64%, BLU-021 64%, ROS-016 36%, caccia 36%, VER-001 36%, VER-011 36%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 36.0 [30–43] (200) |
| rif_LDR05_scudi_armati | 64.0 [57–70] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.14 | 0.00 | 1.77 / 0.00 | 0.00 | 0.00 | 3.6 (200) | 13 | G 41%, R 59% | 2.03 | 0.64 |
| rif_LDR05_scudi_armati | 3.75 | 0.00 | 3.96 / 0.00 | 0.00 | 0.79 | 4.1 (199) | 13 | B 48%, R 52% | 1.74 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.77/1.83/0.94 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.37/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.47/0.23/0.10 | 0.74/0.20/0.58/0.39 | 0.84/0.59/0.23/0.20 | 0.00/0.28/0.00/0.00 | 0.64/0.00/0.28/0.14 | 0.63/0.21/0.36/0.16 | 0.67/1.38/0.06/0.47 | 0.65/0.89/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.51/0.34/0.18/0.21 | 0.23/0.07/0.12/0.14 | 0.00/0.00/0.00/0.00 | 0.67/0.66/0.06/0.45 | 0.71/0.00/0.00/0.00 | 0.55/0.00/0.12/0.07 | 0.68/0.67/0.24/0.16 | 0.65/0.46/0.37/0.34 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.07/0.01 | 0.38/0.04/0.06/0.04 | 0.30/0.12/0.16/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.07/0.02 | 0.30/0.39/0.01/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.96/1.75/0.82 | 0.68/0.63/0.24/0.11 | 0.59/0.00/0.14/0.10 | 0.55/0.40/0.20/0.17 | 0.59/0.35/0.33/0.30 | 0.52/0.00/0.23/0.14 | 0.64/0.93/0.40/0.39 | 0.00/0.47/0.00/0.00 | 0.00/0.48/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.36/0.40/0.23 | 0.66/0.45/0.20/0.15 | 0.00/0.00/0.00/0.00 | 0.65/0.42/0.18/0.10 | 0.00/0.26/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.28/0.35/0.29 | 0.00/0.00/0.00/0.00 | 0.32/0.46/0.00/0.00 | 0.66/0.58/0.40/0.51 | 0.36/0.22/0.18/0.23 | 0.15/0.07/0.15/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.00/0.07/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.04/0.07/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.00/0.01/0.00 | 0.33/0.04/0.04/0.03 | 0.22/0.07/0.16/0.07 | 0.30/0.36/0.14/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.95 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.17 | 0.01 | 0.00 | 0.01 | 0.12 | 0.07 | 0.00 | 0.00 | 0.17 | 0.08 | 0.00 | 0.02 | 0.00 | 0.01 | 0.01 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.03 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.25 | 0.00 | 0.08 | 0.01 | 0.01 | 0.01 | 0.04 | 0.03 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.22 | 0.00 | 0.00 | 0.35 | 0.15 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.77 | 0.01 | 0.05 | 0.09 | 0.10 | 0.12 | 0.12 | 0.11 | 0.10 | 0.03 | 0.01 | 0.01 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 1.17 | 0.04 | 0.10 | 0.07 | 0.19 | 0.20 | 0.17 | 0.18 | 0.10 | 0.06 | 0.01 | 0.03 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 0 | 2 | 0 | 2 |
| 7 | 2 | 3 | 0 | 5 |
| 8 | 8 | 10 | 0 | 18 |
| 9 | 22 | 10 | 0 | 32 |
| 10 | 18 | 13 | 0 | 31 |
| 11 | 22 | 17 | 0 | 39 |
| 12 | 6 | 10 | 0 | 16 |
| 13 | 7 | 11 | 0 | 18 |
| 14 | 6 | 13 | 0 | 19 |
| 15 | 7 | 12 | 0 | 19 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 45.5% | 0.063 | 0.00 | 0.65 | 0.00 | 0.00 | 4.11 | 0.00 | 0.00 | 0.321 |
| rif_LDR05_scudi_armati | 200 | 50.1% | 0.099 | 0.15 | 0.00 | 0.00 | 0.00 | 4.05 | 0.00 | 0.00 | 0.381 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 377 | 0.905 | 0.854 | 0.812 | 0.390 | 2213 | 0.790 | 0.207 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 377 | 0.220 | 0.196 | 0.146 | 0.042 | 2213 | 0.202 | 0.070 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 571 | 0.884 | 0.863 | 0.851 | 0.429 | 2205 | 0.774 | 0.228 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 571 | 0.222 | 0.215 | 0.203 | 0.053 | 2205 | 0.164 | 0.059 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 6.5% | 2.06 | 1.76 | 19.4% | 0.5% | 15.3% | 27.2% | 5.1% | 0.00 | 17.4% | 45.5% | 0.17 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 6.5% | 2.06 | 1.76 | 49.6% | 0.5% | 16.0% | 31.8% | 18.6% | 0.00 | 17.8% | 50.1% | 0.09 | 0.00 |
| Totale | 400 | 6.5% | 2.06 | 1.76 | 33.1% | 0.5% | 15.7% | 29.5% | 12.1% | 0.00 | 17.6% | 47.9% | 0.13 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.381 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.01 |
| rif_LDR05_scudi_armati | 200 | 0.376 | 0.196 | 0.0% | 0.0% | 1.76 | 0.34 | 0.40 | 0.00 | 0.00 | 0.00 | 5.63 |

