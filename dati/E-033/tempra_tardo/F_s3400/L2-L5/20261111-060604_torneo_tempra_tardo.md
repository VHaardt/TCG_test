# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 1375s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 43.2% [41.3–45.1] | 30–45% | ✅ |
| Durata mediana (round) | 13.0 [12.0–13.0] (media 12.56) | 8–11 | ❌ |
| Partite al round 13+ | 57.0% [47.2–66.3] | ≤12% | ❌ |
| Partite oltre il 15 | 3.0% [1.0–8.5] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=27) | 25.9% [13.2–44.7] | 20–35% | ✅ |
| Attacchi con opposizione | 37.1% [35.3–39.0] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 64.4% [62.5–66.3] (con ≥3: 27.1% [25.4–28.9]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.2% [34.3–38.0] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 15.1% [10.9–20.7] (n=205) / 90.6% [84.2–94.5] (n=127) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.2% [10.2–14.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 55.6% [26.7–81.1] (n=9), LDR-02 Risvegliato 92.6% [83.9–96.8] (n=68), LDR-05 Base 68.2% [47.3–83.6] (n=22), LDR-05 Risvegliato 72.3% [58.2–83.1] (n=47) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 64.7% [54.1–74.0] (n=85) | | |
| Attacchi per partita | 26.1 | | |
| Pugno attaccante vuoto / pieno | 52.3% [50.3–54.2] / 9.6% [8.5–10.8] (gemme medie 0.95) | non >90% | |
| Pugno difensore vuoto / pieno | 50.0% [47.4–52.7] / 26.1% [23.9–28.5] (gemme medie 0.36) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 940, 1: 824, 2: 554, 3: 190, 4: 82, 5: 19, 6: 3, 7: 2} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 89, 'crepuscolo': 11} | | |
| G1 vince fra le partite finite al Crepuscolo | 54.5% [28.0–78.7] | | |
| G1 vince fra le partite arrivate al round 15 | 50.0% [32.1–67.9] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 23.1% [11.0–42.1] / 66.7% [30.0–90.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [9.7–70.0]; 11.5% [4.0–29.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-3': 4, '2-2': 4, '3-2': 4, '3-3': 3, '1-1': 2, '1-0': 2, '0-0': 2, '2-0': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=7) | 26.9% [13.7–46.1] / 57.1% [25.0–84.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 6, 16: 1}; 57.1% [25.0–84.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 57.1% [25.0–84.2] / 28.6% [8.2–64.1]; 2.29 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–35.4] / 100.0% [64.6–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=4) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–49.0] / 66.7% [20.8–93.9]; 0.0% [0.0–49.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.0% [1.6–9.8] / 15.4% [6.1–33.5]; 100.0% [51.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 1, 'vinc:atk': 4} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=12) / turno di G2 (n=8) | 0.0% [0.0–24.3] / 0.0% [0.0–32.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=12) | 0.0% [0.0–24.3] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 30.8% [16.5–50.0] (7.7% [2.1–24.1]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 4, 'rif_LDR05_scudi_armati': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 50% (n=26) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 27.0% [19.3–36.4], rif_LDR05_scudi_armati 73.0% [63.6–80.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.510 / 0.089 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.083 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.19 (0.00), rif_LDR05_scudi_armati 0.20 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 23.6% [22.1–25.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 62.9% [61.0–64.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.4% [51.1–53.8]; rif_LDR02_muro_di_parata 49.3%, rif_LDR05_scudi_armati 54.7% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.1% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.323 (247) / 0.341 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 27 vittorie), LDR-05 R: 18.0 (49%, 73 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.85, LDR-02 1.44, BLU-015 0.86, BLU-001 0.73, ROS-020 0.67, ROS-018 0.64, NEU-013 0.49, BLU-008 0.45, ROS-021 0.44, ROS-007 0.38, ROS-019 0.32, BLU-023 0.32 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.62, rif_LDR05_scudi_armati 0.11 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 15% (n=20), rif_LDR05_scudi_armati 57% (n=7) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.6% [8.5–10.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | BLU-021 100%, ponte 100%, collante 100%, NEU-009 100%, BLU-008 73%, NEU-013 73%, ROS-020 73%, BLU-010 73%, RS 27%, NEU-015 27%, NEU-003 27%, 11.1 27%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 27.0 [19–36] (100) |
| rif_LDR05_scudi_armati | 73.0 [64–81] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.67 | 0.00 | 1.44 / 0.00 | 0.00 | 1.25 | 5.1 (99) | 8 | B 78%, K 22% | 2.38 | 0.00 |
| rif_LDR05_scudi_armati | 4.46 | 0.00 | 3.85 / 0.00 | 0.00 | 0.81 | 4.0 (100) | 13 | B 48%, R 52% | 2.11 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.93/0.39/0.24 | 0.93/0.00/0.24/0.19 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.00/0.29/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.25/0.00/0.00 | 0.00/0.16/0.00/0.00 | 0.00/0.41/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.44/1.61/1.19 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.02/0.00/0.00 | 0.00/0.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.36/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.10/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.08/0.12/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.85/1.71/0.31 | 0.73/0.54/0.14/0.04 | 0.72/0.00/0.27/0.07 | 0.68/0.45/0.28/0.07 | 0.63/0.14/0.29/0.08 | 0.78/0.00/0.21/0.09 | 0.69/0.86/0.25/0.22 | 0.00/0.34/0.00/0.00 | 0.00/0.47/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.75/0.49/0.36/0.19 | 0.78/0.31/0.08/0.05 | 0.00/0.00/0.00/0.00 | 0.79/0.30/0.20/0.02 | 0.00/0.38/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.21/0.28/0.08 | 0.00/0.00/0.00/0.00 | 0.36/0.64/0.00/0.00 | 0.83/0.67/0.51/0.22 | 0.41/0.44/0.27/0.08 | 0.24/0.14/0.24/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.00/0.06/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.15/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.01/0.01 | 0.33/0.02/0.00/0.00 | 0.24/0.12/0.06/0.05 | 0.38/0.32/0.06/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.36 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.26 | 0.00 | 0.10 | 0.00 | 0.03 | 0.02 | 0.02 | 0.04 | 0.17 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.28 | 0.25 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 1.30 | 0.01 | 0.08 | 0.06 | 0.24 | 0.20 | 0.20 | 0.17 | 0.12 | 0.02 | 0.05 | 0.07 | 0.06 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.71 | 0.03 | 0.05 | 0.04 | 0.03 | 0.15 | 0.09 | 0.09 | 0.09 | 0.05 | 0.01 | 0.04 | 0.02 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 2 | 0 | 2 |
| 8 | 2 | 0 | 0 | 2 |
| 9 | 4 | 1 | 0 | 5 |
| 10 | 5 | 5 | 0 | 10 |
| 11 | 9 | 5 | 0 | 14 |
| 12 | 4 | 6 | 0 | 10 |
| 13 | 9 | 11 | 0 | 20 |
| 14 | 3 | 8 | 0 | 11 |
| 15 | 10 | 13 | 0 | 23 |
| 16 | 3 | 0 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 49.3% | 0.071 | 1.62 | 0.00 | 0.00 | 0.00 | 3.63 | 0.00 | 0.00 | 0.580 |
| rif_LDR05_scudi_armati | 100 | 54.7% | 0.110 | 0.11 | 0.00 | 0.00 | 0.00 | 1.78 | 0.00 | 0.00 | 0.426 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 403 | 1.000 | 0.998 | 0.998 | 0.201 | 1015 | 1.000 | 0.414 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 403 | 0.536 | 0.514 | 0.471 | 0.047 | 1015 | 0.428 | 0.183 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 296 | 0.905 | 0.885 | 0.875 | 0.378 | 900 | 0.863 | 0.261 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 296 | 0.193 | 0.189 | 0.186 | 0.068 | 900 | 0.126 | 0.043 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 11.0% | 2.84 | 1.52 | 15.2% | 0.0% | 33.0% | 41.7% | 16.4% | 0.00 | 17.5% | 49.3% | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 11.0% | 2.84 | 1.52 | 56.8% | 0.0% | 17.0% | 33.3% | 13.3% | 0.00 | 17.3% | 54.7% | 0.14 | 0.00 |
| Totale | 200 | 11.0% | 2.84 | 1.52 | 31.8% | 0.0% | 25.0% | 37.4% | 15.2% | 0.00 | 17.4% | 52.4% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

