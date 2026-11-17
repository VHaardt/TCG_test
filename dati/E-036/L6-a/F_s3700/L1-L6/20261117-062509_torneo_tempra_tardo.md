# Torneo v0.2 — /home/claude/e036_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e036_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1712s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 29.6% [28.3–30.9] | 30–45% | ❌ |
| Durata mediana (round) | 11.0 [11.0–11.0] (media 11.14) | 8–11 | ✅ |
| Partite al round 13+ | 32.5% [26.4–39.3] | ≤12% | ❌ |
| Partite oltre il 15 | 0.5% [0.1–2.8] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=77) | 28.6% [19.7–39.5] | 20–35% | ✅ |
| Attacchi con opposizione | 28.0% [26.7–29.2] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 61.0% [59.5–62.4] (con ≥3: 21.4% [20.2–22.7]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.5% [36.1–38.8] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 5.0% [3.4–7.5] (n=436) / 82.0% [77.6–85.7] (n=339) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.0% [13.5–16.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 57.9% [36.3–76.9] (n=19), LDR-01 Risvegliato 78.0% [69.3–84.7] (n=109), LDR-06 Base 66.7% [20.8–93.9] (n=3), LDR-06 Risvegliato 72.2% [65.0–78.4] (n=169) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 35.1% [28.3–42.6] (n=168) | | |
| Attacchi per partita | 24.7 | | |
| Pugno attaccante vuoto / pieno | 50.2% [48.7–51.7] / 14.0% [13.0–15.0] (gemme medie 0.89) | non >90% | |
| Pugno difensore vuoto / pieno | 57.6% [55.5–59.6] / 25.3% [23.5–27.1] (gemme medie 0.26) | non >90% | |
| Reazioni per scontro | 0.08 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1517, 1: 1710, 2: 1174, 3: 369, 4: 112, 5: 42, 6: 7} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 189, 'crepuscolo': 11} | | |
| G1 vince fra le partite finite al Crepuscolo | 45.5% [21.3–72.0] | | |
| G1 vince fra le partite arrivate al round 15 | 50.0% [29.9–70.1] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 35.0% [18.1–56.7] / 57.1% [25.0–84.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 28.6% [8.2–64.1]; 5.0% [0.9–23.6] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 7, '0-0': 3, '1-0': 2, '2-0': 2, '2-3': 2, '0-3': 1, '0-1': 1, '1-1': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=7) | 35.0% [18.1–56.7] / 57.1% [25.0–84.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 7}; 71.4% [35.9–91.8] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 28.6% [8.2–64.1] / 28.6% [8.2–64.1]; 2.00 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–35.4] / 57.1% [25.0–84.2] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=4) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–49.0] / 66.7% [20.8–93.9]; 0.0% [0.0–49.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.8–5.0] / 20.0% [8.1–41.6]; 100.0% [51.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:pronto': 4, 'vinc:atk': 4} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=11) / turno di G2 (n=9) | 0.0% [0.0–25.9] / 0.0% [0.0–29.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=11) | 0.0% [0.0–25.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 25.0% [11.2–46.9] (0.0% [0.0–16.1]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 4, 'rif_LDR01_puntata_e_preda': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR06_ferite_e_caccia 50% (n=20) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 60.0% [53.1–66.5], rif_LDR06_ferite_e_caccia 40.0% [33.5–46.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.334 / 0.082 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.082 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.10 (0.00), rif_LDR06_ferite_e_caccia 0.10 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 34.7% [33.4–36.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 5.14 (328 / 700); 56.5% [55.2–57.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 48.4% [47.3–49.4]; rif_LDR01_puntata_e_preda 52.1%, rif_LDR06_ferite_e_caccia 44.9% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.326 (415) / 0.315 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 120 vittorie), LDR-06 G: 17.0 (49%, 80 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 3.12, VER-020 2.05, LDR-01 1.85, ROS-016 1.46, NER-017 1.06, ROS-018 1.03, VER-008 0.75, NEU-001 0.71, VER-001 0.64, NER-013 0.62, NER-009 0.61, VER-011 0.53 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.99, rif_LDR06_ferite_e_caccia 3.08 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.03, rif_LDR06_ferite_e_caccia 0.20 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 50% (n=10), rif_LDR06_ferite_e_caccia 25% (n=67) | 20–35% |
| M13 | Pugno d'attacco pieno | 14.0% [13.0–15.0] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR06_ferite_e_caccia 0.81; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | VER-008 100%, VER-001 100%, ponte 100%, caccia 100%, VER-011 60%, ROS-016 60%, NEW-B06 40%, NER-017 40%, NEU-001 40%, NER-009 40%, NEU-012 40%, collante 40%; oltre il 60%: VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 60.0 [53–67] (200) |
| rif_LDR06_ferite_e_caccia | 40.0 [33–47] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 3.83 | 0.00 | 1.85 / 0.00 | 0.00 | 0.00 | 4.4 (200) | 13 | G 39%, R 61% | 2.65 | 0.45 |
| rif_LDR06_ferite_e_caccia | 3.86 | 0.00 | 3.12 / 0.14 | 0.00 | 0.27 | 4.2 (196) | 9 | G 51%, K 49% | 2.08 | 1.52 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.85/1.97/0.55 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.43/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.39/0.15/0.10 | 0.76/0.09/0.56/0.25 | 0.70/0.34/0.14/0.06 | 0.00/0.43/0.00/0.00 | 0.69/0.00/0.20/0.09 | 0.71/0.20/0.24/0.11 | 0.80/1.46/0.06/0.61 | 0.67/1.03/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.41/0.33/0.22 | 0.23/0.09/0.15/0.17 | 0.00/0.00/0.00/0.00 | 0.67/0.65/0.02/0.52 | 0.60/0.00/0.00/0.00 | 0.75/0.00/0.13/0.07 | 0.77/0.53/0.22/0.10 | 0.65/0.28/0.32/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.00/0.07/0.01 | 0.42/0.03/0.09/0.03 | 0.34/0.05/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.00/0.07/0.01 | 0.36/0.51/0.00/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.23/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.64/0.07/0.54 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.57/0.37/0.42/0.25 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/3.12/1.91/0.77 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.47/0.22/0.09 | 0.35/0.36/0.10/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.08/0.27/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.25/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.51/0.34/0.02/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.99/0.04/0.49 | 0.33/0.03/0.04/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.71/0.18/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.18/0.24/0.04/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.15/0.06 | 0.23/0.46/0.10/0.05 | 0.47/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.12 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.01 | 0.00 | 0.04 | 0.15 | 0.12 | 0.00 | 0.00 | 0.28 | 0.10 | 0.00 | 0.02 | 0.00 | 0.01 | 0.04 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.59 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.73 | 0.00 | 0.01 | 0.04 | 0.04 | 0.10 | 0.12 | 0.11 | 0.12 | 0.07 | 0.06 | 0.02 | 0.03 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.94 | 0.00 | 0.06 | 0.04 | 0.08 | 0.14 | 0.14 | 0.10 | 0.14 | 0.10 | 0.04 | 0.05 | 0.01 | 0.04 | 0.00 | 0.00 | 0.81 | 0.13 | 0.10 | 0.14 | 0.10 | 0.12 | 0.10 | 0.05 | 0.03 | 0.03 | 0.00 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca |
|---|---|
| rif_LDR01_puntata_e_preda | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.39 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 2 | 0 | 0 | 2 |
| 7 | 2 | 3 | 0 | 5 |
| 8 | 9 | 10 | 0 | 19 |
| 9 | 17 | 6 | 0 | 23 |
| 10 | 18 | 18 | 0 | 36 |
| 11 | 15 | 16 | 0 | 31 |
| 12 | 7 | 11 | 0 | 18 |
| 13 | 14 | 17 | 0 | 31 |
| 14 | 6 | 8 | 0 | 14 |
| 15 | 9 | 10 | 0 | 19 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 52.1% | 0.086 | 0.00 | 0.99 | 0.00 | 0.00 | 3.31 | 0.00 | 0.00 | 0.323 |
| rif_LDR06_ferite_e_caccia | 200 | 44.9% | 0.078 | 0.82 | 2.25 | 0.00 | 0.00 | 4.82 | 0.00 | 0.00 | 0.346 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 558 | 0.864 | 0.783 | 0.738 | 0.366 | 2057 | 0.740 | 0.169 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 558 | 0.142 | 0.138 | 0.125 | 0.038 | 2057 | 0.103 | 0.038 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 401 | 0.883 | 0.810 | 0.761 | 0.399 | 1915 | 0.778 | 0.215 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 401 | 0.267 | 0.219 | 0.170 | 0.052 | 1915 | 0.182 | 0.065 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 5.5% | 2.06 | 1.76 | 37.9% | 0.5% | 19.2% | 25.9% | 3.9% | 0.00 | 15.1% | 52.1% | 0.06 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 5.5% | 2.06 | 1.76 | 30.8% | 0.5% | 18.2% | 30.0% | 10.7% | 0.00 | 13.4% | 44.9% | 0.01 | 0.00 |
| Totale | 400 | 5.5% | 2.06 | 1.76 | 33.6% | 0.5% | 18.7% | 28.0% | 7.9% | 0.00 | 14.2% | 48.4% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 200 | 0.267 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.81 |
| rif_LDR06_ferite_e_caccia | 200 | 0.294 | 0.041 | 0.0% | 0.0% | 0.34 | 0.04 | 0.08 | 0.00 | 0.00 | 0.00 | 4.43 |

