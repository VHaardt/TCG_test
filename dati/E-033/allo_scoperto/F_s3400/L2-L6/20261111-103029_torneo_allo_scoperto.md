# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 1393s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 48.8% [46.8–50.8] | 30–45% | ❌ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 13.11) | 8–11 | ❌ |
| Partite al round 13+ | 66.0% [56.3–74.5] | ≤12% | ❌ |
| Partite oltre il 15 | 10.0% [5.5–17.4] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=29) | 31.0% [17.3–49.2] | 20–35% | ✅ |
| Attacchi con opposizione | 25.7% [24.0–27.5] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 55.5% [53.6–57.5] (con ≥3: 18.1% [16.6–19.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 33.4% [31.6–35.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.4% [2.4–7.9] (n=229) / 77.0% [68.8–83.6] (n=122) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.3% [9.3–13.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 33.3% [12.1–64.6] (n=9), LDR-02 Risvegliato 87.9% [72.7–95.2] (n=33), LDR-06 Base 0.0% [0.0–79.3] (n=1), LDR-06 Risvegliato 70.5% [58.1–80.4] (n=61) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 65.5% [54.8–74.8] (n=84) | | |
| Attacchi per partita | 24.9 | | |
| Pugno attaccante vuoto / pieno | 51.9% [49.9–53.9] / 10.1% [8.9–11.4] (gemme medie 1.00) | non >90% | |
| Pugno difensore vuoto / pieno | 48.4% [45.9–51.0] / 21.7% [19.7–23.9] (gemme medie 0.38) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 812, 1: 952, 2: 437, 3: 225, 4: 57, 5: 9, 6: 2} | | |
| Azioni legali per decisione | 5.8 | <60 | ✅ |
| Fine partita | {'colpo_finale': 75, 'crepuscolo': 25} | | |
| G1 vince fra le partite finite al Crepuscolo | 52.0% [33.5–70.0] | | |
| G1 vince fra le partite arrivate al round 15 | 53.8% [38.6–68.4] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 12.8% [5.6–26.7] / 60.0% [23.1–88.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 20.0% [3.6–62.4]; 25.6% [14.6–41.1] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 9, '3-2': 7, '2-1': 3, '2-3': 2, '0-2': 2, '4-2': 2, '1-1': 2, '1-2': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=11) | 28.2% [16.5–43.8] / 45.5% [21.3–72.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 5, 16: 6}; 54.5% [28.0–78.7] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 72.7% [43.4–90.3] / 36.4% [15.2–64.6]; 3.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–25.9] / 90.9% [62.3–98.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 66.7% [30.0–90.3]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.0% [2.2–11.2] / 12.8% [5.6–26.7]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 5, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=19) / turno di G2 (n=8) | 0.0% [0.0–16.8] / 0.0% [0.0–32.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=19) | 0.0% [0.0–16.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 43.6% [29.3–59.0] (20.5% [10.8–35.5]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 7, 'rif_LDR02_muro_di_parata': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR06_ferite_e_caccia 54% (n=39) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 50.0% [40.4–59.6], rif_LDR06_ferite_e_caccia 50.0% [40.4–59.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.558 / 0.066 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.064 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.14 (0.00), rif_LDR06_ferite_e_caccia 0.06 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 23.4% [21.8–25.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.83 (88 / 195); 65.4% [63.5–67.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.5% [50.1–53.0]; rif_LDR02_muro_di_parata 53.2%, rif_LDR06_ferite_e_caccia 50.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.356 (32) / 0.339 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 50 vittorie), LDR-06 G: 17.0 (49%, 50 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-02 2.62, VER-020 1.55, LDR-06 1.52, NER-017 0.78, VER-008 0.76, NER-013 0.59, BLU-001 0.59, NER-001 0.58, NEU-001 0.51, VER-023 0.50, NER-009 0.47, NEU-004 0.47 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.58, rif_LDR06_ferite_e_caccia 1.88 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 0.13 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 29% (n=14), rif_LDR06_ferite_e_caccia 33% (n=15) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.1% [8.9–11.4] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 0.57; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, collante 100%, NEU-003 50%, NER-014 50%, BLU-022 50%, NEU-015 50%, RS 50%, 11.1 50%, BLU-021 50%, NEU-009 50%, NER-015 50%, caccia 50%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 50.0 [40–60] (100) |
| rif_LDR06_ferite_e_caccia | 50.0 [40–60] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.22 | 0.00 | 2.62 / 0.00 | 0.00 | 1.44 | 5.6 (98) | 8 | B 81%, K 19% | 3.13 | 0.00 |
| rif_LDR06_ferite_e_caccia | 4.46 | 0.00 | 1.52 / 0.01 | 0.00 | 0.26 | 4.9 (100) | 9 | G 55%, K 45% | 2.47 | 2.64 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.90/0.59/0.20/0.07 | 0.94/0.00/0.16/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.00/0.46/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.16/0.00/0.00 | 0.00/0.40/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.62/1.68/0.84 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.47/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.05/0.12/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.27/0.28/0.25 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.75/0.41/0.07/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.44/0.51/0.09 | 0.00/0.25/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.52/1.83/0.21 | 0.00/0.00/0.00/0.00 | 0.50/0.00/0.00/0.00 | 0.28/0.50/0.01/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.58/0.21/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.16/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.05/0.21/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.50/0.47/0.06/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.27/0.04/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.76/0.02/0.24 | 0.46/0.04/0.04/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.86/0.51/0.17/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.72 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.19 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.18 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.77 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 1.21 | 0.00 | 0.02 | 0.06 | 0.08 | 0.20 | 0.15 | 0.13 | 0.14 | 0.11 | 0.12 | 0.08 | 0.02 | 0.08 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 1.18 | 0.00 | 0.00 | 0.03 | 0.05 | 0.18 | 0.10 | 0.14 | 0.14 | 0.12 | 0.11 | 0.11 | 0.09 | 0.07 | 0.04 | 0.57 | 0.10 | 0.16 | 0.05 | 0.03 | 0.04 | 0.03 | 0.04 | 0.02 | 0.01 | 0.05 | 0.03 | 0.00 | 0.01 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 0 | 0 | 1 |
| 8 | 2 | 1 | 0 | 3 |
| 9 | 4 | 1 | 0 | 5 |
| 10 | 3 | 5 | 0 | 8 |
| 11 | 7 | 3 | 0 | 10 |
| 12 | 5 | 2 | 0 | 7 |
| 13 | 8 | 4 | 0 | 12 |
| 14 | 11 | 4 | 0 | 15 |
| 15 | 15 | 14 | 0 | 29 |
| 16 | 6 | 4 | 0 | 10 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 53.2% | 0.057 | 1.58 | 0.00 | 0.00 | 0.00 | 2.34 | 0.00 | 0.00 | 0.598 |
| rif_LDR06_ferite_e_caccia | 100 | 50.5% | 0.080 | 0.70 | 1.18 | 0.00 | 0.00 | 2.10 | 0.00 | 0.00 | 0.498 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 514 | 1.000 | 1.000 | 0.998 | 0.138 | 977 | 1.000 | 0.387 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 514 | 0.426 | 0.405 | 0.372 | 0.027 | 977 | 0.285 | 0.096 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 231 | 0.935 | 0.913 | 0.892 | 0.320 | 772 | 0.902 | 0.352 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 231 | 0.199 | 0.177 | 0.152 | 0.026 | 772 | 0.190 | 0.100 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 25.0% | 2.60 | 1.36 | 30.0% | 0.0% | 47.0% | 44.8% | 13.6% | 0.00 | 15.0% | 53.2% | 0.01 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 25.0% | 2.60 | 1.36 | 42.2% | 0.0% | 30.7% | 32.0% | 9.7% | 0.00 | 12.4% | 50.5% | 0.10 | 0.00 |
| Totale | 200 | 25.0% | 2.60 | 1.36 | 36.8% | 0.0% | 38.8% | 38.4% | 11.8% | 0.00 | 13.4% | 51.5% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

