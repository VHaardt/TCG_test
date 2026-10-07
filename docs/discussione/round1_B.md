# Round 1 — Posizione dell'agente B (Cicatrici)

> Valuto A (Crocevia) e C (Fulcro) rispetto agli obiettivi dell'utente: gioco intuitivo ma profondo, archetipi flessibili con combo tra archetipi, 1v1, partite da 5 a 15 turni, niente OTK, niente hard-control, regole simulabili. Poi critico B senza sconti.

---

## 1. Critica di A e C

### A · Crocevia (zone)

**Punti forti**
- L'**inerzia** (max 1 casella per Fronte per turno) è l'anti-OTK più elegante dei tre: è visibile sul tavolo e non serve una regola d'eccezione.
- La vittoria a Gloria è **positiva** (si costruisce, non si toglie): permette archetipi molto diversi.
- Il "principio vincolante" (nessuna carta annulla un'altra carta) è il migliore dei tre: va adottato in qualunque base vinca.
- Lo sfondato che sceglie la nuova zona è un comeback guadagnato, non regalato.

**Punti deboli**
- **Peso cognitivo e computazionale.** Tre zone × 4 slot × Manovra × Comandare × Ingaggio × due finestre di reazione: è il sistema meno simulabile e meno intuitivo. Lo ammette anche la tabella del coordinatore ("bassa" facilità per l'IA).
- **La Verifica è una somma di Forze.** Esattamente la critica fatta ad Altered ("vince il numero più alto"). L'Ingaggio esaurisce *entrambi* i lati della presenza, quindi chi è avanti di Forza presidia e basta. Rischio concreto: Ingaggi rari e un gioco "a contabilità".
- **Il Leader perde peso.** Se viene sconfitto non dà Gloria e torna in Retrovia: è una pedina potenziata. Va contro la richiesta di un Leader-identità.
- **Durata alta.** Vittoria più rapida al turno 7 anche contro un avversario inerte. Il limite duro al round 15 con spareggio a Gloria, poi a posizioni, poi **patta**, è il finale-indovinello di Snap che la ricerca chiede di evitare.
- **Dottrina come decisione solitaria.** È lo stesso problema dell'"inchiostro" di Lorcana, segnalato dallo stesso autore.

### C · Fulcro (iniziativa)

**Punti forti**
- È il più **nuovo**.
- È l'unico che risolve davvero il turno avversario passivo: le azioni sono alternate e si blocca anche dopo aver passato.
- Unire il passaggio del turno, l'investimento di risorse e la minaccia di vittoria in un solo gesto ("passare") è un'idea da tenere.
- La Breccia annunciata con anticipo è un ottimo anti-OTK, gemello del mio "Alle Corde".
- La Riscossa è un comeback pulito.

**Punti deboli**
- **Troppi sistemi.** Slancio, Soglia variabile, Clessidra, Fulcro, Breccia, Riserva, requisiti d'Aspetto, Spinta, Seme. Sono nove concetti prima della prima carta: viola "rimuovere complessità, non profondità".
- **I requisiti d'Aspetto ("3 FF") reintroducono lo screw di colore.** L'anti-pattern n.1 rientra dalla porta di servizio: la Riserva dipende da quali carte hai pescato e investito.
- **La finestra Riflesso è per combattimento, non per turno**, e anche l'attaccante può rispondere. Con 3–4 attacchi per round sono 6–8 risposte potenziali: di fatto una mini-pila. Crea anche la "tassa da hand trap": vince chi ha il Riflesso giusto.
- **Rischio di hard-control.** *Marea Montante* ("non si prepara al prossimo round") e *Controcorrente* nel round di Breccia sono lock morbidi sul tempo.
- **Ramificazione per l'IA.** Le azioni alternate a grana fine moltiplicano l'albero di ricerca; il momento del Passo è una decisione molto lunga da valutare per un MCTS.
- **La vittoria ai punti al round 15** decisa da chi detiene il Fulcro rischia lo stesso finale-indovinello di A.

---

## 2. Debolezze oneste di B che A e C evitano

1. **Novità media.** B è "One Piece ben aggiustato". Infondere Brace per +1 Forza è il DON!! con un altro nome. A e C hanno un'identità più forte.
2. **Un solo asse di vittoria** (colpire il Leader). Gli archetipi differiscono solo nel *modo* di fare Forza o di negarla. A (zone) e C (tempo/iniziativa) offrono più dimensioni strategiche.
3. **Il turno avversario è più povero di C.** Un intercetto e una reazione sono meglio di Lorcana, ma C dà un'agency continua.
4. **Il Risveglio può scoraggiare l'attacco.** È il mio rischio n.1: un comeback che fa esitare chi è avanti genera stalli. Né A (Ascesa via Dottrina) né C hanno questo difetto.
5. **Il confronto a statistica singola** contro il Leader è binario: o colpisci o non succede nulla. Ha la stessa piattezza "numero più alto" che rimprovero ad A.
6. **Rimarginare rischia di diventare automatico** (ogni turno, 1 Brace, sempre).

---

## 3. Cosa ruberei e cosa concedo

**Da A**
- Il **principio "nessuna negazione"** come legge di design scritta.
- Il **campo variabile in versione minima**: una carta Campo per giocatore con una regola locale simmetrica. Dà varietà tra le partite senza il costo di tre corsie.
- L'**Ascesa a tempo** come rete di sicurezza (vedi la regola ibrida 4).

**Da C**
- La **Riscossa** come sostituto più leggero di Rimarginare: la prima volta per turno in cui perdi Vita, peschi gratis dalle Cicatrici. Elimina la decisione finta "spendo sempre 1 Brace".
- La **soglia decrescente nel tempo** al posto del Crepuscolo che toglie Vita a entrambi. Il mio Crepuscolo è un martello; la Clessidra di C è un'inerzia che *apre* il finale invece di punire.
- Le **leggi di design** di C (niente scarto forzato, nessun "non si prepara" per più di 1 round).

**Concedo da B**
- Il Risveglio solo da danno (va legato anche al tempo).
- Il nome e la forma OPTCG di "Infondere" (meglio un tetto: +2 per unità).
- Il Crepuscolo distruttivo.

---

## 4. Base preferita: **B+ (Cicatrici con innesti di A e C)**

1. **Leader** sempre in gioco, Vita 5. Ogni Vita persa diventa una **Cicatrice** pubblica. Le Reazioni si possono giocare dalle Cicatrici. La parola chiave **Furia N** conta le Cicatrici.
2. **Riscossa** (da C): la prima volta in ogni turno in cui perdi Vita, metti in mano una Cicatrice a tua scelta. Non ci sono altri recuperi in mano.
3. **Fornace** +1 per turno, massimo 8. Ogni Brace si **spende**, si **infonde** (+1 Forza, massimo +2 per unità) o si **accantona** come Guardia (massimo 2).
4. **Risveglio** del Leader alla 3ª Cicatrice **oppure** all'inizio del tuo 7° turno, se arriva prima (da A, Ascesa garantita). Ritardare i colpi non serve più a niente: risolve il mio rischio n.1.
5. **Esposizione**: chi attacca, intercetta o usa ⟳ è attaccabile fino al suo Ripristino. La rimozione economica colpisce solo bersagli Esposti.
6. **Una sola reazione per turno avversario** (Parata con Guardia, una carta Reazione o la Reazione del Leader), più l'intercetto con Scudo. **Nessuna carta annulla altre carte** (da A).
7. **Anti-OTK**: un Leader perde al massimo 2 Vite per turno (Saldo). Il colpo finale vale solo su un Leader che era a 0 Vita a inizio turno ("Alle Corde", gemello della Breccia di C).
8. **Clessidra** (da C) al posto del Crepuscolo: dal turno 10 il Saldo sale a 3; dal turno 13 il colpo finale vale anche su un Leader a 1 Vita. Nessuna vittoria ai punti, nessuna patta: la partita si chiude sul tavolo.
9. **Campo** (da A, versione minima): ogni giocatore porta 1 carta Campo. È attivo il Campo del secondo giocatore; passa a quello di chi si Risveglia per primo. Il comeback cambia anche il terreno.

**Perché questa base.** Mantiene l'intuitività e la simulabilità di B (turni chiusi, nessuna pila, azioni enumerabili). Prende la miglior inerzia di C e il miglior principio di A. Corregge i miei due difetti peggiori: il Risveglio che frena l'attacco e il Crepuscolo punitivo.

### Voto
1. **B+ (ibrido sopra).** È il miglior rapporto tra profondità e complessità, ed è l'unico costruibile e testabile in simulatore già alla prima iterazione.
2. **C, semplificato.** Va a C e non ad A perché la sua idea firma (passare = investire + iniziativa) è la più originale del lotto e risolve il turno passivo. Lo voterei primo se: (a) togliesse i requisiti d'Aspetto; (b) passasse a 1 Riflesso per round, solo per il difensore; (c) eliminasse la Spinta. Anche così resta il più difficile da insegnare.
3. **A.** Ha idee eccellenti (inerzia, nessuna negazione, zone scelte dallo sfondato) che vanno *assorbite*, ma come base è la più costosa da simulare e da imparare, e la più esposta al "vince il numero più alto".
