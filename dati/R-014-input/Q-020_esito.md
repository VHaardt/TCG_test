# Q-020 — Esito: ciclo di bilanciamento 01 (LDR-05, Vey, Thorn)

| Campo | Valore |
|---|---|
| Livello | 2 (`protocolli/livello2_breve.md`; passa con i 2/3 dei votanti e senza veti validi) |
| Stato | **chiusa, decisa il 2026-10-13** |
| Decisione | **M1 approvata 8/8** (T1 + V2 su Thorn, come unica decisione); **M2 respinta 0/8**, con BLOCCO dell'analista; **M3 approvata 8/8** (rinvii) |
| Modifiche del ciclo | 2 su 5: T1 (lista) e V2 (Base di Thorn), votate come una sola decisione |
| Dati | `esperimenti/E-020/` (fase 1 S, round 2 S, fase 2 F su nucleo V024); letture dell'analista: `esito_fase1.md`, `esito_r2_S.md`, `esito_fase2_F.md`, `diagnosi_LDR05.md` |
| Editor | non vota |

## 1. Decisione

**M1. Thorn (LDR-04): T1 + V2 — SÌ 8/8.**
- **V2, nuova Base:** "Quando il tuo Leader attacca, Stanca un'Unità avversaria Pronta con costo ≤3." Prima era: "⟳, 1 Brace: Stanca un'Unità avversaria Pronta con costo ≤3." Il Risvegliato non cambia.
  - JSON: `leaders[LDR-04].base = [{"trigger":"on_attack","target":{"side":"opp","ready":true,"cost_le":3},"do":[{"op":"stanca","target":"chosen"}],"text":…}]`.
  - Serve la primitiva `on_attack` del Leader, presente nel motore dal commit feabc5c.
- **T1, lista `rif_LDR04_stanca_e_smonta`:** −1 BLU-016, −1 NEU-020, −1 VER-024, +3 BLU-015. Colore minore B 15/38 = 39.5%. Nessuna carta cambia testo.
- Le due modifiche sono state votate come **un'unica decisione**, perché V2 è stato misurato solo sopra T1. T1 da sola non passava: F +2.4, S +0.7.

**M2. LDR-05, braccio 18 (ROS-020 3/+3 più A2+A3 del Leader) — NO 0/8,** con **BLOCCO dell'analista** ("conclusioni senza evidenza sufficiente"). Nessuna leva su LDR-05 entra nel ciclo 01.

**M3. Rinvii — SÌ 8/8.**
- **Vey resta com'è:** l'innesco V-I non si applica.
- **LDR-05 va al ciclo 02** come problema di densità del pool Rosso/Blu.
- **LDR-01 e LDR-06 vanno a Q-021.**

## 2. Motivi in breve

**M1, motivi citati da tutti gli 8:**
- con F Thorn passa da 33.8 a **45.2 [40.9–49.6]**: +9.0 su T1, +11.4 su B0, cioè fuori dal rumore (Δ fra bracci circa ±6);
- è l'unico braccio che lo porta vicino alla fascia;
- R9-5 scende (Thorn 0.25, mix_M3 0.32, contro 0.56 di B0), quindi il super-controllo temuto non c'è.

Il competitivo aggiunge che la ⟳ smette di essere una scelta finta: il Leader attacca e insieme Stanca. Il ponti aggiunge che il Leader blu fa attaccare il mazzo verde.

**M2, motivi citati da tutti gli 8:**
- con F il Δ è −4.9, con un IC di circa [−11.5, +1.7] che contiene lo 0;
- LDR-05 resta a 67.3, fuori fascia;
- il round 13+ negli incroci di LDR-05 sale di +3.3;
- con S il braccio restituisce +2.6 a Vey e +2.0 a LDR-01;
- sono 2 modifiche (una sul testo del Leader) per un parziale, su un problema che le regole già mandano al ciclo 02 (D-tetto −15.7 con S, con uno scarto di 6.9 dal gradino; D-05f −3.7).

Il rosso: ROS-020 3/+3 resta la prima candidata del ciclo 02.

**M3, motivi:**
- **Vey.** Con F è già in fascia (49.8) e V-I vale +0.2, ma allunga le partite (round 13+ +6.8). L'eccesso visto con S (66–68) è un effetto dell'IA semplice.
- **LDR-05.** È fuori fascia con entrambe le IA (72.2 F, 72.0 S), e il tetto della lista dice che la causa è la densità del pool.
- **LDR-01 (68.2 F) e LDR-06 (27.8 F).** Vanno a Q-021; per LDR-06 si chiede prima la diagnosi carta/IA (nero, blu).

## 3. Numeri dell'IA forte

Fonte: forte:30 v2, motore 19c11bc, preset V024, seed 3000. B0 è un torneo completo da 100 partite per incrocio; il braccio 11 ha 100 partite per incrocio sugli incroci di Thorn.

| Leader | B0 F | Con T1+V2 | Fonte del "dopo" |
|---|---|---|---|
| LDR-01 Arden | 68.2 | circa 65.8 | stima: celle di B0, con quella contro Thorn presa dal braccio 11 (75 → 63) |
| LDR-02 Maera | 48.2 | circa 46.8 | stima (54 → 47) |
| LDR-03 Vey | 49.8 | circa 46.4 | stima (71 → 54) |
| **LDR-04 Thorn** | **33.8** | **45.2 [40.9–49.6]** | misurato (500 partite) |
| LDR-05 | 72.2 | circa 69.0 | stima (91 → 75) |
| LDR-06 | 27.8 | circa 26.8 | stima (40 → 35) |

- **Leader in fascia 45–55:** prima 2 (Maera, Vey), dopo 3 (Maera, Vey, Thorn al limite).
- **Scarto fra primo e ultimo:** da 44.4 a circa 42.2.
- **Braccio 11:**
  - vittorie prima del R5: 0.0% (B0 0.2%);
  - M6 +1.6;
  - attacchi del Leader 5.44 a partita, on_attack 1.84;
  - nessun Leader peggiora la sua distanza dalla fascia di oltre 1.0.

## 4. Rischi da sorvegliare (dichiarati nel voto)
1. **Round 13+ negli incroci di Thorn:** 53.0% contro 49.6% di T1 (+3.4) e 49.2% di B0 (+3.8).
   - La guardia del piano chiedeva "non sale" e al massimo +3: **alla lettera il braccio 11 non la passava**.
   - Tutti gli 8 lo hanno votato dichiarando il rischio, perché è dentro il rumore (±6).
   - Lo stallo Thorn–Maera c'era già: round 13+ all'84% in B0, all'86% in T1 e in 11 (critico).
2. **`mix_M3_thorn_lucchetto`:** vince il 35.0% [29.8–40.6] contro il 26.3% di B0 (+8.7). La soglia di sorveglianza è **≤45%** (critico).
3. **Riverifica:** entrambi i rischi si rimisurano nel prossimo torneo con F (ciclo 02 o Q-021). Thorn è in fascia al limite.

## 5. Minoranze, blocchi, cambi di posizione
- **Minoranze:** nessuna. Tutti gli 8 hanno votato allo stesso modo su ogni mozione.
- **Blocchi:**
  - **critico:** toglie il BLOCCO su V2 (posto nella discussione del r1) con un dato: R9-5 scende con F e mix_M3 resta sotto fascia;
  - **analista:** BLOCCO su M2, che è comunque respinta 0/8.
- **Cambi motivati:**
  - **blu:** sì a V2. Prima la rinviava perché chiedeva una primitiva, che ora c'è; la sua P-B ha dato solo +1.8 su T1;
  - **nero:** ritira "Vey alto = carta" del suo r1 (con F Vey è in fascia);
  - **competitivo:** applica la regola "se nessun gradino passa, si archivia" che aveva scritto nel round 2.
- **Previsioni su T1+V2** (F, scritte prima dei dati): verde 41, rosso 41, competitivo 43; misurato 45.2. Tutte le stime erano sotto il dato, al contrario della fase 1, dove tutte le leve erano state sovrastimate.

## 6. Applicazione (editor, 2026-10-13)
**File modificati:**
- `tcg/set/carte/bozza_neutrali.json`: Base di LDR-04;
- `tcg/set/finale/mazzi_v02.json`: carte di `rif_LDR04_stanca_e_smonta`.

**Rigenerazione:** `genera_finale.py` ha rigenerato `set_v02.json`, `set_v02.csv`, `leader_v02.csv` e `set_v02.xlsx`.

**Uguaglianza con gli input del braccio 11:**
- `leaders` e `cards` di `set_v02.json` coincidono con `tcg/set/esperimenti/E-020/11_T1_V2/carte.json` (sha256 dei JSON canonici: leaders 3da6affde7ed1613…, cards 4706847a789bd28e…, LDR-04 a361b52060788f7c…);
- le 6 liste `rif` e `mix_M3` coincidono con `11_T1_V2/mazzi.json` e `mazzi_mix_M3.json`, con `rif_LDR04` 521da777708ea921….

**Validatore:**
- comando: `python3 -m sim.v02.run valida set_v02.json --mazzi mazzi_v02.json`;
- motore 19c11bc, eseguito in una copia temporanea del repo;
- esito: **120 carte, 6 Leader, 0 errori**, exit 0.

**Hash dei file** (sha256):
- `set_v02.json` b8c056c3…;
- `mazzi_v02.json` 4f92dc82…;
- `bozza_neutrali.json` e1eab79e….

**Restano invariati, per uguaglianza con il set misurato:**
- il campo `intent` di LDR-04, che parla ancora di "Stanca economica dal Leader";
- l'intestazione del set (`rules` v0.2.1, `data` 2026-10-08), scritta fissa in `genera_finale.py`.

**Da propagare (thread principale):**
- testo di Thorn nel regolamento §12.2 e nel glossario;
- `bozza_neutrali.md`, la scheda leggibile;
- la primitiva `on_attack` del Leader nel regolamento, con il controllo del pilastro 9.

## 7. Condizione di revisione
Si riapre la decisione su Thorn se nel prossimo torneo con F almeno una di queste condizioni si verifica:
- il round 13+ negli incroci di Thorn supera di oltre 3 punti quello di B0 con un IC che esclude il rumore;
- `mix_M3` supera il 45%;
- Thorn esce dalla fascia (sotto 45 con l'estremo superiore sotto 45, oppure sopra 55).
