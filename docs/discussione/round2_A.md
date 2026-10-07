# Round 2 — Risposte dell'agente A

> Premessa: accetto **B come base**. Nel round 1 avevo proposto un ibrido con le zone come scheletro, ma la revisione critica mi convince. B ha due partite giocate a mente, problemi quasi solo numerici o di scrittura e lo stato più semplice da simulare. Le zone come nucleo non hanno ancora nulla di paragonabile. Cambio posizione su questo punto e mi concentro su cosa rende B migliore.

## 1. Struttura del turno → **turni classici di B**

C sostiene che B è "ancora io-gioco-tu-guardi" e che con 4 attacchi "conta una decisione, poi 3 attacchi in cui si guarda". È vero solo in parte. Nella revisione il difensore decide a **ogni** attacco: intercettare, sì o no, con quale Scudo, se lasciare passare il Leader per conservare la reazione. Le giocate migliori delle due partite (A-T5 della partita 1, A-T5 della partita 2) sono proprio decisioni difensive. Il turno avversario di B non è passivo, è **a decisioni rade ma pesanti**: è il formato giusto per chi impara.

Il round ad azioni alternate costa invece tre cose concrete:
- raddoppia la profondità dell'albero per l'IA;
- complica l'infusione, che va nella fase principale e "fuori dai combattimenti";
- ci obbliga a riscrivere la sequenza a 9 passi della revisione, appena fissata.

Lo stesso C riconosce che "le azioni alternate allungano l'albero di ricerca rispetto ai turni chiusi".

**Compromesso che accetto:** turni classici nella v0.2. Il **Fulcro di C come variante A/B nel simulatore**, da misurare sul vantaggio del primo giocatore (che è l'argomento forte di C): se la compensazione fissa resta oltre il 52%, il Fulcro entra nella v0.3.

## 2. Zone → **carta Campo leggera (B), le zone di A come espansione**

Concedo le critiche. B ha scritto "Verifica = somma di Forze", C "partita contabile": l'argomento è giusto, perché le unità che entrano pronte e contano subito premiano la curva più che la scelta. Ritiro le due zone dal nucleo.

Chiedo però che la carta Campo non sia un ornamento:
1. Ogni giocatore porta **1 Campo** dal proprio mazzo-extra. All'inizio è attivo quello del secondo giocatore (piccolo compensatore).
2. **Chi si Risveglia per primo può sostituirlo con il proprio**: è il mio principio "lo sfondato sceglie il terreno", già fatto proprio da B.
3. Regole di design per il Campo: effetti **simmetrici** e **mai** di negazione.

Le corsie con il Fronte a inerzia restano disponibili come modulo futuro (formato "Assedio"), se il simulatore mostra stalli da Scudo strutturali (rischio residuo della revisione).

## 3. Vittoria e anti-stallo → **Vita + Alle Corde (B) + Clessidra (adattata da C), niente punti né patte**

Ritiro la Gloria e la patta. B ha ragione: lo spareggio a posizioni e la patta sono il "finale-indovinello" di Snap. Il colpo finale su un Leader che era già a 0 è l'equivalente leggibile della mia inerzia: l'avversario vede sempre il colpo arrivare.

Per l'anti-stallo sostengo la versione di B del round 1, che rende "aperta" la Clessidra di C invece del Crepuscolo-martello:
- dal turno 10 il Saldo sale a 3;
- dal turno 13 il colpo finale vale anche su un Leader a 1 Vita.

È inerzia nel senso di Rosewater: lo stato neutro spinge verso la fine, senza togliere Vita a chi gioca bene.

**Colpo finale legato all'iniziativa (C): no.** Aggiunge un concetto in più proprio nel momento più teso, e la revisione mostra che il problema di Alle Corde è opposto: è *troppo facile* chiudere, non troppo improvviso. Il telegrafo c'è già (il Leader a 0 a inizio turno).

## 4. Economia della reazione → **Guardia di B, una reazione per turno, due in Alle Corde**

La differenza tra "Guardia" e "Brace non spesa che resta" (la mia posizione nel round 1) è soprattutto di nome. Il tetto che B impone (2 accantonate) è utile: rende l'informazione pubblica e il valore leggibile. Accetto i segnalini Guardia. Sono pronto a chiamarli "Brace alzata" se aiuta l'onboarding.

**Una per attacco (C): no.** Lo ha scritto B: con 3–4 attacchi si ottengono "6–8 risposte potenziali, una mini-pila", con il rischio della tassa da hand trap.

**Compromesso:**
- una reazione per turno avversario;
- **Parata scalabile** (+2 per ogni Guardia, revisione n. 5): risolve il "sì o no" segnalato dal critico;
- **Ultimo respiro** (2 reazioni da Alle Corde, revisione n. 6).

Così la "decisione per ogni attacco" che chiede C arriva quando serve davvero, senza la pila.

## 5. Leader e Risveglio

- **Leader con Forza 3 e Tempra 5: sì, pienamente.** La revisione lo dimostra: il 70% delle Vite perse viene dal Leader che attacca gratis. È l'unico difetto che rende B inadatta così com'è.
- **Risveglio a 3 Vite perse: sì.** Contare le Cicatrici *presenti* era anti-intuitivo, e la Furia conserva la tensione.
- **Rimarginare come ⟳ del Leader: sì.** È il miglior intervento della revisione: una decisione finta diventa un dilemma tra attaccare e curarsi, senza testo nuovo.
- **Risveglio anche al turno 7 (B): no**, o al massimo al turno 9 come rete. Due argomenti:
  1. la revisione mostra che il Risveglio non scoraggia l'attacco ("ogni colpo serve comunque"), quindi la toppa cura un male che non c'è;
  2. un Risveglio a tempo premia anche chi **non** ha subito colpi, cioè chi è in vantaggio. Diventa anti-comeback e cancella la storia "le ferite ti risvegliano".

  Con Forza 3 e Tempra 5, e Risvegliato a Forza 4, il Risveglio è un premio offensivo per chi sta sotto: esattamente il rubber band "guadagnato" che volevamo.

  **Compromesso:** Risveglio a tempo solo come leva di riserva, se il simulatore mostra mediane oltre il turno 11.

## 6. Le 10 modifiche della revisione

| N. | Modifica | Posizione | Nota |
|---|---|---|---|
| 1 | Leader Forza 3 / Tempra 5 | **Accetto** | Priorità assoluta. L'alternativa "strettamente maggiore" va solo nel simulatore come confronto. |
| 2 | Nessuno attacca nel primo turno | **Accetto** | Poi si ritara la mano iniziale: 6 carte oppure 5 più Scintilla, non entrambe. |
| 3 | Sequenza di combattimento in 9 passi | **Accetto** | È il contratto per il simulatore. |
| 4 | Risveglio a Vite perse | **Accetto** | |
| 5 | Parata scalabile | **Accetto con tetto** | Massimo di Guardia 2, quindi +4; 3 da Risvegliato. Muro e Grido vanno ritarati. Misurare lo stallo da Scudo. |
| 6 | Ultimo respiro | **Accetto** | Lo preferisco alla Riscossa di C come leva principale: agisce solo nel momento critico. |
| 7 | Rimarginare come ⟳ | **Accetto** | |
| 8 | Rinnovo e Muro di Scudi corretti | **Accetto** | |
| 9 | Regole su Vita e Saldo | **Accetto** | Aggiungo: la regola "perde il giocatore attivo" va estesa a ogni simultaneità futura. |
| 10 | Glossario | **Accetto** | Aggiungo la mia legge "nessuna carta annulla un'altra carta o vieta di giocare", insieme alle leggi di C (niente scarto forzato, niente lock oltre 1 round). |

**Un rischio che segnalo io:** le modifiche 1, 5 e 6 rafforzano *tutte* la difesa nello stesso momento. Se si applicano insieme, la mediana potrebbe passare da 7 a 11 o più, con lo stallo da Scudo. Propongo di introdurle **in sequenza nel simulatore**: prima la 1 da sola, poi la 5, poi la 6. Ogni passo va controllato sulla mediana (obiettivo 8–10) e sulla quota di partite che arrivano al turno 13 (obiettivo sotto il 10%).

## In sintesi
Base B v0.2 con le 10 modifiche, la Clessidra in versione "aperta" e il Campo leggero con sostituzione al Risveglio. Il Fulcro e le zone come varianti misurabili, non come nucleo.
