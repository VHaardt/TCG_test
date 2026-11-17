# Torneo v0.2 — /root/in37/dati/E-037-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in37/dati/E-037-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 842s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 31.1% [29.4–32.9] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.0–13.0] (media 11.68) | 8–11 | ❌ |
| Partite al round 13+ | 44.0% [34.7–53.8] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=43) | 41.9% [28.4–56.7] | 20–35% | ❌ |
| Attacchi con opposizione | 27.4% [25.7–29.1] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 60.9% [58.9–62.9] (con ≥3: 21.4% [19.8–23.1]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.2% [34.4–38.1] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.6% [4.0–10.8] (n=211) / 83.7% [76.9–88.8] (n=147) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.8% [10.8–15.0] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 54.5% [28.0–78.7] (n=11), LDR-01 Risvegliato 71.1% [56.6–82.3] (n=45), LDR-06 Base 66.7% [20.8–93.9] (n=3), LDR-06 Risvegliato 69.2% [58.3–78.4] (n=78) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 48.2% [37.8–58.8] (n=83) | | |
| Attacchi per partita | 26.6 | | |
| Pugno attaccante vuoto / pieno | 50.6% [48.6–52.6] / 12.2% [11.0–13.6] (gemme medie 0.89) | non >90% | |
| Pugno difensore vuoto / pieno | 60.3% [57.6–62.9] / 24.1% [21.8–26.5] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 786, 1: 906, 2: 669, 3: 187, 4: 71, 5: 32, 6: 6} | | |
| Azioni legali per decisione | 5.8 | <60 | ✅ |
| Fine partita | {'colpo_finale': 94, 'crepuscolo': 6} | | |
| G1 vince fra le partite finite al Crepuscolo | 50.0% [18.8–81.2] | | |
| G1 vince fra le partite arrivate al round 15 | 30.0% [10.8–60.3] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 30.0% [10.8–60.3] / 66.7% [20.8–93.9] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [6.1–79.2]; 0.0% [0.0–27.8] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'3-1': 1, '2-3': 1, '3-5': 1, '1-0': 1, '1-2': 1, '0-0': 1, '2-1': 1, '2-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=3) | 30.0% [10.8–60.3] / 66.7% [20.8–93.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 3}; 66.7% [20.8–93.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 33.3% [6.1–79.2] / 0.0% [0.0–56.2]; 1.33 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–56.2] / 100.0% [43.8–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 0.0% [0.0–79.3]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.6–7.0] / 20.0% [5.7–51.0]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 1, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=4) / turno di G2 (n=5) | 0.0% [0.0–49.0] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=4) | 0.0% [0.0–49.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 20.0% [5.7–51.0] (0.0% [0.0–27.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 2, 'rif_LDR01_puntata_e_preda': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR06_ferite_e_caccia 30% (n=10) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 50.0% [40.4–59.6], rif_LDR06_ferite_e_caccia 50.0% [40.4–59.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.373 / 0.079 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.079 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.11 (0.00), rif_LDR06_ferite_e_caccia 0.20 (0.05) | |
| M4 | Scontri decisi prima dell'impegno | 32.2% [30.5–34.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.65 (159 / 406); 57.4% [55.5–59.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 46.9% [45.5–48.3]; rif_LDR01_puntata_e_preda 51.5%, rif_LDR06_ferite_e_caccia 42.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.361 (238) / 0.329 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 50 vittorie), LDR-06 G: 17.0 (49%, 50 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.90, VER-020 2.27, LDR-01 1.98, NER-017 1.96, ROS-016 1.43, NER-013 0.85, VER-008 0.84, NEU-001 0.76, ROS-018 0.75, VER-011 0.71, NER-001 0.60, NER-009 0.59 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.78, rif_LDR06_ferite_e_caccia 3.47 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR06_ferite_e_caccia 0.39 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 35% (n=17), rif_LDR06_ferite_e_caccia 46% (n=26) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.2% [11.0–13.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR06_ferite_e_caccia 1.31; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-001 100%, caccia 100%, ponte 100%, VER-008 100%, NEU-012 50%, NER-017 50%, VER-020 50%, NEW-B06 50%, NER-009 50%, NEU-001 50%, collante 50%, NER-015 50%; oltre il 60%: VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 50.0 [40–60] (100) |
| rif_LDR06_ferite_e_caccia | 50.0 [40–60] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.91 | 0.00 | 1.98 / 0.00 | 0.00 | 0.00 | 4.9 (100) | 13 | G 39%, R 61% | 2.43 | 0.48 |
| rif_LDR06_ferite_e_caccia | 3.67 | 0.00 | 3.90 / 0.35 | 0.00 | 0.21 | 4.6 (99) | 9 | G 51%, K 49% | 1.95 | 1.82 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR01_puntata_e_preda | 1.98 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.57 | 2.33 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.98/1.86/0.49 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.36/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.46/0.16/0.08 | 0.84/0.14/0.51/0.46 | 0.71/0.33/0.15/0.06 | 0.00/0.48/0.00/0.00 | 0.79/0.00/0.26/0.10 | 0.70/0.21/0.30/0.10 | 0.87/1.43/0.08/0.63 | 0.67/0.75/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.61/0.50/0.36/0.27 | 0.17/0.03/0.16/0.13 | 0.00/0.00/0.00/0.00 | 0.76/0.51/0.01/0.41 | 0.60/0.00/0.00/0.00 | 0.83/0.00/0.13/0.08 | 0.85/0.71/0.29/0.10 | 0.63/0.51/0.34/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.06/0.01 | 0.45/0.05/0.07/0.03 | 0.37/0.08/0.06/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.00/0.11/0.01 | 0.40/0.45/0.02/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.22/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.25/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.64/0.06/0.50 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.45/0.53/0.14 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.90/1.72/0.77 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.60/0.30/0.12 | 0.35/0.36/0.09/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.23/0.08/0.11/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.33/0.02/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.42/0.05/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/1.23/0.03/0.61 | 0.37/0.04/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.86/0.76/0.23/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.21/0.39/0.02/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.00/0.11/0.02 | 0.24/0.53/0.22/0.07 | 0.48/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.99 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.17 | 0.00 | 0.00 | 0.01 | 0.11 | 0.09 | 0.00 | 0.00 | 0.24 | 0.05 | 0.00 | 0.01 | 0.00 | 0.01 | 0.05 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.78 | 0.00 | 0.01 | 0.08 | 0.02 | 0.11 | 0.14 | 0.13 | 0.09 | 0.04 | 0.05 | 0.06 | 0.04 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.87 | 0.00 | 0.03 | 0.04 | 0.02 | 0.05 | 0.06 | 0.11 | 0.14 | 0.10 | 0.09 | 0.09 | 0.07 | 0.05 | 0.02 | 1.31 | 0.13 | 0.16 | 0.21 | 0.14 | 0.19 | 0.14 | 0.12 | 0.09 | 0.08 | 0.02 | 0.00 | 0.02 | 0.01 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR01_puntata_e_preda | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.72 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 0 | 0 | 1 |
| 8 | 6 | 3 | 0 | 9 |
| 9 | 5 | 3 | 0 | 8 |
| 10 | 11 | 6 | 0 | 17 |
| 11 | 6 | 5 | 0 | 11 |
| 12 | 2 | 8 | 0 | 10 |
| 13 | 18 | 2 | 0 | 20 |
| 14 | 4 | 10 | 0 | 14 |
| 15 | 3 | 7 | 0 | 10 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 51.5% | 0.075 | 0.00 | 0.78 | 0.00 | 0.00 | 3.41 | 0.00 | 0.00 | 0.372 |
| rif_LDR06_ferite_e_caccia | 100 | 42.5% | 0.085 | 0.79 | 2.68 | 0.00 | 0.00 | 5.27 | 0.00 | 0.00 | 0.375 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 298 | 0.909 | 0.846 | 0.799 | 0.319 | 1123 | 0.832 | 0.218 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 298 | 0.181 | 0.161 | 0.141 | 0.037 | 1123 | 0.123 | 0.049 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 225 | 0.840 | 0.787 | 0.751 | 0.378 | 1011 | 0.767 | 0.230 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 225 | 0.293 | 0.236 | 0.191 | 0.089 | 1011 | 0.246 | 0.073 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 6.0% | 2.11 | 1.71 | 25.5% | 0.0% | 22.7% | 26.8% | 5.3% | 0.00 | 14.9% | 51.5% | 0.10 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 6.0% | 2.11 | 1.71 | 39.7% | 0.0% | 20.7% | 30.3% | 11.0% | 0.00 | 12.6% | 42.5% | 0.04 | 0.00 |
| Totale | 200 | 6.0% | 2.11 | 1.71 | 33.9% | 0.0% | 21.7% | 28.6% | 8.6% | 0.00 | 13.7% | 46.9% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.262 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.93 |
| rif_LDR06_ferite_e_caccia | 100 | 0.287 | 0.044 | 0.0% | 0.0% | 0.40 | 0.03 | 0.09 | 0.00 | 0.00 | 0.00 | 4.69 |

