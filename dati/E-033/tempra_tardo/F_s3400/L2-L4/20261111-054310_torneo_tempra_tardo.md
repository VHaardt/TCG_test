# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 1404s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 49.0% [47.1–50.9] | 30–45% | ❌ |
| Durata mediana (round) | 14.0 [14.0–14.0] (media 13.45) | 8–11 | ❌ |
| Partite al round 13+ | 73.0% [63.6–80.7] | ≤12% | ❌ |
| Partite oltre il 15 | 6.0% [2.8–12.5] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=28) | 28.6% [15.3–47.1] | 20–35% | ✅ |
| Attacchi con opposizione | 29.0% [27.3–30.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 58.8% [56.9–60.7] (con ≥3: 20.7% [19.2–22.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 32.7% [30.9–34.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 14.2% [10.4–19.1] (n=246) / 86.0% [77.9–91.5] (n=100) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.1% [8.3–12.3] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 50.0% [29.0–71.0] (n=18), LDR-02 Risvegliato 68.2% [53.4–80.0] (n=44), LDR-04 Base 47.1% [26.2–69.0] (n=17), LDR-04 Risvegliato 69.0% [54.0–80.9] (n=42) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 76.9% [66.4–84.9] (n=78) | | |
| Attacchi per partita | 26.1 | | |
| Pugno attaccante vuoto / pieno | 51.9% [49.9–53.9] / 9.4% [8.3–10.6] (gemme medie 0.94) | non >90% | |
| Pugno difensore vuoto / pieno | 51.3% [48.8–53.8] / 20.5% [18.6–22.7] (gemme medie 0.36) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 905, 1: 988, 2: 438, 3: 221, 4: 45, 5: 5, 6: 2, 7: 1} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'crepuscolo': 26, 'colpo_finale': 74} | | |
| G1 vince fra le partite finite al Crepuscolo | 65.4% [46.2–80.6] | | |
| G1 vince fra le partite arrivate al round 15 | 65.8% [49.9–78.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 23.7% [13.0–39.2] / 33.3% [12.1–64.6] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [12.1–64.6]; 15.8% [7.4–30.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'3-2': 8, '2-3': 4, '2-1': 4, '0-0': 3, '1-0': 3, '0-1': 3, '2-2': 2, '3-1': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=15) | 39.5% [25.6–55.3] / 20.0% [7.0–45.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 9, 16: 6}; 40.0% [19.8–64.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 73.3% [48.0–89.1] / 33.3% [15.2–58.3]; 3.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–20.4] / 93.3% [70.2–98.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 41.7% [19.3–68.0]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.0–8.5] / 7.9% [2.7–20.8]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 1, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=9) / turno di G2 (n=7) | 0.0% [0.0–29.9] / 0.0% [0.0–35.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=9) | 0.0% [0.0–29.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 47.4% [32.5–62.7] (13.2% [5.8–27.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 10, 'rif_LDR02_muro_di_parata': 5} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR04_stanca_e_smonta 66% (n=38) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 40.0% [30.9–49.8], rif_LDR04_stanca_e_smonta 60.0% [50.2–69.1]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.491 / 0.079 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.077 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.10 (0.00), rif_LDR04_stanca_e_smonta 0.04 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 24.9% [23.3–26.6] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.12 (24 / 88); 67.4% [65.6–69.2] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 53.2% [51.8–54.6]; rif_LDR02_muro_di_parata 52.9%, rif_LDR04_stanca_e_smonta 53.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.408 (31) / 0.354 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 40 vittorie), LDR-04 B: 14.0 (40%, 60 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 4.11, LDR-02 1.64, BLU-015 1.04, VER-008 0.93, VER-014 0.69, BLU-001 0.52, VER-019 0.49, BLU-025 0.46, VER-023 0.44, BLU-023 0.43, VER-001 0.41, BLU-005 0.40 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.69, rif_LDR04_stanca_e_smonta 2.41 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.33 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 25% (n=20), rif_LDR04_stanca_e_smonta 38% (n=8) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.4% [8.3–10.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-009 100%, NEU-003 100%, RS 100%, BLU-010 60%, VER-008 60%, VER-001 60%, VER-014 60%, caccia 60%, VER-023 60%, NEU-011 60%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 40.0 [31–50] (100) |
| rif_LDR04_stanca_e_smonta | 60.0 [50–69] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.76 | 0.00 | 1.64 / 0.00 | 0.00 | 1.33 | 5.2 (98) | 8 | B 82%, K 18% | 3.24 | 0.00 |
| rif_LDR04_stanca_e_smonta | 5.40 | 1.23 | 4.11 / 0.00 | 0.00 | 0.71 | 4.4 (98) | 10 | B 40%, G 60% | 2.48 | 1.29 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 1.01/0.42/0.21/0.19 | 1.01/0.00/0.25/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.95/0.00/0.37/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.46/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.64/1.64/1.31 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.02/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.03/0.09/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.15/0.28/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.61/0.15/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.82/0.15/0.34/0.04 | 0.38/0.00/0.13/0.01 | 0.78/1.04/0.36/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.72/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.41/0.08/0.24 | 0.59/0.00/0.00/0.00 | 0.76/0.00/0.21/0.05 | 0.00/0.00/0.00/0.00 | 0.54/0.49/0.46/0.07 | 0.00/0.30/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/4.11/1.82/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.44/0.05/0.12 | 0.00/0.00/0.00/0.00 | 0.49/0.40/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.00/0.24/0.03 | 0.28/0.00/0.01/0.00 | 0.35/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.93/0.10/0.35 | 0.41/0.03/0.04/0.02 | 0.35/0.00/0.09/0.02 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.54 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.43 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 1.47 | 0.03 | 0.09 | 0.09 | 0.07 | 0.18 | 0.18 | 0.28 | 0.15 | 0.12 | 0.14 | 0.08 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 1.17 | 0.03 | 0.08 | 0.07 | 0.08 | 0.11 | 0.20 | 0.13 | 0.14 | 0.09 | 0.12 | 0.06 | 0.01 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 8 | 2 | 0 | 0 | 2 |
| 9 | 3 | 1 | 0 | 4 |
| 10 | 2 | 1 | 0 | 3 |
| 11 | 6 | 2 | 0 | 8 |
| 12 | 6 | 4 | 0 | 10 |
| 13 | 5 | 6 | 0 | 11 |
| 14 | 9 | 15 | 0 | 24 |
| 15 | 19 | 13 | 0 | 32 |
| 16 | 6 | 0 | 0 | 6 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 52.9% | 0.055 | 1.69 | 0.00 | 0.00 | 0.00 | 3.48 | 0.00 | 0.00 | 0.611 |
| rif_LDR04_stanca_e_smonta | 100 | 53.5% | 0.108 | 1.82 | 0.59 | 0.00 | 0.00 | 1.30 | 0.00 | 0.00 | 0.341 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 448 | 1.000 | 0.998 | 0.996 | 0.154 | 995 | 1.000 | 0.437 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 448 | 0.424 | 0.402 | 0.344 | 0.022 | 995 | 0.307 | 0.120 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 275 | 0.840 | 0.775 | 0.673 | 0.444 | 887 | 0.693 | 0.179 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 275 | 0.109 | 0.102 | 0.095 | 0.015 | 887 | 0.082 | 0.032 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 26.0% | 2.73 | 1.83 | 8.7% | 0.0% | 37.3% | 41.5% | 15.2% | 0.00 | 10.6% | 52.9% | 0.02 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 26.0% | 2.73 | 1.83 | 38.6% | 0.0% | 24.0% | 31.0% | 7.5% | 0.00 | 17.1% | 53.5% | 0.09 | 0.00 |
| Totale | 200 | 26.0% | 2.73 | 1.83 | 23.3% | 0.0% | 30.7% | 36.3% | 11.7% | 0.00 | 14.6% | 53.2% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

