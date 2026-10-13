# Q-019, condizione di revisione R-1 (esito §8.1): lettura del thread principale

Dati: `R1_vite_attivo/` e `R1_vite_difensore/`, 10 080 partite per parola, IA `cambio:14:forte:30` (semplice fino al R13, forte v2 dal R14), seed 19 (come la diagnostica V024), motore 19c11bc, set v0.2 (bd92257). Nessuna regola cambia: è solo una misura.

| Riga | vite_attivo (regola in vigore) | vite_difensore (braccio pronto) |
|---|---|---|
| Spareggi (entrambi Alle Corde, qualunque controllo) | 399 | 450 |
| Stallo: il vincitore dello spareggio non va a segno nel suo ultimo turno | **93.7 [90.9–95.7]** | **95.1 [92.7–96.7]** |
| Stallo: il vincitore non attacca nel suo ultimo turno | **60.9 [56.0–65.6]** | **69.8 [65.4–73.8]** |
| Guardia media del vincitore nella sua ultima Fine | 2.78 | 3.23 |
| G2 vince lo spareggio | 70.9 | 23.8 |
| G1 fra le arrivate al R15 | 43.5 [40.9–46.0] | 56.0 [53.4–58.5] |
| G1 nei mirror | 49.3 [47.5–51.1] | 51.1 [49.3–52.9] |
| Rimonte | 20.0 [18.5–21.6] | 20.3 [18.8–21.9] |
| Vincitori degli spareggi (primi tre) | LDR-04 163, LDR-02 117, LDR-06 71 | LDR-04 159, LDR-02 140, LDR-06 86 |

Lettura (fatti, non decisione):
1. **La soglia scritta è superata alla lettera**: con `attivo` il vincitore dello spareggio non va a segno nel 93.7% (>50%). Per l'esito §8.1 questo **riapre la parola a parità**. La decisione spetta allo swarm (livello 3).
2. Il primo indicatore è quasi tautologico: chi vince allo spareggio vince al controllo e non con un colpo, quindi il suo ultimo turno di rado ha un colpo a segno. L'indicatore "non attacca" è più informativo e sta comunque sopra il 50% (60.9).
3. **Il braccio pronto non risolve lo stallo, lo peggiora**: con `difensore` lo stallo sale su entrambe le righe (non attacca: 69.8 contro 60.9, IC disgiunti) e la Guardia finale del vincitore è più alta. Lo spareggio cambia solo *chi* vince lo stallo (G2 nel 71% con `attivo`, G1 nel 76% con `difensore`), non se c'è.
4. Lo stallo viene dai mazzi difensivi: LDR-04 e LDR-02 vincono circa due terzi degli spareggi con entrambe le parole.
5. Con la forte dal R14 lo scarto di G1 al R15 è simmetrico: −6.5 con `attivo`, +6.0 con `difensore`.
