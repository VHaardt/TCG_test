# Torneo v0.2 — /root/in/dati/E-036-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in/dati/E-036-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1295s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 34.7% [33.3–36.2] | 30–45% | ✅ |
| Durata mediana (round) | 11.0 [10.0–11.5] (media 11.13) | 8–11 | ✅ |
| Partite al round 13+ | 35.0% [28.7–41.8] | ≤12% | ❌ |
| Partite oltre il 15 | 1.0% [0.3–3.6] | <2% | ✅ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=77) | 39.0% [28.8–50.1] | 20–35% | ❌ |
| Attacchi con opposizione | 29.4% [28.1–30.8] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 60.3% [58.9–61.8] (con ≥3: 23.2% [22.0–24.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 37.9% [36.5–39.4] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 4.4% [2.6–7.4] (n=295) / 84.3% [80.0–87.8] (n=331) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 17.0% [15.3–18.9] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-03 Base 28.6% [8.2–64.1] (n=7), LDR-03 Risvegliato 98.7% [95.4–99.6] (n=156), LDR-06 Base 50.0% [18.8–81.2] (n=6), LDR-06 Risvegliato 65.9% [57.1–73.6] (n=123) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 35.3% [28.8–42.4] (n=187) | | |
| Attacchi per partita | 21.6 | | |
| Pugno attaccante vuoto / pieno | 56.3% [54.7–57.8] / 11.6% [10.6–12.6] (gemme medie 0.86) | non >90% | |
| Pugno difensore vuoto / pieno | 54.4% [52.3–56.5] / 24.3% [22.5–26.1] (gemme medie 0.29) | non >90% | |
| Reazioni per scontro | 0.09 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1258, 1: 1736, 2: 929, 3: 284, 4: 91, 5: 24, 6: 2} | | |
| Azioni legali per decisione | 5.8 | <60 | ✅ |
| Fine partita | {'colpo_finale': 182, 'crepuscolo': 18} | | |
| G1 vince fra le partite finite al Crepuscolo | 72.2% [49.1–87.5] | | |
| G1 vince fra le partite arrivate al round 15 | 69.2% [50.0–83.5] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 34.6% [19.4–53.8] / 33.3% [12.1–64.6] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 55.6% [26.7–81.1]; 7.7% [2.1–24.1] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 5, '1-0': 5, '2-1': 4, '2-3': 3, '0-0': 3, '5-2': 2, '4-1': 1, '1-2': 1} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=9) | 34.6% [19.4–53.8] / 33.3% [12.1–64.6] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 9}; 44.4% [18.9–73.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 66.7% [35.4–87.9] / 44.4% [18.9–73.3]; 2.33 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–29.9] / 88.9% [56.5–98.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=3) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–56.2] / 66.7% [30.0–90.3]; 0.0% [0.0–56.2] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 1.5% [0.5–4.3] / 11.5% [4.0–29.0]; 100.0% [43.8–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:abil': 1, 'perd:atk': 1, 'perd:pronto': 1, 'vinc:atk': 3} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=12) / turno di G2 (n=13) | 0.0% [0.0–24.3] / 0.0% [0.0–22.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=12) | 0.0% [0.0–24.3] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 53.8% [35.5–71.2] (3.8% [0.7–18.9]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 6, 'rif_LDR03_sanguinare_per_accendere': 3} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR03_sanguinare_per_accendere vs rif_LDR06_ferite_e_caccia 69% (n=26) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR03_sanguinare_per_accendere 54.0% [47.1–60.8], rif_LDR06_ferite_e_caccia 46.0% [39.2–52.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.415 / 0.092 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.092 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR03_sanguinare_per_accendere 0.19 (0.06), rif_LDR06_ferite_e_caccia 0.14 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 33.3% [31.9–34.7] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 3.04 (226 / 381); 60.5% [59.1–62.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 52.7% [51.7–53.8]; rif_LDR03_sanguinare_per_accendere 54.6%, rif_LDR06_ferite_e_caccia 50.6% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.374 (58) / 0.326 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-03 R: 14.0 (35%, 108 vittorie), LDR-06 G: 19.0 (54%, 92 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 2.12, VER-020 0.94, ROS-019 0.89, NER-008 0.82, NER-017 0.76, ROS-011 0.75, NER-001 0.65, NER-006 0.64, NER-010 0.64, NEU-001 0.57, NER-013 0.56, VER-019 0.49 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR03_sanguinare_per_accendere 1.33, rif_LDR06_ferite_e_caccia 1.94 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR06_ferite_e_caccia 0.12 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR03_sanguinare_per_accendere 42% (n=53), rif_LDR06_ferite_e_caccia 33% (n=24) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.6% [10.6–12.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR03_sanguinare_per_accendere 1.62, rif_LDR06_ferite_e_caccia 0.79; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, NER-017 100%, caccia 100%, NER-009 100%, NER-010 54%, ROS-011 54%, collante 46%, NER-015 46%, NEW-B06 46%, NEU-012 46%, VER-001 46%, VER-020 46%; oltre il 60%: NER-009, NER-017 | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR03_sanguinare_per_accendere | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | — | 54.0 [47–61] (200) |
| rif_LDR06_ferite_e_caccia | 46.0 [39–53] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 3.29 | 0.00 | 0.00 / 0.00 | 2.46 | 0.00 | 4.9 (199) | 10 | K 62%, R 38% | 2.09 | 0.46 |
| rif_LDR06_ferite_e_caccia | 3.47 | 0.00 | 2.12 / 0.14 | 0.00 | 0.18 | 4.6 (193) | 9 | G 51%, K 49% | 2.26 | 1.14 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.80 | 1.33 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.35/0.00/0.06/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.56/0.52 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.94/0.38/0.18 | 0.85/0.98/0.15/0.07 | 0.00/0.00/0.00/0.00 | 0.04/0.00/0.00/0.00 | 0.35/0.10/0.30/0.10 | 0.00/0.28/0.00/0.00 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.00/0.03/0.00 | 0.00/0.00/0.00/0.00 | 0.39/0.08/0.15/0.06 | 0.67/0.89/0.41/0.23 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.09/0.04 | 0.83/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.38/0.06/0.30 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.49/0.42/0.28 | 0.00/0.27/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.12/1.57/0.63 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.27/0.35/0.11/0.05 | 0.33/0.28/0.05/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.12/0.18/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.38/0.29/0.01/0.02 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.52/0.30/0.03/0.23 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.34/0.05/0.03/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.57/0.12/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.62/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.17/0.25/0.04/0.13 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.41/0.00/0.08/0.04 | 0.20/0.36/0.07/0.06 | 0.00/0.00/0.00/0.00 | 0.54/0.29/0.06/0.21 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.69 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.01 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.61 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.02 | 0.01 | 0.00 | 0.03 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 1.08 | 0.00 | 0.03 | 0.10 | 0.12 | 0.14 | 0.16 | 0.13 | 0.14 | 0.10 | 0.04 | 0.04 | 0.03 | 0.03 | 0.02 | 1.62 | 0.23 | 0.26 | 0.36 | 0.24 | 0.15 | 0.18 | 0.07 | 0.07 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.58 | 0.00 | 0.01 | 0.06 | 0.07 | 0.07 | 0.06 | 0.10 | 0.10 | 0.03 | 0.04 | 0.02 | 0.02 | 0.01 | 0.00 | 0.79 | 0.10 | 0.17 | 0.10 | 0.08 | 0.10 | 0.09 | 0.07 | 0.04 | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca | NER-002 stanca | NER-002 vita |
|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.62 | 0.21 |
| rif_LDR06_ferite_e_caccia | 0.45 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 2 | 0 | 0 | 2 |
| 7 | 7 | 4 | 0 | 11 |
| 8 | 15 | 5 | 0 | 20 |
| 9 | 19 | 11 | 0 | 30 |
| 10 | 20 | 11 | 0 | 31 |
| 11 | 14 | 5 | 0 | 19 |
| 12 | 11 | 6 | 0 | 17 |
| 13 | 16 | 7 | 0 | 23 |
| 14 | 4 | 17 | 0 | 21 |
| 15 | 16 | 8 | 0 | 24 |
| 16 | 2 | 0 | 0 | 2 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 54.6% | 0.100 | 0.82 | 0.52 | 0.00 | 0.00 | 2.68 | 0.00 | 0.00 | 0.480 |
| rif_LDR06_ferite_e_caccia | 200 | 50.6% | 0.084 | 0.79 | 1.15 | 0.00 | 0.00 | 3.23 | 0.00 | 0.00 | 0.356 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | mano | 526 | 0.905 | 0.895 | 0.880 | 0.319 | 1540 | 0.852 | 0.310 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 526 | 0.272 | 0.260 | 0.257 | 0.072 | 1540 | 0.219 | 0.088 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | mano | 468 | 0.855 | 0.799 | 0.739 | 0.346 | 1790 | 0.736 | 0.206 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 468 | 0.226 | 0.197 | 0.165 | 0.060 | 1790 | 0.178 | 0.050 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 9.0% | 2.25 | 1.87 | 38.8% | 0.0% | 23.2% | 30.8% | 9.2% | 0.00 | 12.4% | 54.6% | 0.05 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 9.0% | 2.25 | 1.87 | 36.1% | 0.0% | 25.0% | 36.5% | 11.6% | 0.00 | 13.9% | 50.6% | 0.03 | 0.00 |
| Totale | 400 | 9.0% | 2.25 | 1.87 | 37.3% | 0.0% | 24.1% | 33.6% | 10.5% | 0.00 | 13.1% | 52.7% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR03_sanguinare_per_accendere | 200 | 0.305 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.82 |
| rif_LDR06_ferite_e_caccia | 200 | 0.284 | 0.052 | 0.0% | 0.0% | 0.47 | 0.06 | 0.07 | 0.04 | 0.00 | 0.00 | 3.38 |

