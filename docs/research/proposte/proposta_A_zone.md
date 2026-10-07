# Proposta A — "CROCEVIA": controllo di zone a Fronte mobile

> Direzione: controllo di zone/campi di battaglia + Leader personale. Versione regole 0.1, pensata per essere simulabile (stato discreto, timing chiuso, informazione nascosta = solo mano e mazzo).

---

## 1. Elevator pitch e meccanica firma

**Pitch.** Tre zone contese, un Leader che scende in campo, un solo obiettivo: spingere il fronte fino allo sfondamento.
Ogni turno scegli se *presidiare* (le tue unità pronte spingono il fronte) o *combattere* (ingaggiare costa la presenza).
Nessuna esplosione in un turno: il fronte si muove di una casella alla volta, e chi sfonda paga lo slancio.

**Meccanica firma — il Fronte a inerzia.** Ogni zona ha un **segnalino Fronte** su un tracciato a 7 caselle (−3 … 0 … +3). A fine turno il giocatore attivo che ha più Forza *pronta* in una zona sposta il segnalino di **una** casella verso l'avversario. **Regola d'inerzia: ogni segnalino si muove al massimo di 1 casella per turno, da qualunque fonte** (Verifica o effetti). Alla terza casella c'è lo **Sfondamento**: si incassano Gloria, la zona viene sostituita da una nuova scelta *da chi l'ha persa*, e le unità vincitrici si esauriscono. È un tiro alla fune: la vittoria richiede pressione visibile su più turni, l'avversario vede sempre arrivare il colpo e ha sempre un turno per reagire.

Idee prese dalla ricerca: punti territoriali e "ultimo punto" vincolato (Riftbound), slot limitati (Snap), agire-espone (Lorcana), risorsa garantita (OPTCG/Hearthstone), Leader-identità (OPTCG), finestra di reazione unica e budgetata (hook 6.4.3), zone portate dai giocatori (Riftbound), comeback "guadagnato" sul cambio di terreno.

---

## 2. Regole base v0.1

### 2.1 Componenti e deckbuilding
- **Leader** (1, fuori mazzo): Forza/Tempra, un'abilità, due **Vessilli** (colori) e soglie di **Dottrina**.
- **Mazzo principale**: esattamente **40 carte**, max 3 copie per nome, solo carte dei 2 Vessilli del Leader o **Neutrali**.
- **Pila Zone** (3 carte Zona, fuori mazzo, tutte diverse, pubbliche).
- Quattro Vessilli nel set base: **Ferro** (difesa), **Brace** (aggressione), **Marea** (movimento), **Radice** (crescita).

### 2.2 Tavolo e setup
- Tre corsie: **Sinistra – Centro – Destra** (adiacenza: Centro è adiacente a entrambe).
- Il **Centro** inizia sempre con la zona neutra **Crocevia** (Valore 1, nessun effetto). Il primo giocatore piazza una zona della sua Pila a Sinistra, il secondo una della sua a Destra. Tutti i Fronti a 0.
- Ogni lato di ogni zona ha **4 slot** unità (per giocatore: non si può bloccare lo spazio altrui) + 1 slot **Stendardo**.
- Il Leader parte nella **Retrovia** (fuori dalle zone).
- Si sceglie a caso chi inizia. Mano iniziale 5; **mulligan** unico: rimetti in fondo quante carte vuoi e ripesca lo stesso numero.

### 2.3 Risorsa: Comando
- All'inizio del tuo turno il tuo Comando si ricarica a **min(numero del tuo turno, 8)**. Risorsa garantita: niente screw/flood.
- Il Comando **non speso resta disponibile durante il turno avversario** (solo per la tua reazione), poi si ricarica. È il "mana alzato": rinunciare a sviluppo per minacciare una risposta.
- **Dottrina** (decisione sulla carta, anti-flood): una volta per turno puoi mettere una carta dalla mano **a faccia in su** sotto il Leader. Non dà Comando: sblocca le abilità del Leader a soglia (tipicamente 2 e 4 = **Ascesa**). Le carte morte a fine partita diventano progressione.

### 2.4 Struttura del turno
1. **Inizio** — Prepara (raddrizza) unità e Leader; ricarica Comando; pesca 1 (il primo giocatore salta la pesca del suo turno 1); effetti "a inizio turno".
2. **Principale** — In qualsiasi ordine e quante volte vuoi, salvo limiti:
   - giocare carte pagando Comando (unità in uno slot libero di una zona a tua scelta);
   - **Dottrina** (1/turno);
   - **Manovra**: paga 1, sposta un'unità pronta in una zona adiacente (resta pronta; max 1 Manovra per unità per turno);
   - **Comandare**: paga 1, sposta il Leader dalla Retrovia a una zona o tra zone adiacenti (1/turno);
   - **Ingaggio** (vedi 2.6); abilità attivate.
3. **Verifica** — Finestra di reazione avversaria "Allarme", poi per ogni zona da sinistra a destra: confronta la **Forza totale delle unità pronte (+ Leader se pronto)** dei due lati. Se l'attivo è **strettamente superiore**, il Fronte si sposta di 1 verso l'avversario (se non si è già mosso in questo turno). Se arriva a 3: **Sfondamento**.
4. **Fine** — Effetti di fine turno; i danni sulle unità si azzerano; limite mano 8 (scarta l'eccesso).

### 2.5 Tipi di carta
| Tipo | Quando | Note |
|---|---|---|
| **Unità** | Principale | Forza/Tempra. Entra **pronta** (conta subito in Verifica) ma non può ingaggiare nel turno in cui entra (salvo *Slancio*). |
| **Tattica** | Principale | Effetto una tantum, poi scarti. |
| **Tattica Rapida** | Principale o come reazione | Unico tipo giocabile nel turno avversario. |
| **Stendardo** | Principale | Permanente legato al tuo lato di una zona (max 1). Distrutto se quella zona viene sfondata. |
| **Zona** | Setup/Sfondamento | Valore (Gloria che dà) 1–2 e una regola locale simmetrica. |
| **Leader** | Sempre | Unità speciale, vedi 2.7. |

### 2.6 Interazione: Ingaggio e reazioni
- **Ingaggio**: esaurisci una tua unità pronta (o il Leader) per attaccare un'unità/Leader nemico **nella stessa zona**. Danno **simultaneo**: ciascuno infligge la propria Forza all'altro; danno ≥ Tempra = sconfitto (scarti; il Leader torna in Retrovia).
- **Il dilemma centrale**: un'unità esaurita **non conta in Verifica**, né nella tua né in quella avversaria (si prepara solo al tuo prossimo inizio turno). Combattere toglie presenza ai due lati; presidiare tiene la spinta ma lascia vivere le minacce.
- **Scorta** (parola chiave): quando un'unità nemica ingaggia nella zona, puoi ridirigere l'Ingaggio su una tua unità pronta con Scorta. Gratuito, non conta come reazione.
- **Reazione — una sola per turno avversario.** Due finestre possibili: (a) dopo la dichiarazione di un Ingaggio, prima del danno; (b) **Allarme**, all'inizio della Verifica avversaria. Si gioca 1 Tattica Rapida (o 1 abilità "Reazione") pagando con il Comando lasciato aperto. L'attivo **non** può rispondere alla reazione: nessuna pila, risoluzione immediata.
- **Principio di design vincolante**: nessuna carta "annulla" un'altra carta o vieta azioni. Le reazioni modificano Forza, posizione o danno, mai la possibilità di giocare.

### 2.7 Leader
- Ha Forza/Tempra, conta in Verifica nella sua zona se pronto, può ingaggiare ed essere ingaggiato.
- Se sconfitto: torna in Retrovia ed è **Stordito** fino alla fine del tuo prossimo turno (non può Comandare). Non dà Gloria all'avversario: niente "uccidi il generale e vinci".
- Abilità base sempre attiva + soglie di Dottrina (es. 2: bonus; 4: **Ascesa**, il Leader cambia lato con statistiche/abilità migliori, come i campioni LoR).

### 2.8 Sfondamento
Quando un Fronte raggiunge la casella 3 verso un giocatore:
1. L'attivo guadagna **Gloria = Valore della zona** (+1 in Crepuscolo).
2. Gli Stendardi in quella zona vengono distrutti; la zona va nella pila scarti Zone.
3. **Il giocatore sfondato sceglie** la nuova zona dalla propria Pila Zone (se vuota: dalla Pila avversaria; se entrambe vuote: Crocevia). Il Fronte torna a 0.
4. **Contraccolpo**: le unità (e il Leader) dell'attivo in quella zona si **esauriscono**. Lo sfondato **pesca 1 carta**.

### 2.9 Vittoria, fine partita, anti-stallo
- **Vittoria**: arrivare a **8 Gloria** (controllo immediato).
- **Crepuscolo** (dal round 10): in Verifica, in caso di **parità** con almeno 1 unità pronta dell'attivo nella zona, il Fronte si muove comunque verso l'avversario; gli Sfondamenti valgono +1.
- **Limite duro**: a fine round 15 vince chi ha più Gloria; parità → somma delle posizioni dei Fronti a proprio favore; ancora parità → patta.
- **Mazzo vuoto**: se devi pescare e non puoi, l'avversario guadagna 1 Gloria al posto della tua pescata (niente sconfitta istantanea, niente mill-OTK).

### 2.10 Compensazione primo giocatore
- Il primo giocatore **non pesca** al suo turno 1 e **salta la Verifica** del suo turno 1.
- Il secondo giocatore riceve il gettone **Iniziativa**: una volta per partita, +1 Comando nel suo turno (anche per una reazione). Valore da tarare con simulazioni di massa.

### 2.11 Anti-OTK (riassunto strutturale)
1. Inerzia: max 1 casella per Fronte per turno → max 3 caselle totali per turno.
2. Uno Sfondamento richiede almeno 3 Verifiche vinte nella stessa zona (3 turni del giocatore).
3. Contraccolpo: chi sfonda si esaurisce lì e perde la spinta per un giro.
4. Slot 4 per lato: tetto alla Forza concentrabile.
5. Una sola reazione per turno, nessuna catena, nessuna negazione.

---

## 3. Perché 5–15 turni per giocatore

**Massimo teorico (goldfish, avversario inerte, curva perfetta).** Caso peggiore: il secondo giocatore (che verifica già al T1). Con 1 Comando a T1 copri una zona, da T3 tutte e tre:
- Zona A: spinte T1-T2-T3 → Sfondamento T3; Zona B: T2-T3-T4 → T4; Zona C (Crocevia, V1): T3-T4-T5 → T5. Totale con Valori 2+2+1 = **5 Gloria a T5**.
- Contraccolpo: le unità si preparano al turno successivo, la nuova zona riparte da 0 → secondo Sfondamento in A a T6 (+2 = 7), in B a T7 (**9 ≥ 8**).
- **Vittoria più rapida possibile: turno 7**, con avversario che non gioca. Un OTK è impossibile per costruzione.

**Partita reale.** Se l'avversario contesta, ogni zona oscilla: assumendo che chi è in vantaggio vinca stabilmente 2 zone su 3 e l'altro 1, il vantaggiato fa netto circa +1 casella per round nelle sue zone (spinge 1, l'avversario ne recupera ~0–0,5 con reazioni/Ingaggi e col contraccolpo). Servono ~3–4 round per Sfondamento, cioè 2 zone ogni ~4 round = ~4 Gloria ogni 4 round → **8 Gloria verso i turni 9–12**. Mazzi molto difensivi scivolano verso il Crepuscolo (round 10+), che sblocca le parità e alza il valore degli Sfondamenti; il limite a 15 chiude comunque.

| Profilo | Turno di vittoria stimato |
|---|---|
| Aggro (Incursori) vs mazzo lento | 7–9 |
| Midrange speculare | 9–12 |
| Difesa vs difesa | 11–15 (Crepuscolo decisivo) |

Parametri di taratura: soglia Gloria (7–9), lunghezza del tracciato (±3), round del Crepuscolo (9–11).

---

## 4. Archetipi di esempio

Formato carta: **Nome** — costo — tipo — Forza/Tempra — testo. Parole chiave: *Scorta*, *Slancio* (può ingaggiare nel turno in cui entra), *Presidio X* (+X Forza durante la Verifica avversaria), *Fluido* (Manovra gratuita), *Crescita* (segnalino +1/+1).

### 4.1 Bastioni (Ferro) — difendere per avanzare
Vince "tenendo": unità a Tempra alta e Presidio che rendono le Verifiche avversarie impossibili, poi spinge lentamente 1–2 zone. Debole al movimento (Correnti). **Combo**: con Germogli (Stendardi che potenziano molte piccole unità) e con Correnti (spostare Presidio dove serve all'ultimo).
- **Sentinella del Bastione** — 2 — Unità — 1/4 — Scorta. Presidio 2.
- **Muro di Scudi** — 3 — Stendardo — Le tue unità in questa zona hanno Presidio 1 e +0/+1.
- **Castellana di Ferro** — 5 — Unità — 3/6 — Quando entra: se il Fronte di questa zona è a tuo sfavore, spostalo di 1 casella verso il centro (conta per l'inerzia del turno).

### 4.2 Incursori (Brace) — colpire e restare in piedi
Tempo e Ingaggi: Slancio e "Bottino" (si raddrizza dopo un'uccisione) aggirano il dilemma attacca/presidia per un turno. Pressione rapida, ma unità fragili. **Combo**: con Correnti (entrare in una zona e colpire subito dove il nemico è scoperto); con i neutrali di rimozione.
- **Predone di Cenere** — 1 — Unità — 2/1 — Slancio.
- **Carica Incendiaria** — 2 — Tattica Rapida — Un'unità ottiene +2/+0 fino a fine turno. Se usata nel tuo turno, ha anche Slancio.
- **Capobanda Rosso** — 4 — Unità — 4/3 — Bottino: la prima volta ogni turno che sconfigge un'unità in un Ingaggio, si prepara.

### 4.3 Correnti (Marea) — il fronte è dove decido io
Sposta unità (proprie e talvolta altrui) per vincere le Verifiche con il minimo di Forza, sfruttando l'Allarme per "rubare" una zona all'ultimo. Pescata legata al movimento. **Combo**: con Incursori (Manovra + Slancio), Germogli (sparpagliare token), Bastioni (Presidio mobile).
- **Messaggero dell'Onda** — 1 — Unità — 1/2 — Fluido. Quando si sposta: +1/+0 fino a fine turno.
- **Risacca** — 1 — Tattica Rapida — Sposta un'unità con costo ≤3 (tua o nemica) in una zona adiacente con slot libero. Resta pronta.
- **Navigatrice delle Maree** — 4 — Unità — 3/4 — La prima volta in ogni tuo turno che una tua unità si sposta, pesca 1 carta.

### 4.4 Germogli (Radice) — larghezza e crescita
Riempie gli slot con token e segnalini Crescita: tanta Forza distribuita, difficile da rimuovere con Ingaggi singoli. Vulnerabile a unità grandi con Bottino. **Combo**: con Bastioni (Stendardi a beneficio di massa) e Correnti (Fluido sui token per "versare" Forza nella zona giusta).
- **Seminatrice** — 2 — Unità — 1/2 — Quando entra: crea un Germoglio (unità 1/1) nella stessa zona o in una adiacente.
- **Pioggia di Primavera** — 3 — Tattica — Metti 1 Crescita su ogni tua unità in una zona.
- **Antico Radicante** — 6 — Unità — 3/6 — +1 Forza per ogni altra tua unità in questa zona (max +3 per gli slot).

### 4.5 Neutrali di esempio
- **Esploratore di Ventura** — 2 — Unità — 2/2 — Quando entra: se hai meno Gloria dell'avversario, pesca 1 carta. *(comeback guadagnato, gioca in ogni mazzo)*
- **Colpo Mirato** — 3 — Tattica — Infliggi 3 danni a un'unità. *(rimozione universale ma costosa e limitata: risposta disponibile a tutti i colori, contro i matchup polarizzati)*

### 4.6 Zone e Leader di esempio
- **Guado** (V1) — Le Manovre verso o da questa zona costano 0.
- **Torre di Guardia** (V2) — Le unità qui hanno Scorta.
- **Campo di Cenere** (V2) — Le unità qui hanno +1/+0 mentre ingaggiano.
- **Varra, Maresciallo** (Ferro/Radice) — 2/5 — Le unità nella zona di Varra hanno Presidio 1. Dottrina 2: Muro di Scudi costa 1 in meno. Dottrina 4 (Ascesa): 3/6, quando Varra entra in una zona crea un Germoglio.
- **Kesh, Lama di Brace** (Brace/Marea) — 3/3 — Comandare costa 0. Dottrina 2: Slancio. Dottrina 4 (Ascesa): 4/4, Bottino.

---

## 5. Autocritica: 5 rischi principali e come testarli

1. **"Vince il numero più alto" (critica rivolta ad Altered).** Se la Verifica domina, il gioco diventa somma di Forze e l'Ingaggio sparisce. *Test*: nel simulatore misurare Ingaggi per turno e % di partite vinte senza Ingaggi; obiettivo ≥1,5 Ingaggi/turno nei midrange. Leve: costo di presenza dell'Ingaggio, Bottino, rimozione neutra.
2. **Stallo difensivo / Presidio troppo forte.** Due Bastioni possono pareggiare tutte le zone fino al Crepuscolo. *Test*: distribuzione della lunghezza partita per matchup; allarme se >15% delle partite arriva al round 15. Leve: tetto a Presidio (max +2 per unità), Crepuscolo al round 9, valore delle parità.
3. **Vantaggio del primo giocatore e snowball.** Chi sviluppa per primo vince Verifiche "gratis"; chi sfonda può incatenare zone. *Test*: 10.000+ partite AI vs AI a mazzi specchio, win rate per posto (obiettivo 48–52%) e "tasso di rimonta" (vittoria di chi era sotto di ≥3 Gloria al round 6; obiettivo 20–30%). Leve: gettone Iniziativa, contraccolpo, pesca dello sfondato, scelta della zona.
4. **Correnti/Risacca come controllo frustrante.** Spostare unità avversarie in Allarme può annullare un intero turno di sviluppo (anti-pattern "risposta che toglie agency"). *Test*: frequenza e impatto delle reazioni sulla Verifica (quante Verifiche ribaltate per partita), sondaggi di playtest umano sul "turno rubato". Leve: limite di costo bersaglio, solo unità tue nelle versioni comuni, l'unità spostata resta pronta (può ancora agire).
5. **Difficoltà per il simulatore/AI.** Ramificazione alta (3 zone × slot × ordine di giocate × Manovre × Ingaggi), timing delle due finestre di reazione, informazione nascosta della mano. *Mitigazioni già nelle regole*: niente pila, una reazione per turno, risoluzione zona per zona da sinistra a destra, slot fissi, danni che si azzerano a fine turno, nessuna moneta. *Test*: implementare prima un'AI greedy (valuta Δ Forza per zona + Fronti + Gloria), poi MCTS con determinizzazione della mano avversaria; misurare il branching medio per turno e il divario greedy/MCTS (se il greedy vince >45% contro MCTS, il gioco ha poca profondità; se le decisioni ottime sono troppo profonde per MCTS a 1 s, semplificare Manovre).

**Rischio minore da monitorare**: la Dottrina potrebbe diventare automatica ("butto sempre la peggiore"). Se nei log l'AI la usa sempre al primo turno utile, renderla più costosa (es. solo dal turno 3) o dare alle carte effetti "Eco" leggeri mentre stanno in Dottrina.
