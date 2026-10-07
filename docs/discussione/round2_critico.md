# Round 2: la voce del critico e playtester

> Base delle prove: le due partite giocate a mano con la bozza B in `revisione_critica_B.md` §2: Arden (Rosso/Verde) contro Maera (Blu/Nero). Entrambe sono finite al turno 7 a testa.
> Lì sono emersi tre problemi: il Leader colpisce il Leader gratis, chi finisce Alle Corde ha già perso, e la Guardia si riduce a una scelta binaria. Valuto ogni idea ibrida su una domanda sola: corregge o rompe quello che ho visto al tavolo?

## 1. Struttura del turno: round condiviso ad azioni alternate (C)

**Cosa correggerebbe.**
- I turni ripetitivi "il Leader attacca il Leader". Il difensore avrebbe una decisione dopo ogni attacco, non una sola per tutto il turno.
- La compensazione al rovescio: il secondo giocatore che colpisce per primo verrebbe sostituita dal Fulcro, una compensazione che si paga.

**Cosa romperebbe.**
- **L'Esposizione.** Al tavolo il costo di attaccare era restare Esposti per *tutto* il turno avversario: il Leader Maera sconfiggeva gratis la Scudiera nel turno dopo. In un round condiviso tutto si prepara a inizio round, quindi chi attacca con l'ultima azione non paga quasi niente. Il pilastro 2 si svuota, a meno di riscrivere l'Esposizione come "fino alla fine del prossimo round".
- **L'ordine dei passaggi.** "Passare per ultimo" diventa una strategia dominante da verificare.
- **Il simulatore.** Il branching cresce (stimo da 2 a 3 volte).

**Test A/B.**
- Varianti: turni chiusi contro round condiviso, entrambi con le correzioni del Leader.
- Metriche: decisioni del difensore per round, vittorie del primo giocatore, margine tra IA forte e IA semplice, azioni legali medie, percentuale di attacchi lanciati come ultima azione.

**Posizione.** Turni chiusi nella v0.2. Il round condiviso entra come variante, ma solo dopo che il nucleo è stabile. Non va introdotto insieme al resto, altrimenti non sapremo quale modifica ha prodotto quale effetto.

## 2. Zone

**Cosa ho visto.** Nessuna partita ha sofferto la mancanza di un "luogo". Il timore di A sulle unità "parcheggiate" non si è visto, perché il danno veniva tutto dal Leader.
Con Tempra 5 però il parcheggio può emergere: è il rischio di stallo da Scudo che segnalo nella revisione.

**Valutazione delle opzioni.**
- **Due zone contese:** raddoppiano le regole di combattimento e danno al Leader una posizione da gestire. Nessun problema osservato al tavolo verrebbe risolto.
- **Campo leggero di B:** innocuo. Dà varietà tra partite ma non corregge niente.

**Test A/B.**
- Percentuale di turni con almeno 3 unità Pronte che non attaccano.
- Percentuale di partite chiuse dall'anti-stallo, con e senza Campo.

**Posizione.** Nessuna zona nel nucleo. Il Campo leggero va come modulo, testato da solo. Contro il parcheggio la risposta va data con le carte: effetti che espongono (stile Esca) in almeno 3 colori.

## 3. Vittoria e anti-stallo

**Cosa ho visto.** Il problema è stato l'opposto dello stallo: partite troppo corte (7 turni), Crepuscolo mai attivo, e chi arrivava per primo a 0 vinceva con un turno di vantaggio.

**Valutazione delle opzioni.**
- **Soglia decrescente** (versione di B+: Saldo 3 dal turno 10, colpo finale a 1 Vita dal 13): meglio del Crepuscolo, che regala anche Cicatrici, cioè carburante. Per la mediana però non cambia nulla.
- **Punti zona:** reintroducono la vittoria ai punti e la patta. No.
- **Colpo finale legato al Fulcro:** allungherebbe di circa un round la fase Alle Corde, quindi aiuta la rimonta, ma aggiunge una condizione da ricordare. Con i turni chiusi non esiste.

**Test A/B.** Tre modi di rendere giocabile la fase Alle Corde:
- "Ultimo respiro" (2 reazioni quando sei Alle Corde);
- colpo finale legato al Fulcro;
- nessuna correzione.

Metriche: rimonte (obiettivo 20–35%), durata, percentuale di partite chiuse dall'anti-stallo.

**Posizione.** Vita, colpo finale e la Clessidra di B+ al posto del Crepuscolo distruttivo. Più "Ultimo respiro".

## 4. Economia della reazione

**Cosa ho visto.**
- La Guardia è stata quasi sempre 0 o 1.
- L'aggro arrivava a 0 Guardia perché spendeva tutto: è giusto, è il prezzo della pressione.
- Il turno migliore del difensore (B-T5 della partita 2) è venuto dagli Scudo, non dalla Guardia.

**Valutazione delle opzioni.**
- **Risorsa non spesa senza tetto, più una reazione per attacco:** il controllo che tiene 5 Brace ferma 3 attacchi al turno 5, dove l'aggro ne ha circa 3. È proprio lo stallo da hard-control che il brief vieta.
- **Risorsa non spesa con tetto, una reazione per turno:** equivale alla Guardia, solo con un nome più naturale. Va bene.

**Test A/B.** Quattro combinazioni:
- (a) una reazione per turno, Parata scalabile;
- (b) una reazione per attacco, con tetto di Guardia a 3;
- (c) una reazione per attacco, senza tetto;
- (d) Brace residua usata come Guardia, con tetto.

Metriche: attacchi al Leader fermati (obiettivo 30–45%) e percentuale di partite chiuse dall'anti-stallo.

**Posizione.**
- Una reazione per turno, con Parata scalabile.
- Accetto "Brace non spesa = Guardia" come pura riformulazione, ma solo con un tetto.
- Una reazione per attacco solo se il test (b) dà meno del 45% di attacchi fermati.

## 5. Leader e Risveglio

**Cosa ho visto.**
- **Leader Forza 3 / Tempra 5:** resta la correzione più importante. Circa il 70% delle Vite perse veniva da colpi gratuiti del Leader.
- **Risveglio a 3 Vite perse:** al tavolo Arden ha perso 4 Vite senza risvegliarsi, perché Rimarginare toglieva Cicatrici.
- **Risveglio al turno 7 (B):** nelle mie partite il Risveglio arrivava comunque tra il turno 5 e il 6. Il "non colpisco per non risvegliarlo" non l'ho visto.
  - Il turno 7 è innocuo se il Risveglio è *offensivo* (Forza +1, Tempra invariata).
  - Se il Risveglio alza la difesa, il turno 7 allunga tutte le partite.
  - Attenzione all'asimmetria: il primo giocatore si risveglia per primo.

**Rimarginare: ⟳ contro Riscossa.**
- La Riscossa (B+, pesca gratis alla prima ferita del turno) toglie la decisione finta, ma la sostituisce con un automatismo e regala carte a chi subisce l'aggro.
- Rimarginare ⟳ crea un dilemma vero: il Leader attacca oppure si cura.

**Test A/B.**
- Risveglio: solo a 3 Vite perse, contro "3 Vite perse o turno 7".
- Recupero: Rimarginare ⟳, contro Riscossa, contro Rimarginare base.
- Metriche: vittorie per numero di Cicatrici e turni con vantaggio di board senza attacchi al Leader.

**Posizione.** Tempra 5, Risveglio offensivo a 3 Vite perse o al turno 7, Rimarginare come ⟳.

## 6. Le 10 modifiche della revisione dopo il round 1

**Incondizionate:**
- n. 1 (Forza / Tempra);
- n. 3 (sequenza di combattimento);
- n. 8 (Rinnovo e Muro);
- n. 9 (Vita e Saldo);
- n. 10 (glossario).

Correggono difetti emersi giocando, qualunque struttura vinca.

**Condizionate:**
- **n. 2** (niente attacchi nel primo turno): necessaria con i turni chiusi. Con il round condiviso diventa "nessuno attacca i Leader nel round 1", come propone C.
- **n. 4** (Risveglio a Vite perse): si unisce alla clausola del turno 7 di B.
- **n. 5** (Parata scalabile): dipende dal test del punto 4.
- **n. 6** (Ultimo respiro): va confrontata con il colpo finale legato al Fulcro.
- **n. 7** (Rimarginare ⟳): va confrontata con la Riscossa.

**Ritiro:** nessuna, ma cambio l'ordine di priorità. La n. 1 è il prerequisito di ogni altra misura, perché finché il Leader colpisce gratis tutte le metriche di durata e di reazione sono falsate. Chiedo che il primo lotto del simulatore la contenga, con un singolo A/B che la confronti con la regola "Forza strettamente maggiore".
