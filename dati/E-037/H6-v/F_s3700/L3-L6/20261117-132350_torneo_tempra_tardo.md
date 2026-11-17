# Torneo v0.2 — /root/in37/dati/E-037-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in37/dati/E-037-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 642s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 35.0% [33.1–37.1] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 11.07) | 8–11 | ✅ |
| Partite al round 13+ | 27.0% [19.3–36.4] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=51) | 27.5% [17.1–40.9] | 20–35% | ✅ |
| Attacchi con opposizione | 27.5% [25.6–29.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 60.5% [58.5–62.6] (con ≥3: 24.6% [22.9–26.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.4% [37.4–41.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.8% [2.4–9.1] (n=168) / 80.9% [74.0–86.3] (n=157) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.6% [12.4–17.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 100.0% [56.6–100.0] (n=5), LDR-03 Risvegliato 100.0% [94.7–100.0] (n=69), LDR-06 Base 66.7% [20.8–93.9] (n=3), LDR-06 Risvegliato 69.0% [56.2–79.4] (n=58) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 26.9% [18.9–36.7] (n=93) | | |
| Attacchi per partita | 22.0 | | |
| Pugno attaccante vuoto / pieno | 57.4% [55.2–59.6] / 11.4% [10.1–12.9] (gemme medie 0.80) | non >90% | |
| Pugno difensore vuoto / pieno | 53.7% [50.7–56.7] / 25.4% [22.8–28.1] (gemme medie 0.28) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 605, 1: 905, 2: 487, 3: 146, 4: 47, 5: 12, 6: 1} | | |
| Azioni legali per decisione | 6.0 | <60 | ✅ |
| Fine partita | {'colpo_finale': 91, 'crepuscolo': 9} | | |
| G1 vince fra le partite finite al Crepuscolo | 88.9% [56.5–98.0] | | |
| G1 vince fra le partite arrivate al round 15 | 69.2% [42.4–87.3] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 23.1% [8.2–50.3] / 0.0% [0.0–56.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 66.7% [20.8–93.9]; 7.7% [1.4–33.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 3, '2-1': 2, '1-0': 2, '2-0': 1, '3-2': 1, '2-3': 1, '4-1': 1, '0-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=4) | 30.8% [12.7–57.6] / 0.0% [0.0–49.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 1, 15: 3}; 25.0% [4.6–69.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 75.0% [30.1–95.4] / 75.0% [30.1–95.4]; 3.75 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–49.0] / 75.0% [30.1–95.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=0) / a Vite diverse; nessuno attacca a Vite pari | nan% [nan–nan] / 75.0% [30.1–95.4]; nan% [nan–nan] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 0.0% [0.0–3.7] / 0.0% [0.0–22.8]; nan% [nan–nan] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=5) | 0.0% [0.0–43.4] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 61.5% [35.5–82.3] (0.0% [0.0–22.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 2, 'rif_LDR03_sanguinare_per_accendere': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR06_ferite_e_caccia 69% (n=13) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 53.0% [43.3–62.5], rif_LDR06_ferite_e_caccia 47.0% [37.5–56.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.371 / 0.096 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.096 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.18 (0.08), rif_LDR06_ferite_e_caccia 0.19 (0.10) | |
| M4 | Scontri decisi prima dell'impegno | 34.0% [32.1–36.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.36 (131 / 205); 61.4% [59.3–63.4] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 53.7% [52.2–55.1]; rif_LDR03_sanguinare_per_accendere 57.6%, rif_LDR06_ferite_e_caccia 48.9% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.316 (25) / 0.311 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 53 vittorie), LDR-06 G: 17.0 (49%, 47 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 2.78, VER-020 0.95, ROS-011 0.92, ROS-019 0.92, NER-017 0.91, NER-010 0.84, NER-001 0.80, NER-008 0.80, VER-008 0.72, NEU-001 0.67, NER-006 0.66, NER-013 0.66 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.39, rif_LDR06_ferite_e_caccia 2.27 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR06_ferite_e_caccia 0.17 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 36% (n=39), rif_LDR06_ferite_e_caccia 0% (n=12) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.4% [10.1–12.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.52, rif_LDR06_ferite_e_caccia 1.19; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | NER-009 100%, caccia 100%, ponte 100%, NER-017 100%, NER-010 53%, ROS-011 53%, VER-001 47%, collante 47%, NER-015 47%, NEW-B06 47%, VER-020 47%, NEU-012 47%; oltre il 60%: NER-009, NER-017 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 53.0 [43–62] (100) |
| rif_LDR06_ferite_e_caccia | 47.0 [38–57] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.47 | 0.00 | 0.00 / 0.00 | 2.67 | 0.00 | 4.4 (99) | 8 | K 63%, R 37% | 2.11 | 0.22 |
| rif_LDR06_ferite_e_caccia | 3.10 | 0.00 | 2.78 / 0.23 | 0.00 | 0.13 | 4.5 (99) | 10 | G 50%, K 50% | 2.32 | 1.24 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 1.54 | 1.24 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.00/0.11/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.67/0.56 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/1.09/0.50/0.23 | 0.88/1.11/0.24/0.03 | 0.00/0.00/0.00/0.00 | 0.06/0.00/0.00/0.00 | 0.34/0.12/0.18/0.12 | 0.00/0.27/0.00/0.00 | 0.00/0.16/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.05/0.02 | 0.00/0.00/0.00/0.00 | 0.33/0.13/0.14/0.09 | 0.60/0.92/0.36/0.20 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.00/0.09/0.03 | 0.85/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.48/0.04/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.28/0.29/0.13 | 0.00/0.25/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.78/1.58/0.41 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.51/0.23/0.06 | 0.42/0.21/0.02/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.09/0.39/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.27/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.23/0.01/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.72/0.02/0.30 | 0.32/0.02/0.03/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.67/0.08/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.22/0.28/0.03/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.00/0.08/0.02 | 0.25/0.33/0.09/0.04 | 0.41/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.70 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.51 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 1.05 | 0.00 | 0.01 | 0.10 | 0.13 | 0.21 | 0.19 | 0.09 | 0.10 | 0.10 | 0.03 | 0.04 | 0.02 | 0.02 | 0.01 | 1.52 | 0.30 | 0.30 | 0.26 | 0.11 | 0.13 | 0.13 | 0.09 | 0.09 | 0.04 | 0.02 | 0.05 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.63 | 0.00 | 0.01 | 0.05 | 0.09 | 0.10 | 0.08 | 0.08 | 0.10 | 0.05 | 0.03 | 0.02 | 0.01 | 0.00 | 0.01 | 1.19 | 0.11 | 0.19 | 0.20 | 0.14 | 0.09 | 0.20 | 0.07 | 0.07 | 0.05 | 0.02 | 0.03 | 0.02 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca | NER-002 stanca | NER-002 vita |
|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.62 | 0.23 |
| rif_LDR06_ferite_e_caccia | 0.79 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 4 | 0 | 4 |
| 8 | 8 | 4 | 0 | 12 |
| 9 | 2 | 6 | 0 | 8 |
| 10 | 8 | 13 | 0 | 21 |
| 11 | 4 | 16 | 0 | 20 |
| 12 | 4 | 4 | 0 | 8 |
| 13 | 2 | 5 | 0 | 7 |
| 14 | 0 | 7 | 0 | 7 |
| 15 | 8 | 4 | 0 | 12 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 57.6% | 0.104 | 0.76 | 0.63 | 0.00 | 0.00 | 2.80 | 0.00 | 0.00 | 0.435 |
| rif_LDR06_ferite_e_caccia | 100 | 48.9% | 0.088 | 0.89 | 1.38 | 0.00 | 0.00 | 2.83 | 0.00 | 0.00 | 0.314 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 249 | 0.924 | 0.908 | 0.892 | 0.361 | 790 | 0.863 | 0.268 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 249 | 0.277 | 0.261 | 0.253 | 0.072 | 790 | 0.229 | 0.065 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 240 | 0.796 | 0.725 | 0.654 | 0.350 | 924 | 0.725 | 0.166 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 240 | 0.233 | 0.200 | 0.167 | 0.079 | 924 | 0.188 | 0.039 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 9.0% | 2.11 | 1.76 | 41.2% | 0.0% | 18.7% | 31.2% | 12.8% | 0.00 | 10.0% | 57.6% | 0.02 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 9.0% | 2.11 | 1.76 | 24.2% | 0.0% | 22.7% | 33.3% | 9.5% | 0.00 | 14.7% | 48.9% | 0.01 | 0.00 |
| Totale | 200 | 9.0% | 2.11 | 1.76 | 32.8% | 0.0% | 20.7% | 32.3% | 11.1% | 0.00 | 12.1% | 53.7% | 0.01 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 0.265 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.09 |
| rif_LDR06_ferite_e_caccia | 100 | 0.284 | 0.050 | 0.0% | 0.0% | 0.42 | 0.04 | 0.08 | 0.05 | 0.00 | 0.00 | 3.59 |

