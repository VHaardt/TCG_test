# Proposta C — FULCRO: economia di tempo e iniziativa

> Direzione: azioni alternate nel round, iniziativa contesa, economia ibrida (carta giocata **o** investita), vittoria in due fasi (Slancio → Colpo di Grazia) con clock visibile.
> Fonti di ispirazione: SWU (azioni alternate, iniziativa, risorse da qualsiasi carta), LoR (round condiviso, alternanza), FaB (pitch in fondo al mazzo), Sorcery (Death's Door), Riftbound (regola dell'ultimo punto), OPTCG (danno → carte), Lorcana (agire espone).

---

## 1. Pitch e meccanica firma

**Elevator pitch.**
1. Due condottieri si contendono il **Fulcro**: chi lo tiene agisce per primo, ed è l'unico che può sferrare il colpo che vince la partita.
2. Ogni carta è un'arma oppure un investimento; ogni azione è una mossa a scacchi alternata, mai un turno passato a guardare.
3. Accumuli **Slancio** colpendo, apri la **Breccia** e chiudi con il **Colpo di Grazia**, prima che la **Clessidra** finisca.

**La meccanica firma: "Il Passo del Fulcro".**
Iniziativa, crescita delle risorse e condizione di vittoria sono **una sola economia**, regolata da un unico gesto: *passare*.
- Si investe una carta in Riserva **solo nel momento in cui si passa** (non in una fase solitaria a inizio turno).
- Il giocatore che **non** detiene il Fulcro può prenderlo passando: smette di agire per il resto del round.
- Il Colpo di Grazia è possibile solo nel round che inizi **detenendo il Fulcro** con Slancio sufficiente.

Ogni round pone quindi la domanda centrale: *continuo ad agire, o mi fermo ora per prendere l'iniziativa e minacciare la vittoria?* Nessun gioco esistente fonde ordine di gioco, risorsa e finale in un'unica decisione (cfr. `ricerca_web.md` §2.5 punti 1–2).

---

## 2. Regole core v0.1

### 2.1 Componenti e mazzo
- **Condottiero** (fuori dal mazzo): ha 1 o 2 **Aspetti** e un'abilità passiva. È il bersaglio degli attacchi; non ha punti vita.
- **Mazzo**: esattamente **40 carte**, max **3 copie** per nome; solo carte degli Aspetti del Condottiero o **Neutrali**.
- **Quattro Aspetti**: Fiamma (F), Corrente (C), Radice (R), Ombra (O).
- **Segnalini**: tracciato Slancio (0–10) per giocatore; il **Fulcro** (1 gettone condiviso); la **Clessidra** (tracciato round 1–15).

### 2.2 Zone
Mazzo, Mano, **Fronte** (max 5 unità), **Riserva** (carte investite, **a faccia in su**), Scarti. Le sole informazioni nascoste sono mano e ordine del mazzo.

### 2.3 Preparazione
1. Si sceglie a caso chi riceve il Fulcro: chi lo detiene agirà per primo nel round 1.
2. Si pescano 6 carte; l'altro giocatore ne pesca **7**.
3. **Mulligan parziale**, una volta sola: si mettono in fondo al mazzo quante carte si vuole e se ne pescano altrettante.
4. Ognuno **investe 2 carte** dalla mano in Riserva.
5. Il giocatore senza Fulcro riceve la **Scintilla**: un gettone monouso che vale +1 energia in un pagamento.

### 2.4 Risorse (economia ibrida)
- **Energia**: ogni carta in Riserva si esaurisce per produrre 1 energia. All'inizio di ogni round la Riserva si prepara.
- **Requisito d'Aspetto**: un costo "3 FF" chiede 3 energia **e** almeno 2 carte di Fiamma in Riserva (presenti, non esaurite). Le carte Neutrali in Riserva danno energia ma nessun Aspetto.
- **Investire** (risorsa permanente, modello SWU/Lorcana): max **1 carta per round**, e solo **quando passi** (vedi 2.5). La carta va in Riserva esausta. Alcune carte hanno **Seme**: un effetto che si attiva quando vengono investite. Così l'investimento diventa una scelta tattica e non uno scarto del peggio.
- **Spinta** (risorsa temporanea, modello FaB): **una volta per round**, mentre paghi un costo, puoi mettere 1 carta dalla mano in fondo al mazzo per +1 energia. Serve a fare la giocata giusta un round prima, ma costa una carta.

### 2.5 Struttura del round
Partita = sequenza di **round**; in ogni round entrambi giocano, quindi **round = turno per giocatore**.

**A. Inizio round**
1. La Clessidra avanza.
2. Si prepara tutto (unità e Riserva).
3. Ognuno pesca 2 carte (nel round 1 non si pesca).
4. **Controllo Breccia**: se chi detiene il Fulcro ha Slancio ≥ **Soglia** (vedi 2.8), è **In Breccia** per tutto il round. Lo stato non cambia durante il round, anche se il Fulcro passa di mano.

**B. Fase d'azione.** Inizia chi detiene il Fulcro; poi si alterna **un'azione a testa**. Le azioni possibili sono:
- **Giocare** una carta pagandone il costo.
- **Attaccare** con un'unità pronta (vedi 2.7).
- **Attivare** un'abilità ⟳ (richiede di esaurire la fonte).
- **Passare**: puoi investire 1 carta, poi non agisci più in questo round.
- **Prendere il Fulcro**: solo per chi **non** lo detiene e una sola volta per round. Il Fulcro si sposta subito; è un Passo a tutti gli effetti, quindi puoi investire.

Chi ha passato **non è fuori dal gioco**: continua a bloccare e a giocare Riflessi nelle finestre di combattimento. L'altro giocatore prosegue con un'azione alla volta finché non passa. Il round termina quando entrambi hanno passato.

**C. Fine round**
1. Rimuovi i danni dalle unità.
2. Terminano gli effetti "fino a fine round".
3. Scarta fino a 8 carte in mano.

### 2.6 Tipi di carta
- **Unità**: Costo, Forza/Tenacia, **Impeto** (Slancio guadagnato quando colpisce il Condottiero; 1 se non indicato). Entra **Fresca**: non può attaccare in questo round.
- **Tattica**: effetto immediato, giocabile solo come azione.
- **Riflesso**: giocabile come azione **oppure** in una finestra di combattimento, anche dopo aver passato.
- **Reliquia**: permanente, max 2 in gioco per giocatore.

**Parole chiave base (6):**
- **Rapida**: ignora Fresca.
- **Sfuggente**: può essere bloccata solo da unità con Vedetta.
- **Vedetta**: può bloccare unità Sfuggenti.
- **Baluardo**: bloccare non la esaurisce.
- **Seme**: effetto all'investimento.
- **Rancore**: bonus attivo se l'avversario ha più Slancio di te.

### 2.7 Combattimento e finestre di reazione (nessuna pila)
1. **Dichiarazione**: esaurisci un'unità pronta non Fresca. Il bersaglio è il **Condottiero** avversario oppure un'**unità avversaria esausta** (agire espone, modello Lorcana).
2. **Blocco** (solo se il bersaglio è il Condottiero): il difensore può bloccare con 1 unità pronta, che si esaurisce (salvo Baluardo). Il blocco reindirizza il combattimento sul bloccante.
3. **Finestra Riflesso**: il difensore può giocare **1** Riflesso, poi l'attaccante può giocarne **1**. Ognuno si risolve subito e non ci sono risposte alle risposte.
4. **Danno**: i due combattenti si infliggono simultaneamente la propria Forza; un'unità muore se il danno subito è ≥ Tenacia.
5. **Colpo non bloccato al Condottiero**: l'attaccante guadagna Slancio pari all'Impeto. Se l'attaccante è **In Breccia**, vince invece la partita (**Colpo di Grazia**).

### 2.8 Vittoria in due fasi
- **Fase 1, Slancio**: si guadagna con colpi non bloccati e con effetti (rari). Il **tetto è 3 Slancio per round** per giocatore.
- **Fase 2, Breccia**: con Slancio ≥ Soglia, devi **iniziare un round detenendo il Fulcro**. Di solito questo significa averlo preso passando nel round precedente: la minaccia è **sempre telegrafata** con almeno mezzo round d'anticipo, e il difensore ha azioni libere per prepararsi.
- **Soglia sulla Clessidra**:

  | Round | 1–8 | 9–11 | 12–14 | 15 |
  |---|---|---|---|---|
  | Soglia | 7 | 6 | 5 | 4 |

- **Fine forzata**: se nessuno ha vinto alla fine del round 15, vince chi ha più Slancio. In caso di parità vince chi detiene il Fulcro (esito deterministico, mai patta).
- **Round 1**: non si possono attaccare i Condottieri.

### 2.9 Compensazione del primo giocatore
Chi agisce per primo nel round 1 ha il tempo; l'altro riceve:
- **+1 carta** nella mano iniziale;
- la **Scintilla**;
- la possibilità di **prendere il Fulcro già nel round 1**.

Il vantaggio non è assegnato una volta per tutte: si **paga** rinunciando ad azioni, round dopo round (lezione SWU in `ricerca_web.md` §2.4).

### 2.10 Anti-OTK
- Tetto di **3 Slancio per round**.
- Il Colpo di Grazia richiede Breccia, che si controlla **solo a inizio round**: è impossibile salire di Slancio e chiudere nello stesso round.
- Unità Fresche, nessun attacco ai Condottieri nel round 1.
- Max 5 unità sul Fronte, Spinta 1 per round, investimento 1 per round.
- Il difensore blocca anche dopo aver passato.

### 2.11 Anti-stallo e anti-hard-control
- **Clessidra**: la Soglia scende nel tempo e il round 15 chiude sempre la partita. È l'"inerzia" di Rosewater: lo stato neutro spinge verso la fine.
- Il Fulcro **non è difendibile**: chi lo detiene non può impedire che venga preso. Nessuno può negare per sempre la Breccia, al massimo ritardarla di un round pagando in azioni.
- **Leggi di design** (vincoli per chi crea le carte):
  - niente "annulla una carta giocata";
  - niente scarto forzato dalla mano;
  - niente distruzione della Riserva;
  - nessun effetto impedisce a un'unità di prepararsi per più di 1 round;
  - perdita di Slancio dell'avversario massimo 1 per carta, e mai sotto la Soglia meno 2.
- **Riscossa** (comeback strutturale e limitato): la prima volta in ogni round in cui l'avversario guadagna Slancio colpendo il tuo Condottiero, peschi 1 carta.

### 2.12 Mazzo esaurito
Se devi pescare da un mazzo vuoto, non peschi e l'avversario guadagna 1 Slancio per ogni carta mancata (fuori dal tetto). È raro: 40 carte, 2 pescate a round e la Spinta che rimette carte in fondo.

---

## 3. Perché le partite durano 5–15 turni

**Limite inferiore (5 round).** Il round 1 è senza attacchi ai Condottieri e il tetto è 3 Slancio per round:
- servono almeno 3 round di colpi per arrivare a 7 (rounds 2, 3, 4: 3+3+1);
- la Breccia può iniziare solo nel round successivo (round 5);
- serve inoltre aver preso il Fulcro passando nel round 4, cioè rinunciando a parte del round in cui si sale di Slancio.

Il caso migliore assoluto è quindi la vittoria nel **round 5**, e solo se il difensore non blocca mai. Questo è il requisito anti-OTK.

**Curva aggro realistica.** Ipotesi: l'energia cresce di circa 1 per round (2 nel round 1, circa 6 nel round 5); i 3 colpi non bloccati per round diventano in media 1,5–2, perché il difensore ha 1–3 bloccanti e la Riscossa gli dà carte.
- Si arriva a 7 nei **round 5–6**.
- Il difensore anticipa la Breccia prendendo lui il Fulcro, il che ritarda di 1 round.
- Primo Colpo di Grazia ai **round 6–8**, con la Breccia spesso respinta una volta.

**Midrange.** Scambi di unità e circa 1 Slancio per round dal round 3: 7 Slancio verso il round 9, dove la Soglia scende a 6. Chiusura nei **round 9–11**.

**Controllo.** Pochi colpi subiti, poi la vittoria con la Soglia a 5 (round 12) grazie a unità grandi con Impeto 2. Il round 15 è il tetto rigido: anche un controllo puro che non attacca mai **perde** ai punti contro chiunque abbia segnato almeno 1 Slancio, quindi deve vincere e non solo negare.

**Durata reale.** Le azioni alternate a grana fine evitano i tempi morti; si stimano 2–3 minuti per round, cioè **15–30 minuti** a partita.

---

## 4. Archetipi e carte d'esempio

Formato delle carte: **Nome**, poi costo con requisito d'Aspetto, tipo, Forza/Tenacia (Impeto se diverso da 1), testo. Gli Aspetti sono indicati con le lettere F (Fiamma), C (Corrente), R (Radice), O (Ombra).

### 4.1 Avanguardia (Fiamma, partner naturale: Corrente)
**Piano di gioco.** Unità economiche e Rapide fanno Slancio dal round 2 e forzano il difensore a bloccare tutto. A metà partita prende il Fulcro e minaccia una Breccia dopo l'altra.

**Combo tra archetipi:**
- con i rimbalzi di Corrente (Avanguardia-Risacca): toglie i bloccanti proprio nel round di Breccia;
- con Ombra: le unità Rancore puniscono chi corre più veloce.

**Carte:**
- **Staffetta di Brace** — 1 F — Unità 2/1 — Rapida. Non può attaccare unità.
- **Ariete Rovente** — 4 FF — Unità 4/3, Impeto 2 — Non può essere bloccata da unità con Forza 1 o meno.
- **Grido di Carica** — 2 F — Tattica — Le tue unità hanno +1 Forza fino a fine round. Se sei In Breccia, prepara anche un'unità esausta.

### 4.2 Risacca (Corrente, partner: Fiamma o Ombra)
**Piano di gioco.** È il mazzo "del Fulcro". Le sue carte premiano chi detiene l'iniziativa o chi la prende, e i suoi Riflessi economici rimbalzano attaccanti e bloccanti. Vince giocando sul tempo: costringe l'avversario a passare in momenti scomodi.

**Combo tra archetipi:**
- con Fiamma: tempo-aggro;
- con Ombra: un controllo morbido che chiude con la Soglia bassa.

**Carte:**
- **Navigatrice del Fulcro** — 2 C — Unità 1/3 — Quando prendi il Fulcro, pesca 1 carta.
- **Controcorrente** — 2 C — Riflesso — Riporta in mano al proprietario un'unità in combattimento di costo ≤3. Il combattimento termina senza danni.
- **Marea Montante** — 3 CC — Tattica — Esaurisci un'unità avversaria. Se detieni il Fulcro, quell'unità non si prepara all'inizio del prossimo round.

### 4.3 Radici (Radice, partner: Ombra o neutrali)
**Piano di gioco.** Trasforma l'investimento in un motore: le carte Seme danno valore anche quando vengono investite, e i Baluardi grandi tengono il Fronte. È più lenta e vince a metà o fine Clessidra con unità Impeto 2.

**Combo tra archetipi:**
- con Ombra: rimette in Riserva le unità morte, riattivando i Seme;
- con i neutrali Seme: aumenta la Riserva multi-Aspetto per **Raccolto Paziente**.

**Carte:**
- **Germoglio di Quercia** — 1 R — Unità 1/2 — Seme: una tua unità ottiene permanentemente +1/+1.
- **Antico Custode** — 5 RR — Unità 3/6, Impeto 2 — Baluardo. Costa 1 in meno se hai 7 o più carte in Riserva.
- **Raccolto Paziente** — 3 R — Tattica — Pesca 1 carta per ogni Aspetto diverso presente nella tua Riserva (max 3).

### 4.4 Spoglie (Ombra, partner: Radice o Corrente)
**Piano di gioco.** Sacrifici, effetti alla morte e **Rancore**: diventa più forte quando è indietro di Slancio, quindi incassa i primi colpi e poi ribalta. La Riscossa la alimenta naturalmente.

**Combo tra archetipi:**
- con Radice: il ciclo morte, Riserva, Seme;
- con Corrente: rimbalzo e sacrificio per generare valore.

**Carte:**
- **Spettro del Rancore** — 2 O — Unità 2/2 — Rancore: +1 Forza e Sfuggente.
- **Patto di Cenere** — 1 O — Riflesso — Distruggi una tua unità; infliggi danno pari alla sua Forza a un'unità avversaria.
- **Ritorno dalle Spoglie** — 3 OO — Tattica — Investi un'unità dai tuoi Scarti nella Riserva (fuori dal limite di 1 per round; il suo Seme si attiva). Pesca 1 carta.

### 4.5 Neutrali d'esempio
- **Cartografo Errante** — 2 — Unità 2/2 — Seme: pesca 1 carta. È il "connettore" di ogni mazzo: una buona giocata al round 2 e un buon investimento a fine partita.
- **Cambio di Vento** — 1 — Riflesso — Un'unità che blocca ottiene +0/+3 fino a fine round. Costa 0 se hai già passato in questo round. Premia la difesa dopo il Passo del Fulcro.

---

## 5. Autocritica: i 5 rischi principali e come testarli

1. **Degenerazione del Passo del Fulcro.** Prendere il Fulcro potrebbe essere sempre giusto alla prima azione (troppo economico) o mai prima di avere Slancio pari alla Soglia (irrilevante).
   - *Test*: nel simulatore, IA con politiche diverse (prende subito, prende tardi, euristica sullo Slancio). Si misurano la distribuzione del momento in cui il Fulcro viene preso e il tasso di vittoria per politica.
   - *Correttivo*: sostituire il "passa e basta" con un costo dosabile, per esempio "Prendi il Fulcro dopo almeno 1 azione".

2. **Vantaggio del primo giocatore.** Agire per primi in un gioco ad azioni alternate premia il tempo (i dati HS mostrano oltre 10 punti per i mazzi tempo).
   - *Test*: 10.000 partite IA contro IA, per matchup e archetipo.
   - *Obiettivo*: tasso di vittoria di chi detiene il Fulcro nel round 1 tra 49% e 52%.
   - *Leve*: carta extra, Scintilla, 2 o 3 carte investite in partenza per il secondo.

3. **Muri di Baluardo: la Breccia non entra mai** e le partite finiscono troppo spesso ai punti al round 15.
   - *Test*: percentuale di partite che arrivano alla fine forzata (obiettivo sotto il 10%) e numero medio di Brecce respinte per partita.
   - *Correttivi*: dalla Soglia 5 in giù, anche il danno in eccesso del bloccato conta come Colpo; oppure un limite di 2 Baluardi sul Fronte.

4. **Il problema di Sam Black che rientra dalla finestra.** Se investire a ogni Passo diventa automatico ("investo sempre la peggiore"), la decisione torna solitaria.
   - *Test*: percentuale di round in cui si investe, varietà delle carte investite e quanto spesso un'IA "intelligente" batte un'IA che "investe a caso".
   - *Correttivi*: più Seme e più carte che premiano una Riserva piccola o una mano piena.

5. **Carico cognitivo e ramificazione per l'IA.** Le due fasi di vittoria, la Clessidra, gli Aspetti e il momento del Passo possono essere troppo per un neofita. Le azioni alternate fanno inoltre esplodere l'albero di ricerca.
   - *Test*:
     - tempo di apprendimento in playtest con 6 giocatori nuovi (obiettivo: una partita completa in 20 minuti dopo 5 minuti di spiegazione);
     - per l'IA, MCTS con potatura sulle azioni "passa/attacca/gioca" e misura della differenza tra IA con budget basso e alto (se è alta, c'è profondità reale; se è nulla, il gioco è risolto o caotico).

**Altri rischi da monitorare:**
- la pericolosità di **Marea Montante** e di **Controcorrente** nel round di Breccia (tempo a due vie);
- il tetto di 5 unità che potrebbe congelare il Fronte;
- la parità della fine forzata decisa dal Fulcro, che va verificata come incentivo a prenderlo al round 15.
