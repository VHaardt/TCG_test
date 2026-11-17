# Torneo v0.2 — /root/in/dati/E-036-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in/dati/E-036-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1723s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 43.1% [41.7–44.5] | 30–45% | ✅ |
| Durata mediana (round) | 13.0 [12.0–13.0] (media 12.31) | 8–11 | ❌ |
| Partite al round 13+ | 53.0% [46.1–59.8] | ≤12% | ❌ |
| Partite oltre il 15 | 4.5% [2.4–8.3] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=80) | 21.2% [13.7–31.4] | 20–35% | ✅ |
| Attacchi con opposizione | 29.9% [28.6–31.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 61.8% [60.4–63.1] (con ≥3: 21.8% [20.7–23.0]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 35.7% [34.3–37.1] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 12.1% [9.4–15.6] (n=428) / 85.7% [81.2–89.3] (n=287) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.9% [13.2–16.7] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 41.9% [28.4–56.7] (n=43), LDR-02 Risvegliato 82.5% [74.1–88.7] (n=103), LDR-06 Base 55.6% [26.7–81.1] (n=9), LDR-06 Risvegliato 69.2% [61.2–76.2] (n=143) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 56.8% [48.9–64.3] (n=155) | | |
| Attacchi per partita | 23.2 | | |
| Pugno attaccante vuoto / pieno | 55.9% [54.4–57.4] / 11.8% [10.9–12.9] (gemme medie 0.84) | non >90% | |
| Pugno difensore vuoto / pieno | 52.4% [50.3–54.4] / 23.6% [21.9–25.4] (gemme medie 0.31) | non >90% | |
| Reazioni per scontro | 0.10 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1624, 1: 1794, 2: 827, 3: 265, 4: 90, 5: 28, 6: 8} | | |
| Azioni legali per decisione | 5.6 | <60 | ✅ |
| Fine partita | {'colpo_finale': 162, 'crepuscolo': 38} | | |
| G1 vince fra le partite finite al Crepuscolo | 50.0% [34.8–65.2] | | |
| G1 vince fra le partite arrivate al round 15 | 44.6% [32.4–57.6] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 26.8% [17.0–39.6] / 46.7% [24.8–69.9] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 26.7% [10.9–52.0]; 16.1% [8.7–27.8] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 8, '2-3': 7, '3-2': 5, '4-2': 5, '1-0': 4, '0-0': 4, '0-1': 4, '2-1': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=22) | 39.3% [27.6–52.4] / 45.5% [26.9–65.3] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 15, 16: 7}; 63.6% [43.0–80.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 59.1% [38.7–76.7] / 36.4% [19.7–57.0]; 2.09 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–14.9] / 81.8% [61.5–92.7] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=10) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–27.8] / 66.7% [39.1–86.2]; 0.0% [0.0–27.8] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 5.0% [2.7–9.0] / 17.9% [10.0–29.8]; 100.0% [72.2–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 5, 'perd:rim': 1, 'vinc:atk': 10} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=17) / turno di G2 (n=15) | 0.0% [0.0–18.4] / 0.0% [0.0–20.4] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=17) | 0.0% [0.0–18.4] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 42.9% [30.8–55.9] (12.5% [6.2–23.6]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR06_ferite_e_caccia': 14, 'rif_LDR02_muro_di_parata': 8} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR06_ferite_e_caccia 45% (n=56) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 69.0% [62.3–75.0], rif_LDR06_ferite_e_caccia 31.0% [25.0–37.7]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.518 / 0.105 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.101 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.14 (0.00), rif_LDR06_ferite_e_caccia 0.12 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 28.8% [27.5–30.1] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.54 (157 / 352); 61.5% [60.1–62.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 53.3% [52.3–54.3]; rif_LDR02_muro_di_parata 58.3%, rif_LDR06_ferite_e_caccia 49.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.1% [0.0–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.381 (64) / 0.337 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 138 vittorie), LDR-06 G: 19.0 (54%, 62 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-06 2.48, LDR-02 1.75, VER-020 1.64, NER-017 0.84, NEW-P31 0.81, NEU-001 0.68, NEW-I04 0.67, NER-013 0.52, BLU-005 0.52, NER-003 0.52, VER-019 0.46, NER-006 0.42 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.72, rif_LDR06_ferite_e_caccia 2.67 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 0.11 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 38% (n=16), rif_LDR06_ferite_e_caccia 17% (n=64) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.8% [10.9–12.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR06_ferite_e_caccia 0.94; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-009 69%, NEU-015 69%, RS 69%, BLU-021 69%, NEU-003 69%, NER-014 69%, VER-001 31%, NER-009 31%, NER-015 31%, NEW-B06 31%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR06_ferite_e_caccia |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 69.0 [62–75] (200) |
| rif_LDR06_ferite_e_caccia | 31.0 [25–38] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.08 | 0.00 | 1.75 / 0.00 | 0.00 | 1.03 | 5.2 (199) | 8 | B 84%, K 16% | 2.74 | 0.00 |
| rif_LDR06_ferite_e_caccia | 3.84 | 0.00 | 2.48 / 0.10 | 0.00 | 0.18 | 4.7 (195) | 10 | G 51%, K 49% | 2.19 | 1.90 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR02_muro_di_parata | 1.75 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.69 | 1.79 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.86/0.41/0.21/0.07 | 0.84/0.00/0.17/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.95/0.00/0.37/0.19 | 0.00/0.00/0.00/0.00 | 0.00/0.38/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.36/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.75/1.92/0.62 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.87/0.00/0.06/0.02 | 0.97/0.52/0.14/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.04/0.00/0.00 | 0.45/0.00/0.00/0.00 | 0.45/0.22/0.04/0.01 | 0.40/0.07/0.09/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.55/0.15/0.25/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.67/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR06_ferite_e_caccia | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.34/0.09/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.64/0.46/0.36/0.20 | 0.00/0.20/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/2.48/1.66/0.41 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.29/0.07/0.04 | 0.41/0.42/0.11/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.31/0.09/0.20/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.18/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.40/0.30/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.63/0.30/0.04/0.14 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.32/0.04/0.04/0.01 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.85/0.68/0.19/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.59/0.00/0.00/0.00 | 0.45/0.00/0.00/0.00 | 0.28/0.32/0.08/0.10 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.00/0.12/0.03 | 0.24/0.29/0.05/0.03 | 0.00/0.00/0.00/0.00 | 0.68/0.81/0.07/0.36 | 0.61/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.36 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.54 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.04 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.83 | 0.00 | 0.05 | 0.03 | 0.06 | 0.09 | 0.10 | 0.14 | 0.13 | 0.06 | 0.05 | 0.05 | 0.04 | 0.04 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 0.98 | 0.00 | 0.01 | 0.05 | 0.06 | 0.10 | 0.17 | 0.10 | 0.14 | 0.12 | 0.06 | 0.07 | 0.04 | 0.04 | 0.03 | 0.94 | 0.09 | 0.20 | 0.09 | 0.15 | 0.13 | 0.10 | 0.08 | 0.06 | 0.02 | 0.01 | 0.01 | 0.01 | 0.00 | 0.01 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | LDR-06 stanca | NEW-P32 stanca |
|---|---|---|
| rif_LDR02_muro_di_parata | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 0.28 | 0.61 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 0 | 1 | 0 | 1 |
| 7 | 0 | 4 | 0 | 4 |
| 8 | 2 | 8 | 0 | 10 |
| 9 | 10 | 2 | 0 | 12 |
| 10 | 14 | 12 | 0 | 26 |
| 11 | 17 | 11 | 0 | 28 |
| 12 | 5 | 8 | 0 | 13 |
| 13 | 24 | 9 | 0 | 33 |
| 14 | 5 | 12 | 0 | 17 |
| 15 | 19 | 28 | 0 | 47 |
| 16 | 6 | 3 | 0 | 9 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 58.3% | 0.122 | 1.72 | 0.00 | 0.00 | 0.00 | 2.20 | 0.00 | 0.00 | 0.541 |
| rif_LDR06_ferite_e_caccia | 200 | 49.1% | 0.084 | 1.42 | 1.25 | 0.00 | 0.00 | 2.72 | 0.00 | 0.00 | 0.367 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 650 | 0.991 | 0.932 | 0.882 | 0.232 | 1849 | 0.985 | 0.394 | 0.160 | 0.069 |
| rif_LDR02_muro_di_parata | Cicatrice | 650 | 0.283 | 0.208 | 0.138 | 0.031 | 1849 | 0.241 | 0.054 | 0.015 | 0.004 |
| rif_LDR06_ferite_e_caccia | mano | 455 | 0.888 | 0.818 | 0.725 | 0.341 | 1682 | 0.762 | 0.206 | 0.000 | 0.000 |
| rif_LDR06_ferite_e_caccia | Cicatrice | 455 | 0.202 | 0.174 | 0.149 | 0.055 | 1682 | 0.181 | 0.059 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 19.0% | 2.47 | 1.87 | 41.6% | 0.0% | 30.3% | 32.7% | 7.8% | 0.00 | 14.3% | 58.3% | 0.02 | 0.00 |
| rif_LDR06_ferite_e_caccia | 200 | 19.0% | 2.47 | 1.87 | 20.4% | 0.0% | 28.5% | 31.3% | 7.5% | 0.00 | 13.2% | 49.1% | 0.09 | 0.00 |
| Totale | 400 | 19.0% | 2.47 | 1.87 | 27.7% | 0.0% | 29.4% | 32.0% | 7.7% | 0.00 | 13.7% | 53.3% | 0.06 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.259 | 0.154 | 0.3% | 0.5% | 0.84 | 0.79 | 0.77 | 1.05 | 0.00 | 0.00 | 4.42 |
| rif_LDR06_ferite_e_caccia | 200 | 0.347 | 0.053 | 0.0% | 0.0% | 0.40 | 0.00 | 0.07 | 0.08 | 0.00 | 0.00 | 3.85 |

