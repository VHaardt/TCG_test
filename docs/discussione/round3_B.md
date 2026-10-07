# Round 3 — Ratifica dell'agente B

> Ho letto `regolamento_v0.1.md`, `pilastri_design.md` ed `esito_dibattito.md`. Il registro riporta in modo fedele le mie posizioni e le mie concessioni. Accetto di essere in minoranza sul Crepuscolo: la Clessidra B+ è la mia proposta del round 1, ed è un esito che sottoscrivo senza riserve.

## 1. Sezioni del regolamento

| § | Voto | Note |
|---|---|---|
| 1 Panoramica | **Approvo** | |
| 2 Componenti | **Approvo** | |
| 3 Zone di gioco | **Approvo** | |
| 4 Preparazione | **Approvo** | |
| 5 Risorse | **Approvo** | |
| 6 Struttura del turno | **Approvo** | Vedi la correzione 1 qui sotto |
| 7 Tipi e stati | **Approvo** | |
| 8 Combattimento in 9 passi | **Approvo** | La sequenza è chiara e simulabile |
| 9 Vita e vittoria | **Contesto solo la scrittura** | Correzione 1 |
| 10 Il Leader in azione | **Approvo** | |
| 11 Primo giocatore | **Approvo** | |
| 12 Colori e carte | **Approvo con riserva** | Correzione 2 (Muro), punto c (Grido) |
| 13 Leggi di design | **Approvo** | |
| 14 Glossario | **Approvo** | |
| 15 Parametri | **Approvo** | |
| 16 Varianti | **Approvo** | V1-b descrive correttamente la mia posizione |
| 17 Moduli futuri | **Approvo** | |
| Pilastri | **Approvo** | |

**Correzione 1 — incoerenza nell'istantanea (§9.5 contro §6.1).**
- Il §9.5 scrive: *"istantanea §6.1, presa prima del Ripristino"*.
- Il §6.1 la colloca invece **al passo 2 del Ripristino**, dopo l'aumento del numero di turno. È la versione corretta: la soglia del turno 13 della Clessidra ne ha bisogno.
- Fix: in §9.5 scrivere *"presa al passo 2 del Ripristino"*. Senza questa correzione, chi implementa il simulatore deve scegliere tra due timing diversi.

**Correzione 2 — Muro di Scudi è troppo forte rispetto alla Parata (§12.3).**
- Muro dà *"+5 per 1 Guardia"*. È più di una Parata da 2 Guardia (+4), e in più riporta Pronto l'intercettore.
- Il principio "migliore della Parata a parità di Guardia" chiede almeno +3, non +5.
- Proposta: **+4**, sempre provvisorio, nella tabella del §15.

## 2. Voto sui punti aperti

**a. Terminazione entro il turno 15.**
**Voto:** aggiungere una terza soglia alla Clessidra: **dal turno 15 del giocatore attivo, ogni Leader è Alle Corde** (con qualsiasi numero di Vite). Il primo colpo a segno vince.
Leva di riserva, solo se il simulatore mostra più del 2% di partite oltre il turno 16: dal turno 15 la Tempra scende di 1 per turno, fino a un minimo di 1.
*Motivo:* chiude in pratica ogni partita al turno 15–16 senza introdurre punti, patte o perdita di Vita. È coerente con lo spirito della Clessidra (apre il finale invece di punire).

**b. Il primo giocatore raggiunge per primo le soglie della Clessidra.**
**Voto:** sì, va compensato, a costo zero. Le soglie della Clessidra (10 / 13 / 15) si leggono sul **numero di turno di G2** (il "round"), non su quello del giocatore attivo. Così il primo turno con Saldo 3 o con il colpo finale anticipato tocca a G2.
*Motivo:* G1 ha già il vantaggio di tempo della Fornace. Spostare il vantaggio della Clessidra su G2 non aggiunge testo né componenti, e dà al bilanciamento una leva gratuita in più.

**c. Grido dalla mano a −4 vale quanto una Parata di pari costo.**
**Voto:** Grido costa **1 Guardia, −3 Forza** all'attaccante, e diventa **−5 se giocata dalle Cicatrici** (sempre 1 Guardia).
*Motivo:* dalla mano batte la Parata a parità di Guardia (−3 contro +2). Dalle Cicatrici diventa il premio firma del Nero. Rispetta anche la clausola "ogni reazione costa almeno 1 Guardia" della variante V1-b, quindi vale con entrambe le versioni di V1.

**d. Bastione (costo 5, Forza 6, Scudo) contro la leva "Scudo con Forza ≤ costo".**
**Voto:** cambiare la **leva**, non la carta. Nuova forma: *"Le Unità con Scudo di costo ≤3 hanno Forza ≤ costo"*.
*Motivo:* lo stallo nasce da molti Scudo economici ed efficienti, non da un singolo finale da 5 Brace che è l'identità del Blu. La leva era mia e la scrivo meglio.

## 3. Ratifica

**Ratifico il regolamento v0.1** con le due correzioni di testo indicate sopra. Per il simulatore, l'ordine che propongo è:
1. le correzioni dei punti a–d;
2. il protocollo sequenziale del §16.3 senza modifiche;
3. V1 (una reazione per turno contro una per attacco) decisa dai dati, come concordato.
