# Torneo v0.2 — /root/in37/dati/E-037-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in37/dati/E-037-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 875s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 45.7% [43.7–47.7] | 30–45% | ❌ |
| Durata mediana (round) | 12.0 [11.5–13.0] (media 12.08) | 8–11 | ❌ |
| Partite al round 13+ | 49.0% [39.4–58.7] | ≤12% | ❌ |
| Partite oltre il 15 | 4.0% [1.6–9.8] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=54) | 16.7% [9.0–28.7] | 20–35% | ❌ |
| Attacchi con opposizione | 28.9% [27.1–30.7] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 62.4% [60.5–64.4] (con ≥3: 22.3% [20.6–24.0]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 32.5% [30.6–34.4] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 8.9% [5.6–13.8] (n=191) / 84.4% [77.1–89.7] (n=128) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.0% [11.8–16.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 56.2% [33.2–76.9] (n=16), LDR-02 Risvegliato 61.5% [42.5–77.6] (n=26), LDR-06 Base 0.0% [0.0–79.3] (n=1), LDR-06 Risvegliato 80.5% [70.6–87.6] (n=82) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 56.2% [44.8–67.0] (n=73) | | |
| Attacchi per partita | 23.7 | | |
| Pugno attaccante vuoto / pieno | 57.6% [55.5–59.7] / 9.9% [8.7–11.2] (gemme medie 0.82) | non >90% | |
| Pugno difensore vuoto / pieno | 49.4% [46.6–52.2] / 28.7% [26.2–31.3] (gemme medie 0.33) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 802, 1: 877, 2: 429, 3: 190, 4: 50, 5: 16, 6: 2} | | |
| Azioni legali per decisione | 5.7 | <60 | ✅ |
| Fine partita | {'crepuscolo': 13, 'colpo_finale': 87} | | |
| G1 vince fra le partite finite al Crepuscolo | 76.9% [49.7–91.8] | | |
| G1 vince fra le partite arrivate al round 15 | 70.6% [46.9–86.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 29.4% [13.3–53.1] / 20.0% [3.6–62.4] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 80.0% [37.6–96.4]; 23.5% [9.6–47.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 4, '3-2': 3, '2-3': 2, '2-2': 1, '2-0': 1, '4-0': 1, '5-4': 1, '0-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=8) | 47.1% [26.2–69.0] / 25.0% [7.1–59.1] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 3, 15: 5}; 25.0% [7.1–59.1] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 87.5% [52.9–97.8] / 50.0% [21.5–78.5]; 2.25 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–32.4] / 87.5% [52.9–97.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 66.7% [30.0–90.3]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 11.8% [3.3–34.3]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 1, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=7) / turno di G2 (n=11) | 0.0% [0.0–35.4] / 0.0% [0.0–25.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=7) | 0.0% [0.0–35.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 52.9% [31.0–73.8] (5.9% [1.0–27.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 5, 'rif_LDR06_ferite_e_caccia': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR06_ferite_e_caccia 71% (n=17) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 76.0% [66.8–83.3], rif_LDR06_ferite_e_caccia 24.0% [16.7–33.2]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.529 / 0.101 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.097 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.15 (0.00), rif_LDR06_ferite_e_caccia 0.13 (0.05) | |
| M4 | Scontri decisi prima dell'impegno | 30.1% [28.3–32.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.67 (97 / 270); 58.6% [56.6–60.6] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.6% [51.2–54.0]; rif_LDR02_muro_di_parata 57.7%, rif_LDR06_ferite_e_caccia 48.7% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.386 (27) / 0.341 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 76 vittorie), LDR-06 G: 17.0 (49%, 24 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 4.20, LDR-02 2.41, VER-020 2.27, NER-017 1.23, VER-008 1.02, NEU-001 0.81, NEW-I04 0.69, VER-001 0.60, NER-003 0.52, NER-009 0.48, NEW-B06 0.48, BLU-005 0.46 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.60, rif_LDR06_ferite_e_caccia 2.55 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 0.29 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 50% (n=4), rif_LDR06_ferite_e_caccia 14% (n=50) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.9% [8.7–11.2] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 1.35; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-009 76%, RS 76%, NER-014 76%, BLU-021 76%, NEU-003 76%, NEU-015 76%, caccia 24%, NER-009 24%, VER-008 24%, NER-017 24%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 76.0 [67–83] (100) |
| rif_LDR06_ferite_e_caccia | 24.0 [17–33] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.04 | 0.00 | 2.41 / 0.00 | 0.00 | 1.26 | 5.4 (100) | 8 | B 83%, K 17% | 2.69 | 0.00 |
| rif_LDR06_ferite_e_caccia | 3.30 | 0.00 | 4.20 / 0.21 | 0.00 | 0.16 | 5.7 (97) | 10 | G 54%, K 46% | 2.16 | 1.80 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR02_muro_di_parata | 2.41 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.54 | 2.66 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.88/0.45/0.26/0.04 | 0.85/0.00/0.25/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 1.03/0.00/0.29/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.44/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.41/1.74/0.55 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.00/0.11/0.05 | 0.84/0.46/0.08/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.02/0.00/0.00 | 0.49/0.00/0.00/0.00 | 0.38/0.19/0.04/0.00 | 0.43/0.06/0.09/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.19/0.25/0.19 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.69/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.75/0.60/0.07/0.33 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.38/0.41/0.18 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/4.20/1.45/0.31 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.43/0.14/0.09 | 0.36/0.33/0.07/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.25/0.06/0.19/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.19/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.38/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.32/0.05/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/1.02/0.01/0.31 | 0.34/0.04/0.02/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.81/0.16/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.00/0.00/0.00 | 0.61/0.00/0.00/0.00 | 0.28/0.48/0.01/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.51/0.00/0.14/0.04 | 0.18/0.25/0.07/0.02 | 0.40/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.34 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.32 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.16 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 0.73 | 0.00 | 0.01 | 0.05 | 0.11 | 0.05 | 0.07 | 0.09 | 0.12 | 0.09 | 0.04 | 0.05 | 0.04 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 1.02 | 0.00 | 0.01 | 0.08 | 0.15 | 0.08 | 0.16 | 0.11 | 0.10 | 0.12 | 0.07 | 0.05 | 0.05 | 0.03 | 0.01 | 1.35 | 0.09 | 0.28 | 0.24 | 0.22 | 0.19 | 0.10 | 0.07 | 0.04 | 0.03 | 0.02 | 0.01 | 0.05 | 0.01 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR02_muro_di_parata | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.81 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 1 | 0 | 1 |
| 7 | 1 | 0 | 0 | 1 |
| 8 | 1 | 3 | 0 | 4 |
| 9 | 8 | 5 | 0 | 13 |
| 10 | 5 | 4 | 0 | 9 |
| 11 | 8 | 5 | 0 | 13 |
| 12 | 6 | 4 | 0 | 10 |
| 13 | 3 | 11 | 0 | 14 |
| 14 | 2 | 16 | 0 | 18 |
| 15 | 9 | 4 | 0 | 13 |
| 16 | 3 | 1 | 0 | 4 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 57.7% | 0.112 | 1.60 | 0.00 | 0.00 | 0.00 | 1.98 | 0.00 | 0.00 | 0.538 |
| rif_LDR06_ferite_e_caccia | 100 | 48.7% | 0.087 | 0.86 | 1.69 | 0.00 | 0.00 | 3.18 | 0.00 | 0.00 | 0.397 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 364 | 0.986 | 0.901 | 0.843 | 0.184 | 959 | 0.973 | 0.386 | 0.170 | 0.069 |
| rif_LDR02_muro_di_parata | Cicatrice | 364 | 0.294 | 0.209 | 0.148 | 0.033 | 959 | 0.218 | 0.066 | 0.019 | 0.003 |
| rif_LDR06_ferite_e_caccia | mano | 245 | 0.894 | 0.820 | 0.771 | 0.318 | 798 | 0.805 | 0.232 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 245 | 0.204 | 0.180 | 0.163 | 0.053 | 798 | 0.179 | 0.050 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 13.0% | 2.47 | 2.26 | 41.4% | 0.0% | 32.3% | 34.5% | 6.3% | 0.00 | 15.1% | 57.7% | 0.02 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 13.0% | 2.47 | 2.26 | 13.9% | 0.0% | 23.0% | 29.4% | 7.1% | 0.00 | 11.8% | 48.7% | 0.21 | 0.00 |
| Totale | 200 | 13.0% | 2.47 | 2.26 | 21.8% | 0.0% | 27.7% | 31.9% | 6.7% | 0.00 | 13.2% | 52.6% | 0.12 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 0.246 | 0.164 | 0.0% | 0.0% | 0.89 | 1.08 | 0.80 | 0.55 | 0.00 | 0.00 | 4.14 |
| rif_LDR06_ferite_e_caccia | 100 | 0.342 | 0.061 | 0.0% | 0.0% | 0.37 | 0.00 | 0.11 | 0.05 | 0.00 | 0.00 | 3.55 |

