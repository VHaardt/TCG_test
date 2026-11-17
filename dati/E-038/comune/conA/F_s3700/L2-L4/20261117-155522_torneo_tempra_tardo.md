# Torneo v0.2 — /root/in38/dati/E-038-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in38/dati/E-038-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2046s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 47.1% [45.7–48.4] | 30–45% | ❌ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 13.24) | 8–11 | ❌ |
| Partite al round 13+ | 69.5% [62.8–75.5] | ≤12% | ❌ |
| Partite oltre il 15 | 7.5% [4.6–12.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=58) | 29.3% [19.2–42.0] | 20–35% | ✅ |
| Attacchi con opposizione | 34.4% [33.1–35.7] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 69.6% [68.3–70.8] (con ≥3: 28.6% [27.4–29.9]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.6% [33.3–35.9] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 12.5% [10.0–15.5] (n=544) / 75.9% [69.9–81.0] (n=228) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.0% [8.6–11.5] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 62.5% [47.0–75.8] (n=40), LDR-02 Risvegliato 76.5% [66.4–84.2] (n=85), LDR-04 Base 46.4% [29.5–64.2] (n=28), LDR-04 Risvegliato 70.5% [60.2–79.0] (n=88) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 74.5% [67.2–80.7] (n=157) | | |
| Attacchi per partita | 25.1 | | |
| Pugno attaccante vuoto / pieno | 50.0% [48.5–51.5] / 12.1% [11.1–13.1] (gemme medie 0.97) | non >90% | |
| Pugno difensore vuoto / pieno | 64.3% [62.4–66.1] / 17.9% [16.5–19.4] (gemme medie 0.27) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1663, 1: 2005, 2: 816, 3: 400, 4: 116, 5: 21, 6: 5} | | |
| Azioni legali per decisione | 5.4 | <60 | ✅ |
| Fine partita | {'colpo_finale': 149, 'crepuscolo': 51} | | |
| G1 vince fra le partite finite al Crepuscolo | 66.7% [53.0–78.0] | | |
| G1 vince fra le partite arrivate al round 15 | 55.4% [44.1–66.2] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 20.3% [12.7–30.8] / 46.7% [24.8–69.9] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 40.0% [19.8–64.3]; 20.3% [12.7–30.8] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 10, '1-0': 6, '3-1': 6, '2-3': 6, '3-3': 5, '3-2': 5, '2-1': 5, '1-1': 4} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=23) | 31.1% [21.7–42.3] / 43.5% [25.6–63.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 8, 15: 15}; 52.2% [33.0–70.8] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 73.9% [53.5–87.5] / 43.5% [25.6–63.2]; 2.13 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–14.3] / 87.0% [67.9–95.5] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=10) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–27.8] / 76.9% [49.7–91.8]; 0.0% [0.0–27.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.0% [2.7–9.0] / 13.5% [7.5–23.1]; 100.0% [72.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 7, 'perd:pronto': 3, 'vinc:atk': 10} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=30) / turno di G2 (n=26) | 0.0% [0.0–11.4] / 0.0% [0.0–12.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=30) | 0.0% [0.0–11.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 54.1% [42.8–64.9] (14.9% [8.5–24.7]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 17, 'rif_LDR02_muro_di_parata': 6} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR04_stanca_e_smonta 55% (n=74) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 54.0% [47.1–60.8], rif_LDR04_stanca_e_smonta 46.0% [39.2–52.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.646 / 0.099 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.097 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.14 (0.00), rif_LDR04_stanca_e_smonta 0.14 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 27.3% [26.0–28.5] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 1.23 (78 / 168); 62.0% [60.7–63.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 58.3% [57.4–59.2]; rif_LDR02_muro_di_parata 61.4%, rif_LDR04_stanca_e_smonta 55.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.1% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.375 (54) / 0.317 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 108 vittorie), LDR-04 B: 12.0 (36%, 92 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 5.91, LDR-02 1.62, BLU-015 1.33, VER-014 0.90, VER-008 0.84, NEW-I04 0.67, BLU-001 0.56, VER-001 0.53, VER-006 0.48, VER-023 0.39, BLU-025 0.37, VER-019 0.36 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.70, rif_LDR04_stanca_e_smonta 2.33 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.37 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 48% (n=21), rif_LDR04_stanca_e_smonta 19% (n=37) | 20–35% |
| M13 | Pugno d'attacco pieno | 12.1% [11.1–13.1] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR04_stanca_e_smonta 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-009 100%, NEU-015 54%, NEU-003 54%, BLU-021 54%, RS 54%, NER-014 54%, VER-001 46%, VER-023 46%, BLU-010 46%, caccia 46%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR04_stanca_e_smonta |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 54.0 [47–61] (200) |
| rif_LDR04_stanca_e_smonta | 46.0 [39–53] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.52 | 0.00 | 1.62 / 0.00 | 0.00 | 1.39 | 4.4 (197) | 8 | B 83%, K 17% | 2.50 | 0.00 |
| rif_LDR04_stanca_e_smonta | 5.38 | 1.93 | 5.91 / 0.00 | 0.00 | 0.69 | 4.7 (197) | 10 | B 38%, G 62% | 2.22 | 0.81 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR02_muro_di_parata | 1.62 | 0.00 |
| rif_LDR04_stanca_e_smonta | 1.93 | 3.98 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.95/0.47/0.17/0.08 | 0.92/0.00/0.19/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.00/0.38/0.17 | 0.00/0.00/0.00/0.00 | 0.00/0.34/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.37/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.62/2.17/0.86 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.90/0.00/0.10/0.03 | 0.95/0.34/0.10/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.49/0.24/0.01/0.01 | 0.45/0.04/0.07/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.14/0.20/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.66/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR04_stanca_e_smonta | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.64/0.20/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.71/0.16/0.20/0.07 | 0.42/0.00/0.12/0.03 | 0.87/1.33/0.54/0.24 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.53/0.04/0.21 | 0.77/0.00/0.00/0.00 | 0.71/0.00/0.16/0.04 | 0.00/0.00/0.00/0.00 | 0.43/0.36/0.34/0.15 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/5.91/1.69/0.36 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.39/0.04/0.11 | 0.00/0.00/0.00/0.00 | 0.45/0.32/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.74/0.00/0.17/0.06 | 0.28/0.00/0.01/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.69/0.84/0.04/0.20 | 0.34/0.07/0.06/0.04 | 0.36/0.00/0.16/0.03 | 0.00/0.30/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.36/0.00/0.00/0.00 | 0.68/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.69/0.00/0.00 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.56 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 0.41 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | 0.01 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.08 | 0.00 | 0.06 | 0.07 | 0.13 | 0.14 | 0.17 | 0.14 | 0.10 | 0.08 | 0.06 | 0.07 | 0.04 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 1.11 | 0.04 | 0.04 | 0.12 | 0.08 | 0.14 | 0.14 | 0.15 | 0.15 | 0.06 | 0.07 | 0.06 | 0.04 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 8 | 0 | 1 | 0 | 1 |
| 9 | 7 | 5 | 0 | 12 |
| 10 | 10 | 5 | 0 | 15 |
| 11 | 14 | 3 | 0 | 17 |
| 12 | 12 | 4 | 0 | 16 |
| 13 | 12 | 19 | 0 | 31 |
| 14 | 8 | 26 | 0 | 34 |
| 15 | 31 | 28 | 0 | 59 |
| 16 | 10 | 5 | 0 | 15 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 61.4% | 0.107 | 1.70 | 0.00 | 0.00 | 0.00 | 2.96 | 0.00 | 0.00 | 0.547 |
| rif_LDR04_stanca_e_smonta | 200 | 55.5% | 0.089 | 1.93 | 0.40 | 0.00 | 0.00 | 1.66 | 0.00 | 0.00 | 0.494 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 657 | 0.995 | 0.939 | 0.887 | 0.201 | 2015 | 0.989 | 0.408 | 0.137 | 0.063 |
| rif_LDR02_muro_di_parata | Cicatrice | 657 | 0.306 | 0.247 | 0.181 | 0.035 | 2015 | 0.199 | 0.066 | 0.014 | 0.002 |
| rif_LDR04_stanca_e_smonta | mano | 296 | 0.841 | 0.767 | 0.696 | 0.182 | 2058 | 0.785 | 0.423 | 0.168 | 0.063 |
| rif_LDR04_stanca_e_smonta | Cicatrice | 296 | 0.159 | 0.142 | 0.108 | 0.064 | 2058 | 0.119 | 0.053 | 0.034 | 0.004 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 25.5% | 2.73 | 1.73 | 29.6% | 0.0% | 27.3% | 35.7% | 9.8% | 0.00 | 12.0% | 61.4% | 0.01 | 0.00 |
| rif_LDR04_stanca_e_smonta | 200 | 25.5% | 2.73 | 1.73 | 27.9% | 0.0% | 25.3% | 31.3% | 8.2% | 0.00 | 16.0% | 55.5% | 0.06 | 0.00 |
| Totale | 400 | 25.5% | 2.73 | 1.73 | 28.6% | 0.0% | 26.3% | 33.5% | 9.0% | 0.00 | 14.2% | 58.3% | 0.04 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.252 | 0.150 | 0.3% | 0.5% | 0.77 | 0.23 | 1.15 | 1.34 | 0.00 | 0.00 | 4.66 |
| rif_LDR04_stanca_e_smonta | 200 | 0.448 | 0.195 | 0.0% | 0.0% | 0.90 | 0.00 | 0.55 | 1.02 | 0.00 | 0.00 | 4.03 |

