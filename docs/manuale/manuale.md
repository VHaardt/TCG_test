---
versione: 1.0
basato_su: v0.2.6
preset: V026
---

## La partita in un minuto

Due giocatori, un **Leader** a testa e un mazzo di {{mazzo}} carte. Il Leader resta sempre in gioco: è lui che devi abbattere. Ogni volta che lo colpisci, una delle sue Vite si gira a faccia in su e diventa una **Cicatrice**. Le Cicatrici non spariscono: restano sul tavolo e il giocatore ferito può usarle.

<div class="griglia" markdown="1">
<div markdown="1">
#### Come si vince
Togli all'avversario tutte le {{life}} Vite: il suo Leader è **Alle Corde**. Poi colpiscilo ancora quando non ha ferite fresche (prese in questo turno): è il **colpo finale**.
</div>
<div markdown="1">
#### La risorsa
Le **gemme** :gemma:, tutte uguali. Ogni turno ne prendi dalla scorta tante quante dice il round (fino a {{brace_max}}). Le spendi per giocare carte o le metti in un attacco.
</div>
<div markdown="1">
#### La difesa
Le gemme che non usi, a fine turno, vanno sul tuo Leader come **Guardia**: nel turno avversario le usi per parare i colpi (+{{parata_per_gemma}} ciascuna).
</div>
<div markdown="1">
#### Agire costa
Chi attacca o usa un'abilità :ruota: si **ruota** e resta ruotato fino al tuo turno successivo. Un personaggio ruotato non può difenderti.
</div>
</div>

::: ricorda Il ritmo
I turni sono **chiusi**: gioca solo il giocatore attivo. L'avversario interviene in due momenti fissi di ogni attacco: può **opporsi** con una sua Unità e può **rispondere** con la Guardia e una carta Reazione. Non esiste una pila di effetti da risolvere al contrario.
:::

## Cosa serve

- **1 Leader** a testa, fuori dal mazzo. È una carta a due facce: lato **Base** e lato **Risvegliato**.
- **1 mazzo di {{mazzo}} carte** a testa.
- **Gemme** tutte uguali in una **scorta comune** al centro del tavolo: circa {{gemme_scorta}} per giocatore, quindi circa {{gemme_totali}} in tutto.
- **1 carta-tracciato del round** con **1 segnalino**, in comune.

Niente dadi, contatori o altri segnalini. Tutti gli stati si mostrano **ruotando le carte**.

[[figura:carta_leader|Il Leader nei due lati. Il lato Risvegliato si usa dopo che il Leader ha perso {{vite_risveglio}} Vite.]]

### Come si legge una carta

Le carte del primo set non hanno nome né illustrazione: si riconoscono dall'**ID** (per esempio ROS-001). Il prefisso indica il colore: ROS Rosso, BLU Blu, NER Nero, VER Verde, NEU Neutrale.

[[figura:anatomia_carta|Una Unità del set. Il costo si paga in gemme; la Forza serve per attaccare e per difendere.]]

Ci sono quattro tipi di carta nel mazzo:

| Tipo | Quando la giochi | Cosa fa |
|---|---|---|
| **Unità** | Nel tuo turno, pagando il costo | Resta in campo, attacca e difende. Entra **ruotata**. Massimo {{max_units}} |
| **Tattica** | Nel tuo turno, fuori da un attacco | Ha effetto subito, poi va negli Scarti |
| **Reliquia** | Nel tuo turno, pagando il costo | Resta in campo con un effetto permanente. Non ha Forza e non si può attaccare. Massimo {{max_relics}} |
| **Reazione** | Solo nel turno avversario, quando difendi | Modifica l'attacco in corso, poi va negli Scarti |

Unità e Leader insieme si chiamano **personaggi**.

### Il tracciato del round

Un **round** è un turno di G1 seguito da un turno di G2. Il tracciato dice a entrambi quante gemme prendere e quando la partita accelera.

[[figura:tracciato|Le soglie stampate sul tracciato valgono per entrambi i giocatori.]]

## Il tavolo

[[figura:tavolo|Il tavolo di un giocatore. L'avversario ha lo stesso schema, specchiato, dall'altra parte.]]

| Zona | Chi la vede | Cosa contiene |
|---|---|---|
| **Mazzo** | Nessuno | Si pesca dalla cima |
| **Mano** | Solo tu | Al massimo {{hand_limit}} carte alla fine del tuo turno |
| **Vita** | **Nessuno, neanche tu** | {{life}} carte coperte sotto il Leader; si prende sempre quella in cima |
| **Cicatrici** | Tutti | Le Vite perse, a faccia in su |
| **Campo** | Tutti | Il Leader, fino a {{max_units}} Unità e fino a {{max_relics}} Reliquie |
| **Scarti** | Tutti | Unità sconfitte, Tattiche e Reazioni usate, carte scartate |

Le gemme sono sempre visibili. Possono stare in quattro posti: nella **scorta** comune, nella tua **Brace** (davanti a te, nel tuo turno), nella tua **Guardia** (sopra il Leader, nel turno avversario) o nell'**impegno** (al centro, durante un attacco). **Spendere** una gemma vuol dire rimetterla nella scorta. Le gemme non vanno mai sulle Unità.

::: attenzione Niente sostituzioni
Se hai già {{max_units}} Unità non puoi giocarne una sesta, e con {{max_relics}} Reliquie non puoi giocarne una terza. Non puoi sacrificarne una per fare posto.
:::

## Preparazione

1. Scegliete **a caso** chi inizia: è **G1**. L'altro è **G2**.
2. Mettete il Leader in campo sul lato **Base**, dritto.
3. Mescolate il mazzo e pescate **{{hand}} carte**.
4. **Mulligan**, una volta sola, prima G1 e poi G2: puoi mettere in fondo al mazzo da 0 a {{mulligan_max}} carte della mano, nell'ordine che vuoi, e pescarne altrettante. Il mazzo non si rimescola.
5. Mettete le prime **{{life}} carte** del mazzo coperte sotto il Leader, senza guardarle: sono le vostre **Vite**.
6. Il segnalino del round va prima della casella 1. Tutte le gemme sono nella scorta.
7. Comincia G1.

::: ricorda Vantaggio di chi inizia
Partire per primi è un vantaggio, quindi: **nessuno attacca nel round {{no_attack_round}}**, **G1 non pesca nel round 1** e **G2 prende 1 gemma in più nei round {{round_g2}}** (è stampato sul tracciato).
:::

::: prova Compensazione di G2
La gemma in più di G2 nei round {{round_g2}} è la regola in vigore, ma i suoi valori sono ancora in prova: potrebbero cambiare dopo nuovi test.
:::

## Il turno

Ogni turno ha quattro fasi, sempre in quest'ordine. Il **giocatore attivo** è quello di turno; l'altro è il **difensore**.

[[figura:turno|Le quattro fasi del turno, con i passi in ordine.]]

### 1. Ripristino

1. Se sei G1, **avanza il segnalino** del round di una casella.
2. **Crepuscolo**: dal round {{crepuscolo_round}}, solo nel turno di G1 (vedi [La fine della partita](#la-fine-della-partita)).
3. Rimetti nella scorta le gemme di **Guardia** rimaste sul tuo Leader.
4. **Raddrizza** il tuo Leader e le tue Unità.
5. Prendi dalla scorta la tua **Brace**: tante gemme quanto il numero del round, fino a un massimo di {{brace_max}}. Se sei G2, nei round {{round_g2}} prendine una in più.

### 2. Pesca

Pesca 1 carta. G1 non pesca nel round 1. Se devi pescare e il mazzo è vuoto, perdi invece 1 Vita (vedi [Casi particolari](#casi-particolari)).

### 3. Fase principale

Fai quante azioni vuoi, una alla volta e in qualsiasi ordine. Ogni azione si risolve per intero prima della successiva.

| Azione | Costo | Note |
|---|---|---|
| Giocare un'Unità | gemme di Brace | Entra **ruotata**: non può attaccare né opporsi fino al tuo prossimo Ripristino (salvo Assalto) |
| Giocare una Reliquia | gemme di Brace | Massimo {{max_relics}} |
| Giocare una Tattica | gemme di Brace | Si risolve e va negli Scarti |
| Usare un'abilità :ruota: | ruotare la carta, più quanto stampato | Solo se la carta è dritta |
| **Rimarginare** | :ruota: del Leader + 1 gemma di Brace | Riprendi in mano una tua Cicatrice dritta |
| **Attaccare** | ruotare l'attaccante | Con un tuo personaggio dritto. Mai nel round {{no_attack_round}} |

Dopo un attacco torni alla fase principale: puoi giocare altre carte e attaccare ancora con un altro personaggio dritto.

::: attenzione Costi da pagare per intero
Un'azione che non puoi pagare tutta non si può fare. Vale anche per i costi in Vita.
:::

### 4. Fine

1. Si risolvono gli effetti "a fine turno".
2. **Forma la Guardia**: sposta sul tuo Leader le gemme di Brace che non hai usato, fino al tuo **massimo di Guardia** ({{guard_max}} sul lato Base). Le altre tornano nella scorta.
3. **Tutte le Cicatrici fresche** di entrambi i giocatori si raddrizzano.
4. Se hai più di {{hand_limit}} carte in mano, scarta fino ad averne {{hand_limit}}.

Poi tocca all'avversario.

## Le gemme

Le gemme sono una sola risorsa con due usi: nel tuo turno sono **Brace** (attacco e carte), nel turno avversario sono **Guardia** (difesa). Quello che spendi per attaccare non ti protegge dopo.

[[figura:gemme|Il giro delle gemme. Ogni gemma finisce sempre nella scorta comune.]]

- **Spendere**: paghi carte e abilità con la Brace. Le abilità e le carte si pagano **sempre con la Brace**, mai con la Guardia.
- **Impegnare in attacco**: ogni gemma di Brace che metti in un tuo attacco dà **+{{forza_per_gemma}}** alla Forza dell'attaccante. Dopo l'attacco torna nella scorta.
- **Guardia**: nella tua Fine sposti sul Leader la Brace avanzata, fino al massimo di Guardia. Nel turno avversario ogni gemma di Guardia che impegni dà **+{{parata_per_gemma}}** alla difesa (è la **Parata**) oppure paga il costo di una Reazione.

### Massimo di Guardia

| Leader | Massimo di Guardia |
|---|---|
| Lato Base | {{guard_max}} |
| Lato Risvegliato | {{guard_max_awakened}} |
| Alle Corde | +{{guard_alle_corde_bonus}} (quindi {{guard_max_corde}} sul Base, {{guard_max_risv_corde}} sul Risvegliato) |
| Carte che lo aumentano | quanto stampato sulla carta |

Se il massimo scende (per esempio lascia il gioco una carta che lo aumentava), le gemme in eccesso tornano subito nella scorta. Se sale nel turno avversario (per esempio perché il Leader si Risveglia), si alza solo il tetto: non ricevi gemme nuove.

::: esempio Brace e Guardia in un turno
Round 4: G1 prende 4 gemme. Ne spende 2 per un'Unità e ne impegna 1 in un attacco. Gliene resta 1: nella Fine la mette sul Leader come Guardia. Nel turno di G2 potrà usarla per parare (+{{parata_per_gemma}}) o per pagare una Reazione da 1.
:::

## Dritto e ruotato

Ogni carta in campo è **dritta** (pronta) o **ruotata** di 90°. Ruotata vuol dire solo **"ha già agito"**.

[[figura:pronto_ruotato|Lo stato di una carta si vede a colpo d'occhio.]]

- Una carta si ruota quando **attacca**, quando **si oppone**, quando usa un'abilità :ruota: (anche Rimarginare) o quando un effetto la **Stanca**.
- Un personaggio ruotato non può attaccare, opporsi né usare abilità :ruota:.
- Le Unità **entrano ruotate**. Con **Assalto** entrano dritte.
- I tuoi personaggi si raddrizzano **solo nel tuo Ripristino**, salvo effetti che dicono altro.
- Essere ruotata **non** rende una carta attaccabile. Si attacca sempre il Leader (salvo la parola chiave Caccia).

::: ricorda Agire costa la difesa
Se attacchi con un'Unità, resta ruotata per tutto il turno dell'avversario e non potrà opporsi ai suoi attacchi. Anche un'Unità appena giocata non può difenderti nel turno avversario, perché è entrata ruotata. Scegli ogni turno chi colpisce e chi resta di guardia.
:::

## L'attacco

Un attacco è un'azione della fase principale e si risolve in **sei passi**. Il bersaglio è **sempre il Leader avversario**, salvo che il difensore si opponga con un'Unità.

[[figura:scontro|I sei passi di un attacco: in arancio decide l'attaccante, in blu il difensore.]]

### I passi

1. **Dichiarazione.** Scegli un tuo personaggio dritto e **ruotalo**. Si risolvono gli effetti "quando attacca".
2. **Opposizione (difensore).** Il difensore può ruotare **una** sua Unità dritta: diventa lei il bersaglio al posto del Leader. Il Leader non può opporsi.
3. **Impegno dell'attaccante.** Metti al centro da 0 a tutte le tue gemme di Brace, **scoperte**. Ognuna vale +{{forza_per_gemma}}.
4. **Risposta del difensore.** Dopo aver visto le tue gemme, il difensore mette al centro da 0 a tutte le sue gemme di Guardia e può giocare **al massimo una Reazione**, dalla mano o da una sua Cicatrice dritta. Le sue gemme pagano prima il costo della Reazione; ognuna delle restanti vale +{{parata_per_gemma}} (**Parata**).
5. **Confronto.** Si confrontano la Forza dell'attaccante e il valore di difesa del bersaglio.
6. **Esiti.** Le Unità sconfitte vanno negli Scarti, il Leader colpito perde una Vita, tutte le gemme impegnate tornano nella scorta e si risolvono gli effetti "quando sconfigge" e "dopo lo scontro".

### Il conto

<div class="griglia" markdown="1">
<div markdown="1">
#### <span class="att">Attacco</span>
- Forza dell'attaccante
- \+ {{forza_per_gemma}} per ogni gemma impegnata
- \+ bonus delle carte
</div>
<div markdown="1">
#### <span class="dif">Difesa</span>
- **Tempra** del Leader ({{tempra}}) oppure Forza dell'Unità bersaglio
- \+ {{parata_per_gemma}} per ogni gemma di Parata
- \+ Reazione e bonus delle carte
</div>
</div>

| Chi attacca | Chi difende | Risultato |
|---|---|---|
| Unità o Leader | **Leader** | Se l'attacco è **pari o superiore** alla difesa, va **a segno**: il Leader perde 1 Vita. Altrimenti non succede nulla. Chi attacca non viene mai sconfitto |
| Unità | **Unità** | È sconfitta l'Unità con il valore più basso. A pari sono sconfitte **entrambe** |
| Leader | **Unità** | Se l'attacco è pari o superiore, l'Unità è sconfitta. Altrimenti non succede nulla. Il Leader non viene mai sconfitto |

**Scudo**: un'Unità con Scudo vince i pareggi quando è il bersaglio. Contro un'Unità a pari è sconfitto solo l'attaccante; contro un Leader l'Unità con Scudo è sconfitta solo se l'attacco è **superiore**.

::: prova Scudo
"Lo Scudo vince i pareggi" è la regola in vigore, ma è ancora in prova.
:::

::: esempio Un attacco al Leader
Round 5. G1 attacca con un'Unità di Forza 3 e il difensore non si oppone: il bersaglio è il Leader di G2, Tempra {{tempra}}. G1 impegna 2 gemme: attacco 3 + 2 = **5**.

G2 ha 2 gemme di Guardia. Se ne impegna 1, la difesa è {{tempra}} + {{parata_per_gemma}} = **6**: l'attacco è fermato. Se non impegna nulla, 5 contro {{tempra}}: l'attacco va a segno e G2 perde una Vita.
:::

::: esempio Una Reazione
G1 attacca il Leader con attacco **6**. G2 impegna 2 gemme di Guardia e gioca una Reazione da 1 ("L'attaccante ha −3 in questo scontro"): la prima gemma paga la Reazione, la seconda è Parata. Attacco 6 − 3 = **3**, difesa {{tempra}} + {{parata_per_gemma}} = **6**. Fermato.
:::

::: esempio Opporsi con un'Unità
G1 attacca con un'Unità di Forza 4. G2 oppone un'Unità di Forza 2 e la ruota. G1 impegna 1 gemma: 5. G2 impegna 1 gemma di Parata: 2 + {{parata_per_gemma}} = 4. Perde il valore più basso: l'Unità di G2 è sconfitta, e il Leader di G2 non ha perso Vite.
:::

### Chi decide cosa

- **Attaccante**: chi attacca (passo 1) e quante gemme impegnare (passo 3).
- **Difensore**: se e con quale Unità opporsi (passo 2); quante gemme di Guardia impegnare e se giocare una Reazione (passo 4).

Le gemme sono sempre scoperte e le scelte sono in sequenza: l'attaccante non risponde mai alla risposta del difensore.

::: ricorda Nessun bonus dura oltre l'attacco
Tutti i bonus "in questo scontro" finiscono quando l'attacco è risolto. Non esistono bonus "fino a fine turno".
:::

## Vite e Cicatrici

Quando il tuo Leader perde una Vita, la carta in cima alla pila delle Vite si gira **a faccia in su** e va tra le tue **Cicatrici**, **fresca** (cioè ruotata).

[[figura:cicatrici|Il percorso di una Vita persa.]]

### Cicatrici fresche e dritte

- Una Cicatrice **fresca** è nata in questo turno. Si tiene ruotata e si raddrizza nella **Fine** del turno.
- Una Cicatrice **dritta** si può usare: puoi giocarla come **Reazione** (se è una carta Reazione) o riprenderla in mano con **Rimarginare**.
- Le Cicatrici fresche non si usano, ma proteggono: finché il Leader ne ha almeno una, l'avversario non può dargli il colpo finale.

### Il Saldo: quante ferite per turno

Un Leader può avere al massimo **{{saldo}} Cicatrici fresche** (dal round {{saldo_late_round}}: **{{saldo_late}}**). È il **Saldo**. Se le ha già, ogni altra perdita di Vita in quel turno **si ignora**. Non serve un contatore: basta contare le Cicatrici ruotate.

::: esempio Il Saldo
Round 6. G1 colpisce tre volte il Leader di G2. Il primo e il secondo colpo creano due Cicatrici fresche. Il terzo va a segno, ma G2 ha già {{saldo}} fresche: la perdita si ignora. Nella Fine di G1 le due Cicatrici si raddrizzano.
:::

### Rimarginare

> :ruota: del Leader + 1 gemma di Brace: riprendi in mano una tua Cicatrice **dritta**.

Ogni Leader ha questa abilità. Siccome ruota il Leader, in un turno il tuo Leader **o attacca o Rimargina**. Rimarginare non ti restituisce la Vita: recuperi la carta. Puoi farlo anche con {{hand_limit}} o più carte in mano (l'eccesso si scarta nella Fine).

### Il Risveglio

Quando il tuo Leader scende a **{{awaken_at_life}} Vite o meno** (ne ha perse almeno {{vite_risveglio}}), si gira sul lato **Risvegliato**: Forza {{leader_power_awakened}}, Tempra {{tempra_risv}}, massimo di Guardia {{guard_max_awakened}} e la sua abilità del lato Risvegliato. Succede una volta sola, è permanente e può accadere anche nel turno avversario. Se era ruotato resta ruotato.

## Come si vince

### Alle Corde

Un Leader è **Alle Corde** quando ha **0 Vite**. Dal round {{corde_one_life_round}} lo è anche con **1 Vita**. Non serve segnarlo: si vede dalla Vita e dal tracciato.

### Il colpo finale

**Vinci** quando un tuo attacco va a segno sul Leader avversario mentre è **Alle Corde e non ha Cicatrici fresche**.

Siccome le Cicatrici fresche si raddrizzano solo alla fine del turno, chi va Alle Corde ha sempre **un turno intero** per reagire prima del colpo finale.

::: esempio Il colpo finale
Round 7. Il Leader di G2 ha 1 Vita. G1 lo colpisce: la Vita diventa una Cicatrice fresca e il Leader è a 0, **Alle Corde**. Un secondo colpo nello stesso turno non vince, perché c'è una Cicatrice fresca.

Nella Fine di G1 la Cicatrice si raddrizza. G2 gioca il suo turno e nella sua Fine può mettere sul Leader 1 gemma di Guardia in più, perché è Alle Corde.

Round 8: il primo attacco di G1 che va a segno è il **colpo finale**.
:::

### Tutti i modi di vincere

1. Il **colpo finale**.
2. L'avversario deve pescare da un mazzo vuoto quando ha già 0 Vite.
3. Il **Crepuscolo** (dal round {{crepuscolo_round}}): se il Leader avversario è Alle Corde nel controllo del Crepuscolo, perde.

Non esistono patte né vittorie ai punti. Se due condizioni capitano nello stesso momento, **perde il giocatore attivo**.

## La fine della partita

Il tracciato garantisce che la partita finisca. Più si va avanti, più si rischia:

| Dal round | Cosa cambia |
|---|---|
| {{saldo_late_round}} | Il Saldo sale a {{saldo_late}} Cicatrici fresche |
| {{corde_one_life_round}} | Un Leader con 1 Vita è già Alle Corde |
| {{crepuscolo_round}} | **Crepuscolo** a ogni Ripristino di G1 |

### Il Crepuscolo

Dal round {{crepuscolo_round}}, all'inizio di ogni turno di G1 (passo 2 del Ripristino), si controllano **entrambi i Leader insieme**:

- se **un solo** Leader è Alle Corde, il suo giocatore **perde**;
- se lo sono **tutti e due**, perde chi ha meno Vite; a Vite pari perde G1;
- se **nessuno** è Alle Corde, ognuno perde **{{crepuscolo_loss}} Vite**. Queste Cicatrici entrano già **dritte** e non contano per il Saldo.

Nel turno di G2 il Crepuscolo non fa nulla.

::: esempio Fine garantita
Al più tardi, un giocatore perde nel Ripristino di G1 di questi round, a seconda delle Vite che ha all'inizio del round {{crepuscolo_round}}:

| Perde al più tardi nel | Vite all'inizio del round {{crepuscolo_round}} |
|---|---|
{{fine_garantita_righe}}
:::

## Il Leader

| | Forza | Tempra | Vite iniziali | Massimo di Guardia |
|---|---|---|---|---|
| Lato Base | {{leader_power}} | {{tempra}} | {{life}} | {{guard_max}} |
| Lato Risvegliato | {{leader_power_awakened}} | {{tempra_risv}} | — | {{guard_max_awakened}} |

- Il Leader è sempre in gioco: non può essere sconfitto, rimosso né Stancato. Non può opporsi.
- **Attacca** come un'Unità, con la sua Forza. Attaccare lo ruota, quindi attacca al massimo una volta per turno.
- Contro un Leader che non si difende (Tempra {{tempra}}, niente Parata), il Leader Base deve impegnare almeno {{gemme_leader_base}} gemma per andare a segno; il Leader Risvegliato va a segno anche senza gemme.
- Ogni Leader ha **Rimarginare** e un'abilità propria per lato. Le abilità di difesa del Leader sono **sempre attive**: non lo ruotano e non costano gemme.
- Le abilità "**Quando il tuo Leader attacca**" si risolvono subito dopo la dichiarazione, **prima** che il difensore scelga se opporsi.

## Costruire il mazzo

- Esattamente **{{mazzo}} carte**, al massimo **{{copie}} copie per ID** (ROS-007 e ROS-008 sono carte diverse, anche se avessero lo stesso testo).
- Ogni carta deve avere **almeno un colore in comune col Leader**, oppure essere **Neutrale**.
- I Leader hanno 1 o 2 colori. Nel mazzo non ci sono carte-risorsa: la risorsa sono le gemme.

| Colore | Stile di gioco | Parole chiave tipiche |
|---|---|---|
| <span class="colore rosso"></span>**Rosso** | Pressione: tutte le gemme in Forza | Assalto, Impeto, Rinnovo |
| <span class="colore blu"></span>**Blu** | Difesa, Guardia, contrattacco | Scudo, Reazioni |
| <span class="colore nero"></span>**Nero** | Le ferite diventano potere | Furia, Cicatrici, costi in Vita |
| <span class="colore verde"></span>**Verde** | Caccia alle Unità | Bracconiere, Stanca, Caccia, :ruota: |
| <span class="colore neutro"></span>**Neutrale** | Collante tra i colori | qualsiasi |

## Parole chiave

<dl class="chiavi" markdown="1">
<dt>Assalto</dt>
<dd>L'Unità entra <strong>dritta</strong> e può attaccare nel turno in cui la giochi (mai nel round {{no_attack_round}}).</dd>
<dt>Scudo</dt>
<dd>Quando è il bersaglio, vince i pareggi: contro un'Unità a pari è sconfitto solo l'attaccante; contro un Leader è sconfitta solo se l'attacco è superiore. Si ruota quando si oppone, come le altre.</dd>
<dt>Impeto N: +X</dt>
<dd>Se nell'impegno hai almeno N gemme, +X in questo scontro. Quando l'Unità è il bersaglio contano solo le tue gemme di Parata (non quella che paga la Reazione).</dd>
<dt>Caccia</dt>
<dd>Quando attacca, puoi scegliere come bersaglio un'Unità avversaria, <strong>anche ruotata</strong>, invece del Leader. L'avversario può ancora opporsi con un'altra Unità, che diventa il bersaglio. L'Unità cacciata si difende con la sua Forza, la Parata, una Reazione e lo Scudo, ma non "si oppone": i suoi effetti "quando si oppone" non scattano.</dd>
<dt>Furia N: +X</dt>
<dd>+X nel Confronto se hai almeno N Cicatrici, contando <strong>tutte</strong> le Cicatrici, dritte e fresche. Rimarginare ne abbassa il numero.</dd>
<dt>Bracconiere X</dt>
<dd>Quando attacca e il suo bersaglio è un'Unità (che si oppone o cacciata), +X in questo scontro. Non vale quando è lei a opporsi.</dd>
<dt>Rinnovo</dt>
<dd>Quando attacca e sconfigge un'Unità, si raddrizza: può attaccare ancora.</dd>
<dt>Stanca</dt>
<dd>Ruota un'Unità avversaria dritta. Solo nel tuo turno e mai sul Leader.</dd>
<dt>⟳</dt>
<dd>Simbolo di costo: ruota la carta. Si può pagare solo se la carta è dritta.</dd>
</dl>

## Casi particolari

**Più effetti nello stesso momento.** Prima quelli del giocatore attivo, nell'ordine che sceglie, poi quelli del difensore. Un effetto che dice "puoi" è facoltativo.

**"Quando sconfigge" e "dopo lo scontro".** Scattano alla fine dell'attacco anche se la carta che li ha è stata sconfitta in quello stesso attacco (anche se sono state sconfitte entrambe le Unità), salvo che il testo chieda che resti in gioco.

**Controlli automatici.** Dopo ogni azione e alla fine di ogni attacco si controlla, in ordine: se la partita è finita; se un Leader deve Risvegliarsi (prima quello del giocatore attivo); se c'è Guardia oltre il massimo (torna nella scorta).

**Mazzo vuoto.** Se devi pescare e il mazzo è vuoto, invece di pescare perdi 1 Vita (rispettando il Saldo). Se il tuo Leader ha già 0 Vite, perdi la partita.

**Costi in Vita.** Se una carta ti chiede di perdere Vita come costo e non puoi perderla tutta (Saldo pieno, 0 Vite o una soglia scritta sulla carta), non puoi giocarla.

**Una Reazione a partita?** No: al massimo **una per attacco**. Puoi usarne una in ogni attacco avversario, se hai le gemme di Guardia per pagarle.

**Reazione dalle Cicatrici.** Una Reazione tra le tue Cicatrici dritte si gioca come se fosse in mano. Dopo l'uso va negli Scarti.

**Stanca nel turno avversario.** Un effetto Stanca che si risolverebbe nel turno avversario non ha effetto.

### Cosa non troverai mai su una carta

- Carte che annullano altre carte o vietano di giocarne: le Reazioni modificano un attacco, non lo cancellano.
- Scarto forzato dalla mano dell'avversario.
- Effetti sul tracciato del round o sulla Brace che riceve l'avversario.
- Blocchi che impediscono a un personaggio di raddrizzarsi per più di un turno.
- Dadi o monete: il caso sta solo nella pescata.

## Riepilogo rapido

<div class="rapido" markdown="1">
<div markdown="1">
#### Turno
1. **Ripristino**: (G1) round +1 · Crepuscolo dal {{crepuscolo_round}} · Guardia nella scorta · raddrizza · prendi la Brace
2. **Pesca** 1 (G1 non pesca nel round 1)
3. **Fase principale**: carte, abilità, Rimarginare, attacchi
4. **Fine**: Guardia (max {{guard_max}}/{{guard_max_awakened}}, +{{guard_alle_corde_bonus}} Alle Corde) · Cicatrici fresche dritte · mano max {{hand_limit}}
</div>
<div markdown="1">
#### Attacco
1. Dichiara e ruota
2. <span class="dif">Il difensore</span> può opporre un'Unità dritta
3. <span class="att">Attaccante</span>: gemme a vista, +{{forza_per_gemma}}
4. <span class="dif">Difensore</span>: Guardia, +{{parata_per_gemma}} · max 1 Reazione
5. Confronto: attacco ≥ difesa va a segno
6. Esiti, gemme nella scorta
</div>
<div markdown="1">
#### Numeri
<p>Vite {{life}} · Tempra {{tempra}} · Forza Leader {{leader_power}}/{{leader_power_awakened}}</p>
<p>Brace = round, max {{brace_max}} · G2 +1 nei round {{round_g2}}</p>
<p>Saldo {{saldo}} fresche ({{saldo_late}} dal round {{saldo_late_round}})</p>
<p>Risveglio a {{awaken_at_life}} Vite · Unità max {{max_units}} · Reliquie max {{max_relics}}</p>
</div>
<div markdown="1">
#### Vittoria
<p><strong>Alle Corde</strong>: 0 Vite (1 Vita dal round {{corde_one_life_round}})</p>
<p><strong>Colpo finale</strong>: a segno su un Leader Alle Corde senza Cicatrici fresche</p>
<p><strong>Crepuscolo</strong> dal round {{crepuscolo_round}}: chi è Alle Corde perde, altrimenti −{{crepuscolo_loss}} Vite a testa</p>
<p>Pareggio di condizioni: perde il giocatore attivo</p>
</div>
</div>

## Glossario

| Termine | Significato |
|---|---|
| **Alle Corde** | Leader con 0 Vite; dal round {{corde_one_life_round}} anche con 1 Vita |
| **A segno** | Attacco al Leader pari o superiore alla sua difesa |
| **Brace** | Le gemme che prendi nel tuo turno per giocare carte e attaccare |
| **Cicatrice** | Una Vita persa, a faccia in su. **Fresca** (ruotata) nel turno in cui nasce, poi **dritta** |
| **Colpo finale** | Attacco a segno su un Leader Alle Corde senza Cicatrici fresche: vittoria |
| **Crepuscolo** | Dal round {{crepuscolo_round}}, nel Ripristino di G1: chi è Alle Corde perde, altrimenti −{{crepuscolo_loss}} Vite a testa |
| **Difensore** | Il giocatore che non è di turno |
| **Guardia** | Gemme sul Leader, formate nella tua Fine e usate nel turno avversario |
| **Impegno** | Gemme messe scoperte in un attacco, da attaccante e difensore |
| **Opposizione** | Il difensore ruota una sua Unità dritta, che diventa il bersaglio |
| **Parata** | Ogni gemma di Guardia impegnata che non paga una Reazione: +{{parata_per_gemma}} alla difesa |
| **Personaggio** | Un'Unità o un Leader |
| **Rimarginare** | :ruota: del Leader + 1 Brace: riprendi in mano una Cicatrice dritta |
| **Risveglio** | Il Leader passa al lato Risvegliato quando ha {{awaken_at_life}} Vite o meno |
| **Round** | Un turno di G1 più un turno di G2 |
| **Ruotato** | Ha già agito: non può attaccare, opporsi né usare :ruota: |
| **Saldo** | Massimo di Cicatrici fresche: {{saldo}}, {{saldo_late}} dal round {{saldo_late_round}} |
| **Scorta** | La riserva comune di gemme. Spendere = rimettere nella scorta |
| **Tempra** | La difesa del Leader: {{tempra}} |
