# Q-027: proposta unificata per la passata 2 (editor, 2026-10-27)

**Fonti:** le 8 shortlist della passata 1 (`discussione_*.md`) e `punti_passata1.md`. Ogni voce si vota ACCETTO, CONTRO o EMENDAMENTO; passa con 6/8 e nessun veto.

**Sostegno:** quante shortlist contengono la carta, anche se in forma diversa. "Testo" indica quante usano esattamente il testo scelto.

**Rarità:** applico il criterio di Q-026 (`../Q-026_feedback_playtest/tabella_rarita.md`). Per questo alcune carte che le shortlist davano Comuni qui risultano Rare.

## 1. Regole di glossario
- **G1, sacrificio (D1, 8/8 sulla forma (a)).** "Sacrificare: metti negli Scarti una tua Unità Pronta senza Assalto. Si sacrifica solo come costo aggiuntivo di una Tattica, e un sacrificio non dà mai come premio pescare o riprendere carte."
- **G2, anti-loop (D2, una frase).** "Un effetto che prende carte dagli Scarti non può prendere una carta che prende dagli Scarti; una carta giocata direttamente dagli Scarti, dopo l'uso, va in fondo al mazzo del suo proprietario."
  - Cade la forma "una carta *presa* dagli Scarti, quando ci torna, va in fondo al mazzo" (ponti, rosso): richiede di ricordare quali carte sono state riprese. È una memoria, come hanno notato critico, blu e nero.

## 2. Obiettivi e guardie (D5, D6)
Tutti misurati con l'IA forte, su B0c05.

**Obiettivi:**
- Unità ferme ≤ 38% per ogni Leader;
- Reazioni ≥ 0.10 per scontro;
- rimozioni ≥ 1.0 a partita, solo per i Leader non Rossi; per LDR-01 e LDR-05 il dato si riporta come costo.

**Guardie, per ogni braccio:**
- Δ01 + Δ05 ≤ +1;
- nessuna vittoria prima del R5;
- R9-5 ≤ 1;
- Leader fra 45 e 55.

**Durata:** round 13+ ≤ +2. Se un braccio cade solo per la durata, con un punto fra +2 e +4, si rimisura sul torneo completo. La rimisura si fa una volta sola, sugli stessi semi, solo se tutte le altre guardie passano, e il suo risultato è definitivo. Sopra +4 il braccio cade.

## 3. Le carte (10 nel pool, più le riserve)
| ID | Colore, tipo, costo, F, rarità | Testo finale | Unisce | Sostegno | Primitiva |
|---|---|---|---|---|---|
| NEW-I01 | Nero, Tattica, 3, —, Rara | Costo aggiuntivo: Stanca una tua Unità Pronta. Sconfiggi un'Unità avversaria Pronta con costo ≤3. | PC1, N11, C01, 302 | 8/8; testo 7/8 (il nero: "anche Pronta") | nessuna (`stanca_own` c'è) |
| NEW-I02 | Nero, Tattica, 2, —, Rara | Costo aggiuntivo: sacrifica una tua Unità Pronta senza Assalto. Sconfiggi un'Unità avversaria, anche Pronta, con costo ≤4. | N31, 305, V10, P02, C06 | 8/8; Nero 7/8 (il critico: Verde) | `sacrifice` |
| NEW-I03 | Blu, Tattica, 3, —, Rara | Costo aggiuntivo: Stanca una tua Unità Pronta. Riporta in mano al suo proprietario un'Unità avversaria con costo ≤4. | B20, PC3, C02, P01, 301 | 8/8; testo 5/8 | `bounce` |
| NEW-I04 | Neutrale, Reazione, 0, —, Rara | Giocala solo se il bersaglio è una tua Unità e nel tuo impegno non hai gemme. Il bersaglio ha +2 in questo scontro. | 309, V13 | 8/8; testo 6/8; Neutrale 5/8 (Verde 3/8) | condizione `play_if`; costo 0 da verificare |
| NEW-I05 | Neutrale, Reazione, 1, —, Rara | L'attaccante ha −2 in questo scontro. Se la giochi da una tua Cicatrice, pesca 1. | C12, PC8 | 6/8; testo 4/8 (critico e verde: "pesca sempre") | nessuna |
| NEW-I06 | Nero, Reazione, 1, —, Rara | L'attaccante ha −2 in questo scontro. Se la giochi da una tua Cicatrice, dopo lo scontro sconfiggi l'attaccante, se è un'Unità con costo ≤2. | N51, P09, C12 | 8/8; testo 7/8 (il nero: −3) | nessuna |
| NEW-I07 | Blu, Reazione, 1, —, Rara | L'attaccante ha −3 in questo scontro. Puoi giocarla anche dai tuoi Scarti pagando 1 gemma in più; in quel caso, dopo lo scontro, mettila in fondo al tuo mazzo. | C05 "Eco", N22 | 2/8 (critico, nero), più la riserva del blu | gioco dagli Scarti |
| NEW-I08 | Nero, Unità, 3, F2, Rara | Quando entra, se hai almeno 2 Cicatrici, riprendi in mano dai tuoi Scarti un'Unità con costo ≤2 che non ha "Quando entra". | N21, C04, PC4, 303, P03 | 8/8; "senza Quando entra" 4/8 | `recover` |
| NEW-I09 | Nero, Unità, 3, F2, Rara | Quando il tuo Leader Rimargina, Stanca un'Unità avversaria Pronta con Forza attuale pari o inferiore alle tue Cicatrici. | N41, PC7, B24, C08, P07, V11, 308 | 8/8 sul tipo; questa forma 4/8 | `on_rim` |
| NEW-I10 | Verde, Unità, 2, F2, Comune | Quando il tuo Leader Rimargina, se questa Unità è Ruotata, raddrizzala. | V12, 307, PC6, R16 | 6/8; Verde 3/8 (Rosso 2, Neutrale 1) | `on_rim` |

**Perché queste versioni:**
- **I01:** le Pronte si rimuovono pagando lo Stanca solo nel Nero, l'unico colore che non va né a LDR-01 né a LDR-05.
- **I03:** il rimbalzo blu è una Tattica, non una Reazione, come chiedeva il competitivo. Al voto c'è un emendamento "Pronta" (analista, critico, competitivo), che punterebbe dritto sulle Unità ferme.
- **I04:** il bersaglio è solo un'Unità, come chiedeva il critico, così il Leader non arriva a 6.
- **I08:** la clausola "senza Quando entra" chiude il giro sacrificio → recupero → nuovo ingresso. L'ha scelta il competitivo; sul punto i ruoli sono 4 contro 4.
- **I09:** la soglia scende proprio quando Rimargini, e non ci sono Stanca ripetute a ogni turno: niente lock R9-5. È nera, quindi lontana dai Rossi; la forma "costo ≤3" in Blu andrebbe a LDR-05.
- **I07:** è la seconda carta del cimitero, l'unica che usa la seconda metà di G2. Ha poco sostegno: è la prima da tagliare se la lista scende a 10.

**Colori:** Nero 5, Blu 2, Neutrale 2, Verde 1, Rosso 0. **Rarità:** 9 Rare, 1 Comune.

**Riserve, non nel pool:**
- **R15**, Rosso, Unità: si sacrifica mentre attacca. Rientra solo quando i Rossi tornano in fascia.
- **P08**, Reazione che rimbalza (PC9, C10, V14). Ha 7/8 in passata 1, ma è esclusa dal vincolo del competitivo (difesa d'attrito, R9-5). Il voto può riammetterla con un emendamento.
- **V06**, Tattica verde di K2 (4/8). Il verde l'ha ritirata, perché la carta andrebbe a LDR-01.
- **Cura "risucchio"**, solo se Vittorio vuole le cure (C13, PC10, B28, 311, R19; la forma è unanime, ma tutti votano contro). Testo: Nero, Unità, costo 4, F3, Epica: "Quando un suo attacco fa perdere una Vita al Leader avversario, se il round è ≤12, puoi rimettere una tua Cicatrice dritta sotto il tuo Leader come Vita. Il tuo Leader resta Risvegliato."

## 4. Errori segnalati e correzioni
- **V14 ("Dopo lo scontro, Stanca…").** La Stanca si risolverebbe nel turno avversario, e per Q-016 non ha effetto. La carta è esclusa; la sua "coda" sopravvive solo in P08, in riserva.
- **P01 (rimbalzo "risposta al boss").** Il tetto ≤4 non arriva al boss da 6, quindi la motivazione era sbagliata. Il tetto resta (I03), perché tiene fuori NEW-B06 e NER-022. La risposta al boss resta quella della guardia M3 di Q-026: le Stanca senza tetto (VER-017, NEU-018, NEW-V05) e BLU-019.
- **B26 ("quando giochi una Reazione, pesca 1").** Insieme a I04, che costa 0, diventerebbe un motore di pesca: una carta a ogni attacco avversario. Resta fuori. Se tornerà, avrà la condizione "se hai pagato almeno 1 gemma".
- **S8, il critico chiede se un'Unità raddrizzata può attaccare di nuovo.** **Sì.** Il regolamento v0.2 §7 dice che un personaggio Ruotato non può attaccare e che si raddrizza nel Ripristino "oppure prima se un effetto lo dice". Il §9 dice del Leader "salvo effetti che lo raddrizzano". ROS-002 e Rinnovo già concedono un secondo attacco. Conseguenze:
  - **Cade la forma "raddrizza un'altra Unità"** (S8, PC6, R16): darebbe un secondo attacco all'Unità migliore.
  - **Resta I10, che raddrizza solo sé stessa.** Rimarginare usa la ⟳ del Leader, quindi l'attacco del Leader (F3 o F4) si scambia con un secondo attacco di un'Unità F2. Non c'è nessun attacco netto in più, e non serve una frase "non può attaccare". Resta la guardia Δ01 ≤ +1, perché il Verde va a LDR-01.

## 5. Bracci di misura
Proposta dell'analista: IA forte, su B0c05, 200 partite per incrocio, 2 copie per carta nelle liste dei Leader non Rossi, con i contatori (a)–(f). Ogni braccio si misura anche sulla lista di rottura del Leader che riceve le carte (competitivo, critico).

| Braccio | Carte | Dove vanno | Ore |
|---|---|---|---|
| **A, Reazioni** | I04, I05, I06 | Thorn e Maera (protagonisti 4 e 2); I06 solo in Maera | 7.2 |
| **B, rimozioni e sacrificio** | I01, I02, I03 | LDR-06 e Maera (protagonisti 6 e 2); I03 solo in Maera | 7.2 |
| **C, cimitero e Rimarginare** | I07, I08, I09, I10 | Maera per I07–I09, LDR-06 per I08–I10 (protagonisti 2 e 6) | 7.2 |
| **D, riserva** | "−3 → −4" sulle 6 gemelle | torneo completo | 12 |

- **Totale:** 21.6 ore, che diventano 33.6 con D.
- **C costa più delle 4 ore dell'analista** perché I10 è verde e deve andare in LDR-06. Senza I10 si torna a 4 ore, solo in Maera.
- **D è respinto in maggioranza.** Contrari critico, blu e competitivo; analista e rosso lo tengono come facoltativo o in riserva. Tocca carte delle liste rif_, quindi conta fra le 5 modifiche di Q-026. Si lancia solo se A non porta le Reazioni a 0.10.

## 6. Primitive per il thread principale, in ordine
1. **`bounce`** (I03).
2. **`on_rim`** (I09, I10).
3. **`sacrifice`** (I02), con le regole G1.
4. **`recover`** (I08), poi il gioco dagli Scarti (I07), con le regole G2.
5. **Verifiche da fare subito, in parallelo:**
   - se `valida` e il motore accettano una Reazione a costo 0. Il §8 C4 (a) lo permette già ("si gioca solo se le gemme impegnate ne pagano il costo"), ma va tolto l'eventuale vincolo di set "costo ≥1";
   - la condizione "nessuna gemma nel tuo impegno" per I04. `target_is_unit` esiste già.
6. **`heal`** per ultima, e solo se Vittorio vuole le cure.

I01, I05 e I06 si scrivono già oggi nel DSL.
