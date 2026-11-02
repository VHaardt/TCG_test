# R-026: primitive del motore per Q-027 (interattività), senza toccare le corse in coda

Data: 2026-11-02. Da: thread "Design delle carte del set". A: thread principale.
Esito: tcg/swarm/questioni/Q-027_interattivita/esito_passata2.md. Testi delle carte: round1/proposta_unificata.md, con l'emendamento "Pronta" su I03.
Priorità: **dopo** D-2M ed E-030. Le primitive si possono scrivere mentre la coda gira, ma il motore usato da E-030 (ab6f2dd) non deve cambiare sotto la corsa.

## Primitive, in ordine
1. **`bounce`** (NEW-I03): "Riporta in mano al suo proprietario un'Unità avversaria Pronta con costo ≤4". Il filtro va su costo e stato (Pronta). L'Unità torna in mano senza modificatori.
2. **`on_rim`**: evento "Quando il tuo Leader Rimargina".
   - NEW-I09: "Stanca un'Unità avversaria Pronta con Forza attuale ≤ le tue Cicatrici". Il filtro usa la Forza attuale e il numero di Cicatrici del controllore al momento dell'evento.
   - NEW-I10: "se questa Unità è Ruotata, raddrizzala". Un'Unità raddrizzata può attaccare di nuovo (§7 v0.2).
3. **`sacrifice`**, costo aggiuntivo di una Tattica (NEW-I02), con la regola G1 nel glossario: "Sacrificare: metti negli Scarti una tua Unità Pronta senza Assalto. Si sacrifica solo come costo aggiuntivo di una Tattica, e un sacrificio non dà mai come premio pescare o riprendere carte." `valida` deve rifiutare una carta che usa `sacrifice` fuori da una Tattica o con una pesca o un recupero come effetto.
4. **`recover`** (NEW-I08): "Quando entra, se hai almeno 2 Cicatrici, riprendi in mano dai tuoi Scarti un'Unità con costo ≤2 che non ha 'Quando entra'". Regola G2 nel glossario: "Un effetto che prende carte dagli Scarti non può prendere una carta che prende dagli Scarti; una carta giocata direttamente dagli Scarti, dopo l'uso, va in fondo al mazzo del suo proprietario." Il gioco dagli Scarti (I07) per ora **non serve**: I07 è in riserva.

## Verifiche
5. **Reazione a costo 0** (NEW-I04): `valida` e il motore la accettano? Il §8 C4 (a) lo permette già. Se esiste un vincolo di set "costo ≥1", va tolto solo per le Reazioni.
6. **Condizione "nel tuo impegno non hai gemme"** (NEW-I04): "Giocala solo se il bersaglio è una tua Unità e nel tuo impegno non hai gemme. Il bersaglio ha +2 in questo scontro." `target_is_unit` esiste già; serve la condizione sulle gemme impegnate.

## Contatori nuovi nel report (servono agli obiettivi di Q-027)
- Unità ferme per Leader (% di Unità in campo che a fine turno non hanno attaccato né bloccato), se non c'è già.
- Reazioni giocate per scontro, per Leader.
- Rimozioni a partita per Leader, divise per fonte: sconfiggi, rimbalzo, sacrificio.
- Sacrifici e recuperi a partita.

## Non serve
- `heal`: le cure restano fuori finché Vittorio non le chiede.
- Regolamento: aggiungete G1 e G2 al glossario solo dopo il voto finale di Q-027 (dopo E-031), non adesso.

Quando le primitive sono pronte, il programmatore del thread delle carte scrive le carte e gli input di E-031: bracci A, B e C su B0c05 e V027, con l'IA forte e 200 partite per incrocio, più le celle sulle liste di rottura di L5 e L1.
