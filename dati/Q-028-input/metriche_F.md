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


## Misure aggiuntive per l'analista (dagli stessi 300 log, nessuna partita nuova)

**Come sono calcolate:** script `script/metriche_f_extra.py`; definizioni e approssimazioni sono in testa allo script.

### 1. Scontri senza possibilità
Un attacco è senza possibilità quando l'attaccante, mettendo tutte le gemme che gli restano, non arriva nemmeno a pareggiare la difesa con 0 gemme di Parata.
Gli scontri con una Reazione restano fuori dal conto.

| Leader (difende) | Scontri difesi | Senza possibilità | Reazioni per scontro difeso | … senza quelli | Unità ferme (M6) | … contando ferme le Unità che attaccano senza possibilità |
|---|---|---|---|---|---|---|
| LDR01 | 1290 | 58 (4.5%) | 0.062 | 0.065 | 52.5% | 54.3% |
| LDR02 | 1541 | 92 (6.0%) | 0.066 | 0.070 | 47.4% | 47.7% |
| LDR03 | 1043 | 72 (6.9%) | 0.078 | 0.083 | 51.7% | 52.2% |
| LDR04 | 1339 | 26 (1.9%) | 0.081 | 0.083 | 53.4% | 54.9% |
| LDR05 | 1289 | 48 (3.7%) | 0.114 | 0.118 | 54.6% | 55.4% |
| LDR06 | 1161 | 62 (5.3%) | 0.065 | 0.069 | 46.9% | 50.4% |
| Totale | 7663 | 358 (4.7%) | 0.078 | 0.081 | 51.5% | 52.9% |

Le ultime due colonne sono le Unità ferme dell'attaccante: la riga di un Leader conta le sue Unità e i suoi attacchi senza possibilità. Nell'ultima colonna un'Unità che attacca senza possibilità conta come ferma (limite superiore).
Attacchi senza possibilità per Leader attaccante: LDR01 50 (di Unità 47), LDR02 7 (di Unità 5), LDR03 17 (di Unità 14), LDR04 169 (di Unità 40), LDR05 32 (di Unità 24), LDR06 83 (di Unità 79).

### 2. Round in cui la partita è decisa
Il motore non dà una stima di vittoria. Uso la regola di riserva: il round da cui il vincitore resta avanti nelle Vite (strettamente) fino alla fine, misurato a ogni inizio di turno.

- Media **10.0**, mediana 10.0, su 300 partite con un vincitore.
- Decise entro il round 6: 23.7%. Dal round 10 in poi: 56.3%.
- Distribuzione: R2: 3, R3: 21, R4: 18, R5: 9, R6: 20, R7: 23, R8: 18, R9: 19, R10: 23, R11: 24, R12: 20, R13: 20, R14: 24, R15: 37, R16: 18, R17: 3.

### 3. Turni vuoti nei round 1–3 (nessuna carta, attacco, Rimarginare o ⟳)

| Leader | Turni R1–3 | Vuoti |
|---|---|---|
| LDR01 | 300 | 16.3% |
| LDR02 | 300 | 36.3% |
| LDR03 | 300 | 17.7% |
| LDR04 | 300 | 24.0% |
| LDR05 | 300 | 21.3% |
| LDR06 | 300 | 28.3% |
| Totale | 1800 | 24.0% |

### 4. A 0 Vite senza esito
Caso contato: un giocatore inizia un turno con 0 Vite mentre l'altro ne ha almeno 1. Si conta la prima volta in cui succede.

- Partite con questo caso: **244 su 300** (81.3%).
- Round che restano dopo: media **1.6**, mediana 1.0; distribuzione 0: 78, 1: 89, 2: 27, 3: 14, 4: 8, 5: 10, 6: 9, 7: 4, 8: 5.
- Il giocatore a 0 Vite ribalta e vince: **42** (17.2%).

**Note:**
- **Controllo delle gemme:** le gemme ricostruite dal log non vanno mai sotto zero nei 7.663 scontri, quindi le spese della fase principale sono tutte contate.
- **Round 16–17:** il valore "R16–R17" del punto 2 vuol dire che il vincitore non era mai avanti all'inizio dell'ultimo turno. Sono le partite decise all'ultimo colpo o al Crepuscolo.
- **Vite a 0:** "0 Vite" non è ancora la sconfitta: perde chi a 0 Vite subisce un colpo finale. Il 26% dei casi (78) si chiude nello stesso round.
