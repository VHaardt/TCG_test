# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2830s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 41.0% [39.6–42.4] | 30–45% | ✅ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 13.02) | 8–11 | ❌ |
| Partite al round 13+ | 66.5% [59.7–72.7] | ≤12% | ❌ |
| Partite oltre il 15 | 7.0% [4.2–11.4] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=66) | 28.8% [19.3–40.6] | 20–35% | ✅ |
| Attacchi con opposizione | 45.5% [44.1–46.9] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 73.9% [72.7–75.1] (con ≥3: 37.3% [36.0–38.7]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 33.9% [32.5–35.2] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 13.3% [10.3–17.0] (n=392) / 90.0% [85.2–93.4] (n=210) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.4% [10.0–13.0] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 60.7% [42.4–76.4] (n=28), LDR-02 Risvegliato 76.7% [66.9–84.2] (n=90), LDR-05 Base 54.2% [35.1–72.1] (n=24), LDR-05 Risvegliato 75.8% [66.5–83.1] (n=99) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 66.9% [59.5–73.5] (n=169) | | |
| Attacchi per partita | 24.4 | | |
| Pugno attaccante vuoto / pieno | 51.9% [50.4–53.3] / 10.5% [9.7–11.4] (gemme medie 0.96) | non >90% | |
| Pugno difensore vuoto / pieno | 49.6% [47.6–51.6] / 27.3% [25.5–29.2] (gemme medie 0.32) | non >90% | |
| Reazioni per scontro | 0.11 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1605, 1: 1658, 2: 1033, 3: 393, 4: 140, 5: 52, 6: 6, 7: 1} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 159, 'crepuscolo': 41} | | |
| G1 vince fra le partite finite al Crepuscolo | 68.3% [53.0–80.4] | | |
| G1 vince fra le partite arrivate al round 15 | 53.2% [42.2–64.0] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 13.0% [7.2–22.3] / 20.0% [5.7–51.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [23.7–76.3]; 18.2% [11.2–28.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 14, '3-3': 9, '2-3': 8, '3-1': 5, '1-0': 5, '4-2': 5, '3-2': 5, '2-1': 4} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=15) | 19.5% [12.2–29.7] / 20.0% [7.0–45.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 10, 16: 5}; 46.7% [24.8–69.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 80.0% [54.8–93.0] / 33.3% [15.2–58.3]; 2.73 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–20.4] / 93.3% [70.2–98.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 41.7% [19.3–68.0]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.5% [0.5–4.3] / 3.9% [1.3–10.8]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 1, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=31) / turno di G2 (n=22) | 0.0% [0.0–11.0] / 0.0% [0.0–14.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=31) | 0.0% [0.0–11.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 40.3% [30.0–51.4] (7.8% [3.6–16.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 8, 'rott_LDR05_2c': 7} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rott_LDR05_2c 53% (n=77) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 49.5% [42.6–56.4], rott_LDR05_2c 50.5% [43.6–57.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.513 / 0.115 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.108 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.12 (0.00), rott_LDR05_2c 0.09 (0.01) | |
| M4 | Scontri decisi prima dell'impegno | 27.4% [26.2–28.7] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 54.5% [53.1–55.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 59.8% [58.9–60.6]; rif_LDR02_muro_di_parata 59.2%, rott_LDR05_2c 60.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.1% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.288 (502) / 0.312 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 99 vittorie), LDR-05 R: 18.0 (50%, 101 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.77, LDR-02 1.47, BLU-015 1.01, NEW-I04 0.74, BLU-001 0.74, BLU-005 0.67, ROS-018 0.62, BLU-008 0.53, ROS-005 0.51, NEU-004 0.44, BLU-021 0.43, ROS-021 0.43 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.51, rott_LDR05_2c 0.14 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rott_LDR05_2c 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 32% (n=34), rott_LDR05_2c 25% (n=32) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.5% [9.7–11.4] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rott_LDR05_2c 0.51; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, BLU-021 100%, NEU-013 50%, BLU-010 50%, BLU-008 50%, NEU-001 50%, ROS-020 50%, NEU-003 50%, RS 50%, NEU-009 50%, NER-014 50%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rott_LDR05_2c |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 49.5 [43–56] (200) |
| rott_LDR05_2c | 50.5 [44–57] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.09 | 0.00 | 1.47 / 0.00 | 0.00 | 1.33 | 5.0 (197) | 8 | B 84%, K 16% | 1.99 | 0.00 |
| rott_LDR05_2c | 4.11 | 0.00 | 3.77 / 0.00 | 0.00 | 0.69 | 4.2 (199) | 13 | B 46%, R 54% | 2.08 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.85/0.98/0.20/0.10 | 0.78/0.00/0.23/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.00/0.34/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.47/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.28/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.47/1.44/0.91 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 1.02/0.00/0.09/0.06 | 0.94/0.67/0.12/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.43/0.00/0.00/0.00 | 0.44/0.44/0.02/0.04 | 0.41/0.00/0.07/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.11/0.14/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.74/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rott_LDR05_2c | 0.00/0.00/0.00/0.00 | 0.00/3.77/1.57/0.53 | 0.72/0.50/0.10/0.04 | 0.66/0.00/0.11/0.07 | 0.74/0.53/0.26/0.12 | 0.59/0.21/0.20/0.14 | 0.58/0.00/0.12/0.06 | 0.82/1.01/0.29/0.33 | 0.00/0.39/0.00/0.00 | 0.00/0.41/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.21/0.15/0.08 | 0.77/0.41/0.14/0.10 | 0.71/0.13/0.34/0.33 | 0.82/0.51/0.15/0.12 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.17/0.16/0.12 | 0.00/0.00/0.00/0.00 | 0.38/0.62/0.00/0.00 | 0.64/0.38/0.28/0.24 | 0.51/0.43/0.22/0.31 | 0.23/0.14/0.09/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.27/0.06/0.09/0.12 | 0.83/0.35/0.12/0.03 | 0.51/0.00/0.12/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.45 | 0.00 | 0.00 | 0.01 | 0.03 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rott_LDR05_2c | 1.00 | 0.00 | 0.08 | 0.00 | 0.01 | 0.03 | 0.06 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.10 | 0.01 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.14 | 0.23 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.00 | 0.00 | 0.03 | 0.06 | 0.08 | 0.12 | 0.15 | 0.15 | 0.14 | 0.10 | 0.03 | 0.05 | 0.04 | 0.04 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rott_LDR05_2c | 200 | 1.01 | 0.00 | 0.01 | 0.04 | 0.08 | 0.12 | 0.14 | 0.17 | 0.17 | 0.10 | 0.04 | 0.05 | 0.04 | 0.03 | 0.01 | 0.01 | 0.51 | 0.10 | 0.10 | 0.09 | 0.07 | 0.03 | 0.04 | 0.03 | 0.01 | 0.02 | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 8 | 6 | 2 | 0 | 8 |
| 9 | 7 | 4 | 0 | 11 |
| 10 | 11 | 9 | 0 | 20 |
| 11 | 7 | 9 | 0 | 16 |
| 12 | 8 | 4 | 0 | 12 |
| 13 | 12 | 20 | 0 | 32 |
| 14 | 9 | 15 | 0 | 24 |
| 15 | 29 | 34 | 0 | 63 |
| 16 | 12 | 2 | 0 | 14 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 59.2% | 0.123 | 1.51 | 0.00 | 0.00 | 0.00 | 3.17 | 0.00 | 0.00 | 0.528 |
| rott_LDR05_2c | 200 | 60.3% | 0.105 | 0.14 | 0.00 | 0.00 | 0.00 | 2.98 | 0.00 | 0.00 | 0.404 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 588 | 0.997 | 0.937 | 0.900 | 0.270 | 2015 | 0.984 | 0.392 | 0.152 | 0.068 |
| rif_LDR02_muro_di_parata | Cicatrice | 588 | 0.337 | 0.253 | 0.180 | 0.020 | 2015 | 0.283 | 0.088 | 0.029 | 0.005 |
| rott_LDR05_2c | mano | 587 | 0.913 | 0.899 | 0.891 | 0.380 | 1698 | 0.868 | 0.213 | 0.000 | 0.000 |
| rott_LDR05_2c | Cicatrice | 587 | 0.174 | 0.170 | 0.164 | 0.029 | 1698 | 0.165 | 0.051 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 20.5% | 3.00 | 1.66 | 26.4% | 0.0% | 21.0% | 36.8% | 13.2% | 0.00 | 17.5% | 59.2% | 0.04 | 0.00 |
| rott_LDR05_2c | 200 | 20.5% | 3.00 | 1.66 | 35.4% | 0.0% | 19.2% | 35.1% | 16.1% | 0.00 | 14.1% | 60.3% | 0.14 | 0.00 |
| Totale | 400 | 20.5% | 3.00 | 1.66 | 30.6% | 0.0% | 20.1% | 36.0% | 14.6% | 0.00 | 15.7% | 59.8% | 0.09 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.455 | 0.297 | 0.3% | 0.3% | 1.87 | 0.00 | 0.87 | 0.06 | 0.00 | 0.00 | 3.77 |
| rott_LDR05_2c | 200 | 0.456 | 0.228 | 0.0% | 0.0% | 1.49 | 0.00 | 0.93 | 0.95 | 0.00 | 0.00 | 4.50 |

