# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 727s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 41.0% [39.1–42.9] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.0–13.0] (media 12.11) | 8–11 | ❌ |
| Partite al round 13+ | 43.0% [33.7–52.8] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=36) | 44.4% [29.5–60.4] | 20–35% | ❌ |
| Attacchi con opposizione | 22.0% [20.4–23.6] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 59.2% [57.2–61.2] (con ≥3: 20.9% [19.3–22.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 33.7% [31.9–35.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 11.5% [8.1–16.0] (n=252) / 77.8% [71.0–83.5] (n=167) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.0% [12.8–17.5] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 47.4% [27.3–68.3] (n=19), LDR-04 Risvegliato 78.0% [64.8–87.2] (n=50), LDR-06 Base 60.0% [31.3–83.2] (n=10), LDR-06 Risvegliato 78.8% [68.6–86.3] (n=80) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 48.8% [38.1–59.5] (n=80) | | |
| Attacchi per partita | 25.7 | | |
| Pugno attaccante vuoto / pieno | 54.8% [52.7–56.9] / 11.3% [10.1–12.7] (gemme medie 0.82) | non >90% | |
| Pugno difensore vuoto / pieno | 60.9% [58.2–63.6] / 21.2% [19.1–23.6] (gemme medie 0.24) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 924, 1: 993, 2: 434, 3: 142, 4: 51, 5: 20, 6: 2} | | |
| Azioni legali per decisione | 5.7 | <60 | ✅ |
| Fine partita | {'colpo_finale': 85, 'crepuscolo': 15} | | |
| G1 vince fra le partite finite al Crepuscolo | 33.3% [15.2–58.3] | | |
| G1 vince fra le partite arrivate al round 15 | 33.3% [16.3–56.3] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 44.4% [24.6–66.3] / 50.0% [21.5–78.5] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 12.5% [2.2–47.1]; 5.6% [1.0–25.8] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-1': 3, '0-0': 3, '1-3': 2, '2-1': 2, '2-3': 2, '1-1': 1, '3-1': 1, '2-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=9) | 50.0% [29.0–71.0] / 55.6% [26.7–81.1] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 8, 16: 1}; 88.9% [56.5–98.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 44.4% [18.9–73.3] / 11.1% [2.0–43.5]; 1.78 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–29.9] / 77.8% [45.3–93.7] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 25.0% [4.6–69.9]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.0% [2.2–11.2] / 27.8% [12.5–50.9]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 1, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=5) | 0.0% [0.0–43.4] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 44.4% [24.6–66.3] (16.7% [5.8–39.2]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 6, 'rif_LDR06_ferite_e_caccia': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR06_ferite_e_caccia 33% (n=18) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 60.0% [50.2–69.1], rif_LDR06_ferite_e_caccia 40.0% [30.9–49.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.374 / 0.075 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.075 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.09 (0.00), rif_LDR06_ferite_e_caccia 0.08 (0.01) | |
| M4 | Scontri decisi prima dell'impegno | 35.9% [34.0–37.7] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.02 (144 / 358); 62.2% [60.3–64.1] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 53.6% [52.2–55.1]; rif_LDR04_stanca_e_smonta 57.0%, rif_LDR06_ferite_e_caccia 50.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.7] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.383 (46) / 0.322 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 14.0 (40%, 60 vittorie), LDR-06 G: 17.0 (49%, 40 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 3.99, LDR-06 2.52, VER-020 1.72, VER-008 1.07, NER-017 0.93, BLU-023 0.73, BLU-015 0.62, NEU-012 0.60, NER-013 0.57, VER-001 0.56, VER-003 0.54, NER-001 0.53 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.75, rif_LDR06_ferite_e_caccia 3.14 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.24, rif_LDR06_ferite_e_caccia 0.20 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 64% (n=14), rif_LDR06_ferite_e_caccia 32% (n=22) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.3% [10.1–12.7] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR06_ferite_e_caccia 0.93; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-008 100%, VER-001 100%, collante 100%, caccia 100%, VER-023 100%, ponte 100%, NEU-011 60%, RS 60%, VER-014 60%, BLU-010 60%, NEU-009 60%, NEU-003 60%; oltre il 60%: VER-001, VER-008, VER-023 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 60.0 [50–69] (100) |
| rif_LDR06_ferite_e_caccia | 40.0 [31–50] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.15 | 1.61 | 3.99 / 0.00 | 0.00 | 0.63 | 5.2 (100) | 8 | B 41%, G 59% | 2.45 | 0.72 |
| rif_LDR06_ferite_e_caccia | 4.25 | 0.00 | 2.52 / 0.06 | 0.00 | 0.15 | 4.4 (98) | 9 | G 56%, K 44% | 2.34 | 1.64 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.43/0.17/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.82/0.22/0.46/0.15 | 0.36/0.00/0.12/0.04 | 0.65/0.62/0.32/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.73/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.60/0.06/0.48 | 0.60/0.00/0.00/0.00 | 0.61/0.00/0.12/0.05 | 0.00/0.00/0.00/0.00 | 0.40/0.26/0.21/0.14 | 0.00/0.31/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.99/2.06/0.33 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.27/0.30/0.02/0.14 | 0.00/0.00/0.00/0.00 | 0.38/0.21/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.18/0.20/0.01 | 0.29/0.00/0.01/0.00 | 0.28/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.86/0.01/0.36 | 0.49/0.03/0.03/0.02 | 0.34/0.00/0.11/0.02 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.52/0.04/0.40 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.57/0.57/0.25 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.52/2.13/0.64 | 0.00/0.00/0.00/0.00 | 0.60/0.00/0.00/0.00 | 0.33/0.64/0.04/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.53/0.20/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.06/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.10/0.24/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.11/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.25/0.05/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.60/0.05/0.39 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/1.29/0.02/0.54 | 0.28/0.04/0.03/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.82/0.41/0.14/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.51 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.07 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.01 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.73 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.24 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 1.01 | 0.00 | 0.03 | 0.10 | 0.07 | 0.09 | 0.11 | 0.15 | 0.12 | 0.18 | 0.06 | 0.03 | 0.00 | 0.04 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.88 | 0.00 | 0.03 | 0.09 | 0.03 | 0.08 | 0.10 | 0.10 | 0.15 | 0.09 | 0.07 | 0.05 | 0.05 | 0.03 | 0.01 | 0.93 | 0.11 | 0.14 | 0.05 | 0.05 | 0.15 | 0.12 | 0.07 | 0.04 | 0.12 | 0.05 | 0.02 | 0.00 | 0.01 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 0 | 0 | 1 |
| 8 | 2 | 1 | 0 | 3 |
| 9 | 6 | 2 | 0 | 8 |
| 10 | 4 | 7 | 0 | 11 |
| 11 | 11 | 9 | 0 | 20 |
| 12 | 5 | 9 | 0 | 14 |
| 13 | 4 | 7 | 0 | 11 |
| 14 | 5 | 9 | 0 | 14 |
| 15 | 6 | 11 | 0 | 17 |
| 16 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 57.0% | 0.092 | 1.91 | 0.84 | 0.00 | 0.00 | 2.04 | 0.00 | 0.00 | 0.310 |
| rif_LDR06_ferite_e_caccia | 100 | 50.3% | 0.056 | 0.82 | 2.32 | 0.00 | 0.00 | 4.45 | 0.00 | 0.00 | 0.449 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 263 | 0.859 | 0.783 | 0.711 | 0.449 | 1115 | 0.676 | 0.160 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 263 | 0.167 | 0.148 | 0.118 | 0.034 | 1115 | 0.080 | 0.039 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 225 | 0.973 | 0.920 | 0.880 | 0.258 | 963 | 0.924 | 0.327 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 225 | 0.262 | 0.249 | 0.213 | 0.036 | 963 | 0.185 | 0.070 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 100 | 15.0% | 2.27 | 1.93 | 29.8% | 0.0% | 23.0% | 28.8% | 7.6% | 0.00 | 14.2% | 57.0% | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 15.0% | 2.27 | 1.93 | 15.9% | 0.0% | 23.0% | 27.9% | 7.4% | 0.00 | 9.0% | 50.3% | 0.05 | 0.00 |
| Totale | 200 | 15.0% | 2.27 | 1.93 | 21.8% | 0.0% | 23.0% | 28.3% | 7.5% | 0.00 | 11.6% | 53.6% | 0.03 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

