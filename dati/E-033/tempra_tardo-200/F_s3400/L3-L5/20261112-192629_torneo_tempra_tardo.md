# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 855s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 33.2% [31.9–34.5] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.0] (media 10.84) | 8–11 | ✅ |
| Partite al round 13+ | 34.0% [27.8–40.8] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=86) | 17.4% [10.9–26.8] | 20–35% | ❌ |
| Attacchi con opposizione | 39.2% [37.8–40.6] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 67.3% [65.8–68.7] (con ≥3: 27.2% [25.9–28.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.7% [36.4–39.1] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 3.5% [2.0–6.2] (n=314) / 91.2% [87.5–93.9] (n=307) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.7% [14.1–17.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 50.0% [9.5–90.5] (n=2), LDR-03 Risvegliato 100.0% [98.0–100.0] (n=189), LDR-05 Base 77.8% [45.3–93.7] (n=9), LDR-05 Risvegliato 70.3% [60.3–78.7] (n=91) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 36.0% [29.5–43.1] (n=186) | | |
| Attacchi per partita | 23.7 | | |
| Pugno attaccante vuoto / pieno | 53.1% [51.7–54.6] / 11.9% [11.0–12.9] (gemme medie 0.86) | non >90% | |
| Pugno difensore vuoto / pieno | 53.6% [51.6–55.7] / 25.4% [23.6–27.2] (gemme medie 0.28) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 1205, 1: 1809, 2: 1172, 3: 391, 4: 127, 5: 32} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 182, 'crepuscolo': 18} | | |
| G1 vince fra le partite finite al Crepuscolo | 72.2% [49.1–87.5] | | |
| G1 vince fra le partite arrivate al round 15 | 72.7% [51.8–86.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 45.5% [26.9–65.3] / 30.0% [10.8–60.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 70.0% [39.7–89.2]; 13.6% [4.7–33.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 7, '2-1': 4, '2-3': 3, '1-1': 2, '2-4': 2, '0-0': 1, '2-2': 1, '2-0': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=12) | 54.5% [34.7–73.1] / 41.7% [19.3–68.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 10, 16: 2}; 41.7% [19.3–68.0] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 83.3% [55.2–95.3] / 41.7% [19.3–68.0]; 2.08 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–24.3] / 91.7% [64.6–98.5] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 71.4% [35.9–91.8]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.5% [1.1–5.7] / 22.7% [10.1–43.4]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 1, 'perd:rim': 1, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=13) / turno di G2 (n=15) | 0.0% [0.0–22.8] / 0.0% [0.0–20.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=13) | 0.0% [0.0–22.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 68.2% [47.3–83.6] (13.6% [4.7–33.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 8, 'rif_LDR03_sanguinare_per_accendere': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR05_scudi_armati 73% (n=22) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 37.0% [30.6–43.9], rif_LDR05_scudi_armati 63.0% [56.1–69.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.406 / 0.096 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.095 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.09 (0.04), rif_LDR05_scudi_armati 0.14 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 32.5% [31.2–33.9] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.21 (100 / 141); 57.5% [56.1–58.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.2% [49.2–51.2]; rif_LDR03_sanguinare_per_accendere 49.4%, rif_LDR05_scudi_armati 51.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.316 (431) / 0.323 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 74 vittorie), LDR-05 R: 18.0 (49%, 126 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 2.75, NER-017 1.15, NER-001 1.13, NER-013 1.11, NER-006 1.10, ROS-011 0.96, NER-008 0.90, BLU-015 0.73, NER-010 0.71, NER-009 0.67, ROS-019 0.63, BLU-001 0.60 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.35, rif_LDR05_scudi_armati 0.14 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 18% (n=76), rif_LDR05_scudi_armati 10% (n=10) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.9% [11.0–12.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.50, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, NEU-013 63%, NEU-009 63%, BLU-021 63%, ROS-020 63%, BLU-010 63%, collante 63%, BLU-008 63%, caccia 37%, NER-010 37%, NER-009 37%, ROS-011 37%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 37.0 [31–44] (200) |
| rif_LDR05_scudi_armati | 63.0 [56–69] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.62 | 0.00 | 0.00 / 0.00 | 2.23 | 0.00 | 4.1 (200) | 10 | K 60%, R 40% | 1.78 | 0.41 |
| rif_LDR05_scudi_armati | 3.67 | 0.00 | 2.75 / 0.00 | 0.00 | 0.58 | 4.3 (200) | 12 | B 48%, R 52% | 2.30 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.00/0.07/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.54/0.92 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/1.13/0.34/0.33 | 0.86/1.10/0.20/0.08 | 0.00/0.00/0.00/0.00 | 0.04/0.00/0.00/0.00 | 0.34/0.17/0.39/0.17 | 0.00/0.19/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.39/0.16/0.20/0.14 | 0.60/0.99/0.32/0.36 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.00/0.12/0.07 | 0.26/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.75/1.56/0.55 | 0.70/0.60/0.12/0.08 | 0.57/0.00/0.07/0.08 | 0.65/0.39/0.14/0.15 | 0.55/0.10/0.17/0.07 | 0.55/0.00/0.10/0.12 | 0.63/0.73/0.28/0.23 | 0.00/0.45/0.00/0.00 | 0.00/0.48/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.26/0.14/0.11 | 0.61/0.31/0.15/0.05 | 0.00/0.00/0.00/0.00 | 0.74/0.36/0.14/0.11 | 0.00/0.34/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.20/0.17/0.18 | 0.00/0.00/0.00/0.00 | 0.32/0.38/0.00/0.00 | 0.61/0.49/0.28/0.33 | 0.49/0.42/0.24/0.24 | 0.19/0.10/0.09/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.00/0.04/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.27/0.02/0.06/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.03/0.00 | 0.35/0.02/0.04/0.01 | 0.20/0.10/0.06/0.07 | 0.32/0.27/0.13/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.74 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.04 | 0.00 | 0.07 | 0.01 | 0.01 | 0.02 | 0.02 | 0.02 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.20 | 0.24 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 1.13 | 0.00 | 0.04 | 0.10 | 0.13 | 0.24 | 0.17 | 0.14 | 0.12 | 0.07 | 0.03 | 0.05 | 0.03 | 0.01 | 0.01 | 1.50 | 0.33 | 0.28 | 0.32 | 0.20 | 0.12 | 0.10 | 0.04 | 0.04 | 0.02 | 0.02 | 0.00 | 0.01 | 0.01 | 0.01 |
| rif_LDR05_scudi_armati | 200 | 0.69 | 0.00 | 0.01 | 0.06 | 0.09 | 0.09 | 0.07 | 0.12 | 0.12 | 0.07 | 0.01 | 0.02 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 2 | 0 | 2 |
| 7 | 9 | 11 | 0 | 20 |
| 8 | 15 | 8 | 0 | 23 |
| 9 | 25 | 10 | 0 | 35 |
| 10 | 12 | 7 | 0 | 19 |
| 11 | 12 | 10 | 0 | 22 |
| 12 | 5 | 6 | 0 | 11 |
| 13 | 13 | 11 | 0 | 24 |
| 14 | 7 | 15 | 0 | 22 |
| 15 | 15 | 4 | 0 | 19 |
| 16 | 1 | 2 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 49.4% | 0.081 | 0.79 | 0.56 | 0.00 | 0.00 | 4.16 | 0.00 | 0.00 | 0.486 |
| rif_LDR05_scudi_armati | 200 | 51.1% | 0.107 | 0.14 | 0.00 | 0.00 | 0.00 | 2.73 | 0.00 | 0.00 | 0.344 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 434 | 0.912 | 0.899 | 0.882 | 0.343 | 1618 | 0.849 | 0.341 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 434 | 0.343 | 0.313 | 0.265 | 0.039 | 1618 | 0.316 | 0.111 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 603 | 0.867 | 0.844 | 0.834 | 0.430 | 2081 | 0.780 | 0.173 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 603 | 0.174 | 0.159 | 0.154 | 0.048 | 2081 | 0.169 | 0.044 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 9.0% | 2.10 | 1.97 | 27.7% | 0.0% | 17.8% | 32.3% | 11.3% | 0.00 | 14.6% | 49.4% | 0.14 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 9.0% | 2.10 | 1.97 | 43.8% | 0.0% | 17.2% | 30.9% | 11.0% | 0.00 | 21.9% | 51.1% | 0.05 | 0.00 |
| Totale | 400 | 9.0% | 2.10 | 1.97 | 34.6% | 0.0% | 17.5% | 31.6% | 11.2% | 0.00 | 18.0% | 50.2% | 0.09 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

