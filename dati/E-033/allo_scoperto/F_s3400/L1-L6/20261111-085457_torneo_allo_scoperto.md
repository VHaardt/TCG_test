# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 653s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.7% [27.8–31.6] | 30–45% | ❌ |
| Durata mediana (round) | 10.0 [9.0–11.0] (media 10.08) | 8–11 | ✅ |
| Partite al round 13+ | 22.0% [15.0–31.1] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=47) | 23.4% [13.6–37.2] | 20–35% | ✅ |
| Attacchi con opposizione | 24.1% [22.4–25.9] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 55.3% [53.1–57.5] (con ≥3: 16.2% [14.6–17.9]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 40.1% [38.1–42.1] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 10.5% [7.4–14.9] (n=256) / 89.2% [83.5–93.0] (n=166) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.9% [13.7–18.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 61.5% [42.5–77.6] (n=26), LDR-01 Risvegliato 60.4% [46.3–73.0] (n=48), LDR-06 Base 100.0% [20.7–100.0] (n=1), LDR-06 Risvegliato 72.0% [62.5–79.9] (n=100) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 28.9% [20.0–40.0] (n=76) | | |
| Attacchi per partita | 23.1 | | |
| Pugno attaccante vuoto / pieno | 52.5% [50.3–54.7] / 13.1% [11.7–14.6] (gemme medie 0.77) | non >90% | |
| Pugno difensore vuoto / pieno | 59.9% [56.8–62.8] / 25.4% [22.9–28.2] (gemme medie 0.23) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 797, 1: 764, 2: 523, 3: 162, 4: 46, 5: 18, 6: 3} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 93, 'crepuscolo': 7} | | |
| G1 vince fra le partite finite al Crepuscolo | 28.6% [8.2–64.1] | | |
| G1 vince fra le partite arrivate al round 15 | 33.3% [12.1–64.6] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 77.8% [45.3–93.7] / 42.9% [15.8–75.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 28.6% [8.2–64.1]; 0.0% [0.0–29.9] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-1': 2, '1-0': 2, '0-0': 2, '2-2': 1, '1-1': 1, '2-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=7) | 77.8% [45.3–93.7] / 42.9% [15.8–75.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 7}; 71.4% [35.9–91.8] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 28.6% [8.2–64.1] / 14.3% [2.6–51.3]; 1.14 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–35.4] / 71.4% [35.9–91.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 25.0% [4.6–69.9]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.0–8.5] / 33.3% [12.1–64.6]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:pronto': 3, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=1) / turno di G2 (n=0) | 0.0% [0.0–79.3] / nan% [nan–nan] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=1) | 0.0% [0.0–79.3] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 22.2% [6.3–54.7] (0.0% [0.0–29.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 5, 'rif_LDR01_puntata_e_preda': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR06_ferite_e_caccia 33% (n=9) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 72.0% [62.5–79.9], rif_LDR06_ferite_e_caccia 28.0% [20.1–37.5]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.353 / 0.069 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.069 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.08 (0.00), rif_LDR06_ferite_e_caccia 0.16 (0.05) | |
| M4 | Scontri decisi prima dell'impegno | 35.8% [33.9–37.8] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 4.77 (132 / 345); 61.0% [59.0–62.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 44.6% [43.0–46.2]; rif_LDR01_puntata_e_preda 48.1%, rif_LDR06_ferite_e_caccia 41.2% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.7] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.374 (179) / 0.337 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 72 vittorie), LDR-06 G: 17.0 (49%, 28 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 2.85, VER-020 2.37, LDR-01 1.70, ROS-018 0.88, ROS-016 0.83, VER-008 0.82, NER-017 0.71, NEU-001 0.62, VER-001 0.60, VER-011 0.59, NER-009 0.53, NER-013 0.51 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.78, rif_LDR06_ferite_e_caccia 3.04 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.03, rif_LDR06_ferite_e_caccia 0.25 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 30% (n=10), rif_LDR06_ferite_e_caccia 22% (n=37) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.1% [11.7–14.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR06_ferite_e_caccia 0.88; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-001 100%, ponte 100%, caccia 100%, VER-008 100%, ROS-016 72%, VER-011 72%, VER-020 28%, NEU-001 28%, NER-015 28%, NER-009 28%, NER-017 28%, collante 28%; oltre il 60%: ROS-016, VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 72.0 [63–80] (100) |
| rif_LDR06_ferite_e_caccia | 28.0 [20–37] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.98 | 0.00 | 1.70 / 0.00 | 0.00 | 0.00 | 4.1 (100) | 13 | G 40%, R 60% | 2.48 | 0.42 |
| rif_LDR06_ferite_e_caccia | 3.79 | 0.00 | 2.85 / 0.06 | 0.00 | 0.18 | 4.4 (99) | 9 | G 59%, K 41% | 2.17 | 1.45 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.70/2.24/0.46 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.38/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.82/0.49/0.18/0.15 | 0.78/0.06/0.59/0.25 | 0.66/0.31/0.15/0.01 | 0.00/0.25/0.00/0.00 | 0.73/0.00/0.17/0.09 | 0.63/0.14/0.33/0.10 | 0.57/0.83/0.04/0.34 | 0.67/0.88/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.42/0.27/0.21 | 0.21/0.02/0.13/0.11 | 0.00/0.00/0.00/0.00 | 0.70/0.49/0.04/0.41 | 0.61/0.00/0.00/0.00 | 0.65/0.00/0.10/0.00 | 0.59/0.59/0.18/0.15 | 0.63/0.32/0.41/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.24/0.00/0.04/0.00 | 0.37/0.05/0.02/0.04 | 0.34/0.04/0.15/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.06/0.01 | 0.38/0.55/0.02/0.25 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.16/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.72/0.09/0.58 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.27/0.48/0.15 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.85/1.98/0.61 | 0.00/0.00/0.00/0.00 | 0.44/0.00/0.00/0.00 | 0.15/0.24/0.03/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.40/0.18/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.27/0.09/0.24/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.29/0.03/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.35/0.04/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/1.10/0.04/0.54 | 0.36/0.03/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.62/0.17/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.97 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.12 | 0.02 | 0.00 | 0.00 | 0.09 | 0.08 | 0.00 | 0.00 | 0.29 | 0.03 | 0.00 | 0.01 | 0.00 | 0.00 | 0.04 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.44 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.65 | 0.00 | 0.04 | 0.05 | 0.07 | 0.04 | 0.08 | 0.14 | 0.07 | 0.06 | 0.02 | 0.03 | 0.03 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.95 | 0.00 | 0.02 | 0.03 | 0.11 | 0.12 | 0.20 | 0.11 | 0.13 | 0.10 | 0.05 | 0.05 | 0.01 | 0.02 | 0.88 | 0.06 | 0.18 | 0.18 | 0.12 | 0.14 | 0.08 | 0.03 | 0.03 | 0.02 | 0.02 | 0.01 | 0.01 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 4 | 0 | 4 |
| 6 | 3 | 0 | 0 | 3 |
| 7 | 2 | 6 | 0 | 8 |
| 8 | 10 | 11 | 0 | 21 |
| 9 | 8 | 3 | 0 | 11 |
| 10 | 5 | 4 | 0 | 9 |
| 11 | 8 | 7 | 0 | 15 |
| 12 | 3 | 4 | 0 | 7 |
| 13 | 6 | 3 | 0 | 9 |
| 14 | 2 | 2 | 0 | 4 |
| 15 | 3 | 6 | 0 | 9 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 48.1% | 0.067 | 0.00 | 0.78 | 0.00 | 0.00 | 2.73 | 0.00 | 0.00 | 0.287 |
| rif_LDR06_ferite_e_caccia | 100 | 41.2% | 0.071 | 0.83 | 2.21 | 0.00 | 0.00 | 4.26 | 0.00 | 0.00 | 0.423 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 218 | 0.817 | 0.780 | 0.748 | 0.326 | 964 | 0.718 | 0.150 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 218 | 0.188 | 0.165 | 0.161 | 0.037 | 964 | 0.132 | 0.034 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 189 | 0.931 | 0.910 | 0.905 | 0.339 | 942 | 0.823 | 0.306 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 189 | 0.254 | 0.222 | 0.196 | 0.085 | 942 | 0.195 | 0.081 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 7.0% | 1.83 | 1.72 | 45.2% | 4.0% | 18.7% | 23.5% | 4.3% | 0.00 | 15.0% | 48.1% | 0.09 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 7.0% | 1.83 | 1.72 | 15.7% | 4.0% | 21.7% | 26.4% | 8.2% | 0.00 | 13.7% | 41.2% | 0.05 | 0.00 |
| Totale | 200 | 7.0% | 1.83 | 1.72 | 25.6% | 4.0% | 20.2% | 24.9% | 6.6% | 0.00 | 14.4% | 44.6% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

