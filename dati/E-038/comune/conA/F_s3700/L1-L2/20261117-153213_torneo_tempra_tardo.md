# Torneo v0.2 — /root/in38/dati/E-038-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in38/dati/E-038-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 3100s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 38.7% [37.4–40.1] | 30–45% | ✅ |
| Durata mediana (round) | 13.0 [13.0–14.0] (media 12.55) | 8–11 | ❌ |
| Partite al round 13+ | 59.0% [52.1–65.6] | ≤12% | ❌ |
| Partite oltre il 15 | 3.0% [1.4–6.4] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=76) | 30.3% [21.1–41.3] | 20–35% | ✅ |
| Attacchi con opposizione | 38.2% [36.9–39.6] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 70.6% [69.3–71.8] (con ≥3: 31.3% [30.0–32.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.2% [34.9–37.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 9.0% [6.7–11.8] (n=480) / 87.3% [82.4–90.9] (n=236) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.2% [9.8–12.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 46.2% [23.2–70.9] (n=13), LDR-01 Risvegliato 64.9% [55.8–73.1] (n=114), LDR-02 Base 40.0% [24.6–57.7] (n=30), LDR-02 Risvegliato 80.4% [71.2–87.3] (n=92) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 60.9% [53.4–68.0] (n=169) | | |
| Attacchi per partita | 25.5 | | |
| Pugno attaccante vuoto / pieno | 47.9% [46.5–49.3] / 12.0% [11.1–13.0] (gemme medie 0.99) | non >90% | |
| Pugno difensore vuoto / pieno | 52.7% [50.8–54.7] / 24.4% [22.7–26.1] (gemme medie 0.32) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1730, 1: 1710, 2: 1044, 3: 377, 4: 160, 5: 61, 6: 18, 7: 1} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 160, 'crepuscolo': 40} | | |
| G1 vince fra le partite finite al Crepuscolo | 62.5% [47.0–75.8] | | |
| G1 vince fra le partite arrivate al round 15 | 50.8% [38.8–62.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 22.2% [13.7–33.9] / 42.9% [21.4–67.4] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 35.7% [16.3–61.2]; 9.5% [4.4–19.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 7, '2-1': 7, '2-3': 6, '3-3': 5, '1-0': 5, '1-1': 4, '3-2': 3, '1-2': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=15) | 23.8% [15.0–35.6] / 40.0% [19.8–64.3] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 14, 16: 1}; 60.0% [35.7–80.2] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 60.0% [35.7–80.2] / 26.7% [10.9–52.0]; 1.93 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–20.4] / 73.3% [48.0–89.1] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=6) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–39.0] / 44.4% [18.9–73.3]; 0.0% [0.0–39.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.4–6.4] / 9.5% [4.4–19.3]; 100.0% [61.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 4, 'vinc:atk': 6} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=19) / turno di G2 (n=18) | 0.0% [0.0–16.8] / 0.0% [0.0–17.6] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=19) | 0.0% [0.0–16.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 42.9% [31.4–55.1] (11.1% [5.5–21.2]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 11, 'rif_LDR01_puntata_e_preda': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR02_muro_di_parata 51% (n=63) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 42.0% [35.4–48.9], rif_LDR02_muro_di_parata 58.0% [51.1–64.6]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.500 / 0.098 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.095 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.10 (0.00), rif_LDR02_muro_di_parata 0.17 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 26.0% [24.8–27.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.27 (94 / 161); 57.9% [56.5–59.2] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 56.0% [55.1–56.9]; rif_LDR01_puntata_e_preda 54.4%, rif_LDR02_muro_di_parata 57.7% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.2% [0.1–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.326 (588) / 0.314 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 84 vittorie), LDR-02 K: 6.0 (19%, 116 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-01 2.08, LDR-02 1.38, ROS-018 1.12, ROS-016 1.05, BLU-001 0.68, VER-011 0.64, ROS-021 0.63, BLU-005 0.60, NEW-I04 0.57, ROS-001 0.57, VER-019 0.56, VER-001 0.54 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.53, rif_LDR02_muro_di_parata 1.35 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR02_muro_di_parata 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 24% (n=37), rif_LDR02_muro_di_parata 36% (n=39) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.0% [11.1–13.0] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR02_muro_di_parata 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, collante 58%, NER-014 58%, NEU-003 58%, BLU-021 58%, RS 58%, NEU-015 58%, NEU-009 58%, VER-008 42%, ROS-016 42%, caccia 42%, VER-001 42%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR02_muro_di_parata |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 42.0 [35–49] (200) |
| rif_LDR02_muro_di_parata | 58.0 [51–65] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.04 | 0.00 | 2.08 / 0.00 | 0.00 | 0.00 | 4.2 (198) | 13 | G 40%, R 60% | 2.58 | 0.47 |
| rif_LDR02_muro_di_parata | 4.33 | 0.00 | 1.38 / 0.00 | 0.00 | 1.50 | 4.5 (199) | 8 | B 82%, K 18% | 2.08 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR01_puntata_e_preda | 2.08 | 0.00 |
| rif_LDR02_muro_di_parata | 1.38 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/2.08/1.68/0.55 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.43/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.86/0.57/0.21/0.12 | 0.73/0.16/0.42/0.26 | 0.87/0.47/0.14/0.10 | 0.00/0.41/0.00/0.00 | 0.81/0.00/0.28/0.12 | 0.77/0.34/0.28/0.17 | 0.71/1.05/0.01/0.30 | 0.70/1.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.63/0.27/0.24 | 0.26/0.12/0.14/0.10 | 0.00/0.00/0.00/0.00 | 0.66/0.54/0.04/0.25 | 0.76/0.00/0.00/0.00 | 0.67/0.00/0.14/0.04 | 0.71/0.64/0.23/0.09 | 0.80/0.56/0.36/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.03/0.02 | 0.45/0.09/0.04/0.04 | 0.36/0.11/0.14/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.06/0.03 | 0.34/0.40/0.00/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.17/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.68/0.26/0.17 | 0.78/0.00/0.28/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.00/0.40/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.52/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.26/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.38/1.90/1.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.94/0.00/0.15/0.08 | 0.89/0.60/0.07/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.02/0.00/0.00 | 0.38/0.00/0.00/0.00 | 0.52/0.39/0.06/0.04 | 0.40/0.03/0.14/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.12/0.17/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.57/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.23 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.16 | 0.03 | 0.00 | 0.02 | 0.20 | 0.09 | 0.00 | 0.00 | 0.30 | 0.09 | 0.00 | 0.02 | 0.00 | 0.00 | 0.04 | 0.11 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 0.45 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 1.04 | 0.01 | 0.04 | 0.03 | 0.12 | 0.14 | 0.15 | 0.17 | 0.13 | 0.08 | 0.07 | 0.06 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 200 | 0.99 | 0.04 | 0.07 | 0.07 | 0.10 | 0.17 | 0.15 | 0.14 | 0.14 | 0.04 | 0.04 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 7 | 1 | 2 | 0 | 3 |
| 8 | 8 | 5 | 0 | 13 |
| 9 | 7 | 4 | 0 | 11 |
| 10 | 8 | 12 | 0 | 20 |
| 11 | 14 | 3 | 0 | 17 |
| 12 | 10 | 7 | 0 | 17 |
| 13 | 15 | 15 | 0 | 30 |
| 14 | 9 | 16 | 0 | 25 |
| 15 | 27 | 30 | 0 | 57 |
| 16 | 5 | 1 | 0 | 6 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 54.4% | 0.082 | 0.00 | 0.53 | 0.00 | 0.00 | 2.94 | 0.00 | 0.00 | 0.362 |
| rif_LDR02_muro_di_parata | 200 | 57.7% | 0.113 | 1.35 | 0.00 | 0.00 | 0.00 | 3.46 | 0.00 | 0.00 | 0.532 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 580 | 0.886 | 0.857 | 0.824 | 0.314 | 1900 | 0.821 | 0.188 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 580 | 0.183 | 0.171 | 0.140 | 0.036 | 1900 | 0.156 | 0.047 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | mano | 589 | 0.997 | 0.946 | 0.886 | 0.268 | 2032 | 0.983 | 0.388 | 0.133 | 0.052 |
| rif_LDR02_muro_di_parata | Cicatrice | 589 | 0.314 | 0.267 | 0.188 | 0.041 | 2032 | 0.256 | 0.085 | 0.025 | 0.004 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 20.0% | 2.56 | 1.74 | 25.5% | 0.5% | 17.5% | 29.6% | 5.9% | 0.00 | 15.9% | 54.4% | 0.21 | 0.00 |
| rif_LDR02_muro_di_parata | 200 | 20.0% | 2.56 | 1.74 | 36.1% | 0.5% | 20.2% | 35.3% | 14.1% | 0.00 | 15.2% | 57.7% | 0.02 | 0.00 |
| Totale | 400 | 20.0% | 2.56 | 1.74 | 30.4% | 0.5% | 18.8% | 32.4% | 10.7% | 0.00 | 15.6% | 56.0% | 0.12 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.409 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.48 |
| rif_LDR02_muro_di_parata | 200 | 0.357 | 0.226 | 0.4% | 0.7% | 1.50 | 0.28 | 0.86 | 0.00 | 0.00 | 0.00 | 4.75 |

