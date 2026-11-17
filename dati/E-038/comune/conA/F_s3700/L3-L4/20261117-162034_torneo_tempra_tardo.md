# Torneo v0.2 — /root/in38/dati/E-038-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in38/dati/E-038-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1512s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 38.9% [37.6–40.3] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [11.0–12.0] (media 11.40) | 8–11 | ✅ |
| Partite al round 13+ | 37.0% [30.6–43.9] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–1.9] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=84) | 38.1% [28.4–48.8] | 20–35% | ❌ |
| Attacchi con opposizione | 30.0% [28.7–31.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 63.6% [62.2–65.0] (con ≥3: 24.2% [23.0–25.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.9% [35.5–38.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 8.0% [5.6–11.2] (n=363) / 74.6% [69.8–78.8] (n=354) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.9% [13.3–16.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 75.0% [40.9–92.9] (n=8), LDR-03 Risvegliato 98.9% [96.1–99.7] (n=181), LDR-04 Base 47.6% [28.3–67.6] (n=21), LDR-04 Risvegliato 80.7% [71.0–87.8] (n=83) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 37.6% [30.9–44.9] (n=178) | | |
| Attacchi per partita | 24.1 | | |
| Pugno attaccante vuoto / pieno | 55.9% [54.4–57.4] / 10.9% [10.0–11.9] (gemme medie 0.83) | non >90% | |
| Pugno difensore vuoto / pieno | 69.1% [67.3–70.9] / 15.2% [13.8–16.6] (gemme medie 0.22) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1432, 1: 1963, 2: 937, 3: 338, 4: 118, 5: 24, 6: 2} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 181, 'crepuscolo': 19} | | |
| G1 vince fra le partite finite al Crepuscolo | 57.9% [36.3–76.9] | | |
| G1 vince fra le partite arrivate al round 15 | 57.7% [38.9–74.5] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 46.2% [28.8–64.5] / 41.7% [19.3–68.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [25.4–74.6]; 0.0% [0.0–12.9] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 6, '2-2': 4, '0-0': 3, '3-0': 2, '1-1': 2, '2-1': 2, '3-2': 2, '3-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=12) | 46.2% [28.8–64.5] / 41.7% [19.3–68.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 12}; 50.0% [25.4–74.6] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 75.0% [46.8–91.1] / 41.7% [19.3–68.0]; 2.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–24.3] / 83.3% [55.2–95.3] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 71.4% [35.9–91.8]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.5% [1.1–5.7] / 19.2% [8.5–37.9]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 2, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=16) / turno di G2 (n=9) | 0.0% [0.0–19.4] / 0.0% [0.0–29.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=16) | 0.0% [0.0–19.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 57.7% [38.9–74.5] (15.4% [6.1–33.5]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 8, 'rif_LDR03_sanguinare_per_accendere': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR04_stanca_e_smonta 58% (n=26) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 51.0% [44.1–57.8], rif_LDR04_stanca_e_smonta 49.0% [42.2–55.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.561 / 0.072 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.072 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.13 (0.04), rif_LDR04_stanca_e_smonta 0.10 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 34.1% [32.8–35.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.42 (180 / 305); 63.1% [61.8–64.5] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.8% [51.8–53.8]; rif_LDR03_sanguinare_per_accendere 53.3%, rif_LDR04_stanca_e_smonta 52.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.405 (32) / 0.328 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 102 vittorie), LDR-04 B: 12.0 (36%, 98 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 5.07, NER-017 2.06, ROS-019 1.50, BLU-015 1.15, NER-001 0.97, ROS-011 0.74, NER-006 0.73, NER-008 0.73, VER-008 0.70, NER-013 0.69, VER-014 0.59, NER-010 0.59 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.66, rif_LDR04_stanca_e_smonta 2.08 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR04_stanca_e_smonta 0.17 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 39% (n=71), rif_LDR04_stanca_e_smonta 31% (n=13) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.9% [10.0–11.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.51, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | caccia 100%, ponte 100%, NER-010 51%, NER-017 51%, NER-009 51%, ROS-011 51%, BLU-010 49%, VER-008 49%, VER-023 49%, VER-001 49%, VER-014 49%, collante 49%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 51.0 [44–58] (200) |
| rif_LDR04_stanca_e_smonta | 49.0 [42–56] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.43 | 0.00 | 0.00 / 0.00 | 2.50 | 0.00 | 4.8 (197) | 8 | K 61%, R 39% | 2.23 | 0.45 |
| rif_LDR04_stanca_e_smonta | 4.93 | 1.98 | 5.07 / 0.00 | 0.00 | 0.60 | 4.8 (197) | 10 | B 40%, G 60% | 2.40 | 0.56 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 1.98 | 3.08 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.10/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.89/0.61 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.97/0.46/0.23 | 0.77/0.73/0.14/0.02 | 0.00/0.00/0.00/0.00 | 0.04/0.00/0.00/0.00 | 0.37/0.12/0.28/0.12 | 0.00/0.24/0.00/0.00 | 0.00/0.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.37/0.09/0.19/0.07 | 0.76/1.50/0.58/0.51 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.07/0.03 | 0.83/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.45/0.10/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.18/0.26/0.14 | 0.33/0.00/0.08/0.04 | 0.80/1.15/0.39/0.33 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.38/0.04/0.29 | 0.73/0.00/0.00/0.00 | 0.69/0.00/0.10/0.02 | 0.00/0.00/0.00/0.00 | 0.34/0.37/0.24/0.19 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/5.07/1.70/0.36 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.25/0.38/0.04/0.18 | 0.00/0.00/0.00/0.00 | 0.39/0.28/0.04/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.07/0.14/0.06 | 0.29/0.00/0.02/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.70/0.01/0.28 | 0.33/0.01/0.01/0.01 | 0.32/0.00/0.10/0.04 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.53/0.00/0.00 | 0.00/0.04/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.89 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.56 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.03 | 0.01 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 1.03 | 0.00 | 0.01 | 0.05 | 0.07 | 0.15 | 0.17 | 0.12 | 0.12 | 0.09 | 0.06 | 0.08 | 0.04 | 0.03 | 0.03 | 1.51 | 0.27 | 0.27 | 0.24 | 0.14 | 0.17 | 0.14 | 0.10 | 0.09 | 0.06 | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 0.82 | 0.00 | 0.01 | 0.02 | 0.04 | 0.09 | 0.17 | 0.18 | 0.13 | 0.07 | 0.05 | 0.03 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | NER-002 stanca | NER-002 vita |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.56 | 0.28 |
| rif_LDR04_stanca_e_smonta | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 1 | 0 | 0 | 1 |
| 7 | 1 | 4 | 0 | 5 |
| 8 | 3 | 13 | 0 | 16 |
| 9 | 12 | 22 | 0 | 34 |
| 10 | 10 | 12 | 0 | 22 |
| 11 | 18 | 8 | 0 | 26 |
| 12 | 9 | 12 | 0 | 21 |
| 13 | 8 | 11 | 0 | 19 |
| 14 | 13 | 16 | 0 | 29 |
| 15 | 15 | 11 | 0 | 26 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 53.3% | 0.081 | 0.88 | 0.79 | 0.00 | 0.00 | 3.71 | 0.00 | 0.00 | 0.524 |
| rif_LDR04_stanca_e_smonta | 200 | 52.3% | 0.065 | 1.58 | 0.50 | 0.00 | 0.00 | 2.12 | 0.00 | 0.00 | 0.454 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 497 | 0.928 | 0.915 | 0.907 | 0.314 | 1739 | 0.866 | 0.377 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 497 | 0.294 | 0.276 | 0.249 | 0.052 | 1739 | 0.256 | 0.121 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 301 | 0.860 | 0.801 | 0.748 | 0.159 | 2277 | 0.783 | 0.372 | 0.155 | 0.044 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 301 | 0.176 | 0.146 | 0.103 | 0.047 | 2277 | 0.150 | 0.068 | 0.031 | 0.002 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 9.5% | 2.11 | 2.08 | 29.9% | 0.5% | 25.7% | 31.1% | 9.4% | 0.00 | 9.9% | 53.3% | 0.07 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 9.5% | 2.11 | 2.08 | 31.2% | 0.5% | 22.5% | 28.9% | 7.2% | 0.00 | 18.5% | 52.3% | 0.01 | 0.00 |
| Totale | 400 | 9.5% | 2.11 | 2.08 | 30.6% | 0.5% | 24.1% | 30.0% | 8.3% | 0.00 | 13.9% | 52.8% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 0.243 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.47 |
| rif_LDR04_stanca_e_smonta | 200 | 0.349 | 0.145 | 0.0% | 0.0% | 0.86 | 0.26 | 0.37 | 0.54 | 0.00 | 0.00 | 3.40 |

