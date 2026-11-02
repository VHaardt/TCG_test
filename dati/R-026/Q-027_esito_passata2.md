# Q-027: esito della passata 2 (2026-11-02)

Hanno votato 8 ruoli su 8 sulla `round1/proposta_unificata.md`. Una voce passa con 6/8 e nessun veto. Questa è la scelta del pool da misurare: il voto finale sulle carte si fa dopo E-031.

## Approvate
| Voce | Voto | Note |
|---|---|---|
| G1, sacrificio | 8/8 | testo della proposta |
| G2, anti-loop | 8/8 | testo della proposta |
| Obiettivi (Unità ferme ≤38%, Reazioni ≥0.10, rimozioni ≥1.0 per i non Rossi) | 8/8 | |
| NEW-I01 | 8/8 | |
| NEW-I02 | 6/8 | costo 2, tetto ≤4. Il competitivo voleva costo 3 e il critico tetto ≤3: nessuno dei due emendamenti arriva a 6 |
| NEW-I03, emendamento "Pronta" | 7/8 | il nero è contrario. Testo: "…Riporta in mano al suo proprietario un'Unità avversaria **Pronta** con costo ≤4." |
| NEW-I04 | 6/8 | resta Neutrale. Il competitivo voleva Verde e l'analista Nero: si guarda il dato nella lista di rottura di L5 |
| NEW-I05 | 6/8 | il nero è contrario. Il critico chiede "pesca 1 se il mazzo non è vuoto": è già la regola generale della pesca, nessun cambio di testo |
| NEW-I06 | 8/8 | |
| NEW-I08 | 8/8 | con "che non ha Quando entra" |
| NEW-I09, NEW-I10 | 8/8 | |
| Bracci A, B, C | 8/8 | |

## Respinte o non adottate
- **NEW-I07:** 4/8 (verde, blu, nero, critico; il ponti la voleva Nera). Torna in riserva. Il braccio C perde I07: Maera riceve I08 e I09.
- **Braccio D ("−3 → −4"):** respinto 8/8.
- **Riammissione di P08:** respinta 7/8. Torna solo se il braccio A resta sotto 0.09–0.10 Reazioni per scontro.

## Guardie riscritte
- **"Leader fra 45 e 55"** non si può soddisfare oggi, perché i Rossi sono fuori fascia. Vale la forma dell'analista: per ogni Leader, valore ≤ 55 **oppure** distanza dalla fascia che non peggiora di più di 1.0 punti.
- **Δ01 + Δ05 ≤ +1, regola del rumore (analista).** Su un braccio da ~1.000 partite l'IC è circa ±10. Fra +1 e +6 si rimisura sul torneo completo; sopra +6 il braccio cade.
- **Durata:** come nella proposta (round 13+ ≤ +2; fra +2 e +4 una sola rimisura; sopra +4 cade).
- **Celle extra sulle liste di rottura di L5 e L1** (rosso, blu, critico, analista): si aggiungono a ogni braccio come dettaglio di misura, circa +2–4 ore.

## Previsioni registrate (per il confronto dopo E-031)
- **A:** Reazioni da 0.07 a circa 0.09–0.10 per scontro.
- **B:** Unità ferme −2/−3 punti; rimozioni +0.6/0.8 a partita.
- **C:** Rimarginare +0.3/0.6 a partita.
- round 13+ entro circa +1 per ogni braccio.
- Nessun braccio da solo porta le Unità ferme a ≤38%.

## Prossimi passi
1. R-026 al thread principale: primitive `bounce`, `on_rim`, `sacrifice` (G1), `recover` (G2); verifica della Reazione a costo 0 e della condizione "nessuna gemma nel tuo impegno" (I04). `heal` non si chiede.
2. Il programmatore scrive le carte e i bracci di E-031 su B0c05 e V027. I01, I05 e I06 si scrivono subito.
3. E-031 parte dopo E-030.
4. Cure: restano fuori finché Vittorio non le chiede come vincolo. La forma "risucchio" resta in riserva.
