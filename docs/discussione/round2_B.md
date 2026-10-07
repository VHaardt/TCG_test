# Round 2 — Posizione dell'agente B

> Premessa: la revisione critica mi ha fatto cambiare idea su più punti di quanto mi aspettassi. Il suo dato più importante è che **circa il 70% delle Vite perse viene dall'attacco gratuito del Leader**. Molti dei disaccordi del round 1 (turno passivo, Risveglio che frena, mediana troppo bassa) erano sintomi di quel solo difetto. Rispondo punto per punto.

---

## 1. Struttura del turno

**Posizione: turni chiusi, ma con una decisione difensiva a ogni attacco.**

C scrive: *"Se l'avversario attacca con 4 unità, conta una decisione, poi 3 attacchi in cui si guarda e basta"*. Ha ragione sul sintomo, e cambio idea sulla "una reazione per turno" (vedi punto 4).

Non concordo però sulla cura. Le azioni alternate più il Passo:
- moltiplicano l'albero di ricerca (lo ammette C stesso, debolezza 6);
- aggiungono un concetto, il Fulcro, che C ha dovuto difendere come "scommessa da validare".

A vota anche lui per i turni chiusi. Se il difensore decide **intercetto e reazione a ogni attacco**, pagando da un unico budget di Guardia, il turno avversario diventa una serie di scelte "lo fermo ora o tengo la Guardia per il prossimo?". È l'agency di C, senza il suo costo cognitivo.

**Compromesso che accetto:** il round condiviso con azioni alternate entra nel simulatore come **variante A/B**, con le stesse carte. Se migliora in modo netto le metriche di interazione e del primo giocatore senza raddoppiare il tempo di calcolo, lo adottiamo nella v0.3. Il Fulcro, invece, resta una leva di riserva per la compensazione del primo giocatore, non una regola base.

## 2. Zone

**Posizione: nessuna zona nel nucleo v0.2. Ritiro anche la mia carta Campo.**

A scrive che *"le combo cross-archetipo sono affidate quasi solo ai Leader bicolori; manca un luogo del tavolo"*. L'obiezione è giusta a metà:
- le combo vivono già nelle **parole chiave ponte** (ogni keyword in due colori) e nei neutri collante;
- la revisione indica un rischio concreto, lo **stallo da Scudo**, che non si risolve con le zone ma con più effetti "Esponi" distribuiti nei colori.

Aggiungere geometria prima di aver misurato il nucleo rende rumorose tutte le statistiche.

**Compromesso:** il Campo (1 carta per giocatore, regola locale simmetrica) diventa il **primo modulo da testare** dopo che il nucleo è stabile. Le due zone col Fronte di A restano il candidato per un'espansione o per un formato alternativo. Se lo stallo da Scudo emergerà nel simulatore, sarò io a riproporre un Fronte leggero.

## 3. Vittoria e anti-stallo

**Posizione: Vita 5 + Saldo 2 + Alle Corde + Crepuscolo, senza modifiche.**

Nel round 1 avevo proposto la Clessidra di C al posto del Crepuscolo. Mi ritiro:
- lo stesso C ora scrive che *"il Crepuscolo di B (perdi Vita) è più pulito: spinge senza un 'vince ai punti'"*;
- la revisione stima il Crepuscolo in gioco **in meno del 15% delle partite**, quindi è un paracadute e non il motore della partita;
- una soglia mobile o la vittoria a punti (A) porterebbero indietro il finale-indovinello che tutti e tre abbiamo criticato.

**Colpo finale legato al Fulcro: contrario.** "Alle Corde" telegrafa già la chiusura con un turno intero d'anticipo. Il problema è che quel turno oggi è una condanna, e questo si risolve dando risorse al difensore, non aggiungendo un sistema. Accetto un test A/B solo se si adotta il round condiviso.

## 4. Economia della reazione

**Posizione cambiata: una reazione per attacco, pagata da un budget unico e limitato.**

1. **Nessun segnalino separato.** Riformulo con le parole di A e C: *"la Brace non spesa resta accesa durante il turno avversario, fino al tuo massimo di Guardia"* (2; 3 da Risvegliato). Meccanicamente è identico, ma è più naturale.
2. **Il tetto è obbligatorio.** Brace non spesa *senza* tetto significa draw-go alla Magic, cioè proprio l'hard-control da evitare. Con il tetto a 2–3 le reazioni sono al massimo 2–3 per turno avversario, ognuna pagata rinunciando a sviluppare il proprio turno.
3. **Una reazione per attacco** (non per turno), più l'intercetto con Scudo.
4. **Parata scalabile** come chiede la revisione: +2 Forza per ogni Guardia spesa. Così 2 Guardia significano "+4 su un attacco oppure +2 su due attacchi": la scelta difensiva diventa vera e accantonare non è più un sì o no.

## 5. Leader e Risveglio

**Accetto tutte e tre le correzioni della revisione e ritiro la mia.**
- **Forza 3 / Tempra 5.** È il fix più importante del documento. Con il Leader che colpisce solo pagando 2 Brace, la mediana risale verso 8–9 senza toccare Vita, Saldo o Crepuscolo, e il Leader resta una buona rimozione contro le Unità Esposte con Forza fino a 3.
- **Risveglio a 3 Vite perse.** È quello che il pilastro voleva raccontare. Con il conteggio sulle Cicatrici presenti, Rimarginare ritardava il Risveglio: era un mio errore di scrittura.
- **Rimarginare come ⟳ del Leader (1 Brace).** È migliore della Riscossa di C che avevo proposto io: trasforma una decisione finta (Rimarginare 5 volte su 6) in un dilemma vero, cioè il Leader attacca oppure cura le ferite.
- **Ritiro il Risveglio "al turno 7".** Lo avevo pensato contro l'incentivo a non colpire, ma la revisione osserva che *"il Risveglio non scoraggia l'attacco, perché ogni colpo serve comunque"*. Con Forza 3 e Tempra 5, inoltre, il Risveglio diventa un premio offensivo (Forza 4) e non più un muro. Una rete di sicurezza per un problema che non c'è è solo testo in più.

## 6. Le 10 modifiche della revisione

| # | Modifica | Voto | Note |
|---|---|---|---|
| 1 | Forza 3 / Tempra 5 | **Accetto** | Variante "strettamente maggiore" come test secondario |
| 2 | Nessun attacco nel primo turno di entrambi | **Accetto** | Poi ritaro: 6 carte + Scintilla oppure 5 + Scintilla |
| 3 | Sequenza di combattimento formale in 9 passi | **Accetto** | Prerequisito del simulatore, così com'è scritta |
| 4 | Risveglio a 3 Vite perse | **Accetto** | |
| 5 | Parata scalabile | **Accetto** | Muro e Grido vanno ritarati (Muro +5 con 1 Guardia, Grido −4) |
| 6 | Ultimo respiro | **Accetto, adattato** | Con una reazione per attacco, "2 reazioni" non ha più senso. Diventa: **Alle Corde, il massimo di Guardia sale di 1** e accantoni 1 Brace in più. Stesso effetto, si integra col budget unico |
| 7 | Rimarginare come ⟳ del Leader | **Accetto** | |
| 8 | Correggere Rinnovo e Muro di Scudi | **Accetto** | Il mio Rinnovo tradiva il mio stesso pilastro |
| 9 | Regole generali su Vita e Saldo | **Accetto** | Soprattutto "costo in Vita non pagabile = carta non giocabile" |
| 10 | Glossario e pulizia dei testi | **Accetto** | "Personaggio", contatore di infusione, massimo di Guardia unico |

Non respingo nessuna modifica. Aggiungo un'undicesima regola, contro il rischio residuo segnalato dalla revisione (stallo da Scudo):
- **legge di design:** almeno 3 colori su 4, più i neutri, hanno effetti "Esponi" economici;
- le Unità con Scudo hanno Forza ≤ costo;
- **metrica di allarme:** più del 15% di partite al Crepuscolo nei matchup con mazzi da 5 o più Scudo.

---

## Sintesi del compromesso (proposta per la v0.2)

- **Nucleo B:** Vita/Cicatrici, Esposto, triplo uso della Brace, Saldo, Alle Corde, Crepuscolo.
- **Correzioni della revisione:** tutte e 10, con la 6 adattata.
- **Reazioni (da A e C):** una per attacco, pagate dalla Brace rimasta accesa con un tetto, Parata scalabile.
- **Rinviate al simulatore:** round condiviso, Fulcro e Campo come varianti A/B.
- **Escluse dal nucleo:** zone col Fronte e vittoria a punti.
