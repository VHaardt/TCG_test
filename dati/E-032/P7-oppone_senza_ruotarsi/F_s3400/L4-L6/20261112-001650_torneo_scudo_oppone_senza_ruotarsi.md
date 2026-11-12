# Torneo v0.2 — /home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json

- Regole `v0.2`, configurazione `/home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json`; differenze da B0: {'pugno': 'sequenziale', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L')}
- IA: forte:30; partite: 200; tempo 1655s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 41.8% [40.5–43.2] | 30–45% | ✅ |
| Durata mediana (round) | 13.0 [12.0–13.0] (media 12.30) | 8–11 | ❌ |
| Partite al round 13+ | 55.5% [48.6–62.2] | ≤12% | ❌ |
| Partite oltre il 15 | 2.0% [0.8–5.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=71) | 29.6% [20.2–41.0] | 20–35% | ✅ |
| Attacchi con opposizione | 23.5% [22.4–24.7] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 59.2% [57.8–60.6] (con ≥3: 20.1% [19.0–21.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 31.1% [29.9–32.4] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–0.8] (n=497) / 86.8% [82.5–90.1] (n=310) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 17.0% [15.2–18.9] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-04 Risvegliato 76.9% [67.3–84.4] (n=91), LDR-06 Risvegliato 80.9% [74.5–86.0] (n=178) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 61.9% [54.2–69.0] (n=160) | | |
| Attacchi per partita | 25.5 | | |
| Pugno attaccante vuoto / pieno | 53.9% [52.4–55.3] / 11.7% [10.8–12.6] (gemme medie 0.86) | non >90% | |
| Pugno difensore vuoto / pieno | 58.1% [56.2–59.9] / 24.8% [23.2–26.5] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1777, 1: 1908, 2: 918, 3: 344, 4: 99, 5: 37, 6: 8, 7: 1} | | |
| Azioni legali per decisione | 5.8 | <60 | ✅ |
| Fine partita | {'colpo_finale': 160, 'crepuscolo': 40} | | |
| G1 vince fra le partite finite al Crepuscolo | 45.0% [30.7–60.2] | | |
| G1 vince fra le partite arrivate al round 15 | 52.9% [39.5–65.9] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 29.4% [18.7–43.0] / 60.0% [35.7–80.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 20.0% [7.0–45.2]; 7.8% [3.1–18.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-0': 8, '2-0': 7, '2-1': 6, '2-2': 5, '2-3': 5, '1-2': 5, '1-0': 3, '0-1': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=19) | 37.3% [25.3–51.0] / 57.9% [36.3–76.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15, 16: 4}; 78.9% [56.7–91.5] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 63.2% [41.0–80.9] / 15.8% [5.5–37.6]; 1.42 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–16.8] / 78.9% [56.7–91.5] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=11) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–25.9] / 37.5% [13.7–69.4]; 0.0% [0.0–25.9] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.5% [3.1–9.6] / 21.6% [12.5–34.6]; 100.0% [74.1–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 7, 'perd:pronto': 3, 'perd:rim': 1, 'vinc:atk': 11} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=12) / turno di G2 (n=13) | 0.0% [0.0–24.3] / 0.0% [0.0–22.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=12) | 0.0% [0.0–24.3] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 56.9% [43.3–69.5] (23.5% [14.0–36.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 11, 'rif_LDR06_ferite_e_caccia': 8} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR04_stanca_e_smonta vs rif_LDR06_ferite_e_caccia 53% (n=51) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR04_stanca_e_smonta 57.5% [50.6–64.1], rif_LDR06_ferite_e_caccia 42.5% [35.9–49.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.390 / 0.083 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.083 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR04_stanca_e_smonta 0.11 (0.00), rif_LDR06_ferite_e_caccia 0.10 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 32.5% [31.2–33.8] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.45 (341 / 748); 60.7% [59.3–62.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.4% [51.4–53.4]; rif_LDR04_stanca_e_smonta 57.8%, rif_LDR06_ferite_e_caccia 46.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 4.8% [3.7–6.1] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.390 (76) / 0.322 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-04 B: 14.0 (40%, 115 vittorie), LDR-06 G: 17.0 (49%, 85 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 3.92, LDR-06 3.00, VER-020 1.96, NER-017 1.34, VER-008 1.00, BLU-023 0.73, BLU-015 0.70, VER-003 0.65, NER-015 0.63, VER-001 0.62, VER-014 0.59, BLU-001 0.58 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR04_stanca_e_smonta 2.88, rif_LDR06_ferite_e_caccia 3.40 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR04_stanca_e_smonta 0.23, rif_LDR06_ferite_e_caccia 0.28 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR04_stanca_e_smonta 38% (n=13), rif_LDR06_ferite_e_caccia 28% (n=58) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.7% [10.8–12.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR04_stanca_e_smonta 0.00, rif_LDR06_ferite_e_caccia 1.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-001 100%, ponte 100%, caccia 100%, VER-008 100%, VER-023 100%, collante 100%, RS 57%, BLU-010 57%, NEU-003 57%, NEU-011 57%, VER-014 57%, NEU-009 57%; oltre il 60%: VER-001, VER-008, VER-023 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR04_stanca_e_smonta | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR04_stanca_e_smonta | — | 57.5 [51–64] (200) |
| rif_LDR06_ferite_e_caccia | 42.5 [36–49] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 5.38 | 1.63 | 3.92 / 0.00 | 0.00 | 0.79 | 5.2 (197) | 9 | B 41%, G 59% | 2.44 | 0.76 |
| rif_LDR06_ferite_e_caccia | 3.98 | 0.00 | 3.00 / 0.07 | 0.00 | 0.23 | 4.5 (197) | 10 | G 56%, K 44% | 2.52 | 1.53 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.58/0.12/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.14/0.23/0.10 | 0.39/0.00/0.12/0.07 | 0.68/0.70/0.28/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.73/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.54/0.04/0.43 | 0.64/0.00/0.00/0.00 | 0.69/0.00/0.14/0.01 | 0.00/0.00/0.00/0.00 | 0.38/0.28/0.21/0.11 | 0.00/0.34/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.92/2.04/0.34 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.29/0.04/0.14 | 0.00/0.00/0.00/0.00 | 0.41/0.18/0.03/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.14/0.13/0.04 | 0.32/0.00/0.01/0.01 | 0.27/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.97/0.01/0.45 | 0.39/0.04/0.03/0.03 | 0.32/0.00/0.10/0.04 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.70/0.03/0.50 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.48/0.52/0.27 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.00/2.00/0.60 | 0.00/0.00/0.00/0.00 | 0.64/0.00/0.00/0.00 | 0.30/0.82/0.06/0.40 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.33/0.18/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.12/0.23/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.26/0.02/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.46/0.03/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/1.02/0.03/0.46 | 0.35/0.02/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.88/0.41/0.15/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 0.48 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.01 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.73 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.29 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 1.14 | 0.00 | 0.03 | 0.05 | 0.10 | 0.12 | 0.14 | 0.12 | 0.14 | 0.12 | 0.10 | 0.07 | 0.10 | 0.01 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 1.26 | 0.00 | 0.05 | 0.03 | 0.06 | 0.12 | 0.10 | 0.20 | 0.15 | 0.14 | 0.14 | 0.13 | 0.09 | 0.07 | 0.01 | 1.00 | 0.12 | 0.12 | 0.10 | 0.09 | 0.10 | 0.12 | 0.12 | 0.09 | 0.06 | 0.04 | 0.02 | 0.01 | 0.01 | 0.01 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 0 | 0 | 1 |
| 7 | 4 | 2 | 0 | 6 |
| 8 | 5 | 4 | 0 | 9 |
| 9 | 9 | 11 | 0 | 20 |
| 10 | 7 | 5 | 0 | 12 |
| 11 | 12 | 12 | 0 | 24 |
| 12 | 8 | 9 | 0 | 17 |
| 13 | 16 | 21 | 0 | 37 |
| 14 | 10 | 13 | 0 | 23 |
| 15 | 26 | 21 | 0 | 47 |
| 16 | 1 | 3 | 0 | 4 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 57.8% | 0.099 | 2.09 | 0.79 | 0.00 | 0.00 | 2.10 | 0.00 | 0.00 | 0.296 |
| rif_LDR06_ferite_e_caccia | 200 | 46.5% | 0.065 | 0.95 | 2.44 | 0.00 | 0.00 | 4.79 | 0.00 | 0.00 | 0.498 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | mano | 616 | 0.815 | 0.708 | 0.633 | 0.399 | 2104 | 0.699 | 0.144 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 616 | 0.131 | 0.115 | 0.104 | 0.036 | 2104 | 0.069 | 0.026 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 474 | 0.949 | 0.928 | 0.909 | 0.281 | 1898 | 0.883 | 0.378 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 474 | 0.287 | 0.262 | 0.217 | 0.044 | 1898 | 0.193 | 0.079 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 20.0% | 2.29 | 2.23 | 21.2% | 0.0% | 23.0% | 26.6% | 7.2% | 0.00 | 13.4% | 57.8% | 0.03 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 20.0% | 2.29 | 2.23 | 23.1% | 0.0% | 26.8% | 26.7% | 7.3% | 0.00 | 9.4% | 46.5% | 0.04 | 0.00 |
| Totale | 400 | 20.0% | 2.29 | 2.23 | 22.3% | 0.0% | 24.9% | 26.6% | 7.2% | 0.00 | 11.5% | 52.4% | 0.03 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR04_stanca_e_smonta | 200 | 0.274 | 0.129 | 7.4% | 15.7% | 0.90 | 0.99 | 0.32 | 0.46 | 0.00 | 0.00 | 3.72 |
| rif_LDR06_ferite_e_caccia | 200 | 0.191 | 0.029 | 0.4% | 2.9% | 0.27 | 0.07 | 0.04 | 0.28 | 0.00 | 0.00 | 4.21 |

