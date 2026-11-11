# Torneo v0.2 — /home/claude/e033_in/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/home/claude/e033_in/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 100; tempo 1155s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 37.7% [35.8–39.6] | 30–45% | ✅ |
| Durata mediana (round) | 12.0 [11.0–12.0] (media 11.93) | 8–11 | ❌ |
| Partite al round 13+ | 38.0% [29.1–47.8] | ≤12% | ❌ |
| Partite oltre il 15 | 2.0% [0.6–7.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–3.7] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=32) | 34.4% [20.4–51.7] | 20–35% | ✅ |
| Attacchi con opposizione | 30.1% [28.4–32.0] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 59.4% [57.4–61.4] (con ≥3: 22.9% [21.2–24.7]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 39.4% [37.5–41.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 12.8% [9.0–17.9] (n=219) / 88.7% [82.4–92.9] (n=141) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 12.8% [10.8–15.0] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Base 23.8% [10.6–45.1] (n=21), LDR-01 Risvegliato 58.6% [45.8–70.4] (n=58), LDR-02 Base 57.1% [25.0–84.2] (n=7), LDR-02 Risvegliato 91.0% [81.8–95.8] (n=67) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 40.5% [30.6–51.2] (n=84) | | |
| Attacchi per partita | 24.8 | | |
| Pugno attaccante vuoto / pieno | 51.1% [49.0–53.1] / 10.8% [9.6–12.1] (gemme medie 0.95) | non >90% | |
| Pugno difensore vuoto / pieno | 54.5% [51.7–57.2] / 23.1% [20.9–25.5] (gemme medie 0.31) | non >90% | |
| Reazioni per scontro | 0.07 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 901, 1: 814, 2: 529, 3: 152, 4: 66, 5: 16, 6: 4} | | |
| Azioni legali per decisione | 5.3 | <60 | ✅ |
| Fine partita | {'colpo_finale': 90, 'crepuscolo': 10} | | |
| G1 vince fra le partite finite al Crepuscolo | 60.0% [31.3–83.2] | | |
| G1 vince fra le partite arrivate al round 15 | 52.9% [31.0–73.8] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 11.8% [3.3–34.3] / 0.0% [0.0–65.8] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 100.0% [34.2–100.0]; 11.8% [3.3–34.3] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-3': 3, '2-2': 3, '1-0': 2, '1-2': 1, '4-2': 1, '0-2': 1, '2-4': 1, '1-3': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=2) | 11.8% [3.3–34.3] / 0.0% [0.0–65.8] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 2}; 0.0% [0.0–65.8] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 100.0% [34.2–100.0] / 100.0% [34.2–100.0]; 3.50 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–65.8] / 100.0% [34.2–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=0) / a Vite diverse; nessuno attacca a Vite pari | nan% [nan–nan] / 100.0% [34.2–100.0]; nan% [nan–nan] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 0.0% [0.0–3.7] / 0.0% [0.0–18.4]; nan% [nan–nan] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=7) / turno di G2 (n=5) | 0.0% [0.0–35.4] / 0.0% [0.0–43.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=7) | 0.0% [0.0–35.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 35.3% [17.3–58.7] (0.0% [0.0–18.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR01_puntata_e_preda': 2} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR02_muro_di_parata 53% (n=17) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 63.0% [53.2–71.8], rif_LDR02_muro_di_parata 37.0% [28.2–46.8]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.471 / 0.066 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.063 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.05 (0.00), rif_LDR02_muro_di_parata 0.12 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 25.8% [24.1–27.6] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.48 (39 / 109); 64.9% [63.0–66.7] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 51.6% [50.2–53.1]; rif_LDR01_puntata_e_preda 53.7%, rif_LDR02_muro_di_parata 48.2% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.341 (248) / 0.332 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 16.0 (42%, 63 vittorie), LDR-02 K: 9.0 (26%, 37 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-01 1.96, LDR-02 1.36, ROS-016 1.32, ROS-018 1.08, VER-011 0.60, VER-001 0.55, BLU-001 0.54, ROS-001 0.54, ROS-021 0.53, VER-008 0.50, VER-019 0.40, BLU-025 0.35 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.84, rif_LDR02_muro_di_parata 1.42 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.06, rif_LDR02_muro_di_parata 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 40% (n=15), rif_LDR02_muro_di_parata 29% (n=17) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.8% [9.6–12.1] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR02_muro_di_parata 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, VER-008 63%, ROS-016 63%, VER-001 63%, VER-011 63%, caccia 63%, NEU-009 37%, collante 37%, 11.1 37%, NER-014 37%, RS 37%, BLU-022 37%; oltre il 60%: ROS-016, VER-001, VER-008 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR02_muro_di_parata |
|---|---|---|
| rif_LDR01_puntata_e_preda | — | 63.0 [53–72] (100) |
| rif_LDR02_muro_di_parata | 37.0 [28–47] (100) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 4.02 | 0.00 | 1.96 / 0.00 | 0.00 | 0.00 | 4.6 (100) | 13 | G 42%, R 58% | 2.24 | 0.79 |
| rif_LDR02_muro_di_parata | 4.38 | 0.00 | 1.36 / 0.00 | 0.00 | 1.23 | 4.8 (98) | 8 | B 77%, K 23% | 2.87 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 0.00/1.96/1.62/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.31/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.54/0.28/0.02 | 0.73/0.29/0.67/0.14 | 0.67/0.29/0.12/0.01 | 0.00/0.27/0.00/0.00 | 0.70/0.00/0.20/0.06 | 0.69/0.19/0.32/0.02 | 0.78/1.32/0.06/0.44 | 0.65/1.08/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.53/0.42/0.15 | 0.28/0.14/0.25/0.06 | 0.00/0.00/0.00/0.00 | 0.74/0.55/0.07/0.37 | 0.64/0.00/0.00/0.00 | 0.91/0.00/0.18/0.02 | 0.68/0.60/0.26/0.09 | 0.74/0.40/0.50/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.50/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.00/0.12/0.01 | 0.40/0.01/0.01/0.00 | 0.33/0.09/0.18/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.00/0.06/0.01 | 0.36/0.50/0.01/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.14/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.84/0.54/0.23/0.21 | 0.76/0.00/0.29/0.20 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.00/0.39/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.25/0.00/0.00 | 0.00/0.20/0.00/0.00 | 0.00/0.35/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.36/1.98/1.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.04/0.16/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.42/0.06/0.12/0.27 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 1.43 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.24 | 0.00 | 0.00 | 0.01 | 0.12 | 0.10 | 0.00 | 0.00 | 0.38 | 0.13 | 0.00 | 0.08 | 0.00 | 0.00 | 0.07 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 0.37 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 0.85 | 0.00 | 0.07 | 0.08 | 0.12 | 0.16 | 0.13 | 0.09 | 0.13 | 0.04 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 100 | 1.22 | 0.03 | 0.07 | 0.12 | 0.15 | 0.17 | 0.15 | 0.15 | 0.18 | 0.10 | 0.05 | 0.02 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 1 | 0 | 1 |
| 8 | 4 | 1 | 0 | 5 |
| 9 | 5 | 6 | 0 | 11 |
| 10 | 3 | 4 | 0 | 7 |
| 11 | 11 | 8 | 0 | 19 |
| 12 | 13 | 6 | 0 | 19 |
| 13 | 6 | 5 | 0 | 11 |
| 14 | 2 | 8 | 0 | 10 |
| 15 | 7 | 8 | 0 | 15 |
| 16 | 2 | 0 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 53.7% | 0.064 | 0.00 | 0.84 | 0.00 | 0.00 | 2.06 | 0.00 | 0.00 | 0.351 |
| rif_LDR02_muro_di_parata | 100 | 48.2% | 0.068 | 1.42 | 0.00 | 0.00 | 0.00 | 3.63 | 0.00 | 0.00 | 0.570 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | mano | 232 | 0.836 | 0.806 | 0.784 | 0.289 | 894 | 0.779 | 0.204 | 0.000 | 0.000 |
| rif_LDR01_puntata_e_preda | Cicatrice | 232 | 0.220 | 0.190 | 0.155 | 0.022 | 894 | 0.189 | 0.056 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | mano | 346 | 1.000 | 0.988 | 0.988 | 0.231 | 1010 | 1.000 | 0.427 | 0.000 | 0.000 |
| rif_LDR02_muro_di_parata | Cicatrice | 346 | 0.405 | 0.379 | 0.332 | 0.035 | 1010 | 0.322 | 0.115 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 10.0% | 2.53 | 1.56 | 40.7% | 0.0% | 20.3% | 29.7% | 9.9% | 0.00 | 15.2% | 53.7% | 0.16 | 0.00 |
| rif_LDR02_muro_di_parata | 100 | 10.0% | 2.53 | 1.56 | 20.0% | 0.0% | 35.3% | 43.3% | 17.8% | 0.00 | 15.0% | 48.2% | 0.00 | 0.00 |
| Totale | 200 | 10.0% | 2.53 | 1.56 | 29.4% | 0.0% | 27.8% | 36.4% | 14.7% | 0.00 | 15.1% | 51.6% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

