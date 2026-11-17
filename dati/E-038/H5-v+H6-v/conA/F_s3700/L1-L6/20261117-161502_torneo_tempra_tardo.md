# Torneo v0.2 — /home/claude/e038_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e038_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1836s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 30.8% [29.6–32.1] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [11.0–12.0] (media 11.42) | 8–11 | ✅ |
| Partite al round 13+ | 36.5% [30.1–43.4] | ≤12% | ❌ |
| Partite oltre il 15 | 0.5% [0.1–2.8] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=106) | 36.8% [28.2–46.3] | 20–35% | ❌ |
| Attacchi con opposizione | 26.8% [25.6–28.0] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 60.3% [58.9–61.8] (con ≥3: 20.5% [19.3–21.7]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.1% [35.8–38.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 8.5% [6.3–11.5] (n=445) / 85.4% [80.9–89.0] (n=294) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.8% [11.4–14.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 53.8% [35.5–71.2] (n=26), LDR-01 Risvegliato 74.2% [64.7–81.9] (n=97), LDR-06 Base 66.7% [39.1–86.2] (n=12), LDR-06 Risvegliato 72.7% [65.2–79.1] (n=154) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 40.5% [33.3–48.2] (n=163) | | |
| Attacchi per partita | 26.3 | | |
| Pugno attaccante vuoto / pieno | 51.7% [50.3–53.1] / 11.8% [10.9–12.8] (gemme medie 0.86) | non >90% | |
| Pugno difensore vuoto / pieno | 59.2% [57.2–61.1] / 24.5% [22.9–26.2] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1606, 1: 1789, 2: 1272, 3: 392, 4: 138, 5: 58, 6: 11} | | |
| Azioni legali per decisione | 5.7 | <60 | ✅ |
| Fine partita | {'colpo_finale': 187, 'crepuscolo': 13} | | |
| G1 vince fra le partite finite al Crepuscolo | 38.5% [17.7–64.5] | | |
| G1 vince fra le partite arrivate al round 15 | 31.6% [15.4–54.0] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 31.6% [15.4–54.0] / 66.7% [30.0–90.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [9.7–70.0]; 5.3% [0.9–24.6] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-0': 3, '2-3': 2, '1-0': 2, '1-2': 2, '2-1': 2, '3-1': 1, '3-5': 1, '2-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=7) | 36.8% [19.1–59.0] / 71.4% [35.9–91.8] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 6, 16: 1}; 71.4% [35.9–91.8] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 28.6% [8.2–64.1] / 14.3% [2.6–51.3]; 1.43 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–35.4] / 100.0% [64.6–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 50.0% [9.5–90.5]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.5% [1.1–5.7] / 26.3% [11.8–48.8]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 2, 'vinc:atk': 4, 'vinc:rim': 1} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=6) | 0.0% [0.0–43.4] / 0.0% [0.0–39.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 21.1% [8.5–43.3] (0.0% [0.0–16.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 4, 'rif_LDR06_ferite_e_caccia': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR06_ferite_e_caccia 32% (n=19) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 54.5% [47.6–61.3], rif_LDR06_ferite_e_caccia 45.5% [38.7–52.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.362 / 0.080 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.080 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.10 (0.00), rif_LDR06_ferite_e_caccia 0.20 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 33.2% [32.0–34.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.50 (309 / 790); 58.0% [56.7–59.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 46.2% [45.2–47.2]; rif_LDR01_puntata_e_preda 50.6%, rif_LDR06_ferite_e_caccia 42.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.356 (468) / 0.330 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 109 vittorie), LDR-06 G: 17.0 (49%, 91 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.82, VER-020 2.19, LDR-01 2.08, NER-017 1.93, ROS-016 1.44, ROS-018 1.03, NER-013 0.95, VER-008 0.82, VER-011 0.76, NEU-001 0.69, NER-009 0.62, VER-001 0.58 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.88, rif_LDR06_ferite_e_caccia 3.36 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR06_ferite_e_caccia 0.36 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 40% (n=40), rif_LDR06_ferite_e_caccia 35% (n=66) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.8% [10.9–12.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR06_ferite_e_caccia 1.30; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | caccia 100%, ponte 100%, VER-008 100%, VER-001 100%, ROS-016 55%, VER-011 55%, NEW-B06 46%, collante 46%, NEU-012 46%, NER-017 46%, NER-015 46%, NEU-001 46%; oltre il 60%: VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 54.5 [48–61] (200) |
| rif_LDR06_ferite_e_caccia | 45.5 [39–52] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.11 | 0.00 | 2.08 / 0.00 | 0.00 | 0.00 | 4.6 (200) | 13 | G 39%, R 61% | 2.63 | 0.46 |
| rif_LDR06_ferite_e_caccia | 3.56 | 0.00 | 3.82 / 0.34 | 0.00 | 0.16 | 4.6 (196) | 9 | G 51%, K 49% | 1.91 | 1.72 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR01_puntata_e_preda | 2.08 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.61 | 2.21 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/2.08/1.94/0.54 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.40/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.44/0.17/0.08 | 0.84/0.10/0.59/0.38 | 0.74/0.34/0.18/0.06 | 0.00/0.47/0.00/0.00 | 0.68/0.00/0.23/0.08 | 0.71/0.21/0.31/0.10 | 0.88/1.44/0.09/0.60 | 0.76/1.03/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.54/0.34/0.26 | 0.22/0.08/0.18/0.15 | 0.00/0.00/0.00/0.00 | 0.70/0.46/0.03/0.38 | 0.65/0.00/0.00/0.00 | 0.79/0.00/0.15/0.07 | 0.79/0.76/0.32/0.11 | 0.68/0.43/0.29/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.05/0.01 | 0.44/0.06/0.06/0.04 | 0.35/0.07/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.08/0.02 | 0.36/0.53/0.02/0.27 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.22/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.19/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.70/0.07/0.58 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.41/0.54/0.16 | 0.00/0.25/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.82/1.76/0.67 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.56/0.27/0.10 | 0.39/0.36/0.07/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.10/0.21/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.32/0.01/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.43/0.04/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/1.11/0.03/0.53 | 0.34/0.04/0.03/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.82/0.69/0.17/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.20/0.28/0.03/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.00/0.10/0.02 | 0.24/0.51/0.17/0.06 | 0.48/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.10 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.14 | 0.01 | 0.00 | 0.01 | 0.12 | 0.14 | 0.00 | 0.00 | 0.28 | 0.10 | 0.00 | 0.03 | 0.00 | 0.01 | 0.06 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.85 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.72 | 0.00 | 0.01 | 0.07 | 0.04 | 0.09 | 0.13 | 0.11 | 0.10 | 0.04 | 0.04 | 0.04 | 0.03 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.89 | 0.00 | 0.03 | 0.04 | 0.04 | 0.09 | 0.09 | 0.13 | 0.14 | 0.12 | 0.06 | 0.06 | 0.04 | 0.04 | 0.01 | 1.30 | 0.14 | 0.17 | 0.20 | 0.18 | 0.18 | 0.16 | 0.12 | 0.05 | 0.06 | 0.02 | 0.01 | 0.01 | 0.01 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR01_puntata_e_preda | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.74 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 3 | 1 | 0 | 4 |
| 8 | 9 | 8 | 0 | 17 |
| 9 | 9 | 11 | 0 | 20 |
| 10 | 21 | 12 | 0 | 33 |
| 11 | 15 | 14 | 0 | 29 |
| 12 | 11 | 13 | 0 | 24 |
| 13 | 25 | 14 | 0 | 39 |
| 14 | 4 | 11 | 0 | 15 |
| 15 | 6 | 12 | 0 | 18 |
| 16 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 50.6% | 0.078 | 0.00 | 0.88 | 0.00 | 0.00 | 3.40 | 0.00 | 0.00 | 0.359 |
| rif_LDR06_ferite_e_caccia | 200 | 42.1% | 0.082 | 0.81 | 2.54 | 0.00 | 0.00 | 5.04 | 0.00 | 0.00 | 0.365 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 583 | 0.887 | 0.827 | 0.789 | 0.338 | 2189 | 0.796 | 0.210 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 583 | 0.180 | 0.165 | 0.148 | 0.034 | 2189 | 0.127 | 0.042 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 448 | 0.855 | 0.790 | 0.737 | 0.371 | 2046 | 0.769 | 0.228 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 448 | 0.292 | 0.250 | 0.210 | 0.087 | 2046 | 0.240 | 0.078 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 6.5% | 2.04 | 1.69 | 29.7% | 0.0% | 21.7% | 25.7% | 4.3% | 0.00 | 14.9% | 50.6% | 0.12 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 6.5% | 2.04 | 1.69 | 33.1% | 0.0% | 21.2% | 29.7% | 11.4% | 0.00 | 12.8% | 42.1% | 0.04 | 0.00 |
| Totale | 400 | 6.5% | 2.04 | 1.69 | 31.7% | 0.0% | 21.4% | 27.7% | 8.3% | 0.00 | 13.8% | 46.2% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.254 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.11 |
| rif_LDR06_ferite_e_caccia | 200 | 0.283 | 0.042 | 0.0% | 0.0% | 0.41 | 0.05 | 0.07 | 0.00 | 0.00 | 0.00 | 4.67 |

