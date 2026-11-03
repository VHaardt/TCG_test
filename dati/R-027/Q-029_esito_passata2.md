# Q-029: esito della passata 2 (2026-11-03)

Hanno votato 8 ruoli su 8 su `round1/proposta_passata2.md`.

## Chiuse subito
- **P8, CONFERMATO 8/8.** La correzione di nucleo del critico non serve, e il riquadro "in coda" del §17.4 si può togliere. Il vincolo del §14 diventa permanente:
  - (a) `valida` contiene l'elenco dei casi in cui `lose_life` è ammesso: solo nei costi pagati nella propria fase principale, guardando anche dentro i costi `any`, e mai su Reazioni o trigger del turno avversario;
  - (b) regola di set: ogni pesca fuori dal proprio turno stampa "se il tuo mazzo non è vuoto", e `valida` richiede `deck_nonempty`;
  - (c) le abilità ⟳ si attivano solo nel proprio turno.
  - **Testo corretto di NEW-I05:** "L'attaccante ha −2 in questo scontro. Se la giochi da una tua Cicatrice e il tuo mazzo non è vuoto, pesca 1."
- **Reazioni a costo 0: il nucleo è CONFERMATO 8/8.** §8 C4 (a) le ammette già e Vittorio non serve. Regola di set, controllata in `valida`: "**Una Reazione a costo stampato 0 stampa una condizione di gioco e non ha effetti dopo lo scontro.**" Le due metà sono passate 8/8 ciascuna; la seconda è l'emendamento del nero. NEW-I04 la rispetta.

## Disegno di R-027 (le decisioni su P6, P7 e P9b arrivano con i dati)
- **P6, 8/8, regola a tre esiti:**
  - G1 in 48–52 → conferma;
  - IC tutto fuori dalla fascia (sotto circa 46.2 o sopra circa 53.8) → bracci {2, 4} più `scintilla_guardia_g2`, a 200 partite per incrocio;
  - casi intermedi → un nuovo blocco di E-030 su semi nuovi.
- **P7.** Il disegno è approvato 8/8: 12 incroci a 200 partite; le 3 celle con Scudo da tutte e due le parti e Thorn riportati a parte; la lista di rottura di LDR-05 su 01–05 e 02–05; le metriche della proposta, con i colpi al Leader divisi per Leader attaccante.
  - **Criterio di cambio:** 5 ruoli hanno accettato il testo base e 3 hanno proposto emendamenti compatibili (analista, critico, rosso). Vale la forma che li unisce. Il testo è più severo, quindi chi ha accettato il base non ne esce penalizzato.
  - "Senza ruotarsi" sostituisce "vince i pareggi" solo se valgono **tutte** queste condizioni:
    - round 13+ ≤ +1;
    - la somma delle distanze dalla fascia 45–55 di LDR-02, LDR-04 e LDR-05 scende di almeno 2 punti;
    - nessuno dei tre si allontana dalla fascia di più di 2 punti;
    - nessun Leader senza Scudo (L1, L3, L6) scende sotto 45;
    - Δ01+Δ05 ≤ +1.
  - Altrimenti "vince i pareggi" si conferma. Il motivo del tavolo (ponti) resta a verbale.
- **P9b, 8/8:**
  - la diagnostica in tre casi diventa permanente;
  - il braccio −1 da Cicatrice si lancia solo se il braccio A di E-031 resta sotto 0.10 **e** ci sono Reazioni disponibili ma non pagabili. Si misura sulle liste di A;
  - passa solo con almeno +0.02 Reazioni per scontro, round 13+ ≤ +2, Maera ≤ 55 e R9-5 ≤ 1. Poi un blocco su Leader e rimonte;
  - il braccio "minimo 1" non si fa;
  - se il braccio −1 non parte o non passa, C4 (a) si conferma.

## Previsioni registrate (mediane del round 1, con le correzioni della passata 1)
- **P6:** G1 49.5.
- **P7 con "senza ruotarsi":**
  - round 13+ da +1 a +5;
  - LDR-05 da +1 a +3;
  - Maera da +1 a +2;
  - Δ01+Δ05 da +1 a +1.5.
- **P9b con il −1:** Reazioni da 0.078 a 0.085.
