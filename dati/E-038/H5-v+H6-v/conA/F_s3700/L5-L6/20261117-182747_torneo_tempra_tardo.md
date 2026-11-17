# Torneo v0.2 — /home/claude/e038_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e038_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1796s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 35.3% [34.0–36.7] | 30–45% | ✅ |
| Durata mediana (round) | 11.5 [11.0–12.5] (media 11.63) | 8–11 | ❌ |
| Partite al round 13+ | 43.0% [36.3–49.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.3–3.6] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=80) | 40.0% [30.0–51.0] | 20–35% | ❌ |
| Attacchi con opposizione | 29.8% [28.5–31.1] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 65.5% [64.1–66.9] (con ≥3: 28.0% [26.7–29.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.6% [35.3–38.0] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 6.6% [4.4–9.8] (n=332) / 90.3% [86.5–93.1] (n=319) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 16.3% [14.7–18.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-05 Base 37.5% [18.5–61.4] (n=16), LDR-05 Risvegliato 72.7% [64.4–79.6] (n=128), LDR-06 Base 33.3% [9.7–70.0] (n=6), LDR-06 Risvegliato 66.2% [58.6–73.1] (n=160) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 43.8% [36.6–51.1] (n=176) | | |
| Attacchi per partita | 24.1 | | |
| Pugno attaccante vuoto / pieno | 55.6% [54.1–57.1] / 10.3% [9.5–11.3] (gemme medie 0.77) | non >90% | |
| Pugno difensore vuoto / pieno | 54.0% [51.9–56.0] / 27.6% [25.8–29.5] (gemme medie 0.28) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1467, 1: 1718, 2: 1119, 3: 330, 4: 131, 5: 51, 6: 4} | | |
| Azioni legali per decisione | 5.9 | <60 | ✅ |
| Fine partita | {'colpo_finale': 176, 'crepuscolo': 24} | | |
| G1 vince fra le partite finite al Crepuscolo | 62.5% [42.7–78.8] | | |
| G1 vince fra le partite arrivate al round 15 | 58.8% [42.2–73.6] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 29.4% [16.8–46.2] / 40.0% [16.8–68.7] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [23.7–76.3]; 5.9% [1.6–19.1] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 5, '1-0': 5, '2-3': 4, '0-0': 3, '2-1': 3, '2-0': 3, '1-3': 2, '3-1': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=11) | 32.4% [19.1–49.2] / 45.5% [21.3–72.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 10, 16: 1}; 54.5% [28.0–78.7] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 63.6% [35.4–84.8] / 36.4% [15.2–64.6]; 3.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–25.9] / 90.9% [62.3–98.4] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 66.7% [30.0–90.3]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.5% [1.1–5.7] / 14.7% [6.4–30.1]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 1, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=9) / turno di G2 (n=9) | 0.0% [0.0–29.9] / 0.0% [0.0–29.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=9) | 0.0% [0.0–29.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 44.1% [28.9–60.5] (8.8% [3.0–23.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 8, 'rif_LDR06_ferite_e_caccia': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR05_scudi_armati vs rif_LDR06_ferite_e_caccia 59% (n=34) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR05_scudi_armati 50.0% [43.1–56.9], rif_LDR06_ferite_e_caccia 50.0% [43.1–56.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.375 / 0.098 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.098 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR05_scudi_armati 0.14 (0.00), rif_LDR06_ferite_e_caccia 0.12 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 33.9% [32.6–35.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.95 (254 / 536); 58.2% [56.8–59.6] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 54.0% [53.1–55.0]; rif_LDR05_scudi_armati 61.3%, rif_LDR06_ferite_e_caccia 46.6% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.332 (374) / 0.318 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-05 R: 18.0 (49%, 100 vittorie), LDR-06 G: 17.0 (49%, 100 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.92, LDR-05 3.17, VER-020 2.48, NER-017 1.44, NER-013 1.04, VER-008 0.85, NER-009 0.72, VER-001 0.69, NEU-001 0.65, NER-015 0.58, BLU-015 0.55, BLU-021 0.55 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR05_scudi_armati 0.12, rif_LDR06_ferite_e_caccia 3.03 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.41 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR05_scudi_armati 43% (n=60), rif_LDR06_ferite_e_caccia 30% (n=20) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.3% [9.5–11.3] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 1.26; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEW-B06 50%, VER-001 50%, VER-020 50%, NER-015 50%, caccia 50%, NER-017 50%, NEU-012 50%, NEU-001 50%, NER-009 50%, VER-008 50%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR05_scudi_armati | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR05_scudi_armati | — | 50.0 [43–57] (200) |
| rif_LDR06_ferite_e_caccia | 50.0 [43–57] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 3.90 | 0.00 | 3.17 / 0.00 | 0.00 | 0.77 | 4.6 (199) | 13 | B 47%, R 53% | 2.08 | 0.00 |
| rif_LDR06_ferite_e_caccia | 3.23 | 0.00 | 3.92 / 0.28 | 0.00 | 0.14 | 4.6 (195) | 9 | G 52%, K 48% | 1.96 | 1.38 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR05_scudi_armati | 1.12 | 2.04 |
| rif_LDR06_ferite_e_caccia | 1.72 | 2.21 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.17/1.70/0.59 | 0.55/0.31/0.15/0.06 | 0.61/0.00/0.12/0.07 | 0.66/0.42/0.22/0.15 | 0.59/0.18/0.27/0.14 | 0.58/0.00/0.22/0.10 | 0.69/0.55/0.24/0.17 | 0.00/0.55/0.00/0.00 | 0.00/0.45/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.33/0.27/0.16 | 0.61/0.41/0.14/0.07 | 0.00/0.00/0.00/0.00 | 0.69/0.44/0.17/0.07 | 0.00/0.42/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.10/0.27/0.10 | 0.00/0.00/0.00/0.00 | 0.33/0.34/0.00/0.00 | 0.65/0.40/0.32/0.19 | 0.47/0.40/0.28/0.28 | 0.18/0.02/0.18/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.00/0.09/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.07/0.07/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.03/0.01 | 0.32/0.04/0.01/0.04 | 0.26/0.07/0.10/0.06 | 0.33/0.15/0.10/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.69/0.06/0.49 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.34/0.45/0.21 | 0.00/0.19/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.92/1.56/0.47 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.44/0.15/0.09 | 0.38/0.34/0.04/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.06/0.23/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.30/0.05/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.53/0.42/0.03/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.85/0.03/0.34 | 0.29/0.05/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.65/0.14/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.00/0.00/0.00 | 0.44/0.00/0.00/0.00 | 0.19/0.25/0.02/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.07/0.04 | 0.19/0.37/0.08/0.04 | 0.53/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 0.87 | 0.00 | 0.06 | 0.01 | 0.01 | 0.03 | 0.04 | 0.01 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.16 | 0.27 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.56 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 0.75 | 0.00 | 0.04 | 0.07 | 0.04 | 0.15 | 0.12 | 0.11 | 0.08 | 0.04 | 0.04 | 0.01 | 0.03 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.64 | 0.00 | 0.01 | 0.06 | 0.08 | 0.08 | 0.09 | 0.07 | 0.07 | 0.10 | 0.03 | 0.03 | 0.01 | 0.02 | 0.01 | 0.01 | 1.26 | 0.10 | 0.21 | 0.20 | 0.17 | 0.15 | 0.16 | 0.09 | 0.10 | 0.03 | 0.01 | 0.01 | 0.03 | 0.01 | 0.01 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR05_scudi_armati | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.92 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 7 | 6 | 5 | 0 | 11 |
| 8 | 3 | 5 | 0 | 8 |
| 9 | 13 | 12 | 0 | 25 |
| 10 | 17 | 11 | 0 | 28 |
| 11 | 18 | 9 | 0 | 27 |
| 12 | 10 | 4 | 0 | 14 |
| 13 | 15 | 15 | 0 | 30 |
| 14 | 6 | 16 | 0 | 22 |
| 15 | 19 | 13 | 0 | 32 |
| 16 | 1 | 1 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 61.3% | 0.121 | 0.12 | 0.00 | 0.00 | 0.00 | 2.50 | 0.00 | 0.00 | 0.377 |
| rif_LDR06_ferite_e_caccia | 200 | 46.6% | 0.072 | 0.95 | 2.08 | 0.00 | 0.00 | 4.25 | 0.00 | 0.00 | 0.374 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | mano | 641 | 0.888 | 0.867 | 0.858 | 0.446 | 1940 | 0.784 | 0.204 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 641 | 0.131 | 0.122 | 0.112 | 0.042 | 1940 | 0.088 | 0.027 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 402 | 0.853 | 0.806 | 0.716 | 0.338 | 1837 | 0.766 | 0.236 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 402 | 0.301 | 0.269 | 0.249 | 0.062 | 1837 | 0.249 | 0.073 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 12.0% | 2.25 | 1.52 | 28.3% | 0.5% | 19.7% | 33.0% | 15.3% | 0.00 | 12.7% | 61.3% | 0.07 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 12.0% | 2.25 | 1.52 | 34.1% | 0.5% | 22.7% | 33.3% | 7.3% | 0.00 | 12.4% | 46.6% | 0.08 | 0.00 |
| Totale | 400 | 12.0% | 2.25 | 1.52 | 31.5% | 0.5% | 21.2% | 33.1% | 11.0% | 0.00 | 12.6% | 54.0% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR05_scudi_armati | 200 | 0.282 | 0.136 | 0.0% | 0.0% | 0.96 | 0.95 | 0.46 | 0.41 | 0.00 | 0.00 | 4.93 |
| rif_LDR06_ferite_e_caccia | 200 | 0.316 | 0.057 | 0.0% | 0.0% | 0.53 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 3.90 |

