# Revisione critica della proposta B (bozza di regolamento) — passata da playtester

> Autore: agente critico/playtester dello swarm. Fonti: `research/proposte/bozza_pilastri_B.md`, `research/proposte/bozza_regolamento_B.md` (qui citato come "v0.1"; i § si riferiscono a questa bozza), `research/proposte/proposta_B_leader.md` (§4), `research/proposte/confronto.md`.
> Scopo: trovare ciò che un programmatore del simulatore incontrerebbe come caso non definito, giocare a mente due partite e proporre le modifiche per la v0.2. Identità da preservare: Cicatrici, triplo uso della Brace, Esposto.

## 0. Sintesi in 6 righe
1. **Il problema strutturale principale: Leader contro Leader colpisce di default** (Forza 4 ≥ Forza 4). Ogni turno il Leader fa 1 danno "gratis" e senza rischio. Nelle mie due partite circa il 70% delle Vite perse viene da attacchi del Leader.
2. Per lo stesso motivo **il secondo giocatore colpisce per primo** (il suo turno 1 ha il Leader libero di attaccare, più Scintilla e Assalto): la compensazione è rovesciata.
3. Le partite simulate durano **7 turni a testa**, sotto la mediana obiettivo di 8–10. La fase "Alle Corde" è quasi sempre una condanna: il "turno intero per reagire" è più cosmetico che reale.
4. Una sola reazione per turno e una Guardia massima di 2 rendono l'accantonamento una scelta quasi binaria (0 o 1 Guardia).
5. **Rinnovo** e **Muro di Scudi** hanno testi che contraddicono il pilastro "agire è esporsi" oppure non fanno nulla.
6. Il Risveglio conta le Cicatrici *presenti*, quindi Rimarginare lo ritarda in modo anti-intuitivo.

---

## 1. Passata da azzeccagarbugli: ambiguità e casi non definiti

Formato: **Problema** → *Fix proposto*.

### 1.1 Combattimento e sequenza
1. **Ordine dei passi e dei trigger non formalizzato.** Vesh ("quando attacca"), Sentinella ("quando intercetta") e Bastione ("quando sconfigge") non hanno un punto fisso nella sequenza.
   → *Sequenza canonica:* (a) Dichiarazione: l'attaccante diventa Esposto e si sceglie il bersaglio; (b) trigger "quando attacca"; (c) Intercetto opzionale; (d) trigger "quando intercetta"; (e) finestra di reazione; (f) confronto delle Forze; (g) sconfitte e perdite di Vita; (h) controlli di stato (Cicatrici, Risveglio, Alle Corde); (i) trigger "quando sconfigge" e "dopo il combattimento". Ogni trigger si risolve nell'ordine scelto dal suo controllore, prima quelli dell'attaccante.
2. **Un'unità che attacca il Leader non è mai sconfitta.** Lo dice solo la proposta B (§2.7), il regolamento no.
   → *Fix:* scriverlo in §8.4: "Attaccare il Leader non mette mai a rischio l'attaccante".
3. **Leader che attacca un'Unità con Forza maggiore della sua.** Il testo dice solo che "viene sconfitta l'Unità se ha Forza minore o uguale".
   → *Fix:* "altrimenti non succede nulla". Va detto esplicitamente, perché il simulatore non deve inventare un rimbalzo.
4. **Intercetto: casi limite.** Si può intercettare un attacco rivolto a un'Unità Esposta? Può intercettare un'Unità entrata in questo turno avversario? Quante volte?
   → *Fix:* qualsiasi attacco si può intercettare. Basta un'Unità con Scudo che sia Pronta: diventando Esposta, intercetta al massimo una volta per turno salvo effetti. Un intercettore Esposto resta bersaglio legale per gli attacchi successivi dello stesso turno: va detto, perché è una linea di gioco forte (esca l'intercetto, poi Bracconiere sull'intercettore).
5. **Intercetto più Parata.** È legale usare entrambi sullo stesso attacco? Si può usare per la Parata la Guardia ottenuta da Sentinella in quello stesso intercetto?
   → *Fix:* sì a entrambe le domande, perché l'intercetto precede la finestra. Va scritto, perché è la principale combinazione difensiva del Blu.
6. **"Una sola volta per turno avversario".** Non è chiaro se le finestre si aprano a ogni attacco, anche contro le Unità, e se il difensore possa lasciarne passare una per usare la reazione dopo.
   → *Fix:* la finestra si apre a ogni attacco, contro qualunque bersaglio. Si conta l'uso, non la finestra.
7. **Tattiche e infusione tra gli attacchi.** "Fuori da un combattimento" è vago.
   → *Fix:* tra due attacchi il giocatore attivo torna in fase principale e può giocare Tattiche, infondere e Rimarginare. Durante i passi (a)–(i) nessuno agisce, tranne l'intercetto e la reazione.
8. **Parità tra Leader attaccante e Unità.** Il Leader non è sconfitto, l'Unità sì. È già scritto, ma la parità è un caso frequente e il testo va reso più chiaro.

### 1.2 Brace, infusione e Guardia
9. **"Brace infusa" come quantità tracciata.** Vesh sposta "tutta la Brace infusa", Carica della Fornace chiede "almeno 2 Brace ricevute", Arden "2+ Brace in una stessa unità". Serve un contatore per ogni personaggio, non solo un +Forza.
   → *Fix:* ogni personaggio ha un contatore "Brace infusa in questo turno". La Brace spostata da Vesh si somma al contatore della destinazione, ma **non** attiva Infuso (Infuso scatta solo con l'azione di infondere).
10. **Arden: "unità" include il Leader?** Infondere è un'azione da 1 Brace: quando scatta "2+"?
    → *Fix:* introdurre il termine **personaggio** (Unità o Leader) e riscrivere: "La seconda volta che infondi in uno stesso personaggio in un turno, +1 Forza".
11. **Scadenza dell'infusione e ordine della fase Fine.** Gli effetti "a fine turno" vengono prima o dopo l'accantonamento? Possono generare Brace?
    → *Fix:* ordine della Fine: effetti "a fine turno", poi accantonamento, poi scadenza di infusioni e bonus, poi limite di mano. La Brace infusa non torna mai disponibile.
12. **Il massimo di Guardia vale per l'accantonamento o per la riserva?** Sentinella dice "nel rispetto del massimo", Lanterna dice "1 Brace in più".
    → *Fix:* esiste un solo valore, il **massimo di Guardia** (2, 3 da Risvegliato, +1 per Lanterna), e vale per la riserva in ogni momento.
13. **Il Risveglio a metà del turno avversario** alza il massimo di Guardia da 2 a 3. Dà subito la Guardia mancante?
    → *Fix:* no, alza solo il tetto.
14. **Scintilla.** Si può usare nel turno 1 del secondo giocatore e accantonarla come Guardia?
    → *Fix:* sì, è Brace a tutti gli effetti, ma va scritto.

### 1.3 Stati Pronto ed Esposto
15. **Un Leader Esposto si attacca in modo diverso?** No: il Leader è sempre un bersaglio legale. L'Esposizione per il Leader conta solo per attaccare e per usare la sua Reazione. La regola "non può usare la Reazione nel turno avversario successivo" è ridondante, perché l'Esposizione dura fino al Ripristino.
    → *Fix:* una regola sola, "un personaggio Esposto non può usare abilità di Reazione né ⟳", più una riga: "il Leader è bersaglio legale sia Pronto sia Esposto".
16. **Rinnovo** ("torna Pronta dopo aver attaccato"). Un'Unità con Rinnovo che non riattacca finisce il turno **Pronta**, quindi non attaccabile. Rinnovo diventa così un "attacca senza esporti" e tradisce il pilastro 2.
    → *Fix:* "Rinnovo: può attaccare una seconda volta in questo turno anche se Esposta; resta Esposta".
17. **Muro di Scudi** ("se ha intercettato, a fine turno torna Pronta"). A fine turno avversario non c'è più nulla da fare e il Ripristino arriva comunque, quindi la seconda frase **non fa nulla**.
    → *Fix:* "torna Pronta **subito** dopo il combattimento (può intercettare di nuovo)".
18. **Esca o abilità ⟳ su un'Unità già Esposta, ed Esposizione forzata sul Leader.**
    → *Fix:* esporre chi è già Esposto non ha effetto. Le Tattiche che espongono hanno come bersaglio solo le Unità, mai il Leader (lo dice già la legge 4, ma va scritto).

### 1.4 Vita, Saldo, Cicatrici, fine partita
19. **Saldo e "turno".** Il Crepuscolo e il Patto, nel tuo turno, contano per il tuo Saldo?
    → *Fix:* "turno" è sempre quello del giocatore attivo. Le perdite che subisci nel tuo turno (Crepuscolo, mazzo vuoto, Patto) contano per il Saldo di quel turno.
20. **Abuso del Saldo con i costi in Vita.** Una volta raggiunto il Saldo (per esempio Crepuscolo più Patto), un altro Patto di Sangue pesca senza far perdere Vita. Lo stesso vale per il "non può portarti sotto 1".
    → *Fix:* regola generale: "se un effetto ti chiede di perdere Vita come costo e non puoi perderla (Saldo, 1 Vita), non puoi giocarlo".
21. **Una Vita persa per effetto, senza attacco, su un Leader Alle Corde** fa vincere?
    → *Fix:* no. Solo un attacco va a segno come colpo finale. Tutte le altre perdite su un Leader a 0 vengono ignorate.
22. **"Va a segno" e momento del controllo.**
    → *Fix:* la Forza si confronta al passo (f), dopo le reazioni. "Alle Corde all'inizio del tuo turno" si verifica **prima** del Ripristino, quindi il tuo Crepuscolo non conta.
23. **Il Risveglio conta le Cicatrici presenti.** Rimarginare e le Reazioni giocate dalle Cicatrici le tolgono. Nella partita 1 Arden perde 4 Vite senza risvegliarsi, cosa contro-intuitiva e diversa dalla storia che racconta il pilastro 1.
    → *Fix:* Risveglio quando le **Vite perse** sono almeno 3 (cioè Vita ≤ 2). La Furia continua a contare le Cicatrici presenti: è lì la tensione interessante.
24. **Una Cicatrice creata a metà turno è usabile subito?** E il Risveglio a metà combattimento?
    → *Fix:* sì a entrambe. La carta Reazione appena finita nelle Cicatrici si può usare negli attacchi successivi dello stesso turno, se la reazione non è già stata usata. Il Risveglio si applica al controllo di stato (h), quindi per gli attacchi successivi la Forza del Leader è già 5. È un bel momento di gioco e va dichiarato.
25. **Crepuscolo, mazzo vuoto e simultaneità.** Nel set base non possono capitare insieme a due giocatori, ma un effetto futuro potrebbe farlo.
    → *Fix:* regola di riserva: "se entrambi perdono nello stesso momento, perde il giocatore attivo".
26. **Rimarginare e limite di mano.** È legale con 8 carte in mano? Si può Rimarginare solo per abbassare la Furia o per scartare la carta a fine turno?
    → *Fix:* sì, è legale. La carta in eccesso va negli Scarti, è informazione pubblica e non serve un caso speciale.
27. **Sesta Unità o terza Reliquia.**
    → *Fix:* il gioco è illegale; non esiste la sostituzione. Questo semplifica il simulatore.
28. **Primo turno.** Il regolamento vieta di attaccare solo al primo giocatore. Il secondo, nel suo turno 1, attacca col Leader (4 ≥ 4) e con un'Unità con Assalto infusa grazie alla Scintilla: **due attacchi nel turno 1**. Vedi §2 e §4.

---

## 2. Playtest mentale

### 2.1 Mazzi
Le carte d'esempio sono 15 nomi, quindi ho riempito i mazzi con **carte vanilla segnaposto** sulla curva implicita della proposta: 2 Brace → F3, 3 Brace → F4, 4 Brace → F5.

**Mazzo A — Arden (Rosso/Verde, aggro), 40 carte.**
- 3 Scudiera di Brace, 3 Lince, 3 Carica della Fornace, 3 Vesh, 3 Esca, 2 Matriarca, 3 Colpo Mirato, 3 Recluta.
- Segnaposto: 3 Predone (2, F3), 3 Lupo (3, F4), 3 Colosso (4, F5), 3 Segugio (3, F3, Bracconiere +2), 3 Fiammata (1, Tattica, +2 Forza fino a fine turno), 2 Corridore (1, F1, Assalto).

**Mazzo B — Maera (Blu/Nero, difesa e Furia), 40 carte.**
- 3 Sentinella, 3 Muro di Scudi, 3 Bastione Vivente, 3 Penitente, 3 Patto, 3 Grido, 3 Recluta, 2 Lanterna, 3 Colpo Mirato.
- Segnaposto: 3 Guardiano (3, F3, Scudo), 3 Ombra (3, F4), 3 Colosso, 3 Divoratore (4, F3, Furia 3: +3), 2 Custode (5, F5, Scudo).

Notazione: `G1-T3` significa giocatore 1, suo turno 3. "Vita A/B" indica le Vite dei due Leader.

### 2.2 Partita 1: G1 = Arden (A), G2 = Maera (B)
- **A-T1** (1 Brace): Scudiera. Nessun attacco (regola), 0 Guardia.
- **B-T1** (1 Brace): Recluta. **Il Leader Maera attacca: 4 ≥ 4, A non ha difese → A 4.** Cicatrice di A: Predone.
- **A-T2** (2 Brace): 1 Brace infusa in Scudiera (F4 con Infuso), 1 nel Leader (F5): due minacce. Recluta intercetta Scudiera e muore. Il Leader va a segno: **B 4** (Cicatrice: Muro di Scudi, ora giocabile dalle Cicatrici).
- **B-T2** (2 + Scintilla): Sentinella. **Il Leader Maera sconfigge gratis la Scudiera Esposta**: prima scelta interessante, tra colpire il Leader e fare rimozione gratuita. Accantona 1 Guardia.
- **A-T3** (3): Lupo, poi il Leader attacca senza infusione. B gioca Muro dalle Cicatrici (+3): nessun colpo. Turno a vuoto per A.
- **B-T3** (3): Ombra. Il Leader attacca: A non ha Guardia, **A 3** (Cicatrice: Esca).
- **A-T4** (4): Rimargina Esca (1) e la gioca su Sentinella (1). Lupo sconfigge Sentinella. Leader con 2 Brace (7 con Arden) a segno: **B 3**.
- **B-T4** (4): Guardiano. Il Leader sconfigge Lupo gratis, Ombra (4) colpisce: **A 2**. Le Cicatrici di A sono 2 (ha recuperato Esca): niente Risveglio dopo 3 Vite perse (problema 23).
- **A-T5** (5): Rimargina Vesh e la gioca (Assalto, F4). A manda **prima il Leader** come esca. B lo lascia passare, **B 2**, e tiene Guardiano più Parata (F5) per intercettare Vesh, che muore. È la decisione difensiva più bella della partita.
- **B-T5** (5): Bastione Vivente, poi il Leader colpisce: **A 1**.
- **A-T6** (6): Colosso, poi Leader +2 (F7). B non ha Guardia: potrebbe intercettare con Bastione, che morirebbe (6 ≤ 7), e preferisce subire: **B 1**, Risveglio di Maera.
- **B-T6** (6): il Leader Maera (F5) colpisce: **A 0, Alle Corde**. A si Risveglia.
- **A-T7**: A porta B a 0, ma non può vincere in questo turno.
- **B-T7**: Maera ha Leader, Bastione, Guardiano e un'Unità nuova, contro una sola reazione di A. Colpo finale. **Vince G2 al turno 7.**

### 2.3 Partita 2: G1 = Maera (B), G2 = Arden (A)
- **B-T1**: Recluta.
- **A-T1** (1 + Scintilla): Scudiera con Assalto, infusa (F4), **più il Leader: due attacchi nel turno 1**. Recluta intercetta il Leader, Scudiera colpisce: **B 4**.
- **B-T2**: il Leader sconfigge Scudiera gratis. Rimargina Patto, accantona 1.
- **A-T2**: Lince. Il Leader attacca, Parata (Maera F6): **fermato**.
- **B-T3**: Patto (**B 3**, pesca), Sentinella. Il Leader colpisce: **A 4**.
- **A-T3**: Leader +2 (F7) contro Sentinella. B sceglie di non sacrificarla: **B 2**. Furia 2 attiva.
- **B-T4**: Penitente (F4). Leader +2 contro la Parata di A (6 contro 6): a segno, **A 3**.
- **A-T4**: Lupo, Leader +1 (F5). B non ha Guardia: **B 1**, Risveglio (Maera F5, Parata +3).
- **B-T5**: Bastione. Penitente (4) e Leader (5) a segno contro A senza Guardia: **A 1** (Saldo 2). Arden si Risveglia.
- **A-T5**: A deve solo portare B a 0. B ha 0 Guardia ma due Scudi: Sentinella fa da sacrificio contro il Leader (F8), Bastione intercetta Lupo infuso e lo sconfigge, Lince e Penitente pareggiano. **B resta a 1**: è il turno migliore del difensore in entrambe le partite.
- **B-T6**: il Leader (5 contro 5) a segno: **A 0**. B accantona 3 Guardia e tiene Bastione Pronto.
- **A-T6**: Vesh (Assalto) infusa a 8 viene intercettata da Bastione. Il Leader 5 incontra la Parata +3: fermato.
- **B-T7**: colpo finale. **Vince G1 al turno 7.**

### 2.4 Cosa ho osservato
- **Durata: 7 turni a testa in entrambe le partite.** È sotto la mediana obiettivo e gli scambi non sono stati eccezionali.
- **Strategia dominante: "il Leader attacca il Leader, ogni turno".** È gratis (nessun rischio), colpisce senza Brace se il difensore non ha Guardia, e con 2 Brace supera la Parata. Il turno più ripetitivo del gioco è proprio questo. Il Leader è anche il miglior removal: sconfigge gratis ogni Unità Esposta con Forza fino a 4. Quindi ogni attacco di un'Unità piccola costa quell'Unità nel turno dopo. È coerente con "agire è esporsi", ma rende il Leader il pezzo più forte in ogni ruolo.
- **Il difensore para sempre?** No. La Parata (+2) è debole contro un Leader infuso e forte sulle Unità che intercettano, perché rende l'intercetto una sconfitta per l'attaccante. Il difensore esperto **subisce i colpi del Leader** (ogni Vita è anche una carta) e spende reazione e Scudo sulle Unità. È una dinamica sana, ma va misurata.
- **Le Unità Pronte non sono un muro:** senza Scudo non difendono nulla. Il vero muro è avere **2–3 Scudo più 1 Guardia** (B-T5 della partita 2). Contro il Rosso puro, senza Esca, un mazzo con 5 Scudo potrebbe andare allo stallo, ma il Leader che colpisce gratis impedisce lo stallo in v0.1. Attenzione: se il Leader viene indebolito (cambio n. 1), lo stallo da Scudo diventa un rischio reale da misurare.
- **"Mai attaccare finché non fai 2 a turno"?** No, è il contrario: non c'è motivo di aspettare, perché colpire presto è quasi sempre giusto. Il Risveglio non scoraggia l'attacco, perché ogni colpo serve comunque. Rende però inutili le Unità F4 dopo la terza ferita, e questo spinge all'all-in prima del Risveglio.
- **Alle Corde = condanna.** Chi arriva a 0 deve fermare *tutti* gli attacchi avversari con una sola reazione e gli Scudo. Con 3 o più attaccanti avversari è impossibile. In entrambe le partite ha vinto chi ha portato l'altro a 0 per primo, con un turno di vantaggio. La rimonta guadagnata del pilastro 1 non è emersa.
- **Il primo giocatore subisce il primo colpo** in tutte e due le partite. Il secondo ha 6 carte, la Scintilla e attacca per primo: sospetto che G2 sia sopra il 52% negli aggro mirror.
- **Accantonare:** non ho mai voluto più di 1 Guardia (una reazione per turno, Parata da 1), salvo da Risvegliato. Il terzo uso della Brace è, nei fatti, un sì o no.

---

## 3. Matematica di bilanciamento

### 3.1 Soglie
Sia T la Forza del Leader difensore: 4, oppure 5 da Risvegliato.
- **Colpo base:** serve Forza ≥ T.
- **Colpo "a prova di Parata":** Forza ≥ T + 2, cioè 6 (7 da Risvegliato). Con Muro serve T + 3; con Grido o Maera, Forza − 3 ≥ T.

| Attaccante | Brace extra per un colpo base (T=4) | A prova di Parata (6) |
|---|---|---|
| **Leader F4** | **0** | 2 (con Arden: 2 danno 7) |
| Scudiera (1, F2, Infuso) | 1 (2+1+1) | 3 |
| Unità da 2 (F3) | 1 (totale 3 Brace) | 3 (totale 5) |
| Unità da 3 (F4) | 0 | 2 |
| Unità da 4 (F5) / Vesh F4 | 0 / 0 | 1 / 2 |

**Conclusione:** per le Unità la soglia 4 è giusta (il colpo base costa circa 3 Brace in tutto, cioè una carta da 3 o una da 2 più un'infusione). Per il Leader è troppo bassa: il personaggio che non costa carte e non rischia nulla ha la soglia di colpo più bassa di tutte. Dopo il Risveglio (T=5) le Unità da 3 diventano inutili come attaccanti diretti. Il salto è forte ma accettabile.

### 3.2 Colpi attesi per turno (aggro contro difesa tipica)
Modello: attaccante con M minacce valide; difensore con R ∈ {0,1} reazione efficace (cioè col margine dell'attaccante sotto il bonus) e S intercetti con Scudo. Colpi = min(2, M − R − S), con un minimo di 0.

| Turno aggro | M (Leader + Unità) | R + S tipici | Colpi attesi | Cumulativo |
|---|---|---|---|---|
| 2 | 1,8 | 0,9 | 0,9 | 0,9 |
| 3 | 2,0 | 1,2 | 0,9 | 1,8 |
| 4 | 2,6 | 1,4 | 1,2 | 3,0 |
| 5 | 3,0 | 1,6 | 1,4 | 4,4 |
| 6 | 3,3 | 1,8 | 1,5 | 5,9 |
| 7 | 3,5 | 2,0 | 1,5 → colpo finale | ≥6 |

Le 6 azioni che servono (5 Vite più il colpo finale) arrivano al **turno 6–7** per l'aggro. Nel controllo speculare il Leader garantisce comunque circa 0,8–1 colpo per turno dal turno 2, quindi si chiude al **turno 7–8**. Il Crepuscolo non entra quasi mai in gioco: ben sotto il 15%, e questo va bene. Il rischio non è lo stallo, è la **mediana troppo bassa** (circa 7).

### 3.3 Vita 5, Saldo 2 e colpo finale contro la mediana 8–10
Il minimo teorico (turno 5) è corretto e il Saldo funziona da anti-OTK. Per una mediana di 9, però, il tasso medio di colpi dal turno 2 deve essere circa **0,75 per turno**. Oggi è circa 1,0–1,2, e il surplus coincide quasi del tutto con l'attacco gratuito del Leader (0,6–0,8 colpi per turno). Se il Leader colpisce solo pagando circa 2 Brace (cambio n. 1), il tasso stimato scende a 0,7–0,85 e la mediana sale a **8–9** senza toccare Vita, Saldo o Crepuscolo. Consiglio di non toccare questi tre parametri prima di aver corretto il Leader.

### 3.4 Economia delle Cicatrici
Ogni Vita persa vale fino a +1 carta per 1 Brace. Tre colpi subiti equivalgono a circa 3 carte in più, quanto un buon motore di pesca. In v0.1 questo non basta per la rimonta, perché la partita si decide su *chi arriva prima a 0*, e lì le carte in più arrivano tardi. Rimarginare, poi, è giusto in quasi ogni turno in cui avanza 1 Brace: in queste partite l'ho fatto 5 volte su 6 occasioni. È la "decisione finta" temuta al §5.5 della proposta.

---

## 4. Le 10 modifiche raccomandate per la v0.2, in ordine di priorità

**1. Separare attacco e difesa del Leader: Forza 3, Tempra 5.**
Il Leader perde Vita se la Forza dell'attaccante è ≥ la sua **Tempra** (5). Attacca con Forza 3. Da Risvegliato: Forza 4, Tempra invariata.
*Motivo:* elimina il colpo gratis Leader contro Leader (servono 2 Brace), riporta la mediana verso 8–9, rende il Risveglio un premio offensivo invece di un muro difensivo che scoraggia l'attacco (rischio n. 1 della proposta), e mantiene il Leader forte come rimozione contro le Unità Esposte con Forza fino a 3. È una sola parola nuova.
*Alternativa da simulare:* tenere un solo valore di Forza, ma il colpo va a segno solo con Forza **strettamente maggiore**.

**2. Nessuno attacca nel proprio primo turno.**
*Motivo:* oggi il secondo giocatore attacca per primo e può farlo due volte nel turno 1 (Leader, più Assalto con la Scintilla), il che rovescia la compensazione. Con la simmetria i parametri 6 carte e Scintilla tornano a compensare solo il tempo della Fornace. Leva da tarare dopo il cambio: tenere 6 carte oppure scendere a 5 più Scintilla.

**3. Sequenza di combattimento formale con controlli di stato** (problemi 1, 6, 7, 22, 24).
Nove passi fissi. Cicatrici, Risveglio e Alle Corde si controllano dopo ogni perdita di Vita. Le Cicatrici sono subito giocabili. Le Tattiche si giocano solo tra un attacco e l'altro.
*Motivo:* è il prerequisito del simulatore (pilastro 9) e rende chiaramente leggibili i momenti più belli, come la Reazione appena uscita dalle Cicatrici.

**4. Risveglio quando hai perso almeno 3 Vite (Vita ≤ 2), non quando hai 3 Cicatrici.**
*Motivo:* oggi Rimarginare e le Reazioni giocate dalle Cicatrici ritardano il Risveglio, in modo contro-intuitivo e aggirabile. La Furia continua a contare le Cicatrici presenti: la tensione "recupero una carta o tengo la Furia" resta dove funziona.

**5. Parata scalabile: +2 Forza per ogni Guardia spesa**, sempre come unica reazione del turno.
*Motivo:* oggi accantonare più di 1 Guardia non serve quasi mai, quindi il terzo uso della Brace è binario. Con la Parata scalabile, 2 Guardia (+4) sono una vera promessa pubblica che l'attaccante deve leggere e superare con l'infusione: un duello Brace contro Brace. Va ritarata la soglia di Muro e Grido, che devono restare migliori della Parata a parità di Guardia (per esempio Muro +5 con 1 Guardia, Grido −4).

**6. "Ultimo respiro": un Leader Alle Corde ha 2 reazioni per turno avversario invece di 1.**
*Motivo:* il "turno intero per reagire" oggi è una condanna (in entrambe le partite ha vinto chi è arrivato a 0 per secondo, con un turno di vantaggio). Con due reazioni il colpo finale richiede pianificazione e la metrica delle rimonte (20–35%) diventa raggiungibile. Non crea OTK né stalli: il Crepuscolo resta il paracadute.

**7. Rimarginare diventa un'abilità ⟳ del Leader: espone il Leader, 1 Brace.**
*Motivo:* toglie la decisione finta di Rimarginare sempre e la sostituisce con un dilemma vero: il Leader attacca oppure cura le ferite. È coerente con il pilastro 2 e non aggiunge testo: è la stessa azione con il simbolo che il giocatore già conosce.

**8. Correggere Rinnovo e Muro di Scudi.**
- Rinnovo: "può attaccare di nuovo anche se Esposta; resta Esposta".
- Muro: "torna Pronta subito".

*Motivo:* il primo tradisce il pilastro 2 (attaccare senza esporsi), il secondo oggi non ha effetto.

**9. Regole generali su Vita e Saldo** (problemi 19, 20, 21).
- "Turno" è quello del giocatore attivo.
- Un costo in Vita che non puoi pagare (per il Saldo o perché hai 1 Vita) rende la carta non giocabile.
- Su un Leader Alle Corde solo un attacco va a segno.
- Se entrambi perdono nello stesso momento, perde il giocatore attivo.

*Motivo:* chiude l'abuso del Patto e rende la condizione di vittoria una funzione pura dello stato.

**10. Glossario e pulizia dei testi** (problemi 9–15, 18, 27).
- Termine **personaggio** (Unità o Leader).
- Contatore "Brace infusa in questo turno" per ogni personaggio; Infuso scatta solo con l'azione di infondere.
- Un solo **massimo di Guardia** che vale per la riserva.
- Esporre chi è già Esposto non ha effetto.
- Sesta Unità o terza Reliquia: illegale.
- Testi riscritti: Arden ("la seconda volta che infondi in uno stesso personaggio…"), Patto di Sangue ("se hai 1 Vita non puoi giocarla"), Lanterna ("+1 al massimo di Guardia").

*Motivo:* ogni frase ambigua è un `if` speciale nel simulatore. Va chiusa prima che le statistiche diventino rumore.

### Da misurare subito con il simulatore dopo la v0.2
- Quota di Vite perse per attacco del Leader: obiettivo sotto il 40%.
- Durata mediana: obiettivo 8–10.
- Vittorie di G1 per archetipo.
- % di partite al Crepuscolo con mazzi con 5 o più Scudo: è il rischio di stallo che il cambio n. 1 può far emergere.
- Guardia media accantonata: obiettivo una distribuzione non degenere tra 0, 1 e 2.
- % di turni con Rimarginare quando possibile: obiettivo sotto il 70%.

---

## 5. Verdetto per il dibattito

**Sì: la proposta B è abbastanza solida per fare da base, con alcune condizioni.**

**Perché.**
- Il nucleo regge alla prova delle regole.
- I problemi trovati sono di due tipi:
  - **numerici**: soglia del Leader, primo turno, Parata;
  - **di scrittura**: sequenza di combattimento, Rinnovo, Muro, Saldo con i costi in Vita.
- Nessuno dei due tocca l'identità del gioco. Cicatrici, triplo uso della Brace ed Esposto hanno generato le decisioni migliori delle due partite:
  - esca col Leader per attirare l'intercetto;
  - subire il colpo del Leader per conservare intercetto e Parata per le Unità;
  - Leader che sceglie tra colpire il Leader avversario e la rimozione gratuita;
  - doppio Scudo in Alle Corde.
- Lo stato è discreto e le azioni sono enumerabili: per il simulatore resta l'opzione più economica, come dice già `confronto.md`.

**Cosa le serve per diventare il regolamento v0.2**, in ordine di priorità:
1. **Leader con Forza 3 e Tempra 5** (o la regola del "strettamente maggiore"). Senza, la partita si riduce a "Leader contro Leader ogni turno" e la mediana resta intorno a 7. Questo è l'unico difetto che, se non corretto, renderebbe B inadatta.
2. **Nessun attacco nel primo turno di ciascun giocatore.**
3. **Sequenza di combattimento formale** con controlli di stato.
4. **Una vera rimonta in Alle Corde** (Ultimo respiro, oppure la Riscossa di C come leva di riserva, come già suggerito in `confronto.md`).
5. **Rimarginare con un costo di scelta** (⟳ del Leader) e **Parata scalabile**, perché i due "terzi usi" non restino decisioni finte.

**Rischio residuo da dichiarare nel dibattito.** Una volta indebolito il Leader, il pericolo si sposta dallo "scontro troppo rapido" allo **stallo da Scudo**: mazzi Blu con 4–5 Scudo e Guardia contro mazzi senza effetti che espongono. Le contromisure sono già nel sistema (Esca e simili in più colori, Crepuscolo), ma vanno verificate con il simulatore prima di fissare i numeri. Se lo stallo emergesse in modo strutturale, le zone di A o l'iniziativa di C restano ingredienti da innestare come archetipi, non come nucleo.
