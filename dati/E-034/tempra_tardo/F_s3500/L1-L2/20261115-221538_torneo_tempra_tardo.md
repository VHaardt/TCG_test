# Torneo v0.2 — /home/claude/e034_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e034_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2616s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 39.6% [38.3–41.0] | 30–45% | ✅ |
| Durata mediana (round) | 13.0 [13.0–14.0] (media 12.55) | 8–11 | ❌ |
| Partite al round 13+ | 61.0% [54.1–67.5] | ≤12% | ❌ |
| Partite oltre il 15 | 3.5% [1.7–7.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=63) | 20.6% [12.5–32.2] | 20–35% | ✅ |
| Attacchi con opposizione | 38.1% [36.7–39.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 70.5% [69.2–71.8] (con ≥3: 32.1% [30.8–33.4]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 35.9% [34.6–37.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 9.5% [7.1–12.5] (n=454) / 84.0% [78.8–88.0] (n=243) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.1% [9.8–12.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 25.0% [11.2–46.9] (n=20), LDR-01 Risvegliato 66.3% [55.6–75.5] (n=83), LDR-02 Base 60.9% [40.8–77.8] (n=23), LDR-02 Risvegliato 75.2% [66.8–82.0] (n=121) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 60.2% [52.8–67.3] (n=171) | | |
| Attacchi per partita | 25.6 | | |
| Pugno attaccante vuoto / pieno | 49.5% [48.1–50.9] / 12.5% [11.6–13.5] (gemme medie 0.97) | non >90% | |
| Pugno difensore vuoto / pieno | 54.1% [52.1–56.0] / 23.7% [22.0–25.4] (gemme medie 0.31) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1768, 1: 1703, 2: 1041, 3: 384, 4: 155, 5: 50, 6: 16, 7: 1} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 158, 'crepuscolo': 42} | | |
| G1 vince fra le partite finite al Crepuscolo | 64.3% [49.2–77.0] | | |
| G1 vince fra le partite arrivate al round 15 | 57.4% [44.9–69.0] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 29.5% [19.6–41.9] / 38.9% [20.3–61.4] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [29.0–71.0]; 11.5% [5.7–21.8] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 9, '2-3': 8, '3-3': 5, '3-1': 4, '2-0': 4, '0-0': 4, '2-1': 4, '1-1': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=21) | 34.4% [23.7–47.0] / 38.1% [20.8–59.1] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 18, 16: 3}; 52.4% [32.4–71.7] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 47.6% [28.3–67.6] / 38.1% [20.8–59.1]; 2.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–15.5] / 85.7% [65.4–95.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=8) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–32.4] / 61.5% [35.5–82.3]; 0.0% [0.0–32.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.0% [2.0–7.7] / 13.1% [6.8–23.8]; 100.0% [67.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 5, 'vinc:atk': 8} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=18) / turno di G2 (n=18) | 0.0% [0.0–17.6] / 0.0% [0.0–17.6] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=18) | 0.0% [0.0–17.6] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 39.3% [28.1–51.9] (3.3% [0.9–11.2]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 11, 'rif_LDR02_muro_di_parata': 10} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR02_muro_di_parata 57% (n=61) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 49.5% [42.6–56.4], rif_LDR02_muro_di_parata 50.5% [43.6–57.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.507 / 0.097 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.094 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.06 (0.00), rif_LDR02_muro_di_parata 0.14 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 26.2% [25.0–27.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.27 (96 / 159); 58.6% [57.3–60.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 56.4% [55.5–57.3]; rif_LDR01_puntata_e_preda 54.9%, rif_LDR02_muro_di_parata 57.9% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.2% [0.1–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.324 (534) / 0.318 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 99 vittorie), LDR-02 K: 6.0 (19%, 101 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-01 2.29, LDR-02 1.31, ROS-016 1.23, ROS-018 0.97, BLU-001 0.80, BLU-005 0.72, VER-011 0.68, NEW-I04 0.66, ROS-001 0.66, VER-019 0.65, NEU-004 0.49, BLU-021 0.49 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.42, rif_LDR02_muro_di_parata 1.45 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR02_muro_di_parata 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 20% (n=20), rif_LDR02_muro_di_parata 21% (n=43) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.5% [11.6–13.5] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR02_muro_di_parata 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, NEU-015 50%, NEU-009 50%, RS 50%, NEU-003 50%, collante 50%, NER-014 50%, BLU-021 50%, caccia 50%, VER-001 50%, ROS-016 50%, VER-008 50%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR02_muro_di_parata |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 49.5 [43–56] (200) |
| rif_LDR02_muro_di_parata | 50.5 [44–57] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.17 | 0.00 | 2.29 / 0.00 | 0.00 | 0.00 | 4.1 (197) | 13 | G 41%, R 59% | 2.61 | 0.61 |
| rif_LDR02_muro_di_parata | 4.42 | 0.00 | 1.31 / 0.00 | 0.00 | 1.51 | 4.4 (196) | 8 | B 83%, K 17% | 2.25 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/2.29/1.61/0.57 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.39/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.85/0.66/0.30/0.09 | 0.78/0.19/0.39/0.27 | 0.77/0.41/0.17/0.10 | 0.00/0.33/0.00/0.00 | 0.81/0.00/0.27/0.08 | 0.68/0.16/0.20/0.14 | 0.81/1.23/0.06/0.38 | 0.73/0.97/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.47/0.23/0.24 | 0.28/0.10/0.13/0.12 | 0.00/0.00/0.00/0.00 | 0.67/0.40/0.02/0.19 | 0.80/0.00/0.00/0.00 | 0.85/0.00/0.21/0.07 | 0.69/0.68/0.20/0.10 | 0.80/0.65/0.45/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.10/0.03 | 0.39/0.07/0.05/0.03 | 0.37/0.10/0.10/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.04/0.01 | 0.38/0.46/0.01/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.91/0.80/0.26/0.21 | 0.76/0.00/0.26/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.00/0.49/0.34 | 0.00/0.00/0.00/0.00 | 0.00/0.49/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.31/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.31/1.88/1.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.88/0.00/0.09/0.07 | 0.91/0.72/0.13/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.02/0.00/0.00 | 0.38/0.00/0.00/0.00 | 0.49/0.49/0.07/0.03 | 0.40/0.04/0.13/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.14/0.14/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.66/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.08 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.15 | 0.01 | 0.00 | 0.01 | 0.11 | 0.13 | 0.00 | 0.00 | 0.24 | 0.07 | 0.00 | 0.01 | 0.00 | 0.01 | 0.04 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 0.46 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.97 | 0.01 | 0.07 | 0.06 | 0.10 | 0.11 | 0.12 | 0.18 | 0.12 | 0.09 | 0.06 | 0.02 | 0.04 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 200 | 1.18 | 0.04 | 0.09 | 0.12 | 0.14 | 0.17 | 0.15 | 0.18 | 0.12 | 0.04 | 0.04 | 0.04 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 1 | 0 | 1 |
| 7 | 1 | 5 | 0 | 6 |
| 8 | 7 | 5 | 0 | 12 |
| 9 | 10 | 5 | 0 | 15 |
| 10 | 9 | 6 | 0 | 15 |
| 11 | 5 | 10 | 0 | 15 |
| 12 | 10 | 4 | 0 | 14 |
| 13 | 12 | 16 | 0 | 28 |
| 14 | 10 | 23 | 0 | 33 |
| 15 | 31 | 23 | 0 | 54 |
| 16 | 4 | 3 | 0 | 7 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 54.9% | 0.075 | 0.00 | 0.42 | 0.00 | 0.00 | 2.87 | 0.00 | 0.00 | 0.357 |
| rif_LDR02_muro_di_parata | 200 | 57.9% | 0.118 | 1.45 | 0.00 | 0.00 | 0.00 | 3.40 | 0.00 | 0.00 | 0.542 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 532 | 0.885 | 0.829 | 0.778 | 0.320 | 1896 | 0.820 | 0.197 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 532 | 0.173 | 0.158 | 0.139 | 0.021 | 1896 | 0.148 | 0.056 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | mano | 616 | 0.997 | 0.927 | 0.847 | 0.261 | 2074 | 0.986 | 0.416 | 0.169 | 0.061 |
| rif_LDR02_muro_di_parata | Cicatrice | 616 | 0.300 | 0.231 | 0.183 | 0.039 | 2074 | 0.221 | 0.081 | 0.018 | 0.002 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 21.0% | 2.61 | 1.79 | 33.9% | 0.0% | 15.7% | 29.2% | 6.2% | 0.00 | 15.0% | 54.9% | 0.16 | 0.00 |
| rif_LDR02_muro_di_parata | 200 | 21.0% | 2.61 | 1.79 | 28.9% | 0.0% | 21.3% | 37.0% | 13.2% | 0.00 | 15.6% | 57.9% | 0.00 | 0.00 |
| Totale | 400 | 21.0% | 2.61 | 1.79 | 31.6% | 0.0% | 18.5% | 33.1% | 10.3% | 0.00 | 15.3% | 56.4% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.398 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.55 |
| rif_LDR02_muro_di_parata | 200 | 0.365 | 0.220 | 0.3% | 0.2% | 1.39 | 0.23 | 0.77 | 0.00 | 0.00 | 0.00 | 4.63 |

