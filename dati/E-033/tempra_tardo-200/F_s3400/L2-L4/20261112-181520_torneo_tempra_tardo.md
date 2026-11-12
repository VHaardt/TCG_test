# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1504s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 49.2% [47.8–50.5] | 30–45% | ❌ |
| Durata mediana (round) | 14.0 [14.0–14.0] (media 13.37) | 8–11 | ❌ |
| Partite al round 13+ | 68.5% [61.8–74.5] | ≤12% | ❌ |
| Partite oltre il 15 | 8.0% [5.0–12.6] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=69) | 34.8% [24.6–46.6] | 20–35% | ✅ |
| Attacchi con opposizione | 28.6% [27.3–29.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 59.5% [58.2–60.9] (con ≥3: 20.7% [19.6–21.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 33.4% [32.1–34.7] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 10.1% [7.7–13.0] (n=507) / 82.5% [77.0–86.9] (n=223) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.7% [9.4–12.3] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 58.3% [38.8–75.5] (n=24), LDR-02 Risvegliato 76.1% [66.4–83.6] (n=92), LDR-04 Base 37.0% [21.5–55.8] (n=27), LDR-04 Risvegliato 66.3% [56.2–75.1] (n=92) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 71.8% [64.4–78.1] (n=163) | | |
| Attacchi per partita | 25.6 | | |
| Pugno attaccante vuoto / pieno | 51.3% [49.9–52.8] / 9.2% [8.4–10.1] (gemme medie 0.94) | non >90% | |
| Pugno difensore vuoto / pieno | 50.4% [48.6–52.3] / 21.6% [20.1–23.1] (gemme medie 0.36) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1717, 1: 1985, 2: 874, 3: 424, 4: 108, 5: 15, 6: 6, 7: 1} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'crepuscolo': 61, 'colpo_finale': 139} | | |
| G1 vince fra le partite finite al Crepuscolo | 62.3% [49.7–73.4] | | |
| G1 vince fra le partite arrivate al round 15 | 60.7% [50.0–70.5] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 23.8% [16.0–33.9] / 35.0% [18.1–56.7] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 35.0% [18.1–56.7]; 19.0% [12.1–28.7] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'3-2': 10, '2-1': 10, '1-0': 7, '0-0': 6, '2-2': 6, '2-3': 6, '0-1': 6, '2-0': 6} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=29) | 34.5% [25.2–45.2] / 34.5% [19.9–52.7] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 20, 16: 9}; 55.2% [37.5–71.6] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 69.0% [50.8–82.7] / 24.1% [12.2–42.1]; 2.48 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–11.7] / 86.2% [69.4–94.5] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=10) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–27.8] / 36.8% [19.1–59.0]; 0.0% [0.0–27.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.0% [2.7–9.0] / 11.9% [6.6–20.5]; 100.0% [72.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 8, 'perd:pronto': 2, 'vinc:atk': 10} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=22) / turno di G2 (n=18) | 0.0% [0.0–14.9] / 0.0% [0.0–17.6] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=22) | 0.0% [0.0–14.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 56.0% [45.3–66.1] (15.5% [9.3–24.7]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 21, 'rif_LDR02_muro_di_parata': 8} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR04_stanca_e_smonta 61% (n=84) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 38.5% [32.0–45.4], rif_LDR04_stanca_e_smonta 61.5% [54.6–68.0]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.495 / 0.083 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.081 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.12 (0.00), rif_LDR04_stanca_e_smonta 0.06 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 25.2% [24.1–26.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.03 (50 / 157); 68.1% [66.8–69.4] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 54.0% [53.0–55.0]; rif_LDR02_muro_di_parata 53.4%, rif_LDR04_stanca_e_smonta 54.4% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.342 (50) / 0.341 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 77 vittorie), LDR-04 B: 14.0 (40%, 123 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 4.41, LDR-02 1.71, BLU-015 1.23, VER-008 0.77, VER-014 0.71, BLU-025 0.53, BLU-001 0.46, BLU-023 0.43, VER-019 0.43, VER-023 0.42, VER-001 0.41, BLU-011 0.32 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.74, rif_LDR04_stanca_e_smonta 2.33 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.32 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 25% (n=40), rif_LDR04_stanca_e_smonta 48% (n=29) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.2% [8.4–10.1] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, NEU-003 100%, ponte 100%, NEU-009 100%, RS 100%, NEU-011 62%, VER-014 62%, BLU-010 62%, VER-008 62%, VER-001 62%, caccia 62%, VER-023 62%; oltre il 60%: VER-001, VER-008, VER-023 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 38.5 [32–45] (200) |
| rif_LDR04_stanca_e_smonta | 61.5 [55–68] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.81 | 0.00 | 1.71 / 0.00 | 0.00 | 1.30 | 4.8 (196) | 8 | B 81%, K 19% | 3.34 | 0.00 |
| rif_LDR04_stanca_e_smonta | 5.36 | 1.16 | 4.41 / 0.00 | 0.00 | 0.72 | 4.8 (197) | 10 | B 41%, G 59% | 2.32 | 1.18 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.98/0.34/0.18/0.17 | 1.00/0.00/0.27/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.85/0.00/0.29/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.53/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.71/1.81/1.19 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.04/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.03/0.10/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.17/0.20/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.58/0.17/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.17/0.33/0.07 | 0.38/0.00/0.14/0.03 | 0.82/1.23/0.49/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.75/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.41/0.09/0.24 | 0.58/0.00/0.00/0.00 | 0.71/0.00/0.21/0.03 | 0.00/0.00/0.00/0.00 | 0.46/0.43/0.39/0.06 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/4.41/1.83/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.42/0.05/0.11 | 0.00/0.00/0.00/0.00 | 0.42/0.29/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.00/0.21/0.02 | 0.34/0.00/0.01/0.01 | 0.32/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.77/0.06/0.29 | 0.40/0.02/0.03/0.01 | 0.35/0.00/0.13/0.02 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.51 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.43 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.01 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.37 | 0.03 | 0.07 | 0.09 | 0.09 | 0.17 | 0.17 | 0.27 | 0.11 | 0.10 | 0.13 | 0.07 | 0.06 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 1.30 | 0.03 | 0.07 | 0.08 | 0.13 | 0.16 | 0.17 | 0.12 | 0.17 | 0.12 | 0.12 | 0.07 | 0.03 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 8 | 3 | 2 | 0 | 5 |
| 9 | 4 | 3 | 0 | 7 |
| 10 | 8 | 7 | 0 | 15 |
| 11 | 10 | 6 | 0 | 16 |
| 12 | 13 | 7 | 0 | 20 |
| 13 | 6 | 8 | 0 | 14 |
| 14 | 16 | 23 | 0 | 39 |
| 15 | 42 | 26 | 0 | 68 |
| 16 | 9 | 7 | 0 | 16 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 53.4% | 0.061 | 1.74 | 0.00 | 0.00 | 0.00 | 3.25 | 0.00 | 0.00 | 0.606 |
| rif_LDR04_stanca_e_smonta | 200 | 54.4% | 0.111 | 1.79 | 0.54 | 0.00 | 0.00 | 1.22 | 0.00 | 0.00 | 0.355 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 895 | 1.000 | 0.999 | 0.998 | 0.165 | 1963 | 0.999 | 0.426 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 895 | 0.441 | 0.418 | 0.366 | 0.028 | 1963 | 0.304 | 0.124 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 546 | 0.853 | 0.786 | 0.689 | 0.440 | 1726 | 0.698 | 0.185 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 546 | 0.152 | 0.136 | 0.110 | 0.022 | 1726 | 0.107 | 0.043 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 30.5% | 2.73 | 1.92 | 15.4% | 0.0% | 34.7% | 42.7% | 16.0% | 0.00 | 10.6% | 53.4% | 0.02 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 30.5% | 2.73 | 1.92 | 39.1% | 0.0% | 26.0% | 30.7% | 8.9% | 0.00 | 16.5% | 54.4% | 0.07 | 0.00 |
| Totale | 400 | 30.5% | 2.73 | 1.92 | 26.5% | 0.0% | 30.3% | 36.7% | 12.8% | 0.00 | 14.3% | 54.0% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

