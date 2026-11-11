# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 642s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 39.5% [37.5–41.5] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–12.0] (media 10.99) | 8–11 | ✅ |
| Partite al round 13+ | 35.0% [26.4–44.7] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=43) | 32.6% [20.5–47.5] | 20–35% | ✅ |
| Attacchi con opposizione | 30.0% [28.1–31.9] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 62.2% [60.2–64.3] (con ≥3: 21.7% [20.0–23.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.6% [35.6–39.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 7.0% [4.1–11.5] (n=187) / 78.0% [70.9–83.7] (n=159) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.6% [12.4–17.2] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 100.0% [43.8–100.0] (n=3), LDR-03 Risvegliato 100.0% [95.9–100.0] (n=90), LDR-04 Base 50.0% [23.7–76.3] (n=10), LDR-04 Risvegliato 79.4% [63.2–89.7] (n=34) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 34.9% [25.7–45.4] (n=86) | | |
| Attacchi per partita | 22.6 | | |
| Pugno attaccante vuoto / pieno | 55.7% [53.5–57.9] / 11.3% [10.0–12.8] (gemme medie 0.82) | non >90% | |
| Pugno difensore vuoto / pieno | 58.6% [55.6–61.5] / 23.1% [20.7–25.7] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 669, 1: 920, 2: 462, 3: 146, 4: 48, 5: 12} | | |
| Azioni legali per decisione | 5.4 | <60 | ✅ |
| Fine partita | {'colpo_finale': 87, 'crepuscolo': 13} | | |
| G1 vince fra le partite finite al Crepuscolo | 30.8% [12.7–57.6] | | |
| G1 vince fra le partite arrivate al round 15 | 30.8% [12.7–57.6] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 84.6% [57.8–95.7] / 54.5% [28.0–78.7] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 27.3% [9.7–56.6]; 0.0% [0.0–22.8] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-0': 3, '1-0': 3, '1-1': 3, '0-1': 2, '3-1': 1, '1-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=11) | 84.6% [57.8–95.7] / 54.5% [28.0–78.7] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 11}; 72.7% [43.4–90.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 72.7% [43.4–90.3] / 18.2% [5.1–47.7]; 1.82 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–25.9] / 81.8% [52.3–94.9] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=6) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–39.0] / 40.0% [11.8–76.9]; 0.0% [0.0–39.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 6.0% [2.8–12.5] / 46.2% [23.2–70.9]; 100.0% [61.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 2, 'vinc:atk': 6} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=4) / turno di G2 (n=6) | 0.0% [0.0–49.0] / 0.0% [0.0–39.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=4) | 0.0% [0.0–49.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 69.2% [42.4–87.3] (38.5% [17.7–64.5]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 7, 'rif_LDR03_sanguinare_per_accendere': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR04_stanca_e_smonta 31% (n=13) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 51.0% [41.3–60.6], rif_LDR04_stanca_e_smonta 49.0% [39.4–58.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.354 / 0.083 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.083 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.09 (0.06), rif_LDR04_stanca_e_smonta 0.08 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 34.1% [32.2–36.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.64 (54 / 110); 65.1% [63.1–67.1] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.6% [50.1–53.1]; rif_LDR03_sanguinare_per_accendere 53.4%, rif_LDR04_stanca_e_smonta 49.2% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.261 (12) / 0.351 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 51 vittorie), LDR-04 B: 14.0 (40%, 49 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 4.41, ROS-019 1.05, NER-017 0.97, NER-001 0.94, NER-008 0.92, BLU-015 0.85, NER-006 0.75, NER-013 0.72, ROS-011 0.71, NER-010 0.65, BLU-023 0.65, VER-014 0.65 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.11, rif_LDR04_stanca_e_smonta 2.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR04_stanca_e_smonta 0.18 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 37% (n=35), rif_LDR04_stanca_e_smonta 12% (n=8) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.3% [10.0–12.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.75, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | caccia 100%, ponte 100%, NER-009 51%, NER-017 51%, NER-010 51%, ROS-011 51%, NEU-011 49%, VER-014 49%, VER-008 49%, NEU-009 49%, RS 49%, NEU-003 49%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 51.0 [41–61] (100) |
| rif_LDR04_stanca_e_smonta | 49.0 [39–59] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.45 | 0.00 | 0.00 / 0.00 | 3.15 | 0.00 | 4.7 (100) | 8 | K 60%, R 40% | 2.13 | 0.34 |
| rif_LDR04_stanca_e_smonta | 4.56 | 1.92 | 4.41 / 0.00 | 0.00 | 0.40 | 5.2 (99) | 10 | B 42%, G 58% | 2.49 | 0.58 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.07/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.78/0.52 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.94/0.38/0.26 | 0.72/0.75/0.14/0.07 | 0.00/0.00/0.00/0.00 | 0.04/0.00/0.00/0.00 | 0.41/0.10/0.31/0.10 | 0.00/0.24/0.00/0.00 | 0.00/0.05/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.07/0.03 | 0.00/0.00/0.00/0.00 | 0.33/0.10/0.11/0.07 | 0.76/1.05/0.36/0.37 | 0.00/0.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.00/0.26/0.05 | 0.32/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.52/0.09/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.14/0.20/0.12 | 0.33/0.00/0.12/0.07 | 0.74/0.85/0.35/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.65/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.25/0.02/0.15 | 0.78/0.00/0.00/0.00 | 0.57/0.00/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.34/0.31/0.16/0.21 | 0.00/0.31/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/4.41/1.68/0.41 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.26/0.36/0.05/0.14 | 0.00/0.00/0.00/0.00 | 0.43/0.32/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.07/0.06/0.05 | 0.33/0.00/0.02/0.00 | 0.24/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.51/0.56/0.04/0.28 | 0.30/0.01/0.00/0.01 | 0.30/0.00/0.11/0.03 | 0.00/0.21/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.49 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 1.13 | 0.00 | 0.02 | 0.07 | 0.16 | 0.19 | 0.19 | 0.14 | 0.15 | 0.06 | 0.04 | 0.05 | 0.02 | 0.04 | 0.00 | 1.75 | 0.19 | 0.23 | 0.36 | 0.24 | 0.24 | 0.16 | 0.13 | 0.11 | 0.04 | 0.03 | 0.00 | 0.00 | 0.02 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 0.74 | 0.00 | 0.00 | 0.04 | 0.03 | 0.08 | 0.07 | 0.17 | 0.16 | 0.09 | 0.03 | 0.01 | 0.02 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 0 | 0 | 1 |
| 7 | 3 | 6 | 0 | 9 |
| 8 | 7 | 6 | 0 | 13 |
| 9 | 7 | 5 | 0 | 12 |
| 10 | 7 | 6 | 0 | 13 |
| 11 | 7 | 2 | 0 | 9 |
| 12 | 4 | 4 | 0 | 8 |
| 13 | 4 | 6 | 0 | 10 |
| 14 | 5 | 7 | 0 | 12 |
| 15 | 4 | 9 | 0 | 13 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 53.4% | 0.073 | 0.69 | 0.42 | 0.00 | 0.00 | 3.32 | 0.00 | 0.00 | 0.504 |
| rif_LDR04_stanca_e_smonta | 100 | 49.2% | 0.091 | 1.72 | 0.40 | 0.00 | 0.00 | 1.86 | 0.00 | 0.00 | 0.241 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 219 | 0.959 | 0.950 | 0.950 | 0.279 | 746 | 0.873 | 0.358 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 219 | 0.274 | 0.256 | 0.219 | 0.041 | 746 | 0.194 | 0.080 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 230 | 0.813 | 0.752 | 0.696 | 0.474 | 1062 | 0.677 | 0.112 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 230 | 0.174 | 0.143 | 0.096 | 0.035 | 1062 | 0.121 | 0.023 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 13.0% | 2.10 | 2.36 | 29.4% | 0.0% | 21.0% | 31.2% | 9.1% | 0.00 | 9.4% | 53.4% | 0.08 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 13.0% | 2.10 | 2.36 | 26.2% | 0.0% | 25.7% | 29.4% | 6.0% | 0.00 | 22.1% | 49.2% | 0.02 | 0.00 |
| Totale | 200 | 13.0% | 2.10 | 2.36 | 27.6% | 0.0% | 23.3% | 30.3% | 7.5% | 0.00 | 15.0% | 51.6% | 0.05 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

