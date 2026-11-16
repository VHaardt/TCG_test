# E-036-input — vaglio delle leve su L5 e L6 (ciclo 05, esito_piano.md P2)

Autore: programmatore (swarm), 2026-11-16. Voto: `tcg/swarm/cicli/ciclo-05/esito_piano.md` (P2, 8/8 con emendamenti). Richiesta al motore: `tcg/set/richieste/R-031_primitive_ciclo05.md`.

## Base e regole
- **Riferimento B0c06.** Carte da `tcg/set/finale/set_v02.json` (125); liste `rif_` da `tcg/set/finale/mazzi_v02.json`, senza le mix_.
- **Regole.** Tutti i bracci girano con `varianti/tempra_tardo.json`, cioè V027 + Tempra 3 dal round 10 (A), lo stesso file di E-033 ed E-034.
- **Cartelle.** Ogni braccio ha la sua, con `carte.json`, `mazzi.json` e `traccia.txt`, prodotte da `genera_e036.py`. Sono solo dati e si rigenerano con `python3 -B genera_e036.py [tcg/set]`.
- **Carte e testi provvisori.** Le nuove Basi e NEW-P31 e NEW-P32 sono solo nel braccio che le usa, non in `set/finale`.
- **Traccia.** È quella di E-034, più ROS-020, ROS-021, VER-002, VER-008, VER-003, NER-011, BLU-004, BLU-012, ROS-004, ROS-006, ROS-014, ROS-019, NEW-P31 e NEW-P32.

| Braccio | Cosa cambia rispetto a B0c06 | Celle (forte:30, 200 partite, semi 3700+k) | `valida` (V027 + A) | Stima su 4 core |
|---|---|---|---|---|
| **L5-c** | Base di LDR-05: "La prima delle tue Unità con Scudo che attacca in ogni turno ha +1 in questo scontro, se nell'impegno hai almeno 1 gemma." | i 5 incroci di L5 | **1 errore**: la condizione `first_attack_kw` non esiste (R-031 n.1) | ~3.6 h |
| **L5-b** | rif_LDR05: −BLU-004 ×2, −BLU-012 ×2; +ROS-004, +ROS-006, +ROS-014, +ROS-019 (ognuna da 1 a 2 copie). Gli Scudo scendono da 15 a 11 | i 5 incroci di L5, più L1-R5 e L2-R5 | 0 errori | ~5 h |
| **L6-a** | Base di LDR-06 con costo "perdi 1 Vita oppure Stanca una tua Unità Pronta" (vedi sotto) | i 5 incroci di L6 | 0 errori | ~3.6 h |
| **L6-ab** | L6-a più rif_LDR06: −VER-008, −VER-003; +VER-002 ×2 (NER-022 resta) | i 5 incroci di L6 | 0 errori | ~3.6 h |
| **L6-ad** | L6-a più rif_LDR06: −VER-008 ×2, +NEW-P31 ×2; −NER-011 ×2, +NEW-P32 ×2 | i 5 incroci di L6 | **1 errore**: la condizione `target_has` di NEW-P31 non esiste (R-031 n.2) | ~3.6 h |
| 00_B0c06A (facoltativo) | nulla: riferimento B0c06 + A sugli stessi semi | i 9 incroci di L5 e L6, più L1-R5 e L2-R5 | 0 errori | ~6.5 h |

Note sulle celle:
- **L1-R5 e L2-R5.** Sono L1 e L2 contro `rott_LDR05_2c`, la lista di rottura R5-2c del critico, presa da E-030 `R5-2c` (ciclo 04) e oggi legale con V027.
- **Semi.** Il seme della cella i-j è 3700+k, dove k è l'indice della coppia (1-2 → 1 … 5-6 → 15). L1-R5 usa il k di 1-5 (4) e L2-R5 quello di 2-5 (8), quindi sono appaiate con le celle L1-L5 e L2-L5.

**Riferimento per i Δ.** Il piano approvato non ha un braccio base sui semi 3700. Il riferimento che c'è è E-034 `tempra_tardo`, su semi 3500 e non appaiato. Se il thread vuole i Δ appaiati partita per partita, con IC più stretti (il "potenza insufficiente" dell'analista), può lanciare `00_B0c06A`: sono 2.200 partite, circa 6.5 h. Non fa parte del vaglio approvato, quindi è una scelta del thread.

## L6-a: costo "any" espresso come dati
Il testo è "⟳, il tuo Leader perde 1 Vita *(rispetta il Saldo)* oppure Stanca una tua Unità Pronta: Stanca un'Unità avversaria Pronta con Forza attuale inferiore alle tue Cicatrici. Non puoi pagare in Vita se il tuo Leader ha 2 Vite o meno."

Nella Base ci sono **due abilità ⟳**. Tutte e due ruotano il Leader, quindi se ne usa una sola per turno:
1. costo `lose_life` 1 con `floor` 2; bersaglio Pronto con `power_le` Cicatrici. È come oggi: le Cicatrici si contano prima di pagare, e dopo il pagamento ce n'è una in più;
2. costo `stanca_own` 1; bersaglio Pronto con `power_le` {Cicatrici − 1}. Il pagamento non aggiunge Cicatrici, quindi "inferiore" significa ≤ Cicatrici − 1.

Un solo `any` con `power_le` Cicatrici farebbe bersagliare con la Stanca anche la Forza pari alle Cicatrici, cioè una carta più forte del testo. Per questo le abilità sono due e il motore non va toccato.

Prova (forte:30, 1 partita per cella): la Base si attiva in tutti e due i modi. Il log ha, per esempio, "P2 Stanca NER-009 per pagare il costo / P2 usa ⟳ del Leader su BLU-005"; nelle 5 celle ci sono da 1 a 5 attivazioni e da 0 a 2 costi in Vita.

## Lancio
Dalla radice della repo, su main 7ec6380 o successivo:

    nohup bash dati/E-036-input/lancia_e036.sh tutti > /dev/null 2>&1 &

- Con `tutti` partono i cinque bracci in ordine. **L5-c e L6-ad si saltano**, con un messaggio nel registro, finché `sim/v02/validate.py` non ha le condizioni di R-031. Dopo R-031 basta rilanciare: gli incroci già finiti si saltano.
- Record per partita: in ogni cella resta `partite.pkl`, come in E-034. Lo stesso vale per `--riprendi`.
- Le uscite vanno in `tcg/swarm/esperimenti/E-036_vaglio/<braccio>/F_s3700/<cella>/`.

## Cosa leggere nel report
Oltre alle tabelle di E-034 (R-028, R-026, P9b, Scudo, R-017, M5):

| Misura | Dove |
|---|---|
| Attivazioni della Base del Leader protagonista | R-012 "contatori per mazzo", colonna "Attivazioni del Leader (⟳ e trigger)". **Oggi è la somma fra Base e Risvegliato**: la divisione per lato è R-031 n.3. Prima di R-031 si legge sulla somma, dichiarandolo |
| Costi in Vita a partita | R-005 M14 ("Costi in Vita pagati per partita") e Q-026 M5 per round; dai record, `life_costs` |
| Fa ≥ 8 di ROS-021 e ROS-020 | tabella R-017 per carta tracciata: ROS-020 e ROS-021 sono nella traccia di ogni braccio |
| Scudo a ≥2 gemme | R-012 "contatori per mazzo", colonna "Scudo a ≥2 gemme" |
| Cella L6–L5 | `L5-L6` in tutti i bracci, perché è sia fra gli incroci di L5 sia fra quelli di L6 |
| Vey con A | cella `L3-L5` nei bracci L5 e `L3-L6` nei bracci L6. Il livello di Vey su tutti gli incroci non si vede, perché il vaglio gioca solo le celle del protagonista: va letto su E-034 `tempra_tardo` |
| Vittorie entro il R5 (≤ 1%) | R-028 ritmo |
