# Torneo v0.2 — /root/in37/dati/E-037-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in37/dati/E-037-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 1706s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 41.3% [39.4–43.2] | 30–45% | ✅ |
| Durata mediana (round) | 14.0 [13.0–15.0] (media 13.20) | 8–11 | ❌ |
| Partite al round 13+ | 62.0% [52.2–70.9] | ≤12% | ❌ |
| Partite oltre il 15 | 11.0% [6.3–18.6] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=26) | 34.6% [19.4–53.8] | 20–35% | ✅ |
| Attacchi con opposizione | 46.3% [44.4–48.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 75.3% [73.5–76.9] (con ≥3: 38.4% [36.5–40.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 33.2% [31.4–35.0] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 11.4% [7.7–16.5] (n=202) / 92.3% [85.6–96.1] (n=104) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.3% [9.3–13.6] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 63.6% [35.4–84.8] (n=11), LDR-02 Risvegliato 70.9% [57.9–81.2] (n=55), LDR-05 Base 50.0% [25.4–74.6] (n=12), LDR-05 Risvegliato 73.2% [58.1–84.3] (n=41) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 63.2% [52.7–72.6] (n=87) | | |
| Attacchi per partita | 25.7 | | |
| Pugno attaccante vuoto / pieno | 52.0% [50.0–54.0] / 10.6% [9.4–11.9] (gemme medie 0.99) | non >90% | |
| Pugno difensore vuoto / pieno | 52.9% [50.1–55.7] / 25.4% [23.1–27.9] (gemme medie 0.30) | non >90% | |
| Reazioni per scontro | 0.11 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 952, 1: 852, 2: 463, 3: 199, 4: 69, 5: 28, 6: 3} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 78, 'crepuscolo': 22} | | |
| G1 vince fra le partite finite al Crepuscolo | 59.1% [38.7–76.7] | | |
| G1 vince fra le partite arrivate al round 15 | 45.5% [31.7–59.9] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 13.6% [6.4–26.7] / 66.7% [30.0–90.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [9.7–70.0]; 25.0% [14.6–39.4] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-3': 8, '2-2': 3, '1-1': 3, '3-2': 3, '4-2': 3, '3-3': 3, '4-4': 3, '4-5': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=9) | 20.5% [11.2–34.5] / 66.7% [35.4–87.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 6, 17: 1, 16: 2}; 66.7% [35.4–87.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 66.7% [35.4–87.9] / 22.2% [6.3–54.7]; 1.44 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–29.9] / 100.0% [70.1–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=6) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–39.0] / 66.7% [20.8–93.9]; 0.0% [0.0–39.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 6.0% [2.8–12.5] / 13.6% [6.4–26.7]; 100.0% [61.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 5, 'perd:rim': 1, 'vinc:atk': 6} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=13) / turno di G2 (n=15) | 0.0% [0.0–22.8] / 0.0% [0.0–20.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=13) | 0.0% [0.0–22.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 45.5% [31.7–59.9] (15.9% [7.9–29.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 5, 'rif_LDR02_muro_di_parata': 4} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 45% (n=44) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 41.0% [31.9–50.8], rif_LDR05_scudi_armati 59.0% [49.2–68.1]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.512 / 0.112 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.108 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.15 (0.00), rif_LDR05_scudi_armati 0.10 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 27.8% [26.1–29.6] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 53.7% [51.7–55.6] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 58.4% [57.3–59.6]; rif_LDR02_muro_di_parata 58.4%, rif_LDR05_scudi_armati 58.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.2% [0.0–0.6] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.312 (254) / 0.311 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 41 vittorie), LDR-05 R: 18.0 (49%, 59 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-02 1.55, BLU-015 0.88, BLU-005 0.80, LDR-05 0.77, BLU-001 0.76, NEW-I04 0.75, ROS-021 0.56, ROS-020 0.55, ROS-001 0.53, BLU-021 0.52, ROS-018 0.48, NEU-004 0.44 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.52, rif_LDR05_scudi_armati 0.06 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 35% (n=17), rif_LDR05_scudi_armati 33% (n=9) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.6% [9.4–11.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, collante 100%, BLU-021 100%, NEU-009 100%, ROS-020 59%, BLU-010 59%, NEU-013 59%, BLU-008 59%, NEU-015 41%, NER-014 41%, RS 41%, NEU-003 41%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 41.0 [32–51] (100) |
| rif_LDR05_scudi_armati | 59.0 [49–68] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.38 | 0.00 | 1.55 / 0.00 | 0.00 | 1.35 | 5.5 (98) | 8 | B 85%, K 15% | 2.02 | 0.00 |
| rif_LDR05_scudi_armati | 4.22 | 0.00 | 0.77 / 0.00 | 0.00 | 1.00 | 4.5 (99) | 12 | B 47%, R 53% | 1.91 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR02_muro_di_parata | 1.55 | 0.00 |
| rif_LDR05_scudi_armati | 0.00 | 0.77 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.90/0.92/0.32/0.15 | 0.68/0.00/0.06/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.00/0.31/0.37 | 0.00/0.00/0.00/0.00 | 0.00/0.51/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.31/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.55/1.56/1.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 1.02/0.00/0.13/0.07 | 0.96/0.80/0.04/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.41/0.44/0.04/0.00 | 0.51/0.00/0.15/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.16/0.18/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.75/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/0.77/1.50/0.61 | 0.76/0.59/0.15/0.02 | 0.76/0.00/0.11/0.07 | 0.64/0.42/0.23/0.09 | 0.63/0.19/0.23/0.12 | 0.67/0.00/0.14/0.08 | 0.66/0.88/0.19/0.35 | 0.00/0.53/0.00/0.00 | 0.00/0.31/0.00/0.00 | 0.00/0.09/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.70/0.32/0.21/0.12 | 0.81/0.53/0.23/0.10 | 0.00/0.00/0.00/0.00 | 0.71/0.44/0.20/0.07 | 0.00/0.24/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.22/0.21/0.14 | 0.00/0.00/0.00/0.00 | 0.33/0.48/0.00/0.00 | 0.65/0.55/0.40/0.35 | 0.56/0.56/0.27/0.37 | 0.20/0.09/0.10/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.76/0.00/0.06/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.28/0.00/0.01/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.03/0.00 | 0.44/0.05/0.07/0.03 | 0.40/0.20/0.12/0.12 | 0.39/0.38/0.09/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.47 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.06 | 0.00 | 0.09 | 0.00 | 0.00 | 0.01 | 0.02 | 0.04 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.03 | 0.00 | 0.02 | 0.00 | 0.00 | 0.11 | 0.00 | 0.00 | 0.18 | 0.31 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.02 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 0.87 | 0.04 | 0.06 | 0.04 | 0.12 | 0.11 | 0.19 | 0.08 | 0.09 | 0.04 | 0.05 | 0.04 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 0.90 | 0.05 | 0.03 | 0.02 | 0.05 | 0.11 | 0.15 | 0.13 | 0.16 | 0.06 | 0.04 | 0.03 | 0.02 | 0.04 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 1 | 0 | 0 | 1 |
| 8 | 0 | 4 | 0 | 4 |
| 9 | 3 | 0 | 0 | 3 |
| 10 | 5 | 1 | 0 | 6 |
| 11 | 6 | 6 | 0 | 12 |
| 12 | 8 | 4 | 0 | 12 |
| 13 | 0 | 6 | 0 | 6 |
| 14 | 4 | 8 | 0 | 12 |
| 15 | 14 | 19 | 0 | 33 |
| 16 | 6 | 4 | 0 | 10 |
| 17 | 0 | 1 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 58.4% | 0.127 | 1.52 | 0.00 | 0.00 | 0.00 | 3.66 | 0.00 | 0.00 | 0.529 |
| rif_LDR05_scudi_armati | 100 | 58.5% | 0.095 | 0.06 | 0.00 | 0.00 | 0.00 | 2.89 | 0.00 | 0.00 | 0.400 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 292 | 0.993 | 0.966 | 0.914 | 0.281 | 1048 | 0.978 | 0.397 | 0.150 | 0.070 |
| rif_LDR02_muro_di_parata | Cicatrice | 292 | 0.240 | 0.195 | 0.144 | 0.045 | 1048 | 0.239 | 0.074 | 0.010 | 0.002 |
| rif_LDR05_scudi_armati | mano | 297 | 0.906 | 0.889 | 0.879 | 0.360 | 929 | 0.842 | 0.234 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 297 | 0.202 | 0.192 | 0.182 | 0.034 | 929 | 0.174 | 0.058 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 22.0% | 2.90 | 1.36 | 34.4% | 0.0% | 18.3% | 36.8% | 12.6% | 0.00 | 17.4% | 58.4% | 0.01 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 22.0% | 2.90 | 1.36 | 41.7% | 0.0% | 19.0% | 34.8% | 18.1% | 0.00 | 16.0% | 58.5% | 0.10 | 0.00 |
| Totale | 200 | 22.0% | 2.90 | 1.36 | 37.5% | 0.0% | 18.7% | 35.8% | 15.0% | 0.00 | 16.7% | 58.4% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 100 | 0.440 | 0.287 | 0.3% | 0.5% | 1.79 | 0.00 | 1.13 | 0.01 | 0.00 | 0.00 | 3.97 |
| rif_LDR05_scudi_armati | 100 | 0.489 | 0.242 | 0.0% | 0.0% | 1.69 | 0.00 | 0.94 | 0.92 | 0.00 | 0.00 | 4.55 |

