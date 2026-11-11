# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 810s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 33.4% [31.6–35.4] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [9.5–12.0] (media 10.91) | 8–11 | ✅ |
| Partite al round 13+ | 38.0% [29.1–47.8] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=43) | 16.3% [8.1–30.0] | 20–35% | ❌ |
| Attacchi con opposizione | 39.7% [37.7–41.7] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 68.1% [66.1–70.0] (con ≥3: 28.3% [26.4–30.2]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.4% [35.4–39.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.4% [2.1–8.8] (n=159) / 92.9% [87.7–96.0] (n=154) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 16.1% [13.8–18.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 50.0% [9.5–90.5] (n=2), LDR-03 Risvegliato 100.0% [96.1–100.0] (n=95), LDR-05 Base 80.0% [37.6–96.4] (n=5), LDR-05 Risvegliato 77.1% [63.5–86.7] (n=48) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 40.7% [31.1–50.9] (n=91) | | |
| Attacchi per partita | 23.7 | | |
| Pugno attaccante vuoto / pieno | 53.0% [50.9–55.1] / 11.3% [10.1–12.7] (gemme medie 0.88) | non >90% | |
| Pugno difensore vuoto / pieno | 53.2% [50.3–56.1] / 25.5% [23.1–28.2] (gemme medie 0.28) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 574, 1: 931, 2: 601, 3: 187, 4: 63, 5: 18} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 90, 'crepuscolo': 10} | | |
| G1 vince fra le partite finite al Crepuscolo | 70.0% [39.7–89.2] | | |
| G1 vince fra le partite arrivate al round 15 | 72.7% [43.4–90.3] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 54.5% [28.0–78.7] / 33.3% [9.7–70.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 66.7% [30.0–90.3]; 9.1% [1.6–37.7] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 4, '2-1': 3, '2-3': 1, '1-1': 1, '0-0': 1, '2-4': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=7) | 63.6% [35.4–84.8] / 42.9% [15.8–75.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 6, 16: 1}; 42.9% [15.8–75.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 71.4% [35.9–91.8] / 28.6% [8.2–64.1]; 1.86 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–35.4] / 85.7% [48.7–97.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 50.0% [15.0–85.0]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.0–8.5] / 27.3% [9.7–56.6]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 1, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=5) / turno di G2 (n=7) | 0.0% [0.0–43.4] / 0.0% [0.0–35.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=5) | 0.0% [0.0–43.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 63.6% [35.4–84.8] (9.1% [1.6–37.7]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 5, 'rif_LDR03_sanguinare_per_accendere': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR05_scudi_armati 73% (n=11) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 36.0% [27.3–45.8], rif_LDR05_scudi_armati 64.0% [54.2–72.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.404 / 0.096 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.094 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.09 (0.03), rif_LDR05_scudi_armati 0.14 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 32.7% [30.8–34.6] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.42 (64 / 78); 56.4% [54.4–58.4] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.4% [50.0–52.8]; rif_LDR03_sanguinare_per_accendere 50.8%, rif_LDR05_scudi_armati 52.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.309 (218) / 0.324 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 36 vittorie), LDR-05 R: 18.0 (49%, 64 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 2.57, NER-017 1.50, NER-013 1.29, ROS-011 1.11, NER-006 1.00, NER-001 1.00, NER-008 0.92, BLU-015 0.80, NER-010 0.73, NER-009 0.73, ROS-019 0.61, BLU-001 0.60 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.43, rif_LDR05_scudi_armati 0.09 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 16% (n=37), rif_LDR05_scudi_armati 17% (n=6) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.3% [10.1–12.7] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.51, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, BLU-021 64%, NEU-013 64%, NEU-009 64%, collante 64%, ROS-020 64%, BLU-010 64%, BLU-008 64%, ROS-011 36%, caccia 36%, NER-010 36%, NER-017 36%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 36.0 [27–46] (100) |
| rif_LDR05_scudi_armati | 64.0 [54–73] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.61 | 0.00 | 0.00 / 0.00 | 2.20 | 0.00 | 4.0 (100) | 10 | K 60%, R 40% | 1.71 | 0.40 |
| rif_LDR05_scudi_armati | 3.79 | 0.00 | 2.57 / 0.00 | 0.00 | 0.51 | 4.1 (100) | 12 | B 48%, R 52% | 2.28 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.00/0.08/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.47/0.88 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/1.00/0.34/0.25 | 0.84/1.00/0.14/0.08 | 0.00/0.00/0.00/0.00 | 0.06/0.00/0.00/0.00 | 0.29/0.16/0.34/0.16 | 0.00/0.15/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.03/0.02 | 0.00/0.00/0.00/0.00 | 0.40/0.16/0.21/0.14 | 0.59/1.00/0.30/0.41 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.12/0.09 | 0.23/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.57/1.66/0.48 | 0.72/0.60/0.13/0.10 | 0.50/0.00/0.09/0.03 | 0.65/0.33/0.13/0.12 | 0.53/0.11/0.21/0.08 | 0.62/0.00/0.08/0.11 | 0.63/0.80/0.29/0.24 | 0.00/0.47/0.00/0.00 | 0.00/0.58/0.00/0.00 | 0.00/0.11/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.22/0.14/0.05 | 0.59/0.28/0.15/0.03 | 0.00/0.00/0.00/0.00 | 0.72/0.35/0.13/0.10 | 0.00/0.37/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.22/0.13/0.18 | 0.00/0.00/0.00/0.00 | 0.27/0.31/0.00/0.00 | 0.59/0.45/0.21/0.30 | 0.56/0.46/0.25/0.24 | 0.20/0.12/0.08/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.00/0.04/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.26/0.01/0.05/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.01/0.00 | 0.35/0.03/0.04/0.01 | 0.21/0.10/0.07/0.06 | 0.33/0.23/0.11/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.87 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.05 | 0.00 | 0.07 | 0.01 | 0.00 | 0.02 | 0.01 | 0.01 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.16 | 0.00 | 0.00 | 0.19 | 0.26 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 1.01 | 0.00 | 0.03 | 0.10 | 0.18 | 0.22 | 0.14 | 0.10 | 0.09 | 0.04 | 0.03 | 0.04 | 0.02 | 0.02 | 0.00 | 1.51 | 0.26 | 0.31 | 0.38 | 0.18 | 0.14 | 0.10 | 0.04 | 0.02 | 0.04 | 0.01 | 0.00 | 0.00 | 0.01 | 0.02 |
| rif_LDR05_scudi_armati | 100 | 0.66 | 0.00 | 0.02 | 0.04 | 0.06 | 0.07 | 0.08 | 0.09 | 0.14 | 0.08 | 0.03 | 0.02 | 0.02 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 1 | 0 | 1 |
| 7 | 4 | 5 | 0 | 9 |
| 8 | 9 | 6 | 0 | 15 |
| 9 | 10 | 5 | 0 | 15 |
| 10 | 5 | 4 | 0 | 9 |
| 11 | 2 | 6 | 0 | 8 |
| 12 | 1 | 4 | 0 | 5 |
| 13 | 6 | 9 | 0 | 15 |
| 14 | 3 | 9 | 0 | 12 |
| 15 | 8 | 2 | 0 | 10 |
| 16 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 50.8% | 0.073 | 0.74 | 0.69 | 0.00 | 0.00 | 4.43 | 0.00 | 0.00 | 0.484 |
| rif_LDR05_scudi_armati | 100 | 52.1% | 0.112 | 0.09 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 | 0.00 | 0.345 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 210 | 0.924 | 0.910 | 0.900 | 0.310 | 797 | 0.816 | 0.326 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 210 | 0.352 | 0.329 | 0.286 | 0.043 | 797 | 0.351 | 0.133 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 323 | 0.839 | 0.817 | 0.811 | 0.430 | 1044 | 0.751 | 0.162 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 323 | 0.192 | 0.176 | 0.170 | 0.043 | 1044 | 0.156 | 0.040 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 100 | 10.0% | 2.22 | 2.18 | 26.7% | 0.0% | 18.7% | 33.2% | 12.1% | 0.00 | 13.5% | 50.8% | 0.18 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 10.0% | 2.22 | 2.18 | 41.7% | 0.0% | 17.7% | 31.2% | 11.6% | 0.00 | 22.7% | 52.1% | 0.03 | 0.00 |
| Totale | 200 | 10.0% | 2.22 | 2.18 | 32.5% | 0.0% | 18.2% | 32.2% | 11.9% | 0.00 | 17.7% | 51.4% | 0.10 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

