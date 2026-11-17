# Torneo v0.2 — /root/in38/dati/E-038-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in38/dati/E-038-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 2345s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 42.0% [40.7–43.4] | 30–45% | ✅ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 12.82) | 8–11 | ❌ |
| Partite al round 13+ | 63.5% [56.6–69.9] | ≤12% | ❌ |
| Partite oltre il 15 | 6.0% [3.5–10.2] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=82) | 28.0% [19.5–38.6] | 20–35% | ✅ |
| Attacchi con opposizione | 45.5% [44.1–46.9] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 74.0% [72.8–75.2] (con ≥3: 36.8% [35.4–38.1]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 32.4% [31.1–33.7] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 8.9% [6.4–12.3] (n=360) / 90.9% [85.9–94.2] (n=186) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 10.8% [9.4–12.4] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 50.0% [29.9–70.1] (n=20), LDR-02 Risvegliato 82.5% [70.6–90.2] (n=57), LDR-05 Base 33.3% [13.8–60.9] (n=12), LDR-05 Risvegliato 70.5% [61.5–78.2] (n=112) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 65.7% [58.2–72.5] (n=166) | | |
| Attacchi per partita | 24.2 | | |
| Pugno attaccante vuoto / pieno | 50.3% [48.8–51.7] / 10.7% [9.8–11.6] (gemme medie 0.98) | non >90% | |
| Pugno difensore vuoto / pieno | 50.1% [48.1–52.1] / 26.4% [24.7–28.2] (gemme medie 0.34) | non >90% | |
| Reazioni per scontro | 0.11 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1508, 1: 1725, 2: 980, 3: 429, 4: 134, 5: 44, 6: 13} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'crepuscolo': 53, 'colpo_finale': 147} | | |
| G1 vince fra le partite finite al Crepuscolo | 86.8% [75.2–93.5] | | |
| G1 vince fra le partite arrivate al round 15 | 72.4% [61.4–81.2] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 9.2% [4.5–17.8] / 57.1% [25.0–84.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 42.9% [15.8–75.0]; 15.8% [9.3–25.6] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 14, '2-1': 13, '2-0': 10, '2-3': 7, '3-2': 7, '1-1': 4, '3-1': 4, '1-0': 3} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=15) | 19.7% [12.3–30.0] / 26.7% [10.9–52.0] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 8, 15: 7}; 33.3% [15.2–58.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 80.0% [54.8–93.0] / 46.7% [24.8–69.9]; 2.40 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–20.4] / 86.7% [62.1–96.3] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=4) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–49.0] / 63.6% [35.4–84.8]; 0.0% [0.0–49.0] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 2.0% [0.8–5.0] / 5.3% [2.1–12.8]; 100.0% [51.0–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 2, 'perd:pronto': 2, 'vinc:atk': 4} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=26) / turno di G2 (n=20) | 0.0% [0.0–12.9] / 0.0% [0.0–16.1] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=26) | 0.0% [0.0–12.9] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 59.2% [48.0–69.6] (3.9% [1.4–11.0]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR02_muro_di_parata': 9, 'rif_LDR05_scudi_armati': 6} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 72% (n=76) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 54.5% [47.6–61.3], rif_LDR05_scudi_armati 45.5% [38.7–52.4]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.542 / 0.112 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.109 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.14 (0.00), rif_LDR05_scudi_armati 0.13 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 25.7% [24.5–27.0] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 54.5% [53.1–55.9] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 58.9% [58.0–59.7]; rif_LDR02_muro_di_parata 58.0%, rif_LDR05_scudi_armati 59.7% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.2% [0.1–0.5] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.297 (466) / 0.311 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 109 vittorie), LDR-05 R: 18.0 (49%, 91 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.88, LDR-02 1.54, BLU-015 0.86, BLU-005 0.77, NEW-I04 0.69, BLU-001 0.68, BLU-008 0.56, ROS-020 0.56, ROS-018 0.53, BLU-023 0.43, NEU-013 0.43, ROS-001 0.43 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.42, rif_LDR05_scudi_armati 0.10 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 31% (n=16), rif_LDR05_scudi_armati 27% (n=66) | 20–35% |
| M13 | Pugno d'attacco pieno | 10.7% [9.8–11.6] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | collante 100%, ponte 100%, NEU-009 100%, BLU-021 100%, NEU-003 55%, RS 55%, NEU-015 55%, NER-014 55%, NEU-013 46%, BLU-010 46%, ROS-020 46%, BLU-008 46%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 54.5 [48–61] (200) |
| rif_LDR05_scudi_armati | 45.5 [39–52] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 3.98 | 0.00 | 1.54 / 0.00 | 0.00 | 1.37 | 4.7 (195) | 8 | B 84%, K 16% | 2.07 | 0.00 |
| rif_LDR05_scudi_armati | 4.16 | 0.00 | 3.88 / 0.00 | 0.00 | 0.86 | 4.5 (199) | 13 | B 47%, R 53% | 1.76 | 0.00 |

## R-031: attivazioni del Leader per lato (per partita del mazzo)

Le stesse attivazioni della colonna R-012 (⟳, trigger e statiche in scontro), divise secondo il lato del Leader al momento dell'attivazione.

| Mazzo | Base | Risvegliato |
|---|---|---|
| rif_LDR02_muro_di_parata | 1.54 | 0.00 |
| rif_LDR05_scudi_armati | 1.22 | 2.67 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.79/0.91/0.28/0.17 | 0.80/0.00/0.19/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.75/0.00/0.29/0.29 | 0.00/0.00/0.00/0.00 | 0.00/0.42/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.28/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.54/1.33/0.99 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.93/0.00/0.07/0.05 | 0.89/0.77/0.10/0.06 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.03/0.00/0.00 | 0.40/0.00/0.00/0.00 | 0.41/0.41/0.04/0.02 | 0.42/0.00/0.11/0.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.50/0.12/0.14/0.26 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.69/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.88/1.40/0.76 | 0.65/0.45/0.09/0.06 | 0.66/0.00/0.10/0.07 | 0.69/0.56/0.30/0.15 | 0.64/0.21/0.20/0.12 | 0.57/0.00/0.18/0.08 | 0.68/0.86/0.28/0.20 | 0.00/0.39/0.00/0.00 | 0.00/0.43/0.00/0.00 | 0.00/0.13/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.65/0.43/0.25/0.17 | 0.76/0.43/0.18/0.07 | 0.00/0.00/0.00/0.00 | 0.72/0.39/0.13/0.06 | 0.00/0.23/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.56/0.12/0.13/0.12 | 0.00/0.00/0.00/0.00 | 0.35/0.53/0.00/0.00 | 0.68/0.56/0.30/0.30 | 0.47/0.41/0.18/0.26 | 0.24/0.10/0.12/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.81/0.00/0.08/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.30/0.00/0.07/0.05 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.33/0.00/0.03/0.00 | 0.48/0.07/0.07/0.04 | 0.34/0.16/0.15/0.10 | 0.34/0.23/0.12/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.39 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.12 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.03 | 0.00 | 0.09 | 0.00 | 0.01 | 0.04 | 0.03 | 0.02 | 0.06 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.03 | 0.00 | 0.01 | 0.00 | 0.00 | 0.06 | 0.00 | 0.00 | 0.23 | 0.24 | 0.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.01 | 0.03 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.00 | 0.03 | 0.04 | 0.09 | 0.10 | 0.14 | 0.14 | 0.17 | 0.12 | 0.04 | 0.05 | 0.04 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.84 | 0.02 | 0.05 | 0.10 | 0.10 | 0.10 | 0.12 | 0.12 | 0.09 | 0.02 | 0.02 | 0.04 | 0.03 | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 6 | 1 | 0 | 0 | 1 |
| 7 | 0 | 4 | 0 | 4 |
| 8 | 5 | 4 | 0 | 9 |
| 9 | 8 | 8 | 0 | 16 |
| 10 | 9 | 8 | 0 | 17 |
| 11 | 11 | 4 | 0 | 15 |
| 12 | 6 | 5 | 0 | 11 |
| 13 | 7 | 11 | 0 | 18 |
| 14 | 11 | 22 | 0 | 33 |
| 15 | 44 | 20 | 0 | 64 |
| 16 | 11 | 1 | 0 | 12 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 58.0% | 0.119 | 1.42 | 0.00 | 0.00 | 0.00 | 3.35 | 0.00 | 0.00 | 0.534 |
| rif_LDR05_scudi_armati | 200 | 59.7% | 0.104 | 0.10 | 0.00 | 0.00 | 0.00 | 2.84 | 0.00 | 0.00 | 0.421 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 618 | 0.995 | 0.935 | 0.862 | 0.246 | 1963 | 0.987 | 0.389 | 0.153 | 0.065 |
| rif_LDR02_muro_di_parata | Cicatrice | 618 | 0.354 | 0.262 | 0.209 | 0.029 | 1963 | 0.283 | 0.085 | 0.019 | 0.005 |
| rif_LDR05_scudi_armati | mano | 591 | 0.904 | 0.895 | 0.876 | 0.354 | 1661 | 0.840 | 0.233 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 591 | 0.169 | 0.162 | 0.154 | 0.044 | 1661 | 0.137 | 0.054 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 26.5% | 2.81 | 1.89 | 28.6% | 0.0% | 20.0% | 37.2% | 12.9% | 0.00 | 18.1% | 58.0% | 0.01 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 26.5% | 2.81 | 1.89 | 26.0% | 0.0% | 19.5% | 36.3% | 18.7% | 0.00 | 14.6% | 59.7% | 0.17 | 0.00 |
| Totale | 400 | 26.5% | 2.81 | 1.89 | 27.3% | 0.0% | 19.8% | 36.7% | 15.5% | 0.00 | 16.2% | 58.9% | 0.09 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.437 | 0.284 | 0.4% | 0.5% | 1.75 | 0.00 | 0.93 | 0.04 | 0.00 | 0.00 | 3.44 |
| rif_LDR05_scudi_armati | 200 | 0.475 | 0.238 | 0.0% | 0.0% | 1.53 | 0.00 | 0.96 | 0.85 | 0.00 | 0.00 | 4.38 |

