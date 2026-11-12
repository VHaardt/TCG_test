# Torneo v0.2 — /home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json

- Regole `v0.2`, configurazione `/home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json`; differenze da B0: {'pugno': 'sequenziale', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L')}
- IA: forte:30; partite: 200; tempo 1761s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 36.8% [35.5–38.1] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [11.0–12.0] (media 11.41) | 8–11 | ✅ |
| Partite al round 13+ | 41.5% [34.9–48.4] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.5% [0.1–2.8] | 0 | ❌ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=84) | 22.6% [15.0–32.6] | 20–35% | ✅ |
| Attacchi con opposizione | 31.0% [29.7–32.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 62.0% [60.5–63.4] (con ≥3: 22.2% [21.0–23.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 33.5% [32.2–34.8] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–1.1] (n=358) / 90.1% [86.1–93.0] (n=293) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.4% [13.8–17.2] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-05 Risvegliato 83.1% [73.7–89.7] (n=83), LDR-06 Risvegliato 71.8% [64.9–77.9] (n=181) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 49.7% [41.8–57.6] (n=151) | | |
| Attacchi per partita | 25.5 | | |
| Pugno attaccante vuoto / pieno | 55.1% [53.6–56.5] / 11.1% [10.2–12.0] (gemme medie 0.80) | non >90% | |
| Pugno difensore vuoto / pieno | 56.9% [55.0–58.8] / 26.0% [24.3–27.7] (gemme medie 0.28) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1638, 1: 1716, 2: 1207, 3: 375, 4: 119, 5: 44, 6: 7} | | |
| Azioni legali per decisione | 5.6 | <60 | ✅ |
| Fine partita | {'colpo_finale': 173, 'crepuscolo': 27} | | |
| G1 vince fra le partite finite al Crepuscolo | 70.4% [51.5–84.1] | | |
| G1 vince fra le partite arrivate al round 15 | 65.6% [48.3–79.6] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 46.9% [30.9–63.6] / 26.7% [10.9–52.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 66.7% [41.7–84.8]; 9.4% [3.2–24.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 10, '3-2': 3, '1-1': 3, '2-1': 3, '2-3': 2, '2-0': 2, '0-2': 1, '1-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=17) | 53.1% [36.4–69.1] / 29.4% [13.3–53.1] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15, 16: 2}; 35.3% [17.3–58.7] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 64.7% [41.3–82.7] / 52.9% [31.0–73.8]; 2.71 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–18.4] / 100.0% [81.6–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 75.0% [46.8–91.1]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.5% [1.1–5.7] / 15.6% [6.9–31.8]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 2, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=9) / turno di G2 (n=10) | 0.0% [0.0–29.9] / 0.0% [0.0–27.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=9) | 0.0% [0.0–29.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 53.1% [36.4–69.1] (9.4% [3.2–24.2]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 9, 'rif_LDR06_ferite_e_caccia': 8} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR05_scudi_armati vs rif_LDR06_ferite_e_caccia 66% (n=32) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR05_scudi_armati 75.5% [69.1–80.9], rif_LDR06_ferite_e_caccia 24.5% [19.1–30.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.407 / 0.094 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.092 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR05_scudi_armati 0.15 (0.00), rif_LDR06_ferite_e_caccia 0.12 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 31.1% [29.9–32.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 4.26 (288 / 565); 57.3% [56.0–58.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 48.0% [47.0–49.1]; rif_LDR05_scudi_armati 53.1%, rif_LDR06_ferite_e_caccia 43.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 2.5% [1.9–3.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.319 (447) / 0.322 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-05 R: 18.0 (49%, 151 vittorie), LDR-06 G: 17.0 (49%, 49 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.32, LDR-05 2.77, VER-020 2.59, NER-017 1.17, VER-008 1.05, NER-013 0.76, NER-009 0.72, BLU-015 0.69, VER-001 0.68, NEU-001 0.63, ROS-020 0.62, ROS-018 0.58 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR05_scudi_armati 0.13, rif_LDR06_ferite_e_caccia 3.05 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.24 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR05_scudi_armati 40% (n=10), rif_LDR06_ferite_e_caccia 20% (n=74) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.1% [10.2–12.0] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.96; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-013 76%, BLU-010 76%, BLU-008 76%, BLU-021 76%, NEU-009 76%, ROS-020 76%, NER-017 24%, caccia 24%, VER-020 24%, NER-015 24%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR05_scudi_armati | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR05_scudi_armati | — | 75.5 [69–81] (200) |
| rif_LDR06_ferite_e_caccia | 24.5 [19–31] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 3.90 | 0.00 | 2.77 / 0.00 | 0.00 | 0.67 | 5.0 (200) | 13 | B 45%, R 55% | 2.60 | 0.00 |
| rif_LDR06_ferite_e_caccia | 4.00 | 0.00 | 3.32 / 0.07 | 0.00 | 0.26 | 5.3 (194) | 10 | G 57%, K 43% | 2.23 | 1.49 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.77/1.62/0.45 | 0.65/0.49/0.09/0.05 | 0.60/0.00/0.13/0.03 | 0.58/0.26/0.14/0.04 | 0.62/0.13/0.15/0.10 | 0.67/0.00/0.18/0.13 | 0.72/0.69/0.29/0.23 | 0.00/0.56/0.00/0.00 | 0.00/0.56/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.40/0.29/0.14 | 0.77/0.35/0.12/0.07 | 0.00/0.00/0.00/0.00 | 0.68/0.34/0.09/0.07 | 0.00/0.38/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.24/0.34/0.17 | 0.00/0.00/0.00/0.00 | 0.37/0.58/0.00/0.00 | 0.70/0.62/0.41/0.28 | 0.55/0.55/0.32/0.34 | 0.24/0.06/0.16/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.00/0.06/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.07/0.04/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.03/0.03 | 0.36/0.02/0.01/0.01 | 0.35/0.07/0.12/0.06 | 0.29/0.20/0.12/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.68/0.04/0.45 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.38/0.44/0.30 | 0.00/0.25/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.32/1.63/0.73 | 0.00/0.00/0.00/0.00 | 0.68/0.00/0.00/0.00 | 0.26/0.34/0.03/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.48/0.17/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.17/0.36/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.40/0.03/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.53/0.04/0.37 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/1.05/0.03/0.46 | 0.38/0.03/0.06/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.63/0.14/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 1.23 | 0.00 | 0.09 | 0.00 | 0.01 | 0.01 | 0.03 | 0.03 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.24 | 0.34 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.03 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.62 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 0.53 | 0.00 | 0.01 | 0.02 | 0.02 | 0.06 | 0.09 | 0.09 | 0.07 | 0.05 | 0.04 | 0.04 | 0.01 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.87 | 0.00 | 0.01 | 0.06 | 0.07 | 0.10 | 0.12 | 0.13 | 0.10 | 0.07 | 0.07 | 0.07 | 0.04 | 0.04 | 0.01 | 0.96 | 0.12 | 0.23 | 0.11 | 0.12 | 0.10 | 0.09 | 0.07 | 0.04 | 0.04 | 0.03 | 0.01 | 0.00 | 0.01 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 4 | 0 | 1 | 0 | 1 |
| 6 | 1 | 3 | 0 | 4 |
| 7 | 4 | 6 | 0 | 10 |
| 8 | 10 | 5 | 0 | 15 |
| 9 | 13 | 11 | 0 | 24 |
| 10 | 13 | 15 | 0 | 28 |
| 11 | 13 | 9 | 0 | 22 |
| 12 | 6 | 7 | 0 | 13 |
| 13 | 11 | 15 | 0 | 26 |
| 14 | 9 | 16 | 0 | 25 |
| 15 | 19 | 10 | 0 | 29 |
| 16 | 2 | 1 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 53.1% | 0.117 | 0.13 | 0.00 | 0.00 | 0.00 | 2.52 | 0.00 | 0.00 | 0.368 |
| rif_LDR06_ferite_e_caccia | 200 | 43.1% | 0.066 | 0.87 | 2.18 | 0.00 | 0.00 | 5.06 | 0.00 | 0.00 | 0.455 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | mano | 727 | 0.828 | 0.810 | 0.803 | 0.410 | 2082 | 0.710 | 0.196 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 727 | 0.116 | 0.109 | 0.106 | 0.043 | 2082 | 0.096 | 0.034 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 380 | 0.924 | 0.897 | 0.853 | 0.337 | 1917 | 0.895 | 0.355 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 380 | 0.266 | 0.237 | 0.221 | 0.061 | 1917 | 0.231 | 0.105 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 13.5% | 2.12 | 1.88 | 48.6% | 0.5% | 27.3% | 29.4% | 11.1% | 0.00 | 17.4% | 53.1% | 0.06 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 13.5% | 2.12 | 1.88 | 14.6% | 0.5% | 24.7% | 29.1% | 8.2% | 0.00 | 13.3% | 43.1% | 0.04 | 0.00 |
| Totale | 400 | 13.5% | 2.12 | 1.88 | 25.3% | 0.5% | 26.0% | 29.2% | 9.4% | 0.00 | 15.3% | 48.0% | 0.05 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 0.313 | 0.156 | 4.4% | 8.9% | 1.47 | 1.12 | 0.27 | 0.41 | 0.00 | 0.00 | 4.71 |
| rif_LDR06_ferite_e_caccia | 200 | 0.306 | 0.052 | 0.1% | 0.8% | 0.53 | 0.00 | 0.11 | 0.01 | 0.00 | 0.00 | 3.84 |

