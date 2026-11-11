# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 1641s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 49.0% [47.1–51.0] | 30–45% | ❌ |
| Durata mediana (round) | 15.0 [14.0–15.0] (media 13.63) | 8–11 | ❌ |
| Partite al round 13+ | 79.0% [70.0–85.8] | ≤12% | ❌ |
| Partite oltre il 15 | 8.0% [4.1–15.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=26) | 42.3% [25.5–61.1] | 20–35% | ❌ |
| Attacchi con opposizione | 30.0% [28.3–31.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 61.1% [59.2–62.9] (con ≥3: 21.2% [19.7–22.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 31.5% [29.7–33.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.4% [2.5–7.6] (n=252) / 85.4% [76.6–91.3] (n=89) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 9.4% [7.6–11.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 60.0% [23.1–88.2] (n=5), LDR-02 Risvegliato 81.0% [66.7–90.0] (n=42), LDR-04 Base 33.3% [9.7–70.0] (n=6), LDR-04 Risvegliato 61.8% [45.0–76.1] (n=34) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 81.0% [71.0–88.1] (n=79) | | |
| Attacchi per partita | 25.7 | | |
| Pugno attaccante vuoto / pieno | 49.3% [47.3–51.3] / 9.6% [8.4–10.8] (gemme medie 1.04) | non >90% | |
| Pugno difensore vuoto / pieno | 54.1% [51.5–56.6] / 21.9% [19.9–24.1] (gemme medie 0.34) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 898, 1: 931, 2: 431, 3: 227, 4: 60, 5: 16, 6: 4} | | |
| Azioni legali per decisione | 5.4 | <60 | ✅ |
| Fine partita | {'colpo_finale': 63, 'crepuscolo': 37} | | |
| G1 vince fra le partite finite al Crepuscolo | 51.4% [35.9–66.6] | | |
| G1 vince fra le partite arrivate al round 15 | 58.5% [45.1–70.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 11.3% [5.3–22.6] / 83.3% [43.6–97.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 0.0% [0.0–39.0]; 15.1% [7.9–27.1] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 7, '2-0': 5, '3-1': 5, '0-2': 4, '3-2': 4, '1-1': 4, '1-2': 3, '3-3': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=10) | 18.9% [10.6–31.4] / 50.0% [23.7–76.3] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 4, 15: 6}; 60.0% [31.3–83.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 70.0% [39.7–89.2] / 20.0% [5.7–51.0]; 2.80 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–27.8] / 100.0% [72.2–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 40.0% [11.8–76.9]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.0% [2.2–11.2] / 9.4% [4.1–20.3]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 5, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=16) / turno di G2 (n=8) | 0.0% [0.0–19.4] / 0.0% [0.0–32.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=16) | 0.0% [0.0–19.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 49.1% [36.1–62.1] (18.9% [10.6–31.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 6, 'rif_LDR04_stanca_e_smonta': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR04_stanca_e_smonta 58% (n=53) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 48.0% [38.5–57.7], rif_LDR04_stanca_e_smonta 52.0% [42.3–61.5]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.474 / 0.085 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.082 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.06 (0.00), rif_LDR04_stanca_e_smonta 0.07 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 25.7% [24.1–27.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.20 (44 / 76); 66.3% [64.4–68.1] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 54.0% [52.6–55.4]; rif_LDR02_muro_di_parata 52.5%, rif_LDR04_stanca_e_smonta 55.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.348 (32) / 0.330 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 48 vittorie), LDR-04 B: 14.0 (40%, 52 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 4.25, LDR-02 2.02, BLU-015 1.22, VER-014 0.84, VER-008 0.81, VER-023 0.64, BLU-025 0.55, VER-019 0.54, BLU-001 0.48, BLU-011 0.46, BLU-023 0.43, VER-001 0.40 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.88, rif_LDR04_stanca_e_smonta 2.46 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.27 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 46% (n=13), rif_LDR04_stanca_e_smonta 38% (n=13) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.6% [8.4–10.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | NEU-003 100%, NEU-009 100%, RS 100%, ponte 100%, collante 100%, BLU-010 52%, caccia 52%, NEU-011 52%, VER-008 52%, VER-001 52%, VER-014 52%, VER-023 52%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 48.0 [38–58] (100) |
| rif_LDR04_stanca_e_smonta | 52.0 [42–62] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 5.07 | 0.00 | 2.02 / 0.00 | 0.00 | 1.44 | 4.7 (97) | 8 | B 79%, K 21% | 3.60 | 0.00 |
| rif_LDR04_stanca_e_smonta | 5.40 | 1.11 | 4.25 / 0.00 | 0.00 | 0.63 | 5.0 (97) | 9 | B 41%, G 59% | 2.23 | 1.07 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.95/0.38/0.14/0.13 | 0.99/0.00/0.23/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.00/0.34/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.11/0.00/0.00 | 0.00/0.55/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.02/1.80/1.34 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.03/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.06/0.11/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.14/0.19/0.39 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.59/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.88/0.15/0.42/0.08 | 0.41/0.00/0.22/0.00 | 0.84/1.22/0.48/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.75/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.75/0.40/0.03/0.20 | 0.62/0.00/0.00/0.00 | 0.76/0.00/0.15/0.04 | 0.00/0.00/0.00/0.00 | 0.47/0.54/0.46/0.09 | 0.00/0.37/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/4.25/1.61/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.64/0.02/0.21 | 0.00/0.00/0.00/0.00 | 0.49/0.29/0.02/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.00/0.11/0.01 | 0.34/0.00/0.00/0.00 | 0.36/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.81/0.01/0.24 | 0.40/0.03/0.02/0.01 | 0.39/0.00/0.21/0.01 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.84 | 0.00 | 0.00 | 0.03 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.18 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.64 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.18 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.19 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 1.11 | 0.02 | 0.04 | 0.04 | 0.13 | 0.10 | 0.17 | 0.12 | 0.12 | 0.16 | 0.12 | 0.08 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 1.41 | 0.01 | 0.08 | 0.08 | 0.13 | 0.10 | 0.16 | 0.18 | 0.15 | 0.14 | 0.08 | 0.13 | 0.10 | 0.06 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 2 | 0 | 2 |
| 8 | 0 | 2 | 0 | 2 |
| 9 | 1 | 1 | 0 | 2 |
| 10 | 4 | 3 | 0 | 7 |
| 11 | 3 | 1 | 0 | 4 |
| 12 | 1 | 3 | 0 | 4 |
| 13 | 7 | 7 | 0 | 14 |
| 14 | 5 | 7 | 0 | 12 |
| 15 | 26 | 19 | 0 | 45 |
| 16 | 5 | 3 | 0 | 8 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 52.5% | 0.062 | 1.88 | 0.00 | 0.00 | 0.00 | 3.85 | 0.00 | 0.00 | 0.606 |
| rif_LDR04_stanca_e_smonta | 100 | 55.0% | 0.110 | 1.90 | 0.56 | 0.00 | 0.00 | 1.14 | 0.00 | 0.00 | 0.328 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 399 | 1.000 | 1.000 | 1.000 | 0.195 | 945 | 0.998 | 0.440 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 399 | 0.409 | 0.391 | 0.343 | 0.015 | 945 | 0.299 | 0.121 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 269 | 0.888 | 0.818 | 0.706 | 0.476 | 954 | 0.744 | 0.184 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 269 | 0.104 | 0.097 | 0.071 | 0.026 | 954 | 0.053 | 0.015 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 37.0% | 3.05 | 1.63 | 30.2% | 0.0% | 37.0% | 42.7% | 15.3% | 0.00 | 10.4% | 52.5% | 0.02 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 37.0% | 3.05 | 1.63 | 30.2% | 0.0% | 24.7% | 28.8% | 9.5% | 0.00 | 17.5% | 55.0% | 0.06 | 0.00 |
| Totale | 200 | 37.0% | 3.05 | 1.63 | 30.2% | 0.0% | 30.8% | 35.7% | 12.6% | 0.00 | 14.8% | 54.0% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

