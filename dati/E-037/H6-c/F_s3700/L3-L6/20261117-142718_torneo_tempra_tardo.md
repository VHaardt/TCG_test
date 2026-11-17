# Torneo v0.2 — /root/in37/dati/E-037-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in37/dati/E-037-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 561s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 35.1% [33.1–37.2] | 30–45% | ✅ |
| Durata mediana (round) | 10.0 [10.0–11.0] (media 10.74) | 8–11 | ✅ |
| Partite al round 13+ | 29.0% [21.0–38.5] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=40) | 40.0% [26.3–55.4] | 20–35% | ❌ |
| Attacchi con opposizione | 27.5% [25.7–29.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 58.9% [56.7–61.0] (con ≥3: 23.1% [21.3–24.9]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.1% [34.1–38.1] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 3.3% [1.3–8.1] (n=123) / 81.0% [74.7–86.0] (n=184) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 19.5% [16.8–22.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 50.0% [15.0–85.0] (n=4), LDR-03 Risvegliato 100.0% [94.7–100.0] (n=69), LDR-06 Risvegliato 73.8% [63.2–82.1] (n=80) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 30.5% [22.2–40.4] (n=95) | | |
| Attacchi per partita | 21.2 | | |
| Pugno attaccante vuoto / pieno | 57.4% [55.2–59.6] / 10.3% [9.0–11.7] (gemme medie 0.82) | non >90% | |
| Pugno difensore vuoto / pieno | 56.7% [53.7–59.6] / 26.1% [23.6–28.8] (gemme medie 0.29) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 626, 1: 805, 2: 486, 3: 145, 4: 51, 5: 9, 6: 1} | | |
| Azioni legali per decisione | 6.0 | <60 | ✅ |
| Fine partita | {'colpo_finale': 90, 'crepuscolo': 10} | | |
| G1 vince fra le partite finite al Crepuscolo | 50.0% [23.7–76.3] | | |
| G1 vince fra le partite arrivate al round 15 | 50.0% [23.7–76.3] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 70.0% [39.7–89.2] / 28.6% [8.2–64.1] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 42.9% [15.8–75.0]; 10.0% [1.8–40.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 3, '1-1': 2, '0-1': 2, '2-1': 1, '2-0': 1, '3-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=8) | 80.0% [49.0–94.3] / 37.5% [13.7–69.4] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 7, 16: 1}; 62.5% [30.6–86.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 62.5% [30.6–86.3] / 37.5% [13.7–69.4]; 2.38 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–32.4] / 87.5% [52.9–97.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 60.0% [23.1–88.2]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.0–8.5] / 30.0% [10.8–60.3]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 1, 'vinc:atk': 2, 'vinc:rim': 1} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=4) / turno di G2 (n=4) | 0.0% [0.0–49.0] / 0.0% [0.0–49.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=4) | 0.0% [0.0–49.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 70.0% [39.7–89.2] (20.0% [5.7–51.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 4, 'rif_LDR03_sanguinare_per_accendere': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR06_ferite_e_caccia 50% (n=10) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 59.0% [49.2–68.1], rif_LDR06_ferite_e_caccia 41.0% [31.9–50.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.409 / 0.090 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.090 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.09 (0.06), rif_LDR06_ferite_e_caccia 0.13 (0.06) | |
| M4 | Scontri decisi prima dell'impegno | 35.8% [33.7–37.8] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.62 (118 / 244); 60.3% [58.2–62.4] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.1% [50.7–53.6]; rif_LDR03_sanguinare_per_accendere 56.7%, rif_LDR06_ferite_e_caccia 47.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.7] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.491 (27) / 0.323 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 59 vittorie), LDR-06 G: 17.0 (49%, 41 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.53, VER-020 1.25, ROS-019 0.91, VER-008 0.77, NER-017 0.76, ROS-011 0.72, NER-006 0.67, NER-008 0.66, NER-010 0.63, NER-001 0.61, NER-013 0.59, NER-009 0.56 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.29, rif_LDR06_ferite_e_caccia 2.39 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR06_ferite_e_caccia 0.23 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 50% (n=20), rif_LDR06_ferite_e_caccia 30% (n=20) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.3% [9.0–11.7] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.71, rif_LDR06_ferite_e_caccia 1.36; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, NER-017 100%, caccia 100%, NER-009 100%, ROS-011 59%, NER-010 59%, NEU-001 41%, NEW-B06 41%, collante 41%, VER-020 41%, NEU-012 41%, NER-015 41%; oltre il 60%: NER-009, NER-017 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 59.0 [49–68] (100) |
| rif_LDR06_ferite_e_caccia | 41.0 [32–51] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.18 | 0.00 | 0.00 / 0.00 | 2.70 | 0.00 | 5.1 (100) | 8 | K 60%, R 40% | 2.01 | 0.32 |
| rif_LDR06_ferite_e_caccia | 3.17 | 0.00 | 3.53 / 0.13 | 0.00 | 0.09 | 4.6 (96) | 10 | G 51%, K 49% | 2.36 | 1.32 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.51 | 2.02 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.05/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.53/0.47 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.87/0.26/0.20 | 0.85/0.98/0.17/0.07 | 0.00/0.00/0.00/0.00 | 0.03/0.00/0.00/0.00 | 0.39/0.10/0.22/0.10 | 0.00/0.22/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.41/0.07/0.15/0.06 | 0.63/0.91/0.24/0.30 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.00/0.10/0.03 | 0.73/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.51/0.03/0.37 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.47/0.29/0.26 | 0.00/0.29/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.53/1.54/0.41 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.35/0.13/0.08 | 0.36/0.36/0.04/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.08/0.25/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.19/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.26/0.01/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.33/0.02/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.77/0.01/0.38 | 0.34/0.02/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.46/0.11/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.19/0.25/0.04/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.04/0.03 | 0.22/0.33/0.05/0.04 | 0.45/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.62 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.95 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 0.97 | 0.00 | 0.01 | 0.07 | 0.12 | 0.13 | 0.18 | 0.12 | 0.11 | 0.09 | 0.05 | 0.04 | 0.03 | 0.01 | 0.01 | 1.71 | 0.28 | 0.20 | 0.40 | 0.29 | 0.17 | 0.13 | 0.08 | 0.08 | 0.02 | 0.02 | 0.02 | 0.00 | 0.02 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.79 | 0.00 | 0.01 | 0.04 | 0.11 | 0.07 | 0.13 | 0.12 | 0.15 | 0.05 | 0.05 | 0.04 | 0.02 | 0.00 | 0.00 | 1.36 | 0.13 | 0.26 | 0.27 | 0.22 | 0.18 | 0.10 | 0.12 | 0.03 | 0.04 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca | NER-002 stanca | NER-002 vita |
|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.53 | 0.20 |
| rif_LDR06_ferite_e_caccia | 0.59 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 0 | 1 | 0 | 1 |
| 7 | 1 | 4 | 0 | 5 |
| 8 | 11 | 3 | 0 | 14 |
| 9 | 6 | 10 | 0 | 16 |
| 10 | 6 | 8 | 0 | 14 |
| 11 | 6 | 7 | 0 | 13 |
| 12 | 2 | 5 | 0 | 7 |
| 13 | 6 | 6 | 0 | 12 |
| 14 | 2 | 5 | 0 | 7 |
| 15 | 5 | 4 | 0 | 9 |
| 16 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 56.7% | 0.089 | 0.75 | 0.54 | 0.00 | 0.00 | 2.73 | 0.00 | 0.00 | 0.477 |
| rif_LDR06_ferite_e_caccia | 100 | 47.1% | 0.092 | 0.77 | 1.62 | 0.00 | 0.00 | 3.38 | 0.00 | 0.00 | 0.343 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 235 | 0.911 | 0.898 | 0.877 | 0.357 | 808 | 0.833 | 0.322 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 235 | 0.285 | 0.268 | 0.247 | 0.038 | 808 | 0.248 | 0.098 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 233 | 0.785 | 0.717 | 0.648 | 0.369 | 847 | 0.736 | 0.189 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 233 | 0.240 | 0.202 | 0.185 | 0.056 | 847 | 0.196 | 0.058 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 10.0% | 1.93 | 1.97 | 40.4% | 1.0% | 22.7% | 30.3% | 10.5% | 0.00 | 11.3% | 56.7% | 0.05 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 10.0% | 1.93 | 1.97 | 34.2% | 1.0% | 21.7% | 32.3% | 9.9% | 0.00 | 14.1% | 47.1% | 0.11 | 0.00 |
| Totale | 200 | 10.0% | 1.93 | 1.97 | 36.8% | 1.0% | 22.2% | 31.3% | 10.2% | 0.00 | 12.6% | 52.1% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 0.258 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.41 |
| rif_LDR06_ferite_e_caccia | 100 | 0.292 | 0.051 | 0.0% | 0.0% | 0.42 | 0.04 | 0.02 | 0.05 | 0.00 | 0.00 | 3.25 |

