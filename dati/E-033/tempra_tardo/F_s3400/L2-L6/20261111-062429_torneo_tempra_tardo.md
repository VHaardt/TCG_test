# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 1104s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 44.9% [43.0–46.9] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.5–13.0] (media 12.21) | 8–11 | ❌ |
| Partite al round 13+ | 46.0% [36.6–55.7] | ≤12% | ❌ |
| Partite oltre il 15 | 4.0% [1.6–9.8] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=26) | 61.5% [42.5–77.6] | 20–35% | ❌ |
| Attacchi con opposizione | 20.8% [19.3–22.5] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 52.0% [50.0–54.0] (con ≥3: 16.4% [15.0–18.0]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.8% [34.9–38.7] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 13.6% [9.8–18.5] (n=243) / 86.2% [80.1–90.7] (n=160) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.2% [13.0–17.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 50.0% [26.8–73.2] (n=14), LDR-02 Risvegliato 94.6% [85.4–98.2] (n=56), LDR-06 Base 26.3% [11.8–48.8] (n=19), LDR-06 Risvegliato 73.2% [62.7–81.6] (n=82) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 46.0% [35.9–56.4] (n=87) | | |
| Attacchi per partita | 24.7 | | |
| Pugno attaccante vuoto / pieno | 56.9% [54.8–58.9] / 10.0% [8.8–11.3] (gemme medie 0.86) | non >90% | |
| Pugno difensore vuoto / pieno | 47.4% [44.8–50.1] / 25.8% [23.5–28.2] (gemme medie 0.37) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 881, 1: 915, 2: 438, 3: 175, 4: 47, 5: 8, 6: 2} | | |
| Azioni legali per decisione | 5.6 | <60 | ✅ |
| Fine partita | {'colpo_finale': 83, 'crepuscolo': 17} | | |
| G1 vince fra le partite finite al Crepuscolo | 47.1% [26.2–69.0] | | |
| G1 vince fra le partite arrivate al round 15 | 43.5% [25.6–63.2] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 21.7% [9.7–41.9] / 60.0% [23.1–88.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 20.0% [3.6–62.4]; 17.4% [7.0–37.1] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-0': 2, '2-1': 2, '2-3': 2, '3-2': 2, '0-0': 2, '2-4': 1, '1-5': 1, '1-0': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=5) | 21.7% [9.7–41.9] / 60.0% [23.1–88.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 5}; 80.0% [37.6–96.4] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 60.0% [23.1–88.2] / 20.0% [3.6–62.4]; 1.40 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–43.4] / 80.0% [37.6–96.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 50.0% [9.5–90.5]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.0–8.5] / 13.0% [4.5–32.1]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 1, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=6) / turno di G2 (n=5) | 0.0% [0.0–39.0] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=6) | 0.0% [0.0–39.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 43.5% [25.6–63.2] (21.7% [9.7–41.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 4, 'rif_LDR02_muro_di_parata': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR06_ferite_e_caccia 43% (n=23) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 47.0% [37.5–56.7], rif_LDR06_ferite_e_caccia 53.0% [43.3–62.5]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.516 / 0.071 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.068 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.14 (0.00), rif_LDR06_ferite_e_caccia 0.09 (0.02) | |
| M4 | Scontri decisi prima dell'impegno | 27.0% [25.3–28.8] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.76 (65 / 211); 69.5% [67.6–71.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.5% [48.9–52.0]; rif_LDR02_muro_di_parata 51.7%, rif_LDR06_ferite_e_caccia 49.8% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.7] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.362 (25) / 0.327 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 47 vittorie), LDR-06 G: 17.0 (49%, 53 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-02 2.54, LDR-06 1.49, VER-020 1.41, NER-017 1.24, VER-008 0.64, NEU-001 0.57, NER-013 0.55, VER-023 0.50, NER-009 0.47, BLU-025 0.47, VER-003 0.46, VER-019 0.44 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.53, rif_LDR06_ferite_e_caccia 2.37 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 0.12 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 75% (n=8), rif_LDR06_ferite_e_caccia 56% (n=18) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.0% [8.8–11.3] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 0.49; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NER-009 53%, NEU-001 53%, VER-008 53%, NER-017 53%, NEU-012 53%, VER-023 53%, NER-015 53%, caccia 53%, VER-020 53%, VER-001 53%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 47.0 [38–57] (100) |
| rif_LDR06_ferite_e_caccia | 53.0 [43–62] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.39 | 0.00 | 2.54 / 0.00 | 0.00 | 1.00 | 5.3 (99) | 8 | B 79%, K 21% | 3.10 | 0.00 |
| rif_LDR06_ferite_e_caccia | 4.27 | 0.00 | 1.49 / 0.00 | 0.00 | 0.14 | 4.8 (100) | 9 | G 55%, K 45% | 2.19 | 2.93 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.34/0.17/0.05 | 0.95/0.00/0.25/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.00/0.34/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.11/0.00/0.00 | 0.00/0.22/0.00/0.00 | 0.00/0.47/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.54/2.02/0.83 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.04/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.05/0.10/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.21/0.20/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.34/0.15/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.44/0.57/0.14 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.49/2.01/0.12 | 0.00/0.00/0.00/0.00 | 0.48/0.00/0.00/0.00 | 0.34/0.50/0.08/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.35/0.16/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.02/0.23/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.36/0.07/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.29/0.09/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.64/0.03/0.24 | 0.35/0.01/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.57/0.14/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.62 | 0.00 | 0.00 | 0.01 | 0.02 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.69 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 0.94 | 0.00 | 0.01 | 0.07 | 0.07 | 0.15 | 0.14 | 0.13 | 0.14 | 0.06 | 0.07 | 0.04 | 0.04 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 0.87 | 0.00 | 0.01 | 0.01 | 0.15 | 0.10 | 0.06 | 0.15 | 0.05 | 0.17 | 0.06 | 0.03 | 0.03 | 0.04 | 0.01 | 0.49 | 0.11 | 0.12 | 0.08 | 0.05 | 0.02 | 0.05 | 0.04 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 1 | 0 | 1 |
| 8 | 3 | 0 | 0 | 3 |
| 9 | 5 | 3 | 0 | 8 |
| 10 | 7 | 6 | 0 | 13 |
| 11 | 10 | 5 | 0 | 15 |
| 12 | 8 | 6 | 0 | 14 |
| 13 | 7 | 9 | 0 | 16 |
| 14 | 3 | 4 | 0 | 7 |
| 15 | 8 | 11 | 0 | 19 |
| 16 | 2 | 2 | 0 | 4 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 51.7% | 0.064 | 1.53 | 0.00 | 0.00 | 0.00 | 2.20 | 0.00 | 0.00 | 0.556 |
| rif_LDR06_ferite_e_caccia | 100 | 49.8% | 0.082 | 0.71 | 1.66 | 0.00 | 0.00 | 2.31 | 0.00 | 0.00 | 0.455 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 507 | 1.000 | 0.998 | 0.998 | 0.160 | 988 | 0.998 | 0.329 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 507 | 0.485 | 0.454 | 0.420 | 0.028 | 988 | 0.316 | 0.103 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 196 | 0.929 | 0.898 | 0.888 | 0.362 | 775 | 0.872 | 0.315 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 196 | 0.194 | 0.168 | 0.163 | 0.046 | 775 | 0.186 | 0.063 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 17.0% | 2.56 | 1.33 | 21.1% | 0.0% | 43.3% | 44.0% | 11.7% | 0.00 | 13.5% | 51.7% | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 17.0% | 2.56 | 1.33 | 33.3% | 0.0% | 30.0% | 31.4% | 10.2% | 0.00 | 11.3% | 49.8% | 0.09 | 0.00 |
| Totale | 200 | 17.0% | 2.56 | 1.33 | 26.7% | 0.0% | 36.7% | 37.7% | 11.0% | 0.00 | 12.1% | 50.5% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

