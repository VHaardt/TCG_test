# Torneo v0.2 — /home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json

- Regole `v0.2`, configurazione `/home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json`; differenze da B0: {'pugno': 'sequenziale', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L')}
- IA: forte:30; partite: 200; tempo 1555s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 40.2% [38.8–41.6] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [11.0–12.0] (media 11.45) | 8–11 | ✅ |
| Partite al round 13+ | 43.0% [36.3–49.9] | ≤12% | ❌ |
| Partite oltre il 15 | 1.5% [0.5–4.3] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=75) | 18.7% [11.5–28.9] | 20–35% | ❌ |
| Attacchi con opposizione | 31.3% [30.0–32.7] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 64.7% [63.3–66.1] (con ≥3: 24.2% [23.0–25.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.0% [32.7–35.4] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–1.2] (n=325) / 82.7% [78.0–86.5] (n=306) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 15.9% [14.2–17.8] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Risvegliato 98.8% [95.9–99.7] (n=173), LDR-04 Risvegliato 81.2% [71.3–88.3] (n=80) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 47.3% [40.0–54.8] (n=169) | | |
| Attacchi per partita | 23.4 | | |
| Pugno attaccante vuoto / pieno | 53.4% [51.9–54.9] / 11.7% [10.8–12.7] (gemme medie 0.90) | non >90% | |
| Pugno difensore vuoto / pieno | 57.9% [55.8–59.9] / 22.7% [21.1–24.5] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1417, 1: 1713, 2: 999, 3: 374, 4: 128, 5: 42, 6: 6} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 163, 'crepuscolo': 37} | | |
| G1 vince fra le partite finite al Crepuscolo | 43.2% [28.7–59.1] | | |
| G1 vince fra le partite arrivate al round 15 | 38.6% [25.7–53.4] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 45.5% [31.7–59.9] / 40.0% [21.9–61.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 15.0% [5.2–36.0]; 6.8% [2.3–18.2] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-1': 9, '2-2': 6, '2-1': 6, '0-0': 4, '1-1': 4, '1-0': 3, '2-0': 3, '3-0': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=23) | 52.3% [37.9–66.2] / 43.5% [25.6–63.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 3, 15: 20}; 87.0% [67.9–95.5] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 87.0% [67.9–95.5] / 8.7% [2.4–26.8]; 2.04 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–14.3] / 100.0% [85.7–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=10) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–27.8] / 15.4% [4.3–42.2]; 0.0% [0.0–27.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.0% [2.7–9.0] / 22.7% [12.8–37.0]; 100.0% [72.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 7, 'perd:pronto': 2, 'perd:rim': 1, 'vinc:atk': 10} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=27) / turno di G2 (n=23) | 0.0% [0.0–12.5] / 0.0% [0.0–14.3] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=27) | 0.0% [0.0–12.5] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 75.0% [60.6–85.4] (40.9% [27.7–55.6]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 15, 'rif_LDR03_sanguinare_per_accendere': 8} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR04_stanca_e_smonta 39% (n=44) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 51.0% [44.1–57.8], rif_LDR04_stanca_e_smonta 49.0% [42.2–55.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.365 / 0.086 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.086 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.07 (0.03), rif_LDR04_stanca_e_smonta 0.08 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 32.0% [30.7–33.3] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.13 (152 / 274); 62.2% [60.8–63.6] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 54.1% [53.1–55.1]; rif_LDR03_sanguinare_per_accendere 55.5%, rif_LDR04_stanca_e_smonta 52.4% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 3.8% [2.9–4.9] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.328 (45) / 0.317 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 102 vittorie), LDR-04 B: 14.0 (40%, 98 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 5.45, NER-017 1.35, ROS-019 1.23, NER-001 1.03, NER-006 0.94, NER-008 0.89, BLU-015 0.85, BLU-023 0.77, NER-013 0.76, ROS-011 0.70, NER-010 0.69, VER-008 0.62 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.32, rif_LDR04_stanca_e_smonta 2.35 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR04_stanca_e_smonta 0.23 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 19% (n=63), rif_LDR04_stanca_e_smonta 17% (n=12) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.7% [10.8–12.7] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.76, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | caccia 100%, ponte 100%, NER-010 51%, ROS-011 51%, NER-009 51%, NER-017 51%, collante 49%, NEU-009 49%, VER-008 49%, NEU-003 49%, NEU-011 49%, BLU-010 49%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 51.0 [44–58] (200) |
| rif_LDR04_stanca_e_smonta | 49.0 [42–56] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.35 | 0.00 | 0.00 / 0.00 | 2.99 | 0.00 | 4.9 (198) | 10 | K 61%, R 39% | 2.08 | 0.35 |
| rif_LDR04_stanca_e_smonta | 4.80 | 2.20 | 5.45 / 0.00 | 0.00 | 0.47 | 4.7 (194) | 8 | B 42%, G 58% | 2.42 | 0.56 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.11/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.55/0.63 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/1.03/0.46/0.28 | 0.83/0.94/0.20/0.07 | 0.00/0.00/0.00/0.00 | 0.06/0.00/0.00/0.00 | 0.40/0.19/0.28/0.19 | 0.00/0.20/0.00/0.00 | 0.00/0.09/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.03/0.01 | 0.00/0.00/0.00/0.00 | 0.34/0.12/0.17/0.07 | 0.73/1.23/0.40/0.47 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.11/0.06 | 0.31/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.54/0.09/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.17/0.14/0.14 | 0.29/0.00/0.07/0.04 | 0.78/0.85/0.29/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.77/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.40/0.01/0.26 | 0.77/0.00/0.00/0.00 | 0.63/0.00/0.07/0.05 | 0.00/0.00/0.00/0.00 | 0.34/0.41/0.24/0.20 | 0.00/0.31/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/5.45/1.60/0.46 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.22/0.23/0.02/0.10 | 0.00/0.00/0.00/0.00 | 0.41/0.29/0.01/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.58/0.06/0.06/0.04 | 0.30/0.00/0.01/0.03 | 0.32/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.60/0.62/0.01/0.26 | 0.29/0.03/0.03/0.01 | 0.32/0.00/0.04/0.02 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.94 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.17 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.47 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 1.26 | 0.00 | 0.01 | 0.06 | 0.10 | 0.15 | 0.14 | 0.14 | 0.19 | 0.10 | 0.10 | 0.09 | 0.10 | 0.04 | 0.01 | 0.01 | 1.76 | 0.26 | 0.23 | 0.35 | 0.26 | 0.09 | 0.14 | 0.19 | 0.10 | 0.04 | 0.07 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 0.92 | 0.00 | 0.01 | 0.03 | 0.04 | 0.10 | 0.10 | 0.14 | 0.14 | 0.11 | 0.09 | 0.09 | 0.07 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 1 | 0 | 0 | 1 |
| 6 | 1 | 2 | 0 | 3 |
| 7 | 5 | 12 | 0 | 17 |
| 8 | 11 | 9 | 0 | 20 |
| 9 | 11 | 11 | 0 | 22 |
| 10 | 9 | 13 | 0 | 22 |
| 11 | 7 | 9 | 0 | 16 |
| 12 | 3 | 10 | 0 | 13 |
| 13 | 10 | 4 | 0 | 14 |
| 14 | 7 | 21 | 0 | 28 |
| 15 | 17 | 24 | 0 | 41 |
| 16 | 0 | 3 | 0 | 3 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 55.5% | 0.066 | 0.65 | 0.68 | 0.00 | 0.00 | 4.05 | 0.00 | 0.00 | 0.501 |
| rif_LDR04_stanca_e_smonta | 200 | 52.4% | 0.100 | 1.90 | 0.46 | 0.00 | 0.00 | 1.97 | 0.00 | 0.00 | 0.265 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 442 | 0.962 | 0.950 | 0.941 | 0.265 | 1549 | 0.900 | 0.362 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 442 | 0.274 | 0.265 | 0.253 | 0.034 | 1549 | 0.207 | 0.082 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | mano | 524 | 0.828 | 0.758 | 0.677 | 0.483 | 2164 | 0.693 | 0.121 | 0.000 | 0.000 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 524 | 0.120 | 0.095 | 0.078 | 0.031 | 2164 | 0.100 | 0.037 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 18.5% | 2.14 | 2.30 | 30.6% | 0.5% | 23.7% | 31.8% | 11.6% | 0.00 | 9.1% | 55.5% | 0.06 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 18.5% | 2.14 | 2.30 | 20.4% | 0.5% | 28.8% | 30.7% | 4.9% | 0.00 | 19.8% | 52.4% | 0.01 | 0.00 |
| Totale | 400 | 18.5% | 2.14 | 2.30 | 25.3% | 0.5% | 26.2% | 31.3% | 8.3% | 0.00 | 13.8% | 54.1% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 0.254 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.13 |
| rif_LDR04_stanca_e_smonta | 200 | 0.357 | 0.152 | 5.7% | 13.4% | 1.25 | 0.29 | 0.25 | 0.39 | 0.00 | 0.00 | 2.83 |

