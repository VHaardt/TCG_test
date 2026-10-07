# Round 2 — Risposte dell'agente C (Fulcro)

> **Sintesi della mia posizione.** La revisione critica ha spostato il problema. Il difetto reale di B non è il turno passivo, ma **il Leader che colpisce gratis** e la condizione **Alle Corde che equivale a una condanna**. Per questo **ritiro la richiesta di azioni alternate e del Fulcro nella base v0.2**. In cambio chiedo una cosa sola: che il budget di reazione sia **la Guardia, non un contatore**.

---

## 1. Struttura del turno → **turni chiusi di B** (cambio idea)

**Cosa mi hanno obiettato.**
- B: «con 3–4 attacchi per round sono 6–8 risposte potenziali: di fatto una mini-pila».
- A: «fallisce due vincoli espliciti: intuitività e facilità di simulazione».

Sul primo punto hanno ragione: nel mio C anche l'attaccante rispondeva, e quello era un errore.

**Cosa mi ha convinto.** Le due partite giocate a mente dal revisore mostrano decisioni difensive vere anche a turni chiusi:
- far uscire l'intercetto con il Leader usato come esca;
- subire il colpo del Leader per conservare Scudo e Parata;
- il doppio Scudo in Alle Corde.

Il turno avversario di B non è passivo come temevo. È **povero di budget**, e questo si corregge al punto 4 senza cambiare la struttura.

**Compromesso.** v0.2 a turni chiusi. Il "round condiviso con Fulcro" resta una **variante documentata** da provare nel simulatore solo se due metriche escono male:
- la vittoria del primo giocatore resta fuori dalla fascia 48–52% nonostante le leve fisse;
- i log mostrano troppi turni avversari con zero decisioni.

Non la chiedo per principio.

## 2. Zone → **nessuna zona nella base; Campo leggero come modulo successivo**

A propone due zone con Fronte, e la sua critica a B («manca un luogo del tavolo che crei sinergie trasversali») è giusta. Però le zone reintroducono il problema che A stessa ammette («la Verifica è una somma di Forze») e raddoppiano lo spazio di stato proprio mentre stiamo tarando la soglia del Leader.

Le combo trasversali si possono ottenere con le **parole chiave ponte** di B e con i Neutrali collante.

**Compromesso.**
- Accetto il **Campo** di B (1 carta per giocatore, con una regola simmetrica) come **primo modulo dopo la v0.2**, quando durata e primo giocatore saranno stabili.
- Così si misura l'effetto del Campo isolato.
- Le due zone di A le terrei per un formato o un'espansione.

## 3. Vittoria e anti-stallo → **Vita + colpo finale; il colpo finale NON va legato all'iniziativa**

Ritiro il legame Fulcro–colpo finale: senza azioni alternate non ha senso, e aggiungerebbe un concetto.

La revisione dice anche che il rischio è **la mediana troppo bassa (circa 7), non lo stallo**: il Crepuscolo «non entra quasi mai in gioco». Quindi:
- respingo la mia Clessidra a punti, che serviva solo contro lo stallo;
- respingo anche la vittoria ai punti con patta di A.

Tra il Crepuscolo distruttivo di B v0.1 e la "Clessidra" di B+ («dal turno 10 Saldo 3; dal turno 13 colpo finale su un Leader a 1») preferisco **B+**: apre il finale invece di punire chi gioca lento. Va però misurata dopo il cambio n. 1 del revisore, perché il rischio residuo dichiarato è lo **stallo da Scudo**.

**Compromesso.** Clessidra B+ come anti-stallo. Se lo stallo da Scudo non si presenta, la semplifichiamo in una sola soglia, al turno 12.

## 4. Economia della reazione → **la Guardia è il budget, non il contatore** (il mio unico punto fermo)

B ha ragione su un punto: la Guardia **pubblica e con un tetto** è migliore della mia "risorsa non spesa senza tetto". È leggibile, e limita in modo strutturale la "tassa da hand trap". Cedo su questo.

Contesto invece la regola «una sola reazione per turno avversario». Il revisore mostra due cose:
- «Alle Corde = condanna»: con 3 o più attaccanti è impossibile difendersi;
- «non ho mai voluto più di 1 Guardia»: il terzo uso della Brace diventa un sì/no.

Per rimediare propone **due toppe separate**: Parata scalabile (n. 5) e Ultimo respiro (n. 6).

**La mia proposta unifica le due toppe:**
- **Una reazione per attacco**, solo per il difensore. L'attaccante non risponde mai.
- **Ogni reazione costa almeno 1 Guardia.** Vale anche per le carte giocate dalle Cicatrici e per l'abilità di Reazione del Leader; le Reazioni da 0 Guardia passano a 1.
- **Massimo di Guardia 2** (3 da Risvegliato, +1 con la Lanterna). Il limite è quindi già di 2–3 reazioni per turno.
- **Parata**: +2 per ogni Guardia spesa.

Così nasce una decisione vera ("concentro 2 Guardia su un solo attacco o fermo due attacchi?") e Alle Corde smette di essere una condanna **senza una regola speciale**. È una riga in meno, non una in più, e per il simulatore è la stessa cosa: un attacco apre sempre la stessa finestra, e la legalità dipende da Guardia ≥ costo.

**Compromesso.** Se B e il revisore temono che il difensore diventi troppo forte, accetto la loro versione (1 reazione per turno, più Ultimo respiro a 2 reazioni in Alle Corde, più Parata scalabile). Chiedo però di simulare entrambe le versioni con le stesse metriche: rimonte 20–35% e attacchi fermati 30–45%.

## 5. Leader e Risveglio

- **Leader Forza 3 / Tempra 5: sì, senza riserve.** È il cambio che risolve la mediana a 7 e la strategia dominante "Leader contro Leader".
- **Risveglio a 3 Vite perse: sì.** Separare il Risveglio dalla Furia mette la tensione dove funziona.
- **Rimarginare come abilità ⟳ del Leader: sì.** È meglio della mia Riscossa automatica, che B propone di adottare e che ora ritiro come prima scelta. La Riscossa elimina una decisione finta sostituendola con *nessuna* decisione; la ⟳ la sostituisce con un dilemma vero, "il Leader attacca o cura". La Riscossa resta una **leva di riserva** se le rimonte sono sotto il 20%.
- **Risveglio anche al turno 7 (B): no.** B lo propone contro il suo rischio n. 1, ma il playtest lo smentisce: «il Risveglio non scoraggia l'attacco, perché ogni colpo serve comunque». Inoltre, al turno 7 si risvegliano **entrambi**: il bonus diventa simmetrico e annulla la funzione di comeback.
  - *Compromesso:* rete di sicurezza al turno 10, solo se i log mostrano attaccanti in vantaggio che rinunciano a colpire.

## 6. Le 10 modifiche della revisione

| N. | Modifica | Voto | Nota |
|---|---|---|---|
| 1 | Forza 3 / Tempra 5 | **Accetto** | Priorità assoluta. L'alternativa "strettamente maggiore" va simulata come controllo. |
| 2 | Nessuno attacca nel proprio turno 1 | **Accetto** | Poi va ritarata la compensazione: con la simmetria, 6 carte più Scintilla potrebbero diventare troppo. Si parte da 6 carte senza Scintilla e si misura. |
| 3 | Sequenza di combattimento in 9 passi | **Accetto** | È il contratto con il simulatore. |
| 4 | Risveglio a Vite perse | **Accetto** | |
| 5 | Parata scalabile | **Accetto** | Integrata nel budget di Guardia del punto 4. |
| 6 | Ultimo respiro | **Accetto la funzione, propongo un'altra forma** | La reazione per attacco pagata in Guardia rende inutile il caso speciale. Se il gruppo preferisce il contatore, accetto la forma del revisore. |
| 7 | Rimarginare ⟳ | **Accetto** | |
| 8 | Rinnovo e Muro | **Accetto** | Erano bug contro il pilastro 2. |
| 9 | Regole generali su Vita e Saldo | **Accetto** | Aggiungo: un costo in Vita non pagabile rende la carta illegale, quindi va escluso già dall'elenco delle azioni legali. |
| 10 | Glossario | **Accetto** | Aggiungo anche "Guardia: ogni reazione costa ≥1". |

**Aggiunta per il rischio di stallo da Scudo:** una **legge di design**. Ogni colore ha almeno una risposta comune a Scudo o ai muri (esporre, ignorare lo Scudo, o colpire chi intercetta). È la stessa logica della "rimozione neutra" di A.

---

**Cosa resta di C nella base:**
- le leggi di design anti-lock;
- la Riscossa come leva di riserva;
- la reazione per attacco con budget, se passa il test.

Il resto è giusto che finisca nella variante. La convergenza su B con le correzioni del revisore è, a mio giudizio, la scelta migliore per l'utente.
