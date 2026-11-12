# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 669s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 40.2% [38.9–41.6] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.0–12.0] (media 11.94) | 8–11 | ❌ |
| Partite al round 13+ | 41.0% [34.4–47.9] | ≤12% | ❌ |
| Partite oltre il 15 | 0.5% [0.1–2.8] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=78) | 35.9% [26.1–47.0] | 20–35% | ❌ |
| Attacchi con opposizione | 20.9% [19.8–22.1] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 57.1% [55.6–58.5] (con ≥3: 19.6% [18.5–20.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.6% [33.3–35.9] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 11.0% [8.6–14.0] (n=510) / 79.2% [74.5–83.2] (n=331) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.0% [13.4–16.8] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 42.5% [28.5–57.8] (n=40), LDR-04 Risvegliato 75.2% [66.0–82.6] (n=101), LDR-06 Base 56.2% [33.2–76.9] (n=16), LDR-06 Risvegliato 81.4% [74.6–86.6] (n=161) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 46.5% [39.0–54.3] (n=159) | | |
| Attacchi per partita | 25.2 | | |
| Pugno attaccante vuoto / pieno | 55.2% [53.7–56.7] / 11.2% [10.3–12.2] (gemme medie 0.81) | non >90% | |
| Pugno difensore vuoto / pieno | 61.4% [59.4–63.3] / 21.9% [20.3–23.5] (gemme medie 0.24) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1822, 1: 1949, 2: 859, 3: 278, 4: 97, 5: 31, 6: 4} | | |
| Azioni legali per decisione | 5.7 | <60 | ✅ |
| Fine partita | {'colpo_finale': 174, 'crepuscolo': 26} | | |
| G1 vince fra le partite finite al Crepuscolo | 30.8% [16.5–50.0] | | |
| G1 vince fra le partite arrivate al round 15 | 31.0% [17.3–49.2] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 51.7% [34.4–68.6] / 53.3% [30.1–75.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 6.7% [1.2–29.8]; 3.4% [0.6–17.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-1': 6, '0-0': 5, '1-1': 3, '2-1': 3, '2-0': 3, '1-3': 2, '2-3': 2, '3-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=16) | 55.2% [37.5–71.6] / 56.2% [33.2–76.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15, 16: 1}; 93.8% [71.7–98.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 37.5% [18.5–61.4] / 6.2% [1.1–28.3]; 1.31 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–19.4] / 75.0% [50.5–89.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=9) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–29.9] / 14.3% [2.6–51.3]; 0.0% [0.0–29.9] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.5% [2.4–8.3] / 31.0% [17.3–49.2]; 100.0% [70.1–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 6, 'perd:pronto': 3, 'vinc:atk': 9} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=7) / turno di G2 (n=9) | 0.0% [0.0–35.4] / 0.0% [0.0–29.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=7) | 0.0% [0.0–35.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 44.8% [28.4–62.5] (20.7% [9.8–38.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 10, 'rif_LDR06_ferite_e_caccia': 6} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR06_ferite_e_caccia 31% (n=29) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 60.5% [53.6–67.0], rif_LDR06_ferite_e_caccia 39.5% [33.0–46.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.370 / 0.077 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.077 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.07 (0.00), rif_LDR06_ferite_e_caccia 0.12 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 35.4% [34.1–36.7] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.11 (286 / 735); 62.8% [61.4–64.1] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.7% [51.6–53.7]; rif_LDR04_stanca_e_smonta 56.6%, rif_LDR06_ferite_e_caccia 48.7% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.326 (77) / 0.315 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 14.0 (40%, 121 vittorie), LDR-06 G: 17.0 (49%, 79 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 3.48, LDR-06 2.57, VER-020 1.73, VER-008 1.08, NER-017 0.93, BLU-023 0.69, NER-009 0.63, BLU-015 0.62, VER-023 0.57, VER-001 0.55, VER-003 0.52, NER-013 0.50 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.77, rif_LDR06_ferite_e_caccia 3.36 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.20, rif_LDR06_ferite_e_caccia 0.28 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 54% (n=26), rif_LDR06_ferite_e_caccia 27% (n=52) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.2% [10.3–12.2] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR06_ferite_e_caccia 0.96; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-001 100%, VER-008 100%, ponte 100%, VER-023 100%, collante 100%, caccia 100%, BLU-010 60%, RS 60%, VER-014 60%, NEU-003 60%, NEU-009 60%, NEU-011 60%; oltre il 60%: VER-001, VER-008, VER-023 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 60.5 [54–67] (200) |
| rif_LDR06_ferite_e_caccia | 39.5 [33–46] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.17 | 1.42 | 3.48 / 0.00 | 0.00 | 0.66 | 5.2 (199) | 10 | B 42%, G 58% | 2.46 | 0.69 |
| rif_LDR06_ferite_e_caccia | 4.13 | 0.00 | 2.57 / 0.07 | 0.00 | 0.13 | 4.7 (195) | 10 | G 57%, K 43% | 2.46 | 1.58 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.41/0.15/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.82/0.18/0.40/0.11 | 0.37/0.00/0.14/0.04 | 0.66/0.62/0.34/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.69/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.56/0.05/0.45 | 0.65/0.00/0.00/0.00 | 0.62/0.00/0.14/0.06 | 0.00/0.00/0.00/0.00 | 0.42/0.26/0.23/0.12 | 0.00/0.32/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.48/2.11/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.42/0.06/0.20 | 0.00/0.00/0.00/0.00 | 0.42/0.24/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.14/0.24/0.02 | 0.30/0.00/0.01/0.00 | 0.26/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.86/0.01/0.36 | 0.40/0.03/0.03/0.02 | 0.32/0.00/0.10/0.03 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.54/0.04/0.39 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.54/0.57/0.26 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.57/2.10/0.60 | 0.00/0.00/0.00/0.00 | 0.61/0.00/0.00/0.00 | 0.35/0.72/0.06/0.33 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.44/0.20/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.07/0.21/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.19/0.06/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.49/0.04/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/1.29/0.01/0.58 | 0.32/0.04/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.47/0.15/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.61 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.06 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.01 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.16 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.78 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.28 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.94 | 0.00 | 0.03 | 0.07 | 0.07 | 0.10 | 0.14 | 0.15 | 0.12 | 0.15 | 0.04 | 0.02 | 0.02 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.93 | 0.00 | 0.01 | 0.10 | 0.04 | 0.11 | 0.08 | 0.12 | 0.16 | 0.09 | 0.07 | 0.05 | 0.06 | 0.04 | 0.01 | 0.96 | 0.10 | 0.18 | 0.07 | 0.08 | 0.12 | 0.13 | 0.07 | 0.08 | 0.07 | 0.04 | 0.01 | 0.01 | 0.01 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 7 | 1 | 1 | 0 | 2 |
| 8 | 4 | 1 | 0 | 5 |
| 9 | 9 | 7 | 0 | 16 |
| 10 | 10 | 14 | 0 | 24 |
| 11 | 26 | 22 | 0 | 48 |
| 12 | 12 | 10 | 0 | 22 |
| 13 | 9 | 17 | 0 | 26 |
| 14 | 9 | 18 | 0 | 27 |
| 15 | 9 | 19 | 0 | 28 |
| 16 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 56.6% | 0.093 | 1.92 | 0.85 | 0.00 | 0.00 | 1.93 | 0.00 | 0.00 | 0.286 |
| rif_LDR06_ferite_e_caccia | 200 | 48.7% | 0.058 | 0.94 | 2.42 | 0.00 | 0.00 | 4.42 | 0.00 | 0.00 | 0.465 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 520 | 0.837 | 0.744 | 0.681 | 0.452 | 2169 | 0.681 | 0.145 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 520 | 0.129 | 0.106 | 0.079 | 0.029 | 2169 | 0.076 | 0.031 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 443 | 0.950 | 0.898 | 0.862 | 0.255 | 1908 | 0.911 | 0.352 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 443 | 0.271 | 0.255 | 0.217 | 0.054 | 1908 | 0.175 | 0.068 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 13.0% | 2.33 | 1.92 | 33.7% | 0.5% | 22.7% | 27.3% | 7.3% | 0.00 | 14.0% | 56.6% | 0.02 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 13.0% | 2.33 | 1.92 | 18.1% | 0.5% | 25.3% | 27.2% | 7.3% | 0.00 | 8.7% | 48.7% | 0.04 | 0.00 |
| Totale | 400 | 13.0% | 2.33 | 1.92 | 24.9% | 0.5% | 24.0% | 27.2% | 7.3% | 0.00 | 11.4% | 52.7% | 0.03 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

