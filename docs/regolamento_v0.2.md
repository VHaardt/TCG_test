# CICATRICI — Regolamento v0.2

| Campo | Valore |
|---|---|
| Versione | v0.2 (nucleo) |
| Data | 2026-10-08 |
| Stato | **ratificato dallo swarm (Q-013, 8/8 APPROVO); pilastri 2–3–4–6 in revisione, vedi pilastri** (`pilastri_design_v0.2.md`) |
| Fonte normativa | `swarm/questioni/Q-013_rework_nucleo_v0.2/esito.md`, sezione A "Specifica consolidata". Dati: `swarm/esperimenti/E-014/sintesi_r3.md` |
| Sostituisce | `regolamento_v0.1.md`. Le parti di v0.1 non toccate da Q-013 restano valide e sono riportate qui |

> Convenzioni. "Deve", "non può", "è illegale" sono vincolanti anche per il simulatore. I punti marcati **[default, aperto: Px]** sono regole in vigore scelte come default da un voto senza maggioranza: ognuno ha una variante con metrica nel §17. I nomi fra parentesi quadre, come [`tempra`], sono i parametri del simulatore (`sim/v02/config.py`, preset `V02`).

> **Cosa cambia da v0.1**
> 1. Componenti: solo carte, gemme di una sola specie e una carta-tracciato del round. Spariscono Fornace, contatori, Scintilla.
> 2. Pronto/Ruotato sostituisce Esposto: Ruotata vuol dire solo "ha agito" e non rende bersaglio. I tuoi personaggi si raddrizzano nel tuo Ripristino.
> 3. Si attacca sempre il Leader avversario; il difensore può opporre una sua Unità Pronta.
> 4. Combattimento in 6 passi: l'attaccante impegna gemme a vista, poi il difensore risponde con la Guardia (+2 per gemma) e al massimo una Reazione.
> 5. Tempra del Leader 4 su entrambi i lati.
> 6. Saldo e colpo finale si leggono dalle Cicatrici fresche: niente istantanea, niente contatore del Saldo.
> 7. Ultimo respiro diventa +1 Guardia Alle Corde; spariscono finestra e limite di reazioni.
> 8. Infondere sparisce ("se hai impegnato almeno N gemme"); le abilità di Reazione dei Leader sono statiche.
> 9. Esponi diventa Stanca, Intercetto diventa opposizione; lo Scudo vince i pareggi [aperto: P7].
> 10. G2 prende 1 gemma in più nei round 1 e 3 [aperto: P6].

---

## 1. Panoramica

CICATRICI è un gioco di carte collezionabili 1 contro 1. Ogni giocatore guida un **Leader**, sempre in gioco, e un mazzo di 40 carte.

- Per vincere devi portare il Leader avversario **Alle Corde** (0 Vite) e poi metterlo a segno con un attacco quando non ha **Cicatrici fresche**: è il **colpo finale** (§9). Le Cicatrici fresche di un turno si raddrizzano alla fine di quel turno, quindi l'avversario ha sempre un turno intero per reagire.
- Ogni Vita persa non sparisce: la carta Vita si gira a faccia in su e diventa una **Cicatrice**, che il giocatore ferito può riprendere in mano, giocare come Reazione o contare per la **Furia**. Dopo 3 Vite perse il Leader si **Risveglia**.
- La risorsa sono le **gemme**. Ogni turno prendi dalla scorta tante gemme di **Brace** quanto dice il tracciato del round. Le spendi per giocare carte, le **impegni** in un attacco, oppure, a fine turno, le metti sul Leader come **Guardia** per difenderti nel turno avversario.
- **Agire costa la difesa**: chi attacca, si oppone o usa un'abilità ⟳ si **ruota** e resta Ruotato fino al Ripristino del suo controllore. Un personaggio Ruotato non può opporsi né attaccare.
- I turni sono **chiusi**: c'è un solo giocatore attivo e non esiste una pila. Nel turno avversario il difensore decide in due punti fissi di ogni attacco: **opposizione** (C2) e **risposta** (C4).

Durata obiettivo: 5–15 round, mediana 8–10 (vedi pilastri). Misurata nel simulatore con le regole di questo documento: mediana 8 round, 0% di vittorie prima del round 5.

---

## 2. Componenti e costruzione del mazzo

### 2.1 Componenti fisici
Per giocare servono solo:
- **1 Leader per giocatore** (fuori dal mazzo), carta a due facce: lato **Base** e lato **Risvegliato**;
- **1 mazzo di 40 carte per giocatore**;
- **gemme** tutte uguali, in una **scorta comune** al centro del tavolo: circa 12 per giocatore, quindi circa 24 in tutto;
- **1 carta-tracciato del round** con **1 segnalino**, comune ai due giocatori.

Non servono altri segnalini, contatori o dadi. Gli stati si mostrano ruotando le carte (§7.2).

**La carta-tracciato del round** ha le caselle da 1 a 15 e riporta stampati:
- per ogni round, la Brace del round: min(round, 8);
- "round 1 e 3: G2 +1 gemma" **[default, aperto: P6]**;
- "10: Saldo 3";
- "13: Alle Corde a 1 Vita";
- "15: Crepuscolo".

### 2.2 Il Leader
Ogni Leader stampa: nome, 1 o 2 colori, **Forza**, **Tempra**, **Vita iniziale**, un'abilità sul lato Base e una sul lato Risvegliato.

Valori standard per tutti i Leader del set base [`leader_power`, `leader_power_awakened`, `tempra`, `life`, `guard_max`, `guard_max_awakened`]:

| | Forza | Tempra | Vita iniziale | Massimo di Guardia |
|---|---|---|---|---|
| Lato Base | 3 | **4** | 5 | 2 |
| Lato Risvegliato | 4 | **4** | — | 3 |

- **Forza**: il valore con cui il Leader attacca.
- **Tempra**: il valore che un attacco deve eguagliare o superare per andare a segno sul Leader.
- Il Risveglio dà +1 Forza e +1 al massimo di Guardia; la Tempra resta 4.

### 2.3 Regole di costruzione (invariate da v0.1)
- Esattamente 40 carte, al massimo **3 copie per nome**. Le carte del primo set non hanno nome: il limite vale per **ID** (es. ROS-007). Due ID con lo stesso testo sono carte diverse, ognuna con le sue 3 copie; se differenziarle lo decide chi scrive le carte (R-007 T-3).
- Ogni carta deve condividere almeno un colore col Leader oppure essere **Neutrale**.
- Colori del set base: Rosso, Blu, Nero, Verde (§12). Leader bicolori consigliati.
- Il mazzo non contiene carte-risorsa: la risorsa sono le gemme.
- Un mazzo che viola queste regole è illegale e non può essere usato.

---

## 3. Zone di gioco

### 3.1 Zone delle carte

| Zona | Visibilità | Ordine | Note |
|---|---|---|---|
| Mazzo | Nascosto a entrambi | Ordinato, segreto | Si pesca dalla cima |
| Mano | Nascosta all'avversario | — | Massimo 8 carte a fine turno (§6.4) |
| Vita | Nascosta a **entrambi** | Pila, segreta | Coperta sotto il Leader; si prende sempre la carta in cima |
| Cicatrici | **Pubblica** | Insieme non ordinato | Carte Vita perse, a faccia in su; ognuna è dritta o fresca (ruotata) |
| Campo | Pubblica | — | Il Leader, **massimo 5 Unità**, **massimo 2 Reliquie** |
| Scarti | Pubblica | Ordinato per arrivo | Unità sconfitte, Tattiche risolte, Reazioni usate, carte scartate |

- Le sole informazioni nascoste sono: la **mano** (all'avversario), l'**ordine del mazzo** e la **Vita** (a entrambi). Tutto il resto, gemme comprese, è pubblico.
- Giocare una sesta Unità o una terza Reliquia è illegale. Non esiste sostituzione.

### 3.2 Zone delle gemme
Ogni gemma in gioco sta in una di queste zone:

| Zona | Dove | Quando |
|---|---|---|
| **Scorta** | Al centro, comune ai due giocatori | Sempre |
| **Brace** | Davanti al giocatore | Si prende nel tuo Ripristino, si usa nel tuo turno |
| **Guardia** | Sulla carta Leader | Si forma nella tua Fine, si usa nel turno avversario |
| **Impegno** | Al centro dello scontro, scoperte | Solo durante uno scontro (§8) |

- **Spendere** una gemma vuol dire rimetterla nella scorta.
- Nessuna gemma va mai su un'Unità.
- L'impegno è chiamato anche "pugno", ma le gemme impegnate sono sempre scoperte.

---

## 4. Preparazione

In quest'ordine:
1. Si sceglie **a caso** il primo giocatore (G1); l'altro è il secondo giocatore (G2).
2. Ogni giocatore mette il Leader sul Campo, lato **Base**, **Pronto** (dritto).
3. Ogni giocatore mescola il mazzo e pesca **5 carte** [`hand` 5].
4. **Mulligan**, una sola volta, prima G1 poi G2: scegli da 0 a 3 carte della mano, mettile in fondo al mazzo nell'ordine che preferisci e pesca altrettante carte dalla cima [`mulligan_max` 3]. Il mazzo non si rimescola.
5. Ogni giocatore mette le prime **5 carte** del mazzo coperte sotto il Leader, senza guardarle: è la sua **Vita** [`life` 5].
6. Il segnalino del round va sulla casella **0** (prima della casella 1). Tutte le gemme sono nella scorta.
7. Inizia il turno di G1.

---

## 5. Risorse: gemme, Brace, Guardia e tracciato del round

### 5.1 Il tracciato del round
- Un **round** è un turno di G1 seguito da un turno di G2.
- Il segnalino avanza di 1 all'inizio di ogni turno di G1 (Ripristino, passo a). Il primo turno di G1 e il primo turno di G2 sono quindi il round 1.
- Tutte le soglie del gioco (Brace, Saldo 3, Alle Corde a 1 Vita, Crepuscolo) si leggono sul round del tracciato, uguale per i due giocatori.

### 5.2 Brace
- Nel tuo Ripristino prendi dalla scorta **min(round, 8)** gemme: è la tua Brace [`brace_max` 8].
- Se sei G2, nel **round 1** e nel **round 3** ne prendi **1 in più** **[default, aperto: P6; `scintilla_g2_gems` 1, `scintilla_extra_gems` 1, `scintilla_extra_round` 3]**.
- Nel tuo turno la Brace si usa in due modi:
  1. **spenderla** per pagare carte e abilità (le gemme tornano nella scorta);
  2. **impegnarla** in un tuo attacco (§8, C3): ogni gemma impegnata dà +1 alla Forza dell'attaccante, poi torna nella scorta.
- I costi in gemme di carte e abilità ⟳ si pagano **sempre con la Brace**: la Guardia si usa solo nell'impegno, nel turno avversario (§5.3) (R-007 T-5).
- Nella Fine la Brace non spesa diventa Guardia fino al massimo; il resto torna nella scorta (§5.3).

### 5.3 Guardia e massimo di Guardia
- **Formare la Guardia**: nella Fine del tuo turno sposti sulla carta Leader le gemme di Brace non spese, fino al **massimo di Guardia**; le altre tornano nella scorta.
- **Massimo di Guardia** = 2 sul lato Base, 3 sul lato Risvegliato, **più gli aumenti stampati sulle carte** (es. NEU-002; la carta dice il proprio tetto e se più copie si sommano), **+1 se il tuo Leader è Alle Corde** [`guard_max`, `guard_max_awakened`, `guard_alle_corde_bonus` 1].
- La Guardia si usa **solo nel turno avversario**, impegnandola in uno scontro (§8, C4): ogni gemma paga il costo di una Reazione oppure dà **+2** al valore di difesa del bersaglio (**Parata**) [`parata_per_gemma` 2].
- All'inizio del tuo Ripristino rimetti nella scorta la Guardia rimasta.
- Il massimo vale sempre. Se scende (per esempio lascia il gioco la carta che lo aumentava), la Guardia in eccesso torna nella scorta al controllo di stato successivo. Se sale nel turno avversario (per esempio col Risveglio), si alza solo il tetto: non ricevi gemme.

---

## 6. Struttura del turno

Il **giocatore attivo** è quello di cui è il turno; l'altro è il **difensore**. "Turno" indica sempre il turno del giocatore attivo. Ogni turno ha quattro fasi, in quest'ordine.

### 6.1 Ripristino
In quest'ordine:
- **(a)** Se sei G1, avanzi il segnalino del round di 1.
- **(b) Crepuscolo** (dal round 15): se il tuo Leader è Alle Corde, **perdi la partita**. Altrimenti il tuo Leader perde 2 Vite: le carte vanno tra le Cicatrici **dritte** e non contano per il Saldo (§9.3) [`crepuscolo_round` 15, `crepuscolo_loss` 2].
- **(c)** Rimetti nella scorta le tue gemme di Guardia.
- **(d)** **Raddrizzi i tuoi personaggi** (il Leader e le tue Unità).
- **(e)** Prendi dalla scorta la tua Brace: min(round, 8) gemme; se sei G2, nel round 1 e nel round 3 ne prendi 1 in più **[default, aperto: P6]**.
- **(f)** Controlli di stato (§7.4).

### 6.2 Pesca
Peschi 1 carta. **G1 non pesca nel round 1.** Se devi pescare e il mazzo è vuoto, vedi §9.6.

### 6.3 Fase principale
Ripeti "scegli un'azione legale, risolvila per intero, controlli di stato" finché decidi di terminare la fase. Le azioni sono, in qualsiasi ordine e quante volte vuoi:

| Azione | Costo | Note |
|---|---|---|
| Giocare un'Unità | gemme di Brace | **Entra Ruotata**; con Assalto entra Pronta. Massimo 5 Unità |
| Giocare una Reliquia | gemme di Brace | Massimo 2 Reliquie |
| Giocare una Tattica | gemme di Brace | Si risolve e va negli Scarti |
| Usare un'abilità ⟳ | ruotare la carta + quanto stampato | Legale solo se la carta è Pronta |
| **Rimarginare** | ⟳ del Leader + 1 Brace | Prendi in mano una tua Cicatrice **dritta** (§10.2) |
| Dichiarare un attacco | — | §8. **Nessuno attacca nel round 1** [`no_attack_round` 1] |
| Terminare la fase | — | — |

- Un'azione il cui costo non può essere pagato per intero è **illegale** (vale anche per i costi in Vita, §9.4).
- Un attacco, una volta dichiarato, si risolve per intero (C1–C6). Dopo ogni attacco si torna alla fase principale: puoi giocare carte, usare abilità e attaccare di nuovo con un altro personaggio Pronto.
- Le carte Reazione non si giocano mai nel tuo turno.

### 6.4 Fine
In quest'ordine:
- **(a)** Si risolvono gli effetti "a fine turno" (nel nucleo non ce ne sono).
- **(b) Guardia**: sposti sul tuo Leader le gemme di Brace non spese, fino al massimo di Guardia (§5.3); le altre tornano nella scorta.
- **(c)** **Tutte le Cicatrici fresche di entrambi i giocatori si raddrizzano.**
- **(d)** Limite di mano: se hai più di 8 carte in mano, scarti a tua scelta fino ad averne 8 [`hand_limit` 8]. Poi controlli di stato e il turno passa all'avversario.

---

## 7. Tipi di carta, stati e controlli di stato

### 7.1 Tipi di carta
- **Leader**: sempre in gioco; non può essere sconfitto, rimosso né stancato. Attacca con la propria Forza. È sempre il bersaglio di un attacco, salvo opposizione. Non può opporsi.
- **Unità**: costo, Forza, eventuali parole chiave e testo. Entra **Ruotata** (con Assalto entra Pronta). Può attaccare e opporsi solo se è Pronta.
- **Tattica**: effetto immediato, solo nella tua fase principale fuori da uno scontro; poi va negli Scarti.
- **Reazione**: si gioca solo nella risposta del difensore (§8, C4), dalla mano **o da una tua Cicatrice dritta**, pagando il costo con le gemme impegnate. Dopo l'uso va negli Scarti, anche se giocata dalle Cicatrici.
- **Reliquia**: permanente senza Forza; non è un personaggio e non può essere attaccata.
- **Personaggio**: un'Unità o un Leader.

### 7.2 Stati: Pronto e Ruotato
- Ogni carta in campo è **Pronta** (dritta) o **Ruotata**.
- Una carta si ruota quando **attacca**, quando **si oppone**, quando usa un'abilità **⟳** (incluso Rimarginare), oppure per un effetto **Stanca**.
- **Ruotata vuol dire solo "ha agito".** Essere Ruotata non rende bersaglio di un attacco e non protegge dalla Caccia (Q-018).
- Un personaggio Ruotato non può attaccare, opporsi né usare abilità ⟳.
- I tuoi personaggi si raddrizzano nel tuo Ripristino (§6.1 d), oppure prima se un effetto lo dice (per esempio Rinnovo).
- Ruotare una carta già Ruotata non ha effetto.
- Ogni **Cicatrice** è **dritta** o **fresca**. Una Cicatrice fresca si tiene ruotata; diventa dritta nella Fine del turno in cui è nata (§6.4 c).

### 7.3 Forza e valore di difesa
- La **Forza** corrente di un personaggio è la Forza stampata più i bonus attivi. Può scendere a 0 o sotto: non causa sconfitta da sola.
- Il **valore di difesa** del bersaglio è la Forza dell'Unità che si oppone oppure la Tempra del Leader, più i bonus dello scontro (Parata, Reazioni, effetti stampati).
- **Nessun modificatore sopravvive allo scontro.** I bonus del nucleo valgono "per questo scontro" oppure sono permanenti; non esistono bonus "fino a fine turno".

### 7.4 Controlli di stato
Si eseguono dopo ogni azione della fase principale, al passo C6 (d) di ogni scontro, dopo ogni trigger del passo C6 (e), alla fine del Ripristino e della Fine. In quest'ordine, ripetendo finché nulla cambia:
1. **Fine partita**: se un giocatore ha soddisfatto una condizione di sconfitta (§9.7), la partita finisce. Se succede a entrambi nello stesso momento, **perde il giocatore attivo**.
2. **Risveglio**: ogni Leader non ancora Risvegliato con **Vita ≤ 2** si gira sul lato Risvegliato (§9.8). Se succede a entrambi, prima quello del giocatore attivo.
3. **Massimo di Guardia**: la Guardia in eccesso torna nella scorta.

Lo stato **Alle Corde** (§9.1) si legge sempre dallo stato corrente: Vita e round. Non va registrato.

### 7.5 Trigger
Le abilità che iniziano con "quando…" o "a fine turno" sono trigger. Non c'è pila: si risolvono nel punto fisso indicato dalla sequenza (§8) o dalla fase (§6). Se più trigger scattano nello stesso punto, si risolvono prima quelli del giocatore attivo, nell'ordine che sceglie, poi quelli del difensore. Un trigger "puoi…" è facoltativo.

I trigger di C6 (e) ("quando sconfigge", "dopo lo scontro") guardano indietro: scattano anche se la loro fonte è stata sconfitta in quello stesso scontro (anche nella sconfitta reciproca, Q-015 S-9). Una carta che vuole scattare solo se la fonte resta in gioco lo dice.

*Esempio (R-007 T-6).* Un'Unità con Rinnovo, costo 3, attacca; il difensore si oppone e gioca BLU-025 ("L'attaccante ha −5 in questo scontro. Dopo lo scontro, se l'attaccante è un'Unità con costo ≤4, sconfiggila"). L'attaccante vince lo stesso e sconfigge l'Unità che si oppone. In C6 (e) si risolve prima il trigger del giocatore attivo (Rinnovo: l'attaccante si raddrizza), poi quello del difensore (BLU-025 lo sconfigge). L'Unità va negli Scarti: il Rinnovo si è risolto ma non le serve. Nessun ciclo.

---

## 8. Combattimento in 6 passi (C1–C6)

Un attacco è un'azione della fase principale. Lo **scontro** va da C1 a C6. Durante lo scontro nessuno agisce, tranne il difensore in C2 e C4, l'attaccante in C3 e i controllori dei trigger.

- **Attaccante legale**: un tuo personaggio **Pronto** (Leader o Unità). Nessuno attacca nel round 1.
- **Bersaglio**: **sempre il Leader avversario**, salvo opposizione (C2) o parola chiave di carta.

### C1. Dichiarazione
Scegli l'attaccante e **lo ruoti**. Si risolvono i trigger "quando attacca".

### C2. Opposizione (difensore, facoltativa)
Il difensore può ruotare **una** sua **Unità Pronta**: quell'Unità diventa il bersaglio. Un'Unità con Scudo si ruota come le altre. Se nessuno si oppone, il bersaglio resta il Leader. Si risolvono i trigger "quando si oppone".

### C3. Impegno dell'attaccante, a vista
L'attaccante sposta nell'impegno da 0 a tutte le sue gemme di Brace, **scoperte** [`pugno` sequenziale].

### C4. Risposta del difensore
Dopo aver visto l'impegno dell'attaccante, il difensore sposta nell'impegno da 0 a tutte le sue gemme di Guardia, e può giocare **al massimo una** carta Reazione presa dalla mano o da una sua Cicatrice **dritta**.
- **(a)** Le gemme del difensore pagano prima il costo della Reazione. Una Reazione si gioca solo se le gemme impegnate ne pagano il costo.
- **(b)** Ogni gemma restante del difensore dà **+2** al valore di difesa del bersaglio (**Parata**). L'**impegno** del difensore sono tutte le gemme che sposta in C4, compresa quella che paga la Reazione; la **Parata** sono quelle che restano dopo il costo. Le condizioni sulle gemme del difensore (Impeto da bersaglio, statiche dei Leader e delle carte) contano **solo la Parata** (Q-015 S-2). Per l'attaccante contano tutte le gemme impegnate.
- **(c)** Ogni gemma dell'attaccante dà **+1** alla sua Forza [`forza_per_gemma` 1].
- **(d)** Si risolve la Reazione. Si leggono le condizioni sulle gemme (**Impeto**, §12.2; per il difensore solo la Parata) e le abilità di Reazione dei Leader, che sono **statiche** (testi sempre attivi, che non ruotano il Leader e non si pagano).

*Nota di redazione.* La specifica (regola 16a) dice: "Le gemme del difensore pagano prima il costo della Reazione. Se non bastano, la Reazione torna dov'era senza effetto e tutte le gemme restano Parata". Con l'impegno a vista il difensore conosce tutto quando sceglie, quindi la forma scritta sopra dà gli stessi esiti e applica il pilastro 9 ("ogni costo non pagabile rende l'azione illegale"). È la riformulazione proposta dall'editor e sostenuta dall'architetto in ratifica; la scelta della forma è stata affidata a questo regolamento.

### C5. Confronto
Furia, Bracconiere, Scudo e le altre condizioni stampate si leggono qui.
- **Fa** = Forza stampata dell'attaccante + gemme impegnate dall'attaccante + bonus.
- **Db** = Forza dell'Unità che si oppone, oppure Tempra del Leader, + 2 × gemme restanti del difensore + Reazione + bonus.

| Attaccante | Bersaglio | Esito |
|---|---|---|
| Unità | Unità | Perde la più bassa: è sconfitta l'Unità con il valore più basso. A pari sono sconfitte entrambe. **Se il bersaglio ha Scudo, a pari è sconfitto solo l'attaccante** |
| Leader | Unità | L'Unità è sconfitta se Db ≤ Fa (**con Scudo: se Db < Fa**); altrimenti non succede nulla. Il Leader non è mai sconfitto |
| Unità o Leader | Leader | L'attacco **va a segno** se Fa ≥ Db; altrimenti non succede nulla. L'attaccante non è mai sconfitto |

Scudo nella tabella: **[default, aperto: P7; `scudo` vince_pareggi]**.

### C6. Esiti
In quest'ordine:
- **(a)** Le Unità sconfitte vanno negli Scarti.
- **(b)** Se l'attacco è andato a segno sul Leader:
  - se il Leader è **Alle Corde e non ha Cicatrici fresche**, l'attaccante **vince la partita** (colpo finale);
  - altrimenti, se le sue Cicatrici fresche sono **meno del Saldo** (2; 3 dal round 10) e il Leader ha almeno 1 Vita, la carta in cima alla sua Vita va tra le Cicatrici, **fresca**;
  - altrimenti la perdita si ignora.
- **(c)** Le gemme impegnate da entrambi tornano nella scorta. La Reazione va negli Scarti.
- **(d)** Controlli di stato. Il Risveglio scatta con Vita ≤ 2 (§9.8).
- **(e)** Si risolvono i trigger "quando sconfigge" e "dopo lo scontro". **Nessun modificatore sopravvive allo scontro.** Il giocatore attivo torna alla fase principale.

**Riepilogo delle decisioni per scontro.** Attaccante: chi attacca (C1) e quante gemme impegnare (C3). Difensore: se e con quale Unità opporsi (C2); quante gemme di Guardia impegnare e se giocare una Reazione, e quale (C4).

---

## 9. Vita, Cicatrici fresche, Saldo, colpo finale e Crepuscolo

### 9.1 Alle Corde
Un Leader è **Alle Corde** se:
- ha **0 Vite**; oppure
- dal **round 13** in poi, ha **1 Vita** [`corde_one_life_round` 13].

Alle Corde non si registra: si legge in ogni momento dalla Vita e dal round del tracciato.

### 9.2 Perdere Vita
- **Ogni perdita di Vita** (attacchi, costi, mazzo vuoto) sposta la carta in cima alla Vita tra le Cicatrici, **fresca**, ed è soggetta al Saldo.
- Unica eccezione: il **Crepuscolo** (§6.1 b), le cui Cicatrici entrano **dritte** e non contano per il Saldo.
- Un Leader con 0 Vite non perde altre Vite: la perdita si ignora.
- Vite perse = Vita iniziale − Vita attuale.

### 9.3 Saldo
- Il **Saldo** è il massimo di Cicatrici fresche che un Leader può avere: **2**, e **3 dal round 10** [`saldo` 2, `saldo_late` 3, `saldo_late_round` 10].
- Se un Leader ha già tante Cicatrici fresche quante il Saldo, ogni altra perdita di Vita si ignora.
- Non serve un contatore: il Saldo si legge contando le Cicatrici fresche (ruotate). Poiché le fresche si raddrizzano nella Fine di ogni turno (§6.4 c), il Saldo vale di fatto per un turno.

### 9.4 Costi in Vita
Se un effetto chiede di perdere Vita **come costo** e quella perdita non può avvenire per intero (Saldo raggiunto, Vita a 0, o il testo vieta di scendere sotto una soglia), il costo non è pagabile e l'azione è **illegale**.

### 9.5 Colpo finale
Vinci se un tuo attacco va a segno sul Leader avversario mentre quel Leader è **Alle Corde e non ha Cicatrici fresche** (C6 b).

*Esempio.* Nel round 7 il Leader di G2 ha 1 Vita. G1 lo colpisce: la Vita va tra le Cicatrici, fresca, e il Leader è a 0 Vite, Alle Corde. Un secondo colpo nello stesso turno non vince, perché c'è una Cicatrice fresca, e la perdita si ignora (0 Vite). Nella Fine del turno di G1 la Cicatrice si raddrizza. G2 gioca il suo turno; nella sua Fine può mettere sul Leader 1 gemma di Guardia in più, perché è Alle Corde. Nel round 8 il primo attacco di G1 che va a segno è il colpo finale.

### 9.6 Mazzo vuoto
Se devi pescare e il mazzo è vuoto, invece di pescare perdi 1 Vita, soggetta al Saldo. Se in quel momento il tuo Leader ha già **0 Vite**, **perdi la partita**.

### 9.7 Condizioni di vittoria
Si vince **solo** così:
1. col **colpo finale** (§9.5);
2. quando l'avversario deve pescare da un mazzo vuoto con 0 Vite (§9.6);
3. col **Crepuscolo**: dal round 15, se nel suo Ripristino il Leader avversario è Alle Corde, l'avversario perde (§6.1 b).

Se due condizioni si verificano nello stesso momento, **perde il giocatore attivo**. Non esistono patte, vittorie ai punti o vittorie alternative.

### 9.8 Risveglio
- Quando il tuo Leader ha **Vita ≤ 2** (almeno 3 Vite perse), al controllo di stato successivo si gira sul lato **Risvegliato**: Forza 4, Tempra 4, massimo di Guardia 3, abilità del lato Risvegliato [`awaken_at_life` 2].
- Succede una volta per partita ed è permanente, anche a metà del turno avversario. Il numero di Cicatrici è irrilevante.
- Lo stato (Pronto o Ruotato) si conserva.
- Le Vite perse col Crepuscolo possono causare il Risveglio.

### 9.9 Cicatrici
- Le Cicatrici sono pubbliche.
- Una Cicatrice **fresca** non si gioca come Reazione e non si Rimargina. Diventa dritta nella Fine del turno.
- Una carta Reazione tra le tue Cicatrici **dritte** si può giocare in C4 come se fosse in mano; poi va negli Scarti.
- **Rimarginare** (§10.2) riporta in mano una Cicatrice dritta.
- **Furia** conta **tutte** le Cicatrici, dritte e fresche (§12.2).

### 9.10 Fine garantita
Dal round 13 un Leader con 1 Vita è Alle Corde, e dal round 15 il Crepuscolo toglie 2 Vite a ogni Ripristino o fa perdere chi è Alle Corde. Quindi ogni giocatore perde al più tardi:
- al suo turno del round **15** se a quel Ripristino ha ≤ 1 Vita;
- del round **16** se ne ha 2 o 3;
- del round **17** se ne ha 4 o 5.

Il simulatore interrompe e registra come "non conclusa" una partita che superi il round 17 [`max_rounds` 17]: sarebbe un errore di implementazione, non una patta. Misurato: 0.2% di partite oltre il round 15; 99.3% chiuse dal colpo finale e 0.7% dal Crepuscolo.

---

## 10. Il Leader in azione

### 10.1 Attacco del Leader
Il Leader attacca come un personaggio (§8) con la sua Forza: 3, Risvegliato 4. Attaccare lo ruota, quindi attacca al massimo una volta per turno, salvo effetti che lo raddrizzano.
- Contro un Leader che non si difende (Tempra 4, nessuna gemma impegnata, nessuna opposizione) il Leader Base deve impegnare **almeno 1 gemma** per andare a segno. Il Leader Risvegliato va a segno **senza impegnare gemme**.
- Se il difensore gli oppone un'Unità, il Leader la sconfigge se Db ≤ Fa (con Scudo: se Db < Fa) e non è mai sconfitto.

*Questo punto è in attesa di Vittorio:* il pilastro 2 di v0.1 ("il Leader non colpisce gratis") non vale più sul lato Risvegliato. Vedi `pilastri_design_v0.2.md`, pilastro 2.

### 10.2 Rimarginare (abilità ⟳ di ogni Leader)
> **⟳, 1 Brace**: prendi in mano una tua Cicatrice **dritta**.

- È un'abilità ⟳ stampata (implicitamente) su ogni Leader: il Leader deve essere **Pronto** e si ruota.
- Conseguenza: in un turno il Leader **o attacca o Rimargina** (o usa un'altra ⟳), salvo effetti che lo raddrizzano.
- È legale anche con 8 o più carte in mano: l'eccesso si scarta nella Fine.
- Rimarginare abbassa il conteggio della Furia.

### 10.3 Abilità di Reazione dei Leader
Le abilità che in v0.1 erano Reazioni del Leader sono **statiche**: si leggono in C4 (d) quando il loro controllore è il difensore. Non ruotano il Leader, non costano gemme e valgono anche se il Leader è Ruotato.

---

## 11. Compensazione del primo giocatore

- **Nessuno attacca nel round 1** (né con Unità, né con il Leader, né con Assalto).
- **G1 non pesca nel round 1.**
- Mano iniziale: 5 carte per entrambi [`g2_hand_extra` 0].
- **G2 prende 1 gemma di Brace in più nel round 1 e 1 in più nel round 3** **[default, aperto: P6]**. La regola è stampata sul tracciato: non serve un segnalino Scintilla.
- Obiettivo di taratura: G1 vince il 48–52% delle partite (pilastri).
- Misurato (2.000 partite, mazzi convertiti, mirror): senza compensazione G1 vince il 55.7%; con +1 gemma nei round 1 e 3 vince il **50.8%** [48.7–53.0]. La variante che decide è nel §17.1.

---

## 12. Colori e parole chiave

### 12.1 Colori

| Colore | Filosofia | Parole chiave principali | Combo previste |
|---|---|---|---|
| **Rosso** | Pressione, tutta la Brace in Forza | Assalto, Impeto, Rinnovo | + Verde (gemme impegnate + Bracconiere), + Nero (Furia = Forza senza gemme) |
| **Blu** | Difesa, Guardia, contrattacco | Scudo, Reazioni | + Nero (Reazioni dalle Cicatrici). + Verde: da rivedere al thread carte (in v0.1 si basava su Esposto) |
| **Nero** | Ferite come potere | Furia, Cicatrici, costi in Vita | + Rosso (picchi di Forza), + Blu (sopravvivere Alle Corde) |
| **Verde** | Caccia alle Unità | Bracconiere, Stanca, ⟳ | + Blu, + Rosso |
| **Neutrale** | Collante tra archetipi | qualsiasi | tutti |

### 12.2 Parole chiave (ognuna compare in almeno due colori)
- **Assalto**: questa Unità entra **Pronta**, quindi può attaccare nel turno in cui entra (mai nel round 1).
- **Scudo**: quando questa Unità si oppone, vince i pareggi nel Confronto: contro un'Unità a pari è sconfitto solo l'attaccante; contro un Leader è sconfitta solo se Db < Fa. Si ruota come le altre Unità **[default, aperto: P7]**.
- **Impeto N: +X** *(se nell'impegno hai almeno N gemme, +X in questo scontro; quando è il bersaglio contano solo le gemme di Parata)*: si legge in C4 (d), è pubblica. Il difensore conta solo la Parata (C4 b). Sostituisce Infuso N (Q-014, forma Q-015 M2).
- **Caccia** *(quando attacca, puoi scegliere come bersaglio un'Unità avversaria, anche Ruotata, invece del Leader; l'avversario può ancora opporsi con un'altra Unità, che diventa il bersaglio)*: il bersaglio cacciato può essere Pronto o Ruotato e si difende con la sua Forza, la Parata, la Reazione e lo Scudo; non "si oppone", quindi i suoi "quando si oppone" non scattano (Q-014).
- **Furia N: +X**: +X al Confronto se hai almeno N Cicatrici, contando **tutte** le Cicatrici (dritte e fresche). Si legge solo in C5: non è mai un'aura.
- **Bracconiere X** *(quando attacca e il suo bersaglio è un'Unità, +X in questo scontro)*: vale se il bersaglio è un'Unità che si oppone o un'Unità cacciata; mai quando è l'Unità con Bracconiere a opporsi (Q-014).
- **Rinnovo** *(quando attacca e sconfigge un'Unità, si raddrizza)*: mai in opposizione (Q-014).
- **Stanca**: ruota un'Unità avversaria Pronta. Si usa solo nel tuo turno e mai sul Leader. Un effetto Stanca che si risolverebbe nel turno avversario non ha effetto (Q-016).
- **⟳** (simbolo di costo): ruota la carta; legale solo se è Pronta. I costi in gemme si pagano con la Brace (§5.2).

### 12.3 Conversione da v0.1

| v0.1 | v0.2 |
|---|---|
| Infuso N: [effetto] | **Impeto N: +X** (§12.2) |
| Esponi | **Stanca**: ruota un'Unità avversaria Pronta; solo nel tuo turno, mai il Leader |
| Bracconiere +X | Bracconiere X: +X quando attacca e il suo bersaglio è un'Unità |
| Furia N | +X al Confronto se hai almeno N Cicatrici, contando tutte le Cicatrici; mai come aura |
| Scudo (può intercettare) | vince i pareggi quando si oppone (C5) **[aperto: P7]** |
| Rinnovo | quando attacca e sconfigge un'Unità, si raddrizza |
| "fino a fine turno" | "per questo scontro", oppure effetto permanente |
| Rimozione economica (legge 7) | solo su Unità Ruotate; legge 8: gli effetti che stancano hanno per bersaglio solo Unità |
| Abilità di Reazione dei Leader | testi statici letti in C4 (es. Maera Risvegliata: le tue gemme di Parata valgono +3) |
| Intercetto, "quando intercetta" | "quando si oppone" |
| Esposto, "Unità Esposta" | Ruotata; ma una carta Ruotata non è mai bersaglio |
| Fornace, "Brace pari alla Fornace" | Brace = min(round, 8) dal tracciato |
| Guardia "accantonata" | gemme di Brace spostate sul Leader nella Fine |
| Scintilla | +1 gemma a G2 nei round 1 e 3, stampata sul tracciato **[aperto: P6]** |

---

## 13. Carte d'esempio convertite

Sono le carte di v0.1 convertite con la tabella del §12.3, così come le usa il simulatore (`sim/v02/cards_v02.json`) per le misure del nucleo. **Non sono il set**: le carte e i Leader del primo set (LDR-01…06, con i testi approvati, es. Thorn = LDR-04 "⟳, 1 Brace: Stanca … costo ≤3") sono in `tcg/set/finale/set_v02.json`. Le conversioni dei Leader sono provvisorie e i valori vanno al thread carte. Formato: **Nome** — costo · tipo · Forza · testo. Il costo è in gemme.

**Leader** (tutti F3 / Tempra 4 / Vita 5; Risvegliati F4 / Tempra 4)
- **Arden, Fabbro di Guerra** (Rosso/Verde). Base: se un tuo attaccante ha almeno 2 gemme impegnate, ha +1 Forza in questo scontro. Risvegliato: le tue Unità con Assalto hanno +1 Forza.
- **Maera, Custode del Passo** (Blu/Nero). Base, statica: quando difendi, se nell'impegno hai almeno 1 gemma di Parata, l'attaccante ha −2 in questo scontro. Risvegliato, statica: le tue gemme di Parata valgono +3 invece di +2.
- **Sorella Vey, la Segnata** (Nero/Rosso). Base: la tua Furia conta 1 Cicatrice in più. Risvegliato: Rimarginare non costa gemme (resta ⟳).
- **Thorn, Voce del Branco** (Verde/Blu). Base: ⟳, 2 gemme: Stanca un'Unità avversaria Pronta con costo ≤ 2. Risvegliato: le tue Unità con Bracconiere hanno +1 Forza.

**Rosso**
- **Scudiera di Brace** — 1 · Unità · F2 · Assalto. Se hai impegnato almeno 1 gemma: +1 Forza in questo scontro.
- **Carica della Fornace** — 2 · Tattica · Raddrizza una tua Unità Ruotata.
- **Vesh, Lama Rovente** — 4 · Unità · F4 · Assalto. Se hai impegnato almeno 2 gemme: +2 Forza in questo scontro.

**Blu**
- **Sentinella del Guado** — 2 · Unità · F3 · Scudo. Quando si oppone, +2 al valore di difesa in questo scontro.
- **Muro di Scudi** — 1 · Reazione · +4 al valore di difesa del bersaglio in questo scontro [`muro_bonus` 4].
- **Il Bastione Vivente** — 5 · Unità · F6 · Scudo. Quando sconfigge un attaccante, peschi 1 carta.

**Nero**
- **Penitente delle Mille Ferite** — 2 · Unità · F1 · Furia 2: +3.
- **Patto di Sangue** — 1 · Tattica · Costo aggiuntivo: il tuo Leader perde 1 Vita; non puoi giocarla se il tuo Leader ha 1 Vita o meno. Peschi 1 carta.
- **Grido dalla Cicatrice** — 1 · Reazione · L'attaccante ha −3 Forza in questo scontro; −5 invece se la giochi dalle Cicatrici [`grido_hand` 3, `grido_scars` 5].

**Verde**
- **Lince del Sottobosco** — 2 · Unità · F2 · Bracconiere +2.
- **Esca** — 1 · Tattica · Stanca un'Unità avversaria Pronta con costo ≤ 3.
- **Matriarca del Branco** — 5 · Unità · F5 · Quando una tua Unità sconfigge un'Unità, peschi 1 carta.

**Neutrali**
- **Recluta del Crocevia** — 1 · Unità · F1 · Scudo. Se hai almeno 2 Cicatrici, ha +1 Forza.
- **Lanterna del Pellegrino** — 2 · Reliquia · Il tuo massimo di Guardia aumenta di 1.
- **Colpo Mirato** — 3 · Tattica · Sconfiggi un'Unità avversaria Ruotata con Forza ≤ 4.

Il costo di una Reazione si paga con le gemme di Guardia impegnate in C4. Le carte "[test]" del file del simulatore sono riempitive senza testo e non fanno parte del set.

---

## 14. Leggi di design (vincolanti per chi scrive carte)

1. Nessuna carta annulla un'altra carta o vieta di giocare. Le Reazioni **modificano** uno scontro, non annullano carte; l'attaccante non risponde mai alla risposta del difensore.
2. Niente scarto forzato dalla mano avversaria.
3. Nessun effetto modifica il tracciato del round o la Brace che l'avversario ne riceve (in v0.1: "nessuna distruzione o riduzione della Fornace avversaria").
4. Nessun effetto impedisce a un personaggio di raddrizzarsi per più di 1 turno (niente lock oltre un round).
5. Nessuna moneta o dado che decide l'esito dopo una scelta: la casualità sta solo nella pescata.
6. Una carta comune ha al massimo una parola chiave e una frase di testo.
7. **La rimozione economica (costo ≤ 3) colpisce solo Unità Ruotate.**
8. **Gli effetti che stancano hanno per bersaglio solo Unità**, mai il Leader.
9. Ogni parola chiave compare in almeno due colori; le Neutrali fanno da collante.
10. **Risposte agli Scudo**: ogni colore ha almeno una risposta comune agli Scudo e ai muri (stancare, ignorare lo Scudo o colpire chi si oppone); almeno 3 colori su 4, più le Neutrali, hanno effetti Stanca economici.
11. Ogni testo deve poter essere scritto nel simulatore senza casi speciali: un costo non pagabile rende l'azione illegale; i trigger hanno un punto fisso nella sequenza.

**Regole di set proposte (al thread carte, non ancora leggi).** Ogni Reazione costa almeno 1 (il simulatore la applica già); nessun effetto rimette gemme in Guardia durante uno scontro; gli effetti che fanno perdere Vite si risolvono solo nella fase principale di chi li controlla, nessuna Reazione ha un costo in Vita e non esistono effetti "l'avversario perde Vite"; una Reazione a costo N dà più di 2N di difesa equivalente. **Vincolo in vigore fino al voto della variante P8 (§17.4):** nessuna carta stampa costi in Vita pagabili nel turno avversario né effetti "l'avversario perde Vite".

---

## 15. Glossario

| Termine | Definizione |
|---|---|
| **Alle Corde** | Leader con 0 Vite; dal round 13 anche con 1 Vita. Si legge sempre dallo stato corrente (§9.1). |
| **Andare a segno** | Un attacco al Leader con Fa ≥ Db in C5. |
| **Assalto** | L'Unità entra Pronta e può attaccare subito (mai nel round 1). |
| **Attaccante legale** | Un tuo personaggio Pronto (§8). |
| **Bersaglio** | Sempre il Leader avversario, salvo opposizione o parola chiave. |
| **Brace** | Gemme che prendi nel tuo Ripristino: min(round, 8); si spendono o si impegnano nel tuo turno. |
| **Bonus al bersaglio** | "Il bersaglio ha +N": si somma al suo valore di difesa (Forza dell'Unità o Tempra del Leader). |
| **Bracconiere X** | +X in questo scontro quando attacca e il suo bersaglio è un'Unità. |
| **Caccia** | Attaccando, sceglie come bersaglio un'Unità avversaria, anche Ruotata, invece del Leader (§12.2). |
| **Cicatrice** | Carta Vita persa, a faccia in su, pubblica. È **dritta** oppure **fresca**. |
| **Cicatrice fresca** | Cicatrice nata in questo turno, tenuta ruotata. Non si gioca come Reazione, non si Rimargina, conta per il Saldo e impedisce il colpo finale. Si raddrizza nella Fine. |
| **Colpo finale** | Attacco a segno su un Leader Alle Corde senza Cicatrici fresche: vittoria. |
| **Confronto** | Passo C5: si confrontano Fa e Db. |
| **Controlli di stato** | Verifiche automatiche del §7.4. |
| **Crepuscolo** | Dal round 15, nel tuo Ripristino: se il tuo Leader è Alle Corde perdi, altrimenti perde 2 Vite che entrano dritte e non contano per il Saldo. |
| **Db** | Valore di difesa del bersaglio nel Confronto. |
| **Difendi** | Sei il difensore di uno scontro, qualunque sia il bersaglio. |
| **Difensore** | Il giocatore non attivo. |
| **Fa** | Forza dell'attaccante nel Confronto. |
| **Forza** | Valore di attacco di un personaggio e valore di difesa di un'Unità. |
| **Forza attuale** (fuori dallo scontro) | Forza stampata + bonus sempre attivi (aure); è quella che leggono i filtri "con Forza ≤N" (Q-015 S-4). |
| **Furia N** | +X al Confronto con almeno N Cicatrici, contandole tutte. |
| **Gemma** | L'unico segnalino del gioco. Sta nella scorta, in Brace, in Guardia o nell'impegno. |
| **Giocatore attivo** | Il giocatore di cui è il turno. |
| **Guardia** | Gemme sul Leader, formate nella tua Fine; si impegnano solo nel turno avversario. |
| **Impegno** ("pugno") | Gemme messe scoperte in uno scontro: dall'attaccante in C3, dal difensore in C4 (anche quella che paga la Reazione). |
| **Impeto N: +X** | Se nell'impegno hai almeno N gemme, +X in questo scontro; quando è il bersaglio contano solo le gemme di Parata. |
| **Massimo di Guardia** | 2, 3 da Risvegliato, +1 se il tuo Leader è Alle Corde, più gli aumenti stampati sulle carte (NEU-002). |
| **Opposizione** | In C2 il difensore ruota una sua Unità Pronta, che diventa il bersaglio. |
| **Parata** | Ogni gemma di Guardia impegnata che non paga una Reazione: +2 al valore di difesa. |
| **Personaggio** | Unità o Leader. |
| **Pronto** | Carta dritta: può attaccare, opporsi e usare ⟳. |
| **Raddrizzare** | Riportare dritta una carta Ruotata o una Cicatrice fresca. |
| **Reazione** | Carta giocata dal difensore in C4, dalla mano o da una Cicatrice dritta, pagata con le gemme impegnate; al massimo una per scontro. |
| **Rimarginare** | ⟳ del Leader + 1 Brace: prendi in mano una Cicatrice dritta. |
| **Rinnovo** | Quando l'Unità attacca e sconfigge un'Unità, si raddrizza. |
| **Risveglio** | Il Leader si gira sul lato Risvegliato quando ha Vita ≤ 2; una volta per partita. |
| **Round** | Un turno di G1 più un turno di G2; avanza nel Ripristino di G1. |
| **Ruotato** | Carta che ha agito. Non può attaccare, opporsi né usare ⟳; non è mai bersaglio per questo. |
| **Saldo** | Massimo di Cicatrici fresche di un Leader: 2, 3 dal round 10. Le perdite oltre si ignorano. |
| **Scontro** | Un attacco da C1 a C6. |
| **Sconfiggere** | Mandare un'Unità negli Scarti per esito di scontro o per effetto. |
| **Scorta** | Riserva comune delle gemme. Spendere = rimettere nella scorta. |
| **Scudo** | L'Unità che si oppone vince i pareggi [aperto: P7]. |
| **Stanca** | Ruota un'Unità avversaria Pronta; solo nel tuo turno, mai il Leader. |
| **Tempra** | Valore di difesa del Leader: 4. |
| **Tracciato del round** | Carta con il segnalino del round e le soglie stampate. |
| **Trigger** | Abilità "quando…" o "a fine turno"; ordine del §7.5. |
| **Turno** | Sempre il turno del giocatore attivo. |
| **Valore di difesa** | Forza dell'Unità che si oppone o Tempra del Leader, più i bonus dello scontro. |
| **Vite perse** | Vita iniziale − Vita attuale; determina il Risveglio. |
| **⟳** | Simbolo di costo: ruota la carta, che deve essere Pronta. |

---

## 16. Parametri numerici v0.2

Nomi dei parametri da `sim/v02/config.py`; preset del simulatore: `V02`.

| Regola | Valore | Parametro del simulatore | Note |
|---|---|---|---|
| Carte nel mazzo | 40, max 3 copie per ID | — | |
| Mano iniziale | 5 / 5 | `hand` 5, `g2_hand_extra` 0 | G2 a 6 carte non sposta G1 (55.9%) |
| Mulligan | fino a 3 carte | `mulligan_max` 3 | |
| Vita iniziale | 5 | `life` 5 | |
| Forza del Leader | 3 / Risvegliato 4 | `leader_power` 3, `leader_power_awakened` 4 | |
| Tempra del Leader | **4** (entrambi i lati) | `tempra` 4 | Deciso 8/8; con 5: mediana 11, round 13+ 13.2% |
| Risveglio | Vita ≤ 2 | `awaken_at_life` 2 | |
| Brace | min(round, 8) | `brace_max` 8 | |
| Compensazione di G2 | +1 gemma nei round 1 e 3 | `scintilla_g2_gems` 1, `scintilla_extra_gems` 1, `scintilla_extra_round` 3, `scintilla_guardia_g2` 0 | **[aperto: P6]**; G1 50.8% |
| Massimo di Guardia | 2 / Risvegliato 3; +1 Alle Corde; + carte (NEU-002) | `guard_max` 2, `guard_max_awakened` 3, `guard_alle_corde_bonus` 1 | |
| Gemma d'attacco | +1 Forza | `forza_per_gemma` 1 | |
| Gemma di Parata | +2 difesa | `parata_per_gemma` 2 | Maera Risvegliata +3 |
| Impegno | sequenziale, a vista | `pugno` sequenziale | Deciso 8/8 |
| Opposizione | prima dell'impegno | `opposizione` prima | Deciso 8/8 |
| Raddrizzo dei personaggi | nel Ripristino del controllore | `raddrizzo` ripristino | Deciso 8/8; con "Fine": 86.6% al round 13+ |
| Scudo | vince i pareggi | `scudo` vince_pareggi | **[aperto: P7]** |
| Saldo | 2 fresche; 3 dal round 10 | `saldo` 2, `saldo_late` 3, `saldo_late_round` 10 | |
| Alle Corde a 1 Vita | dal round 13 | `corde_one_life_round` 13 | |
| Crepuscolo | dal round 15, −2 Vite dritte | `crepuscolo_round` 15, `crepuscolo_loss` 2 | |
| Nessun attacco | round 1 | `no_attack_round` 1 | |
| Unità / Reliquie | max 5 / max 2 | `max_units` 5, `max_relics` 2 | |
| Limite di mano | 8 a fine turno | `hand_limit` 8 | |
| Limite tecnico | round 17 | `max_rounds` 17 | Oltre: "non conclusa" |
| Muro di Scudi | 1 gemma, +4 | `muro_bonus` 4 | Provvisorio |
| Grido dalla Cicatrice | 1 gemma; −3 dalla mano, −5 dalle Cicatrici | `grido_hand` 3, `grido_scars` 5 | Provvisorio |
| Rimarginare | ⟳ del Leader + 1 Brace | — | Niente limite "1 volta per turno" |

### 16.1 Numeri misurati (E-014, base finale: Tempra 4, impegno sequenziale)
Mazzi convertiti da v0.1, mirror, IA semplice, 10.000 partite salvo dove indicato.

| Metrica | Misura | Obiettivo (pilastri) |
|---|---|---|
| Attacchi fermati | 42.0% | 30–45% |
| Durata | mediana 8 round, media 8.38 | mediana 8–10 |
| Partite al round 13+ | 1.5% | <10% |
| Oltre il round 15 | 0.2% | <2% |
| Vittorie prima del round 5 | 0.0% | 0 |
| G1 vince, senza compensazione | 55.7% | 48–52% |
| G1 vince, con +1 gemma nei round 1 e 3 (2.000 partite) | 50.8% [48.7–53.0] | 48–52% |
| Rimonte (senza / con compensazione) | 14.3% / 12.8% | **20–35% (fuori fascia)** |
| Rimonte negli incroci fra mazzi diversi | 6.7% | 20–35% |
| Margine IA forte (300 partite) | +28.7 (78.7% di vittorie) | ≥65% di vittorie |
| Opposizioni | 15.4% degli attacchi | — |
| Unità ferme | 41.8% dei turni | ≤35–40% (condizione di revisione) |
| Reazioni per scontro | 0.03 | ≥0.10 (condizione di revisione) |
| Impegno vuoto / pieno | attaccante 70% / 17%; difensore 59% / 22% | nessuna degenerazione oltre il 90% |
| Modificatori per scontro | massimo 5; 0 o 1 nel 91% degli scontri | leggibilità |
| Attacchi a segno sul Leader | 44.5%; 29 attacchi per partita | — |
| Fine della partita | colpo finale 99.3%, Crepuscolo 0.7% | — |
| Vittorie per mazzo negli incroci | Arden 53.3, Maera 63.7, Thorn 10.0, Vey 72.9 | 45–55% (squilibrio dei mazzi convertiti) |

---

## 17. Varianti aperte e coda dei test

Le regole qui sotto sono già nel testo come default. Ogni variante si misura **una alla volta**, contro la base vigente, con seed appaiati.

### 17.1 P6 — Compensazione di G1 **[default: G2 +1 gemma nei round 1 e 3]**
- **Voti:** {1,3}: 2; {1,2}: 2; {1,4}: 1; Scintilla 1: 1; 2 gemme di Guardia: 1; non assegnabile: 1. Default per spareggio sulla fascia dei pilastri 48–52.
- **Bracci:** `scintilla_extra_round` ∈ {2, 3, 4}, più la Guardia di Ar (`scintilla_guardia_g2` 2).
- **Misura:** 10.000 partite appaiate per braccio sulla base finale.
- **Metrica:** G1 in 48–52 (con IC); a pari, rimonte più alte; vincolo: vittorie prima del round 6 < 1%.
- **Da sapere:** tutte le compensazioni in gemme abbassano le rimonte (da 14.3 a 9.8–12.8); fa eccezione la Guardia (15.1).

### 17.2 P7 — Scudo **[default: vince i pareggi]**
- **Voti:** vince i pareggi 5; si oppone senza ruotarsi 3.
- **Bracci:** `scudo` = `vince_pareggi` contro `oppone_senza_ruotarsi`, su mazzi del set con almeno 5 Scudo (con i mazzi convertiti l'A/B non distingue nulla).
- **Metrica:** partite al round 13+ nei matchup con ≥ 5 Scudo: ≤ 12% (Ar) / < 5% (Cr); opposizioni nella fascia 15–35%; mazzi Blu 45–55%. Compromesso di Cr: "senza ruotarsi" solo se resta su ≤ 1 Unità per colore.

### 17.3 P9b — Costo delle Reazioni in gemme di Guardia **[default: regola C4 (a), le Reazioni si pagano con le gemme impegnate]**
- **Voti:** va bene 3; non va bene 4; astenuto 1. Nessuna alternativa di nucleo con più di un voto.
- **Prima la diagnostica:** Reazioni disponibili contro giocate; mazzo di prova con 9 Reazioni.
- **Poi, se il problema è il costo:** variante di Ne, `reazione_da_cicatrice_costo` −1 (minimo 0) per le Reazioni giocate da Cicatrici dritte.
- **Metrica:** ≥ 0.10 Reazioni per scontro sui mazzi del set; rimonte in salita.

### 17.4 P8 — Cicatrici fresche: correzione in coda (livello 3)
- **Buco latente** (trovato da Bl e Cr): un Leader Alle Corde senza fresche che perde Vita nel turno avversario (per un costo in Vita o per un effetto "l'avversario perde Vite") riceve una fresca e diventa immune al colpo finale per il resto del turno. Nessuna carta attuale lo apre.
- **Correzione di Cr (nucleo):** una Vita pagata come costo entra dritta e non conta per il Saldo, come il Crepuscolo. Da votare **prima** che il set introduca costi in Vita nel turno avversario.
- **Regole di set di Bl:** vedi §14. Fino al voto vale il vincolo del §14.
- **Condizione di revisione:** più di 1 errore di stato a partita sulle fresche nel playtest fisico → segnalino del Saldo.

### 17.5 Coda dei test, nell'ordine chiesto dai votanti
1. Mazzi bicolori 20/20 contro 32/8 (Po), insieme ai mazzi convertiti riequilibrati (Thorn al 10% falsa la misura).
2. Diagnostica "Reazioni disponibili contro giocate" (P9b).
3. G1 con 10.000 partite appaiate (P6), con il vincolo "vittorie prima del round 6 < 1%".
4. Metrica nuova nel motore: **quota di scontri decisi prima dell'impegno** (l'attaccante non arriva alla soglia oppure la garantisce). Allarme sopra il 60%.
5. Rimonte ≥ 20% e archetipi 45–55% negli incroci, misurati insieme.
6. Varianti legate alla condizione "rimonte ≥ 20%": `reazione_da_cicatrice_costo` −1 e Guardia Alle Corde +2 (Ne).

### 17.6 Condizioni di revisione (primo ciclo del set, mazzi veri, anche incroci)
1. **Rimonte ≥ 20%.** Leve se restano sotto, da misurare una alla volta (ordine non votato): il difensore impegna per primo, a vista (Po; si misura subito se le rimonte restano sotto il 20%); Guardia Alle Corde +2 (Ne); Tempra 4 sul Base e 5 sul Risvegliato (Cr, innesco: rimonte < 12% dopo la compensazione).
2. **Mediana ≥ 8** e 0 vittorie prima del round 5; guardare anche i round 5–6. Se la mediana scende sotto 8: T5 + Parata +1 + Guardia max 1 (An); T5 + Guardia max 1 (Po).
3. **Scontri decisi prima dell'impegno < 60%** (Bl).
4. **Unità ferme ≤ 35–40%** (Ve): prima Caccia e Assalto nel thread carte, poi si riapre il raddrizzo.
5. **Reazioni per scontro ≥ 0.10.**
6. **G1 in 48–52** con 10.000 partite.
7. **Scudo**: round 13+ nei matchup con ≥ 5 Scudo.
8. **Playtest fisico**: tempo per turno; errori di stato ≤ 1 a partita (altrimenti segnalino del Saldo).
9. **Archetipi 45–55%** negli incroci.

### 17.7 Altri punti in coda
- Impegno coperto: si riapre solo con un S2 su ≥ 300 (An) o ≥ 500 (Ro) partite per braccio che rovesci il segno.
- Posto di Guardia extra con la Vita vuota (Ne).
- Tempi delle fresche "solo nel turno avversario" (Ar, Cr).
- Incassa sì/no (Po, Bl).
- Bersaglio scelto dall'attaccante e "preda" (Ve; serve prima Caccia dal thread carte).
- ~~Nome e valori di "se hai impegnato almeno N gemme"~~: deciso in Q-014 e Q-015, **Impeto N: +X** (§12.2).

### 17.8 Moduli futuri
I moduli di v0.1 §17 (campo di battaglia, zone contese, round condiviso, Fulcro) restano fuori dal nucleo e non sono stati toccati da Q-013. Quelli che citano Esposto o l'Esposizione vanno riscritti prima di un test.

---

## 18. Cosa è sparito rispetto a v0.1

- **Fornace** come contatore, e il **numero di turno** di ogni giocatore: c'è un solo round sul tracciato.
- **Infondere** e i **contatori d'infusione**.
- **Esposto** e la regola "Unità Esposta = bersaglio legale".
- **Intercetto** e "quando intercetta".
- La **finestra di reazione** e il **limite di reazioni** per turno.
- **Ultimo respiro**, sostituito da **+1 Guardia Alle Corde**.
- L'**istantanea Alle Corde** e il **contatore del Saldo**: entrambi si leggono dalle Cicatrici fresche.
- Il **segnalino Scintilla**.
- "Ha già attaccato in questo turno", "entrata in questo turno" e "1 volta per turno" del Rimarginare: li sostituisce lo stato Ruotato.
- I bonus **"fino a fine turno"** nel nucleo.
- Mai entrati nel nucleo: **Incassa** e l'**impegno coperto** (pugno simultaneo).

---

## Registro modifiche

| Versione | Data | Modifiche |
|---|---|---|
| v0.1 | 2026-10-07 | Prima stesura consolidata e ratificata (vedi `regolamento_v0.1.md`). |
| v0.2 | 2026-10-08 | Nucleo v0.2 da Q-013 (8 APPROVO su 8), specifica della sezione A dell'esito. Tempra 4; gemme e tracciato del round; Pronto/Ruotato; combattimento C1–C6 con impegno sequenziale e opposizione prima dell'impegno; raddrizzo nel Ripristino; Cicatrici fresche e Saldo senza contatori; +1 Guardia Alle Corde; Reazioni dei Leader statiche. Default aperti: P6 (G2 +1 gemma nei round 1 e 3), P7 (Scudo vince i pareggi), P9b (costo delle Reazioni). Regola C4 (a) scritta nella forma "una Reazione si gioca solo se le gemme impegnate ne pagano il costo" (esiti invariati). |
| v0.2.1 | 2026-10-08 | Chiarimenti per il set (R-007), nessuna regola del nucleo nuova. Stanca solo nel tuo turno, anche nei trigger (Q-016; tolta la riga del §6.3). Impegno e Parata del difensore: le condizioni sulle gemme del difensore contano solo la Parata (C4 b, Q-015 S-2). Trigger di C6 (e) anche nella sconfitta reciproca, con esempio Rinnovo/BLU-025 (§7.5, Q-015 S-9). Limite di copie per ID (§2.3). Massimo di Guardia: "+1 per Lanterna" → aumenti stampati sulle carte (§5.3). Costi ⟳ con la Brace (§5.2). Testi di Impeto, Caccia, Bracconiere, Rinnovo da Q-014/Q-015 (§12). Glossario: Bonus al bersaglio, Caccia, Difendi, Forza attuale, Impeto. |
| v0.2.2 | 2026-10-08 | Refusi da R-009: Rimarginare "⟳, 1 Brace" (§6.3, §10.2, glossario, §16); richiamo di Impeto "contando solo le gemme di Parata"; Maera del §13 con "gemma di Parata"; nota al §13 che le carte d'esempio sono quelle del simulatore del nucleo, non il set. |
| v0.2.3 | 2026-10-08 | Testi di Q-018 (livello 1, R-011 §4): richiami di Impeto e Caccia (§12.2, glossario); al §7.2 "Essere Ruotata non rende bersaglio di un attacco e non protegge dalla Caccia". Nessuna regola nuova. |
