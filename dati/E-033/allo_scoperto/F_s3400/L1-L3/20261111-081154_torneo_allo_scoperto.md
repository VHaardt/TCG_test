# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 633s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 28.3% [26.5–30.1] | 30–45% | ❌ |
| Durata mediana (round) | 9.0 [9.0–11.0] (media 10.13) | 8–11 | ✅ |
| Partite al round 13+ | 24.0% [16.7–33.2] | ≤12% | ❌ |
| Partite oltre il 15 | 0.0% [0.0–3.7] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=42) | 26.2% [15.3–41.1] | 20–35% | ✅ |
| Attacchi con opposizione | 33.5% [31.5–35.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 62.7% [60.5–64.8] (con ≥3: 21.9% [20.1–23.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 41.7% [39.7–43.7] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 5.9% [3.4–10.3] (n=185) / 87.4% [81.4–91.7] (n=159) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.7% [12.6–17.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 50.0% [18.8–81.2] (n=6), LDR-01 Risvegliato 50.9% [37.9–63.9] (n=53), LDR-03 Base 60.0% [23.1–88.2] (n=5), LDR-03 Risvegliato 100.0% [95.7–100.0] (n=86) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 24.7% [17.1–34.4] (n=93) | | |
| Attacchi per partita | 22.8 | | |
| Pugno attaccante vuoto / pieno | 51.0% [48.8–53.2] / 13.6% [12.2–15.2] (gemme medie 0.86) | non >90% | |
| Pugno difensore vuoto / pieno | 58.3% [55.2–61.3] / 24.3% [21.7–27.1] (gemme medie 0.24) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 614, 1: 863, 2: 534, 3: 189, 4: 55, 5: 19, 6: 1} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 95, 'crepuscolo': 5} | | |
| G1 vince fra le partite finite al Crepuscolo | 60.0% [23.1–88.2] | | |
| G1 vince fra le partite arrivate al round 15 | 55.6% [26.7–81.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 0.0% [0.0–29.9] / nan% [nan–nan] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | nan% [nan–nan]; 0.0% [0.0–29.9] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 2, '2-0': 2, '2-1': 1, '1-2': 1, '3-3': 1, '1-3': 1, '2-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=0) | 0.0% [0.0–29.9] / nan% [nan–nan] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {}; nan% [nan–nan] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | nan% [nan–nan] / nan% [nan–nan]; nan | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | nan% [nan–nan] / nan% [nan–nan] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=nan) / a Vite diverse; nessuno attacca a Vite pari | nan% [nan–nan] / nan% [nan–nan]; nan% [nan–nan] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 0.0% [0.0–3.7] / 0.0% [0.0–29.9]; nan% [nan–nan] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=3) / turno di G2 (n=2) | 0.0% [0.0–56.2] / 0.0% [0.0–65.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=3) | 0.0% [0.0–56.2] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 44.4% [18.9–73.3] (11.1% [2.0–43.5]) | | |
| Q-019: vincitori degli spareggi per mazzo | {} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR03_sanguinare_per_accendere 56% (n=9) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 54.0% [44.3–63.4], rif_LDR03_sanguinare_per_accendere 46.0% [36.6–55.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.361 / 0.070 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.070 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.08 (0.00), rif_LDR03_sanguinare_per_accendere 0.07 (0.02) | |
| M4 | Scontri decisi prima dell'impegno | 35.6% [33.7–37.6] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.05 (66 / 139); 60.2% [58.2–62.2] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 47.1% [45.6–48.7]; rif_LDR01_puntata_e_preda 44.2%, rif_LDR03_sanguinare_per_accendere 49.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.348 (200) / 0.332 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 54 vittorie), LDR-03 R: 14.0 (35%, 46 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-01 1.51, NER-001 1.37, NER-017 1.13, NER-006 1.11, ROS-011 1.04, ROS-016 1.02, NER-008 0.98, NER-013 0.88, ROS-019 0.82, ROS-018 0.72, NER-010 0.58, NER-009 0.56 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.55, rif_LDR03_sanguinare_per_accendere 1.30 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR03_sanguinare_per_accendere 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 20% (n=5), rif_LDR03_sanguinare_per_accendere 27% (n=37) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.6% [12.2–15.2] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR03_sanguinare_per_accendere 1.30; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | caccia 100%, ponte 100%, VER-011 54%, VER-008 54%, VER-001 54%, ROS-016 54%, NER-010 46%, NER-009 46%, ROS-011 46%, NER-017 46%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR03_sanguinare_per_accendere |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 54.0 [44–63] (100) |
| rif_LDR03_sanguinare_per_accendere | 46.0 [37–56] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.70 | 0.00 | 1.51 / 0.00 | 0.00 | 0.00 | 3.8 (100) | 13 | G 40%, R 60% | 2.80 | 0.61 |
| rif_LDR03_sanguinare_per_accendere | 3.32 | 0.00 | 0.00 / 0.00 | 2.40 | 0.00 | 4.2 (100) | 8 | K 62%, R 38% | 1.79 | 0.52 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.51/1.80/0.54 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.39/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.46/0.18/0.10 | 0.62/0.16/0.48/0.33 | 0.63/0.26/0.16/0.04 | 0.00/0.37/0.00/0.00 | 0.54/0.00/0.13/0.05 | 0.60/0.22/0.18/0.09 | 0.71/1.02/0.11/0.42 | 0.68/0.72/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.32/0.15/0.20 | 0.22/0.12/0.10/0.17 | 0.00/0.00/0.00/0.00 | 0.63/0.41/0.07/0.33 | 0.59/0.00/0.00/0.00 | 0.59/0.00/0.08/0.09 | 0.57/0.42/0.16/0.08 | 0.67/0.50/0.46/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.50/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.00/0.02/0.01 | 0.34/0.02/0.02/0.02 | 0.33/0.03/0.14/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.03/0.02 | 0.31/0.25/0.01/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.12/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.64/0.89 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/1.37/0.54/0.30 | 0.80/1.11/0.15/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.12/0.31/0.12 | 0.00/0.24/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.04/0.02 | 0.00/0.00/0.00/0.00 | 0.33/0.08/0.17/0.08 | 0.49/0.82/0.35/0.20 | 0.00/0.05/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.04/0.06 | 0.26/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.05 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.17 | 0.00 | 0.00 | 0.00 | 0.11 | 0.14 | 0.00 | 0.00 | 0.16 | 0.12 | 0.00 | 0.01 | 0.00 | 0.01 | 0.03 | 0.19 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.59 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.61 | 0.00 | 0.02 | 0.03 | 0.06 | 0.06 | 0.08 | 0.12 | 0.07 | 0.10 | 0.01 | 0.05 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 100 | 1.18 | 0.00 | 0.02 | 0.06 | 0.16 | 0.18 | 0.21 | 0.15 | 0.12 | 0.12 | 0.07 | 0.03 | 0.02 | 0.01 | 0.03 | 1.30 | 0.28 | 0.19 | 0.26 | 0.19 | 0.12 | 0.10 | 0.09 | 0.01 | 0.01 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 4 | 0 | 4 |
| 7 | 4 | 10 | 0 | 14 |
| 8 | 10 | 5 | 0 | 15 |
| 9 | 7 | 11 | 0 | 18 |
| 10 | 6 | 1 | 0 | 7 |
| 11 | 6 | 6 | 0 | 12 |
| 12 | 3 | 3 | 0 | 6 |
| 13 | 3 | 7 | 0 | 10 |
| 14 | 2 | 3 | 0 | 5 |
| 15 | 5 | 4 | 0 | 9 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 44.2% | 0.074 | 0.00 | 0.55 | 0.00 | 0.00 | 2.81 | 0.00 | 0.00 | 0.276 |
| rif_LDR03_sanguinare_per_accendere | 100 | 49.5% | 0.066 | 0.64 | 0.66 | 0.00 | 0.00 | 4.03 | 0.00 | 0.00 | 0.460 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 204 | 0.892 | 0.828 | 0.789 | 0.402 | 1019 | 0.732 | 0.151 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 204 | 0.196 | 0.172 | 0.157 | 0.039 | 1019 | 0.175 | 0.044 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | mano | 208 | 0.952 | 0.923 | 0.904 | 0.298 | 844 | 0.893 | 0.333 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 208 | 0.216 | 0.202 | 0.188 | 0.034 | 844 | 0.264 | 0.092 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 5.0% | 1.81 | 1.60 | 33.9% | 0.0% | 18.7% | 26.0% | 4.5% | 0.00 | 20.7% | 44.2% | 0.11 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 100 | 5.0% | 1.81 | 1.60 | 36.5% | 0.0% | 16.3% | 29.4% | 10.0% | 0.00 | 13.6% | 49.5% | 0.05 | 0.00 |
| Totale | 200 | 5.0% | 1.81 | 1.60 | 35.3% | 0.0% | 17.5% | 27.7% | 7.7% | 0.00 | 16.8% | 47.1% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

