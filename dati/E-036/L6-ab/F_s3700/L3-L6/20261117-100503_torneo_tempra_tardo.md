# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1546s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 34.9% [33.5–36.4] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 10.89) | 8–11 | ✅ |
| Partite al round 13+ | 31.0% [25.0–37.7] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.3–3.6] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=70) | 38.6% [28.0–50.3] | 20–35% | ❌ |
| Attacchi con opposizione | 27.5% [26.2–28.9] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 59.6% [58.1–61.0] (con ≥3: 22.0% [20.8–23.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 38.2% [36.7–39.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.1% [3.9–9.3] (n=312) / 83.6% [79.4–87.0] (n=365) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 18.5% [16.7–20.5] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 45.5% [21.3–72.0] (n=11), LDR-03 Risvegliato 98.9% [96.0–99.7] (n=180), LDR-06 Base 37.5% [13.7–69.4] (n=8), LDR-06 Risvegliato 67.2% [58.6–74.8] (n=125) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 32.6% [26.3–39.7] (n=184) | | |
| Attacchi per partita | 21.6 | | |
| Pugno attaccante vuoto / pieno | 57.3% [55.7–58.9] / 11.1% [10.1–12.1] (gemme medie 0.80) | non >90% | |
| Pugno difensore vuoto / pieno | 56.9% [54.7–58.9] / 22.8% [21.1–24.7] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1273, 1: 1800, 2: 837, 3: 309, 4: 76, 5: 20, 6: 1} | | |
| Azioni legali per decisione | 5.8 | <60 | ✅ |
| Fine partita | {'colpo_finale': 184, 'crepuscolo': 16} | | |
| G1 vince fra le partite finite al Crepuscolo | 68.8% [44.4–85.8] | | |
| G1 vince fra le partite arrivate al round 15 | 60.0% [38.7–78.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 30.0% [14.5–51.9] / 33.3% [9.7–70.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [18.8–81.2]; 10.0% [2.8–30.1] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-1': 5, '1-0': 3, '2-2': 2, '3-5': 1, '4-2': 1, '2-3': 1, '3-2': 1, '0-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=7) | 35.0% [18.1–56.7] / 28.6% [8.2–64.1] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 1, 15: 6}; 42.9% [15.8–75.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 57.1% [25.0–84.2] / 57.1% [25.0–84.2]; 2.86 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–35.4] / 85.7% [48.7–97.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=2) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–65.8] / 80.0% [37.6–96.4]; 0.0% [0.0–65.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.0% [0.3–3.6] / 10.0% [2.8–30.1]; 100.0% [34.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:abil': 1, 'perd:pronto': 1, 'vinc:atk': 2} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=14) / turno di G2 (n=10) | 0.0% [0.0–21.5] / 0.0% [0.0–27.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=14) | 0.0% [0.0–21.5] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 60.0% [38.7–78.1] (5.0% [0.9–23.6]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR03_sanguinare_per_accendere': 6, 'rif_LDR06_ferite_e_caccia': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR06_ferite_e_caccia 60% (n=20) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 64.0% [57.1–70.3], rif_LDR06_ferite_e_caccia 36.0% [29.7–42.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.397 / 0.087 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.087 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.17 (0.04), rif_LDR06_ferite_e_caccia 0.15 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 33.9% [32.5–35.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.21 (240 / 403); 61.7% [60.2–63.1] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.2% [51.2–53.3]; rif_LDR03_sanguinare_per_accendere 54.1%, rif_LDR06_ferite_e_caccia 50.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.350 (48) / 0.331 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 128 vittorie), LDR-06 G: 17.0 (49%, 72 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 1.97, VER-020 1.04, NER-017 0.92, ROS-019 0.89, NER-008 0.81, ROS-011 0.78, NER-006 0.60, NER-010 0.58, NER-013 0.57, NEU-001 0.57, NER-001 0.56, VER-019 0.49 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.49, rif_LDR06_ferite_e_caccia 2.04 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR06_ferite_e_caccia 0.14 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 48% (n=46), rif_LDR06_ferite_e_caccia 21% (n=24) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.1% [10.1–12.1] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.52, rif_LDR06_ferite_e_caccia 0.79; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | caccia 100%, NER-017 100%, NER-009 100%, ponte 100%, NER-010 64%, ROS-011 64%, collante 36%, NER-015 36%, NEU-001 36%, VER-020 36%, NEW-B06 36%, VER-008 36%; oltre il 60%: NER-009, NER-017 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 64.0 [57–70] (200) |
| rif_LDR06_ferite_e_caccia | 36.0 [30–43] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.27 | 0.00 | 0.00 / 0.00 | 2.65 | 0.00 | 4.8 (199) | 10 | K 62%, R 38% | 2.21 | 0.40 |
| rif_LDR06_ferite_e_caccia | 3.56 | 0.00 | 1.97 / 0.04 | 0.00 | 0.11 | 4.7 (195) | 10 | G 53%, K 47% | 2.52 | 1.22 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.07/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.73/0.47 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.91/0.35/0.21 | 0.83/0.92/0.14/0.04 | 0.00/0.00/0.00/0.00 | 0.01/0.00/0.00/0.00 | 0.39/0.07/0.21/0.07 | 0.00/0.29/0.00/0.00 | 0.00/0.11/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.01/0.02 | 0.00/0.00/0.00/0.00 | 0.35/0.09/0.12/0.06 | 0.68/0.89/0.39/0.24 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.00/0.12/0.03 | 0.79/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.46/0.04/0.33 | 0.62/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.49/0.44/0.20 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.97/1.66/0.58 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.20/0.03/0.05 | 0.34/0.28/0.03/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.07/0.24/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.33/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.28/0.01/0.22 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.36/0.01/0.17 | 0.33/0.01/0.02/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.57/0.08/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.18/0.23/0.03/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.08/0.04 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.69 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.49 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 0.94 | 0.00 | 0.02 | 0.08 | 0.10 | 0.12 | 0.15 | 0.12 | 0.11 | 0.10 | 0.04 | 0.04 | 0.01 | 0.01 | 0.01 | 1.52 | 0.26 | 0.21 | 0.34 | 0.23 | 0.17 | 0.11 | 0.06 | 0.04 | 0.04 | 0.02 | 0.04 | 0.01 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.72 | 0.00 | 0.03 | 0.03 | 0.05 | 0.07 | 0.12 | 0.15 | 0.10 | 0.09 | 0.01 | 0.03 | 0.03 | 0.01 | 0.01 | 0.79 | 0.12 | 0.14 | 0.12 | 0.12 | 0.10 | 0.06 | 0.07 | 0.03 | 0.01 | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca | NER-002 stanca | NER-002 vita |
|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.60 | 0.18 |
| rif_LDR06_ferite_e_caccia | 0.37 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 1 | 0 | 0 | 1 |
| 6 | 2 | 3 | 0 | 5 |
| 7 | 3 | 7 | 0 | 10 |
| 8 | 16 | 11 | 0 | 27 |
| 9 | 14 | 8 | 0 | 22 |
| 10 | 15 | 18 | 0 | 33 |
| 11 | 13 | 6 | 0 | 19 |
| 12 | 11 | 10 | 0 | 21 |
| 13 | 10 | 11 | 0 | 21 |
| 14 | 7 | 14 | 0 | 21 |
| 15 | 11 | 7 | 0 | 18 |
| 16 | 1 | 1 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 54.1% | 0.096 | 0.81 | 0.68 | 0.00 | 0.00 | 2.83 | 0.00 | 0.00 | 0.472 |
| rif_LDR06_ferite_e_caccia | 200 | 50.0% | 0.079 | 0.83 | 1.20 | 0.00 | 0.00 | 2.97 | 0.00 | 0.00 | 0.331 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 467 | 0.927 | 0.919 | 0.910 | 0.340 | 1537 | 0.856 | 0.316 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 467 | 0.278 | 0.266 | 0.255 | 0.073 | 1537 | 0.224 | 0.078 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 449 | 0.846 | 0.793 | 0.728 | 0.339 | 1863 | 0.781 | 0.191 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 449 | 0.263 | 0.229 | 0.205 | 0.069 | 1863 | 0.167 | 0.049 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 8.0% | 2.17 | 1.80 | 49.1% | 0.5% | 23.0% | 30.6% | 9.2% | 0.00 | 11.2% | 54.1% | 0.04 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 8.0% | 2.17 | 1.80 | 24.7% | 0.5% | 23.3% | 32.0% | 5.3% | 0.00 | 14.4% | 50.0% | 0.01 | 0.00 |
| Totale | 400 | 8.0% | 2.17 | 1.80 | 34.7% | 0.5% | 23.2% | 31.3% | 7.2% | 0.00 | 12.7% | 52.2% | 0.03 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 0.273 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.04 |
| rif_LDR06_ferite_e_caccia | 200 | 0.277 | 0.048 | 0.0% | 0.0% | 0.41 | 0.04 | 0.06 | 0.07 | 0.00 | 0.00 | 3.21 |

