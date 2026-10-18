# Ciclo 02 — Piano di E-024 (analista)

Data: 2026-10-18. Fonte: le 8 `round1/discussione_*.md`; la sintesi è in `round1/discussione.md`. Le regole sono scritte prima dei dati.

## 1. Disegno
- **Set:** ogni braccio è il set di `E-020/00_B0` più le sue leve (come E-023). Bracci in `tcg/set/esperimenti/E-024/<braccio>/`, validati sul motore 934a469 con 0 errori.
- **Riferimento appaiato:** B0 V024 già giocato, in `swarm/esperimenti/E-023/00_B0/{F,S}`. Seed: F 3000+k, S 2000+k, mix 20+o. Si lancia subito, senza aspettare Q-022.
- **Prima del voto:** le leve vincenti si rimisurano su B0-c02, cioè con P6 deciso da Q-022 (circa 2 ore per leva).
- **Lancio:** `bash tcg/set/esperimenti/E-024/lancia_e024.sh <braccio> <ia> <N> <seed> <protagonisti> [mix]`, dalla radice della repo.
- **Partite:** F = `forte:30`, 100 partite per incrocio sul protagonista. S = semplice, 400 partite per incrocio sugli stessi incroci.
- **Traccia:**
  - bracci A: `LDR-06,NER-013,VER-019,NER-018,NEU-015,NER-020,VER-008,VER-021`;
  - bracci B: `LDR-01,LDR-05,ROS-015,ROS-003,ROS-021,VER-019`.
- **Costo:** con F, 0.4 ore ogni 100 partite.

## 2. Bracci (testo esatto)
| Braccio | Leva | Protagonisti | IA | Partite F | Ore F | Fase |
|---|---|---|---|---|---|---|
| **A-FV** | rif_LDR06: −3 NER-002, −2 NER-019, +3 NER-013, +2 VER-019 (K19 G18 N3) | 6 | F+S | 500 | 2.0 | 1 |
| **A-IF** | rif_LDR06: −3 NER-002, −2 NER-019, +3 VER-019, +2 NER-018 (K18 G19 N3) | 6 | F+S | 500 | 2.0 | 1 |
| **B-R15** | ROS-015 «Impeto 2: +2 *(se nell'impegno hai almeno 2 gemme, +2 in questo scontro; …)*» (3/4/7 a 0/1/2 gemme) | 1 e 5 (9 incroci) | F+S | 900 | 3.6 | 1 |
| **B-U** | Base LDR-01: «Ogni tua Unità che attacca ha +1 in questo scontro, se nell'impegno hai almeno 2 gemme.» (`kind: unit`; il Leader non riceve il +1) | 1 | F+S | 500 | 2.0 | 1 |
| **B-3g** | Base LDR-01: «Ogni tuo personaggio che attacca ha +1 in questo scontro, se nell'impegno hai almeno 3 gemme.» | 1 | F+S | 500 | 2.0 | 1 |
| **A-LB_FV / A-LB_IF** | la lista vincente più la Base LDR-06: «Quando il tuo Leader attacca, Stanca un'Unità avversaria Pronta con Forza attuale pari o inferiore alle tue Cicatrici.» (stessa forma JSON della V2 di Thorn). Con `mix`: la rottura M6 contro i 5 rif, 60 partite per incrocio, e lo stesso M6 in A-FV come controllo con la Base attuale | 6 + M6 | F+S | 500 + 300 + 300 | 4.4 | 2 |
| **B-U_R15 / B-3g_R15** | la leva di testo più B-R15 | 1 e 5 | F+S | 900 | 3.6 | 2 |
| A-I | rif_LDR06: −3 NER-002, −2 NER-019, +3 VER-019, +2 NEU-015 | 6 | solo S | — | — | 1 |
| A-K | rif_LDR06: −3 NER-002, −2 NER-019, +3 NER-013, +2 NER-020 | 6 | solo S | — | — | 1 |
| B-Risv | Risvegliato LDR-01: «Le tue Unità con Assalto hanno +1 in questo scontro quando attaccano.» | 1 | solo S | — | — | 1 |

- **Rottura M6** (`mazzi_mix_M6.json`, chiesta da critico e nero): dalla rif_LDR06 di B0 −3 NER-002, −2 NER-019, −2 NER-025, −1 NER-022, −1 VER-003, −1 VER-023; +1 VER-021 (a 3), +3 VER-012, +1 NER-011 (a 3), +2 VER-010, +3 VER-002. È la sequenza «Stanca e poi sconfiggi la Ruotata».
- **A-I fusa in A-IF.** A-I (critico, competitivo) e A-F4 (ponti, rosso; uguale ad A-LV del blu) misurano la stessa ipotesi: Forza ≥4 dal turno 4 senza Furia, da opporre alla Furia di A-FV. Ho tenuto NER-018 al posto di NEU-015 per due motivi:
  - NEU-015 è un muro che si accende solo in opposizione (blu, nero);
  - porta il Nero a 16 carte (rosso).

  NER-020 resta fuori, perché il critico l'ha ritirata; A-K la misura con S. A-I gira solo con S come controllo della fusione: se con S supera A-IF di ≥3, lo segnalo al voto.
- **Totale:** fase 1 = 2.900 partite F (11.6 ore) più circa 17.600 S (0.6 ore). Fase 2, al massimo: 2.000 F (8 ore). Se il budget stringe, il primo taglio è B-3g; la regola resta "la leva più piccola fra quelle misurate".

## 3. Regole d'uscita consolidate (Δ F sul punto, appaiato con B0)
Dove i ruoli divergono tengo la versione più severa e indico tra parentesi da chi viene.

**Comuni a tutti i bracci:**
- vittorie prima del R5 che non salgono; R9-5 ≤1;
- nessun altro Leader peggiora di oltre **1.5** la distanza dalla fascia (rosso, verde; gli altri dicevano 2). Le celle contro il protagonista si escludono, salvo la guardia su LDR-05 nei bracci B;
- guardia Blu: Thorn e Maera non sotto 45 per effetto del braccio. Thorn è già a 33.8 in B0 (Thorn di prima di Q-020), quindi per lui la guardia si legge "non scende";
- oltre il 15 non sale (blu);
- **potenza:** se il punto passa ma l'IC del Δ contiene lo 0, prima del voto si aggiungono 100 partite per incrocio.

**A (LDR-06):** si prende il braccio con il Δ F più alto fra A-FV e A-IF, se valgono tutte:
- Δ F ≥ +4 **e** estremo inferiore dell'IC appaiato >0 (blu);
- Δ S ≥ +2 con l'IC di S sopra 0 (nero, ponti, rosso);
- celle contro LDR-01 e LDR-05 insieme ≥ **+4** (competitivo; gli altri +3);
- round 13+ negli incroci di LDR-06 al massimo +3;
- rimonte di LDR-06 fra 15 e 35% (nero);
- quota del colore minore ≥35%.

A parità entro 4 punti vince A-FV (nero): è la convergenza di 5 ruoli e tiene la Furia del Nero.

**A-LB (fase 2):**
- **Quando si lancia:** sopra la lista con il Δ F più alto, anche se quella non passa, se lascia LDR-06 sotto 35 (verde).
- **Quando passa:**
  - supera la sua lista di ≥ +3 con F (blu, verde, competitivo);
  - la combinazione rispetta tutte le regole di A rispetto a B0;
  - con la rottura M6, R9-5 ≤1;
  - M6 con A-LB non supera il suo controllo in A-FV di oltre +5. Questa soglia è mia: viene dal lucchetto M3 di Q-020, che salì di +8.7 con la V2 di Thorn.
- **Al voto:** il costo di originalità (lo stesso trigger della V2 di Thorn) va registrato, e il nero dichiara se il Nero lo accetta (competitivo).

**B (LDR-01 e LDR-05). Ogni leva da sola passa se valgono tutte:**
- Δ F(01) + Δ F(05) ≤ −3, e nessuno dei due sale (critico, rosso);
- per B-U e B-3g, in più Δ F(01) ≤ −3;
- LDR-01 F ≥ **50** (nero, rosso; gli altri 48);
- LDR-05 Δ F ≤ **+1**, cella 01–05 inclusa (critico; gli altri +1.5). La cella 01–05 resta fra 35 e 65 (competitivo);
- Vey non sale di oltre +1.5 (blu);
- round 13+ negli incroci di 01 e 05 al massimo **+2** (ponti e competitivo per R-15, esteso a tutti i bracci B);
- per B-R15 e i combinati: ROS-015 giocata ≥0.5 volte a partita.

**Regola di combinazione per B:**
1. Ordine di grandezza della leva:
   - **B-R15**: un numero su una carta comune;
   - **B-U**: toglie il +1 al solo Leader;
   - **B-3g**: alza la soglia per tutti gli attaccanti.

   Entra la **prima che passa da sola**, nell'ordine del critico, e nessun'altra.
2. Solo se nessuna passa da sola si lancia la coppia «testo di Arden + ROS-015». La leva di testo si sceglie così:
   - B-U o B-3g, la più piccola fra quelle con Δ F(01) ≤ −3 e LDR-01 ≥50;
   - se nessuna delle due rispetta queste condizioni, B-U.

   La coppia passa se rispetta tutte le regole B, con LDR-01 F ≤ **62** e LDR-05 F ≤ **70** (competitivo; il rosso diceva 63 e 71). Costa 2 modifiche.
3. Se anche la coppia non passa, B è "nessuna modifica" e va al ciclo 03 con la traccia F e D-05b.

**Bracci solo S (A-I, A-K, B-Risv):** sono informazione e non entrano al voto.

**Budget del ciclo:** al massimo 4 modifiche (A, eventualmente A-LB, e una o due B). Ne restano 1–2 per Q-022 e Thorn.
