# R-028: leve di ritmo e di divertimento per Q-028 (dopo E-031)

Data: 2026-11-03. Da: thread "Design delle carte del set". A: thread principale.
Esito: tcg/swarm/questioni/Q-028_divertimento/esito_passata2.md.

Sono leve di nucleo (livello 3), da misurare prima di proporle a Vittorio. **Non vanno nel regolamento.** Servono come parametri di regola, con default spento, e i replay a default spento devono restare identici a main.

## Parametri nuovi
1. **`bruciare`** (bool). Una volta per turno, nella fase principale, quando un giocatore gioca una carta può scartare un'altra carta dalla mano: quella carta paga 1 gemma del costo. Non dà gemme al pugno né alla Guardia.
   - Con `bruciare_min_mano` (default 0) si imposta il ripiego "con almeno N carte in mano".
   - L'IA deve poter scegliere se e quale carta bruciare: ogni scelta è un'azione legale a sé, come per `any`.
2. **`tempra_tardo`** (round, default spento): da quel round in poi, la Tempra di tutti e due i Leader scende di 1. Braccio A: round 10.
3. **`allo_scoperto`** (bool): un Leader a 0 Vite ha Tempra −1. È il braccio B.
4. **Parola chiave `breccia`**: "Se questa Unità batte chi si oppone, il Leader avversario perde 1 Vita, nel rispetto del Saldo." Va scritta senza toccare le carte esistenti: entra solo in carte nuove dei bracci, che preparerà il programmatore del thread delle carte.

## Contatori nel report
- Partite chiuse dal Crepuscolo.
- Serie più lunga senza Vite perse nella finestra R4–R10, media per partita.
- Round giocati dopo il primo 0 Vite.
- % di ribaltamenti di chi è a 0 Vite.
- Turni vuoti nei round 1–3.
- Turni senza giocare carte.
- Mano piena senza nulla di giocabile.
- Carte bruciate a partita.
- Unità ferme divise in "si è opposta" e "mai coinvolta".
- Vittorie entro il round 5.
- R-017 entro il round 6.

Se servono, gli script sono in tcg/swarm/questioni/Q-028_divertimento/dati/script/ (metriche_f.py, metriche_f_extra.py).

## Corsa (E-033), dopo E-031
- **Base:** il braccio vincente di Q-027, oppure B0c05 se nessuno passa, con lo stesso riferimento e gli stessi semi di E-031.
- **Vaglio:** tre bracci a 100 partite per incrocio sul torneo completo, IA forte: `bruciare`, `tempra_tardo` 10, `allo_scoperto`. Circa 18 h.
- **Conferma:** il vincitore fra A e B insieme a `bruciare`, a 200 partite per incrocio. Circa 12 h. Lo confermo io dopo il vaglio.
- **Ordine rispetto a R-027:** il vaglio di E-033 viene prima di P7 e P9b. Il divertimento è la richiesta diretta di Vittorio, mentre le regole in prova non bloccano nulla.

Le uscite vanno in dati/E-033/ su dati/e020-v024-forte e in tcg/swarm/esperimenti/E-033_ritmo/.
