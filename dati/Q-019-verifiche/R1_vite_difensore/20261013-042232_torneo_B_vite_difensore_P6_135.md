# Torneo v0.2 — /home/claude/e020_in/dati/Q-019-input/spec/B_vite_difensore_P6_135.json

- Regole `v0.2`, configurazione `/home/claude/e020_in/dati/Q-019-input/spec/B_vite_difensore_P6_135.json`; differenze da B0: {'pugno': 'sequenziale', 'scudo': 'vince_pareggi', 'tempra': 4, 'scintilla_extra_gems': 1, 'scintilla_extra_round': 3, 'scintilla_extra_rounds': [5], 'crepuscolo_simultaneo': True, 'crepuscolo_spareggio': 'vite_difensore'}
- IA: cambio:14:forte:30; partite: 10080; tempo 2381s

| Metrica | Valore [IC 95%] | Fascia | Esito |
|---|---|---|---|
| Attacchi fermati | 57.8% [57.7–58.0] | 30–45% | ❌ |
| Durata mediana (round) | 10.0 [10.0–10.0] (media 10.50) | 8–11 | ✅ |
| Partite al round 13+ | 27.5% [26.6–28.3] | ≤12% | ❌ |
| Partite oltre il 15 | 3.6% [3.2–4.0] | <2% | ❌ |
| Vittorie prima del round 5 | 0.0% [0.0–0.0] | 0 | ✅ |
| G1 vince (mirror) | 51.1% [49.3–52.9] | 48–52% | ✅ |
| Rimonte (n=2542) | 20.3% [18.8–21.9] | 20–35% | ✅ |
| Attacchi con opposizione | 14.1% [14.0–14.2] | 15–35% (V4) | |
| Turni con Unità Pronte ferme | 40.4% [40.2–40.7] (con ≥3: 7.5% [7.4–7.6]) | ≤35% (V4) | |
| Attacchi a segno sul Leader | 26.2% [26.0–26.3] | | |
| Colpi del Leader a segno senza gemme: Base / Risvegliato (Q-017) | 0.0% [0.0–0.0] (n=19560) / 95.1% [94.8–95.3] (n=23118) | | |
| Colpi a segno sui Leader dati dal Risvegliato senza gemme (drain, Q-017) | 22.6% [22.3–22.8] | <35% (Cr) | |
| Colpi del Leader senza gemme con Rimarginare legale, per Leader e lato (Q-017) | LDR-01 Risvegliato 79.3% [77.9–80.7] (n=3174), LDR-02 Risvegliato 85.1% [83.7–86.4] (n=2739), LDR-03 Risvegliato 99.9% [99.7–99.9] (n=5653), LDR-04 Risvegliato 70.9% [69.1–72.7] (n=2422), LDR-05 Risvegliato 86.5% [85.2–87.8] (n=2650), LDR-06 Risvegliato 72.0% [70.8–73.2] (n=5339) | | |
| Round 13+ nelle partite con entrambi Risvegliati (Q-017) | 24.5% [23.6–25.4] (n=8457) | | |
| Attacchi per partita | 36.9 | | |
| Pugno attaccante vuoto / pieno | 72.6% [72.5–72.8] / 9.6% [9.5–9.7] (gemme medie 0.40) | non >90% | |
| Pugno difensore vuoto / pieno | 66.0% [65.8–66.2] / 14.4% [14.2–14.5] (gemme medie 0.22) | non >90% | |
| Reazioni per scontro | 0.05 | | |
| Modificatori per scontro (max; distribuzione) | 7; {0: 182943, 1: 115759, 2: 55811, 3: 12520, 4: 3971, 5: 852, 6: 151, 7: 2} | | |
| Azioni legali per decisione | 5.1 | <60 | ✅ |
| Fine partita | {'colpo_finale': 8824, 'crepuscolo': 1256} | | |
| G1 vince fra le partite finite al Crepuscolo | 56.3% [53.5–59.0] | | |
| G1 vince fra le partite arrivate al round 15 | 56.0% [53.4–58.5] | | |
| Q-019: pareggi al primo Crepuscolo (entrambi Alle Corde) / Vite pari fra i pareggi | 17.2% [15.3–19.2] / 46.0% [39.9–52.2] | | |
| Q-019: G1 vince fra i pareggi; partite vive al round 16 | 75.2% [69.5–80.1]; 24.7% [22.6–27.0] | | |
| Q-019: Vite G1-G2 al primo Crepuscolo (più frequenti) | {'0-2': 117, '2-0': 96, '1-0': 73, '2-2': 73, '3-2': 70, '0-0': 69, '0-1': 62, '2-3': 55} | | |
| Q-019: spareggi (entrambi Alle Corde) a qualunque controllo, fra le arrivate al R15 / Vite pari fra gli spareggi (n=450) | 30.9% [28.6–33.3] / 48.9% [44.3–53.5] | | |
| Q-019: spareggi per round; G2 vince lo spareggio | {15: 250, 16: 163, 17: 37}; 23.8% [20.1–27.9] | | |
| Q-019 R-1: stallo fra gli spareggi: il vincitore non va a segno / non attacca nel suo ultimo turno; Guardia media del vincitore nella sua ultima Fine | 95.1% [92.7–96.7] / 69.8% [65.4–73.8]; 3.23 | ≤50% (Cr) | |
| Q-019: partite finite dal R15 vinte senza colpi a segno del vincitore nei R14–15 (di cui vinte da G2) | 84.6% [82.7–86.4] (36.8% [34.3–39.3]) | | |
| Q-019: vincitori degli spareggi per mazzo | {'rif_LDR04_stanca_e_smonta': 159, 'rif_LDR02_muro_di_parata': 140, 'rif_LDR06_ferite_e_caccia': 86, 'rif_LDR01_puntata_e_preda': 25, 'rif_LDR05_scudi_armati': 22, 'rif_LDR03_sanguinare_per_accendere': 18} | | |
| Q-019: G1 fra le arrivate al R15 per coppia di mazzi | rif_LDR01_puntata_e_preda vs rif_LDR01_puntata_e_preda 100% (n=4), rif_LDR01_puntata_e_preda vs rif_LDR02_muro_di_parata 67% (n=45), rif_LDR01_puntata_e_preda vs rif_LDR03_sanguinare_per_accendere 0% (n=1), rif_LDR01_puntata_e_preda vs rif_LDR04_stanca_e_smonta 64% (n=56), rif_LDR01_puntata_e_preda vs rif_LDR05_scudi_armati 64% (n=11), rif_LDR01_puntata_e_preda vs rif_LDR06_ferite_e_caccia 68% (n=19), rif_LDR02_muro_di_parata vs rif_LDR02_muro_di_parata 58% (n=163), rif_LDR02_muro_di_parata vs rif_LDR03_sanguinare_per_accendere 64% (n=25), rif_LDR02_muro_di_parata vs rif_LDR04_stanca_e_smonta 60% (n=257), rif_LDR02_muro_di_parata vs rif_LDR05_scudi_armati 59% (n=73), rif_LDR02_muro_di_parata vs rif_LDR06_ferite_e_caccia 61% (n=146), rif_LDR03_sanguinare_per_accendere vs rif_LDR04_stanca_e_smonta 43% (n=47), rif_LDR03_sanguinare_per_accendere vs rif_LDR05_scudi_armati 100% (n=1), rif_LDR03_sanguinare_per_accendere vs rif_LDR06_ferite_e_caccia 60% (n=10), rif_LDR04_stanca_e_smonta vs rif_LDR04_stanca_e_smonta 54% (n=321), rif_LDR04_stanca_e_smonta vs rif_LDR05_scudi_armati 74% (n=34), rif_LDR04_stanca_e_smonta vs rif_LDR06_ferite_e_caccia 42% (n=158), rif_LDR05_scudi_armati vs rif_LDR05_scudi_armati 50% (n=2), rif_LDR05_scudi_armati vs rif_LDR06_ferite_e_caccia 42% (n=24), rif_LDR06_ferite_e_caccia vs rif_LDR06_ferite_e_caccia 45% (n=60) | | |
| Nelle fasce comuni | no | | |

Vittorie per mazzo: rif_LDR01_puntata_e_preda 59.1% [57.4–60.7], rif_LDR02_muro_di_parata 45.1% [43.4–46.8], rif_LDR03_sanguinare_per_accendere 60.7% [59.1–62.4], rif_LDR04_stanca_e_smonta 28.1% [26.6–29.6], rif_LDR05_scudi_armati 66.3% [64.7–67.9], rif_LDR06_ferite_e_caccia 40.7% [39.0–42.3]

## Metriche diagnostiche R-005 (M1–M15)

| # | Metrica | Valore | Obiettivo |
|---|---|---|---|
| M1 | Reazioni disponibili / giocate per scontro | 0.516 / 0.053 | giocate ≥0.10 |
| M2 | Reazioni decisive per scontro | 0.051 | ≥0.05 |
| M3 | Reazioni da Cicatrici dritte per partita (di cui nate da un costo in Vita) | rif_LDR01_puntata_e_preda 0.14 (0.00), rif_LDR02_muro_di_parata 0.22 (0.00), rif_LDR03_sanguinare_per_accendere 0.12 (0.04), rif_LDR04_stanca_e_smonta 0.15 (0.00), rif_LDR05_scudi_armati 0.16 (0.00), rif_LDR06_ferite_e_caccia 0.16 (0.03) | |
| M4 | Scontri decisi prima dell'impegno | 26.7% [26.6–26.8] | |
| M5 | Attacchi con Caccia per partita (su Pronte / Ruotate); attacchi sul Leader | 2.97 (3707 / 26228); 78.8% [78.7–79.0] | |
| M6 | Unità ferme (né attaccano né si oppongono) | 24.9% [24.7–25.0]; rif_LDR01_puntata_e_preda 27.5%, rif_LDR02_muro_di_parata 16.6%, rif_LDR03_sanguinare_per_accendere 23.1%, rif_LDR04_stanca_e_smonta 29.0%, rif_LDR05_scudi_armati 28.1%, rif_LDR06_ferite_e_caccia 20.5% | ≤38%, verdi ≤35% |
| M7 | Opposizioni ripetute della stessa Unità nel turno | 0.0% [0.0–0.0] | ≤3% |
| M8 | Gemme contate sia per la Reazione sia per Impeto | 0 | 0 |
| M9 | Opposizioni per Unità che può opporsi: con Impeto / tutte | 0.355 (16251) / 0.365 | |
| M10 | Colore minore nei mazzi vincenti, per Leader (carte, quota) | LDR-01 G: 14.0 (37%, 1985 vittorie), LDR-02 K: 9.0 (26%, 1516 vittorie), LDR-03 R: 15.0 (38%, 2041 vittorie), LDR-04 B: 13.0 (35%, 944 vittorie), LDR-05 R: 18.0 (49%, 2228 vittorie), LDR-06 G: 16.0 (43%, 1366 vittorie) | ≥35% |
| M11 | Attivazioni per partita (prime 12) | LDR-04 6.73, LDR-05 4.95, LDR-06 3.14, VER-020 2.63, LDR-02 2.15, VER-008 1.92, BLU-011 1.59, ROS-016 1.51, NER-001 1.44, LDR-01 1.36, NEU-001 1.33, NER-008 1.33 | |
| M12 | Rimozioni per partita (effetti e Caccia) | rif_LDR01_puntata_e_preda 0.83, rif_LDR02_muro_di_parata 1.83, rif_LDR03_sanguinare_per_accendere 1.10, rif_LDR04_stanca_e_smonta 4.32, rif_LDR05_scudi_armati 0.14, rif_LDR06_ferite_e_caccia 4.05 | |
| R9-5 | Unità Stancate da Pronte e rimosse nello stesso turno, per partita | rif_LDR01_puntata_e_preda 0.05, rif_LDR02_muro_di_parata 0.00, rif_LDR03_sanguinare_per_accendere 0.00, rif_LDR04_stanca_e_smonta 0.89, rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.22 | allarme >1 con LDR-04/LDR-06 |
| R9-6 | Attacchi dichiarati al Leader per turno con ROS-022 e VER-022 in gioco | mai insieme | |
| R9-8 | Rimonte per mazzo (chi era indietro di ≥2 Vite al round 6) | rif_LDR01_puntata_e_preda 18% (n=373), rif_LDR02_muro_di_parata 23% (n=252), rif_LDR03_sanguinare_per_accendere 29% (n=355), rif_LDR04_stanca_e_smonta 9% (n=612), rif_LDR05_scudi_armati 20% (n=162), rif_LDR06_ferite_e_caccia 25% (n=788) | 20–35% |
| M13 | Pugno d'attacco pieno | 9.6% [9.5–9.7] | |
| M14 | Costi in Vita pagati per partita; vittorie per IA (partite miste) | rif_LDR01_puntata_e_preda 0.00, rif_LDR02_muro_di_parata 0.00, rif_LDR03_sanguinare_per_accendere 1.35, rif_LDR04_stanca_e_smonta 0.00, rif_LDR05_scudi_armati 0.00, rif_LDR06_ferite_e_caccia 0.97; nessuna partita mista (comando `vita`) | |
| M15 | Presenza nei mazzi vincenti (slot e Caccia) | ponte 100%, caccia 63%, collante 60%, VER-001 43%, BLU-021 37%, NER-017 34%, NER-009 34%, BLU-010 31%, VER-023 23%, VER-008 23%, NEU-013 22%, BLU-008 22%; oltre il 60%: nessuno | nessuno slot di Caccia o 11.1 >60% |

## R-012: matrice degli incroci (vittorie della riga contro la colonna, n)

| | rif_LDR01_puntata_e_preda | rif_LDR02_muro_di_parata | rif_LDR03_sanguinare_per_accendere | rif_LDR04_stanca_e_smonta | rif_LDR05_scudi_armati | rif_LDR06_ferite_e_caccia |
|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | — | 65.6 [61–70] (480) | 48.8 [44–53] (480) | 93.1 [91–95] (480) | 32.3 [28–37] (480) | 73.8 [70–77] (480) |
| rif_LDR02_muro_di_parata | 34.4 [30–39] (480) | — | 36.0 [32–40] (480) | 64.0 [60–68] (480) | 26.0 [22–30] (480) | 55.4 [51–60] (480) |
| rif_LDR03_sanguinare_per_accendere | 51.2 [47–56] (480) | 64.0 [60–68] (480) | — | 87.7 [84–90] (480) | 44.2 [40–49] (480) | 78.1 [74–82] (480) |
| rif_LDR04_stanca_e_smonta | 6.9 [5–9] (480) | 36.0 [32–40] (480) | 12.3 [10–16] (480) | — | 5.0 [3–7] (480) | 36.5 [32–41] (480) |
| rif_LDR05_scudi_armati | 67.7 [63–72] (480) | 74.0 [70–78] (480) | 55.8 [51–60] (480) | 95.0 [93–97] (480) | — | 71.7 [67–76] (480) |
| rif_LDR06_ferite_e_caccia | 26.2 [23–30] (480) | 44.6 [40–49] (480) | 21.9 [18–26] (480) | 63.5 [59–68] (480) | 28.3 [24–33] (480) | — |

## R-012: contatori per mazzo (per partita)

| Mazzo | Attacchi del Leader | on_attack del Leader eseguiti | Attivazioni del Leader (⟳ e trigger) / ⟳ seguite da un colpo a segno | Scontri con furia_bonus | Scudo a ≥2 gemme | Round del primo colpo al Leader (media, n) | Forza max a 2 gemme | Carte giocate per colore | Turni con una sola Unità in campo | Attacchi al Leader di Unità con Caccia |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 7.98 | 0.00 | 1.36 / 0.00 | 0.00 | 0.00 | 5.0 (3343) | 13 | G 37%, R 63% | 2.67 | 0.25 |
| rif_LDR02_muro_di_parata | 9.52 | 0.00 | 2.15 / 0.00 | 0.00 | 1.11 | 4.8 (3296) | 8 | B 79%, K 21% | 3.10 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 5.97 | 0.00 | 0.00 / 0.00 | 2.67 | 0.00 | 3.9 (3354) | 10 | K 59%, R 41% | 2.01 | 0.29 |
| rif_LDR04_stanca_e_smonta | 5.60 | 0.00 | 6.73 / 0.39 | 0.00 | 0.78 | 5.8 (3041) | 10 | B 39%, G 61% | 2.74 | 0.76 |
| rif_LDR05_scudi_armati | 8.14 | 0.00 | 4.95 / 0.00 | 0.00 | 0.52 | 5.0 (3354) | 13 | B 47%, R 53% | 2.05 | 0.00 |
| rif_LDR06_ferite_e_caccia | 7.91 | 0.00 | 3.14 / 0.02 | 0.00 | 0.37 | 4.2 (3314) | 10 | G 62%, K 38% | 2.86 | 2.62 |

