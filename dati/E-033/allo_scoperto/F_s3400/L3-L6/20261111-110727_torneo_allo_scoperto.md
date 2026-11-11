# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 605s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 33.3% [31.3–35.4] | 30–45% | ✅ |
| Durata mediana (round) | 10.0 [9.0–11.0] (media 10.48) | 8–11 | ✅ |
| Partite al round 13+ | 30.0% [21.9–39.6] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=36) | 27.8% [15.8–44.0] | 20–35% | ✅ |
| Attacchi con opposizione | 25.6% [23.8–27.5] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 57.3% [55.1–59.4] (con ≥3: 18.6% [16.9–20.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 40.4% [38.3–42.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 3.2% [1.4–7.3] (n=155) / 85.0% [79.7–89.1] (n=220) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 22.5% [19.8–25.5] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 80.0% [37.6–96.4] (n=5), LDR-03 Risvegliato 98.2% [93.6–99.5] (n=110), LDR-06 Risvegliato 67.5% [56.5–76.9] (n=77) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 30.5% [22.2–40.4] (n=95) | | |
| Attacchi per partita | 20.6 | | |
| Pugno attaccante vuoto / pieno | 55.4% [53.1–57.7] / 12.4% [11.0–14.0] (gemme medie 0.87) | non >90% | |
| Pugno difensore vuoto / pieno | 52.4% [49.3–55.6] / 27.4% [24.7–30.3] (gemme medie 0.29) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 599, 1: 840, 2: 412, 3: 144, 4: 51, 5: 7, 6: 2} | | |
| Azioni legali per decisione | 5.7 | <60 | ✅ |
| Fine partita | {'colpo_finale': 93, 'crepuscolo': 7} | | |
| G1 vince fra le partite finite al Crepuscolo | 14.3% [2.6–51.3] | | |
| G1 vince fra le partite arrivate al round 15 | 33.3% [13.8–60.9] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 41.7% [19.3–68.0] / 60.0% [23.1–88.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 20.0% [3.6–62.4]; 0.0% [0.0–24.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 2, '1-1': 2, '1-2': 2, '2-3': 2, '0-1': 1, '1-0': 1, '0-0': 1, '3-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=5) | 41.7% [19.3–68.0] / 60.0% [23.1–88.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 5}; 80.0% [37.6–96.4] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 60.0% [23.1–88.2] / 20.0% [3.6–62.4]; 1.60 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–43.4] / 100.0% [56.6–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 50.0% [9.5–90.5]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.0–8.5] / 25.0% [8.9–53.2]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'perd:pronto': 2, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=6) / turno di G2 (n=3) | 0.0% [0.0–39.0] / 0.0% [0.0–56.2] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=6) | 0.0% [0.0–39.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 25.0% [8.9–53.2] (16.7% [4.7–44.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR03_sanguinare_per_accendere': 3, 'rif_LDR06_ferite_e_caccia': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR06_ferite_e_caccia 33% (n=12) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 59.0% [49.2–68.1], rif_LDR06_ferite_e_caccia 41.0% [31.9–50.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.427 / 0.096 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.096 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.15 (0.08), rif_LDR06_ferite_e_caccia 0.08 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 34.5% [32.5–36.6] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.09 (86 / 223); 62.5% [60.4–64.6] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.5% [49.9–53.1]; rif_LDR03_sanguinare_per_accendere 52.8%, rif_LDR06_ferite_e_caccia 49.9% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.7] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.300 (18) / 0.334 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 59 vittorie), LDR-06 G: 17.0 (49%, 41 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 1.77, VER-020 1.09, NER-006 0.90, VER-008 0.89, NER-008 0.79, ROS-019 0.73, NER-017 0.72, ROS-011 0.68, NER-001 0.59, NEU-001 0.57, NER-013 0.56, NER-010 0.50 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.30, rif_LDR06_ferite_e_caccia 2.06 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR06_ferite_e_caccia 0.21 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 33% (n=21), rif_LDR06_ferite_e_caccia 20% (n=15) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.4% [11.0–14.0] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.61, rif_LDR06_ferite_e_caccia 0.83; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | NER-009 100%, ponte 100%, caccia 100%, NER-017 100%, ROS-011 59%, NER-010 59%, NER-015 41%, collante 41%, VER-001 41%, VER-023 41%, NEU-012 41%, NEU-001 41%; oltre il 60%: NER-009, NER-017 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 59.0 [49–68] (100) |
| rif_LDR06_ferite_e_caccia | 41.0 [32–51] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.32 | 0.00 | 0.00 / 0.00 | 2.08 | 0.00 | 4.5 (100) | 8 | K 60%, R 40% | 2.13 | 0.43 |
| rif_LDR06_ferite_e_caccia | 3.42 | 0.00 | 1.77 / 0.02 | 0.00 | 0.13 | 5.1 (96) | 8 | G 54%, K 46% | 2.59 | 1.19 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.04/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/2.02/0.40 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.93/0.47/0.18 | 0.71/0.90/0.13/0.02 | 0.00/0.00/0.00/0.00 | 0.01/0.00/0.00/0.00 | 0.37/0.07/0.19/0.07 | 0.00/0.26/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.00/0.01 | 0.00/0.00/0.00/0.00 | 0.35/0.09/0.18/0.06 | 0.69/0.73/0.33/0.22 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.00/0.09/0.05 | 0.28/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.29/0.02/0.25 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.34/0.27/0.19 | 0.00/0.34/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.77/1.73/0.56 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.00/0.00 | 0.21/0.27/0.00/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.26/0.07/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.11/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.27/0.08/0.13/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.11/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.31/0.01/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.21/0.00/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.89/0.01/0.44 | 0.27/0.02/0.03/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.57/0.07/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.51 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.52 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 1.11 | 0.00 | 0.02 | 0.07 | 0.14 | 0.18 | 0.14 | 0.11 | 0.11 | 0.09 | 0.08 | 0.06 | 0.06 | 0.02 | 0.03 | 1.61 | 0.28 | 0.29 | 0.34 | 0.15 | 0.20 | 0.12 | 0.12 | 0.04 | 0.03 | 0.00 | 0.01 | 0.03 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.77 | 0.00 | 0.02 | 0.06 | 0.03 | 0.13 | 0.11 | 0.10 | 0.11 | 0.08 | 0.07 | 0.03 | 0.00 | 0.03 | 0.00 | 0.83 | 0.11 | 0.13 | 0.14 | 0.10 | 0.06 | 0.07 | 0.06 | 0.09 | 0.02 | 0.03 | 0.00 | 0.01 | 0.00 | 0.01 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 3 | 3 | 0 | 6 |
| 7 | 3 | 6 | 0 | 9 |
| 8 | 7 | 5 | 0 | 12 |
| 9 | 8 | 8 | 0 | 16 |
| 10 | 3 | 10 | 0 | 13 |
| 11 | 5 | 3 | 0 | 8 |
| 12 | 4 | 1 | 0 | 5 |
| 13 | 4 | 2 | 0 | 6 |
| 14 | 6 | 6 | 0 | 12 |
| 15 | 4 | 8 | 0 | 12 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 52.8% | 0.107 | 0.67 | 0.63 | 0.00 | 0.00 | 2.38 | 0.00 | 0.00 | 0.467 |
| rif_LDR06_ferite_e_caccia | 100 | 49.9% | 0.087 | 0.81 | 1.25 | 0.00 | 0.00 | 3.01 | 0.00 | 0.00 | 0.390 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 250 | 0.908 | 0.900 | 0.892 | 0.356 | 719 | 0.834 | 0.291 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 250 | 0.244 | 0.232 | 0.224 | 0.060 | 719 | 0.193 | 0.082 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 216 | 0.944 | 0.903 | 0.894 | 0.398 | 870 | 0.867 | 0.232 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 216 | 0.269 | 0.222 | 0.194 | 0.037 | 870 | 0.261 | 0.076 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 7.0% | 1.82 | 1.44 | 40.4% | 1.0% | 23.3% | 31.9% | 7.7% | 0.00 | 12.9% | 52.8% | 0.02 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 7.0% | 1.82 | 1.44 | 34.9% | 1.0% | 25.7% | 33.8% | 6.2% | 0.00 | 12.9% | 49.9% | 0.03 | 0.00 |
| Totale | 200 | 7.0% | 1.82 | 1.44 | 36.9% | 1.0% | 24.5% | 32.9% | 6.9% | 0.00 | 12.9% | 51.5% | 0.03 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

