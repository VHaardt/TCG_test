# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2290s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 45.0% [43.6–46.4] | 30–45% | ✅ |
| Durata mediana (round) | 13.0 [13.0–13.0] (media 12.39) | 8–11 | ❌ |
| Partite al round 13+ | 58.0% [51.1–64.6] | ≤12% | ❌ |
| Partite oltre il 15 | 3.5% [1.7–7.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=83) | 31.3% [22.4–41.9] | 20–35% | ✅ |
| Attacchi con opposizione | 29.8% [28.6–31.2] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 62.9% [61.5–64.2] (con ≥3: 23.6% [22.4–24.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.4% [33.1–35.8] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 12.8% [9.9–16.5] (n=397) / 85.5% [80.9–89.1] (n=283) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.6% [13.0–16.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 51.3% [36.2–66.1] (n=39), LDR-02 Risvegliato 76.2% [65.9–84.2] (n=80), LDR-06 Base 41.7% [19.3–68.0] (n=12), LDR-06 Risvegliato 67.9% [60.4–74.6] (n=162) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 62.7% [54.9–69.8] (n=158) | | |
| Attacchi per partita | 24.0 | | |
| Pugno attaccante vuoto / pieno | 56.9% [55.4–58.4] / 10.6% [9.7–11.5] (gemme medie 0.81) | non >90% | |
| Pugno difensore vuoto / pieno | 53.7% [51.8–55.7] / 23.0% [21.4–24.7] (gemme medie 0.31) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1748, 1: 1827, 2: 768, 3: 354, 4: 79, 5: 19, 6: 10} | | |
| Azioni legali per decisione | 5.7 | <60 | ✅ |
| Fine partita | {'colpo_finale': 162, 'crepuscolo': 38} | | |
| G1 vince fra le partite finite al Crepuscolo | 55.3% [39.7–69.9] | | |
| G1 vince fra le partite arrivate al round 15 | 55.8% [42.3–68.4] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 26.9% [16.8–40.3] / 42.9% [21.4–67.4] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 35.7% [16.3–61.2]; 13.5% [6.7–25.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 5, '2-3': 5, '2-1': 5, '1-0': 5, '0-1': 3, '0-0': 3, '1-1': 3, '2-0': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=17) | 32.7% [21.5–46.2] / 41.2% [21.6–64.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 14, 16: 3}; 58.8% [36.0–78.4] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 52.9% [31.0–73.8] / 35.3% [17.3–58.7]; 2.06 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–18.4] / 82.4% [59.0–93.8] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=7) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–35.4] / 60.0% [31.3–83.2]; 0.0% [0.0–35.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.5% [1.7–7.0] / 13.5% [6.7–25.3]; 100.0% [64.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 3, 'perd:pronto': 4, 'vinc:atk': 7} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=11) / turno di G2 (n=9) | 0.0% [0.0–25.9] / 0.0% [0.0–29.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=11) | 0.0% [0.0–25.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 48.1% [35.1–61.3] (13.5% [6.7–25.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 11, 'rif_LDR02_muro_di_parata': 6} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR06_ferite_e_caccia 56% (n=52) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 64.5% [57.7–70.8], rif_LDR06_ferite_e_caccia 35.5% [29.2–42.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.514 / 0.101 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.099 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.16 (0.00), rif_LDR06_ferite_e_caccia 0.10 (0.01) | |
| M4 | Scontri decisi prima dell'impegno | 27.9% [26.7–29.2] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.94 (201 / 387); 60.6% [59.2–62.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 53.9% [52.9–54.9]; rif_LDR02_muro_di_parata 58.9%, rif_LDR06_ferite_e_caccia 49.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.2% [0.1–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.394 (80) / 0.336 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 129 vittorie), LDR-06 G: 17.0 (49%, 71 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 2.52, VER-020 1.92, LDR-02 1.79, NER-017 1.03, NEW-I04 0.65, NEU-001 0.57, NER-009 0.57, NER-013 0.56, VER-019 0.53, NER-003 0.51, BLU-001 0.51, BLU-005 0.47 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.69, rif_LDR06_ferite_e_caccia 2.28 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 0.21 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 40% (n=25), rif_LDR06_ferite_e_caccia 28% (n=58) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.6% [9.7–11.5] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 0.92; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, collante 100%, NER-014 64%, RS 64%, BLU-021 64%, NEU-003 64%, NEU-015 64%, NEU-009 64%, NEU-012 36%, NEW-B06 36%, NER-017 36%, VER-020 36%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 64.5 [58–71] (200) |
| rif_LDR06_ferite_e_caccia | 35.5 [29–42] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.01 | 0.00 | 1.79 / 0.00 | 0.00 | 1.09 | 5.5 (199) | 8 | B 82%, K 18% | 2.31 | 0.00 |
| rif_LDR06_ferite_e_caccia | 3.84 | 0.00 | 2.52 / 0.10 | 0.00 | 0.22 | 5.3 (196) | 10 | G 54%, K 46% | 2.50 | 1.67 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.85/0.51/0.17/0.09 | 0.85/0.00/0.23/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.93/0.00/0.40/0.19 | 0.00/0.00/0.00/0.00 | 0.00/0.36/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.35/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.79/1.63/0.69 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.00/0.07/0.03 | 0.94/0.47/0.04/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.43/0.00/0.00/0.00 | 0.41/0.19/0.07/0.01 | 0.43/0.07/0.12/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.19/0.23/0.27 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.65/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.42/0.04/0.19 | 0.67/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.53/0.46/0.16 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.52/1.77/0.43 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.36/0.14/0.03 | 0.37/0.30/0.07/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.09/0.21/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.33/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.41/0.07/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.35/0.01/0.10 | 0.37/0.04/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.57/0.14/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.00/0.00/0.00 | 0.64/0.00/0.00/0.00 | 0.28/0.33/0.05/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.12/0.01 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.35 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.61 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.85 | 0.00 | 0.03 | 0.06 | 0.05 | 0.13 | 0.10 | 0.14 | 0.10 | 0.10 | 0.06 | 0.04 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.90 | 0.00 | 0.01 | 0.05 | 0.07 | 0.06 | 0.10 | 0.12 | 0.12 | 0.12 | 0.07 | 0.06 | 0.06 | 0.04 | 0.01 | 0.92 | 0.07 | 0.23 | 0.10 | 0.12 | 0.07 | 0.14 | 0.07 | 0.04 | 0.02 | 0.04 | 0.04 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR02_muro_di_parata | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.34 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 2 | 0 | 3 |
| 7 | 1 | 4 | 0 | 5 |
| 8 | 6 | 4 | 0 | 10 |
| 9 | 10 | 3 | 0 | 13 |
| 10 | 7 | 7 | 0 | 14 |
| 11 | 13 | 9 | 0 | 22 |
| 12 | 5 | 12 | 0 | 17 |
| 13 | 21 | 19 | 0 | 40 |
| 14 | 8 | 16 | 0 | 24 |
| 15 | 25 | 20 | 0 | 45 |
| 16 | 4 | 3 | 0 | 7 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 58.9% | 0.114 | 1.69 | 0.00 | 0.00 | 0.00 | 2.12 | 0.00 | 0.00 | 0.528 |
| rif_LDR06_ferite_e_caccia | 200 | 49.1% | 0.086 | 0.94 | 1.33 | 0.00 | 0.00 | 2.82 | 0.00 | 0.00 | 0.395 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 625 | 0.997 | 0.931 | 0.885 | 0.218 | 1928 | 0.985 | 0.383 | 0.138 | 0.064 |
| rif_LDR02_muro_di_parata | Cicatrice | 625 | 0.280 | 0.208 | 0.157 | 0.040 | 1928 | 0.218 | 0.060 | 0.014 | 0.004 |
| rif_LDR06_ferite_e_caccia | mano | 535 | 0.869 | 0.809 | 0.746 | 0.327 | 1717 | 0.748 | 0.231 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 535 | 0.217 | 0.198 | 0.138 | 0.036 | 1717 | 0.162 | 0.055 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 19.0% | 2.42 | 1.95 | 32.9% | 0.0% | 33.5% | 33.4% | 8.6% | 0.00 | 13.0% | 58.9% | 0.01 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 19.0% | 2.42 | 1.95 | 23.6% | 0.0% | 25.5% | 31.4% | 5.2% | 0.00 | 14.3% | 49.1% | 0.10 | 0.00 |
| Totale | 400 | 19.0% | 2.42 | 1.95 | 26.8% | 0.0% | 29.5% | 32.4% | 7.0% | 0.00 | 13.6% | 53.9% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.259 | 0.172 | 0.5% | 0.7% | 0.95 | 0.76 | 0.84 | 0.60 | 0.00 | 0.00 | 4.39 |
| rif_LDR06_ferite_e_caccia | 200 | 0.344 | 0.045 | 0.0% | 0.0% | 0.34 | 0.00 | 0.10 | 0.12 | 0.00 | 0.00 | 3.88 |

