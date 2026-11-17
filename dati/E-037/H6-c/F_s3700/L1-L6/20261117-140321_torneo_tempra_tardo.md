# Torneo v0.2 — /root/in37/dati/E-037-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in37/dati/E-037-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 667s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 30.6% [28.7–32.4] | 30–45% | ✅ |
| Durata mediana (round) | 10.0 [10.0–11.0] (media 10.58) | 8–11 | ✅ |
| Partite al round 13+ | 26.0% [18.4–35.4] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=51) | 25.5% [15.5–38.9] | 20–35% | ✅ |
| Attacchi con opposizione | 26.4% [24.7–28.2] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 58.1% [55.9–60.2] (con ≥3: 20.7% [19.0–22.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.2% [34.3–38.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 3.6% [1.8–7.3] (n=192) / 89.7% [83.9–93.5] (n=155) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 16.0% [13.7–18.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 50.0% [18.8–81.2] (n=6), LDR-01 Risvegliato 80.5% [66.0–89.8] (n=41), LDR-06 Base 0.0% [0.0–79.3] (n=1), LDR-06 Risvegliato 66.3% [56.5–74.9] (n=98) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 35.1% [25.2–46.5] (n=74) | | |
| Attacchi per partita | 24.0 | | |
| Pugno attaccante vuoto / pieno | 53.5% [51.4–55.6] / 11.9% [10.6–13.3] (gemme medie 0.81) | non >90% | |
| Pugno difensore vuoto / pieno | 57.3% [54.4–60.2] / 25.0% [22.5–27.6] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 741, 1: 840, 2: 548, 3: 190, 4: 59, 5: 18, 6: 3} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 97, 'crepuscolo': 3} | | |
| G1 vince fra le partite finite al Crepuscolo | 0.0% [0.0–56.2] | | |
| G1 vince fra le partite arrivate al round 15 | 0.0% [0.0–49.0] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 75.0% [30.1–95.4] / 100.0% [43.8–100.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 0.0% [0.0–56.2]; 0.0% [0.0–49.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-0': 3, '2-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=3) | 75.0% [30.1–95.4] / 100.0% [43.8–100.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 3}; 100.0% [43.8–100.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 33.3% [6.1–79.2] / 0.0% [0.0–56.2]; 1.67 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–56.2] / 33.3% [6.1–79.2] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / nan% [nan–nan]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.0–8.5] / 75.0% [30.1–95.4]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 2, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=4) / turno di G2 (n=5) | 0.0% [0.0–49.0] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=4) | 0.0% [0.0–49.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 25.0% [4.6–69.9] (25.0% [4.6–69.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 2, 'rif_LDR01_puntata_e_preda': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR06_ferite_e_caccia 0% (n=4) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 55.0% [45.2–64.4], rif_LDR06_ferite_e_caccia 45.0% [35.6–54.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.366 / 0.080 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.080 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.06 (0.00), rif_LDR06_ferite_e_caccia 0.16 (0.09) | |
| M4 | Scontri decisi prima dell'impegno | 34.9% [33.0–36.9] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.09 (140 / 369); 57.3% [55.3–59.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 45.5% [44.0–47.0]; rif_LDR01_puntata_e_preda 51.4%, rif_LDR06_ferite_e_caccia 40.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.374 (181) / 0.338 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 55 vittorie), LDR-06 G: 17.0 (49%, 45 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 4.58, LDR-01 2.03, VER-020 1.95, ROS-016 1.19, NER-017 1.14, NEU-001 0.90, NER-009 0.80, VER-008 0.70, NER-013 0.68, ROS-018 0.65, NER-001 0.62, VER-001 0.61 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.93, rif_LDR06_ferite_e_caccia 3.28 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.02, rif_LDR06_ferite_e_caccia 0.26 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 0% (n=3), rif_LDR06_ferite_e_caccia 27% (n=48) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.9% [10.6–13.3] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR06_ferite_e_caccia 1.37; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-001 100%, VER-008 100%, ponte 100%, caccia 100%, VER-011 55%, ROS-016 55%, collante 45%, NEW-B06 45%, NEU-001 45%, NER-009 45%, NEU-012 45%, NER-017 45%; oltre il 60%: VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 55.0 [45–64] (100) |
| rif_LDR06_ferite_e_caccia | 45.0 [36–55] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.63 | 0.00 | 2.03 / 0.00 | 0.00 | 0.00 | 4.6 (100) | 12 | G 40%, R 60% | 2.40 | 0.43 |
| rif_LDR06_ferite_e_caccia | 3.23 | 0.00 | 4.58 / 0.25 | 0.00 | 0.17 | 4.2 (94) | 11 | G 52%, K 48% | 1.77 | 1.73 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR01_puntata_e_preda | 2.03 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.85 | 2.73 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/2.03/1.69/0.47 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.31/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.38/0.15/0.05 | 0.72/0.16/0.48/0.29 | 0.59/0.27/0.07/0.06 | 0.00/0.37/0.00/0.00 | 0.74/0.00/0.17/0.06 | 0.70/0.25/0.27/0.18 | 0.84/1.19/0.07/0.51 | 0.52/0.65/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.46/0.34/0.26 | 0.18/0.02/0.10/0.03 | 0.00/0.00/0.00/0.00 | 0.71/0.62/0.02/0.50 | 0.66/0.00/0.00/0.00 | 0.74/0.00/0.16/0.07 | 0.79/0.46/0.18/0.06 | 0.70/0.28/0.35/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.02/0.01 | 0.41/0.02/0.03/0.00 | 0.33/0.05/0.05/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.05/0.04 | 0.37/0.36/0.01/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.29/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.17/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.60/0.08/0.50 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.40/0.40/0.19 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/4.58/1.78/0.61 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.62/0.34/0.10 | 0.28/0.27/0.05/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.26/0.13/0.27/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.22/0.02/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.50/0.41/0.06/0.37 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/1.05/0.03/0.53 | 0.32/0.02/0.07/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.90/0.18/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.61/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.16/0.19/0.05/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.14/0.05 | 0.24/0.54/0.07/0.10 | 0.37/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.98 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.13 | 0.00 | 0.00 | 0.01 | 0.18 | 0.07 | 0.00 | 0.00 | 0.28 | 0.01 | 0.00 | 0.05 | 0.00 | 0.02 | 0.02 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.35 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.81 | 0.00 | 0.05 | 0.04 | 0.09 | 0.11 | 0.16 | 0.09 | 0.08 | 0.07 | 0.04 | 0.04 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.77 | 0.00 | 0.04 | 0.08 | 0.06 | 0.07 | 0.07 | 0.11 | 0.15 | 0.08 | 0.03 | 0.04 | 0.01 | 0.03 | 1.37 | 0.20 | 0.27 | 0.26 | 0.18 | 0.17 | 0.13 | 0.05 | 0.06 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR01_puntata_e_preda | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.96 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 0 | 0 | 1 |
| 7 | 3 | 3 | 0 | 6 |
| 8 | 8 | 7 | 0 | 15 |
| 9 | 8 | 6 | 0 | 14 |
| 10 | 7 | 8 | 0 | 15 |
| 11 | 8 | 9 | 0 | 17 |
| 12 | 2 | 4 | 0 | 6 |
| 13 | 6 | 7 | 0 | 13 |
| 14 | 4 | 5 | 0 | 9 |
| 15 | 0 | 4 | 0 | 4 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 51.4% | 0.074 | 0.00 | 0.93 | 0.00 | 0.00 | 2.96 | 0.00 | 0.00 | 0.338 |
| rif_LDR06_ferite_e_caccia | 100 | 40.3% | 0.087 | 0.84 | 2.44 | 0.00 | 0.00 | 5.01 | 0.00 | 0.00 | 0.400 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 259 | 0.857 | 0.780 | 0.710 | 0.351 | 1047 | 0.808 | 0.195 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 259 | 0.151 | 0.131 | 0.108 | 0.023 | 1047 | 0.151 | 0.058 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 220 | 0.845 | 0.773 | 0.705 | 0.359 | 873 | 0.766 | 0.234 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 220 | 0.309 | 0.241 | 0.218 | 0.073 | 873 | 0.246 | 0.093 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 3.0% | 1.96 | 1.76 | 25.9% | 0.0% | 22.3% | 24.4% | 2.7% | 0.00 | 14.9% | 51.4% | 0.06 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 3.0% | 1.96 | 1.76 | 32.9% | 0.0% | 18.7% | 29.3% | 11.5% | 0.00 | 12.3% | 40.3% | 0.18 | 0.00 |
| Totale | 200 | 3.0% | 1.96 | 1.76 | 30.1% | 0.0% | 20.5% | 26.9% | 7.7% | 0.00 | 13.5% | 45.5% | 0.12 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.249 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.21 |
| rif_LDR06_ferite_e_caccia | 100 | 0.283 | 0.056 | 0.0% | 0.0% | 0.44 | 0.02 | 0.05 | 0.00 | 0.00 | 0.00 | 4.48 |

