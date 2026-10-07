# CICATRICI — Regolamento v0.1 (condiviso)

> Documento consolidato dall'editor neutrale dello swarm a partire da: `research/proposte/proposta_B_leader.md`, `bozza_regolamento_B.md`, `bozza_pilastri_B.md`, `discussione/revisione_critica_B.md`, round 1 e round 2 di A, B, C e del critico.
> Regola di consolidamento: un punto è **deciso** se almeno 3 dei 4 partecipanti al round 2 (A, B, C, critico) concordano. Dove c'è parità o nessuna maggioranza il regolamento scrive un **default** e rimanda la scelta al simulatore (§16). Il registro delle decisioni è in `discussione/esito_dibattito.md`.
> Convenzioni: "deve", "non può", "è illegale" sono vincolanti per il simulatore. I numeri marcati come *parametro* sono raccolti nella tabella del §15 e sono gli unici valori da tarare.

---

## 1. Panoramica

CICATRICI è un gioco di carte collezionabili 1 contro 1. Ogni giocatore guida un **Leader**, sempre in gioco, e un mazzo di 40 carte.

- Per vincere devi portare il Leader avversario **Alle Corde** (0 Vite) e poi, in un tuo turno **successivo**, metterlo a segno con un attacco: il **colpo finale** (§9).
- Ogni Vita persa non sparisce: la carta Vita si gira a faccia in su e diventa una **Cicatrice**, che il giocatore ferito può recuperare in mano, usare come Reazione o contare per la **Furia**. Dopo 3 Vite perse il Leader si **Risveglia**.
- La risorsa è la **Brace**: cresce da sola ogni turno (Fornace) e ogni punto si **spende**, si **infonde** in un personaggio o si **accantona** come **Guardia** per difendersi nel turno avversario.
- **Agire è esporsi**: chi attacca, intercetta o usa un'abilità ⟳ diventa **Esposto** e attaccabile fino al suo prossimo Ripristino.
- I turni sono **chiusi** (un giocatore attivo per volta). Non esiste una pila: ogni azione si risolve per intero, in un ordine fisso, prima della successiva. Nel turno avversario il difensore decide solo in due punti fissi di ogni attacco: **intercetto** e **finestra di reazione**.

Durata obiettivo: 5–15 turni per giocatore, mediana 8–10 (vedi `pilastri_design.md`).

---

## 2. Componenti e costruzione del mazzo

### 2.1 Componenti per giocatore
- **1 Leader** (fuori dal mazzo), carta a due facce: lato **Base** e lato **Risvegliato**.
- **1 mazzo di esattamente 40 carte.**
- Segnalini/contatori pubblici: Fornace, Brace, Guardia, contatore di infusione per personaggio, segnalino Scintilla (solo per il secondo giocatore).

### 2.2 Il Leader
Ogni Leader stampa: nome, 1 o 2 colori, **Forza**, **Tempra**, **Vita iniziale**, un'abilità sul lato Base e un'abilità sul lato Risvegliato.

Valori standard per tutti i Leader del set base:

| | Forza | Tempra | Vita iniziale | Massimo di Guardia |
|---|---|---|---|---|
| Lato Base | 3 | 5 | 5 | 2 |
| Lato Risvegliato | 4 | 5 (invariata) | — | 3 |

- **Forza**: il valore con cui il Leader **attacca**.
- **Tempra**: il valore che un attacco deve **eguagliare o superare** per mettere a segno un colpo sul Leader.
- Il Risveglio è un premio **offensivo** (+1 Forza) e di Guardia (+1 al massimo), non alza la Tempra.

### 2.3 Regole di costruzione
- Esattamente 40 carte, al massimo **3 copie per nome**.
- Ogni carta deve condividere **almeno un colore** col Leader oppure essere **Neutrale**.
- Colori del set base: **Rosso, Blu, Nero, Verde** (§12). Leader bicolori consigliati.
- Il mazzo non contiene carte-risorsa: la risorsa è un contatore.
- Un mazzo che viola queste regole è illegale e non può essere usato.

---

## 3. Zone di gioco

| Zona | Visibilità | Ordine | Note |
|---|---|---|---|
| Mazzo | Nascosto a entrambi | Ordinato, segreto | Si pesca dalla cima |
| Mano | Nascosta all'avversario | — | Massimo 8 carte **a fine turno** (§6.4) |
| Vita | Nascosta a **entrambi** | Pila, segreta | Sotto il Leader; si prende sempre la carta in cima |
| Cicatrici | **Pubblica** | Insieme non ordinato | Carte Vita perse, a faccia in su |
| Campo | Pubblica | — | Il Leader, **massimo 5 Unità**, **massimo 2 Reliquie** |
| Scarti | Pubblica | Ordinato per arrivo | Unità sconfitte, Tattiche risolte, Reazioni usate, carte scartate |
| Contatori | Pubblici | — | Fornace, Brace, Guardia, contatori di infusione, Scintilla, numero di turno, Vite perse nel turno (Saldo) |

- Le uniche informazioni nascoste sono: mano (all'avversario), ordine del mazzo, carte Vita (a entrambi).
- Giocare una sesta Unità o una terza Reliquia è **illegale** (l'azione non è disponibile). Non esiste sostituzione.

---

## 4. Preparazione

Eseguire in quest'ordine:

1. Si sceglie **a caso** il primo giocatore (G1); l'altro è il secondo giocatore (G2).
2. Ogni giocatore mette il Leader sul Campo, lato **Base**, stato **Pronto**.
3. Ogni giocatore mescola il proprio mazzo e pesca **5 carte** *(parametro: mano iniziale; default per entrambi, vedi variante V2 al §16)*.
4. **Mulligan**, una sola volta, prima G1 poi G2: il giocatore sceglie da 0 a 3 carte della mano, le mette in fondo al mazzo nell'ordine che preferisce e pesca altrettante carte dalla cima. Il mazzo non si rimescola.
5. Ogni giocatore mette le prime **5 carte** del mazzo coperte sotto il Leader, senza guardarle: è la sua **Vita**.
6. G2 riceve il segnalino **Scintilla** (§5.5).
7. Fornace a 0, Brace a 0, Guardia a 0 per entrambi. Numero di turno a 0 per entrambi.
8. Inizia il turno 1 di G1.

---

## 5. Risorse: Fornace, Brace, Guardia

### 5.1 Fornace
Livello pubblico, parte da 0. Sale di **+1** all'inizio di ogni tuo turno (Ripristino), fino a un massimo di **8** *(parametro)*. Nessun effetto del set base la riduce (legge di design 3).

### 5.2 Brace
Nel Ripristino la tua Brace diventa **uguale al livello della Fornace** (la Brace del turno precedente è già stata azzerata a fine turno). Ogni Brace ha tre usi, tutti solo nel tuo turno:

1. **Spendere**: pagare il costo di carte e abilità.
2. **Infondere** (§5.3).
3. **Accantonare** come Guardia, a fine turno (§5.4).

La Brace non usata e non accantonata si perde nella Fine del turno. La Brace infusa non torna mai disponibile.

### 5.3 Infondere
- Azione della fase principale, fuori da un combattimento: paga **1 Brace** e scegli un tuo **personaggio** (Unità o Leader), Pronto o Esposto. Quel personaggio ottiene **+1 Forza fino a fine turno** e il suo **contatore di infusione** aumenta di 1.
- Ogni infusione è un'azione separata da 1 Brace (per infondere 3 Brace si eseguono 3 azioni).
- Non esiste un tetto all'infusione per personaggio nella v0.1 (vedi leve di riserva, §16.4).
- Il **contatore di infusione** di ogni personaggio conta la Brace infusa in lui in questo turno. Si azzera nella Fine del turno. Gli effetti che spostano Brace infusa (es. Vesh) spostano anche il contatore e il bonus di Forza, ma **non** sono un'azione di infondere: non attivano **Infuso** né effetti "quando infondi".
- Infondere il Leader aumenta la sua **Forza**, mai la sua Tempra.

### 5.4 Guardia e massimo di Guardia
- **Massimo di Guardia**: un solo valore per giocatore, che vale per la riserva di Guardia **in ogni momento**. È 2 sul lato Base, 3 sul lato Risvegliato, +1 per ogni copia della Reliquia *Lanterna del Pellegrino* in gioco sotto il tuo controllo, più eventuali altri effetti.
- **Accantonare**: nella Fine del tuo turno (§6.4, passo 2), la tua Guardia diventa `min(Brace non usata, massimo di Guardia)`.
- La Guardia si usa **solo nel turno avversario**, per pagare Parate, carte Reazione e abilità di Reazione del Leader (§8, passo 5).
- Gli effetti che danno Guardia (es. Sentinella del Guado) la aggiungono fino al massimo; l'eccesso si perde.
- La Guardia rimasta si scarta all'inizio del tuo Ripristino.
- Se il massimo di Guardia diminuisce (es. una Lanterna lascia il gioco), la Guardia in eccesso si scarta al controllo di stato successivo. Se aumenta (es. Risveglio nel turno avversario), si alza **solo il tetto**: non si ottiene Guardia.

### 5.5 Scintilla
Una volta per partita, nella tua fase principale, scarta il segnalino Scintilla: ricevi **+1 Brace**. È Brace a tutti gli effetti: si può spendere, infondere o accantonare. Si può usare anche nel tuo turno 1.

---

## 6. Struttura del turno

Il **giocatore attivo** è quello di cui è il turno; l'altro è il **difensore**. "Turno" indica sempre il turno del giocatore attivo. Il **numero di turno** di un giocatore è quante volte ha iniziato un proprio turno (il primo turno di G1 è il suo turno 1, il primo turno di G2 è il suo turno 1). Ogni riferimento a "dal turno N" (Clessidra, Crepuscolo terminale) usa il **numero di turno del giocatore attivo** (default della variante V4, §16).

Ogni turno ha quattro fasi, in quest'ordine.

### 6.1 Ripristino
1. Il numero di turno del giocatore attivo aumenta di 1.
2. **Istantanea Alle Corde** (definizione unica, usata da §8 passi 5 e 7 e da §9.5): dopo l'aggiornamento del numero di turno e prima di ogni altro effetto, si registra se il Leader **avversario** è Alle Corde in questo momento (§9.1, con il numero di turno appena aggiornato). Questo valore resta fisso per tutto il turno e serve per il colpo finale e per Ultimo respiro.
3. **Crepuscolo terminale** (dal tuo turno 15, §9.6): se il **tuo** Leader è Alle Corde in questo momento, perdi la partita; altrimenti il tuo Leader perde 2 Vite (non soggette al Saldo).
4. Scarta la tua Guardia rimasta.
5. Tutti i tuoi personaggi tornano **Pronti** (finisce l'Esposizione).
6. Fornace +1 (massimo 8); la tua Brace diventa uguale alla Fornace.
7. Si risolvono gli effetti "all'inizio del tuo turno" (nessuno nel set base).
8. Controlli di stato (§7.4).

### 6.2 Pesca
Pesca 1 carta. **G1 non pesca nel suo turno 1.** Se devi pescare e il mazzo è vuoto, vedi §9.4.

### 6.3 Fase principale
Il giocatore attivo ripete il ciclo "scegli un'azione legale → risolvila per intero → controlli di stato" finché sceglie di terminare la fase. Azioni legali, in qualsiasi ordine e numero salvo i limiti indicati:

| Azione | Costo | Limiti |
|---|---|---|
| Giocare un'Unità | costo in Brace | Massimo 5 Unità sul Campo |
| Giocare una Reliquia | costo in Brace | Massimo 2 Reliquie sul Campo |
| Giocare una Tattica | costo in Brace | Si risolve e va negli Scarti |
| Infondere | 1 Brace | §5.3 |
| Usare un'abilità ⟳ (incluso **Rimarginare**, §10.2) | come stampato | Il personaggio deve essere Pronto; diventa Esposto |
| Usare un'abilità attivata senza ⟳ | come stampato | Come stampato |
| Usare la Scintilla | — | Una volta per partita |
| Dichiarare un attacco | — | §8; **nessuno attacca nel proprio turno 1** |
| Terminare la fase principale | — | — |

- Un'azione il cui costo non può essere pagato per intero è **illegale** e non compare tra le azioni disponibili (vale anche per i costi in Vita, §9.3).
- Un attacco, una volta dichiarato, si risolve per intero (§8, passi 1–9) prima che il giocatore attivo possa scegliere un'altra azione. **Tra un attacco e l'altro** si torna alla fase principale: si possono giocare carte, infondere, usare abilità e Rimarginare.
- Carte Reazione e abilità di Reazione non si usano mai nel proprio turno.

### 6.4 Fine
In quest'ordine:
1. Si risolvono gli effetti "a fine turno" (prima quelli del giocatore attivo, nell'ordine che sceglie; poi quelli del difensore).
2. **Accantonamento**: Guardia = `min(Brace non usata, massimo di Guardia)`.
3. **Scadenza**: la Brace residua si perde; scadono tutti i bonus "fino a fine turno" e le infusioni; i contatori di infusione si azzerano; Rinnovo concesso "fino a fine turno" scade.
4. **Limite di mano**: se hai più di 8 carte in mano, scarta (a tua scelta) fino ad averne 8.
5. Controlli di stato; il turno passa all'avversario.

---

## 7. Tipi di carta, stati e controlli di stato

### 7.1 Tipi di carta
- **Leader**: sempre in gioco; non può essere distrutto, sconfitto, rimosso né reso Esposto da effetti avversari. Può attaccare **una volta per turno** con la propria Forza. È sempre un **bersaglio legale** di attacco, sia Pronto sia Esposto. Non può intercettare.
- **Unità**: costo, Forza, eventuali parole chiave e testo. Entra **Pronta**, ma non può attaccare nel turno in cui entra (salvo **Assalto**). Può intercettare già nel turno avversario successivo se ha Scudo.
- **Tattica**: effetto immediato, solo nella tua fase principale fuori da un combattimento; poi va negli Scarti.
- **Reazione**: giocabile solo nella finestra di reazione (§8, passo 5), dalla mano **o dalle Cicatrici**, pagandone il costo **solo in Guardia**. Dopo l'uso va negli Scarti (anche se giocata dalle Cicatrici).
- **Reliquia**: permanente senza Forza; non è un personaggio, non può essere attaccata, non si espone.
- **Personaggio**: termine che indica un'Unità o un Leader.

### 7.2 Stati: Pronto ed Esposto
- Ogni personaggio è **Pronto** o **Esposto**.
- Un personaggio diventa Esposto quando **attacca**, **intercetta** o usa un'abilità **⟳**, oppure per effetto di una carta. Resta Esposto fino al Ripristino del suo controllore, salvo effetti che lo rendono Pronto prima (es. Muro di Scudi).
- Un personaggio Esposto **non può**: attaccare (salvo Rinnovo), intercettare, usare abilità ⟳, usare abilità di Reazione.
- Una **Unità** Esposta **può essere bersaglio di attacchi**. Un'Unità Pronta non può essere bersaglio di attacchi.
- Il **Leader** è bersaglio legale sia Pronto sia Esposto; per lui l'Esposizione conta solo per attaccare, per ⟳ (incluso Rimarginare) e per la sua abilità di Reazione.
- Rendere Esposto un personaggio già Esposto non ha effetto. Gli effetti di carta che "espongono" possono avere come bersaglio solo **Unità**, mai un Leader.

### 7.3 Forza e valore di difesa
- La **Forza** corrente di un personaggio = Forza stampata + bonus/malus attivi (infusione, Furia, effetti "fino a fine turno", effetti "per questo combattimento"). Può diventare 0 o negativa: non causa sconfitta di per sé, si usa così com'è nei confronti.
- **Valore di difesa** del bersaglio di un attacco: la Forza corrente se è un'Unità, la **Tempra** corrente se è un Leader.
- Un effetto che dà "+X al bersaglio" (Parata, Muro di Scudi) aumenta il **valore di difesa**: la Forza di un'Unità, la Tempra di un Leader.

### 7.4 Controlli di stato
Si eseguono dopo ogni azione della fase principale, al passo 8 di ogni combattimento, dopo ogni trigger del passo 9, alla fine del Ripristino e della Fine. In quest'ordine, ripetendo finché nulla cambia:

1. **Fine partita**: se un giocatore ha soddisfatto una condizione di sconfitta (§9), la partita finisce. Se entrambi la soddisfano nello stesso momento, **perde il giocatore attivo** (regola valida per ogni simultaneità, anche futura).
2. **Risveglio**: ogni Leader non ancora Risvegliato con **Vita ≤ 2** (cioè almeno 3 Vite perse) si gira sul lato Risvegliato. Se succede a entrambi, prima quello del giocatore attivo. Il Risveglio ha effetto immediato (Forza, massimo di Guardia, abilità) anche a metà turno o a metà del turno avversario.
3. **Massimo di Guardia**: la Guardia in eccesso si scarta.
4. Lo stato **Alle Corde** (§9.1) è derivato e si legge sempre dallo stato corrente, con il numero di turno del giocatore attivo **in quel momento**; non è uno stato persistente e non serve aggiornarlo. Colpo finale e Ultimo respiro non lo leggono dallo stato corrente ma dall'istantanea (§6.1, passo 2).

### 7.5 Trigger
Le abilità che iniziano con "quando…" o "a fine turno" sono **trigger**. Non usano una pila: si risolvono nel punto fisso indicato dalla sequenza (§8) o dalla fase (§6). Se più trigger scattano nello stesso punto, si risolvono prima tutti quelli del giocatore attivo, nell'ordine che sceglie, poi quelli del difensore, nell'ordine che sceglie. Un trigger "puoi…" è facoltativo (decisione del controllore).

**I trigger del passo 9 guardano indietro**: "quando sconfigge" e "dopo il combattimento" scattano anche se la loro fonte è stata sconfitta in quello stesso combattimento (es. Bastione Vivente che pareggia e viene sconfitto insieme all'attaccante pesca comunque). I trigger "quando…" valgono in qualsiasi turno, salvo che il testo dica "nel tuo turno".

---

## 8. Combattimento in 9 passi

Un attacco è un'azione della fase principale. Durante i passi 1–9 nessuno può agire, tranne il difensore ai passi 3 e 5 e i controllori dei trigger ai passi 2, 4 e 9.

**Attaccante legale**: un tuo personaggio **Pronto** che non ha già attaccato in questo turno (salvo Rinnovo), e che, se è un'Unità, non è entrato in questo turno (salvo Assalto). Nessun personaggio attacca nel turno 1 del proprio controllore.
**Bersaglio legale**: il **Leader avversario** (sempre) oppure un'**Unità avversaria Esposta**.

### Passo 1 — Dichiarazione
Il giocatore attivo sceglie un attaccante legale e un bersaglio legale. L'attaccante diventa **Esposto** e si registra che ha attaccato in questo turno.

### Passo 2 — Trigger "quando attacca"
Si risolvono i trigger "quando attacca" (es. Vesh), secondo §7.5.

### Passo 3 — Intercetto (difensore, facoltativo)
Il difensore può scegliere **una** sua Unità **Pronta** con **Scudo**. Quell'Unità diventa **Esposta** e diventa il nuovo bersaglio.
- Si può intercettare **qualsiasi** attacco: contro il Leader o contro un'Unità.
- Un'Unità intercetta al massimo una volta per attacco. Poiché intercettare espone, di norma intercetta una sola volta per turno; può farlo di nuovo solo se un effetto la rende Pronta (es. Muro di Scudi).
- Un intercettore Esposto resta **bersaglio legale** degli attacchi successivi dello stesso turno.

### Passo 4 — Trigger "quando intercetta"
Si risolvono i trigger "quando intercetta" (es. Sentinella del Guado: la Guardia ottenuta è già spendibile al passo 5 di questo stesso attacco).

### Passo 5 — Finestra di reazione (difensore, facoltativa)
La finestra si apre a **ogni** attacco, qualunque sia il bersaglio. Il difensore può usare **una** reazione se non ha esaurito il suo **limite di reazioni** per questo turno avversario:
- limite = **1** per turno avversario *(default; variante V1 al §16)*;
- limite = **2** se l'**istantanea** del Ripristino di questo turno (§6.1, passo 2) dice che il suo Leader era **Alle Corde all'inizio del turno** (**Ultimo respiro**). Un Leader portato Alle Corde durante questo turno non ottiene Ultimo respiro fino al turno avversario successivo.

Si conta l'**uso**, non la finestra: lasciar passare una finestra non consuma il limite. Una reazione è **una** tra:
- **Parata**: spendi **k ≥ 1** Guardia (k a scelta, fino alla Guardia disponibile); il bersaglio ottiene **+2 × k** al valore di difesa per questo combattimento (+3 × k se il Leader del difensore lo prevede, es. Maera Risvegliata);
- giocare **una carta Reazione** dalla mano o dalle Cicatrici, pagandone il costo in Guardia;
- usare l'**abilità di Reazione del proprio Leader**, se il Leader è Pronto, pagandone il costo.

L'attaccante non risponde mai. Intercetto e reazione si possono usare entrambi sullo stesso attacco.

### Passo 6 — Confronto
Se l'attaccante o il bersaglio non è più in gioco, il combattimento termina senza confronto: si passa al passo 8. Altrimenti si confrontano la Forza corrente dell'attaccante (Fa) e il valore di difesa corrente del bersaglio (Db):

| Attaccante | Bersaglio | Esito |
|---|---|---|
| Unità | Unità | Se Fa > Db è sconfitto il bersaglio; se Fa < Db è sconfitto l'attaccante; se Fa = Db sono sconfitti **entrambi**. |
| Leader | Unità | Se Db ≤ Fa l'Unità è sconfitta; altrimenti **non succede nulla**. Il Leader non è mai sconfitto. |
| Unità o Leader | Leader | Se Fa ≥ Tempra corrente (Db), l'attacco **va a segno**; altrimenti non succede nulla. L'attaccante non è mai sconfitto. |

### Passo 7 — Esiti
1. Le Unità sconfitte vanno negli Scarti (perdono bonus e contatori).
2. Se l'attacco è **andato a segno** sul Leader avversario:
   - se l'istantanea del Ripristino (§6.1) dice che quel Leader era **Alle Corde all'inizio di questo turno**, il giocatore attivo **vince la partita** (colpo finale);
   - altrimenti quel Leader **perde 1 Vita** (§9.2), salvo Saldo.

### Passo 8 — Controlli di stato
Si eseguono i controlli di stato (§7.4). Le Cicatrici appena create sono subito utilizzabili (anche come Reazione negli attacchi successivi dello stesso turno, se il limite di reazioni lo consente); un Risveglio avvenuto qui vale già per gli attacchi successivi.

### Passo 9 — Trigger "quando sconfigge" e "dopo il combattimento"
Si risolvono, secondo §7.5, i trigger "quando sconfigge" (es. Bastione Vivente, Matriarca del Branco) e "dopo il combattimento" (es. Muro di Scudi: l'intercettore torna Pronto). Questi trigger guardano indietro: scattano anche se la loro fonte è stata sconfitta in questo combattimento (§7.5). Poi scadono gli effetti "per questo combattimento" e si eseguono i controlli di stato. Il giocatore attivo torna alla fase principale.

**Riepilogo per il simulatore**: le decisioni del difensore per attacco sono al massimo due (intercettare: sì/no e con quale Unità; reagire: nessuna / Parata con k / quale Reazione / abilità del Leader). Le decisioni dei trigger "puoi" e dell'ordine dei trigger sono del rispettivo controllore.

---

## 9. Vita, Cicatrici, Risveglio — vittoria e anti-stallo

### 9.1 Alle Corde
Un Leader è **Alle Corde** se:
- ha **0 Vite**; oppure
- (Clessidra) il numero di turno del giocatore attivo è **≥ 13** e il Leader ha **1 Vita**.

Alle Corde si valuta **sempre con il numero di turno del giocatore attivo in quel momento**: non è uno stato che un Leader "acquisisce" e conserva.
*Esempio:* il Leader di G2 ha 1 Vita. All'inizio del turno 13 di G1 è Alle Corde (l'istantanea di G1 lo registra: un colpo a segno di G1 in quel turno è un colpo finale). Nel turno successivo di G2, che è il turno 12 di G2, lo stesso Leader con 1 Vita **non** è Alle Corde; lo torna a essere nel turno 14 di G1.

### 9.2 Perdere Vita
- Quando un Leader perde 1 Vita, la carta in cima alla sua pila Vita va **a faccia in su** tra le sue **Cicatrici**.
- **Saldo**: in uno stesso turno un Leader non può perdere più di **2 Vite** (da qualsiasi fonte: attacchi, costi, mazzo vuoto). Con la **Clessidra**, se il numero di turno del giocatore attivo è **≥ 10**, il Saldo è **3**. Le perdite oltre il Saldo vengono ignorate. Unica eccezione: le perdite del **Crepuscolo terminale** (§9.6) non sono soggette al Saldo e non contano per esso. Le perdite subite nel tuo stesso turno (es. Patto di Sangue, mazzo vuoto) contano per il Saldo di quel turno. Il conteggio si azzera all'inizio di ogni turno.
- Un Leader con **0 Vite** non può perdere altre Vite: ogni ulteriore perdita è ignorata. Su un Leader a 0 Vite **solo un attacco** può chiudere la partita (colpo finale, §9.5).
- Vite perse = Vita iniziale − Vita attuale.

### 9.3 Costi in Vita
Se un effetto chiede di perdere Vita **come costo** e quella perdita non può avvenire per intero (Saldo raggiunto, Vita 0, o il testo vieta di scendere sotto una soglia), il costo non è pagabile e la carta/abilità **non può essere giocata** (è esclusa dalle azioni legali).

### 9.4 Mazzo vuoto
Se devi pescare e il mazzo è vuoto, invece di pescare perdi 1 Vita (soggetta al Saldo). Se in quel momento il tuo Leader ha già **0 Vite**, **perdi la partita**. Ogni pesca mancata si valuta separatamente.

### 9.5 Condizioni di vittoria e sconfitta
Nel set base esistono solo queste:
1. **Colpo finale**: vinci se un tuo attacco va a segno sul Leader avversario e quel Leader era Alle Corde **all'inizio del tuo turno** (istantanea presa al passo 2 del Ripristino, §6.1, dopo l'aggiornamento del numero di turno e prima di ogni altro effetto). Portare un Leader a 0 non basta: l'avversario ha sempre un turno intero per reagire.
2. **Mazzo vuoto** su un Leader a 0 Vite (§9.4): quel giocatore perde.
3. **Crepuscolo terminale** (§9.6): dal tuo turno 15, se al passo 3 del tuo Ripristino il tuo Leader è Alle Corde, perdi.
4. Simultaneità: perde il giocatore attivo (§7.4).

Non esistono patte, vittorie ai punti o vittorie alternative.

### 9.6 Clessidra (anti-stallo)
La Clessidra sostituisce il Crepuscolo della bozza: i primi due gradini non tolgono Vita, **aprono il finale**; il terzo è un limite duro.
- Dal turno **10** del giocatore attivo: Saldo **3** (§9.2).
- Dal turno **13** del giocatore attivo: un Leader con **1 Vita** è Alle Corde (§9.1), quindi un colpo a segno su un Leader che aveva 1 Vita all'inizio di quel turno è un colpo finale.
- **Crepuscolo terminale** — dal tuo turno **15**, al passo 3 del tuo Ripristino (§6.1): se il tuo Leader è Alle Corde, **perdi la partita**; altrimenti il tuo Leader perde **2 Vite**, non soggette al Saldo e non conteggiate per esso (possono causare il Risveglio).

**Garanzia di durata.** Poiché dal turno 13 un Leader con 1 Vita è già Alle Corde, ogni giocatore perde al più tardi:
- al suo turno **15** se a quel Ripristino ha ≤1 Vita;
- al suo turno **16** se ne ha 2 o 3;
- al suo turno **17** se ne ha ancora 4 o 5 (caso limite di un Leader quasi mai colpito).

Ogni partita quindi termina al più tardi al turno 17 di uno dei due giocatori, e di norma al turno 15–16: è il parametro più vicino al vincolo 5–15 compatibile con la maggioranza del round 3 (variante V3 al §16 per anticipare al turno 14). Il mazzo vuoto (§9.4) non è più la garanzia di terminazione: arriverebbe solo verso il turno 30.

### 9.7 Cicatrici
- Le Cicatrici sono pubbliche: entrambi i giocatori le vedono sempre.
- **Reazioni dalle Cicatrici**: una carta Reazione tra le tue Cicatrici si può giocare come se fosse in mano (§8, passo 5); poi va negli Scarti.
- **Rimarginare** (§10.2) riporta una Cicatrice in mano.
- **Furia N**: un effetto con Furia N è attivo finché hai **almeno N Cicatrici** (presenti in questo momento). Rimarginare e le Reazioni giocate dalle Cicatrici abbassano il conteggio.

### 9.8 Risveglio
- Quando il tuo Leader ha perso **almeno 3 Vite** (Vita ≤ 2), al controllo di stato successivo si gira sul lato **Risvegliato**: Forza 4, Tempra 5, massimo di Guardia 3, abilità del lato Risvegliato.
- Succede **una volta per partita** ed è permanente. Il numero di Cicatrici presenti è irrilevante per il Risveglio.
- Lo stato (Pronto/Esposto), le infusioni e i bonus in corso si conservano.
- Non esiste Risveglio a tempo nel nucleo (leva di riserva, §16.4).

---

## 10. Il Leader in azione

### 10.1 Attacco del Leader
Il Leader attacca come un personaggio (§8) con la sua Forza (3, Risvegliato 4). Per mettere a segno un colpo sul Leader avversario (Tempra 5) deve essere infuso di almeno 2 Brace (1 da Risvegliato). Contro le Unità Esposte è una rimozione senza rischio: sconfigge un'Unità con Forza ≤ la sua e non è mai sconfitto.

### 10.2 Rimarginare (abilità ⟳ di ogni Leader)
> **⟳, 1 Brace**: metti in mano una Cicatrice a tua scelta. Massimo 1 volta per turno.

- Il limite di 1 volta per turno vale anche se un effetto rende di nuovo Pronto il Leader.
- È un'abilità ⟳ stampata (implicitamente) su ogni Leader: il Leader deve essere **Pronto** e diventa **Esposto**.
- Conseguenza: in un turno il Leader **o attacca o Rimargina** (o usa un'altra ⟳), mai entrambe; inoltre un Leader Esposto non può usare la sua abilità di Reazione nel turno avversario.
- È legale anche con 8 o più carte in mano: l'eccesso si scarta nella Fine.

---

## 11. Compensazione del primo giocatore

- **Nessun giocatore attacca nel proprio turno 1** (né con Unità, né con il Leader, né con Assalto).
- G1 **non pesca** nel suo turno 1.
- G2 riceve la **Scintilla** (§5.5).
- Mano iniziale: **5 carte per entrambi** *(default della variante V2, §16)*.
- Obiettivo di taratura: G1 vince il 48–52% dei mirror simulati, per ogni archetipo.
- Leve di riserva, nell'ordine: mano di G2 a 6 (V2); Scintilla che dà anche 1 Guardia; Fornace di G1 a −1 al turno 1; Fulcro (modulo, §17).

---

## 12. Colori e parole chiave

### 12.1 Colori
| Colore | Filosofia | Parole chiave principali | Combo previste |
|---|---|---|---|
| **Rosso** | Pressione, tutta la Brace in Forza | Assalto, Infuso, Rinnovo | + Verde (Infuso + Bracconiere), + Nero (Furia = Forza senza Brace) |
| **Blu** | Difesa, Guardia, contrattacco | Scudo, Reazioni | + Nero (Reazioni dalle Cicatrici), + Verde (chi attacca si espone e viene cacciato) |
| **Nero** | Ferite come potere | Furia, Cicatrici, costi in Vita | + Rosso (picchi di Forza), + Blu (sopravvivere Alle Corde) |
| **Verde** | Caccia agli Esposti | Bracconiere, effetti che espongono, ⟳ | + Blu, + Rosso |
| **Neutrale** | Collante tra archetipi | qualsiasi | tutti |

### 12.2 Parole chiave (ognuna compare in almeno due colori)
- **Assalto**: questa Unità può attaccare nel turno in cui entra (non nel turno 1 del controllore).
- **Scudo**: questa Unità può intercettare (§8, passo 3).
- **Infuso: [effetto]**: l'effetto scatta quando il controllore esegue l'azione di **infondere** su questa Unità (non per Brace spostata). "La prima volta… in un turno" si legge sul contatore di infusione.
- **Furia N: [effetto]**: attivo finché hai almeno N Cicatrici.
- **Bracconiere +X**: questa Unità ha +X Forza al passo 6 se il bersaglio corrente è un'**Unità Esposta** (vale anche contro un intercettore, che diventa Esposto intercettando).
- **Rinnovo**: questa Unità può attaccare una seconda volta in questo turno anche se è Esposta; resta Esposta. Al massimo un attacco aggiuntivo per Unità per turno.
- **⟳** (simbolo di costo): usare l'abilità rende Esposto il personaggio; richiede che sia Pronto.

### 12.3 Carte d'esempio v0.1 (testi corretti)
Formato: **Nome** — costo · tipo · Forza · testo. I valori di Muro di Scudi, Grido e della Reazione di Maera sono provvisori (ritarati per la Parata scalabile: ogni Reazione deve battere una Parata di pari Guardia; *parametri*).

**Leader** (tutti F3 / Tempra 5 / Vita 5; Risvegliati F4 / Tempra 5)
- **Arden, Fabbro di Guerra** (Rosso/Verde). Base: la seconda volta che infondi in uno stesso personaggio in un turno, quel personaggio ottiene +1 Forza aggiuntiva fino a fine turno. Risvegliato: le tue Unità con Assalto hanno +1 Forza.
- **Maera, Custode del Passo** (Blu/Nero). Base, Reazione: spendi 1 Guardia, l'attaccante ha −3 Forza per questo combattimento. Risvegliato: la tua Parata dà +3 per ogni Guardia spesa invece di +2.
- **Sorella Vey, la Segnata** (Nero/Rosso). Base: le Cicatrici che Rimargini continuano a contare per la tua Furia fino a fine turno. Risvegliato: una volta per turno, Rimarginare costa 0 Brace (resta ⟳).
- **Thorn, Voce del Branco** (Verde/Blu). Base: ⟳, 2 Brace: un'Unità avversaria con costo ≤2 diventa Esposta. Risvegliato: le tue Unità con Bracconiere hanno +1 Forza.

**Rosso**
- **Scudiera di Brace** — 1 · Unità · F2 · Assalto. Infuso: la prima volta che infondi in lei in un turno, +1 Forza aggiuntiva fino a fine turno.
- **Carica della Fornace** — 2 · Tattica · Una tua Unità con contatore di infusione ≥2 ottiene Rinnovo fino a fine turno.
- **Vesh, Lama Rovente** — 4 · Unità · F4 · Assalto. Quando attacca, puoi scegliere un'altra tua Unità: il suo contatore di infusione si sposta su Vesh, e con esso +1 Forza per ogni Brace del contatore. Non è infondere. Gli altri bonus dell'altra Unità (es. Infuso di Scudiera, bonus aggiuntivo di Arden) restano dove sono e scadono normalmente.

**Blu**
- **Sentinella del Guado** — 2 · Unità · F3 · Scudo. Quando intercetta, ottieni 1 Guardia (fino al massimo di Guardia).
- **Muro di Scudi** — 1 Guardia · Reazione · Il bersaglio ottiene +4 per questo combattimento. Dopo il combattimento, se il bersaglio è un'Unità che ha intercettato ed è ancora in gioco, torna Pronta.
- **Il Bastione Vivente** — 5 · Unità · F6 · Scudo. Quando sconfigge in combattimento un'Unità attaccante, pesca 1 carta (anche se viene sconfitto nello stesso combattimento, §7.5). *(Carta invariata: è la leva di riserva a essere riformulata, variante V5.)*

**Nero**
- **Penitente delle Mille Ferite** — 2 · Unità · F1 · Furia 2: +3 Forza.
- **Patto di Sangue** — 1 · Tattica · Costo aggiuntivo: il tuo Leader perde 1 Vita. Non puoi giocarla se il tuo Leader ha 1 Vita o meno. Pesca 1 carta.
- **Grido dalla Cicatrice** — 1 Guardia · Reazione · L'attaccante ha −3 Forza per questo combattimento; −5 invece se la giochi dalle Cicatrici.

**Verde**
- **Lince del Sottobosco** — 2 · Unità · F2 · Bracconiere +2.
- **Esca** — 1 · Tattica · Un'Unità avversaria con costo ≤3 diventa Esposta.
- **Matriarca del Branco** — 5 · Unità · F5 · Una volta per turno, in qualsiasi turno, quando una tua Unità sconfigge un'Unità Esposta (anche un attaccante, intercettando), pesca 1 carta.

**Neutrali**
- **Recluta del Crocevia** — 1 · Unità · F1 · Scudo. Quando entra, se hai almeno 2 Cicatrici, ottiene +1 Forza permanente.
- **Lanterna del Pellegrino** — 2 · Reliquia · Il tuo massimo di Guardia aumenta di 1.
- **Colpo Mirato** — 3 · Tattica · Sconfiggi un'Unità Esposta con Forza ≤4.

---

## 13. Leggi di design (vincolanti per chi scrive carte)

1. Nessuna carta annulla un'altra carta o vieta di giocare. Le Reazioni **modificano** un combattimento, non annullano carte; l'attaccante non risponde mai.
2. Niente scarto forzato dalla mano avversaria.
3. Nessuna distruzione o riduzione della Fornace avversaria.
4. Nessun effetto impedisce a un personaggio di tornare Pronto per più di 1 turno (niente lock oltre un round).
5. Nessuna moneta o dado che decide l'esito dopo una scelta: la casualità sta solo nella pescata.
6. Una carta comune ha al massimo una parola chiave e una frase di testo.
7. La rimozione economica (costo ≤3) colpisce solo Unità **Esposte**.
8. Gli effetti che espongono hanno come bersaglio solo Unità, mai il Leader.
9. Ogni parola chiave compare in almeno due colori; le Neutrali fanno da collante.
10. **Risposte agli Scudo**: ogni colore ha almeno una risposta comune agli Scudo e ai muri (esporre, ignorare lo Scudo o colpire chi intercetta); almeno 3 colori su 4, più le Neutrali, hanno effetti "Esponi" economici.
11. Ogni testo deve poter essere scritto nel simulatore senza casi speciali: costi non pagabili rendono l'azione illegale; i trigger hanno un punto fisso nella sequenza.

---

## 14. Glossario

| Termine | Definizione |
|---|---|
| **Accantonare** | Nella Fine del tuo turno, convertire la Brace non usata in Guardia, fino al massimo di Guardia. |
| **Alle Corde** | Leader con 0 Vite; dal turno 13 del giocatore attivo anche con 1 Vita (§9.1). Si valuta con il numero di turno del giocatore attivo in quel momento. |
| **Andare a segno** | Un attacco al Leader la cui Forza è ≥ della Tempra corrente del Leader bersaglio al passo 6. |
| **Attaccante legale / bersaglio legale** | §8. |
| **Brace** | Risorsa del turno, pari alla Fornace; si spende, si infonde o si accantona. |
| **Cicatrice** | Carta Vita persa, a faccia in su, pubblica. |
| **Clessidra** | Anti-stallo: Saldo 3 dal turno 10, Alle Corde a 1 Vita dal turno 13, Crepuscolo terminale dal turno 15. |
| **Crepuscolo terminale** | Dal tuo turno 15, nel Ripristino: se il tuo Leader è Alle Corde perdi, altrimenti perde 2 Vite fuori dal Saldo (§9.6). |
| **Istantanea Alle Corde** | Registrazione, al passo 2 del Ripristino, dello stato Alle Corde del Leader avversario; vale per tutto il turno (colpo finale, Ultimo respiro). |
| **Colpo finale** | Attacco a segno su un Leader che era Alle Corde all'inizio del turno dell'attaccante: vittoria. |
| **Contatore di infusione** | Brace infusa in un personaggio in questo turno; si azzera nella Fine. |
| **Controlli di stato** | Verifiche automatiche di §7.4. |
| **Difensore** | Il giocatore non attivo. |
| **Esposto / Esporre** | Stato di un personaggio che ha agito; §7.2. |
| **Fornace** | Livello che cresce di 1 per turno fino a 8 e determina la Brace. |
| **Forza** | Valore di attacco di un personaggio e valore di difesa di un'Unità. |
| **Furia N** | Effetto attivo con almeno N Cicatrici presenti. |
| **Giocatore attivo** | Il giocatore di cui è il turno. |
| **Guardia** | Brace accantonata, spendibile solo nel turno avversario per le reazioni. |
| **Infondere** | Pagare 1 Brace per +1 Forza fino a fine turno a un tuo personaggio. |
| **Intercetto** | Un'Unità Pronta con Scudo diventa il nuovo bersaglio di un attacco e si espone. |
| **Limite di reazioni** | 1 per turno avversario; 2 con Ultimo respiro (istantanea). |
| **Massimo di Guardia** | Tetto unico della riserva di Guardia: 2, 3 da Risvegliato, +1 per Lanterna. |
| **Numero di turno** | Quanti turni propri ha iniziato un giocatore. |
| **Parata** | Reazione: spendi k Guardia, il bersaglio ha +2k al valore di difesa. |
| **Personaggio** | Unità o Leader. |
| **Pronto** | Stato di base: può attaccare, intercettare (se ha Scudo), usare ⟳ e Reazioni; un'Unità Pronta non è attaccabile. |
| **Reazione** | Uso della finestra del passo 5: Parata, carta Reazione o abilità di Reazione del Leader. |
| **Rimarginare** | Abilità ⟳ del Leader: 1 Brace, una Cicatrice in mano; massimo 1 volta per turno. |
| **Risveglio** | Il Leader si gira sul lato Risvegliato quando ha Vita ≤ 2; una volta per partita. |
| **Saldo** | Massimo di Vite che un Leader può perdere in un turno: 2 (3 dal turno 10). |
| **Scintilla** | Segnalino di G2: una volta per partita, +1 Brace. |
| **Sconfiggere** | Mandare un'Unità negli Scarti per esito di combattimento o effetto. |
| **Tempra** | Valore di difesa del Leader: 5. |
| **Trigger** | Abilità "quando…"/"a fine turno"; ordine di §7.5. |
| **Turno** | Sempre il turno del giocatore attivo. |
| **Ultimo respiro** | Limite di reazioni 2 per il difensore il cui Leader era Alle Corde secondo l'istantanea del turno in corso. |
| **Valore di difesa** | Forza (Unità) o Tempra (Leader) del bersaglio. |
| **Vite perse** | Vita iniziale − Vita attuale; determina il Risveglio. |

---

## 15. Parametri numerici v0.1

| Parametro | Valore | Note |
|---|---|---|
| Carte nel mazzo | 40 | Copie per nome: max 3 |
| Mano iniziale | 5 (G1) / 5 (G2) | Variante V2 |
| Mulligan | 1 volta, fino a 3 carte in fondo | |
| Vita iniziale | 5 | |
| Leader: Forza / Tempra | 3 / 5 | Risvegliato: 4 / 5 |
| Soglia di Risveglio | 3 Vite perse (Vita ≤ 2) | |
| Fornace | +1 per turno, max 8 | Parte da 0 |
| Infusione | +1 Forza per Brace | Nessun tetto |
| Massimo di Guardia | 2 (3 Risvegliato) | +1 per Lanterna |
| Parata | +2 al valore di difesa per Guardia | Maera Risvegliata +3 (picco segnalato, leva §16.4) |
| Limite di reazioni | 1 per turno avversario | 2 con Ultimo respiro (letto dall'istantanea); variante V1 |
| Reazione Base di Maera | 1 Guardia, −3 | Provvisorio |
| Muro di Scudi | 1 Guardia, +4 | Provvisorio |
| Grido dalla Cicatrice | 1 Guardia; −3 dalla mano, −5 dalle Cicatrici | Provvisorio; valore dalla mano: variante V6 |
| Saldo | 2 Vite per turno | 3 dal turno 10 (Clessidra) |
| Alle Corde | 0 Vite | 1 Vita dal turno 13 (Clessidra) |
| Crepuscolo terminale | dal turno 15: Alle Corde = sconfitta, altrimenti −2 Vite fuori Saldo | Variante V3; fine garantita entro il turno 17 |
| Contatore delle soglie della Clessidra | numero di turno del giocatore attivo | Variante V4 |
| Unità / Reliquie in gioco | max 5 / max 2 | |
| Limite di mano | 8 a fine turno | |
| Primo turno | nessuno attacca; G1 non pesca | |
| Scintilla | G2, +1 Brace, 1 volta | |
| Rimarginare | ⟳ del Leader, 1 Brace | Max 1 volta per turno |

---

## 16. Varianti da testare

### 16.1 Varianti con default (il dibattito non ha raggiunto 3 voti su 4)

**V1 — Reazioni: una per turno o una per attacco**
- **Default (in regolamento):** 1 reazione per turno avversario, Parata scalabile (+2 per Guardia), **Ultimo respiro** (2 reazioni se il tuo Leader era Alle Corde all'inizio del turno avversario). Sostenuto da A e dal critico; C lo accetta esplicitamente come compromesso.
- *Perché il default:* è l'unica versione già giocata al tavolo (le due partite della revisione) e quella che sia C sia il critico dichiarano accettabile; inoltre permette di introdurre le modifiche una alla volta, come chiesto da A.
- **Alternativa V1-b (B, C):** una reazione **per attacco**, pagata dal budget unico di Guardia (massimo 2, 3 Risvegliato); **ogni reazione costa almeno 1 Guardia** (le Reazioni da 0 passano a 1); Ultimo respiro non esiste come regola speciale, oppure (forma di B) "Alle Corde il massimo di Guardia sale di 1".
- **Esclusa da tutti:** reazione per attacco con Brace residua senza tetto (draw-go / hard-control).
- **Metrica di decisione:** attacchi al Leader fermati da una reazione 30–45%; rimonte 20–35%; mediana di durata 8–10; partite che arrivano al turno 13 <10%. Il critico adotterebbe V1-b solo se dà meno del 45% di attacchi fermati.

**V2 — Compensazione del secondo giocatore**
- **Default (in regolamento):** 5 carte iniziali per entrambi + Scintilla a G2.
- *Perché il default:* è l'unica opzione accettata da tre partecipanti (A, B, critico), ed è la più prudente dopo l'introduzione del "nessuno attacca nel turno 1".
- **Alternative:** 6 carte a G2 + Scintilla (B, critico); 6 carte a G2 senza Scintilla (C, A).
- **Metrica:** vittorie di G1 48–52% nei mirror, separate per archetipo (l'aggro Rosso è il caso critico).

**V3 — Parametri del Crepuscolo terminale** (round 3, punto a)
- **Deciso (3–1):** serve un limite duro a forma di Crepuscolo terminale (sconfitta se Alle Corde al Ripristino, altrimenti perdita di Vita), da **turno 15** (A, C, critico per la forma; A, B, critico per la soglia del turno 15).
- **Senza maggioranza:** quante Vite si perdono. A: 2 Vite soggette al Saldo; C e critico: 1 Vita fuori dal Saldo; B: nessuna perdita (dal turno 15 ogni Leader è Alle Corde).
- **Default (in regolamento): 2 Vite, fuori dal Saldo.** *Perché:* il vincolo dell'utente chiede partite che finiscano al turno 15 o subito dopo. Con 1 Vita il caso peggiore arriva al turno 19, con 2 Vite al turno 17. Il default combina il numero di A con la clausola "fuori dal Saldo" di C e del critico: è il parametro più vicino al vincolo che resti compatibile con la maggioranza. Nessuna opzione della maggioranza porta la fine garantita esattamente al turno 15.
- **Alternative:** 1 Vita fuori dal Saldo (C, critico); inizio al turno 14 (C); dal turno 15 ogni Leader è Alle Corde, con la Tempra che scende di 1 per turno come leva (B).
- **Metrica:** partite oltre il turno 15 <2% (C); ≥90% delle partite tra il turno 5 e il 15. Se si supera il 2%, anticipare al turno 14.

**V4 — Asimmetria della Clessidra** (round 3, punto b; 2–2)
- **Default (in regolamento): nessuna compensazione.** Tutte le soglie (10 / 13 / 15) si leggono sul numero di turno del giocatore attivo. Sostenuto da A e dal critico.
- *Perché il default:* è la regola più semplice, perché un solo contatore vale per tutte le soglie. Non ci sono ancora dati e il protocollo del §16.3 non ammette modifiche senza dati. Inoltre il Crepuscolo terminale colpisce per primo G1 e controbilancia il vantaggio.
- **Alternativa (B, C):** tutte le soglie si leggono sul numero di turno di G2 (i round completi).
- **Metrica:** vittorie di G1 nelle sole partite che arrivano al turno 10. Se superano il 52%, si adotta l'alternativa.

**V5 — Bastione contro la leva anti-Scudo** (round 3, punto d; 2–2: cambiare la carta contro cambiare la leva)
- **Default (in regolamento): si cambia la leva, non le carte.** Nuova forma della leva di riserva: "Unità con Scudo hanno Forza ≤ costo + 1" (C).
- *Perché il default:* C ha notato che anche Sentinella del Guado (2, F3, Scudo) viola la forma originale. Cambiare solo il Bastione (A, critico) lascerebbe quindi la leva incompatibile con il set, e la forma di B (solo costo ≤3) è violata anche lei da Sentinella. "≤ costo + 1" è l'unica formulazione compatibile con tutte le carte attuali (Recluta 1 ≤ 2, Sentinella 3 ≤ 3, Bastione 6 ≤ 6) e non richiede errata.
- **Alternative:** Bastione 5 · F5 con la leva "Forza ≤ costo" (A, critico; richiederebbe di cambiare anche Sentinella); leva limitata alle Unità con Scudo di costo ≤3 (B).
- **Metrica:** partite che arrivano all'anti-stallo nei matchup con mazzi da 5 o più Scudo. Allarme sopra il 15%: in quel caso si attiva la leva.

**V6 — Grido dalla Cicatrice, valore dalla mano** (round 3, punto c)
- **Deciso (3–1):** costo 1 Guardia (A, B, critico); −5 se giocata dalle Cicatrici (B, C, critico).
- **Default per il valore dalla mano: −3** (B e critico, 2 voti contro 1). *Perché:* è l'opzione con più sostenitori e batte comunque la Parata di pari costo (−3 contro +2).
- **Alternative:** −4 dalla mano e −6 dalle Cicatrici (A); 2 Guardia e −5 dalla mano (C).
- **Metrica:** quota di attacchi fermati da Grido rispetto alla Parata; win rate dei mazzi Nero; attacchi fermati complessivi 30–45%.

### 16.2 Test di controllo su punti decisi
Punti decisi, per cui almeno un partecipante ha chiesto un confronto nel simulatore. Il regolamento non cambia se il test conferma.

| Test | Regola in vigore | Confronto | Metrica |
|---|---|---|---|
| T1 | Leader F3 / Tempra 5 | Forza unica 4, colpo a segno solo con Forza **strettamente maggiore** | Vite perse da attacchi del Leader <40%; mediana 8–10 |
| T2 | Clessidra (10 / 13) + Crepuscolo terminale (15) | Crepuscolo della bozza (dal turno 10 il tuo Leader perde 1 Vita al Ripristino); oppure Clessidra a soglia unica al turno 12 (C) | Partite chiuse dall'anti-stallo <15%; partite oltre il turno 15 <2% |
| T3 | Rimarginare ⟳ | Riscossa (prima perdita di Vita del turno: una Cicatrice in mano gratis); Rimarginare base (1/turno, 1 Brace, senza ⟳) | Rimarginare usato <70% dei turni possibili; rimonte 20–35% |
| T4 | Ultimo respiro (in V1 default) | Nessuna correzione Alle Corde | Rimonte 20–35% |

### 16.3 Protocollo di introduzione (A, critico)
Le modifiche che rafforzano la difesa (Tempra 5, Parata scalabile, Ultimo respiro) vanno introdotte **in sequenza** nel simulatore: prima Tempra 5 da sola (insieme a "nessun attacco al turno 1" e alle correzioni di scrittura), poi la Parata scalabile, poi Ultimo respiro. A ogni passo: mediana 8–10, partite al turno 13 <10%, partite che arrivano all'anti-stallo <15% nei matchup con mazzi da 5 o più Scudo. Le varianti strutturali (§17) si testano solo dopo che il nucleo è stabile, una per volta.

### 16.4 Leve di riserva (non attive)
- **Risveglio a tempo**: anche all'inizio del tuo turno 7 (critico), 9 (A) o 10 (C), se i log mostrano attaccanti in vantaggio che rinunciano a colpire o mediane oltre 11.
- **Riscossa** (C) se le rimonte sono sotto il 20%.
- **Tetto all'infusione** +2 per personaggio (B, round 1) se l'aggro Rosso supera il 55%.
- **Unità con Scudo con Forza ≤ costo + 1** (forma di default della variante V5) se emerge lo stallo da Scudo.
- **Maera Risvegliata**: con 3 Guardia la Parata porta la Tempra a 14 (con Ultimo respiro, due attacchi bloccati). Se il simulatore mostra un picco, la sua Parata passa da "+3 per Guardia" a "+1 Forza per Guardia in più" (critico, round 3). Metrica: win rate di Maera e attacchi fermati quando è Risvegliata.
- Scintilla che dà anche 1 Guardia; Fornace di G1 a −1 al turno 1.

### 16.5 Limite tecnico del simulatore
Non è una regola di gioco: con il Crepuscolo terminale ogni partita finisce entro il turno 17. Se una partita simulata supera il turno 17 per entrambi i giocatori, c'è un errore di implementazione: va interrotta e registrata come **"non conclusa"** (non patta).

---

## 17. Moduli futuri (fuori dal nucleo)

1. **Campo di battaglia leggero** — primo modulo da testare dopo la stabilizzazione del nucleo. Ogni giocatore porta 1 carta Campo; all'inizio è attivo quello di G2; chi si Risveglia per primo può sostituirlo con il proprio (proposta A). Effetti sempre simmetrici, mai di negazione. Metriche: % di turni con ≥3 Unità Pronte che non attaccano, % di partite chiuse dall'anti-stallo, con e senza Campo.
2. **Due zone contese con Fronte a inerzia** (formato "Assedio", proposta A) — candidato per un'espansione o un formato alternativo, da riproporre se lo stallo da Scudo risulta strutturale.
3. **Round condiviso ad azioni alternate + Fulcro** (proposta C) — variante strutturale da provare solo se G1 resta fuori dal 48–52% con le leve fisse o se i log mostrano troppi turni avversari senza decisioni. Richiede di riscrivere l'Esposizione ("fino alla fine del prossimo round") e la sequenza di combattimento. Metriche: decisioni del difensore per round, vittorie di G1, margine IA forte/semplice, azioni legali medie, % di attacchi lanciati come ultima azione.
4. **Colpo finale legato al Fulcro** — esiste solo insieme al modulo 3.

**Respinti dal dibattito** (non riproporre senza dati nuovi): vittoria a punti/Gloria e patte; Clessidra a punti di C; requisiti d'Aspetto (pip di colore); Guardia/Brace non spesa senza tetto.

---

## Registro modifiche

| Versione | Data | Modifiche |
|---|---|---|
| v0.1 | 2026-10-07 | Prima stesura consolidata dai round 1–2 e dalla revisione critica. |
| v0.1 (ratificata) | 2026-10-07 | Round 3: ratificata da A, B, C e critico. Il §9.5 ora rimanda all'istantanea del passo 2 del Ripristino (§6.1), come segnalato da tutti e 4. Aggiunto il **Crepuscolo terminale** dal turno 15 (§6.1, §9.5, §9.6; V3) e tolta la frase "terminazione garantita dal mazzo vuoto". Le soglie della Clessidra restano sul turno del giocatore attivo (V4). Leva anti-Scudo riformulata come "≤ costo + 1", Bastione invariato (V5). Grido: 1 Guardia, −3 dalla mano e −5 dalle Cicatrici (V6). Muro di Scudi +4 (B). Reazione di Maera −3 (C). Testo di Vesh precisato. Chiuse le 7 ambiguità del critico: A1 Vesh; A2 i trigger del passo 9 guardano indietro (§7.5); A3 Ultimo respiro letto dall'istantanea; A4 Alle Corde legato al turno attivo, con esempio (§9.1); A5 Matriarca in qualsiasi turno; A6 picco di Maera Risvegliata come leva (§16.4); A7 Rimarginare al massimo 1 volta per turno (§10.2). Il limite tecnico del simulatore scende a 17 turni. |
