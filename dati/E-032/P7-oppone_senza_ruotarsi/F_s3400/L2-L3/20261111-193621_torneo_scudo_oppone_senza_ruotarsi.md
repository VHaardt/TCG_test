# Torneo v0.2 — /home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json

- Regole `v0.2`, configurazione `/home/claude/e020_res/dati/coda/varianti/scudo_oppone_senza_ruotarsi.json`; differenze da B0: {'pugno': 'sequenziale', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L')}
- IA: forte:30; partite: 200; tempo 2435s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 45.6% [44.2–47.1] | 30–45% | ❌ |
| Durata mediana (round) | 13.0 [12.0–13.0] (media 12.21) | 8–11 | ❌ |
| Partite al round 13+ | 56.5% [49.6–63.2] | ≤12% | ❌ |
| Partite oltre il 15 | 3.5% [1.7–7.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=81) | 34.6% [25.1–45.4] | 20–35% | ✅ |
| Attacchi con opposizione | 30.4% [29.1–31.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 56.7% [55.3–58.1] (con ≥3: 19.1% [18.0–20.3]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 35.1% [33.7–36.5] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–1.2] (n=328) / 83.1% [78.7–86.8] (n=332) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 16.9% [15.1–18.8] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Risvegliato 84.5% [75.3–90.7] (n=84), LDR-03 Risvegliato 96.4% [92.7–98.2] (n=192) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 58.6% [51.6–65.4] (n=191) | | |
| Attacchi per partita | 23.3 | | |
| Pugno attaccante vuoto / pieno | 52.9% [51.4–54.4] / 9.9% [9.1–10.8] (gemme medie 1.06) | non >90% | |
| Pugno difensore vuoto / pieno | 43.8% [41.9–45.7] / 25.5% [23.9–27.2] (gemme medie 0.42) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 5; {0: 1344, 1: 1755, 2: 979, 3: 431, 4: 130, 5: 23} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'colpo_finale': 157, 'crepuscolo': 43} | | |
| G1 vince fra le partite finite al Crepuscolo | 67.4% [52.5–79.5] | | |
| G1 vince fra le partite arrivate al round 15 | 65.5% [52.3–76.6] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 27.3% [17.3–40.2] / 33.3% [15.2–58.3] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [15.2–58.3]; 12.7% [6.3–24.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-0': 9, '2-1': 8, '3-2': 7, '2-2': 5, '0-1': 5, '1-0': 5, '1-2': 4, '1-1': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=20) | 36.4% [24.9–49.6] / 25.0% [11.2–46.9] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15, 16: 5}; 50.0% [29.9–70.1] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 90.0% [69.9–97.2] / 25.0% [11.2–46.9]; 3.20 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–16.1] / 100.0% [83.9–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=5) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–43.4] / 33.3% [15.2–58.3]; 0.0% [0.0–43.4] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.5% [1.1–5.7] / 9.1% [3.9–19.6]; 100.0% [56.6–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 5, 'vinc:atk': 5} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=27) / turno di G2 (n=18) | 0.0% [0.0–12.5] / 0.0% [0.0–17.6] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=27) | 0.0% [0.0–12.5] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 67.3% [54.1–78.2] (23.6% [14.4–36.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 13, 'rif_LDR03_sanguinare_per_accendere': 7} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR03_sanguinare_per_accendere 65% (n=55) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 43.0% [36.3–49.9], rif_LDR03_sanguinare_per_accendere 57.0% [50.1–63.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.543 / 0.086 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.082 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.14 (0.00), rif_LDR03_sanguinare_per_accendere 0.07 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 21.9% [20.7–23.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.85 (58 / 113); 66.6% [65.2–67.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.8% [50.8–52.9]; rif_LDR02_muro_di_parata 48.6%, rif_LDR03_sanguinare_per_accendere 53.6% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 8.8% [7.4–10.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.000 (0) / 0.319 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 9.0 (26%, 86 vittorie), LDR-03 R: 14.0 (35%, 114 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-02 2.02, NER-017 1.32, NER-006 1.07, ROS-019 1.00, NER-001 1.00, NER-008 0.82, BLU-001 0.77, ROS-011 0.76, NER-010 0.58, BLU-025 0.57, NER-013 0.54, NER-009 0.32 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.51, rif_LDR03_sanguinare_per_accendere 1.25 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR03_sanguinare_per_accendere 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 6% (n=18), rif_LDR03_sanguinare_per_accendere 43% (n=63) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.9% [9.1–10.8] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR03_sanguinare_per_accendere 1.57; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, caccia 57%, ROS-011 57%, NER-010 57%, NER-009 57%, NER-017 57%, NER-014 43%, NEU-003 43%, collante 43%, RS 43%, BLU-021 43%, 11.1 43%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR03_sanguinare_per_accendere |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 43.0 [36–50] (200) |
| rif_LDR03_sanguinare_per_accendere | 57.0 [50–64] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.16 | 0.00 | 2.02 / 0.00 | 0.00 | 1.11 | 5.2 (194) | 8 | B 81%, K 19% | 3.15 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 3.78 | 0.00 | 0.00 / 0.00 | 2.94 | 0.00 | 4.4 (199) | 10 | K 61%, R 39% | 2.30 | 0.79 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.82/0.77/0.12/0.12 | 0.81/0.00/0.15/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.72/0.00/0.15/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.19/0.00/0.00 | 0.00/0.20/0.00/0.00 | 0.00/0.57/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.02/1.52/0.89 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.44/0.04/0.10/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.25/0.11/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.00/0.08/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.78/0.33 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/1.00/0.39/0.12 | 0.88/1.07/0.23/0.07 | 0.00/0.00/0.00/0.00 | 0.01/0.00/0.00/0.00 | 0.46/0.12/0.37/0.12 | 0.00/0.20/0.00/0.00 | 0.00/0.10/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.00/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.34/0.11/0.17/0.04 | 0.68/1.00/0.32/0.17 | 0.00/0.16/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.48/0.00/0.14/0.04 | 0.29/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.47 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.93 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.01 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.16 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.35 | 0.00 | 0.02 | 0.07 | 0.09 | 0.12 | 0.12 | 0.18 | 0.19 | 0.14 | 0.18 | 0.07 | 0.10 | 0.06 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 200 | 1.45 | 0.00 | 0.03 | 0.05 | 0.11 | 0.21 | 0.20 | 0.18 | 0.15 | 0.09 | 0.15 | 0.15 | 0.06 | 0.04 | 0.04 | 1.57 | 0.20 | 0.18 | 0.29 | 0.32 | 0.14 | 0.18 | 0.09 | 0.07 | 0.01 | 0.03 | 0.02 | 0.00 | 0.01 | 0.01 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 4 | 0 | 5 |
| 7 | 1 | 8 | 0 | 9 |
| 8 | 4 | 6 | 0 | 10 |
| 9 | 6 | 9 | 0 | 15 |
| 10 | 12 | 9 | 0 | 21 |
| 11 | 5 | 7 | 0 | 12 |
| 12 | 8 | 7 | 0 | 15 |
| 13 | 16 | 16 | 0 | 32 |
| 14 | 13 | 13 | 0 | 26 |
| 15 | 29 | 19 | 0 | 48 |
| 16 | 7 | 0 | 0 | 7 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 48.6% | 0.078 | 1.51 | 0.00 | 0.00 | 0.00 | 2.44 | 0.00 | 0.00 | 0.540 |
| rif_LDR03_sanguinare_per_accendere | 200 | 53.6% | 0.099 | 0.69 | 0.57 | 0.00 | 0.00 | 2.06 | 0.00 | 0.00 | 0.548 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 938 | 1.000 | 0.996 | 0.995 | 0.205 | 1870 | 0.999 | 0.311 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 938 | 0.463 | 0.425 | 0.383 | 0.030 | 1870 | 0.373 | 0.124 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | mano | 529 | 0.957 | 0.945 | 0.928 | 0.318 | 1325 | 0.881 | 0.365 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 529 | 0.270 | 0.259 | 0.236 | 0.028 | 1325 | 0.245 | 0.106 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 21.5% | 2.23 | 2.28 | 25.6% | 0.0% | 35.2% | 44.2% | 13.8% | 0.00 | 17.2% | 48.6% | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 200 | 21.5% | 2.23 | 2.28 | 43.5% | 0.0% | 25.2% | 36.2% | 11.7% | 0.00 | 12.5% | 53.6% | 0.09 | 0.00 |
| Totale | 400 | 21.5% | 2.23 | 2.28 | 33.9% | 0.0% | 30.2% | 40.2% | 12.8% | 0.00 | 14.1% | 51.8% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.246 | 0.188 | 18.1% | 23.6% | 1.25 | 0.34 | 0.56 | 0.69 | 0.00 | 0.00 | 3.00 |
| rif_LDR03_sanguinare_per_accendere | 200 | 0.393 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.18 |

