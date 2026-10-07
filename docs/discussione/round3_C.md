# Round 3 — Ratifica dell'agente C

> **Verdetto: approvo il regolamento v0.1.** Il testo riporta fedelmente il dibattito, comprese le mie concessioni: §17 e "Respinti dal dibattito" registrano correttamente il ritiro di Fulcro, Clessidra a punti e requisiti d'Aspetto. Segnalo **due errori** (uno di coerenza interna, uno nell'analisi del punto d) e **un'incoerenza di valori**, che coincide con il punto aperto c.

---

## Approvazione per sezione

| § | Esito | Nota |
|---|---|---|
| 1 Panoramica | Approvo | |
| 2 Componenti | Approvo | Leader 3/5, Risvegliato 4/5, Guardia 2/3: corrisponde a quanto deciso. |
| 3 Zone | Approvo | |
| 4 Preparazione | Approvo | La V2 di default è registrata correttamente come variante. |
| 5 Risorse | Approvo | Guardia pubblica con tetto unico, come concordato. |
| 6 Turno | Approvo | Vedi l'errore 1 (riguarda §6.1 e §9.5). |
| 7 Tipi e stati | Approvo | |
| 8 Combattimento | Approvo | I 9 passi coincidono con la revisione; "l'attaccante non risponde mai" è presente. |
| 9 Vittoria | **Contesto un punto** | Errore 1. |
| 10 Leader | Approvo | Rimarginare ⟳ come deciso. |
| 11 Compensazione | Approvo | |
| 12 Colori e carte | **Contesto due valori** | Grido e Maera Base (vedi punto c). |
| 13 Leggi | Approvo | Le leggi 10 e 11 includono le mie due aggiunte. |
| 14–15 Glossario, parametri | Approvo | |
| 16 Varianti | Approvo, con una correzione | Errore 2 (leva Scudo). Le attribuzioni di V1-b e V2 a C sono corrette. |
| 17 Moduli | Approvo | |
| `pilastri_design.md` | Approvo | |
| `esito_dibattito.md` | Approvo | La mia posizione è riportata fedelmente in tutti e 6 i punti. |

### Errore 1 — Istantanea Alle Corde: due testi in conflitto
- §6.1, passo 2: l'istantanea si prende **dentro** il Ripristino, *dopo* l'incremento del numero di turno.
- §9.5: dice invece «istantanea §6.1, **presa prima del Ripristino**».

Non è un dettaglio. La condizione «Alle Corde a 1 Vita dal turno 13» dipende dal numero di turno già incrementato. Se l'istantanea venisse presa prima del Ripristino, il colpo finale del turno 13 non scatterebbe.
→ *Fix:* in §9.5 scrivere «presa al passo 2 del Ripristino (§6.1)». Lo stesso vale per la nota n. 22 del critico, che ora è superata.

### Errore 2 — La leva "Scudo con Forza ≤ costo" è violata anche da Sentinella
L'editor segnala solo il Bastione (5, F6). Ma anche **Sentinella del Guado (2, F3, Scudo)** viola la leva. La leva è formulata male, non le carte (vedi punto d).

---

## Voti sui 4 punti aperti

**a. Limite duro → "Ultima ora" dal turno 14.**

Regola proposta: all'inizio del tuo Ripristino, dal tuo turno 14:
- se il tuo Leader è Alle Corde, perdi la partita;
- altrimenti il tuo Leader perde 1 Vita, fuori dal Saldo.

Metrica collegata: meno del 2% di partite oltre il turno 15.

*Motivo:* chiude sempre sul tavolo, senza punti né patte, e interviene solo dopo che la Clessidra ha già aperto il finale. È il Crepuscolo di B, ma spostato dove serve solo da paracadute.

**b. Asimmetria della Clessidra → la Clessidra conta il numero di turno di G2 (i round completi).**

Con questa regola le soglie dei turni 10 e 13 scattano per entrambi i giocatori nello stesso round. Nel tardo gioco il primo ad averle diventa G2.

*Motivo:* toglie a G1 un vantaggio di mezzo round proprio nel momento in cui la partita si decide. Basta una parola, nessuna regola nuova, ed è misurabile con la metrica G1 48–52% dei turni lunghi.

**c. Grido dalla Cicatrice → 2 Guardia, −5 Forza (1 Guardia se giocato dalle Cicatrici).**

*Motivo:* il confronto a parità di costo torna a favore della carta:

| | Guardia | Effetto | Parata allo stesso costo |
|---|---|---|---|
| Grido dalla mano | 2 | −5 | +4 |
| Grido dalle Cicatrici | 1 | −5 | +2 |
| Muro di Scudi | 1 | +5 | +2 |

Grido resta allineato a Muro.

*Correzione collegata:* la Reazione Base di **Maera** (1 Guardia, −2) oggi è identica a una Parata da 1 Guardia e in più richiede che il Leader sia Pronto. Va portata a **−3**, altrimenti viola lo stesso principio.

**d. Bastione → si cambia la leva, non la carta: "Unità con Scudo hanno Forza ≤ costo + 1".**

*Motivo:* è compatibile con tutto il set attuale (Recluta 1≤2, Sentinella 3≤3, Bastione 6≤6). La leva serve comunque a impedire muri economici, mentre la formulazione attuale avrebbe invalidato due carte su tre del Blu.

---

**Firma di C:** ratifico il regolamento v0.1 con le due correzioni testuali qui sopra. Le correzioni sono di scrittura e di valori, e non cambiano nessuna decisione presa nel dibattito.
