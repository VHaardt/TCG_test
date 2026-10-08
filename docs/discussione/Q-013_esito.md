# Q-013 — Esito finale (dopo il round 3): nucleo v0.2

| Campo | Valore |
|---|---|
| Redatto da | editor (non vota), 2026-10-08 |
| Base | `esito_r2.md`, `esperimento.md`, gli 8 `r3_<ruolo>.md`, `esperimenti/E-014/sintesi_r3.md` (§1–§7) e gli `esito.md` di `E-014/V1_tempra4`, `V3_tempra4`, `V4_tempra4`, `esplorazione`; i report di `E-014/V2_tempra4`, `scudo_tempra4`, `incroci` |
| Soglia | ≥3/4 dei votanti, cioè **6 su 8**. Conta il voto del r3. Dove un votante ha scritto una regola condizionale ("se la misura dà X voto Y"), l'editor applica la sua regola ai dati di sintesi_r3 §7 e lo dichiara |
| Votanti | analista (An), architetto (Ar), critico (Cr), designer_blu (Bl, avvocato del diavolo), designer_nero (Ne), designer_ponti (Po), designer_rosso (Ro), designer_verde (Ve) |
| Stato | **RATIFICATO il 2026-10-08**: 8 APPROVO su 8, nessun CONTESTO (tabella in fondo). Note non bloccanti dei votanti nella sezione "Note di ratifica"; due imprecisioni del testo corrette senza cambiare decisioni (P3, P6, §5.1) |
| Livello | 3. Serve anche l'ok di Vittorio solo dove la decisione tocca un vincolo o cambia un pilastro (sezione "Da segnalare a Vittorio") |

Legenda: **DECISO** = almeno 6/8. **APERTO** = meno di 6/8: vale il default con più voti e diventa variante con metrica per il ciclo successivo (protocollo livello 3, "Senza maggioranza dopo il round 3").

---

## 1. Esito in breve

| # | Punto (sintesi_r3 §6) | Stato | Scelta |
|---|---|---|---|
| 1 | Tempra del Leader | **DECISO 8/8** | **4** (Base e Risvegliato) |
| 2 | Pugno coperto o sequenziale (V1) | **DECISO 8/8** | **sequenziale**: l'attaccante impegna a vista, poi il difensore risponde |
| 3 | Pugno contro carte scoperte (V2) | **DECISO 8/8** (2 voti diretti + 6 condizionali risolti dalla misura §7) | **il pugno resta** |
| 4 | Opposizione (V3) | **DECISO 8/8** | **prima** dell'impegno |
| 5 | Raddrizzo (V4) | **DECISO 8/8** | **nel Ripristino** del controllore |
| 6 | Compensazione di G1 | **APERTO** (2-2-1-1-1-1) | default **G2 +1 gemma nel round 1 e +1 nel round 3**, per spareggio (vedi P6) |
| 7 | Scudo | **APERTO 5/8** | default **vince i pareggi** (cambia il default del r2) |
| 8 | Cicatrici fresche | **DECISO 8/8** sul principio | confermate come in B0; due correzioni proposte, non votate (in coda e al thread carte) |
| 9a | Reazioni dei Leader | **DECISO 8/8** | **statiche** |
| 9b | Costo delle Reazioni in gemme di Guardia | **APERTO** (3 va bene / 4 non va bene / 1 astenuto) | resta la regola 4b di B0; i rimedi vanno al thread carte e a una misura diagnostica |

Il nucleo che ne esce è B0 con quattro modifiche (Tempra 4, impegno sequenziale, Scudo che vince i pareggi, Scintilla su due round) e una riformulazione conseguente (Infuso letto sulle gemme impegnate). La specifica completa è in fondo (sezione A).

**Il punto debole, detto da quasi tutti:** Tempra 4 è votata 8/8 ma **6 pre-mortem su 8** (Ar, Ro, Ne, Po, Cr, An) prevedono che sia proprio Tempra 4 a essere tolta, per rimonte troppo basse (14.3%, fascia dei pilastri 20–35) o per mediana sotto 8 con le carte del set. Il voto è unanime, la fiducia no: le condizioni di revisione (§3) vanno prese sul serio.

---

## 2. Punto per punto

### P1. Tempra — **DECISO 8/8: Tempra 4**
- **Motivo.** È l'unica leva, fra quelle provate una alla volta, che porta B0 nelle fasce. Le altre (Parata +1, Guardia max 1, Scintilla 2) muovono 1–4 punti, Tempra circa 20 (tutti e 8).
- **Evidenza.** `E-014/esplorazione/esito.md`: B0 fermati 53.9 → 34.3, mediana 11 → 8, round 13+ 13.2 → 0.0. Sulla base finale (sequenziale + T4): fermati 42.0, mediana 8, round 13+ 1.5, 0.0% di vittorie prima del round 5 (sintesi_r3 §5). Cr ha controllato a mano l'OTK: con Saldo 2 e colpo finale senza fresche la vittoria minima resta al round 5.
- **Minoranza.** Nessuna nel voto. Costo dichiarato da Cr, Ne, Bl, Ro: le rimonte scendono da 34.8 (B0, T5) a 14.3, sotto la fascia dei pilastri 20–35; negli incroci fra mazzi diversi sono al 6.7% (sintesi_r3 §7).
- **Nota dell'editor (non votata, da segnalare).** Con Tempra 4 il Leader Risvegliato (Forza 4) va a segno a pugno vuoto su un Leader che non para e non oppone. Il testo del pilastro 2 ("Il Leader non colpisce gratis: con Forza 3 contro Tempra 5 deve investire Brace") non è più vero sul lato Risvegliato. Nessun votante lo tratta; è collegato al ripiego di Cr (Tempra 4 sul Base e 5 sul Risvegliato) e all'aritmetica delle soglie di Bl (controcaso 2).
- **Condizione di revisione.** Vedi §3: rimonte e mediana nel primo ciclo del set.

### P2. Pugno coperto o sequenziale (V1) — **DECISO 8/8: sequenziale**
- **Motivo.** La regola di V1 (`esperimento.md` §5) tiene il coperto solo se valgono S1, S2 e "A nelle fasce". S2 è misurabile e fallisce due volte con lo stesso segno: margine(coperto) − margine(sequenziale) = −16.7 con T5 e −23 con T4. L'abilità conta di più quando il difensore risponde vedendo. In più il sequenziale porta le rimonte da 7.8 a 14.3 (+6.5 [+4.5, +8.5]), lascia intatto il pilastro 9, toglie la primitiva "decisione simultanea" e il rischio di barare al tavolo (Ar, Cr, An).
- **Evidenza.** `E-014/V1/esito.md`, `E-014/V1_tempra4/esito.md`. An unisce le due misure (96 partite per braccio): IA forte 57.3% col coperto contro 77.1% col sequenziale, differenza −19.8 [−33, −7].
- **Minoranza.** Nessuna nel voto. **Controcaso 2 dell'avvocato del diavolo (Bl)**: col sequenziale il combattimento diventa una soglia. L'attaccante ha due mosse sensate (0 gemme, oppure la soglia garantita T + 2G − F) e il dato lo conferma (pugno d'attacco vuoto 70%, pieno 17%). L'exploit "drenaggio" (Unità F4 a pugno vuoto contro T4 per consumare la Guardia, poi il Leader con 1 gemma) premia chi è avanti di board. Bl ricorda anche l'obiezione di An al r2: in un sottogioco a informazione perfetta il margine dell'IA forte misura soprattutto la profondità di calcolo dell'MCTS.
- **Condizione di revisione.** Rimonte ≥20% nel ciclo del set (Bl); se restano sotto, si misura subito la variante in coda di Po (il difensore impegna per primo, a vista). Il motore deve riportare la quota di scontri **decisi prima dell'impegno** (l'attaccante non arriva alla soglia oppure la garantisce): sopra il 60% Bl la considera una conferma del controcaso. Ro, Po e An riaprirebbero il coperto con un S2 su ≥300 (An) o ≥500 (Ro) partite per braccio che rovesci il segno.

### P3. Pugno contro carte scoperte (V2) — **DECISO 8/8: il pugno resta**
- **Voti.** Confermano il pugno subito: Bl, Po (2). Chiedono l'A/B di V2 su T4 prima della ratifica: Ar, Ro, Ne, Ve, Cr, An (6). L'A/B è stato fatto dopo i voti (sintesi_r3 §7, `E-014/V2_tempra4/`).
- **Applicazione delle regole scritte dai votanti ai dati §7.**
  - *Regola di V2* (`esperimento.md` §5, che citano Ne, Ve, An): B è nelle fasce, quindi il pugno resta se margine(A) − margine(B) ≥ +5, con la clausola di validità. Clausola: regge (margine del pugno +28.7 [+23.7, +32.9], sopra 0). Differenza: **+6.7** (IC della differenza circa ±6.6). **→ il pugno resta.**
  - *An*: chiedeva ≥300 partite per braccio con l'IA forte, altrimenti S2 "non misurabile". Sono 300. → vale la regola di V2 → pugno.
  - *Ar*: vota la risposta unica solo se il braccio scoperto è più vicino a 50 su G1 di almeno 2 punti. G1 scoperto 58.5 contro pugno 55.7: lo scoperto è **più lontano**. → pugno.
  - *Cr*: se il margine è non misurabile decidono G1 e rimonte appaiati. Il margine è misurabile; comunque G1 favorisce il pugno (+2.9 [+1.5, +4.2] per lo scoperto) e le rimonte non distinguono (+0.8 [−1.4, +3.0]). → pugno.
  - *Ve*: vota lo scoperto solo con margine ≥ +5 **a favore dello scoperto**. Non succede. → pugno.
  - *Ro*: accetta lo scoperto se l'A/B gli dà ragione. Non succede. → pugno.
  - *Ne*: applica la regola di V2. → pugno.
- **Evidenza.** Tabella V2 di sintesi_r3 §7: fermati 42.0 / 41.5, round 13+ 1.5 / 0.9, durata 8.38 / 8.29, entrambi nelle fasce.
- **Limiti da dichiarare.** La soglia +5 si applica al valore puntuale, come prescrive la regola; l'estremo inferiore dell'IC della differenza è appena sopra 0, quindi la differenza di margine da sola è al limite. La regge il dato appaiato su G1, che va nella stessa direzione ed è significativo. La riserva di Bl sul margine come misura dell'MCTS vale qui per entrambi i bracci, che sono tutti e due a informazione perfetta nello scontro.
- **Minoranza.** Nessuna residua. Bl ritira il proprio braccio di controllo (motivato: con T5 era il peggiore, con T4 peggiora G1).
- **Previsioni (scritte nei r3 prima della misura §7: valide).** *Corretto in ratifica: il §5.1 rinviava qui una valutazione che mancava.* An: G1 dello scoperto +3 punti → +2.9 [+1.5, +4.2], **giusta**. Cr: G1 dello scoperto ≥2 punti sopra il pugno → 58.5 contro 55.7, **giusta**; "rimonte più basse" nello scoperto **non confermata** (+0.8 [−1.4, +3.0], non distingue). Ar: |Δ G1| ≥ 2 a favore del pugno → lo scoperto è 2.9 punti più lontano da 50, **giusta**. Gli altri cinque votanti non hanno scritto previsioni numeriche su V2.
- **Condizione di revisione.** La stessa di P2 (rimonte, scontri decisi prima dell'impegno).

### P4. Opposizione (V3) — **DECISO 8/8: prima dell'impegno**
- **Motivo.** Con T4 sono nelle fasce entrambi i bracci, e la regola di V3 dà "prima" (una decisione in meno). "Dopo" toglie 2.2 punti di rimonte [−4.4, −0.1], che sono già sotto fascia, e la sua IA è sfruttabile al 53.4%. Resta valido il caso del "chump informato" (Cr r2).
- **Evidenza.** `E-014/V3_tempra4/esito.md`: fermati −0.7, G1 +0.2 [−1.1, +1.6], mediana uguale.
- **Minoranza.** Nessuna. Ar e Ne abbandonano "dopo" (motivato col dato).
- **Condizione di revisione.** Nessuna proposta specifica dai votanti.

### P5. Raddrizzo (V4) — **DECISO 8/8: nel Ripristino del controllore**
- **Motivo.** Con il raddrizzo nella Fine il gioco si blocca su entrambe le basi: 86.6% di partite al round 13+, mediana 15, opposizioni 48.4% (fuori dalla fascia 15–35 di Ar). Il "opporsi costa l'attacco" in pratica vuol dire opporsi sempre (Ar, Po). Il pilastro 2 diventa "agire costa la difesa".
- **Evidenza.** `E-014/V4/esito.md`, `E-014/V4_tempra4/esito.md`. La regola di V4 non decideva (nessun braccio rispetta tutte le soglie): decide il voto.
- **Minoranza.** Nessuna nel voto. **Costo dichiarato**: le Unità ferme sono al 41.8%, sopra la soglia 35 di Ve (B: 34.4); negli incroci 39.9%.
- **Chiarimento registrato.** Cr risolve l'incoerenza segnalata in `esito_r2.md` P7c: nel r2 aveva citato "a sproposito" l'opposizione che costa l'attacco; la sua posizione è "agire costa la difesa", cioè il Ripristino.
- **Condizione di revisione (pre-mortem Ve).** Se con le carte vere oltre il 40% dei turni ha un'Unità che potrebbe attaccare e resta ferma, si provano prima Caccia e Assalto nel thread carte (Unità ferme del Verde), poi si riapre il raddrizzo.

### P6. Compensazione di G1 — **APERTO**
- **Voti dopo l'applicazione delle regole di ripiego dei proponenti ai dati §7.**

| Opzione | G1 misurato (2.000 partite) [IC] | Rimonte | Proponenti e loro regola | Voto dopo la misura |
|---|---|---|---|---|
| +1 gemma a G2 nei round 1 e 2 | 47.6 [45.4–49.8] | 9.8 | Ro: "sotto 48 ripiego su Scintilla 1" · Po: "fuori da 48–52 la gemma non è la leva fine, cercare nel ritmo" · Ne: "sotto 47 preferisco Scintilla 1" (sua fascia 47–53) · Ve: "sotto 47 serve un'altra leva" | **Ne, Ve** (47.6 non è sotto 47). Ro passa a Scintilla 1. Po non è assegnabile: la sua regola rinvia a una leva "di ritmo" non specificata |
| +1 gemma a G2 nei round 1 e 3 | **50.8** [48.7–53.0] | 12.8 | Bl, An (An: sposta solo se fuori 48–52) | **Bl, An** |
| +1 gemma a G2 nei round 1 e 4 | **50.0** [47.8–52.2] | 11.0 | Cr (vincolo: vittorie prima del round 6 sotto l'1%) | **Cr** — il vincolo non è verificabile: §7 riporta solo "prima del round 5" (0.0%) |
| +1 Guardia a G2 nella Fine del round 1 | 53.7 [51.5–55.9] | 15.1 | Ar: "se resta sopra 52, 2 gemme di Guardia" | **Ar → 2 gemme di Guardia**, non misurato |
| Scintilla 1 (B0) | 55.7 | 14.3 | — | **Ro** (ripiego) |

- **Conteggio.** {1,3}: 2 · {1,2}: 2 · {1,4}: 1 · Scintilla 1: 1 · Guardia 2: 1 · non assegnabile: 1. Nessuna maggioranza: **APERTO**.
- **Default e spareggio.** Le due opzioni con più voti sono pari (2-2). L'editor non sceglie un criterio nuovo: usa la fascia G1 48–52 dei pilastri (Q-002), la metrica della variante di compensazione. *Corretto in ratifica (Bl, Ne, Ve): la versione precedente diceva che "tutti e 8" avevano dichiarato 48–52 come obiettivo, ed è inesatto: Ne ha scritto una fascia accettabile 47–53 e Ve solo una soglia di ripiego sotto il 47. Lo spareggio non cambia, perché il criterio è la fascia dei pilastri; 48–52 era anche il criterio scritto da An, Ar, Ro e Po, e nessun votante lo contesta.* Delle due solo **{1,3}** sta nella fascia; {1,2} ne esce, ed esce anche dalle regole di due dei suoi quattro proponenti (Ro, Po). **Default: G2 +1 gemma nel round 1 e +1 nel round 3**, stampato sul tracciato. Se un votante ritiene lo spareggio un tradimento della discussione, lo scrive in `CONTESTO`.
- **Previsioni (scritte nei r3 prima della misura: valide).** Giuste: Bl 50 [48–52] → 50.8; An 49.5 (48–51) → 50.8; Cr 50 ± 2 → 50.0. Sbagliate: Ro, Ne, Ve, Po (tutti ~50 per {1,2} → 47.6; per Ne il valore cade dentro la sua fascia accettabile 47–53, ma la stima puntuale era 50); Ar 50 ± 2 → 53.7. Ne prevedeva rimonte invariate (14–16) con la compensazione: sono scese a 9.8.
- **Dato da non perdere.** Tutte le compensazioni in gemme **abbassano le rimonte** (da 14.3 a 9.8–12.8), cioè peggiorano la metrica già fuori fascia. Fa eccezione solo la Guardia di Ar (15.1).
- **Interazione con P1 (regola di Cr).** Cr ha scritto: "se le rimonte restano sotto il 12% dopo la compensazione di G1, voto Tempra 4 sul Base e 5 sul Risvegliato prima di ratificare T4 piatta". Col default {1,3} le rimonte sono 12.8: la condizione **non scatta**, ma il dato è a 2.000 partite e sta a 0.8 punti dalla soglia. Con l'opzione di Cr ({1,4}, 11.0) scatterebbe, e P1 scenderebbe a 7/8 (resterebbe DECISO).
- **Variante per il ciclo successivo.** `scintilla_extra_round` ∈ {2, 3, 4} (e la Guardia 2 di Ar), 10.000 partite appaiate per braccio sulla base finale. Metrica: G1 in 48–52 (con IC); a pari, rimonte più alte; vincolo di Cr: vittorie prima del round 6 <1%.

### P7. Scudo — **APERTO 5/8**
- **Voti.** Vince i pareggi: Ar, Ro, Bl, Ve, Cr (5). Si oppone senza ruotarsi: Ne, Po, An (3). Copertura: nessuno (Ve la lascia).
- **Default: vince i pareggi** (posizione con più voti; nel r2 il default era "senza ruotarsi", 4 contro 3). L'Unità con Scudo che si oppone si ruota come le altre; nel Confronto i pari vanno a suo favore.
- **Argomenti della maggioranza.** Col raddrizzo nel Ripristino lo Scudo "senza ruotarsi" diventa un muro ripetibile, e col sequenziale il difensore gli mette la Parata esatta (Cr, Ro, Bl). È l'unica eccezione a "ruotata = ha agito", mentre "vince i pareggi" è una condizione letta in C5 come Bracconiere (Ar, Cr; pilastro 9). Resta Pronto e quindi sfugge a Stanca e alla legge 7 (Ve).
- **Argomenti della minoranza.** Il muro non si vede nei dati: opposizioni 15.4%, al bordo basso della fascia 15–35, round 13+ 1.5%; indebolire lo Scudo spingerebbe le opposizioni sotto fascia (Ne, Po, An).
- **Applicazione delle regole condizionali ai dati §7.** L'A/B dello Scudo (4.000 partite appaiate, `E-014/scudo_tempra4/`) **non distingue nulla** (fermati −0.3, opposizioni −0.1, round 13+ +0.1, tutti dentro l'IC): nei mazzi convertiti gli Scudo sono pochi. Le regole di Ar ("senza ruotarsi se ≤12% al round 13+ nei matchup con ≥5 Scudo") e di Cr ("ritiro il voto se sotto il 5% nei matchup con ≥5 Scudo") chiedono una metrica **che non è stata misurata**: i dati non bastano a decidere, e nessun voto si sposta.
- **Cambi d'idea.** Ar (da "senza ruotarsi": motivato, il costo che giustificava il suo voto spariva col Ripristino). Ve (dalla Copertura: motivato con Unità ferme 41.8 e legge 7).
- **Variante per il ciclo successivo.** `oppone_senza_ruotarsi` contro `vince_pareggi` su mazzi del set con almeno 5 Scudo. Metriche: round 13+ nei matchup con ≥5 Scudo ≤12% (Ar) / <5% (Cr), opposizioni nella fascia 15–35 (Ne, Po), Blu 45–55% (esperimento.md §5). Compromesso di Cr: "senza ruotarsi" solo se resta su ≤1 Unità per colore.

### P8. Cicatrici fresche — **DECISO 8/8 sul principio; due correzioni proposte, non votate**
- **Motivo.** Il 99.3% delle partite finisce col colpo finale e lo 0.7% col Crepuscolo: fresche, Saldo e colpo finale chiudono le partite senza contatori e senza casi speciali nel motore (tutti).
- **Evidenza.** sintesi_r3 §5. Il simulatore non misura gli errori di stato al tavolo.
- **Controcaso richiesto all'avvocato del diavolo (esito_r2 P8): fatto.** Lo stesso buco lo trovano **indipendentemente** Bl (controcaso 1) e Cr:
  - Un Leader Alle Corde senza fresche, che subisce una perdita di Vita **nel turno avversario**, riceve una Cicatrice fresca e diventa immune al colpo finale per il resto di quel turno; le perdite successive si ignorano (0 Vite). Chi infligge danno peggiora la propria posizione.
  - Le vie sono due: un **costo in Vita** pagato dal difensore (es. una Reazione che costa Vita: Cr, Bl) e un **effetto che fa perdere Vite all'avversario** (Bl).
  - Il pool convertito non contiene nessuna delle due (unico costo in Vita: Patto, nel proprio turno), quindi il simulatore non può vederlo. Le carte del set Rosso e Nero lo introdurranno.
- **Correzioni proposte (nessuna votata dagli altri: i r3 sono stati scritti senza leggerli).**
  - **Cr (nucleo):** una Vita pagata **come costo** entra **dritta** e non conta per il Saldo, come il Crepuscolo. Chiude anche Patto + Saldo. Nota dell'editor: copre i costi ma **non** il danno inflitto dall'avversario (primo esempio di Bl); e una Cicatrice dritta appena pagata è subito usabile come Reazione o Rimarginabile, un'interazione nuova da verificare. Tocca la regola 12 di B0 (oggi ogni perdita di Vita crea una fresca ed è soggetta al Saldo) e v0.1 §9.3.
  - **Bl (regole di set, nucleo invariato):** gli effetti che fanno perdere Vite si risolvono solo nella fase principale di chi li controlla; nessuna Reazione ha un costo in Vita; non esistono effetti "l'avversario perde Vite" (si scrivono come "subisce un attacco"). Prese insieme chiudono entrambe le vie.
  - Le due correzioni sono complementari, non alternative. Siccome il buco è latente (nessuna carta attuale lo apre), **default: B0 invariato**; le regole di set di Bl vanno al thread carte; la correzione di Cr diventa variante di livello 3 in coda, da votare prima che il set introduca costi in Vita nel turno avversario.
- **Minoranza.** Nessuna sul principio.
- **Condizione di revisione.** Più di 1 errore di stato a partita sulle fresche in un playtest fisico → segnalino Saldo (Ar, Ro; ribadita da Ne, Po, Ve, An, Ro).

### P9a. Reazioni dei Leader — **DECISO 8/8: statiche**
- **Motivo.** Una Reazione statica non si paga con la Guardia e resta viva anche con 0.03 Reazioni per scontro (Ne, Ro). Con ⟳ competerebbe con attacco e Rimarginare e aggiungerebbe un caso di stato (Cr).
- **Cambi d'idea.** Ve (da "ruotando": motivato col dato 0.03). **Bl: motivazione debole** ("ritiro il 'ruotando': non ho dati che lo giustifichino"). Si accetta come rinuncia, non come argomento, come per Ve al r2 su P9.
- **Condizione di revisione.** Nessuna proposta.

### P9b. Costo delle Reazioni in gemme di Guardia — **APERTO**
- **Voti.** Va bene: Ar, Ro, Bl (3). Non va bene: Ne, Ve, Po, Cr (4). Astensione: An.
- **Lettura.** I quattro "non va bene" non propongono la stessa cosa e solo uno tocca il nucleo:
  - Ne: parametro di nucleo `reazione_da_cicatrice_costo −1` (minimo 0) per le Cicatrici dritte giocate come Reazione; metrica 0.10–0.25 Reazioni per scontro e rimonte in salita. È in tensione con la regola di set di Cr "ogni Reazione costa almeno 1" (Ne argomenta che l'exploit Sentinella non si apre).
  - Ve: costi bassi a livello di set (≤1 gemma, col minimo 1 di Cr).
  - Cr: regola di set "una Reazione a costo N dà più di 2N di difesa equivalente" (lo stesso ragionamento di Ar, che però giudica giusto il nucleo).
  - Po: prima misurare quante volte una Reazione era **disponibile** e non giocata.
  - An (astenuto): con 2 Reazioni nel pool e 0.15 gemme medie del difensore il collo di bottiglia può essere l'IA (λ); serve un mazzo di prova con 9 Reazioni.
  - Bl (va bene): Muro (+4) e Grido (−3) a costo 1 battono già la gemma di Parata (+2), quindi il prezzo non spiega il dato; le cause sono le 2 Reazioni del pool e l'impegno del difensore nel solo 41% degli scontri. Questo controargomento indebolisce la regola "2N" di Cr come spiegazione.
- **Default.** Resta la regola 4b di B0 (decisa 7/8 al r2). Nessuna regola di nucleo alternativa ha più di un voto.
- **Variante e misure.** (1) Diagnostica prima (Po, An): Reazioni disponibili contro giocate; mazzo di prova con 9 Reazioni. (2) Se il problema è il costo: variante di Ne. Obiettivo condiviso da Ro, Bl, Cr: **≥0.10 Reazioni per scontro** sui mazzi del set.

### Dettagli in coda sollevati dai votanti
| Dettaglio | Stato | Note |
|---|---|---|
| Furia: conta tutte le Cicatrici | **chiuso** | Ne ritira "solo dritte" (motivato: rimonte al 14.3%, una eccezione in meno); Po porta lo stesso argomento. Nessuna minoranza residua |
| Infuso N: formulazione | conseguenza di P2 | Con l'impegno a vista non c'è più un pugno chiuso da aprire: "se hai impegnato almeno N gemme in questo scontro" (Ar, Ve; Bl e Po: la condizione è pubblica) |
| Infuso N: nome | thread carte | Impeto (Bl, Po), Infuso (Ro), Ardente (Ve); Ar, Ne, Cr, An non scelgono |
| Infuso N: valore | thread carte | Pugno d'attacco pieno solo nel 17%: N ∈ {1, 2} sulle comuni, N = 3 solo su rare (Ro); N ≤ 2 sulle comuni (Ne) |
| Variante "il difensore impegna per primo" (Po r2) | in coda, **con innesco** | Si misura subito se le rimonte restano sotto il 20% nel ciclo del set (Bl) |
| Quota di scontri decisi prima dell'impegno | metrica nuova | Richiesta di Bl al motore |
| Mazzi bicolori 20/20 contro 32/8 (Po, test di mandato, 52%) | non misurato | Po lo chiede come condizione della ratifica "o almeno subito dopo": non bloccante per il voto, primo test del ciclo successivo |
| Posto di Guardia extra con la Vita vuota (Ne r2) | in coda | Non ritirato. Ne propone ora, come prima leva per le rimonte, la Guardia Alle Corde a +2 |
| Tempi delle fresche "solo nel turno avversario" (Ar, Cr r2) | in coda | Cr ora propone un'altra correzione (P8) |
| Incassa sì/no (Po, Bl r2) | in coda | Nessun r3 ne parla |
| Bersaglio scelto e "preda" (Ve r2) | in coda | Serve prima Caccia dal thread carte; Ve non lo ripropone |

---

## 3. Condizioni di revisione e pre-mortem raccolti

**Pre-mortem (una riga ciascuno).**
| Ruolo | "Tra un mese è stata tolta perché…" | Bersaglio |
|---|---|---|
| Ar | T4 tarata su 4 mazzi convertiti in mirror; coi mazzi aggressivi del set mediana 7 e rimonte sotto 20 | Tempra 4 |
| Ro | T4 ha comprato la mediana 8 al prezzo delle rimonte: chi colpisce per primo vince, gli altri archetipi sotto il 45% | Tempra 4 |
| Bl | partite decise dal conto delle soglie, nessuna rimonta: snowball scambiato per abilità da 48 partite dell'IA forte | pugno sequenziale |
| Ne | rimonte crollate, partite decise entro il round 6, il Nero non converte le ferite | Tempra 4 |
| Ve | oltre il 40% dei turni con Unità ferme: nessuno attacca con le Unità, il Verde non ha prede | raddrizzo nel Ripristino |
| Po | con Furia, Impeto, Assalto la mediana scende sotto 8 e le rimonte sotto il 10%: i mazzi misti restano indietro | Tempra 4 |
| Cr | partite decise al primo colpo a segno, giudicate già scritte al playtest | Tempra 4 |
| An | T4 tarata su mirror convertiti; coi mazzi del set mediana 7 | Tempra 4 |

**Condizioni di revisione (misurare nel primo ciclo del set, mazzi veri, anche incroci).**
1. **Rimonte ≥20%** (fascia dei pilastri 20–35). Leve proposte se restano sotto, **diverse fra loro**: variante "il difensore impegna per primo" (Bl); Guardia Alle Corde +2 (Ne, che esclude il ritorno a T5); Tempra 4 Base / 5 Risvegliato (Cr, con innesco "rimonte <12% dopo la compensazione"). Ne aggiunge: rimonte sotto il 15% anche con mazzi veri e IA forte gli fanno cambiare voto su T4. Le leve vanno misurate una alla volta; l'ordine non è stato votato.
2. **Mediana ≥8** e 0 vittorie prima del round 5. Se la mediana scende sotto 8: An propone di misurare T5 + Parata +1 + Guardia max 1 insieme; Po T5 + Guardia max 1 (round 13+ al 9.0%); Ro rimette in discussione T4. Ar chiede di guardare i round 5–6, non solo il 13+.
3. **Scontri decisi prima dell'impegno <60%** (Bl).
4. **Unità ferme ≤35–40%** (Ve): prima Caccia e Assalto, poi il raddrizzo.
5. **Reazioni per scontro ≥0.10** (Ro, Bl, Cr).
6. **G1 in 48–52** con 10.000 partite (P6).
7. **Scudo**: round 13+ nei matchup con ≥5 Scudo (P7).
8. **Playtest fisico**: tempo per turno; errori di stato ≤1 a partita (altrimenti segnalino Saldo). Il rischio di barare sul pugno chiuso non c'è più col sequenziale (Cr).
9. **Archetipi 45–55%** negli incroci coi mazzi del set (Ro): oggi Thorn 10%, Vey 72.9%, attribuiti ai mazzi convertiti.

---

## 4. Cambi d'idea

| Ruolo | Da → a | Motivo citato | Giudizio |
|---|---|---|---|
| Ar | S1 sola → sequenziale | S2 −16.7 / −23, rimonte 7.8 → 14.3 | motivato |
| Ar | opposizione dopo → prima | `V3_tempra4`: nessun effetto misurabile, IA sfruttabile | motivato |
| Ar | raddrizzo Fine → Ripristino | `V4_tempra4`: 86.6% al round 13+ | motivato |
| Ar | Scudo senza ruotarsi → pareggi | il costo che giustificava il voto sparisce col Ripristino | motivato |
| Ro, Ne, Ve, Po, An | pugno coperto → sequenziale | S2 con lo stesso segno in due misure (per Ro, Po, Ne è il loro criterio del r2) | motivato |
| Ne | opposizione dopo → prima | `V3_tempra4`: "dopo" riduce le rimonte | motivato |
| Bl, Po | raddrizzo Fine → Ripristino | 86.6% al round 13+ su due basi | motivato |
| Bl | nessun pugno (V2) → pugno | il proprio braccio è il peggiore con T5 e peggiora G1 con T4 | motivato |
| Ve | Scudo Copertura → pareggi | Unità ferme 41.8 e legge 7 | motivato |
| Ve | Reazioni Leader ⟳ → statiche | 0.03 Reazioni per scontro | motivato |
| Bl | Reazioni Leader ⟳ → statiche | "non ho dati che lo giustifichino" | **debole** (rinuncia) |
| Ne | Furia solo dritte → tutte (ritiro) | rimonte al 14.3% | motivato |
| Cr | — | nessun cambio di posizione; chiarisce l'incoerenza P7c del r2 | — |

- **Non motivati:** nessuno.
- **Premesse ritirate dal loro autore (schema di Q-012):** nessuna nuova in questo round.
- **Autocorrezioni sulle previsioni:** An (segno sbagliato su V1: previsto il coperto +4 fermati, misurato −7.7), Cr (mediana 10 → 8, fermati 35 → 42, modificatori ≤3 → max 5), Po (mediana 10 → 8). Le dichiarano loro stessi.

---

## 5. Limiti di validità (da leggere prima di ratificare)
1. **Previsioni non scritte prima del lancio.** Il passo `prev_<ruolo>.md` (esito_r2 §4.2) non è stato fatto: V1–V4 sono partiti senza previsioni, contano solo quelle già nei r2. Le previsioni su V2 e sulla compensazione scritte nei r3 **prima** delle misure §7 sono valide: la valutazione è in P3 (V2) e P6 (compensazione), e le righe sono copiate in `modelli/previsioni.md`. *Corretto in ratifica (An, Cr): il testo precedente rinviava a un "punteggio in P3" che non c'era.*
2. **Tempra 4 scelta dopo un'esplorazione fuori specifica.** Il thread del simulatore ha provato 4 leve dopo aver visto tutti i bracci fuori fascia, e V1, V3, V4 sono stati rifatti sulla leva vincente. È una scelta a posteriori sugli stessi mazzi e seed: va riconfermata su dati nuovi (mazzi del set). V3 e V4 danno lo stesso segno con T5 e T4; S2 di V1 pure.
3. **IA forte a campione ridotto.** S2 di V1: 48 partite per braccio (IC ±14–19), non 2.000 come da `esperimento.md`. V2: 300 per braccio, differenza al limite dell'IC.
4. **Solo mazzi convertiti da v0.1, quasi solo mirror.** Quattro mazzi bicolori; gli incroci (400 partite per incrocio) mostrano uno squilibrio forte (Thorn 10%, Vey 72.9%) e rimonte al 6.7% (calcolate su 733 partite con uno svantaggio, in parte gonfiate dallo squilibrio). Pochi Scudo, 2 Reazioni nel pool: Scudo e Reazioni non sono misurabili.
5. **IA nei bracci "dopo" e "Fine"** leggermente sfruttabile (53–55%); compensazione di G1 a 2.000 partite (±2.2).
6. **Nessun playtest fisico.** Tempo per turno ed errori di stato non sono misurati: la ratifica del nucleo resta condizionata (§3, punto 8).
7. **Pugno coperto contaminato** (esito_r2 §0): il punto è superato, perché i dati hanno scelto il sequenziale contro la convergenza iniziale.

---

## A. SPECIFICA CONSOLIDATA — nucleo v0.2

B0 di `esperimento.md` §1 con le modifiche di questo esito. I punti APERTI sono marcati **[default, aperto: Px]**. Parametri del simulatore fra parentesi quadre.

### A. Componenti, zone, stati
1. **Leader.** Lato Base: Forza 3, **Tempra 4**, Vita 5, Guardia massima 2. Lato Risvegliato: Forza 4, **Tempra 4**, Guardia massima 3. [`tempra` 4]
2. **Mazzo**: 40 carte, al massimo 3 copie per nome (v0.1 §2.3).
3. **Componenti oltre alle carte.**
   - **Gemme** di una sola specie in una scorta comune (circa 12 per giocatore).
   - **Carta-tracciato del round** con un segnalino. Vi sono stampati: Brace = min(round, 8); "10: Saldo 3"; "13: Alle Corde a 1 Vita"; "15: Crepuscolo"; "round 1 e 3: G2 +1 gemma" **[default, aperto: P6]**.
4. **Zone delle gemme.** Brace (davanti al giocatore); Guardia (sulla carta Leader); **impegno** (il "pugno": gemme scoperte messe nello scontro, solo durante uno scontro); scorta comune. Spendere una gemma = rimetterla nella scorta. Nessuna gemma va mai su un'Unità.
5. **Stati.** Ogni carta in campo è **Pronta** (dritta) o **Ruotata**. Ruotata vuol dire solo "ha agito" e non rende mai bersaglio. Ogni Cicatrice è **dritta** o **fresca** (ruotata).
6. **Zone delle carte** come v0.1 §3: al massimo 5 Unità e 2 Reliquie; Cicatrici pubbliche; Vita coperta. **Informazione nascosta: mano, ordine del mazzo, Vita** (pilastro 9 invariato).

### B. Preparazione
7. Come v0.1 §4 passi 1–5: G1 a caso; Leader sul lato Base, Pronti; 5 carte; mulligan da 0 a 3 carte in fondo al mazzo; 5 Vite coperte sotto il Leader. Il segnalino del round parte da 0. Nessuna gemma in gioco, nessun segnalino Scintilla.

### C. Turno del giocatore attivo
8. **Ripristino**, in quest'ordine:
   - (a) se sei G1, avanzi il round di 1;
   - (b) **Crepuscolo**: dal round 15, se il tuo Leader è Alle Corde perdi la partita; altrimenti perde 2 Vite, che entrano tra le Cicatrici **dritte** e non contano per il Saldo;
   - (c) rimetti nella scorta le tue gemme di Guardia;
   - (d) **raddrizzi i tuoi personaggi** (Leader e Unità);
   - (e) prendi dalla scorta min(round, 8) gemme come Brace; **se sei G2, nel round 1 e nel round 3 ne prendi 1 in più** **[default, aperto: P6; `scintilla_g2_gems` 1, `scintilla_extra_gems` 1, `scintilla_extra_round` 3]**;
   - (f) controlli di stato.
9. **Pesca** 1 carta; G1 non pesca nel round 1. Mazzo vuoto: perdi 1 Vita (soggetta al Saldo); se hai già 0 Vite perdi la partita (v0.1 §9.4).
10. **Fase principale.** In qualsiasi ordine e quante volte vuoi:
    - giocare carte pagando gemme di Brace; le Unità **entrano Ruotate**, con Assalto entrano Pronte;
    - usare abilità **⟳**: ruoti la carta; legale solo se è Pronta;
    - **Rimarginare**: ⟳ del Leader + 1 gemma, prendi in mano una Cicatrice **dritta**;
    - usare effetti **Stanca** (solo qui);
    - dichiarare attacchi (sezione D). Nessuno attacca nel round 1. Dopo ogni attacco si torna alla fase principale.
11. **Fine**, in quest'ordine:
    - (a) effetti "a fine turno" (nessuno nel nucleo);
    - (b) **Guardia**: sposti sul tuo Leader le gemme di Brace non spese, fino al massimo di Guardia (2 Base, 3 Risvegliato, +1 per ogni Lanterna, **+1 se il tuo Leader è Alle Corde**); le altre tornano nella scorta;
    - (c) **tutte le Cicatrici fresche di entrambi i giocatori si raddrizzano**;
    - (d) limite di mano 8, poi controlli di stato.

### D. Combattimento (sostituisce v0.1 §8)
12. **Attaccante legale**: un tuo personaggio Pronto. **Bersaglio: sempre il Leader avversario**, salvo opposizione (C2) o parola chiave di carta.
13. **C1. Dichiarazione.** Ruoti l'attaccante. Si risolvono i trigger "quando attacca".
14. **C2. Opposizione** (del difensore). Il difensore può ruotare **una** sua Unità Pronta, che diventa il bersaglio. Un'Unità con Scudo si ruota come le altre. Se non oppone nessuno, il bersaglio resta il Leader.
15. **C3. Impegno dell'attaccante, a vista.** L'attaccante sposta nell'impegno da 0 a tutte le sue gemme di Brace, scoperte. [`pugno` sequenziale]
16. **C4. Risposta del difensore**, dopo aver visto C3. Sposta nell'impegno da 0 a tutte le sue gemme di Guardia, e può giocare **al massimo una** carta Reazione presa dalla mano o da una sua Cicatrice **dritta**.
    - (a) Le gemme del difensore pagano prima il costo della Reazione. Se non bastano, la Reazione torna dov'era senza effetto e tutte le gemme restano Parata. *(Nota di redazione dell'editor, non votata: con l'impegno a vista la clausola si può scrivere come "una Reazione si gioca solo se le gemme impegnate ne pagano il costo", in linea col pilastro 9 "ogni costo non pagabile rende l'azione illegale"; gli esiti non cambiano.)*
    - (b) Ogni gemma restante del difensore dà **+2** al valore di difesa del bersaglio.
    - (c) Ogni gemma dell'attaccante dà **+1** alla sua Forza.
    - (d) Si risolve la Reazione. Si leggono le condizioni **"se hai impegnato almeno N gemme"** (ex Infuso N) e le abilità di Reazione dei Leader, **statiche**.
17. **C5. Confronto.** Furia, Bracconiere, Scudo e le altre condizioni stampate si leggono qui.
    - Fa = Forza stampata dell'attaccante + gemme impegnate + bonus.
    - Db = Forza dell'Unità che si oppone, oppure Tempra del Leader, + 2 × gemme restanti del difensore + Reazione + bonus.

| Attaccante | Bersaglio | Esito |
|---|---|---|
| Unità | Unità | Perde la più bassa; a pari sono sconfitte entrambe. **Se il bersaglio ha Scudo, a pari è sconfitto solo l'attaccante** |
| Leader | Unità | L'Unità è sconfitta se Db ≤ Fa (**con Scudo: se Db < Fa**); altrimenti non succede nulla. Il Leader non è mai sconfitto |
| Unità o Leader | Leader | L'attacco va a segno se Fa ≥ Db |

Scudo nella tabella: **[default, aperto: P7; `scudo` vince_pareggi]**.

18. **C6. Esiti**, in quest'ordine:
    - (a) le Unità sconfitte vanno negli Scarti;
    - (b) se l'attacco va a segno sul Leader: se è **Alle Corde e non ha Cicatrici fresche**, l'attaccante **vince** (colpo finale); altrimenti, se le Cicatrici fresche sono meno del Saldo (2; 3 dal round 10) e il Leader ha almeno 1 Vita, la carta in cima alla Vita va tra le Cicatrici, **fresca**; altrimenti la perdita si ignora;
    - (c) le gemme impegnate tornano nella scorta; la Reazione va negli Scarti;
    - (d) controlli di stato; il Risveglio scatta con Vita ≤ 2 (v0.1 §9.8);
    - (e) trigger "quando sconfigge" e "dopo lo scontro". **Nessun modificatore sopravvive allo scontro.**

### E. Vita e fine della partita
19. **Alle Corde**: il Leader ha 0 Vite, oppure 1 Vita dal round 13.
20. **Ogni perdita di Vita** (attacchi, costi, mazzo vuoto) crea una Cicatrice **fresca** ed è soggetta al Saldo (al massimo 2 fresche, 3 dal round 10; oltre si ignora). Un costo in Vita che il Saldo non lascia pagare rende l'azione illegale (v0.1 §9.3). Unica eccezione: il Crepuscolo (8b). *(Correzione di Cr in coda, P8.)*
21. Le Cicatrici fresche non si giocano come Reazione e non si Rimarginano.
22. **Furia** = "+X al Confronto se hai almeno N Cicatrici", contando **tutte** le Cicatrici; mai come aura.
23. **Si vince solo** col colpo finale (18b); quando l'avversario deve pescare da un mazzo vuoto con 0 Vite; col Crepuscolo (8b). Se succedono due cose insieme perde il giocatore attivo. Niente patte.

### F. Conversione delle parole di v0.1
| v0.1 | v0.2 |
|---|---|
| Infuso N: [effetto] | "se hai impegnato almeno N gemme: [effetto] per questo scontro" (nome al thread carte) |
| Esponi | **Stanca**: ruota un'Unità avversaria Pronta; solo nella tua fase principale, mai il Leader |
| Bracconiere +X | +X se il bersaglio è un'Unità che si oppone |
| Furia N | regola 22 |
| Scudo | vince i pareggi quando si oppone (regola 17) **[aperto: P7]** |
| Rinnovo | quando sconfigge un'Unità, si raddrizza (thread carte) |
| "fino a fine turno" | "per questo scontro", oppure effetto permanente |
| Rimozione economica (legge 7) | solo su Unità Ruotate; legge 8: gli effetti che stancano hanno per bersaglio solo Unità |
| Abilità di Reazione dei Leader | testi statici letti in C4 (es. Maera Risvegliata: le tue gemme di Parata valgono +3) |
| Intercetto, "quando intercetta" | "quando si oppone" |

### G. Cosa sparisce rispetto a v0.1
24. Fornace come contatore e numero di turno per giocatore; Infondere e contatori d'infusione; Esposto e "Esposto = bersaglio legale"; Intercetto; finestra di reazione e limite di reazioni per turno; Ultimo respiro (sostituito da +1 Guardia Alle Corde); istantanea Alle Corde e contatore del Saldo; segnalino Scintilla; "ha già attaccato", "entrata in questo turno", "1 volta per turno" del Rimarginare; bonus "fino a fine turno" nel nucleo. Mai entrati: Incassa, pugno coperto.

---

## B. Da segnalare a Vittorio
1. **Pilastri.** Il 9 resta intatto (vince l'impegno a vista, nessuna informazione nascosta nuova); 2, 3, 4, 6 vanno riscritti come previsto (Esposto sparisce, "agire costa la difesa", Ultimo respiro → +1 Guardia, Reazioni dei Leader statiche 8/8). Con Tempra 4 il Leader Risvegliato (F4) colpisce a pugno vuoto: "il Leader non colpisce gratis" non regge più sul lato Risvegliato.
2. **Vincoli rispettati** (0 vittorie prima del round 5, mediana 8, round 13+ 1.5%), ma metriche dei pilastri fuori obiettivo: **rimonte 14.3%** (obiettivo 20–35; 6.7% negli incroci) e mediana al bordo basso; 6 pre-mortem su 8 puntano su Tempra 4.
3. **G1**: 55.7% senza compensazione; il default aperto (G2 +1 gemma nei round 1 e 3) dà 50.8% su 2.000 partite.
4. **Vincolo archetipi** negli incroci: Thorn 10%, Vey 72.9%, attribuito ai mazzi convertiti e non al nucleo; da verificare col set.
5. **Standard dello swarm**: per la seconda volta le previsioni non sono state scritte prima del lancio, e Tempra 4 viene da un'esplorazione fuori specifica; nessun playtest fisico. La correzione del protocollo sulle previsioni (esito_r2 §0) attende ancora il suo ok.

## C. Per il thread carte
- **Squilibrio dei mazzi convertiti.** Negli incroci: Arden 53.3, Maera 63.7, **Thorn 10.0**, Vey 72.9 (`E-014/incroci/`). È un problema delle conversioni, non del nucleo, ma falsa rimonte e archetipi: va corretto prima del primo ciclo del set.
- **Reazioni rare** (0.03 per scontro, 0.02 negli incroci). Solo 2 Reazioni nel pool. Obiettivo ≥0.10 per scontro (Ro, Bl, Cr). Proposte: costo ≤1 (Ve); Reazione a costo N vale più di 2N di difesa (Cr, Ar); più Reazioni nei mazzi Blu (Bl); prima misurare disponibili contro giocate (Po) e un mazzo di prova con 9 Reazioni (An).
- **Infuso**: testo "se hai impegnato almeno N gemme"; nome da scegliere (Impeto: Bl, Po; Infuso: Ro; Ardente: Ve); N ∈ {1, 2} sulle comuni, 3 solo su rare (Ro, Ne), perché il pugno d'attacco è pieno solo nel 17% dei casi.
- **Regole di set proposte:**
  - ogni Reazione costa almeno 1 (Cr, r2; il simulatore la applica già);
  - nessun effetto rimette gemme in Guardia durante uno scontro (Cr, r2);
  - gli effetti che fanno perdere Vite si risolvono solo nella fase principale di chi li controlla; nessuna Reazione ha un costo in Vita; niente effetti "l'avversario perde Vite" (Bl, controcaso P8);
  - una Reazione a costo N dà più di 2N di difesa equivalente (Cr, Ar);
  - in tensione con la prima: Cicatrici dritte come Reazione a costo −1, minimo 0 (Ne, variante di nucleo in coda).
- **Altri compiti**: Unità ferme al 41.8% (Ve: Caccia e Assalto per il Verde); con T4 la Forza 4 a costo basso diventa la statistica premium e la difesa Blu ne esce svalutata (Bl); posti di Guardia sul Leader (grafica); Rinnovo; Caccia per il Verde; mazzi 20/20 contro 32/8 (Po); Scudo in almeno un mazzo con ≥5 copie per misurare P7.

---

## Note di ratifica (non bloccanti)
Raccolte dall'editor dai file `ratifica_<ruolo>.md`. Nessuna cambia una decisione; sono richieste per la coda dei test e condizioni da rispettare prima del ciclo successivo.

**Correzioni al testo, già fatte in questa versione**
- P6, spareggio: "tutti e 8 hanno dichiarato 48–52" diventa "la fascia dei pilastri" (Bl, Ne, Ve). Bl lo segnala per trasparenza, perché lo spareggio premia la sua proposta; Ne aggiunge che {1,3} ha anche rimonte più alte di {1,2} (12.8 contro 9.8).
- §5.1: il rinvio al "punteggio in P3" che mancava; la valutazione delle previsioni su V2 ora è in P3 (An, Cr).

**Condizioni prima del ciclo successivo**
- **Thread carte, vincolo del critico (P8):** finché la variante "Vita pagata come costo entra dritta" non è votata, nessuna carta stampa costi in Vita pagabili nel turno avversario né effetti "l'avversario perde Vite". Per Cr la prima carta così è un exploit bloccante.
- **Thread carte (Ro):** il valore di Infuso, N ∈ {1, 2} sulle comuni, va passato al thread carte prima della bozza rossa definitiva.
- **Thread carte (Ve):** la condizione Unità ferme (§3 punto 4) si misura sul Verde, con Caccia e Assalto provati prima di riaprire il raddrizzo.
- **Testo della regola 16a (Ar):** l'architetto sostiene come testo finale la riformulazione dell'editor, "una Reazione si gioca solo se le gemme impegnate ne pagano il costo" (esiti invariati). La decide il thread principale quando scrive il regolamento v0.2.
- **Pilastro 2 (Ar):** con Tempra 4 il testo del pilastro va riscritto, e va segnalato a Vittorio (già in sezione B, punto 1). L'architetto ritira la sua lettura del r3 ("livello 1, il testo non cambia").

**Coda dei test e delle misure, nell'ordine in cui i votanti li chiedono**
1. **Mazzi bicolori 20/20 contro 32/8** (Po, test di mandato): primo test del ciclo successivo, insieme ai mazzi convertiti riequilibrati, perché Thorn al 10% falsa anche questa misura.
2. **Diagnostica "Reazioni disponibili contro giocate"** (Po, P9b): prima di qualunque variante sul costo delle Reazioni.
3. **G1 con 10.000 partite appaiate** (An, P6): conferma dello spareggio {1,3}; le 2.000 partite hanno IC ±2.2. Va misurato anche il vincolo di Cr "vittorie prima del round 6 <1%" (Cr).
4. **Metrica nuova nel motore: quota di scontri decisi prima dell'impegno** (Bl, P2): senza questa metrica il controcaso 2 resta senza verifica.
5. **Rimonte ≥20% e archetipi 45–55% negli incroci, misurati insieme** (Ro: condizioni 1 e 9 del §3), perché T4 favorisce chi colpisce per primo.
6. **Varianti in coda legate alla condizione "rimonte ≥20%"** (Ne): `reazione_da_cicatrice_costo −1` e la Guardia Alle Corde +2 restano in coda insieme a quella condizione.

**Previsioni:** An e Cr chiedono che le loro previsioni su V2 vadano in `modelli/previsioni.md`: fatto, con tutte le altre previsioni dei r3 valutate.

## Ratifica
| Votante | Risposta | File |
|---|---|---|
| analista | APPROVO (note non bloccanti) | `ratifica_analista.md` |
| architetto | APPROVO (note non bloccanti) | `ratifica_architetto.md` |
| critico | APPROVO (note non bloccanti) | `ratifica_critico.md` |
| designer_blu | APPROVO (note non bloccanti) | `ratifica_designer_blu.md` |
| designer_nero | APPROVO (note non bloccanti) | `ratifica_designer_nero.md` |
| designer_ponti | APPROVO (note non bloccanti) | `ratifica_designer_ponti.md` |
| designer_rosso | APPROVO (note non bloccanti) | `ratifica_designer_rosso.md` |
| designer_verde | APPROVO (note non bloccanti) | `ratifica_designer_verde.md` |

**Esito della ratifica: 8 APPROVO su 8, 0 CONTESTO. Q-013 RATIFICATA il 2026-10-08.** Restano condizionati: la ratifica del nucleo al playtest fisico (§3 punto 8), i punti APERTI (P6, P7, P9b) come varianti con default per il ciclo successivo, e l'ok di Vittorio sui pilastri da riscrivere (sezione B).
