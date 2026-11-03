# Q-028: metriche del divertimento (F1–F6)

Torneo: 6 liste rif_ di B0c05 (corrette dal critico), 15 incroci × 20 partite = 300, IA forte:30, preset V027, semi 3600+k (k = indice dell'incrocio). Motore: main ad77242, non modificato. Script: `script/metriche_f.py`.

Per Leader i valori sono per partita della lista (ogni partita conta per entrambe le liste).

**Numeri chiave (lettura del programmatore):**
- **F2:** le Unità ferme sono il 47–55% per ogni Leader, contro un obiettivo ≤38%. Le Reazioni per scontro difeso sono 0.06–0.08, con 0.11 solo per L5.
- **F6:** chi è avanti nelle Vite a fine round 6 vince il 66.9% delle partite.
- **F4:** il 48.7% delle partite arriva al round 13 o oltre e il 16.7% finisce al Crepuscolo. Si fanno 0.73 colpi al Leader per round, e la serie più lunga di round senza Vite perse dura in media 3.5 round.
- **F3:** nel 34% delle partite (103 su 300) il vincitore chiude anche lui a 0 Vite. Il margine finale è 0 o 1 nel 69% dei casi.

Le partite giocate dopo un riavvio del container sono riprese dal salvataggio: con lo stesso seme ogni partita è identica.

## F1. Decisioni

| Leader | Azioni legali alla prima scelta del turno | Azioni legali per scelta (fase principale) | Scelte per turno | Turni con una sola azione legale (solo «fine») | Turni senza giocare carte |
|---|---|---|---|---|---|
| LDR01 | 9.8 | 7.1 | 3.2 | 1.4% | 27.4% |
| LDR02 | 6.6 | 5.0 | 2.7 | 4.8% | 42.7% |
| LDR03 | 9.5 | 7.0 | 3.2 | 1.3% | 33.9% |
| LDR04 | 10.2 | 7.3 | 3.2 | 3.1% | 28.5% |
| LDR05 | 8.5 | 6.3 | 3.1 | 1.7% | 31.1% |
| LDR06 | 11.8 | 8.4 | 3.2 | 3.0% | 31.7% |
| Totale | 9.3 | 6.9 | 3.1 | 2.6% | 32.6% |

Turno = turno del giocatore attivo, fase principale (attacchi, carte, ⟳). Le scelte di gemme, opposizioni e Reazioni non sono contate qui. "Passo forzato" = alla prima scelta del turno l'unica azione legale è «fine».

## F2. Interazione (tabella R-026 del report del motore)
## R-026 (Q-027): interattività per Leader (per partita del mazzo)

| Mazzo | n | Unità ferme (M6) | Reazioni per scontro difeso | Rimozioni: sconfiggi | caccia | rimbalzo | sacrificio (tue) | Unità avversarie sconfitte in scontro | Sacrifici | Recuperi |
|---|---|---|---|---|---|---|---|---|---|---|
| rif_LDR01_puntata_e_preda | 100 | 52.5% | 0.062 | 0.00 | 0.65 | 0.00 | 0.00 | 3.32 | 0.00 | 0.00 |
| rif_LDR02_muro_di_parata | 100 | 47.4% | 0.066 | 1.54 | 0.00 | 0.00 | 0.00 | 3.33 | 0.00 | 0.00 |
| rif_LDR03_sanguinare_per_accendere | 100 | 51.7% | 0.078 | 0.66 | 0.74 | 0.00 | 0.00 | 3.29 | 0.00 | 0.00 |
| rif_LDR04_stanca_e_smonta | 100 | 53.4% | 0.081 | 2.21 | 0.77 | 0.00 | 0.00 | 2.56 | 0.00 | 0.00 |
| rif_LDR05_scudi_armati | 100 | 54.6% | 0.114 | 0.06 | 0.00 | 0.00 | 0.00 | 3.33 | 0.00 | 0.00 |
| rif_LDR06_ferite_e_caccia | 100 | 46.9% | 0.065 | 1.00 | 2.08 | 0.00 | 0.00 | 3.91 | 0.00 | 0.00 |

## F3. Tensione

- Cambi di comando nelle Vite (chi è avanti, all'inizio di ogni turno; i pareggi non contano): **0.73 a partita**.
- Rimonte (il vincitore è stato sotto di ≥2 Vite): **27.7%** delle partite vinte.
- Margine finale di Vite: media **1.20**, mediana 1.0; distribuzione 0: 103, 1: 105, 2: 48, 3: 24, 4: 13, 5: 7.
- Round da cui il vincitore non è più dietro: media **6.2**, mediana 6.0; mai dietro (round 1): 39.7%.

| Leader | Partite | Vittorie | Rimonte (sul totale delle sue vittorie) | Cambi di comando a partita |
|---|---|---|---|---|
| LDR01 | 100 | 56.0% | 23.2% | 0.78 |
| LDR02 | 100 | 45.0% | 22.2% | 0.72 |
| LDR03 | 100 | 46.0% | 52.2% | 0.65 |
| LDR04 | 100 | 43.0% | 23.3% | 0.73 |
| LDR05 | 100 | 70.0% | 11.4% | 0.79 |
| LDR06 | 100 | 40.0% | 45.0% | 0.69 |

## F4. Ritmo

- Round finale: media **12.0**, mediana 12.0; round 13+ **48.7%**; oltre il 15 2.3%.
- Distribuzione: R5: 1, R6: 3, R7: 7, R8: 18, R9: 23, R10: 38, R11: 28, R12: 36, R13: 42, R14: 43, R15: 54, R16: 7.
- Fine partita: colpo_finale 83.3%, crepuscolo 16.7%.
- Round consecutivi senza Vite perse (da nessuno dei due): serie più lunga per partita media **3.5** (massimo 8); lunghezza media di una serie 2.0.
- Colpi a segno sul Leader per round (somma dei due giocatori): **0.73**.

## F5. Varietà

| Leader | Unità giocate | Tattiche | Reliquie | Reazioni | Attacchi del Leader | Rimarginare | Attacchi totali | Colpi al Leader avversario |
|---|---|---|---|---|---|---|---|---|
| LDR01 | 9.8 | 1.4 | 0.7 | 0.8 | 3.9 | 0.94 | 12.9 | 4.9 |
| LDR02 | 6.2 | 0.9 | 1.0 | 1.0 | 4.7 | 1.36 | 11.1 | 3.8 |
| LDR03 | 8.7 | 1.0 | 0.0 | 0.8 | 3.8 | 1.36 | 13.4 | 4.9 |
| LDR04 | 9.8 | 2.7 | 0.2 | 1.1 | 5.7 | 1.10 | 12.7 | 3.8 |
| LDR05 | 10.5 | 0.0 | 0.4 | 1.5 | 4.0 | 0.78 | 13.1 | 4.9 |
| LDR06 | 9.0 | 1.7 | 0.0 | 0.8 | 4.3 | 0.92 | 13.4 | 3.9 |

Reazioni = Reazioni giocate in difesa (contatore `reactions`); le altre colonne contano le carte giocate nella fase principale.

**Carte delle liste giocate meno di 0.1 volte a partita (copie nella lista):**

- LDR01: nessuna
- LDR02: nessuna
- LDR03: NER-012 ×1 (0.03)
- LDR04: nessuna
- LDR05: nessuna
- LDR06: nessuna

Le Reazioni sono escluse: si giocano in difesa e `cards_played` non le conta.

## F6. Frustrazione

| Leader | Turni senza nessuna carta giocabile alla prima scelta | Turni con mano ≥6 | … e nessuna carta giocabile |
|---|---|---|---|
| LDR01 | 8.1% | 61.8% | 4.0% |
| LDR02 | 19.4% | 95.6% | 15.9% |
| LDR03 | 11.9% | 79.4% | 11.6% |
| LDR04 | 10.6% | 81.1% | 6.8% |
| LDR05 | 17.6% | 62.3% | 16.0% |
| LDR06 | 11.3% | 86.6% | 9.1% |
| Totale | 13.2% | 78.0% | 10.8% |

- Partite decise presto: chi è avanti nelle Vite all'inizio del round 7 (fine del round 6) vince **66.9%** (su 236 partite non in parità a quel punto).
- "Mano piena" = almeno 6 carte (il limite di mano è 8). "Nessuna carta giocabile" = nessuna azione «gioca» legale alla prima scelta (gemme insufficienti, nessun bersaglio, costo non pagabile).
- Minacce senza risposta: non si ricava dai log senza una definizione di minaccia; non misurata.

