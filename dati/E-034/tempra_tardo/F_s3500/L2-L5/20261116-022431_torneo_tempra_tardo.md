# Torneo v0.2 — /home/claude/e034_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e034_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2841s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 40.6% [39.2–41.9] | 30–45% | ✅ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 12.92) | 8–11 | ❌ |
| Partite al round 13+ | 61.5% [54.6–68.0] | ≤12% | ❌ |
| Partite oltre il 15 | 10.0% [6.6–14.9] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=59) | 18.6% [10.7–30.4] | 20–35% | ❌ |
| Attacchi con opposizione | 44.7% [43.3–46.1] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 72.5% [71.2–73.7] (con ≥3: 36.8% [35.4–38.1]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 33.9% [32.6–35.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 16.1% [12.9–19.9] (n=416) / 89.0% [83.8–92.7] (n=191) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 9.9% [8.6–11.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 46.9% [30.9–63.6] (n=32), LDR-02 Risvegliato 72.7% [62.6–80.9] (n=88), LDR-05 Base 42.9% [28.0–59.1] (n=35), LDR-05 Risvegliato 78.0% [67.9–85.6] (n=82) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 65.8% [58.2–72.7] (n=161) | | |
| Attacchi per partita | 25.3 | | |
| Pugno attaccante vuoto / pieno | 51.3% [49.8–52.7] / 11.2% [10.4–12.1] (gemme medie 0.96) | non >90% | |
| Pugno difensore vuoto / pieno | 51.7% [49.7–53.7] / 25.7% [24.0–27.5] (gemme medie 0.31) | non >90% | |
| Reazioni per scontro | 0.11 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1734, 1: 1695, 2: 997, 3: 428, 4: 131, 5: 57, 6: 11} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 154, 'crepuscolo': 46} | | |
| G1 vince fra le partite finite al Crepuscolo | 67.4% [53.0–79.1] | | |
| G1 vince fra le partite arrivate al round 15 | 48.8% [38.1–59.5] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 13.8% [7.9–23.0] / 45.5% [21.3–72.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 45.5% [21.3–72.0]; 25.0% [16.8–35.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-3': 8, '2-2': 7, '3-3': 6, '1-0': 5, '3-2': 5, '4-4': 5, '2-0': 4, '3-4': 4} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=19) | 23.8% [15.8–34.1] / 31.6% [15.4–54.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 11, 17: 1, 16: 7}; 36.8% [19.1–59.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 73.7% [51.2–88.2] / 47.4% [27.3–68.3]; 2.79 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–16.8] / 94.7% [75.4–99.1] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=6) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–39.0] / 69.2% [42.4–87.3]; 0.0% [0.0–39.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.4–6.4] / 7.5% [3.5–15.4]; 100.0% [61.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 1, 'perd:rim': 1, 'vinc:atk': 6} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=26) / turno di G2 (n=29) | 0.0% [0.0–12.9] / 0.0% [0.0–11.7] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=26) | 0.0% [0.0–12.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 43.8% [33.4–54.7] (11.2% [6.0–20.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 11, 'rif_LDR05_scudi_armati': 8} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 49% (n=80) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 42.0% [35.4–48.9], rif_LDR05_scudi_armati 58.0% [51.1–64.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.532 / 0.110 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.106 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.12 (0.00), rif_LDR05_scudi_armati 0.14 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 26.1% [24.9–27.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 55.3% [53.9–56.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 57.9% [57.1–58.8]; rif_LDR02_muro_di_parata 57.1%, rif_LDR05_scudi_armati 58.7% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.2% [0.1–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.302 (466) / 0.323 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 84 vittorie), LDR-05 R: 18.0 (49%, 116 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.40, LDR-02 1.45, BLU-015 1.02, ROS-018 0.72, BLU-005 0.71, BLU-001 0.68, NEW-I04 0.67, BLU-008 0.57, ROS-020 0.50, ROS-021 0.47, ROS-001 0.46, NEU-004 0.43 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.48, rif_LDR05_scudi_armati 0.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 12% (n=40), rif_LDR05_scudi_armati 32% (n=19) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.2% [10.4–12.1] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, NEU-009 100%, ponte 100%, BLU-021 100%, BLU-008 58%, NEU-013 58%, ROS-020 58%, BLU-010 58%, NER-014 42%, NEU-015 42%, NEU-003 42%, RS 42%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 42.0 [35–49] (200) |
| rif_LDR05_scudi_armati | 58.0 [51–65] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.27 | 0.00 | 1.45 / 0.00 | 0.00 | 1.29 | 4.9 (194) | 8 | B 83%, K 17% | 1.85 | 0.00 |
| rif_LDR05_scudi_armati | 4.19 | 0.00 | 3.40 / 0.00 | 0.00 | 0.84 | 4.3 (198) | 13 | B 48%, R 52% | 1.89 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.88/0.25/0.16 | 0.73/0.00/0.14/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.00/0.36/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.45/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.28/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.45/1.50/1.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.99/0.00/0.12/0.07 | 0.96/0.71/0.10/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.37/0.00/0.00/0.00 | 0.45/0.43/0.06/0.03 | 0.38/0.00/0.11/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.10/0.12/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.67/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.40/1.54/0.54 | 0.64/0.48/0.14/0.04 | 0.69/0.00/0.20/0.14 | 0.70/0.57/0.28/0.14 | 0.64/0.20/0.23/0.12 | 0.61/0.00/0.12/0.09 | 0.84/1.02/0.29/0.30 | 0.00/0.40/0.00/0.00 | 0.00/0.41/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.28/0.16/0.13 | 0.69/0.46/0.17/0.09 | 0.00/0.00/0.00/0.00 | 0.67/0.35/0.12/0.07 | 0.00/0.30/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.23/0.20/0.15 | 0.00/0.00/0.00/0.00 | 0.38/0.72/0.00/0.00 | 0.68/0.50/0.39/0.36 | 0.47/0.47/0.19/0.32 | 0.21/0.09/0.12/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.00/0.04/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.12/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.03/0.01 | 0.40/0.07/0.03/0.04 | 0.30/0.10/0.10/0.06 | 0.40/0.36/0.12/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.50 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.07 | 0.00 | 0.07 | 0.01 | 0.00 | 0.03 | 0.01 | 0.02 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.20 | 0.28 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.02 | 0.01 | 0.07 | 0.08 | 0.14 | 0.15 | 0.17 | 0.14 | 0.10 | 0.07 | 0.03 | 0.03 | 0.02 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.88 | 0.01 | 0.03 | 0.04 | 0.10 | 0.11 | 0.12 | 0.14 | 0.12 | 0.07 | 0.06 | 0.03 | 0.04 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 2 | 0 | 3 |
| 8 | 7 | 5 | 0 | 12 |
| 9 | 7 | 6 | 0 | 13 |
| 10 | 5 | 4 | 0 | 9 |
| 11 | 13 | 12 | 0 | 25 |
| 12 | 11 | 4 | 0 | 15 |
| 13 | 6 | 12 | 0 | 18 |
| 14 | 5 | 20 | 0 | 25 |
| 15 | 26 | 34 | 0 | 60 |
| 16 | 12 | 7 | 0 | 19 |
| 17 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 57.1% | 0.117 | 1.48 | 0.00 | 0.00 | 0.00 | 3.50 | 0.00 | 0.00 | 0.531 |
| rif_LDR05_scudi_armati | 200 | 58.7% | 0.103 | 0.12 | 0.00 | 0.00 | 0.00 | 2.96 | 0.00 | 0.00 | 0.402 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 560 | 0.996 | 0.946 | 0.891 | 0.268 | 2036 | 0.993 | 0.395 | 0.163 | 0.063 |
| rif_LDR02_muro_di_parata | Cicatrice | 560 | 0.295 | 0.241 | 0.154 | 0.036 | 2036 | 0.272 | 0.089 | 0.027 | 0.002 |
| rif_LDR05_scudi_armati | mano | 604 | 0.897 | 0.884 | 0.874 | 0.371 | 1853 | 0.864 | 0.233 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 604 | 0.166 | 0.157 | 0.152 | 0.048 | 1853 | 0.147 | 0.045 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 23.0% | 3.04 | 1.52 | 22.4% | 0.0% | 23.3% | 37.8% | 13.9% | 0.00 | 17.2% | 57.1% | 0.04 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 23.0% | 3.04 | 1.52 | 30.7% | 0.0% | 18.3% | 34.4% | 19.3% | 0.00 | 15.8% | 58.7% | 0.10 | 0.00 |
| Totale | 400 | 23.0% | 3.04 | 1.52 | 26.0% | 0.0% | 20.8% | 36.1% | 16.2% | 0.00 | 16.5% | 57.9% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.433 | 0.284 | 0.4% | 0.4% | 1.87 | 0.00 | 1.04 | 0.05 | 0.00 | 0.00 | 3.98 |
| rif_LDR05_scudi_armati | 200 | 0.461 | 0.234 | 0.0% | 0.0% | 1.70 | 0.00 | 0.80 | 0.82 | 0.00 | 0.00 | 4.58 |

