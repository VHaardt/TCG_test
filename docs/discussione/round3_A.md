# Round 3 — Ratifica dell'agente A

## 1. Approvazione per sezione

| § | Esito | Nota |
|---|---|---|
| 1–4 Panoramica, componenti, zone, preparazione | **Approvo** | |
| 5 Risorse | **Approvo** | Il tetto unico di Guardia e la Parata scalabile riportano fedelmente il round 2. |
| 6 Struttura del turno | **Approvo** | |
| 7 Tipi, stati, controlli di stato | **Approvo** | Corretta l'estensione della regola "perde il giocatore attivo" a ogni simultaneità (mia aggiunta). |
| 8 Combattimento in 9 passi | **Approvo** | |
| 9 Vita, vittoria, Clessidra | **Contesto due punti** (vedi sotto) | |
| 10–11 Leader, primo giocatore | **Approvo** | |
| 12 Colori e carte | **Approvo con riserva** | Su Grido e Bastione vedi i punti c e d. |
| 13 Leggi di design | **Approvo** | La legge 1 ("Nessuna carta annulla un'altra carta o vieta di giocare") è quella che chiedevo. |
| 14–15 Glossario, parametri | **Approvo** | |
| 16 Varianti e protocollo | **Approvo** | Il §16.3 rispecchia la mia proposta di introdurre le modifiche in sequenza. |
| 17 Moduli | **Approvo** | Ho perso 3–1 sul Campo nel nucleo e lo accetto. Le regole del Campo sono riportate correttamente. |
| `pilastri_design.md`, `esito_dibattito.md` | **Approvo** | Le mie posizioni e le mie concessioni sono registrate in modo esatto. |

### Contestazioni (errori, non tradimenti)

**1. Incoerenza sul momento dell'istantanea Alle Corde.**
- Il §9.5 dice: "istantanea §6.1, presa **prima del Ripristino**".
- Il §6.1 la colloca al **passo 2 del Ripristino**, cioè *dopo* l'incremento del numero di turno.

La differenza conta per la Clessidra. Se l'istantanea si prende prima dell'incremento, al turno 13 il numero letto è ancora 12, quindi un Leader a 1 Vita non risulta Alle Corde. Il simulatore riceverebbe due regole diverse.

*Fix:* nel §9.5 scrivere "istantanea presa al passo 2 del Ripristino (§6.1), dopo l'aggiornamento del numero di turno e prima di ogni altro effetto". Vale come definizione unica.

**2. Il §9.6 afferma che "la terminazione è comunque garantita dal mazzo vuoto".** È formalmente vero, ma il mazzo vuoto arriva intorno al turno 30, il doppio del vincolo dell'utente (5–15 turni). Il testo presenta come garanzia ciò che non rispetta il requisito. Si risolve con il punto a.

## 2. Voti sui 4 punti aperti

**a. Limite duro → "Crepuscolo terminale" come terzo gradino della Clessidra.**
Regola proposta: dal turno 15 del giocatore attivo, al passo 2 del suo Ripristino, se il suo Leader è Alle Corde quel giocatore **perde la partita**; altrimenti il suo Leader perde 2 Vite (soggette al Saldo).
- Nel caso peggiore, un Leader a Vita piena chiude entro il turno 17.
- Usa un meccanismo già testato (Crepuscolo, test T2): niente punti, niente patte.
- Spinge in modo simmetrico entrambi i giocatori.
- Il limite tecnico del §16.5 resta come rete per il simulatore.

*Motivo:* è l'unica opzione che garantisce la fine vicino al turno 15 senza reintrodurre le vittorie ai punti, respinte 4–0.

**b. Asimmetria della Clessidra → nessuna compensazione ora; misurarla.**
Nel simulatore va registrato il win rate di G1 **solo nelle partite che arrivano al turno 10**. Se supera il 52%, le soglie della Clessidra si leggono sul numero di turno di G2 (un "round" condiviso), ma solo con i dati in mano.

*Motivo:* anticipare di mezzo round le soglie è lo stesso vantaggio di tempo che V2 già misura; aggiungere una regola senza dati viola il protocollo §16.3.

**c. Grido → Grido dalla Cicatrice: 1 Guardia, −4 Forza; se la giochi dalle Cicatrici, −6.**

*Motivo:* dalla mano diventa migliore della Parata a pari Guardia, ma resta sotto Muro (+5, la difesa è del Blu). Dalle Cicatrici premia l'identità del Nero senza scendere a 0 Guardia, che svuoterebbe l'accantonamento.

**d. Bastione → cambiare la carta, non la leva: Il Bastione Vivente diventa 5 · F5 · Scudo.**

*Motivo:* una leva di riserva deve poter scattare senza errata. Inoltre Forza 6 con Scudo a costo 5 è proprio il prototipo dello stallo da Scudo che vogliamo misurare, non un'eccezione da proteggere.

## Verdetto
**Ratifico il regolamento v0.1** con le due correzioni del §9 e con le soluzioni a–d sopra. Nessuna sezione tradisce il dibattito.
