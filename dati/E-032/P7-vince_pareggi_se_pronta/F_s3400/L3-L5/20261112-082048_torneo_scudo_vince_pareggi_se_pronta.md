# Torneo v0.2 — /home/claude/e020_res/dati/coda/varianti/scudo_vince_pareggi_se_pronta.json

- Regole `v0.2`, configurazione `/home/claude/e020_res/dati/coda/varianti/scudo_vince_pareggi_se_pronta.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi_se_pronta', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L')}
- IA: forte:30; partite: 200; tempo 1776s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 31.6% [30.3–33.0] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–12.0] (media 11.12) | 8–11 | ✅ |
| Partite al round 13+ | 38.0% [31.6–44.9] | ≤12% | ❌ |
| Partite oltre il 15 | 0.5% [0.1–2.8] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=90) | 18.9% [12.1–28.2] | 20–35% | ❌ |
| Attacchi con opposizione | 40.0% [38.6–41.4] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 68.4% [67.0–69.8] (con ≥3: 29.4% [28.1–30.8]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 36.7% [35.3–38.1] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–1.2] (n=319) / 89.7% [85.9–92.6] (n=312) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 16.3% [14.7–18.2] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Risvegliato 99.5% [97.0–99.9] (n=187), LDR-05 Risvegliato 77.4% [67.9–84.7] (n=93) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 39.6% [32.7–46.8] (n=182) | | |
| Attacchi per partita | 23.3 | | |
| Pugno attaccante vuoto / pieno | 51.5% [50.1–53.0] / 11.6% [10.7–12.6] (gemme medie 0.93) | non >90% | |
| Pugno difensore vuoto / pieno | 53.4% [51.3–55.5] / 27.1% [25.2–29.0] (gemme medie 0.29) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 1193, 1: 1700, 2: 1207, 3: 404, 4: 128, 5: 34} | | |
| Azioni legali per decisione | 5.2 | <60 | ✅ |
| Fine partita | {'colpo_finale': 171, 'crepuscolo': 29} | | |
| G1 vince fra le partite finite al Crepuscolo | 41.4% [25.5–59.3] | | |
| G1 vince fra le partite arrivate al round 15 | 51.4% [35.6–67.0] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 34.3% [20.8–50.8] / 66.7% [39.1–86.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 8.3% [1.5–35.4]; 2.9% [0.5–14.5] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-1': 5, '1-2': 5, '1-1': 5, '2-3': 4, '0-0': 3, '0-1': 3, '3-1': 2, '2-0': 2} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=13) | 37.1% [23.2–53.7] / 61.5% [35.5–82.3] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 12, 16: 1}; 84.6% [57.8–95.7] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 61.5% [35.5–82.3] / 15.4% [4.3–42.2]; 1.38 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–22.8] / 84.6% [57.8–95.7] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=8) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–32.4] / 40.0% [11.8–76.9]; 0.0% [0.0–32.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.0% [2.0–7.7] / 22.9% [12.1–39.0]; 100.0% [67.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 5, 'perd:pronto': 3, 'vinc:atk': 8} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=10) / turno di G2 (n=11) | 0.0% [0.0–27.8] / 0.0% [0.0–25.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=10) | 0.0% [0.0–27.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 62.9% [46.3–76.8] (31.4% [18.6–48.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR03_sanguinare_per_accendere': 8, 'rif_LDR05_scudi_armati': 5} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR05_scudi_armati 51% (n=35) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 37.0% [30.6–43.9], rif_LDR05_scudi_armati 63.0% [56.1–69.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.406 / 0.099 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.096 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.11 (0.03), rif_LDR05_scudi_armati 0.17 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 31.7% [30.4–33.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.19 (112 / 126); 56.8% [55.3–58.2] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.7% [51.7–53.7]; rif_LDR03_sanguinare_per_accendere 51.2%, rif_LDR05_scudi_armati 54.3% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.2] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.314 (438) / 0.309 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 74 vittorie), LDR-05 R: 18.0 (49%, 126 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.08, NER-017 1.22, NER-001 1.19, NER-006 1.06, ROS-011 0.96, NER-013 0.89, NER-008 0.83, ROS-019 0.69, BLU-015 0.61, NER-009 0.58, ROS-020 0.58, BLU-021 0.55 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.30, rif_LDR05_scudi_armati 0.17 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 19% (n=79), rif_LDR05_scudi_armati 18% (n=11) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.6% [10.7–12.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.53, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, ROS-020 63%, NEU-013 63%, BLU-010 63%, BLU-021 63%, BLU-008 63%, collante 63%, NEU-009 63%, NER-010 37%, caccia 37%, ROS-011 37%, NER-009 37%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 37.0 [31–44] (200) |
| rif_LDR05_scudi_armati | 63.0 [56–69] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.60 | 0.00 | 0.00 / 0.00 | 1.92 | 0.00 | 3.7 (200) | 8 | K 59%, R 41% | 1.94 | 0.48 |
| rif_LDR05_scudi_armati | 3.60 | 0.00 | 3.08 / 0.00 | 0.00 | 0.67 | 4.1 (197) | 13 | B 47%, R 53% | 1.98 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.00/0.06/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.64/0.89 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/1.19/0.30/0.43 | 0.83/1.06/0.17/0.14 | 0.00/0.00/0.00/0.00 | 0.04/0.00/0.00/0.00 | 0.40/0.26/0.39/0.26 | 0.00/0.14/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.37/0.00/0.01/0.03 | 0.00/0.00/0.00/0.00 | 0.36/0.14/0.17/0.12 | 0.62/1.13/0.26/0.47 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.00/0.10/0.04 | 0.23/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.08/1.51/0.64 | 0.65/0.45/0.12/0.09 | 0.53/0.00/0.14/0.07 | 0.64/0.40/0.17/0.15 | 0.59/0.18/0.10/0.14 | 0.49/0.00/0.12/0.10 | 0.61/0.61/0.20/0.24 | 0.00/0.55/0.00/0.00 | 0.00/0.51/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.51/0.28/0.12/0.13 | 0.65/0.36/0.12/0.12 | 0.00/0.00/0.00/0.00 | 0.76/0.36/0.12/0.12 | 0.00/0.33/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.54/0.23/0.20/0.17 | 0.00/0.00/0.00/0.00 | 0.30/0.38/0.00/0.00 | 0.64/0.58/0.36/0.38 | 0.44/0.45/0.24/0.23 | 0.20/0.06/0.07/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.00/0.07/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.04/0.06/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.01/0.01 | 0.38/0.03/0.04/0.01 | 0.21/0.10/0.05/0.06 | 0.31/0.26/0.09/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.83 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.01 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.22 | 0.00 | 0.09 | 0.01 | 0.01 | 0.01 | 0.03 | 0.01 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.17 | 0.00 | 0.00 | 0.28 | 0.33 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 1.38 | 0.00 | 0.04 | 0.12 | 0.20 | 0.27 | 0.17 | 0.14 | 0.12 | 0.10 | 0.07 | 0.05 | 0.04 | 0.04 | 0.02 | 1.53 | 0.35 | 0.29 | 0.31 | 0.19 | 0.14 | 0.10 | 0.03 | 0.04 | 0.01 | 0.01 | 0.01 | 0.01 | 0.02 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.93 | 0.00 | 0.03 | 0.04 | 0.10 | 0.11 | 0.16 | 0.14 | 0.12 | 0.04 | 0.08 | 0.06 | 0.04 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 3 | 2 | 0 | 5 |
| 7 | 10 | 7 | 0 | 17 |
| 8 | 11 | 11 | 0 | 22 |
| 9 | 15 | 8 | 0 | 23 |
| 10 | 11 | 10 | 0 | 21 |
| 11 | 15 | 7 | 0 | 22 |
| 12 | 6 | 7 | 0 | 13 |
| 13 | 14 | 7 | 0 | 21 |
| 14 | 5 | 15 | 0 | 20 |
| 15 | 17 | 17 | 0 | 34 |
| 16 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 51.2% | 0.072 | 0.81 | 0.49 | 0.00 | 0.00 | 4.37 | 0.00 | 0.00 | 0.481 |
| rif_LDR05_scudi_armati | 200 | 54.3% | 0.121 | 0.17 | 0.00 | 0.00 | 0.00 | 3.02 | 0.00 | 0.00 | 0.346 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 385 | 0.917 | 0.909 | 0.886 | 0.330 | 1685 | 0.872 | 0.355 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 385 | 0.312 | 0.301 | 0.286 | 0.057 | 1685 | 0.291 | 0.116 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | mano | 613 | 0.889 | 0.863 | 0.848 | 0.457 | 1983 | 0.769 | 0.162 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 613 | 0.191 | 0.183 | 0.175 | 0.054 | 1983 | 0.173 | 0.049 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 14.5% | 2.30 | 2.35 | 27.2% | 0.5% | 15.7% | 33.0% | 13.3% | 0.00 | 14.6% | 51.2% | 0.10 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 14.5% | 2.30 | 2.35 | 45.9% | 0.5% | 16.3% | 32.1% | 12.5% | 0.00 | 19.5% | 54.3% | 0.07 | 0.00 |
| Totale | 400 | 14.5% | 2.30 | 2.35 | 34.7% | 0.5% | 16.0% | 32.5% | 12.9% | 0.00 | 17.0% | 52.7% | 0.09 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 0.398 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.66 |
| rif_LDR05_scudi_armati | 200 | 0.401 | 0.194 | 0.0% | 0.0% | 1.91 | 0.22 | 0.35 | 0.56 | 0.00 | 0.00 | 3.91 |

