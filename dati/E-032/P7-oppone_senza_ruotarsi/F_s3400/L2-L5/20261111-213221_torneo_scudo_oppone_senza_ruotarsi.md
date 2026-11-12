# Torneo v0.2 — /home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json

- Regole `v0.2`, configurazione `/home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json`; differenze da B0: {'pugno': 'sequenziale', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L')}
- IA: forte:30; partite: 200; tempo 3332s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 43.1% [41.7–44.4] | 30–45% | ✅ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 12.96) | 8–11 | ❌ |
| Partite al round 13+ | 65.5% [58.7–71.7] | ≤12% | ❌ |
| Partite oltre il 15 | 8.5% [5.4–13.2] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=64) | 25.0% [16.0–36.8] | 20–35% | ✅ |
| Attacchi con opposizione | 38.5% [37.2–39.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 64.5% [63.2–65.8] (con ≥3: 25.8% [24.6–27.0]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 33.6% [32.4–34.9] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–0.9] (n=407) / 85.3% [80.0–89.3] (n=224) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.8% [9.4–12.3] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Risvegliato 86.0% [77.9–91.5] (n=100), LDR-05 Risvegliato 74.7% [64.9–82.5] (n=91) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 69.5% [62.1–76.0] (n=164) | | |
| Attacchi per partita | 26.3 | | |
| Pugno attaccante vuoto / pieno | 50.5% [49.1–51.9] / 9.7% [8.9–10.5] (gemme medie 1.01) | non >90% | |
| Pugno difensore vuoto / pieno | 48.1% [46.3–50.0] / 25.8% [24.2–27.4] (gemme medie 0.38) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1745, 1: 1707, 2: 1134, 3: 434, 4: 172, 5: 64, 6: 8} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'crepuscolo': 70, 'colpo_finale': 130} | | |
| G1 vince fra le partite finite al Crepuscolo | 55.7% [44.1–66.8] | | |
| G1 vince fra le partite arrivate al round 15 | 54.3% [43.5–64.7] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 29.6% [20.8–40.3] / 41.7% [24.5–61.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 50.0% [31.4–68.6]; 21.0% [13.5–31.1] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'1-0': 12, '2-2': 10, '0-0': 6, '3-2': 6, '2-0': 6, '2-1': 5, '2-3': 4, '1-1': 4} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=39) | 48.1% [37.6–58.9] / 46.2% [31.6–61.4] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 15, 15: 24}; 53.8% [38.6–68.4] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 76.9% [61.7–87.4] / 25.6% [14.6–41.1]; 2.38 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–9.0] / 97.4% [86.8–99.5] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=18) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–17.6] / 47.6% [28.3–67.6]; 0.0% [0.0–17.6] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 9.0% [5.8–13.8] / 22.2% [14.5–32.4]; 100.0% [82.4–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 16, 'perd:pronto': 2, 'vinc:atk': 18} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=29) / turno di G2 (n=22) | 0.0% [0.0–11.7] / 0.0% [0.0–14.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=29) | 0.0% [0.0–11.7] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 56.8% [45.9–67.0] (23.5% [15.6–33.8]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 26, 'rif_LDR02_muro_di_parata': 13} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 54% (n=81) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 30.5% [24.5–37.2], rif_LDR05_scudi_armati 69.5% [62.8–75.5]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.507 / 0.096 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.093 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.17 (0.00), rif_LDR05_scudi_armati 0.20 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 21.0% [20.0–22.2] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 61.5% [60.2–62.8] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.7% [50.7–52.6]; rif_LDR02_muro_di_parata 47.2%, rif_LDR05_scudi_armati 54.6% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 7.5% [6.5–8.8] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.291 (508) / 0.318 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 61 vittorie), LDR-05 R: 18.0 (49%, 139 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.63, LDR-02 1.55, BLU-015 1.15, ROS-018 0.88, BLU-001 0.74, ROS-021 0.72, ROS-020 0.68, NEU-013 0.54, BLU-008 0.45, ROS-019 0.42, BLU-023 0.40, BLU-016 0.39 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.45, rif_LDR05_scudi_armati 0.06 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 10% (n=42), rif_LDR05_scudi_armati 55% (n=22) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.7% [8.9–10.5] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, BLU-021 100%, NEU-009 100%, NEU-013 70%, ROS-020 70%, BLU-008 70%, BLU-010 70%, NEU-003 30%, RS 30%, 11.1 30%, NER-014 30%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 30.5 [25–37] (200) |
| rif_LDR05_scudi_armati | 69.5 [63–75] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.83 | 0.00 | 1.55 / 0.00 | 0.00 | 1.56 | 5.1 (199) | 8 | B 78%, K 22% | 2.82 | 0.00 |
| rif_LDR05_scudi_armati | 4.50 | 0.00 | 3.63 / 0.00 | 0.00 | 0.76 | 4.3 (200) | 13 | B 47%, R 53% | 2.01 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.85/0.96/0.23/0.20 | 0.86/0.00/0.18/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.00/0.31/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.23/0.00/0.00 | 0.00/0.30/0.00/0.00 | 0.00/0.34/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.55/1.52/1.49 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.09/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.33/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.10/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.17/0.16/0.22 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.63/1.64/0.23 | 0.67/0.53/0.07/0.07 | 0.76/0.00/0.20/0.06 | 0.66/0.45/0.21/0.09 | 0.66/0.14/0.21/0.09 | 0.77/0.00/0.21/0.12 | 0.80/1.15/0.34/0.21 | 0.00/0.53/0.00/0.00 | 0.00/0.49/0.00/0.00 | 0.00/0.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.54/0.28/0.17 | 0.78/0.34/0.17/0.03 | 0.00/0.00/0.00/0.00 | 0.78/0.33/0.12/0.04 | 0.00/0.39/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.20/0.22/0.15 | 0.00/0.00/0.00/0.00 | 0.42/0.88/0.00/0.00 | 0.79/0.68/0.46/0.30 | 0.54/0.72/0.36/0.27 | 0.24/0.17/0.17/0.11 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.00/0.06/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.07/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.01/0.00 | 0.38/0.03/0.04/0.01 | 0.30/0.12/0.10/0.06 | 0.38/0.42/0.14/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.54 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.49 | 0.00 | 0.09 | 0.01 | 0.01 | 0.03 | 0.03 | 0.01 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.28 | 0.43 | 0.15 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.34 | 0.02 | 0.04 | 0.09 | 0.18 | 0.17 | 0.17 | 0.19 | 0.14 | 0.12 | 0.09 | 0.07 | 0.06 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.93 | 0.01 | 0.02 | 0.06 | 0.09 | 0.12 | 0.12 | 0.12 | 0.11 | 0.07 | 0.08 | 0.06 | 0.06 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 4 | 0 | 4 |
| 8 | 7 | 3 | 0 | 10 |
| 9 | 8 | 9 | 0 | 17 |
| 10 | 8 | 3 | 0 | 11 |
| 11 | 11 | 1 | 0 | 12 |
| 12 | 6 | 9 | 0 | 15 |
| 13 | 12 | 10 | 0 | 22 |
| 14 | 11 | 17 | 0 | 28 |
| 15 | 36 | 28 | 0 | 64 |
| 16 | 8 | 9 | 0 | 17 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 47.2% | 0.072 | 1.45 | 0.00 | 0.00 | 0.00 | 4.01 | 0.00 | 0.00 | 0.588 |
| rif_LDR05_scudi_armati | 200 | 54.6% | 0.124 | 0.06 | 0.00 | 0.00 | 0.00 | 2.12 | 0.00 | 0.00 | 0.409 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 833 | 1.000 | 0.999 | 0.999 | 0.206 | 2035 | 0.997 | 0.419 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 833 | 0.521 | 0.487 | 0.445 | 0.042 | 2035 | 0.387 | 0.161 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 636 | 0.904 | 0.881 | 0.865 | 0.404 | 1760 | 0.806 | 0.223 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 636 | 0.167 | 0.162 | 0.153 | 0.063 | 1760 | 0.120 | 0.040 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 35.0% | 2.72 | 2.06 | 22.6% | 0.0% | 32.3% | 44.8% | 16.9% | 0.00 | 17.5% | 47.2% | 0.05 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 35.0% | 2.72 | 2.06 | 39.4% | 0.0% | 20.7% | 31.8% | 16.8% | 0.00 | 16.4% | 54.6% | 0.12 | 0.00 |
| Totale | 400 | 35.0% | 2.72 | 2.06 | 28.4% | 0.0% | 26.5% | 38.2% | 16.9% | 0.00 | 16.8% | 51.7% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.300 | 0.229 | 9.4% | 12.3% | 1.75 | 0.00 | 0.93 | 0.04 | 0.00 | 0.00 | 3.77 |
| rif_LDR05_scudi_armati | 200 | 0.487 | 0.253 | 6.2% | 11.9% | 2.10 | 0.00 | 0.65 | 0.92 | 0.00 | 0.00 | 5.08 |

