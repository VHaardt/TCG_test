# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1344s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 37.7% [36.4–39.1] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.0–12.0] (media 11.82) | 8–11 | ❌ |
| Partite al round 13+ | 39.0% [32.5–45.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=66) | 27.3% [18.0–39.0] | 20–35% | ✅ |
| Attacchi con opposizione | 30.5% [29.2–31.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 59.6% [58.1–61.0] (con ≥3: 22.3% [21.1–23.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.2% [37.9–40.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 10.8% [8.2–14.2] (n=424) / 91.0% [87.1–93.8] (n=278) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.9% [11.5–14.5] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 41.2% [26.4–57.8] (n=34), LDR-01 Risvegliato 63.3% [54.4–71.4] (n=120), LDR-02 Base 41.7% [19.3–68.0] (n=12), LDR-02 Risvegliato 87.2% [80.5–91.9] (n=133) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 41.7% [34.5–49.2] (n=168) | | |
| Attacchi per partita | 25.0 | | |
| Pugno attaccante vuoto / pieno | 51.1% [49.7–52.5] / 11.5% [10.7–12.5] (gemme medie 0.95) | non >90% | |
| Pugno difensore vuoto / pieno | 54.6% [52.7–56.5] / 23.1% [21.5–24.8] (gemme medie 0.31) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1856, 1: 1597, 2: 1058, 3: 308, 4: 129, 5: 39, 6: 11, 7: 2} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 177, 'crepuscolo': 23} | | |
| G1 vince fra le partite finite al Crepuscolo | 47.8% [29.2–67.0] | | |
| G1 vince fra le partite arrivate al round 15 | 48.6% [33.4–64.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 18.9% [9.5–34.2] / 42.9% [15.8–75.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 42.9% [15.8–75.0]; 8.1% [2.8–21.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 7, '2-3': 5, '1-0': 3, '2-0': 3, '2-1': 3, '0-0': 3, '0-2': 2, '1-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=8) | 21.6% [11.4–37.2] / 50.0% [21.5–78.5] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 7, 16: 1}; 62.5% [30.6–86.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 50.0% [21.5–78.5] / 25.0% [7.1–59.1]; 3.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–32.4] / 100.0% [67.6–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=4) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–49.0] / 50.0% [15.0–85.0]; 0.0% [0.0–49.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.8–5.0] / 10.8% [4.3–24.7]; 100.0% [51.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'vinc:atk': 4} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=14) / turno di G2 (n=9) | 0.0% [0.0–21.5] / 0.0% [0.0–29.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=14) | 0.0% [0.0–21.5] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 27.0% [15.4–43.0] (5.4% [1.5–17.7]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 4, 'rif_LDR02_muro_di_parata': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR02_muro_di_parata 49% (n=37) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 66.5% [59.7–72.7], rif_LDR02_muro_di_parata 33.5% [27.3–40.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.473 / 0.067 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.064 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.07 (0.00), rif_LDR02_muro_di_parata 0.14 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 26.5% [25.3–27.7] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.36 (79 / 194); 64.9% [63.6–66.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 50.4% [49.4–51.4]; rif_LDR01_puntata_e_preda 52.4%, rif_LDR02_muro_di_parata 47.2% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.335 (507) / 0.334 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 133 vittorie), LDR-02 K: 9.0 (26%, 67 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-01 2.04, LDR-02 1.43, ROS-016 1.31, ROS-018 1.23, ROS-001 0.54, BLU-001 0.53, VER-011 0.51, ROS-021 0.50, VER-001 0.47, VER-019 0.47, VER-008 0.45, NEU-006 0.40 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.75, rif_LDR02_muro_di_parata 1.35 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.04, rif_LDR02_muro_di_parata 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 40% (n=25), rif_LDR02_muro_di_parata 20% (n=41) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.5% [10.7–12.5] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR02_muro_di_parata 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, VER-011 66%, ROS-016 66%, VER-008 66%, VER-001 66%, caccia 66%, BLU-022 34%, collante 34%, NEU-009 34%, BLU-021 34%, NER-014 34%, 11.1 34%; oltre il 60%: ROS-016, VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR02_muro_di_parata |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 66.5 [60–73] (200) |
| rif_LDR02_muro_di_parata | 33.5 [27–40] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.00 | 0.00 | 2.04 / 0.00 | 0.00 | 0.00 | 4.4 (200) | 13 | G 40%, R 60% | 2.21 | 0.76 |
| rif_LDR02_muro_di_parata | 4.38 | 0.00 | 1.43 / 0.00 | 0.00 | 1.33 | 4.9 (198) | 8 | B 77%, K 23% | 2.76 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/2.04/1.66/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.40/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.54/0.29/0.04 | 0.73/0.30/0.65/0.18 | 0.73/0.34/0.13/0.02 | 0.00/0.28/0.00/0.00 | 0.81/0.00/0.31/0.04 | 0.74/0.28/0.47/0.07 | 0.76/1.31/0.06/0.43 | 0.67/1.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.50/0.41/0.13 | 0.28/0.14/0.23/0.09 | 0.00/0.00/0.00/0.00 | 0.70/0.47/0.07/0.30 | 0.61/0.00/0.00/0.00 | 0.80/0.00/0.14/0.04 | 0.64/0.51/0.23/0.07 | 0.75/0.47/0.51/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.00/0.07/0.01 | 0.45/0.03/0.03/0.01 | 0.36/0.08/0.19/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.04/0.01 | 0.35/0.45/0.01/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.16/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.53/0.27/0.22 | 0.80/0.00/0.26/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.00/0.39/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.20/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.33/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.43/1.85/1.17 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.06/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.30/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.04/0.14/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.08/0.17/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.50 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.26 | 0.01 | 0.00 | 0.01 | 0.17 | 0.12 | 0.00 | 0.00 | 0.34 | 0.14 | 0.00 | 0.05 | 0.00 | 0.01 | 0.07 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 0.38 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.78 | 0.01 | 0.06 | 0.04 | 0.11 | 0.13 | 0.12 | 0.09 | 0.10 | 0.04 | 0.03 | 0.02 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 200 | 1.18 | 0.03 | 0.07 | 0.12 | 0.15 | 0.14 | 0.17 | 0.17 | 0.17 | 0.07 | 0.04 | 0.03 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 3 | 0 | 4 |
| 8 | 9 | 3 | 0 | 12 |
| 9 | 15 | 10 | 0 | 25 |
| 10 | 8 | 6 | 0 | 14 |
| 11 | 19 | 17 | 0 | 36 |
| 12 | 20 | 11 | 0 | 31 |
| 13 | 7 | 17 | 0 | 24 |
| 14 | 4 | 13 | 0 | 17 |
| 15 | 16 | 18 | 0 | 34 |
| 16 | 2 | 1 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 52.4% | 0.074 | 0.00 | 0.75 | 0.00 | 0.00 | 2.02 | 0.00 | 0.00 | 0.369 |
| rif_LDR02_muro_di_parata | 200 | 47.2% | 0.062 | 1.35 | 0.00 | 0.00 | 0.00 | 3.75 | 0.00 | 0.00 | 0.560 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 491 | 0.878 | 0.837 | 0.800 | 0.316 | 1780 | 0.778 | 0.208 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 491 | 0.224 | 0.198 | 0.165 | 0.026 | 1780 | 0.190 | 0.063 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | mano | 668 | 1.000 | 0.994 | 0.990 | 0.210 | 2061 | 0.999 | 0.419 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 668 | 0.425 | 0.388 | 0.343 | 0.042 | 2061 | 0.338 | 0.132 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 11.5% | 2.44 | 1.53 | 42.9% | 0.0% | 19.7% | 28.8% | 8.5% | 0.00 | 16.3% | 52.4% | 0.20 | 0.00 |
| rif_LDR02_muro_di_parata | 200 | 11.5% | 2.44 | 1.53 | 19.3% | 0.0% | 34.2% | 42.1% | 16.6% | 0.00 | 14.4% | 47.2% | 0.01 | 0.00 |
| Totale | 400 | 11.5% | 2.44 | 1.53 | 29.0% | 0.0% | 26.9% | 35.4% | 13.5% | 0.00 | 15.6% | 50.4% | 0.10 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

