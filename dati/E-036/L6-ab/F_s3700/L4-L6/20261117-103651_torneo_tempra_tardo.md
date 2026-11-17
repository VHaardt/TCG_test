# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1907s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 38.9% [37.5–40.2] | 30–45% | ✅ |
| Durata mediana (round) | 11.5 [11.0–12.0] (media 11.52) | 8–11 | ❌ |
| Partite al round 13+ | 40.0% [33.5–46.9] | ≤12% | ❌ |
| Partite oltre il 15 | 0.5% [0.1–2.8] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=82) | 41.5% [31.4–52.3] | 20–35% | ❌ |
| Attacchi con opposizione | 22.6% [21.4–23.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 61.7% [60.3–63.1] (con ≥3: 20.3% [19.2–21.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.3% [35.0–37.7] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 9.7% [7.4–12.6] (n=485) / 70.3% [65.0–75.1] (n=313) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.3% [10.9–13.9] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Base 45.7% [30.5–61.8] (n=35), LDR-04 Risvegliato 69.7% [58.7–78.9] (n=76), LDR-06 Base 58.3% [32.0–80.7] (n=12), LDR-06 Risvegliato 81.9% [74.9–87.4] (n=144) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 43.5% [36.1–51.2] (n=161) | | |
| Attacchi per partita | 24.6 | | |
| Pugno attaccante vuoto / pieno | 51.4% [49.9–52.9] / 13.0% [12.1–14.1] (gemme medie 0.85) | non >90% | |
| Pugno difensore vuoto / pieno | 67.0% [65.1–68.8] / 18.7% [17.2–20.2] (gemme medie 0.23) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1583, 1: 1997, 2: 954, 3: 284, 4: 75, 5: 19, 6: 2} | | |
| Azioni legali per decisione | 5.7 | <60 | ✅ |
| Fine partita | {'colpo_finale': 188, 'crepuscolo': 12} | | |
| G1 vince fra le partite finite al Crepuscolo | 50.0% [25.4–74.6] | | |
| G1 vince fra le partite arrivate al round 15 | 50.0% [28.0–72.0] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 31.2% [14.2–55.6] / 0.0% [0.0–43.4] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 40.0% [11.8–76.9]; 6.2% [1.1–28.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-1': 3, '1-3': 3, '1-0': 2, '3-2': 2, '3-3': 2, '2-0': 1, '2-1': 1, '2-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=6) | 37.5% [18.5–61.4] / 0.0% [0.0–39.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 5, 16: 1}; 50.0% [18.8–81.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 100.0% [61.0–100.0] / 33.3% [9.7–70.0]; 3.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–39.0] / 100.0% [61.0–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=0) / a Vite diverse; nessuno attacca a Vite pari | nan% [nan–nan] / 33.3% [9.7–70.0]; nan% [nan–nan] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 0.0% [0.0–1.9] / 0.0% [0.0–19.4]; nan% [nan–nan] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=11) / turno di G2 (n=4) | 0.0% [0.0–25.9] / 0.0% [0.0–49.0] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=11) | 0.0% [0.0–25.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 50.0% [28.0–72.0] (18.8% [6.6–43.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 5, 'rif_LDR06_ferite_e_caccia': 1} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR06_ferite_e_caccia 50% (n=16) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 66.5% [59.7–72.7], rif_LDR06_ferite_e_caccia 33.5% [27.3–40.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.474 / 0.076 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.076 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.10 (0.00), rif_LDR06_ferite_e_caccia 0.12 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 33.1% [31.8–34.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 4.75 (278 / 672); 63.2% [61.8–64.5] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.0% [51.0–53.1]; rif_LDR04_stanca_e_smonta 55.6%, rif_LDR06_ferite_e_caccia 48.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.403 (60) / 0.324 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 12.0 (36%, 133 vittorie), LDR-06 G: 17.0 (49%, 67 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 3.79, LDR-06 2.97, VER-020 2.13, NER-017 1.18, BLU-015 0.91, VER-008 0.77, NEW-I04 0.64, VER-023 0.63, NER-009 0.61, VER-001 0.52, NEU-001 0.51, NER-013 0.48 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.51, rif_LDR06_ferite_e_caccia 2.91 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.30, rif_LDR06_ferite_e_caccia 0.24 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 60% (n=20), rif_LDR06_ferite_e_caccia 35% (n=62) | 20–35% |
| M13 | Pugno d'attacco pieno | 13.0% [12.1–14.1] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR06_ferite_e_caccia 0.89; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, VER-001 100%, VER-008 100%, ponte 100%, caccia 100%, VER-023 66%, VER-014 66%, NEU-009 66%, BLU-010 66%, NEU-012 34%, NER-009 34%, NER-015 34%; oltre il 60%: VER-001, VER-008, VER-023 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 66.5 [60–73] (200) |
| rif_LDR06_ferite_e_caccia | 33.5 [27–40] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 4.92 | 1.74 | 3.79 / 0.00 | 0.00 | 0.73 | 5.2 (199) | 9 | B 41%, G 59% | 2.14 | 0.73 |
| rif_LDR06_ferite_e_caccia | 3.77 | 0.00 | 2.97 / 0.15 | 0.00 | 0.17 | 4.3 (196) | 9 | G 54%, K 46% | 2.44 | 1.22 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.40/0.16/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.13/0.34/0.10 | 0.38/0.00/0.23/0.04 | 0.78/0.91/0.52/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.47/0.08/0.39 | 0.61/0.00/0.00/0.00 | 0.69/0.00/0.15/0.07 | 0.00/0.00/0.00/0.00 | 0.40/0.32/0.24/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.79/1.98/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.27/0.63/0.07/0.29 | 0.00/0.00/0.00/0.00 | 0.40/0.21/0.05/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.12/0.17/0.06 | 0.42/0.00/0.02/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.97/0.03/0.39 | 0.32/0.03/0.04/0.01 | 0.38/0.00/0.16/0.03 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.00/0.00 | 0.20/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.64/0.00/0.00 | 0.00/0.05/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.56/0.06/0.34 | 0.69/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.57/0.62/0.30 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.97/2.02/0.53 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.34/0.20/0.07 | 0.39/0.25/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.07/0.24/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.17/0.01/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.38/0.03/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.56/0.01/0.26 | 0.42/0.04/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.90/0.51/0.12/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.00/0.00/0.00 | 0.45/0.00/0.00/0.00 | 0.27/0.41/0.04/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.15/0.05 | 0.00/0.00/0.00/0.00 | 0.49/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.57 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.03 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.58 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.98 | 0.00 | 0.02 | 0.09 | 0.08 | 0.12 | 0.14 | 0.14 | 0.13 | 0.15 | 0.03 | 0.04 | 0.03 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.79 | 0.00 | 0.02 | 0.03 | 0.04 | 0.10 | 0.10 | 0.17 | 0.11 | 0.10 | 0.04 | 0.04 | 0.04 | 0.01 | 0.01 | 0.00 | 0.89 | 0.10 | 0.12 | 0.09 | 0.11 | 0.09 | 0.14 | 0.12 | 0.04 | 0.03 | 0.04 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR04_stanca_e_smonta | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.43 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 2 | 1 | 0 | 3 |
| 7 | 1 | 3 | 0 | 4 |
| 8 | 5 | 4 | 0 | 9 |
| 9 | 10 | 12 | 0 | 22 |
| 10 | 11 | 15 | 0 | 26 |
| 11 | 19 | 17 | 0 | 36 |
| 12 | 9 | 11 | 0 | 20 |
| 13 | 21 | 24 | 0 | 45 |
| 14 | 11 | 8 | 0 | 19 |
| 15 | 7 | 8 | 0 | 15 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 55.6% | 0.073 | 1.66 | 0.85 | 0.00 | 0.00 | 2.10 | 0.00 | 0.00 | 0.463 |
| rif_LDR06_ferite_e_caccia | 200 | 48.3% | 0.079 | 1.03 | 1.88 | 0.00 | 0.00 | 4.00 | 0.00 | 0.00 | 0.383 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 341 | 0.789 | 0.716 | 0.663 | 0.132 | 2170 | 0.770 | 0.397 | 0.171 | 0.055 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 341 | 0.126 | 0.088 | 0.062 | 0.035 | 2170 | 0.108 | 0.050 | 0.029 | 0.004 |
| rif_LDR06_ferite_e_caccia | mano | 498 | 0.880 | 0.807 | 0.729 | 0.333 | 1905 | 0.765 | 0.243 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 498 | 0.227 | 0.181 | 0.149 | 0.046 | 1905 | 0.171 | 0.053 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 6.0% | 2.19 | 1.81 | 42.2% | 0.0% | 23.8% | 27.5% | 6.6% | 0.00 | 14.2% | 55.6% | 0.03 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 6.0% | 2.19 | 1.81 | 18.4% | 0.0% | 24.2% | 27.8% | 5.6% | 0.00 | 8.8% | 48.3% | 0.05 | 0.00 |
| Totale | 400 | 6.0% | 2.19 | 1.81 | 27.9% | 0.0% | 24.0% | 27.6% | 6.1% | 0.00 | 11.6% | 52.0% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.274 | 0.110 | 0.0% | 0.0% | 0.55 | 0.78 | 0.31 | 0.41 | 0.00 | 0.00 | 4.42 |
| rif_LDR06_ferite_e_caccia | 200 | 0.175 | 0.031 | 0.0% | 0.0% | 0.24 | 0.05 | 0.06 | 0.31 | 0.00 | 0.00 | 4.50 |

