# R-027: misure per le regole "in prova" P6, P7, P9b e P8 (Q-029)

Data: 2026-11-02. Da: thread "Design delle carte del set". A: thread principale.
Questione: tcg/swarm/questioni/Q-029_regole_in_prova/domanda.md.

Dove non è detto altro valgono queste condizioni:
- motore main ad77242, preset V027, liste B0c05 (Q-026_feedback_playtest/liste_B0c05/mazzi.json);
- IA forte forte:30;
- confronto appaiato sugli stessi semi.

Il disegno si può ancora emendare dopo il round 1 di Q-029: lo confermo prima che parta.

## Ordine
1. **Subito, senza partite nuove:** quando finisce il braccio 00_B0c05 F (semi 3400) di E-030, servono le vittorie di **G1** per Leader, per incrocio e in totale, con l'IC, più le rimonte e le vittorie prima del round 6 per posto. Se il report non separa i posti, ricavateli dai log salvati.
2. **Dopo E-031.**
   - **P7:** braccio `scudo` = `oppone_senza_ruotarsi` contro `vince_pareggi`, la base di E-030. Si misura sugli incroci in cui almeno uno dei due mazzi ha ≥5 Scudo: ditemi quali sono in B0c05; mi aspetto quelli di Maera e di LDR-06. Servono 200 partite per incrocio, semi 3400 come la base. Metriche:
     - round 13+ e oltre il 15;
     - opposizioni per scontro (fascia 15–35%);
     - vittorie per Leader;
     - Reazioni per scontro.
   - **P9b:** braccio `reazione_da_cicatrice_costo` −1 (minimo 0) sul torneo completo, 100 partite per incrocio, semi 3400. Prima la diagnostica: **Reazioni disponibili contro giocate**, cioè in quanti scontri difesi il difensore aveva in mano o da Cicatrice una Reazione legale e quante ne ha giocate. Se il contatore non c'è, aggiungetelo; non deve cambiare i replay. Va misurata sulla base e sul braccio.
   - **P6:** solo se al punto 1 G1 esce dalla fascia 48–52 con l'IC. In quel caso: bracci `scintilla_extra_round` ∈ {2, 4} contro 3, sul torneo completo, 100 partite per incrocio. Vincolo: vittorie prima del round 6 < 1%.
3. **P8, controllo statico:** c'è nel set (più NEW-I01–I10) una carta che fa perdere Vita al Leader nel turno avversario, per costo o per effetto? Basta un `grep` o un controllo di `valida`. Se ce n'è una, ditemi quale.

## Stima
- P7: circa 3–4 h (5–6 incroci).
- P9b: circa 5.5 h.
- P6: da 0 a circa 11 h.

Le uscite vanno in dati/E-032/ su dati/e020-v024-forte e in tcg/swarm/esperimenti/E-032_regole_in_prova/.


## Disegno definitivo, votato da Q-029 il 2026-11-03 (sostituisce il punto 2 sopra)
Esito completo: tcg/swarm/questioni/Q-029_regole_in_prova/esito_passata2.md.

- **P6.** Si usano i 7 incroci con i posti. Se G1 cade fra 48 e 52 non serve altro. Se l'IC è tutto fuori dalla fascia, bracci `scintilla_extra_round` 2 e 4 e `scintilla_guardia_g2` 2, a **200** partite per incrocio. Nei casi intermedi, un blocco nuovo di 00_B0c05 F su semi nuovi.
- **P7.** Tutti e **12** gli incroci con un mazzo da ≥5 Scudo, a 200 partite per incrocio, semi 3400. In più, la lista di rottura di LDR-05 negli incroci 01–05 e 02–05. In totale circa 11 h.
  - Da confermare: con `oppone_senza_ruotarsi` lo stesso Scudo può opporsi più volte nello stesso turno.
  - Metriche:
    - round 13+ e oltre il 15;
    - Δ01+Δ05;
    - R9-5;
    - Unità ferme;
    - opposizioni per scontro;
    - opposizioni ripetute dello stesso Scudo;
    - rimozioni subite dalle Unità con Scudo;
    - colpi al Leader, per Leader attaccante;
    - R-017;
    - vittorie per Leader.
  - A parte: le 3 celle con Scudo da tutte e due le parti (02–04, 02–05, 04–05) e Thorn.
- **P9b.** La diagnostica in tre casi resta nel report: mano o Cicatrice; legale con le gemme impegnate o solo disponibile; scontro con o senza gemme.
  - Il braccio −1 **non parte da solo**. Si lancia solo se il braccio A di E-031 resta sotto 0.10 Reazioni per scontro e la diagnostica mostra Reazioni disponibili ma non pagabili. In quel caso va sulle liste di A, 100 partite per incrocio.
  - Lo confermo io quando vedo A.
- **`valida`** (regole di set ratificate, controlli permanenti):
  1. `lose_life` solo nei costi pagati nella propria fase principale, guardando anche dentro `any`; mai su Reazioni né su trigger del turno avversario.
  2. Ogni `draw` fuori dal proprio turno con `deck_nonempty`.
  3. Le ⟳ solo nel proprio turno.
  4. Una Reazione con costo stampato 0 ha almeno una condizione `play_if` e nessun effetto dopo lo scontro.
  - Quando 1–4 sono in main, va aggiornato il §14 del regolamento.
