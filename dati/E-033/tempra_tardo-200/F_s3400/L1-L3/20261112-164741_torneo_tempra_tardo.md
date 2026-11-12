# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 787s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 30.5% [29.2–31.9] | 30–45% | ✅ |
| Durata mediana (round) | 10.0 [10.0–11.0] (media 10.53) | 8–11 | ✅ |
| Partite al round 13+ | 27.0% [21.3–33.5] | ≤12% | ❌ |
| Partite oltre il 15 | 0.5% [0.1–2.8] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=98) | 22.4% [15.3–31.7] | 20–35% | ✅ |
| Attacchi con opposizione | 33.9% [32.5–35.2] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 63.4% [61.9–64.9] (con ≥3: 22.4% [21.1–23.7]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.2% [37.8–40.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 5.5% [3.5–8.4] (n=347) / 87.7% [83.8–90.8] (n=341) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 16.0% [14.4–17.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 78.6% [52.4–92.4] (n=14), LDR-01 Risvegliato 64.8% [54.6–73.9] (n=91), LDR-03 Base 60.0% [23.1–88.2] (n=5), LDR-03 Risvegliato 100.0% [98.2–100.0] (n=208) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 28.0% [22.0–34.8] (n=186) | | |
| Attacchi per partita | 23.8 | | |
| Pugno attaccante vuoto / pieno | 54.2% [52.7–55.7] / 12.5% [11.6–13.5] (gemme medie 0.82) | non >90% | |
| Pugno difensore vuoto / pieno | 56.4% [54.3–58.5] / 24.6% [22.8–26.4] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 1331, 1: 1747, 2: 1137, 3: 383, 4: 131, 5: 35} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 188, 'crepuscolo': 12} | | |
| G1 vince fra le partite finite al Crepuscolo | 50.0% [25.4–74.6] | | |
| G1 vince fra le partite arrivate al round 15 | 53.8% [29.1–76.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 46.2% [23.2–70.9] / 50.0% [18.8–81.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [18.8–81.2]; 7.7% [1.4–33.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 3, '0-0': 2, '2-1': 2, '5-2': 1, '3-1': 1, '1-1': 1, '0-2': 1, '1-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=7) | 53.8% [29.1–76.8] / 57.1% [25.0–84.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 6, 16: 1}; 57.1% [25.0–84.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 57.1% [25.0–84.2] / 42.9% [15.8–75.0]; 2.57 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–35.4] / 85.7% [48.7–97.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=4) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–49.0] / 100.0% [43.8–100.0]; 0.0% [0.0–49.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.8–5.0] / 30.8% [12.7–57.6]; 100.0% [51.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 1, 'vinc:atk': 4} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=4) / turno di G2 (n=2) | 0.0% [0.0–49.0] / 0.0% [0.0–65.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=4) | 0.0% [0.0–49.0] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 53.8% [29.1–76.8] (15.4% [4.3–42.2]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR03_sanguinare_per_accendere': 4, 'rif_LDR01_puntata_e_preda': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR03_sanguinare_per_accendere 54% (n=13) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 58.5% [51.6–65.1], rif_LDR03_sanguinare_per_accendere 41.5% [34.9–48.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.380 / 0.079 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.079 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.12 (0.00), rif_LDR03_sanguinare_per_accendere 0.12 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 34.3% [33.0–35.7] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.39 (181 / 297); 59.6% [58.1–60.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 47.4% [46.4–48.5]; rif_LDR01_puntata_e_preda 45.4%, rif_LDR03_sanguinare_per_accendere 49.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.365 (485) / 0.345 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 117 vittorie), LDR-03 R: 14.0 (35%, 83 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-01 1.61, NER-017 1.51, NER-001 1.31, ROS-019 1.11, NER-008 1.00, ROS-016 0.98, ROS-011 0.94, NER-006 0.92, NER-013 0.77, ROS-018 0.76, NER-009 0.64, VER-019 0.56 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.64, rif_LDR03_sanguinare_per_accendere 1.39 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.06, rif_LDR03_sanguinare_per_accendere 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 27% (n=11), rif_LDR03_sanguinare_per_accendere 22% (n=87) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.5% [11.6–13.5] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR03_sanguinare_per_accendere 1.40; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | caccia 100%, ponte 100%, ROS-016 58%, VER-008 58%, VER-011 58%, VER-001 58%, NER-010 42%, NER-017 42%, NER-009 42%, ROS-011 42%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR03_sanguinare_per_accendere |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 58.5 [52–65] (200) |
| rif_LDR03_sanguinare_per_accendere | 41.5 [35–48] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.81 | 0.00 | 1.61 / 0.00 | 0.00 | 0.00 | 3.9 (199) | 13 | G 39%, R 61% | 2.75 | 0.53 |
| rif_LDR03_sanguinare_per_accendere | 3.54 | 0.00 | 0.00 / 0.00 | 2.17 | 0.00 | 4.3 (199) | 8 | K 62%, R 38% | 1.74 | 0.53 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.61/1.69/0.57 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.46/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.41/0.20/0.07 | 0.69/0.15/0.51/0.32 | 0.77/0.44/0.18/0.10 | 0.00/0.35/0.00/0.00 | 0.67/0.00/0.12/0.04 | 0.61/0.16/0.19/0.07 | 0.72/0.98/0.04/0.43 | 0.69/0.76/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.41/0.23/0.19 | 0.20/0.10/0.12/0.13 | 0.00/0.00/0.00/0.00 | 0.65/0.41/0.07/0.34 | 0.64/0.00/0.00/0.00 | 0.60/0.00/0.10/0.07 | 0.64/0.40/0.15/0.05 | 0.67/0.56/0.34/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.00/0.06/0.01 | 0.38/0.03/0.06/0.03 | 0.32/0.07/0.05/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.02/0.02 | 0.29/0.37/0.01/0.19 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.09/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.75/0.80 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/1.31/0.49/0.41 | 0.77/0.92/0.14/0.06 | 0.00/0.00/0.00/0.00 | 0.01/0.00/0.00/0.00 | 0.38/0.23/0.36/0.23 | 0.00/0.24/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.33/0.09/0.17/0.07 | 0.62/1.11/0.37/0.32 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.09/0.01 | 0.32/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.07 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.17 | 0.02 | 0.00 | 0.01 | 0.09 | 0.12 | 0.00 | 0.00 | 0.21 | 0.10 | 0.00 | 0.01 | 0.00 | 0.01 | 0.03 | 0.17 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.65 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.03 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.51 | 0.00 | 0.02 | 0.04 | 0.04 | 0.04 | 0.10 | 0.06 | 0.08 | 0.07 | 0.04 | 0.02 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 200 | 1.15 | 0.00 | 0.04 | 0.09 | 0.17 | 0.13 | 0.20 | 0.16 | 0.12 | 0.09 | 0.04 | 0.04 | 0.04 | 0.04 | 0.00 | 1.40 | 0.29 | 0.22 | 0.34 | 0.19 | 0.12 | 0.09 | 0.06 | 0.04 | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 4 | 0 | 4 |
| 6 | 4 | 4 | 0 | 8 |
| 7 | 6 | 4 | 0 | 10 |
| 8 | 17 | 10 | 0 | 27 |
| 9 | 14 | 11 | 0 | 25 |
| 10 | 19 | 10 | 0 | 29 |
| 11 | 9 | 18 | 0 | 27 |
| 12 | 7 | 9 | 0 | 16 |
| 13 | 12 | 11 | 0 | 23 |
| 14 | 8 | 10 | 0 | 18 |
| 15 | 7 | 5 | 0 | 12 |
| 16 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 45.4% | 0.078 | 0.00 | 0.64 | 0.00 | 0.00 | 2.92 | 0.00 | 0.00 | 0.292 |
| rif_LDR03_sanguinare_per_accendere | 200 | 49.1% | 0.081 | 0.68 | 0.71 | 0.00 | 0.00 | 4.28 | 0.00 | 0.00 | 0.485 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 505 | 0.806 | 0.756 | 0.729 | 0.352 | 2078 | 0.705 | 0.142 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 505 | 0.186 | 0.164 | 0.152 | 0.046 | 2078 | 0.141 | 0.051 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | mano | 450 | 0.929 | 0.909 | 0.891 | 0.336 | 1731 | 0.889 | 0.358 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 450 | 0.293 | 0.287 | 0.276 | 0.056 | 1731 | 0.272 | 0.110 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 6.0% | 1.98 | 1.95 | 38.7% | 2.0% | 15.8% | 26.6% | 3.0% | 0.00 | 21.1% | 45.4% | 0.09 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 200 | 6.0% | 1.98 | 1.95 | 30.7% | 2.0% | 17.5% | 30.8% | 11.6% | 0.00 | 13.8% | 49.1% | 0.05 | 0.00 |
| Totale | 400 | 6.0% | 1.98 | 1.95 | 34.3% | 2.0% | 16.7% | 28.7% | 7.9% | 0.00 | 17.1% | 47.4% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

