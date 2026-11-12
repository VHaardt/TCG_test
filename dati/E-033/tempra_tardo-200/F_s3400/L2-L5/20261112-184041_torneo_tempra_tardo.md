# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1522s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 44.3% [43.0–45.7] | 30–45% | ✅ |
| Durata mediana (round) | 13.0 [12.0–13.0] (media 12.51) | 8–11 | ❌ |
| Partite al round 13+ | 54.5% [47.6–61.3] | ≤12% | ❌ |
| Partite oltre il 15 | 3.5% [1.7–7.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=56) | 23.2% [14.1–35.8] | 20–35% | ✅ |
| Attacchi con opposizione | 36.1% [34.8–37.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 62.9% [61.5–64.2] (con ≥3: 26.4% [25.1–27.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 35.7% [34.4–37.0] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 16.1% [12.9–20.0] (n=409) / 90.0% [85.4–93.2] (n=230) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.0% [9.7–12.5] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 47.4% [27.3–68.3] (n=19), LDR-02 Risvegliato 89.4% [83.0–93.6] (n=132), LDR-05 Base 57.4% [43.3–70.5] (n=47), LDR-05 Risvegliato 72.0% [61.0–80.9] (n=75) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 58.9% [51.4–66.1] (n=168) | | |
| Attacchi per partita | 26.2 | | |
| Pugno attaccante vuoto / pieno | 53.2% [51.8–54.6] / 9.3% [8.6–10.2] (gemme medie 0.91) | non >90% | |
| Pugno difensore vuoto / pieno | 49.8% [47.9–51.6] / 25.6% [24.0–27.2] (gemme medie 0.36) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 1898, 1: 1656, 2: 1084, 3: 400, 4: 160, 5: 43, 6: 4, 7: 2} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 171, 'crepuscolo': 29} | | |
| G1 vince fra le partite finite al Crepuscolo | 48.3% [31.4–65.6] | | |
| G1 vince fra le partite arrivate al round 15 | 47.2% [34.4–60.3] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 26.4% [16.4–39.6] / 64.3% [38.8–83.7] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 28.6% [11.7–54.6]; 13.2% [6.5–24.8] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 7, '3-2': 6, '1-1': 5, '2-3': 4, '1-0': 4, '0-0': 4, '3-3': 4, '2-0': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=17) | 32.1% [21.1–45.5] / 52.9% [31.0–73.8] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 14, 16: 3}; 58.8% [36.0–78.4] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 47.1% [26.2–69.0] / 29.4% [13.3–53.1]; 2.29 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–18.4] / 100.0% [81.6–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=9) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–29.9] / 62.5% [30.6–86.3]; 0.0% [0.0–29.9] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.5% [2.4–8.3] / 17.0% [9.2–29.2]; 100.0% [70.1–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 6, 'perd:pronto': 2, 'perd:rim': 1, 'vinc:atk': 9} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=19) / turno di G2 (n=11) | 0.0% [0.0–16.8] / 0.0% [0.0–25.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=19) | 0.0% [0.0–16.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 34.0% [22.7–47.4] (7.5% [3.0–17.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 9, 'rif_LDR02_muro_di_parata': 8} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 47% (n=53) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 28.5% [22.7–35.1], rif_LDR05_scudi_armati 71.5% [64.9–77.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.504 / 0.091 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.087 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.20 (0.00), rif_LDR05_scudi_armati 0.17 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 23.2% [22.1–24.4] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 63.9% [62.6–65.2] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.7% [50.7–52.7]; rif_LDR02_muro_di_parata 48.9%, rif_LDR05_scudi_armati 53.6% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.1% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.315 (477) / 0.342 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 57 vittorie), LDR-05 R: 18.0 (49%, 143 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.67, LDR-02 1.45, BLU-015 1.02, BLU-001 0.72, ROS-018 0.62, ROS-020 0.57, ROS-021 0.52, NEU-013 0.49, BLU-008 0.43, ROS-007 0.36, ROS-001 0.35, BLU-023 0.34 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.61, rif_LDR05_scudi_armati 0.10 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 13% (n=39), rif_LDR05_scudi_armati 47% (n=17) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.3% [8.6–10.2] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | BLU-021 100%, NEU-009 100%, collante 100%, ponte 100%, NEU-013 72%, ROS-020 72%, BLU-008 72%, BLU-010 72%, BLU-022 28%, NEU-015 28%, 11.1 28%, RS 28%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 28.5 [23–35] (200) |
| rif_LDR05_scudi_armati | 71.5 [65–77] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.71 | 0.00 | 1.45 / 0.00 | 0.00 | 1.30 | 5.0 (198) | 8 | B 77%, K 23% | 2.54 | 0.00 |
| rif_LDR05_scudi_armati | 4.37 | 0.00 | 3.67 / 0.00 | 0.00 | 0.75 | 4.3 (199) | 13 | B 47%, R 53% | 2.10 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.86/0.35/0.22 | 0.78/0.00/0.24/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.80/0.00/0.32/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.23/0.00/0.00 | 0.00/0.24/0.00/0.00 | 0.00/0.44/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.45/1.61/1.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.37/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.10/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.43/0.12/0.17/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.67/1.58/0.24 | 0.69/0.57/0.14/0.04 | 0.71/0.00/0.24/0.07 | 0.63/0.43/0.26/0.07 | 0.66/0.14/0.28/0.08 | 0.71/0.00/0.23/0.07 | 0.72/1.02/0.33/0.21 | 0.00/0.41/0.00/0.00 | 0.00/0.43/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.49/0.39/0.14 | 0.78/0.35/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.75/0.28/0.17/0.03 | 0.00/0.36/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.66/0.26/0.30/0.12 | 0.00/0.00/0.00/0.00 | 0.38/0.62/0.00/0.00 | 0.80/0.57/0.44/0.20 | 0.48/0.52/0.32/0.14 | 0.24/0.13/0.17/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.00/0.06/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.14/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.02/0.01 | 0.35/0.01/0.01/0.00 | 0.29/0.10/0.09/0.06 | 0.34/0.33/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.34 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.20 | 0.00 | 0.08 | 0.00 | 0.01 | 0.01 | 0.03 | 0.04 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.15 | 0.00 | 0.00 | 0.21 | 0.30 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.14 | 0.01 | 0.07 | 0.07 | 0.18 | 0.15 | 0.17 | 0.15 | 0.12 | 0.03 | 0.07 | 0.06 | 0.04 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.68 | 0.03 | 0.04 | 0.07 | 0.06 | 0.12 | 0.08 | 0.10 | 0.07 | 0.03 | 0.03 | 0.03 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 3 | 0 | 3 |
| 8 | 5 | 1 | 0 | 6 |
| 9 | 9 | 2 | 0 | 11 |
| 10 | 10 | 9 | 0 | 19 |
| 11 | 19 | 11 | 0 | 30 |
| 12 | 12 | 10 | 0 | 22 |
| 13 | 17 | 19 | 0 | 36 |
| 14 | 6 | 14 | 0 | 20 |
| 15 | 19 | 27 | 0 | 46 |
| 16 | 6 | 1 | 0 | 7 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 48.9% | 0.076 | 1.61 | 0.00 | 0.00 | 0.00 | 3.60 | 0.00 | 0.00 | 0.580 |
| rif_LDR05_scudi_armati | 200 | 53.6% | 0.109 | 0.10 | 0.00 | 0.00 | 0.00 | 1.64 | 0.00 | 0.00 | 0.414 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 799 | 1.000 | 0.999 | 0.999 | 0.218 | 2034 | 0.998 | 0.415 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 799 | 0.516 | 0.479 | 0.433 | 0.050 | 2034 | 0.381 | 0.153 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 611 | 0.903 | 0.884 | 0.874 | 0.376 | 1803 | 0.840 | 0.241 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 611 | 0.190 | 0.183 | 0.178 | 0.054 | 1803 | 0.123 | 0.042 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 14.5% | 2.78 | 1.60 | 15.0% | 0.0% | 33.3% | 42.8% | 17.0% | 0.00 | 17.2% | 48.9% | 0.01 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 14.5% | 2.78 | 1.60 | 52.5% | 0.0% | 18.2% | 32.8% | 14.3% | 0.00 | 17.3% | 53.6% | 0.14 | 0.00 |
| Totale | 400 | 14.5% | 2.78 | 1.60 | 29.1% | 0.0% | 25.8% | 37.7% | 15.9% | 0.00 | 17.2% | 51.7% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

