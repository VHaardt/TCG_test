# Q-019, condizione di revisione R-3 (esito §8.2): lettura del thread principale

Dati: `R3_V024_forte/`, IA forte:30 v2 per tutta la partita, preset V024 (P6 [1,3,5], spareggio vite_attivo), 390 partite (50 mirror per mazzo + 6 per incrocio), seed 22, motore 19c11bc. Solo misura.

| Riga | Valore | Riferimento |
|---|---|---|
| **G1 nei mirror** (n=300) | **42.3 [36.9–48.0]** | soglia R-3: 48–52; con la forte e P6 [1,3] (E-019) G1 stava a 50.0 |
| G1 fra le arrivate al R15 | 37.0 [27.8–47.2] | semplice 46.1; R-1 (forte dal R14) 43.5 |
| G1 fra le finite al Crepuscolo | 28.6 [19.3–40.1] (n=70) | |
| Durata mediana | 13 (media 12.0) | 8–11 |
| Partite al round 13+ | 53.3 [48.4–58.2] | ≤12 |
| Fini al Crepuscolo | 70/390 = 17.9% | |
| Rimonte | 23.6 [17.3–31.2] (n=140) | 20–35 |
| Vittorie per mazzo | LDR-01 52.3, LDR-02 51.5, LDR-03 47.7, LDR-04 44.6, LDR-05 58.5, LDR-06 45.4 | (set v0.2 di bd92257, Thorn prima di Q-020) |

Lettura (fatti, non decisione):
1. **La soglia di R-3 è superata**: G1 nei mirror 42.3, con l'IC che arriva appena a 48.0. Per l'esito §8.2 questo **riapre P6, non il Crepuscolo**. Decide lo swarm (livello 3).
2. Va nella direzione dei pre-mortem (7 su 8): con la forte la gemma del R5 dà troppo a G2. Su 300 mirror l'IC è largo (±5.6), quindi il valore puntuale va confermato con un campione più grande prima di tarare un nuovo P6.
3. Lo svantaggio di G1 cresce nel finale (37.0 fra le arrivate al R15, 28.6 fra le finite al Crepuscolo). È coerente con R-1: lo spareggio `vite_attivo` premia G2 (71% degli spareggi con la forte dal R14).
4. Con la forte v2 le partite sono lunghe (mediana 13, 53% oltre il R13), come già in E-set R010_forte2 (mediana 12, 46.9%). Il Crepuscolo chiude il 18% delle partite: con la forte il finale pesa più che con la semplice.
