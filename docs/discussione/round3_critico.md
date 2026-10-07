# Round 3: ratifica del critico e playtester

**Voto complessivo: APPROVO il regolamento v0.1 condiviso**, con 4 correzioni di scrittura e 7 ambiguità residue da chiudere prima di scrivere il codice. `esito_dibattito.md` riporta fedelmente le mie posizioni, comprese quelle in cui sono finito in minoranza (Risveglio al turno 7, 3–1).

## 1. Sezione per sezione

| § | Esito | Nota |
|---|---|---|
| 1–3 | Approvo | |
| 4 Preparazione | Approvo | |
| 5 Risorse | Approvo | "si alza **solo il tetto**: non si ottiene Guardia" chiude il mio caso 13. |
| 6 Turno | **Contesto la forma** | §6.1 colloca l'istantanea "Alle Corde" al passo 2 *del* Ripristino, dopo l'aumento del numero di turno. §9.5 invece dice "presa **prima** del Ripristino". Oggi le due versioni danno lo stesso risultato, ma il programmatore ne deve scegliere una. **Fix**: in §9.5 scrivere "istantanea del §6.1, passo 2". |
| 7 Stati e controlli | Approvo | |
| 8 Combattimento | Approvo, con 2 correzioni | Ambiguità A2 e A3 sotto. |
| 9 Vittoria e anti-stallo | **Contesto** | "La terminazione è comunque garantita dal mazzo vuoto" è vero, ma solo verso il turno 31–36, contro il vincolo 5–15. Vedi il punto a. |
| 10 Leader | Approvo | "o attacca o Rimargina" è esattamente il dilemma voluto. |
| 11 Primo giocatore | Approvo | |
| 12 Carte | Contesto Vesh, Grido, Bastione | A1 sotto; punti c e d. |
| 13–17 | Approvo | Le varianti V1 e V2, i test T1–T4 e il protocollo sequenziale rispecchiano il dibattito. |

## 2. Ambiguità residue (per il programmatore)

**A1. Vesh e i bonus extra.**
"bonus di Forza e contatore si spostano": non dice se si spostano anche i +1 *aggiuntivi* di Arden Base e dell'Infuso di Scudiera.
- **Fix**: si sposta solo +1 Forza per ogni Brace del contatore. I bonus extra restano dove sono e scadono normalmente.

**A2. Trigger di un'Unità sconfitta nello stesso combattimento.**
Bastione pareggia con un attaccante F6: muoiono entrambi. "Quando sconfigge" scatta lo stesso?
- **Fix**: regola generale "i trigger del passo 9 guardano indietro". Scattano anche se la loro fonte è stata sconfitta in quel combattimento; Bastione quindi pesca.

**A3. Ultimo respiro a metà turno.**
"se, all'apertura di questa finestra, il suo Leader è Alle Corde": un Leader portato a 0 dal primo attacco ottiene 2 reazioni per il resto del turno, utili solo per proteggere le Unità. È un comportamento non voluto e dipende dall'ordine degli attacchi.
- **Fix**: Ultimo respiro si legge dall'**istantanea** del §6.1, come il colpo finale.

**A4. Alle Corde a 1 Vita dipende dal giocatore attivo.**
Lo stesso Leader con 1 Vita è Alle Corde nel turno 13 di G1, ma non nel turno 12 di G2. Ultimo respiro, colpo finale e la tabella di §9.1 cambiano quindi da un mezzo turno all'altro.
- È coerente, ma va scritto in modo esplicito: "Alle Corde si valuta sempre con il numero di turno del giocatore attivo in quel momento".
- Va aggiunto un esempio, altrimenti il simulatore lo tratterà come uno stato persistente.

**A5. Matriarca in difesa.**
"quando una tua Unità sconfigge un'Unità Esposta": un intercettore che sconfigge l'attaccante (Esposto) nel turno avversario fa pescare.
- Va bene, ma va confermato. **Fix**: "in qualsiasi turno".

**A6. Maera Risvegliata con Parata ×3.**
Con 3 Guardia si arriva a Tempra 14: un attacco per turno diventa impossibile da passare, e con Ultimo respiro gli attacchi bloccati sono due.
- Non è un errore, ma è un picco da segnalare nel simulatore. **Leva**: "+1 Forza per Guardia in più" al posto di "+3 per Guardia".

**A7. Rimarginare più volte nello stesso turno.**
Oggi il limite di "1 per turno" esiste solo perché si usa con ⟳. Un futuro effetto che rende Pronto il Leader permetterebbe di Rimarginare più volte.
- **Fix**: scrivere "massimo 1 volta per turno" nel testo di §10.2.

## 3. Voto sui punti aperti

**a. Limite duro.**
**Voto: Crepuscolo di riserva dal turno 15 del giocatore attivo**: nel Ripristino il tuo Leader perde 1 Vita, ignorando il Saldo; se all'inizio del Ripristino è già Alle Corde, perdi.
- *Motivo:* garantisce la fine verso il turno 15–20 senza punti né patte. Riprende il Crepuscolo di B nel solo ruolo che nessuno ha contestato, quello di paracadute.

**b. Asimmetria della Clessidra.**
**Voto: nessuna compensazione ora.** Si misura la percentuale di vittorie di G1 nelle sole partite che arrivano al turno 10. Leva di riserva: le soglie si leggono sul numero di turno di **G2**.
- *Motivo:* le partite oltre il turno 10 devono essere sotto il 15%. Inoltre il Crepuscolo del punto a colpisce per primo proprio G1, e le due asimmetrie si bilanciano.

**c. Grido contro Parata.**
**Voto: Grido costa 1 Guardia, −3 dalla mano, −5 dalle Cicatrici.**
- *Motivo:* è migliore della Parata a parità di Guardia (−3 contro +2). Dalle Cicatrici vale quanto Muro (5 per 1 Guardia), e il bonus Nero "ferite come potere" resta. Costa almeno 1 Guardia, quindi è compatibile anche con V1-b.

**d. Bastione contro la leva "Scudo con Forza ≤ costo".**
**Voto: cambiare la carta in costo 5, F5, Scudo** (testo invariato) e tenere la leva.
- *Motivo:* il pezzo più forte di un muro non può essere l'eccezione alla leva anti-muro. Con F5 sconfigge ancora ogni Unità da 4 e l'intercetto più Parata (F7–9) resta temibile.
