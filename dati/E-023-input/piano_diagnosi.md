# Ciclo 02 e Q-021 — Piano della diagnosi (analista)

Data: 2026-10-13. È solo diagnosi: nessuna leva, il round 1 alla cieca viene dopo.

**Fonti:** `protocolli/ciclo_bilanciamento.md`, `questioni/Q-021_fuori_fascia_dopo_ciclo01.md`, `Q-020_bilanciamento_ciclo01/{esito, esito_fase2_F, diagnosi_LDR05}.md`.

**Costi:** IA forte circa 4 ore ogni 1.000 partite (thread principale); IA semplice circa 0.2 ore ogni 6.000 (E-020).

## Cosa sappiamo già, a costo zero
Dati E-020 su V024, B0 S con seed 2000 e B0 F con seed 3000:

| LDR-06 | S | F |
|---|---|---|
| Vittorie | 37.0 | 27.8 |
| contro LDR-01 | 31 | 14 |
| contro LDR-05 | 29 | 11 |
| contro Vey | 26 | 34 |
| Attivazioni del Leader | 3.4 | 3.95 |
| Vita pagata (M14) | 0.99 | 1.68 |

Con la forte LDR-06 crolla contro i due Rossi aggressivi. Usa di più la Base e paga più Vita, e perde lo stesso. L'ipotesi "la forte non usa le Cicatrici" va quindi verificata: i contatori dicono che la Base la usa, e di più.

## (a) Da lanciare subito su V024 (non dipendono da P6)
I bracci sono costruiti sul set di `E-020/00_B0`, cioè la Thorn di prima di Q-020. Così sono **appaiati con i B0 S e F V024 già giocati** e non serve un riferimento nuovo. Rispetto al set attuale differisce solo la cella contro Thorn.

Su P6 come leva, i Δ di E-020 sono rimasti entro 1.3 punti passando da V02 a V024. Se Q-022 cambia P6, basta un controllo con S (0.2 ore) su D06_vuoto.

| Pr. | Misura (braccio E-023) | Cosa decide | IA | Preset | Partite | Ore |
|---|---|---|---|---|---|---|
| 1 | **D06_vuoto**: LDR-06 con Base e Risvegliato vuoti | **Carta o IA per LDR-06.** Se il vuoto con F resta ≈27.8 (Δ entro ±6), il testo non vale nulla con la forte, che pure lo attiva 3.95 volte a partita: allora è il testo, o il costo in Vita, che non rende. Se il vuoto scende di oltre 6, il testo serve e il deficit sta nel mazzo | F, protagonista 6, 100 partite per incrocio | V024 | 500 | 2.0 |
| | | | S, torneo completo con `--traccia` sulle carte di `rif_LDR06` | V024 | 6.000 | 0.2 |
| 2 | **D06_base_vuota**: solo la Base vuota | Separa la Base (Vita e Cicatrici) dal Risvegliato (Caccia) | F, protagonista 6, 100 per incrocio | V024 | 500 | 2.0 |
| 3 | **D01_vuoto**: LDR-01 con Base e Risvegliato vuoti | Quanto dei 68.2 di Arden è testo e quanto è mazzo (come `diagnosi_LDR05`) | F, protagonista 1, 100 per incrocio, più S completo tracciato | V024 | 500 + 6.000 | 2.2 |
| 4 | **D05_tetto**: lista di LDR-05 del nero | **Ciclo 02:** se la densità del pool regge anche con F (con S valeva −15.7). Dà anche quanto risale LDR-01 (+5.5 con S) | F, protagonista 5, 60 per incrocio | V024 | 300 | 1.2 |
| 5 | **B0 tracciato con S** (set E-020/00_B0, seed 2000) | Base per carta di LDR-01 e LDR-06: colpi, Unità "da sola", Vita pagata per carta, M11. È il confronto per le righe 1–3 | S, `--traccia` su tutte le carte di `rif_LDR01` e `rif_LDR06` | V024 | 6.000 | 0.2 |
| 6 | **D06_vita0**: la Base senza costo in Vita (solo diagnostico) | Se è il costo in Vita a rendere la Base perdente. **Solo S;** passa alla F (60 per incrocio, 1.2 ore) se con S dà ≥ +5 su B0 | S, poi F se scatta la condizione | V024 | 6.000 (+300) | 0.2 (+1.2) |

**Totale (a):** 7.2 ore di F (8.4 con la riga 6) e circa 1 ora di S. Lettura con IC appaiato al 95%, sempre accanto al numero di partite.

**Partite commentate.** Per LDR-06 contro LDR-01 e contro LDR-05 le chiede Q-021. Spettano ai playtester; i seed suggeriti sono quelli delle celle B0 F 1-6 e 5-6.

## (b) Torneo di riferimento del ciclo 02, dopo l'esito di Q-022
Si usa il set attuale (`tcg/set/finale`, Thorn con T1+V2) e il preset del nucleo uscito da Q-022: V024 se P6 resta [1,3,5], altrimenti il nuovo.

| Misura | Cosa decide | IA | Partite | Ore |
|---|---|---|---|---|
| **B0-c02 F**: torneo completo 15 × 100, seed 3000 | Il riferimento del ciclo 02 e di Q-021. Il livello di LDR-01, 05 e 06 con la nuova Thorn. **Riverifica di Thorn** (45.2 ±4.3) | F | 1.500 | 6.0 |
| **mix_M3** contro i 5 rif, 60 per incrocio | La sorveglianza del lucchetto: deve restare ≤45%, oggi è 35.0 | F | 300 | 1.2 |
| *(facoltativo)* incroci di Thorn +100 per incrocio, seed 3100 | Il round 13+ di Thorn con un IC più stretto (Δ da ±6 a circa ±4.5). Riferimento 49.2 (B0 V024), con guardia ≤ +3 | F | 500 | 2.0 |
| **B0-c02 S**, torneo completo 400 per incrocio più mix | Il controllo con la semplice e il seed 2000 per i bracci futuri | S | 8.000 | 0.3 |

- `--traccia` su tutte le carte di `rif_LDR01`, `rif_LDR04`, `rif_LDR05` e `rif_LDR06`, e su LDR-01…06.
- **Totale (b):** 7.2 ore di F (9.2 con la riga facoltativa) più 0.3 di S.
- **Deviazione dichiarata:** il protocollo chiede ≥2.000 partite per abbinamento con F, cioè circa 120 ore. Si resta a 100 per incrocio come in E-020.

## Bracci creati
Cartelle in `tcg/set/esperimenti/E-023/`: `D06_vuoto`, `D06_base_vuota`, `D06_vita0`, `D01_vuoto`, `D05_tetto`.

- Ogni cartella contiene `set_v02.json`, `mazzi_v02.json` e `LEGGIMI.md`, più le copie `carte.json` e `mazzi.json` per `lancia_e020.sh`.
- Tutte sono validate con il motore 934a469: 0 errori.
- D06_vita0 ha fatto una prova di fumo di 20 partite (gira; la Base si attiva 4.25 volte a partita).
- Non ho toccato repo, set finale, bozze né regolamento.
