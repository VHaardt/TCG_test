# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 677s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 38.5% [37.1–39.9] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 10.89) | 8–11 | ✅ |
| Partite al round 13+ | 33.0% [26.9–39.8] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–1.9] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=81) | 33.3% [24.0–44.1] | 20–35% | ✅ |
| Attacchi con opposizione | 29.0% [27.7–30.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 61.9% [60.4–63.4] (con ≥3: 21.5% [20.3–22.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 38.2% [36.8–39.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.7% [4.5–9.8] (n=359) / 80.7% [76.2–84.5] (n=342) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.7% [14.1–17.5] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 71.4% [35.9–91.8] (n=7), LDR-03 Risvegliato 99.0% [96.4–99.7] (n=199), LDR-04 Base 47.1% [26.2–69.0] (n=17), LDR-04 Risvegliato 72.7% [61.9–81.4] (n=77) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 31.5% [25.1–38.6] (n=178) | | |
| Attacchi per partita | 23.0 | | |
| Pugno attaccante vuoto / pieno | 54.5% [53.0–56.0] / 11.9% [10.9–12.9] (gemme medie 0.84) | non >90% | |
| Pugno difensore vuoto / pieno | 57.7% [55.6–59.8] / 23.9% [22.2–25.8] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1384, 1: 1832, 2: 930, 3: 318, 4: 106, 5: 21, 6: 2} | | |
| Azioni legali per decisione | 5.4 | <60 | ✅ |
| Fine partita | {'colpo_finale': 180, 'crepuscolo': 20} | | |
| G1 vince fra le partite finite al Crepuscolo | 35.0% [18.1–56.7] | | |
| G1 vince fra le partite arrivate al round 15 | 38.1% [20.8–59.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 61.9% [40.9–79.2] / 46.2% [23.2–70.9] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 30.8% [12.7–57.6]; 0.0% [0.0–15.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 4, '0-0': 3, '1-1': 3, '0-1': 3, '1-3': 2, '3-1': 1, '2-0': 1, '2-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=13) | 61.9% [40.9–79.2] / 46.2% [23.2–70.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 13}; 69.2% [42.4–87.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 76.9% [49.7–91.8] / 15.4% [4.3–42.2]; 1.92 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–22.8] / 84.6% [57.8–95.7] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=6) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–39.0] / 28.6% [8.2–64.1]; 0.0% [0.0–39.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.4–6.4] / 28.6% [13.8–50.0]; 100.0% [61.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 2, 'vinc:atk': 6} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=8) / turno di G2 (n=9) | 0.0% [0.0–32.4] / 0.0% [0.0–29.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=8) | 0.0% [0.0–32.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 61.9% [40.9–79.2] (33.3% [17.2–54.6]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 8, 'rif_LDR03_sanguinare_per_accendere': 5} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR04_stanca_e_smonta 38% (n=21) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 54.0% [47.1–60.8], rif_LDR04_stanca_e_smonta 46.0% [39.2–52.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.353 / 0.087 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.087 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.11 (0.06), rif_LDR04_stanca_e_smonta 0.10 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 34.5% [33.2–35.9] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.86 (134 / 239); 65.4% [64.0–66.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.2% [50.1–52.3]; rif_LDR03_sanguinare_per_accendere 53.4%, rif_LDR04_stanca_e_smonta 48.4% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.282 (24) / 0.347 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 108 vittorie), LDR-04 B: 14.0 (40%, 92 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 4.58, NER-017 1.20, BLU-015 0.99, ROS-019 0.94, NER-001 0.92, NER-006 0.82, NER-008 0.81, ROS-011 0.81, NER-010 0.73, BLU-023 0.68, NER-013 0.65, BLU-001 0.59 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.20, rif_LDR04_stanca_e_smonta 2.22 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR04_stanca_e_smonta 0.21 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 39% (n=66), rif_LDR04_stanca_e_smonta 7% (n=15) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.9% [10.9–12.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.67, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, caccia 100%, NER-010 54%, NER-009 54%, NER-017 54%, ROS-011 54%, BLU-010 46%, VER-014 46%, NEU-003 46%, VER-023 46%, VER-001 46%, NEU-009 46%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 54.0 [47–61] (200) |
| rif_LDR04_stanca_e_smonta | 46.0 [39–53] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.46 | 0.00 | 0.00 / 0.00 | 2.88 | 0.00 | 4.6 (199) | 8 | K 61%, R 39% | 2.06 | 0.37 |
| rif_LDR04_stanca_e_smonta | 4.62 | 2.04 | 4.58 / 0.00 | 0.00 | 0.42 | 5.1 (198) | 10 | B 42%, G 58% | 2.41 | 0.56 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.10/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.82/0.53 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.92/0.36/0.27 | 0.81/0.82/0.17/0.06 | 0.00/0.00/0.00/0.00 | 0.04/0.00/0.00/0.00 | 0.41/0.09/0.31/0.09 | 0.00/0.28/0.00/0.00 | 0.00/0.06/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.33/0.12/0.17/0.10 | 0.71/0.94/0.36/0.34 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.00/0.22/0.04 | 0.31/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.59/0.14/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.16/0.24/0.12 | 0.32/0.00/0.09/0.07 | 0.73/0.99/0.41/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.68/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.32/0.01/0.22 | 0.74/0.00/0.00/0.00 | 0.56/0.00/0.08/0.03 | 0.00/0.00/0.00/0.00 | 0.34/0.28/0.14/0.18 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/4.58/1.68/0.48 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.23/0.24/0.03/0.09 | 0.00/0.00/0.00/0.00 | 0.40/0.28/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.06/0.06/0.06 | 0.27/0.00/0.01/0.00 | 0.26/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.58/0.04/0.27 | 0.32/0.01/0.01/0.01 | 0.34/0.00/0.10/0.03 | 0.00/0.25/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.69 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.04 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.51 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 1.12 | 0.00 | 0.01 | 0.07 | 0.12 | 0.17 | 0.18 | 0.16 | 0.15 | 0.08 | 0.04 | 0.06 | 0.03 | 0.04 | 0.01 | 1.67 | 0.27 | 0.24 | 0.33 | 0.19 | 0.18 | 0.12 | 0.14 | 0.08 | 0.04 | 0.04 | 0.01 | 0.00 | 0.01 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 0.74 | 0.00 | 0.01 | 0.03 | 0.04 | 0.11 | 0.10 | 0.14 | 0.15 | 0.10 | 0.03 | 0.01 | 0.01 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 1 | 0 | 2 |
| 7 | 4 | 11 | 0 | 15 |
| 8 | 18 | 12 | 0 | 30 |
| 9 | 11 | 10 | 0 | 21 |
| 10 | 14 | 15 | 0 | 29 |
| 11 | 16 | 9 | 0 | 25 |
| 12 | 7 | 5 | 0 | 12 |
| 13 | 12 | 9 | 0 | 21 |
| 14 | 9 | 15 | 0 | 24 |
| 15 | 8 | 13 | 0 | 21 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 53.4% | 0.080 | 0.62 | 0.57 | 0.00 | 0.00 | 3.38 | 0.00 | 0.00 | 0.471 |
| rif_LDR04_stanca_e_smonta | 200 | 48.4% | 0.092 | 1.83 | 0.39 | 0.00 | 0.00 | 1.97 | 0.00 | 0.00 | 0.262 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 449 | 0.927 | 0.915 | 0.913 | 0.307 | 1548 | 0.862 | 0.328 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 449 | 0.307 | 0.292 | 0.272 | 0.049 | 1548 | 0.200 | 0.087 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 462 | 0.844 | 0.777 | 0.721 | 0.470 | 2134 | 0.685 | 0.127 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 462 | 0.152 | 0.130 | 0.104 | 0.045 | 2134 | 0.109 | 0.026 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 10.0% | 2.06 | 2.11 | 30.6% | 0.0% | 20.5% | 29.9% | 8.4% | 0.00 | 9.6% | 53.4% | 0.06 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 10.0% | 2.06 | 2.11 | 28.5% | 0.0% | 25.5% | 28.1% | 6.0% | 0.00 | 20.8% | 48.4% | 0.01 | 0.00 |
| Totale | 400 | 10.0% | 2.06 | 2.11 | 29.4% | 0.0% | 23.0% | 29.0% | 7.2% | 0.00 | 14.5% | 51.2% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

