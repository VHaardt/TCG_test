# Round 1 — Posizione dell'autore di C (Fulcro)

> Sintesi: **lo scheletro di B è il più solido, ma ha esattamente il difetto che C risolve**, cioè il turno avversario passivo e il vantaggio di tempo del primo giocatore. Propongo B come base, con il round condiviso ad azioni alternate e il Fulcro di C. A va archiviato come sistema base; ne recupero alcune idee per un'espansione.

---

## 1. Critica di A e di B

### A — Crocevia (zone)

**Punti forti**
- È l'anti-OTK più elegante dei tre. L'inerzia (1 casella per turno) è comprensibile al primo sguardo e rende *fisicamente visibile* la minaccia.
- Il dilemma "presidiare o ingaggiare" è vera profondità: combattere toglie presenza a entrambi.
- Le zone portate dai giocatori, con la scelta della nuova zona lasciata a chi è stato sfondato, sono un comeback guadagnato e danno varietà tra le partite senza casualità di output.

**Punti deboli**
- **La Verifica è una somma di Forze.** A lo ammette da solo: è il rischio Altered, "vince il numero più alto". Con 4 slot per lato e unità che entrano pronte e contano subito, il mazzo con la curva migliore vince le Verifiche senza combattere. Profondità apparente, partita contabile.
- **Il turno avversario è passivo come in Hearthstone**: una sola reazione, e conta solo la Verifica del giocatore attivo. Contro l'anti-pattern 8 fa poco più di B.
- **È il peggiore per il simulatore**: 3 zone × 4 slot × Manovre × Ingaggi × ordine delle Verifiche. Il branching per turno esplode e la valutazione di una posizione per l'IA è difficile, perché i Fronti interagiscono tra loro.
- **Il Comando automatico non lascia decisioni sulla risorsa**, e la Dottrina reintroduce proprio la "decisione solitaria" di Sam Black (lo ammette anche A).
- Il minimo realistico (7) e le stime (9–12) spostano la partita verso l'alto del range; inoltre può finire in **patta**.

### B — Cicatrici (duello di Leader)

**Punti forti**
- **È il più intuitivo.** Chi ha giocato a One Piece o Hearthstone impara le regole in 5 minuti.
- Le Cicatrici sono l'idea di comeback migliore del pacchetto: pubbliche, pagate, limitate, e con la tensione "carta in mano contro Furia".
- La regola dell'Esposizione ("la rimozione economica colpisce solo chi agisce") è un antidoto concreto all'hard-control.
- **È il più simulabile**: turni chiusi, azioni enumerabili.

**Punti deboli**
- **È ancora io-gioco-tu-guardi.** Il difensore ha **una sola reazione per l'intero turno avversario**, più l'intercetto. Se l'avversario attacca con 4 unità, conta una decisione, poi 3 attacchi in cui si guarda e basta. Lorcana e Pokémon sono criticati proprio per questo.
- **La Fornace automatica è uguale per tutti**: la ricerca la chiama "partite più scriptate", e in più premia il tempo. I dati Hearthstone (oltre 10 punti per i mazzi tempo nonostante Coin e carta extra) colpiscono B in pieno. La sua compensazione è fissa (Scintilla e carta extra), proprio il tipo che la ricerca dice non basta.
- **La Vita coperta dalla cima del mazzo** toglie 5 carte, anche chiave. È l'anti-pattern "Premi bloccati" di Pokémon, attenuato da Rimarginare ma non risolto. È anche informazione nascosta in più per l'IA.
- **Il Risveglio può scoraggiare l'attacco** (rischio 1 di B). Il comeback rischia di diventare "non colpire più del necessario", e il gioco si trasforma in un indovinello di soglie.
- **La novità è media**: è "One Piece fatto bene". Il brief chiede un prodotto *nuovo e diverso*.

---

## 2. Debolezze di C che A e B evitano (onestamente)

1. **Carico cognitivo.** Le due fasi di vittoria, la Soglia variabile, la Clessidra, i requisiti d'Aspetto e l'investimento al Passo sono troppo per un'introduzione. Su "intuitivo", B batte C senza discussione.
2. **I requisiti d'Aspetto (pip in Riserva) reintroducono lo screw di colore** alla Magic, proprio l'anti-pattern 1 che A e B evitano con una risorsa garantita.
3. **Il Colpo di Grazia "basta un colpo non bloccato" è binario**: mesi di Slancio si decidono in un round all-in, con il rischio di un finale a indovinello alla Snap. Le Cicatrici di B sono una rampa più graduale.
4. **Il tetto di 3 Slancio e la Soglia mobile sono parametri arbitrari** che il giocatore deve ricordare. L'inerzia di A è più fisica, il Saldo di B è più semplice.
5. **La fine forzata ai punti al round 15**, con la parità decisa dal Fulcro, rischia di premiare il controllo che segna 1 punto e poi blocca. Il Crepuscolo di B (perdi Vita) è più pulito: spinge senza un "vince ai punti".
6. **Le azioni alternate allungano l'albero di ricerca** rispetto ai turni chiusi di B.

---

## 3. Cosa prenderei e cosa cedo

**Da B prendo quasi tutto lo scheletro:**
- Leader sempre in gioco, Vita 5 che diventa Cicatrici, Furia e Risveglio;
- Esposto/Pronto e Scudo;
- Saldo (max 2 Vite per turno) e Colpo finale solo su un Leader già a 0;
- Crepuscolo;
- Infondere;
- tutte le leggi di design.

**Da A prendo:**
- il principio "il giocatore sfondato sceglie", da applicare al Risveglio: chi si risveglia sceglie tra 2 lati o bonus;
- la perdita di Vita come penalità del deck-out (già in B);
- le **Zone come modulo di espansione**: una sola carta Campo condivisa, portata da chi non detiene il Fulcro, con una regola locale simmetrica. È varietà alla Snap/Riftbound senza il peso delle 3 corsie.

**Da C cedo:**
- i requisiti d'Aspetto (bastano colori e Leader come in B);
- la Soglia mobile e la Clessidra (sostituite dal Crepuscolo);
- la vittoria ai punti;
- il tetto di Slancio (sostituito dal Saldo);
- l'investimento permanente di carte in Riserva (sostituito dalla Fornace).

**Di C difendo solo due cose, e sono quelle che contano:**
1. **Il round condiviso ad azioni alternate.** Risolve il punto debole numero 1 di B e trasforma la Guardia da segnalino artificiale in "Brace che non hai speso".
2. **Il Fulcro preso passando.** È la compensazione del primo giocatore che *si paga*, invece della Scintilla fissa che la ricerca boccia.

---

## 4. Base preferita: **B + "Round Condiviso" di C** (nome di lavoro: *Cicatrici e Fulcro*)

Regole concrete dell'ibrido:

1. **Scheletro B invariato**: Leader (Forza 4, Vita 5 coperta, poi Cicatrici, Risveglio a 3), mazzo da 40, 4 colori, Leader bicolori, 5 slot unità, 2 Reliquie, Esposto/Pronto, Scudo, Saldo (max 2 Vite per round), Colpo finale su un Leader già a 0 a inizio round, Crepuscolo dal round 10.
2. **Round condiviso.** All'inizio di ogni round entrambi preparano tutto, salgono di Fornace (+1, max 8), ricevono la Brace e pescano 1. Poi **si alterna un'azione a testa**, cominciando da chi detiene il Fulcro. Un'azione è una tra: giocare una carta, attaccare, infondere un'unità, Rimarginare, attivare un'abilità, passare.
3. **Guardia abolita, Brace persistente nel round.** La Brace che non hai speso resta disponibile per tutto il round: è il tuo "mana alzato" per le Reazioni. Il dilemma spendere, infondere o tenere resta identico, ma diventa naturale e non c'è un segnalino in più da gestire.
4. **Reazioni: 1 per attacco avversario** (non 1 per turno), pagate con Brace. Il difensore decide a ogni attacco, ma il bilancio resta limitato perché la Brace è una sola per tutto il round. Le Reazioni restano giocabili dalle Cicatrici.
5. **Passare.** Chi passa non fa più azioni, ma **intercetta e reagisce ancora**. Il round finisce quando passano entrambi.
6. **Il Fulcro.** Il giocatore che **non** lo detiene può "Prendere il Fulcro" come azione: equivale a passare, e il Fulcro si sposta subito (una volta per round). Il detentore agisce per primo nel round successivo. Non si può difendere: chi lo detiene non può impedire che venga preso.
7. **Colpo finale legato al Fulcro** (la mia scommessa, da validare con un test A/B nel simulatore): un Leader Alle Corde perde solo contro un avversario che ha **iniziato il round detenendo il Fulcro**. La chiusura è sempre telegrafata e costa tempo. Se i test mostrano troppo carico, si toglie e resta solo la regola Alle Corde di B.
8. **Primo giocatore.** Il Fulcro iniziale è assegnato a caso; l'altro giocatore pesca 1 carta in più e può prendere il Fulcro già nel round 1. Nessuno attacca i Leader nel round 1. La Scintilla resta solo come leva di riserva.
9. **Durata.** Un round equivale a un turno per giocatore, quindi la matematica di B resta valida: minimo 5, mediana stimata 8–10. Il Fulcro può aggiungere un round alla chiusura.

**Perché questo ibrido vince:**
- tiene l'intuitività e la simulabilità di B (azioni enumerabili, nessuna pila, una sola regola di timing: "si alterna");
- rende attivo il turno avversario per costruzione;
- trasforma il vantaggio del primo giocatore in un costo-opportunità;
- aggiunge la novità che B da solo non ha.

### Voto
1. **B** (come base, con il round condiviso e il Fulcro di C). È il miglior equilibrio tra intuitività, comeback e simulabilità; le sue due debolezze sono curabili con un innesto.
2. **C.** Ha l'idea più nuova e il turno avversario più vivo, ma così com'è è troppo carico e reintroduce lo screw di colore. Va usato come donatore, non come telaio.
3. **A.** Ha l'anti-OTK più bello, ma "vince il numero più alto", ha il turno avversario passivo e il costo per l'IA più alto. Le zone sono un'ottima espansione, non un sistema base.
