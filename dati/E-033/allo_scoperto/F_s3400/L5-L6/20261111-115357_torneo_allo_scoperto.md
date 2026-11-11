# Torneo v0.2 — /home/claude/e033_in/varianti/allo_scoperto.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/allo_scoperto.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'allo_scoperto': True}
- IA: forte:30; partite: 100; tempo 891s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 34.2% [32.3–36.1] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–12.0] (media 11.07) | 8–11 | ✅ |
| Partite al round 13+ | 35.0% [26.4–44.7] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.2–5.4] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=42) | 16.7% [8.3–30.6] | 20–35% | ❌ |
| Attacchi con opposizione | 28.8% [27.1–30.7] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 60.7% [58.6–62.7] (con ≥3: 22.6% [20.9–24.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.7% [35.9–39.7] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 16.3% [12.0–21.7] (n=221) / 91.1% [85.4–94.7] (n=146) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.3% [12.2–16.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-05 Base 55.6% [39.6–70.5] (n=36), LDR-05 Risvegliato 75.6% [61.3–85.8] (n=45), LDR-06 Risvegliato 64.8% [54.4–73.9] (n=88) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 41.1% [30.5–52.6] (n=73) | | |
| Attacchi per partita | 24.7 | | |
| Pugno attaccante vuoto / pieno | 55.3% [53.3–57.4] / 11.9% [10.6–13.3] (gemme medie 0.75) | non >90% | |
| Pugno difensore vuoto / pieno | 55.4% [52.5–58.2] / 26.6% [24.1–29.2] (gemme medie 0.25) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 840, 1: 837, 2: 564, 3: 148, 4: 59, 5: 20, 6: 4} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 94, 'crepuscolo': 6} | | |
| G1 vince fra le partite finite al Crepuscolo | 66.7% [30.0–90.3] | | |
| G1 vince fra le partite arrivate al round 15 | 45.5% [21.3–72.0] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 18.2% [5.1–47.7] / 50.0% [9.5–90.5] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [9.5–90.5]; 9.1% [1.6–37.7] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 3, '2-1': 2, '1-2': 1, '3-3': 1, '2-3': 1, '1-0': 1, '3-2': 1, '1-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=3) | 27.3% [9.7–56.6] / 33.3% [6.1–79.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 2, 16: 1}; 33.3% [6.1–79.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 100.0% [43.8–100.0] / 66.7% [20.8–93.9]; 3.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–56.2] / 100.0% [43.8–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=1) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–79.3] / 100.0% [34.2–100.0]; 0.0% [0.0–79.3] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.0% [0.2–5.4] / 9.1% [1.6–37.7]; 100.0% [20.7–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 1, 'vinc:atk': 1} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=7) / turno di G2 (n=8) | 0.0% [0.0–35.4] / 0.0% [0.0–32.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=7) | 0.0% [0.0–35.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 54.5% [28.0–78.7] (18.2% [5.1–47.7]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 2, 'rif_LDR06_ferite_e_caccia': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR05_scudi_armati vs rif_LDR06_ferite_e_caccia 45% (n=11) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR05_scudi_armati 75.0% [65.7–82.5], rif_LDR06_ferite_e_caccia 25.0% [17.5–34.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.401 / 0.087 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.086 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR05_scudi_armati 0.15 (0.00), rif_LDR06_ferite_e_caccia 0.09 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 33.6% [31.7–35.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.97 (114 / 283); 59.2% [57.3–61.1] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 49.2% [47.7–50.7]; rif_LDR05_scudi_armati 54.3%, rif_LDR06_ferite_e_caccia 43.9% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.330 (176) / 0.332 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-05 R: 18.0 (49%, 75 vittorie), LDR-06 G: 17.0 (49%, 25 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 2.99, LDR-05 2.92, VER-020 2.16, VER-008 1.19, NER-017 1.03, NER-009 0.76, NER-013 0.61, BLU-015 0.60, VER-001 0.57, NEU-001 0.50, NEU-012 0.50, BLU-021 0.48 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR05_scudi_armati 0.08, rif_LDR06_ferite_e_caccia 3.09 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.18 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR05_scudi_armati 50% (n=8), rif_LDR06_ferite_e_caccia 9% (n=34) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.9% [10.6–13.3] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.80; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, collante 100%, BLU-008 75%, NEU-009 75%, BLU-010 75%, ROS-020 75%, NEU-013 75%, BLU-021 75%, NER-015 25%, VER-001 25%, VER-023 25%, NER-017 25%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR05_scudi_armati | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR05_scudi_armati | — | 75.0 [66–82] (100) |
| rif_LDR06_ferite_e_caccia | 25.0 [18–34] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 4.03 | 0.00 | 2.92 / 0.00 | 0.00 | 0.88 | 4.5 (99) | 13 | B 48%, R 52% | 2.21 | 0.00 |
| rif_LDR06_ferite_e_caccia | 3.91 | 0.00 | 2.99 / 0.05 | 0.00 | 0.22 | 4.8 (96) | 9 | G 57%, K 43% | 2.22 | 1.18 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/2.92/1.98/0.41 | 0.79/0.38/0.22/0.06 | 0.62/0.00/0.09/0.07 | 0.60/0.36/0.17/0.10 | 0.58/0.18/0.35/0.15 | 0.74/0.00/0.28/0.12 | 0.71/0.60/0.28/0.22 | 0.00/0.48/0.00/0.00 | 0.00/0.42/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.44/0.30/0.14 | 0.75/0.26/0.11/0.03 | 0.00/0.00/0.00/0.00 | 0.61/0.22/0.10/0.03 | 0.00/0.41/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.22/0.43/0.11 | 0.00/0.00/0.00/0.00 | 0.32/0.45/0.00/0.00 | 0.61/0.33/0.34/0.17 | 0.44/0.26/0.20/0.18 | 0.25/0.09/0.30/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.00/0.03/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.10/0.10/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.00/0.02/0.00 | 0.39/0.03/0.00/0.02 | 0.30/0.13/0.14/0.13 | 0.33/0.16/0.10/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.57/0.04/0.34 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.35/0.57/0.25 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.99/1.69/0.76 | 0.00/0.00/0.00/0.00 | 0.62/0.00/0.00/0.00 | 0.22/0.32/0.03/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.37/0.13/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.19/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.13/0.27/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.37/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.50/0.04/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/1.19/0.00/0.53 | 0.36/0.03/0.06/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.50/0.13/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.93 | 0.00 | 0.09 | 0.00 | 0.01 | 0.02 | 0.05 | 0.01 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.18 | 0.00 | 0.00 | 0.10 | 0.16 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.50 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 0.60 | 0.00 | 0.00 | 0.02 | 0.04 | 0.07 | 0.08 | 0.05 | 0.11 | 0.06 | 0.08 | 0.06 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 1.02 | 0.00 | 0.03 | 0.01 | 0.12 | 0.21 | 0.16 | 0.17 | 0.07 | 0.10 | 0.02 | 0.10 | 0.02 | 0.01 | 0.80 | 0.11 | 0.16 | 0.15 | 0.09 | 0.06 | 0.09 | 0.05 | 0.04 | 0.00 | 0.02 | 0.02 | 0.01 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 3 | 0 | 3 |
| 6 | 1 | 0 | 0 | 1 |
| 7 | 1 | 0 | 0 | 1 |
| 8 | 6 | 7 | 0 | 13 |
| 9 | 4 | 8 | 0 | 12 |
| 10 | 8 | 5 | 0 | 13 |
| 11 | 8 | 5 | 0 | 13 |
| 12 | 5 | 4 | 0 | 9 |
| 13 | 7 | 9 | 0 | 16 |
| 14 | 2 | 6 | 0 | 8 |
| 15 | 4 | 6 | 0 | 10 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 54.3% | 0.109 | 0.08 | 0.00 | 0.00 | 0.00 | 2.29 | 0.00 | 0.00 | 0.361 |
| rif_LDR06_ferite_e_caccia | 100 | 43.9% | 0.064 | 0.94 | 2.15 | 0.00 | 0.00 | 4.65 | 0.00 | 0.00 | 0.445 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | mano | 318 | 0.868 | 0.858 | 0.858 | 0.396 | 980 | 0.768 | 0.188 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 318 | 0.138 | 0.129 | 0.113 | 0.047 | 980 | 0.131 | 0.034 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 191 | 0.942 | 0.916 | 0.885 | 0.346 | 983 | 0.890 | 0.336 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 191 | 0.277 | 0.257 | 0.225 | 0.047 | 983 | 0.194 | 0.089 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 100 | 6.0% | 2.09 | 1.57 | 57.6% | 3.0% | 26.0% | 28.5% | 10.9% | 0.00 | 15.8% | 54.3% | 0.04 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 6.0% | 2.09 | 1.57 | 18.4% | 3.0% | 25.7% | 31.3% | 6.1% | 0.00 | 13.2% | 43.9% | 0.07 | 0.00 |
| Totale | 200 | 6.0% | 2.09 | 1.57 | 29.2% | 3.0% | 25.8% | 29.9% | 8.1% | 0.00 | 14.5% | 49.2% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

