# Proposta B — "CICATRICI": duello di Leader con la vita come risorsa

> Direzione: Leader sempre in gioco, danno subito che diventa risorsa (controllata), risorsa automatica con scelte (spendere / infondere / accantonare), una sola finestra di reazione pagata con risorse non spese, unità che diventano vulnerabili quando agiscono.
> Fonti di riferimento: `analisi_fonti.md` (§6.2–6.5) e `ricerca_web.md` (§2.2–2.5).

---

## 1. Elevator pitch e meccanica firma

**Pitch.**
Due Leader si sfidano: ogni colpo che subisci non sparisce, diventa una **Cicatrice** scoperta che ti dà carte, difese e alla fine **risveglia** il tuo Leader.
La Brace della tua Fornace cresce da sola ogni turno: la spendi per giocare, la infondi nelle unità per colpire più forte o la accantoni come Guardia per l'unica contromossa nel turno avversario.
Chi attacca si espone: ogni azione è una promessa e un bersaglio.

**Meccanica firma: le Cicatrici.**
Quando il tuo Leader perde Vita, la carta Vita va **a faccia in su** nella tua zona Cicatrici (pubblica). Le Cicatrici:
1. **si possono recuperare** in mano (una per turno, pagando 1 Brace): il danno diventa carte, ma con un costo e un tetto;
2. **alimentano le Reazioni**: una carta Reazione si può giocare direttamente dalle Cicatrici;
3. **contano per Furia N** (bonus se hai almeno N Cicatrici);
4. alla **terza Cicatrice il Leader si Risveglia** (si gira sul lato potenziato, una volta per partita).

Rispetto alla Vita di One Piece: niente Trigger casuali (le carte sono visibili, varianza di *input* e non di *output*), il recupero in mano è limitato e pagato, e c'è una tensione nuova: recuperare una Cicatrice ti dà una carta ma *abbassa* il conteggio di Furia. È un comeback **guadagnato** (Riot, Rosewater "catch-up"): crea decisioni per entrambi — l'attaccante sceglie *quando* far risvegliare l'avversario, il difensore *quanto* consumare le proprie ferite.

---

## 2. Regole base v0.1

### 2.1 Mazzo e composizione
- **1 Leader** (fuori dal mazzo) con: Forza (tipicamente 4), Vita 5, 1–2 colori, un'abilità sul lato Base e una sul lato Risvegliato.
- **Mazzo di 40 carte**, massimo 3 copie per nome. Ogni carta deve condividere almeno un colore col Leader oppure essere **Neutrale** (grigia).
- 4 colori nel set base (Rosso, Blu, Nero, Verde); i Leader bicolori sono il veicolo principale dei combo cross-archetipo.
- Nessuna carta-risorsa nel mazzo: la risorsa è un contatore (la Fornace) → zero screw/flood.

### 2.2 Setup
1. Si decide il primo giocatore a caso.
2. Ognuno pesca **5 carte** (il secondo giocatore **6**).
3. **Mulligan parziale** unico: metti in fondo al mazzo fino a 3 carte e ripesca altrettante.
4. Metti le prime **5 carte del mazzo** a faccia in giù sotto il Leader: è la **Vita**. Nessuno può guardarle.
5. Il secondo giocatore riceve il segnalino **Scintilla** (vedi §2.9).
6. Fornace di entrambi a 0.

### 2.3 Risorse: Fornace, Brace, Guardia
- **Fornace**: livello che sale di **+1 all'inizio di ogni tuo turno, fino a 8**.
- **Brace**: all'inizio del tuo turno ricevi Brace pari al livello della Fornace. Le Brace non spese **non** passano al turno dopo come Brace.
- Ogni Brace ha tre usi:
  - **Spendere**: pagare il costo di carte e abilità.
  - **Infondere**: durante la tua fase principale, assegna 1 Brace a una tua unità o al Leader: **+1 Forza fino a fine turno**. Si infonde solo nella fase principale, mai durante un combattimento già dichiarato.
  - **Accantonare**: alla fine del tuo turno, fino a **2** Brace non spese diventano segnalini **Guardia** (3 col Leader Risvegliato). La Guardia esiste solo durante il turno avversario e si scarta al tuo Ripristino successivo.
- **Rimarginare** (1 volta per turno, fase principale): paga 1 Brace, metti in mano una Cicatrice a tua scelta.

### 2.4 Struttura del turno
1. **Ripristino**: le tue unità e il tuo Leader tornano **Pronti** (finisce l'Esposizione); scarta la Guardia rimasta; Fornace +1 (max 8); ricevi le Brace. *Crepuscolo*: vedi §2.8.
2. **Pesca**: pesca 1 carta (il primo giocatore non pesca nel suo turno 1).
3. **Fase principale**, in qualsiasi ordine e quante volte vuoi: giocare carte, infondere, Rimarginare, attivare abilità, **attaccare**. Il primo giocatore non attacca nel suo turno 1.
4. **Fine**: accantona fino a 2 Brace in Guardia; effetti "a fine turno"; limite di mano 8 (scarta l'eccesso).

Il turno attivo è un unico ciclo "scegli un'azione legale → risolvi" (comodo per il simulatore: lo spazio delle azioni è enumerabile, nessuna pila).

### 2.5 Tipi di carta
- **Leader**: sempre in gioco, non può essere distrutto né rimosso. Attacca come un'unità (una volta per turno) con la propria Forza.
- **Unità**: costo, Forza, parole chiave. Massimo **5** unità in gioco. Entrano Pronte ma non possono attaccare nel turno in cui entrano (salvo **Assalto**).
- **Tattica**: effetto immediato, solo nella tua fase principale.
- **Reazione**: giocabile solo nella finestra di reazione, dalla mano **o dalle Cicatrici**; il costo si paga **solo in Guardia**.
- **Reliquia**: permanente senza Forza, massimo 2 in gioco. Le Reliquie non si espongono.

### 2.6 Stati: Pronto ed Esposto
- Un'unità (o il Leader) diventa **Esposta** quando **attacca**, **intercetta** o usa un'abilità con il simbolo ⟳. Resta Esposta fino al **Ripristino del suo controllore**.
- Un'unità Esposta non può attaccare, intercettare né usare ⟳, e **può essere attaccata**. Le unità Pronte non possono essere bersaglio di attacchi.
- Un **Leader Esposto** non può usare la propria abilità Reazione nel turno avversario successivo (attaccare col Leader costa la sua difesa).
- **Regola di design**: la rimozione economica (costo ≤3) colpisce solo unità Esposte. Chi non agisce è al sicuro dagli attacchi, ma non fa pressione e non ferma nessuno.

### 2.7 Combattimento e finestra di reazione
Sequenza di un attacco (nessuna pila, ordine fisso):
1. **Dichiarazione**: scegli un tuo attaccante Pronto (unità o Leader) → diventa Esposto. Scegli il bersaglio: il **Leader** avversario o un'**unità avversaria Esposta**.
2. **Intercetto**: il difensore può far intercettare l'attacco a **una** sua unità Pronta con **Scudo**: diventa il nuovo bersaglio e diventa Esposta.
3. **Finestra di reazione** (solo il difensore, **una sola volta per turno avversario** in tutto): può fare UNA tra:
   - **Parata**: spendi 1 Guardia → il bersaglio ottiene +2 Forza per questo combattimento;
   - giocare **una carta Reazione** (dalla mano o dalle Cicatrici) pagandone il costo in Guardia;
   - usare l'abilità Reazione del proprio Leader (se non è Esposto).
4. **Risoluzione**: si confronta la Forza.
   - **Contro un'unità**: la Forza più bassa viene sconfitta (va nel cimitero); in caso di parità entrambe.
   - **Contro il Leader**: se la Forza dell'attaccante è ≥ della Forza del Leader, il Leader **perde 1 Vita** → la carta va nelle Cicatrici. Altrimenti non succede nulla (l'attaccante non viene sconfitto).
5. **Saldo**: dopo che un Leader ha perso **2 Vite nello stesso turno**, per il resto di quel turno non può più perdere Vita (né da attacchi né da effetti).

L'attaccante sa tutto ciò che gli serve quando dichiara (Guardia e Cicatrici sono pubbliche); l'unica informazione nascosta è la mano. Bluff leggero, nessuna eccezione di timing.

**Limiti per turno**: ogni unità attacca al massimo una volta per turno; un effetto può renderla di nuovo Pronta (**Rinnovo**) al massimo una volta per turno per unità.

### 2.8 Vittoria, Crepuscolo, deck-out
- **Colpo finale**: vinci se colpisci con successo un Leader che era **già a 0 Vita all'inizio del tuo turno** (il Leader è "Alle Corde"). Arrivare a 0 non basta: l'avversario ha sempre un turno intero, col Leader risvegliato e 5 Cicatrici, per reagire.
- **Crepuscolo** (anti-stallo): dal tuo **10° turno** in poi, al Ripristino il tuo Leader perde 1 Vita (diventa Cicatrice, quindi carburante per la spinta finale). Se è già a 0, perdi.
- **Deck-out**: se devi pescare da un mazzo vuoto, al posto della pesca perdi 1 Vita; se sei a 0, perdi.
- Nessuna vittoria alternativa nel set base (no Exodia, no mill-win puro).

### 2.9 Compensazione del primo giocatore
- Il **primo** giocatore non pesca e non attacca nel turno 1, e subisce per primo il Crepuscolo.
- Il **secondo** giocatore ha **6 carte** in mano iniziale e il segnalino **Scintilla**: una volta per partita, nella tua fase principale, +1 Brace.
- Obiettivo di taratura: 48–52% di vittorie per il primo giocatore su 10.000 partite IA in mirror. Leve di riserva: Fornace del primo giocatore a −1 al turno 1, Scintilla che dà anche 1 Guardia.

### 2.10 Anti-OTK e anti-hard-control (riepilogo)
| Problema | Freno strutturale |
|---|---|
| OTK / burst | Saldo (max 2 Vite per turno) + Colpo finale solo su Leader già Alle Corde → minimo 4 turni d'attacco per vincere; Fornace max 8; 1 attacco per unità; Rinnovo max 1 per unità per turno; 5 slot unità |
| FTK del primo giocatore | Nessun attacco nel turno 1; Vita 5 non può scendere sotto 3 nel primo turno d'attacco |
| Hard-control / negazioni | Una sola reazione per turno avversario, pagata con risorse sottratte al proprio turno; le Reazioni modificano il combattimento, non negano carte; nessuna risposta a Tattiche; nessuno scarto forzato dalla mano avversaria (linea guida) |
| Stallo difensivo | Crepuscolo dal turno 10; unità Pronte non attaccabili ma neanche utili se non agiscono; Scudo espone chi intercetta |
| Comeback assente | Cicatrici (carte + Reazioni + Furia) e Risveglio |
| Snowball del comeback | Recupero 1/turno a pagamento; Saldo vale per entrambi; Risveglio una sola volta |

---

## 3. Perché le partite durano 5–15 turni

**Minimo teorico.** Servono 5 Vite + il colpo finale. Con Saldo (max 2 Vite per turno) e Colpo finale solo su un Leader già a 0: 5→3→1→0 richiede tre turni d'attacco, il colpo finale un quarto. Il primo giocatore attacca dal turno 2 → **vittoria più rapida al turno 5** (al turno 5 anche il secondo giocatore). Nessun OTK è possibile per regola.

**Aggro realistico.** Leader Forza 4. Un'unità da 2 Brace ha Forza 2–3: per colpire il Leader serve infondere 1–2 Brace, oppure servono unità da 3–4. Al turno t la Fornace dà t Brace: dal turno 3–4 l'aggro schiera 2 attaccanti validi + il Leader. Il difensore ne ferma ~1 per turno (Parata o Reazione) e talvolta un secondo con Scudo. Quindi ~1–1,5 colpi a turno dal turno 3: 6 colpi → **turno 6–8**.

**Midrange.** Colpi dal turno 4–5, ~1 a turno al netto di intercetti e scambi: **turno 8–11**.

**Controllo.** Rallenta, ma la reazione è una sola per turno e la rimozione economica colpisce solo chi si espone, quindi non blocca tutto. Il Crepuscolo garantisce la fine: se al turno 10 un giocatore ha V Vite, è Alle Corde al più tardi al turno 10+V e cade al primo colpo riuscito o al Crepuscolo successivo. Con V tipico 1–3 a quel punto → **fine entro il turno 12–14**. Il deck-out (35 carte nel mazzo, ~1 pesca per turno) non arriva prima del turno ~30: non è un fattore.

**Bersaglio**: mediana 8–10 turni per giocatore, 90% delle partite tra 6 e 14.

---

## 4. Archetipi e carte d'esempio

Formato: **Nome** — costo · tipo · Forza · testo. Parole chiave: **Assalto** (attacca nel turno in cui entra), **Scudo** (può intercettare), **Infuso** (bonus quando riceve Brace), **Furia N** (attiva con ≥N Cicatrici), **Bracconiere** (bonus contro bersagli Esposti), **⟳** (attivare espone). Le parole chiave sono **ponte**: ognuna compare in due colori.

### 4.1 Lame Cremisi (Rosso) — Infusione / aggro
Tutta la Brace va in Forza: unità economiche con Infuso e Assalto, Tattiche che premiano l'unità più infusa. Gioca contro la Guardia: chi accantona non infonde, e chi aspetta finisce Alle Corde. **Combo**: con il Verde (Infuso + Bracconiere per ripulire le unità Esposte), con il Nero (Furia dà Forza "gratis" senza Brace).
- **Scudiera di Brace** — 1 · Unità · F2 · Assalto. Infuso: la prima volta che riceve Brace in un turno, +1 Forza extra.
- **Carica della Fornace** — 2 · Tattica · Una tua unità che ha ricevuto almeno 2 Brace in questo turno ottiene Rinnovo (torna Pronta dopo il suo attacco).
- **Vesh, Lama Rovente** — 4 · Unità · F4 · Assalto. Quando attacca, puoi spostare su di lei tutta la Brace infusa in un'altra tua unità.
- *Leader esempio — Arden, Fabbro di Guerra* (F4, Rosso/Verde). Base: una volta per turno, quando infondi 2+ Brace in una stessa unità, +1 Forza extra. Risvegliato (F5): le tue unità con Assalto hanno +1 Forza.

### 4.2 Bastioni (Blu) — Guardia / contrattacco
Accumula Guardia, intercetta con Scudo e punisce l'attaccante Esposto nel turno dopo. Non è hard-control: ferma un colpo per turno e vince con unità grosse e Reliquie di valore, non negando. **Combo**: con il Nero (sopravvive mentre le Cicatrici crescono, Reazioni dalle Cicatrici), con il Verde (chi intercetta l'attacco avversario espone l'attaccante, che il Verde caccia).
- **Sentinella del Guado** — 2 · Unità · F3 · Scudo. Quando intercetta, ottieni 1 Guardia (nel rispetto del massimo).
- **Muro di Scudi** — 1 Guardia · Reazione · Il bersaglio ottiene +3 Forza per questo combattimento. Se è un'unità che ha intercettato, a fine turno torna Pronta.
- **Il Bastione Vivente** — 5 · Unità · F6 · Scudo. Quando sconfigge in combattimento un'unità attaccante, pesca 1 carta.
- *Leader esempio — Maera, Custode del Passo* (F4, Blu/Nero). Base, Reazione: spendi 1 Guardia, l'attaccante ha −2 Forza per questo combattimento. Risvegliato (F5): la tua Parata dà +3 invece di +2.

### 4.3 Rancore (Nero) — Cicatrici / Furia
Vuole le ferite: Patti di sangue che trasformano la Vita in carte, unità con Furia che crescono man mano che il Leader sanguina, Reazioni pensate per essere giocate dalle Cicatrici. Rischio esplicito: si avvicina da solo al Colpo finale. **Combo**: con il Rosso (Furia + Infuso = picchi di Forza a basso costo), con il Blu (Guardia per sopravvivere alla fase Alle Corde).
- **Penitente delle Mille Ferite** — 2 · Unità · F1 · Furia 2: +3 Forza.
- **Patto di Sangue** — 1 · Tattica · Il tuo Leader perde 1 Vita (non può portarti sotto 1). Pesca 1 carta.
- **Grido dalla Cicatrice** — 2 Guardia · Reazione · L'attaccante ha −3 Forza per questo combattimento. Se la giochi dalle Cicatrici, costa 1 Guardia.
- *Leader esempio — Sorella Vey, la Segnata* (F4, Nero/Rosso). Base: Rimarginare non abbassa la Furia fino a fine turno. Risvegliato (F5): una volta per turno, quando Rimargini, costa 0.

### 4.4 Predatori (Verde) — Esposizione / caccia
Costringe l'avversario ad agire, poi colpisce chi si è esposto: Tattiche che espongono, Bracconieri che crescono contro bersagli Esposti, abilità ⟳ potenti ma che lasciano la propria unità scoperta. Il dilemma "agire = esporsi" diventa un'arma. **Combo**: con il Blu (l'intercetto espone gli attaccanti avversari), con il Rosso (Infuso per chiudere gli scambi in vantaggio).
- **Lince del Sottobosco** — 2 · Unità · F2 · Bracconiere: +2 Forza quando attacca un'unità Esposta.
- **Esca** — 1 · Tattica · Un'unità avversaria con costo ≤3 diventa Esposta.
- **Matriarca del Branco** — 5 · Unità · F5 · Una volta per turno, quando una tua unità sconfigge un'unità Esposta, pesca 1 carta.
- *Leader esempio — Thorn, Voce del Branco* (F4, Verde/Blu). Base: ⟳ (il Leader si espone), 2 Brace: un'unità avversaria con costo ≤2 diventa Esposta. Risvegliato (F5): i tuoi Bracconieri hanno +1 Forza.

### 4.5 Neutrali (giocabili in ogni mazzo)
- **Recluta del Crocevia** — 1 · Unità · F1 · Scudo. Quando entra, se hai ≥2 Cicatrici, ottiene +1 Forza permanente. *(Collante tra Bastioni e Rancore; utile a tutti come difesa d'apertura.)*
- **Lanterna del Pellegrino** — 2 · Reliquia · Puoi accantonare 1 Brace in più (il massimo di Guardia aumenta di 1). *(Abilita Reazioni costose in qualsiasi colore.)*
- **Colpo Mirato** — 3 · Tattica · Sconfiggi un'unità Esposta con Forza ≤4. *(Rimozione universale ma condizionata: rispetta la regola "colpisce solo chi agisce".)*

---

## 5. Autocritica: i 5 rischi principali e come testarli

**1. Il Risveglio scoraggia l'attacco (rubber band al contrario).** Se la terza Cicatrice è troppo forte, l'attaccante smette di colpire il Leader a 3 Vite e accumula fino a un turno da "2 colpi + colpo finale", generando stalli e partite "a indovinello".
*Test*: IA greedy vs IA "consapevole del Risveglio"; misurare quanti turni di fila l'attaccante con vantaggio di board **non** attacca il Leader, e il win rate per numero di Cicatrici. Leve: soglia 3→4, Risveglio più debole, Forza Leader Risvegliato invariata.

**2. Saldo + Alle Corde rendono l'aggro troppo lento (o il controllo troppo comodo).** Minimo 4 turni d'attacco più una reazione per turno potrebbero spingere la mediana oltre 11 turni.
*Test*: istogramma della durata per coppia di archetipi su 10.000 partite; obiettivo mediana 8–10, ≥90% tra 5 e 15. Leve: Saldo a 3 Vite, Vita 4, Crepuscolo dal turno 9.

**3. La finestra di reazione è sbilanciata.** Troppo debole: tutti accantonano 0 Guardia e il turno avversario torna passivo (anti-pattern 8). Troppo forte: Parata e Reazioni annullano l'aggro, e la Guardia diventa una tassa obbligatoria come le hand trap.
*Test*: frequenza di Guardia accantonata per turno, % di attacchi al Leader fermati dalla reazione (bersaglio 30–45%), win rate di mazzi con 0 carte Reazione vs 8. Leve: Parata +2/+1, massimo di Guardia 2/3, costo delle Reazioni.

**4. Vantaggio del primo giocatore.** La Fornace automatica premia il tempo (dati Hearthstone: compensazioni fisse lasciano 2–4 punti, >10 nei mazzi tempo).
*Test*: mirror IA per ciascun archetipo, separando il win rate del primo giocatore per archetipo (l'aggro Rosso è il caso critico). Obiettivo 48–52%. Leve: Scintilla più forte, Fornace del primo giocatore a 0 al turno 1, Crepuscolo asimmetrico.

**5. Esplosione combinatoria e Recupero dominante per l'IA (e per i giocatori).** Infondere N Brace su M unità, l'ordine degli attacchi e il Rimarginare producono un branching factor alto; e "Rimarginare ogni turno" potrebbe essere sempre corretto (decisione finta).
*Test*: profilare il numero di azioni legali per turno nel simulatore (obiettivo: media <60 con infusione 1 Brace = 1 azione); confrontare MCTS vs euristica semplice — se l'euristica pareggia, la profondità è illusoria. Misurare la % di turni con Rimarginare quando possibile: se >90%, aumentare il costo o legarlo all'Esposizione del Leader.

---

### Parametri v0.1 in sintesi
Mazzo 40 · mano 5 (6 per il secondo) · Vita 5 · Leader F4 · Fornace +1/turno max 8 · Guardia max 2 (3 Risvegliato) · 1 reazione per turno avversario · Saldo 2 Vite/turno · Colpo finale su Leader già a 0 · Risveglio a 3 Cicatrici · Crepuscolo dal turno 10 · 5 unità, 2 Reliquie · mano max 8.
