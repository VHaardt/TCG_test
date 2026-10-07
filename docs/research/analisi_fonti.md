# Analisi comparativa delle fonti — MTG, Yu-Gi-Oh!, Pokémon, Lorcana, One Piece

> Obiettivo: estrarre dai cinque regolamenti forniti ciò che serve a progettare un nuovo TCG 1v1 intuitivo ma profondo, con partite di 5–15 turni per giocatore, senza OTK e senza hard-control opprimente.
> Fonti: `IT_M15_QckStrtBklt_LR_Crop.txt` (MTG M15), `Rulebook_v9_it.txt` (YGO v9), `par_rulebook_it.txt` (Pokémon), `FormatCoconut_Rules.txt` (Lorcana, formato casual multiplayer a 25 leggenda — integrato con le regole base note), `rule_manual.pdf` (OPTCG, analizzato in base alle regole ufficiali note: il layer di testo del PDF è corrotto).

---

## 1. Magic: The Gathering (M15 Quick Start)

**Risorse.** Le terre sono carte del mazzo: «Puoi giocare una terra per turno»; si TAPpano per produrre mana colorato (5 colori) o incolore. Risorsa permanente e crescente (+1 al massimo al turno), ma **dipendente dalla pesca**: la stessa carta è risorsa *oppure* azione, decisa dalla composizione del mazzo (≈40% di terre).
**Turno.** Stap → mantenimento → pescata → fase principale 1 → combattimento (dichiara attaccanti, il difensore dichiara bloccanti, danno) → fase principale 2 → finale. Chi inizia non pesca nel primo turno.
**Vittoria.** Avversario da 20 punti vita a 0 (anche: mazzo vuoto, segnalini veleno).
**Tipi di carta.** Terra, creatura, istantaneo, stregoneria, incantesimo, artefatto, planeswalker.
**Interazione.** La **pila** (LIFO) con priorità alternata: istantanei e abilità rispondono a qualunque cosa. Blocco scelto dal difensore (assegnazione libera di bloccanti, anche multipli). Molto ricca ma pesante cognitivamente.
**Comeback.** Il difensore sceglie i blocchi; le "board wipe" (rimozione di massa) resettano il tavolo; 20 vite sono un buffer ampio; il gioco a carte coperte (istantanei col mana alzato) crea bluff.
**Fun / innovazione.** Ruota dei colori come identità filosofica degli archetipi; il "color pie" rende leggibili punti di forza e debolezze; ogni carta può essere tutto; enorme spazio combinatorio; decisioni di combattimento profonde con regole semplici (attacca/blocca).
**Frustrazioni.** **Mana screw/flood**: in una percentuale non trascurabile di partite un giocatore non gioca (il mulligan mitiga ma penalizza). Contromagie e "tassatori" in eccesso producono partite "draw-go" noiose per l'avversario. Il combo/storm crea turni interminabili. La pila è il primo scoglio per i neofiti.
**Durata tipica.** 6–10 turni a giocatore (aggro 4–6, controllo 12+).

## 2. Yu-Gi-Oh! (Regolamento v9)

**Risorse.** Nessuna risorsa esplicita: la vera risorsa è il **numero di carte** (vantaggio carte) e l'unica Evocazione Normale per turno. Mostri di livello 5–6 richiedono 1 tributo, 7+ due. L'Extra Deck (0–15 carte: Fusion/Synchro/Xyz, poi Link) è accessibile tramite materiali sul campo — di fatto un "mana" fatto di corpi.
**Turno.** Draw (chi inizia non pesca il primo turno) → Standby → Main 1 → Battle (chi inizia non attacca il primo turno) → Main 2 → End.
**Vittoria.** 8000 LP a 0; Deck vuoto alla pescata; vittorie alternative (Exodia).
**Tipi di carta.** Mostri (Normali, Effetto, Rituali, Fusion, Synchro, Xyz, Pendulum, Link), Magie (Normali, Rapide, Continue, Terreno, Equipaggiamento, Rituali), Trappole (Normali, Continue, Contro-Trappole).
**Interazione.** La **Catena** con Spell Speed 1/2/3 (risolve a ritroso), trappole coperte che vanno "settate" un turno prima, effetti rapidi dei mostri, "hand trap" attivabili dalla mano. Combattimento ATK vs ATK/DEF, ma **non c'è scelta del bloccante**: chi attacca sceglie il bersaglio.
**Comeback.** Alto in teoria (una carta può ribaltare il campo; nessun costo di mana), ma in pratica è "chi esaurisce prima le risorse perde".
**Fun / innovazione.** Esplosività ed espressione combinatoria; Extra Deck come "toolbox" sempre disponibile (scelta, non pesca); trappole e set coperti creano tensione/bluff; costo zero = turni spettacolari.
**Frustrazioni.** **Turni combo da 10–20 minuti** con board finale piena di negazioni ("end board"): l'avversario non gioca. Vantaggio del primo giocatore enorme. **Hand trap** come tassa obbligatoria: partite decise da chi ha pescato la risposta giusta. Negazioni "soft" ovunque = hard-control. Testi lunghissimi e opachi; potere fuori scala (power creep). OTK frequenti.
**Durata tipica.** 2–5 turni a giocatore nel competitivo moderno: l'opposto del nostro target.

## 3. Pokémon GCC

**Risorse.** **Energia**: una carta Energia dalla mano a un Pokémon per turno, permanente sul Pokémon (si perde col KO o con la ritirata). Risorsa *localizzata*: investi su specifiche unità. Limiti per turno: 1 Energia, 1 Aiuto (Supporter), 1 Stadio, 1 ritirata, Strumenti illimitati.
**Turno.** Pesca → (energia, evoluzioni, Allenatori, abilità, ritirata in qualunque ordine) → attacco (termina il turno) → Controllo Pokémon (veleno, bruciatura, sonno, paralisi). Chi inizia non attacca né gioca Aiuto al primo turno; nessuno evolve al primo turno.
**Vittoria.** Prendere tutte e **6 le carte Premio** (una per KO, 2–3 per Pokémon-ex/V); avversario senza Pokémon in gioco; avversario che non può pescare.
**Tipi di carta.** Pokémon (Base, Fase 1, Fase 2, ex/V), Allenatore (Strumento, Aiuto, Stadio, Oggetto Pokémon), Energia (base e speciale).
**Interazione.** Quasi assente durante il turno avversario: niente pila, niente risposte. Interazione **posizionale** (Attivo vs Panchina, "gust" per tirare avanti un Pokémon, debolezza/resistenza ×2/−30).
**Comeback.** Moderato: i Premi vanno in mano a chi *infligge* il KO (leggero effetto snowball); il comeback deriva da carte "con meno Premi rimasti" (es. supporter che pescano di più se sei indietro) e dal **prize trade**: scambiare KO su Pokémon a 1 premio contro ex a 2 premi. I Premi nascondono 6 carte, creando incertezza ma anche *rinforzi*.
**Fun / innovazione.** **Evoluzione** (investimento su più turni = crescita visibile); costo d'attacco su energie *agganciate* (la risorsa è sul tavolo e si perde in battaglia); attivo + panchina = semplice e leggibile; condizioni speciali tattiche; prize trade come metagioco.
**Frustrazioni.** **Lanci di moneta** (moneta per chi inizia, paralisi/sonno/confusione, attacchi a testa o croce) = varianza percepita come ingiusta. Prize "bloccati" (carte chiave fra i Premi). Mulligan per mano senza Base. Dipendenza dai Supporter di pescata: chi non ha il "draw supporter" perde il turno. Primo turno avversario con KO del Pokémon d'apertura. Deck thinning/consistenza come unico obiettivo di deckbuilding.
**Durata tipica.** 6–10 turni a giocatore.

## 4. Disney Lorcana (regole base + Format Coconut)

**Risorse.** **Calamaio (inkwell)**: una volta per turno puoi mettere a faccia in giù nel calamaio **qualunque carta col simbolo inkable** (bordo d'inchiostro), che diventa 1 inchiostro permanente. Risolve il mana screw di MTG (ogni mano ha "terre") ma introduce il dilemma "cosa sacrificare".
**Turno.** Inizio (prepara, controlla effetti, pesca; chi inizia salta la pesca) → fase principale (inchiostra 1, gioca carte, **canta** canzoni esaurendo personaggi, **sfida**, **esplora (quest)**, attiva abilità, sposta su Luoghi) → fine.
**Vittoria.** **20 leggenda** (Coconut: 25, multiplayer); mazzo vuoto alla pescata. La vittoria è una *corsa*, non un'eliminazione.
**Tipi di carta.** Personaggi (Forza, Volontà, Leggenda), Azioni (incl. Canzoni), Oggetti, Luoghi. Shift (evoluzione a costo ridotto sopra una versione dello stesso personaggio).
**Interazione.** Minima fuori turno: niente istantanei, niente pila (le abilità risolvono subito). Interazione = **sfida**: si possono sfidare solo personaggi **esauriti**; quindi esplorare (fare punti) espone il personaggio alla sfida. Guardiano (Bodyguard), Evasivo, Sfidante+X, Resistere.
**Comeback.** Il dilemma esplora/difendi rende le corse non lineari; i personaggi esauriti sono vulnerabili, quindi chi è in vantaggio deve "pagare" esponendosi. Luoghi generano leggenda passiva.
**Fun / innovazione.** **Ogni carta è risorsa potenziale** (no screw) con scelta significativa; doppio ruolo dell'esaurimento (agire = esporsi); canzoni pagate col corpo dei personaggi; obiettivo positivo (fare punti) invece di "uccidere"; regole cortissime, onboarding eccellente; tre colori max nel formato Coconut, due nel competitivo: identità chiara.
**Frustrazioni.** "Ink-everything": decidere cosa inchiostrare ogni turno all'inizio è stressante e a volte banale (si inchiostra il peggio) — il costo opportunità è reale ma opaco ai neofiti. Poca interazione nel turno avversario → partite "solitarie" (racing goldfish). Rimozioni economiche rendono i personaggi usa-e-getta. Matchup polarizzati per colore; ramp + carte bomba. Mancanza di scelta dei bloccanti (l'attaccante sceglie il bersaglio).
**Durata tipica.** 7–10 turni a giocatore.

## 5. One Piece Card Game (manuale regole)

**Risorse.** **Mazzo DON!! separato** (10 carte): +2 DON!! per turno (il primo giocatore ne prende 1 al primo turno), fino a 10. Le DON!! si **spendono** (girate) per giocare carte, oppure si **attaccano** a Leader/Personaggi (+1000 potenza ciascuna fino a fine turno) — la stessa risorsa è costo o pompaggio. Effetti DON!! −X restituiscono DON al mazzo DON (costo reale, rigenerabile).
**Turno.** Refresh (tutto torna attivo, DON tornano nell'area) → Draw (primo giocatore salta) → DON!! (+2) → Main (giocare, attaccare DON, attaccare) → End. Il primo giocatore non attacca al turno 1.
**Vittoria.** Infliggere danno quando il Leader avversario ha **0 Vita** (Vita = 4–5 carte a faccia in giù dal Leader). Ogni colpo al Leader sposta una carta Vita **in mano** al difensore (con eventuale **Trigger** gratuito). Anche mazzo vuoto.
**Tipi di carta.** Leader (sempre in gioco, definisce colore, Vita e un'abilità), Personaggi, Eventi, Stage, DON!!.
**Interazione.** In combattimento: **Blocker** (redirige l'attacco su di sé), **Counter** (carte dalla mano scartate per +1000/+2000 potenza, ed Eventi Counter) — interazione dalla mano strutturata in un'unica finestra (il "counter step"), senza pila generale. Si possono attaccare solo Leader o Personaggi **riposati**.
**Comeback.** **Fortissimo e strutturale**: perdere Vita = pescare carte (e Trigger); chi è sotto ha più mano per contrare; il Leader garantisce un "motore" sempre presente.
**Fun / innovazione.** Leader come comandante/identità del mazzo (deckbuilding guidato e accessibile); risorsa che **cresce in modo garantito** (zero screw); scelta spendere DON vs potenziare; Vita-che-diventa-mano come elastico anti-snowball; Counter sulle carte = ogni carta ha doppio uso difensivo; Trigger come piccola sorpresa.
**Frustrazioni.** **Vantaggio del primo giocatore** forte (e paradossalmente del secondo in alcuni meta per la curva DON): asimmetria tempo/carte difficile da bilanciare. I Trigger sono varianza pura a fine partita (un trigger "blocca tutto" ribalta). Matematica della potenza (multipli di 1000) ripetitiva; "rush" a fine partita in cui il difensore deve avere esattamente abbastanza counter; rimozioni KO economiche; leader sbilanciati definiscono il meta.
**Durata tipica.** 6–9 turni a giocatore.

---

## 6. Sintesi trasversale

### 6.1 Sistemi di risorse a confronto

| Gioco | Sistema | Crescita | Pro | Contro |
|---|---|---|---|---|
| MTG | Terre dal mazzo, 1/turno | Variabile (pesca) | Tensione costruttiva, colori come vincolo identitario, curve diverse | Screw/flood; partite decise prima di giocare; mulligan punitivo |
| YGO | Nessuna (carte + 1 Evocazione Normale) | Nessuna, limiti per turno | Esplosività, nessuno screw | Nessun freno al turno 1 → combo/OTK; valutazione di potenza impossibile |
| Pokémon | Energia agganciata a unità, 1/turno | Lineare ma localizzata | Investimento visibile; KO fa perdere risorse (tensione); evoluzione | Energia ancora dal mazzo (screw); dipendenza da carte di accelerazione |
| Lorcana | Calamaio: qualunque carta inkable, 1/turno | Lineare, quasi garantita | Niente screw; ogni carta è doppia scelta | Decisione opaca/ripetitiva; flood mascherato; perdita di "identità" della carta |
| OPTCG | Mazzo DON!! separato, +2/turno, max 10 | Garantita, rapida | Zero screw; DON come costo o buff; curva prevedibile = bilanciabile | Poca variazione tra partite; vantaggio di tempo del primo giocatore; deckbuilding meno teso sulla curva |

**Lettura:** il trend storico va dalla risorsa *pescata* (MTG) alla risorsa *garantita* (OPTCG), con Lorcana in mezzo. Per partite 5–15 turni e anti-frustrazione, una risorsa **garantita ma con scelta** (crescita automatica + decisione di impiego o sacrificio) è il punto ottimale.

### 6.2 Le 10 idee più trasferibili

1. **Risorsa garantita e separata dal mazzo** (DON!! di OPTCG): elimina screw/flood e rende il bilanciamento dei costi prevedibile.
2. **Risorsa a doppio uso** (DON spesa o agganciata per +potenza; calamaio Lorcana): ogni turno contiene una decisione non banale sulla risorsa.
3. **Agire espone** (esaurimento Lorcana, "riposato" OPTCG): chi attacca/fa punti diventa bersagliabile; autoregola la corsa e crea dilemmi offesa/difesa.
4. **Danno subito = carte in mano** (Vita OPTCG): elastico anti-snowball elegante, comeback strutturale senza regole speciali.
5. **Leader/comandante sempre in gioco** (OPTCG, Coconut): identità di archetipo, onboarding, deckbuilding guidato; motore costante che riduce le "mani morte".
6. **Interazione in finestra unica e limitata** (Counter step OPTCG, blocco MTG): risposte nel turno avversario senza pila generale; leggibile per i neofiti.
7. **Scelta del difensore nel blocco** (MTG): il combattimento diventa un dialogo; riduce il "chi attacca vince".
8. **Investimento evolutivo multi-turno** (evoluzione Pokémon, Shift Lorcana): crescita visibile, archetipi "tall", bersagli interessanti per la rimozione.
9. **Limiti per turno per categoria** (Pokémon: 1 Aiuto, 1 Stadio, 1 Energia): freno nativo agli OTK e ai turni-combo senza dover bannare carte.
10. **Ruota dei colori/ink come identità filosofica** (color pie MTG, max 2 ink Lorcana): archetipi leggibili, combinazioni ibride, debolezze dichiarate.

Menzioni: vittoria a punti (Lorcana) che premia anche lo sviluppo, non solo l'eliminazione; Extra Deck come toolbox *scelto* e non pescato (YGO); prize trade come metagioco di valore delle unità (Pokémon).

### 6.3 I 10 anti-pattern da evitare

1. **Risorsa pescata dal mazzo principale** senza mitigazione (screw/flood MTG).
2. **Turni senza costo né limite** che permettono catene da 15 azioni (YGO): genera OTK, turni lunghissimi e board di negazioni.
3. **Negazione/contromagia a basso costo e ripetibile**: hard-control che toglie agenzia all'avversario (YGO end board, MTG draw-go).
4. **Hand trap/risposte gratuite dalla mano** non contrastabili: partite decise da chi pesca la carta d'argento.
5. **Moneta come risolutore di effetti** (Pokémon): varianza percepita ingiusta e non mitigabile dalla skill.
6. **Varianza decisiva a fine partita** non controllabile (Trigger OPTCG, Premi "bloccati" Pokémon).
7. **Asimmetria del primo turno non compensata** (YGO, OPTCG): serve un compensatore esplicito e testato.
8. **Turno avversario passivo** (Lorcana, Pokémon): giochi "solitari" in cui si guarda l'altro per minuti.
9. **Testi lunghi e regole a eccezioni** (YGO Spell Speed, timing "se/quando"): barriera d'ingresso e dispute.
10. **Rimozioni economiche universali + bombe a costo alto** che rendono le unità usa-e-getta e polarizzano il gioco su "chi ha la risposta". Corollario: matchup polarizzati per colore senza risposte neutrali.

### 6.4 Cinque hook concreti per innovare

1. **Risorsa garantita con "investimento" a scelta.** Esempio: +1 risorsa automatica a turno (fino a un tetto), più la possibilità facoltativa di sacrificare una carta per un **bonus permanente di archetipo** (non una risorsa generica): la decisione Lorcana diventa interessante e tematica invece che di scarto.
2. **Danno = carte, ma con un tetto.** Prendere la Vita OPTCG in mano, ma con un costo per usarle (es. le carte Vita si giocano solo come *difesa* o con costo maggiorato) per evitare sia lo snowball sia il "trigger miracolo". Comeback forte, varianza controllata.
3. **Finestra di reazione unica e budgetata.** Una sola "risposta" per turno avversario, pagata con risorse lasciate *libere* dal proprio turno: interazione garantita nel turno altrui (contro l'anti-pattern 8) senza pila infinita né hard-control (contro 3 e 4). Decisione chiara: spendere tutto ora o tenersi "le carte alzate".
4. **Doppia condizione di vittoria intrecciata.** Corsa a punti (Lorcana) + pressione sul Leader (OPTCG): fare punti espone le unità, attaccare il Leader accelera il suo comeback. Due assi permettono archetipi diversi (race, midrange, controllo-che-vince-a-punti) e impediscono partite risolte in un turno (soglia di punti massima ottenibile per turno = anti-OTK strutturale).
5. **Sinergie "a ponte" e unità che evolvono.** Archetipi definiti da parole chiave che appaiono in due colori (ponte), con carte neutre "connettore" e un sistema di evoluzione/Shift che trasforma unità investite: profondità di deckbuilding senza mazzi monotematici, e bersagli di valore che rendono la rimozione una scelta e non un riflesso. Primo giocatore compensato con un token risorsa/difesa una tantum, da tarare in playtest.

### 6.5 Parametri di riferimento per il target 5–15 turni

- Risorsa: +1 a turno con tetto 8–10 (OPTCG raggiunge 10 al turno 5 con +2: troppo rapido per 15 turni; MTG/Lorcana +1 è più adatto).
- Buffer vitale: misurato in "colpi" (5–6, come Premi/Vita) anziché in punti grandi, per leggibilità; ogni colpo deve richiedere almeno un'azione significativa.
- Limite di carte "di accelerazione" per turno (modello Aiuto Pokémon) e tetto al danno/punti per turno per escludere OTK.
- Primo turno: chi inizia non attacca e non pesca, oppure riceve risorse ridotte; il secondo riceve un piccolo compensatore.
- Interazione: ogni turno avversario deve offrire almeno una decisione reale (blocco, reazione budgetata, counter).
