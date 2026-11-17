# Torneo v0.2 — /root/in/dati/E-036-input/varianti/tempra_tardo.json

- Regole `v0.2`, configurazione `/root/in/dati/E-036-input/varianti/tempra_tardo.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_attivo', 'max_copies': 2, 'copies_by_name': True, 'max_copies_rarity': (('L', 1),), 'multicolor_all': True, 'rarity_scale': ('C', 'R', 'E', 'L'), 'tempra_tardo': 10}
- IA: forte:30; partite: 200; tempo 3387s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 41.3% [40.0–42.6] | 30–45% | ✅ |
| Durata mediana (round) | 14.0 [13.0–14.0] (media 13.15) | 8–11 | ❌ |
| Partite al round 13+ | 67.5% [60.7–73.6] | ≤12% | ❌ |
| Partite oltre il 15 | 9.0% [5.8–13.8] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–1.9] | 0 | ✅ |
| G1 vince (mirror) | nan% [nan–nan] | 48–52% | ❌ |
| Rimonte (n=69) | 27.5% [18.4–39.0] | 20–35% | ✅ |
| Attacchi con opposizione | 45.0% [43.6–46.3] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 73.6% [72.4–74.8] (con ≥3: 36.3% [35.0–37.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 33.3% [32.0–34.6] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 13.0% [10.1–16.5] (n=432) / 87.7% [82.8–91.4] (n=228) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 11.5% [10.1–13.1] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-02 Base 41.7% [24.5–61.2] (n=24), LDR-02 Risvegliato 70.2% [60.8–78.1] (n=104), LDR-05 Base 46.9% [30.9–63.6] (n=32), LDR-05 Risvegliato 67.7% [57.8–76.2] (n=96) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 69.1% [61.7–75.6] (n=165) | | |
| Attacchi per partita | 26.2 | | |
| Pugno attaccante vuoto / pieno | 50.7% [49.3–52.1] / 11.0% [10.1–11.9] (gemme medie 0.99) | non >90% | |
| Pugno difensore vuoto / pieno | 51.3% [49.3–53.2] / 26.5% [24.8–28.2] (gemme medie 0.33) | non >90% | |
| Reazioni per scontro | 0.11 | | |
| Modificatori per scontro (max; distribuzione) | 6; {0: 1770, 1: 1713, 2: 1066, 3: 454, 4: 155, 5: 64, 6: 15} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'crepuscolo': 56, 'colpo_finale': 144} | | |
| G1 vince fra le partite finite al Crepuscolo | 67.9% [54.8–78.6] | | |
| G1 vince fra le partite arrivate al round 15 | 52.9% [42.4–63.2] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 20.0% [12.9–29.7] / 47.1% [26.2–69.0] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 47.1% [26.2–69.0]; 21.2% [13.8–31.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'2-2': 12, '2-3': 10, '1-0': 8, '3-2': 8, '2-1': 7, '3-1': 4, '0-0': 4, '1-1': 4} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=27) | 31.8% [22.8–42.3] / 33.3% [18.6–52.2] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {16: 9, 15: 17, 17: 1}; 40.7% [24.5–59.3] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 63.0% [44.2–78.5] / 51.9% [34.0–69.3]; 2.56 | ≤50% (Cr) | |
| Q-022: fra gli spareggi, nessuno dei due attacca nel suo ultimo turno / il perdente attacca | 0.0% [0.0–12.5] / 100.0% [87.5–100.0] | | |
| Q-022: il vincitore non attacca, spareggi a Vite pari (n=9) / a Vite diverse; nessuno attacca a Vite pari | 0.0% [0.0–29.9] / 77.8% [54.8–91.0]; 0.0% [0.0–29.9] | | |
| Q-022: partite decise dal posto (ultima clausola dello spareggio), su tutte / fra le arrivate al R15; G2 vince gli spareggi a Vite pari | 4.5% [2.4–8.3] / 10.6% [5.7–18.9]; 100.0% [70.1–100.0] | | |
| Q-022: come si è ruotato il Leader nell'ultimo turno, spareggi a Vite pari (vincitore/perdente: atk, abil, rim, pronto) | {'perd:atk': 6, 'perd:pronto': 3, 'vinc:atk': 9} | | |
| Q-022 (critico): turni iniziati con entrambi i Leader Alle Corde a Vite pari dal R14, il giocatore di turno non attacca: turno di G1 (n=24) / turno di G2 (n=22) | 0.0% [0.0–13.8] / 0.0% [0.0–14.9] | ≤30% per chi perde la parità | |
| Q-022 (blu, critico): stessi round iniziati da G1 con entrambi Alle Corde a Vite pari, nessuno dei due attacca nel round (n=24) | 0.0% [0.0–13.8] | ≤25–30% | |
| Q-022: G1 nei mirror fra le partite finite prima del R15 | nan% [nan–nan] | | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 45.9% [35.7–56.4] (7.1% [3.3–14.6]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR05_scudi_armati': 14, 'rif_LDR02_muro_di_parata': 13} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 53% (n=85) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR02_muro_di_parata 44.5% [37.8–51.4], rif_LDR05_scudi_armati 55.5% [48.6–62.2]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.537 / 0.114 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.110 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR02_muro_di_parata 0.15 (0.00), rif_LDR05_scudi_armati 0.12 (0.00) | |
| M4 | Scontri decisi prima dell'impegno | 26.7% [25.6–27.9] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 0.00 (0 / 0); 55.0% [53.7–56.4] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 57.1% [56.2–57.9]; rif_LDR02_muro_di_parata 56.0%, rif_LDR05_scudi_armati 58.0% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.1% [0.0–0.3] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.296 (528) / 0.309 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-02 K: 6.0 (19%, 89 vittorie), LDR-05 B: 15.0 (41%, 111 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-05 3.52, LDR-02 1.55, ROS-018 0.91, BLU-015 0.81, BLU-001 0.76, BLU-005 0.70, ROS-020 0.64, NEW-I04 0.62, ROS-019 0.55, ROS-021 0.54, NEU-013 0.53, BLU-021 0.51 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR02_muro_di_parata 1.48, rif_LDR05_scudi_armati 0.12 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR02_muro_di_parata 24% (n=45), rif_LDR05_scudi_armati 33% (n=24) | 20–35% |
| M13 | Pugno d'attacco pieno | 11.0% [10.1–11.9] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR02_muro_di_parata 0.00, rif_LDR05_scudi_armati 0.00; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | BLU-021 100%, collante 100%, NEU-009 100%, ponte 100%, ROS-020 56%, NEU-013 56%, BLU-008 56%, BLU-010 56%, NEU-003 44%, NEU-015 44%, NER-014 44%, RS 44%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR02_muro_di_parata | rif_LDR05_scudi_armati |
|---|---|---|
| rif_LDR02_muro_di_parata | — | 44.5 [38–51] (200) |
| rif_LDR05_scudi_armati | 55.5 [49–62] (200) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 4.45 | 0.00 | 1.55 / 0.00 | 0.00 | 1.43 | 5.1 (196) | 8 | B 85%, K 15% | 2.05 | 0.00 |
| rif_LDR05_scudi_armati | 4.37 | 0.00 | 3.52 / 0.00 | 0.00 | 0.69 | 4.4 (198) | 13 | B 33%, R 67% | 1.90 | 0.00 |

## R-012: carte tracciate (per partita del mazzo: giocate / attivazioni / colpi a segno sul Leader / Unità sconfitte)

| Mazzo | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.84/0.94/0.23/0.18 | 0.80/0.00/0.23/0.16 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.83/0.00/0.38/0.28 | 0.00/0.00/0.00/0.00 | 0.00/0.54/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.31/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/1.55/1.64/1.07 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.97/0.00/0.09/0.07 | 0.96/0.70/0.09/0.09 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.03/0.00/0.00 | 0.39/0.00/0.00/0.00 | 0.47/0.38/0.07/0.04 | 0.46/0.00/0.14/0.08 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.49/0.15/0.15/0.32 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.62/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |
| rif_LDR05_scudi_armati | 0.00/0.00/0.00/0.00 | 0.00/3.52/1.66/0.48 | 0.68/0.58/0.12/0.07 | 0.77/0.00/0.20/0.11 | 0.70/0.49/0.19/0.17 | 0.65/0.27/0.20/0.17 | 0.00/0.00/0.00/0.00 | 0.69/0.81/0.20/0.25 | 0.00/0.47/0.00/0.00 | 0.00/0.41/0.00/0.00 | 0.00/0.15/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.67/0.53/0.28/0.18 | 0.76/0.42/0.18/0.06 | 0.00/0.00/0.00/0.00 | 0.88/0.49/0.21/0.09 | 0.00/0.29/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.68/0.26/0.13/0.20 | 0.00/0.00/0.00/0.00 | 0.43/0.91/0.00/0.00 | 0.68/0.64/0.28/0.32 | 0.52/0.54/0.24/0.27 | 0.27/0.14/0.14/0.12 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.29/0.00/0.09/0.04 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.82/0.00/0.04/0.01 | 0.73/0.09/0.06/0.04 | 0.65/0.29/0.17/0.20 | 0.66/0.55/0.17/0.21 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 | 0.00/0.00/0.00/0.00 |

## R-017: scontri vinti con Forza d'attacco ≥ 8 (per partita del mazzo; vinto = colpo a segno sul Leader o bersaglio sconfitto)

| Mazzo | Totale | LDR-01 | LDR-05 | BLU-001 | BLU-007 | BLU-008 | BLU-010 | BLU-012 | BLU-015 | BLU-021 | BLU-023 | BLU-025 | NEU-006 | NEU-013 | ROS-001 | ROS-003 | ROS-005 | ROS-007 | ROS-010 | ROS-015 | ROS-016 | ROS-018 | ROS-020 | ROS-021 | ROS-023 | ROS-025 | VER-001 | VER-002 | VER-009 | VER-011 | VER-019 | VER-024 | LDR-02 | LDR-03 | LDR-04 | LDR-06 | VER-012 | VER-013 | VER-023 | BLU-004 | BLU-005 | BLU-009 | BLU-022 | NER-001 | NER-006 | NER-007 | NER-012 | NER-018 | NER-023 | NER-025 | NEU-003 | NEU-004 | NEU-009 | NEU-010 | NEU-011 | NEU-012 | ROS-004 | ROS-006 | ROS-014 | ROS-019 | ROS-024 | VER-005 | VER-008 | VER-010 | VER-015 | VER-025 | BLU-003 | NEU-001 | ROS-008 | NER-002 | NER-019 | VER-021 | NEW-V05 | NEW-B06 | NEW-I04 | NEW-I05 | VER-004 | VER-003 | NER-011 | NEW-P31 | NEW-P32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 0.41 | 0.00 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.13 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 1.39 | 0.00 | 0.12 | 0.00 | 0.01 | 0.06 | 0.07 | 0.00 | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.16 | 0.00 | 0.00 | 0.23 | 0.34 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.04 | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: Rimarginare e costi in Vita per round (per partita del mazzo)

| Mazzo | n | Rimarginare | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | Costi in Vita | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 1.06 | 0.03 | 0.04 | 0.11 | 0.09 | 0.15 | 0.17 | 0.15 | 0.12 | 0.06 | 0.07 | 0.03 | 0.03 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 0.84 | 0.02 | 0.04 | 0.04 | 0.10 | 0.14 | 0.10 | 0.12 | 0.09 | 0.03 | 0.06 | 0.07 | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## Q-026 M5: vittorie per round finale (partite)

| Round finale | G1 | G2 | patta | Totale |
|---|---|---|---|---|
| 7 | 0 | 2 | 0 | 2 |
| 8 | 8 | 3 | 0 | 11 |
| 9 | 3 | 5 | 0 | 8 |
| 10 | 6 | 2 | 0 | 8 |
| 11 | 15 | 10 | 0 | 25 |
| 12 | 5 | 6 | 0 | 11 |
| 13 | 13 | 12 | 0 | 25 |
| 14 | 10 | 15 | 0 | 25 |
| 15 | 32 | 35 | 0 | 67 |
| 16 | 12 | 5 | 0 | 17 |
| 17 | 1 | 0 | 0 | 1 |

## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi | Scontri difesi con una Reazione giocabile |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 56.0% | 0.121 | 1.48 | 0.00 | 0.00 | 0.00 | 3.69 | 0.00 | 0.00 | 0.554 |
| rif_LDR05_scudi_armati | 200 | 58.0% | 0.106 | 0.12 | 0.00 | 0.00 | 0.00 | 2.97 | 0.00 | 0.00 | 0.397 |

## R-027 P9b: Reazioni per scontro difeso (disponibile / giocabile con la Guardia / legale con l'impegno / giocata)

| Mazzo | Fonte | Scontri con gemme del difensore | disp | giocabile | con l'impegno | giocata | Scontri a zero gemme | disp | giocabile | con l'impegno | giocata |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | mano | 641 | 0.989 | 0.939 | 0.885 | 0.279 | 2077 | 0.981 | 0.419 | 0.163 | 0.057 |
| rif_LDR02_muro_di_parata | Cicatrice | 641 | 0.337 | 0.271 | 0.193 | 0.039 | 2077 | 0.232 | 0.079 | 0.016 | 0.003 |
| rif_LDR05_scudi_armati | mano | 625 | 0.898 | 0.891 | 0.877 | 0.387 | 1894 | 0.808 | 0.215 | 0.000 | 0.000 |
| rif_LDR05_scudi_armati | Cicatrice | 625 | 0.173 | 0.166 | 0.158 | 0.040 | 1894 | 0.127 | 0.044 | 0.000 | 0.000 |

## R-028 (Q-028): ritmo (per partita del mazzo; Totale = tutte le partite, ognuna contata due volte)

| Mazzo | n | Chiuse dal Crepuscolo | Serie più lunga senza Vite perse R4–R10 | Round dopo il primo 0 Vite | Ribaltamenti da 0 Vite | Vittorie entro il R5 | Turni vuoti R1–3 | Turni senza giocare carte | Mano piena senza nulla di giocabile | Bruciate | Unità ferme: si è opposta | mai coinvolta (M6) | R-017 entro il R6 | Breccia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 28.0% | 3.07 | 1.49 | 26.5% | 0.0% | 21.2% | 37.0% | 12.5% | 0.00 | 18.0% | 56.0% | 0.01 | 0.00 |
| rif_LDR05_scudi_armati | 200 | 28.0% | 3.07 | 1.49 | 34.4% | 0.0% | 19.2% | 33.7% | 17.5% | 0.00 | 16.0% | 58.0% | 0.13 | 0.00 |
| Totale | 400 | 28.0% | 3.07 | 1.49 | 30.1% | 0.0% | 20.2% | 35.3% | 14.7% | 0.00 | 16.9% | 57.1% | 0.07 | 0.00 |

Turni vuoti R1–3: turni dei round 1–3 senza carta, attacco, Rimarginare o ⟳. Mano piena: almeno 6 carte alla prima scelta del turno, senza nessuna azione «gioca» legale. Unità ferme: Unità Pronte nella fase principale che non attaccano; «si è opposta» = poi si oppone nel turno avversario, «mai coinvolta» = no (è la M6). Round dopo il primo 0 Vite: sulle partite in cui un Leader arriva a 0 Vite. Ribaltamenti: Leader arrivati a 0 Vite che vincono.

## R-027 P7: Scudo per Leader (per partita del mazzo)

| Mazzo | n | Opposizioni per scontro difeso | di cui con Scudo | Opposizioni ripetute nel turno (tutte) | ripetute con Scudo | Unità con Scudo rimosse: scontro | caccia | attacco | sconfiggi | rimbalzo | sacrificio | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR02_muro_di_parata | 200 | 0.431 | 0.287 | 0.2% | 0.1% | 1.96 | 0.00 | 1.02 | 0.04 | 0.00 | 0.00 | 4.13 |
| rif_LDR05_scudi_armati | 200 | 0.470 | 0.168 | 0.0% | 0.0% | 1.05 | 0.00 | 0.68 | 0.74 | 0.00 | 0.00 | 4.58 |

