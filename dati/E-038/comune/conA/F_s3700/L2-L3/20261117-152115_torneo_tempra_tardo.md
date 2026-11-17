# Torneo v0.2 — /root/in38/dati/E-038-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in38/dati/E-038-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 1798s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 44.4% [42.9–45.8] | 30–45% | ✅ |
| Durata mediana (round) | 13.0 [12.5–14.0] (media 12.27) | 8–11 | ❌ |
| Partite al round 13+ | 56.0% [49.1–62.7] | ≤12% | ❌ |
| Partite oltre il 15 | 4.0% [2.0–7.7] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=78) | 25.6% [17.3–36.3] | 20–35% | ✅ |
| Attacchi con opposizione | 38.3% [36.9–39.7] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 68.1% [66.8–69.4] (con ≥3: 30.1% [28.8–31.5]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 34.7% [33.3–36.1] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 8.1% [5.7–11.2] (n=384) / 86.4% [81.7–90.1] (n=258) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 14.4% [12.8–16.3] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 53.8% [35.5–71.2] (n=26), LDR-02 Risvegliato 70.1% [59.2–79.2] (n=77), LDR-03 Base 80.0% [37.6–96.4] (n=5), LDR-03 Risvegliato 100.0% [97.4–100.0] (n=146) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 57.7% [50.2–65.0] (n=168) | | |
| Attacchi per partita | 22.3 | | |
| Pugno attaccante vuoto / pieno | 55.5% [53.9–57.0] / 10.7% [9.8–11.7] (gemme medie 0.91) | non >90% | |
| Pugno difensore vuoto / pieno | 47.2% [45.1–49.2] / 25.8% [24.1–27.7] (gemme medie 0.35) | non >90% | |
| Reazioni per scontro | 0.11 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1295, 1: 1833, 2: 813, 3: 370, 4: 105, 5: 32, 6: 4} | | |
| Azioni legali per decisione | 5.5 | <60 | ✅ |
| Fine partita | {'crepuscolo': 40, 'colpo_finale': 160} | | |
| G1 vince fra le partite finite al Crepuscolo | 67.5% [52.0–79.9] | | |
| G1 vince fra le partite arrivate al round 15 | 53.7% [40.6–66.3] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 22.2% [13.2–34.9] / 50.0% [25.4–74.6] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 33.3% [13.8–60.9]; 14.8% [7.7–26.6] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'3-2': 6, '2-1': 5, '2-3': 5, '2-0': 5, '1-0': 4, '1-1': 4, '2-2': 4, '3-4': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=17) | 31.5% [20.7–44.7] / 35.3% [17.3–58.7] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 12, 16: 4, 17: 1}; 52.9% [31.0–73.8] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 70.6% [46.9–86.7] / 41.2% [21.6–64.0]; 2.47 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–18.4] / 88.2% [65.7–96.7] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=6) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–39.0] / 63.6% [35.4–84.8]; 0.0% [0.0–39.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 3.0% [1.4–6.4] / 11.1% [5.2–22.2]; 100.0% [61.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 4, 'perd:pronto': 2, 'vinc:atk': 6} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=14) / turno di G2 (n=13) | 0.0% [0.0–21.5] / 0.0% [0.0–22.8] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=14) | 0.0% [0.0–21.5] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 55.6% [42.4–68.0] (13.0% [6.4–24.4]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 10, 'rif_LDR03_sanguinare_per_accendere': 7} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR03_sanguinare_per_accendere 54% (n=54) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 61.0% [54.1–67.5], rif_LDR03_sanguinare_per_accendere 39.0% [32.5–45.9]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.566 / 0.106 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.102 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.14 (0.00), rif_LDR03_sanguinare_per_accendere 0.10 (0.04) | |
| M4 | Scontri decisi prima dell'impegno | 27.3% [26.0–28.6] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.92 (100 / 84); 58.8% [57.4–60.3] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 57.6% [56.7–58.6]; rif_LDR02_muro_di_parata 59.4%, rif_LDR03_sanguinare_per_accendere 56.1% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.1% [0.0–0.4] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.000 (0) / 0.318 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 122 vittorie), LDR-03 R: 14.0 (35%, 78 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-02 1.92, NER-017 1.23, ROS-019 1.02, NER-006 0.92, NER-001 0.84, NER-008 0.80, ROS-011 0.76, BLU-001 0.70, NEW-I04 0.66, BLU-005 0.64, NER-013 0.59, NER-010 0.56 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.57, rif_LDR03_sanguinare_per_accendere 1.16 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR03_sanguinare_per_accendere 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 20% (n=10), rif_LDR03_sanguinare_per_accendere 26% (n=68) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.7% [9.8–11.7] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR03_sanguinare_per_accendere 1.50; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, RS 61%, NEU-003 61%, NER-014 61%, BLU-021 61%, NEU-015 61%, NEU-009 61%, collante 61%, caccia 39%, NER-009 39%, NER-017 39%, NER-010 39%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR03_sanguinare_per_accendere |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 61.0 [54–67] (200) |
| rif_LDR03_sanguinare_per_accendere | 39.0 [33–46] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 3.71 | 0.00 | 1.92 / 0.00 | 0.00 | 0.94 | 4.9 (194) | 8 | B 85%, K 15% | 2.38 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 3.71 | 0.00 | 0.00 / 0.00 | 2.70 | 0.00 | 4.4 (195) | 10 | K 63%, R 37% | 2.23 | 0.55 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR02_muro_di_parata | 1.92 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.00 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.78/0.70/0.17/0.11 | 0.74/0.00/0.14/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.73/0.00/0.16/0.19 | 0.00/0.00/0.00/0.00 | 0.00/0.43/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.35/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.92/1.63/0.65 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.90/0.00/0.09/0.06 | 0.88/0.64/0.08/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.01/0.00/0.00 | 0.41/0.00/0.00/0.00 | 0.43/0.32/0.02/0.01 | 0.36/0.01/0.04/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.10/0.14/0.18 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.66/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.45/0.00/0.12/0.03 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/1.58/0.53 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.77/0.84/0.20/0.11 | 0.91/0.92/0.14/0.06 | 0.00/0.00/0.00/0.00 | 0.02/0.00/0.00/0.00 | 0.37/0.09/0.25/0.09 | 0.00/0.23/0.00/0.00 | 0.00/0.07/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.47/0.00/0.05/0.01 | 0.00/0.00/0.00/0.00 | 0.38/0.12/0.13/0.06 | 0.76/1.02/0.34/0.23 | 0.00/0.12/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.46/0.00/0.10/0.04 | 0.85/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.43 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.81 | 0.00 | 0.02 | 0.08 | 0.04 | 0.07 | 0.12 | 0.15 | 0.12 | 0.08 | 0.03 | 0.04 | 0.03 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 200 | 1.25 | 0.00 | 0.04 | 0.07 | 0.16 | 0.14 | 0.18 | 0.12 | 0.15 | 0.12 | 0.10 | 0.06 | 0.04 | 0.04 | 0.03 | 1.50 | 0.28 | 0.24 | 0.23 | 0.20 | 0.20 | 0.10 | 0.09 | 0.07 | 0.04 | 0.01 | 0.04 | 0.01 | 0.01 | 0.01 |

## Q-026 M5: costo scelto (pagamenti per partita del mazzo; «stanca» = una tua Unità Stancata)

| Mazzo | NER-002 stanca | NER-002 vita |
|---|---|---|
| rif_LDR02_muro_di_parata | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 0.65 | 0.21 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 5 | 0 | 1 | 0 | 1 |
| 6 | 0 | 3 | 0 | 3 |
| 7 | 5 | 4 | 0 | 9 |
| 8 | 6 | 4 | 0 | 10 |
| 9 | 12 | 6 | 0 | 18 |
| 10 | 12 | 4 | 0 | 16 |
| 11 | 10 | 4 | 0 | 14 |
| 12 | 8 | 9 | 0 | 17 |
| 13 | 6 | 17 | 0 | 23 |
| 14 | 8 | 27 | 0 | 35 |
| 15 | 22 | 24 | 0 | 46 |
| 16 | 6 | 1 | 0 | 7 |
| 17 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 59.4% | 0.118 | 1.57 | 0.00 | 0.00 | 0.00 | 2.25 | 0.00 | 0.00 | 0.525 |
| rif_LDR03_sanguinare_per_accendere | 200 | 56.1% | 0.089 | 0.81 | 0.34 | 0.00 | 0.00 | 2.41 | 0.00 | 0.00 | 0.488 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 679 | 0.993 | 0.931 | 0.866 | 0.219 | 1851 | 0.981 | 0.359 | 0.149 | 0.065 |
| rif_LDR02_muro_di_parata | Cicatrice | 679 | 0.295 | 0.228 | 0.153 | 0.027 | 1851 | 0.279 | 0.071 | 0.028 | 0.006 |
| rif_LDR03_sanguinare_per_accendere | mano | 518 | 0.944 | 0.927 | 0.917 | 0.290 | 1404 | 0.880 | 0.313 | 0.000 | 0.000 |
| rif_LDR03_sanguinare_per_accendere | Cicatrice | 518 | 0.286 | 0.278 | 0.266 | 0.041 | 1404 | 0.279 | 0.100 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 20.0% | 2.42 | 1.95 | 35.1% | 0.5% | 23.2% | 37.0% | 8.8% | 0.00 | 18.0% | 59.4% | 0.01 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 200 | 20.0% | 2.42 | 1.95 | 27.4% | 0.5% | 19.8% | 33.2% | 8.6% | 0.00 | 12.3% | 56.1% | 0.14 | 0.00 |
| Totale | 400 | 20.0% | 2.42 | 1.95 | 30.8% | 0.5% | 21.5% | 35.1% | 8.7% | 0.00 | 14.9% | 57.6% | 0.08 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.369 | 0.234 | 0.2% | 0.0% | 1.20 | 0.20 | 0.71 | 0.75 | 0.00 | 0.00 | 3.35 |
| rif_LDR03_sanguinare_per_accendere | 200 | 0.401 | 0.000 | 0.0% | 0.0% | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.37 |

