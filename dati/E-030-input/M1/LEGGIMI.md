# E-030_q026 / M1

- **Cosa cambia rispetto a B0c05 (carte B0c03 + liste B0c05):**
  - NER-002: `play.costs` da `[{lose_life: 1, floor: 1}]` a `[{any: [{lose_life: 1, floor: 1}, {stanca_own: 1}]}]`; testo aggiornato. Il `floor` vale per il ramo in Vita (come oggi: non pagabile con 1 Vita o meno); la Stanca di una propria Unità Pronta resta sempre pagabile.
  - NER-019: `play.costs` da `[{lose_life: 2, floor: 1}]` (2 Vite, non giocabile con 2 o meno) allo stesso costo `any` di NER-002 (1 Vita con floor 1, oppure Stanca una tua Unità Pronta); bersaglio ed effetti invariati.
  - Rientro nelle liste (senza le carte il braccio non misura nulla). In B0c05 NER-002 è solo in `rif_LDR03` (×2, invariata) e NER-019 in nessuna lista; LDR-06 le aveva tolte per il costo nel ciclo 02.
  - `rif_LDR06_ferite_e_caccia`: −1 NEU-004, −1 VER-010, +2 NER-002 (escono le due carte da 1–2 più deboli della lista, entrate in B0c05 come sostituti di NEU-001 e VER-001); −1 VER-021, +1 NER-019 (stessa carta: Sconfiggi Ruotata costo ≤4 e pesca 1, costo 4). Colori: V −2, N +3; Unità 27 → 25.
  - Il contatore `cost_paid` del motore R-025 registra quale costo si paga, per carta.
- **Voto / ruolo:** M1, variante del nero 6/8 (approvata con condizione: contatore del costo pagato).
- **Liste nel braccio:**
  - `rif_LDR01_puntata_e_preda`: 40 carte, 28 Unità, 0 Scudo, colori G 16 R 22, massimo copie 2.
  - `rif_LDR02_muro_di_parata`: 40 carte, 17 Unità, 11 Scudo, colori B 25 K 9, massimo copie 2.
  - `rif_LDR03_sanguinare_per_accendere`: 40 carte, 28 Unità, 0 Scudo, colori K 26 R 14, massimo copie 2.
  - `rif_LDR04_stanca_e_smonta`: 40 carte, 27 Unità, 10 Scudo, colori B 14 G 21, massimo copie 2.
  - `rif_LDR05_scudi_armati`: 40 carte, 32 Unità, 15 Scudo, colori B 19 R 18, massimo copie 2.
  - `rif_LDR06_ferite_e_caccia`: 40 carte, 25 Unità, 2 Scudo, colori G 15 K 21, massimo copie 2.
- **Si misura:** IA forte, 200 partite per incrocio, protagonisti `3,6` (9 incroci), semi 3400+k; contro E-030_q026/00_B0c05 F_s3400.
- **Comando:** `E030_TRACCIA=$(cat traccia.txt) bash ../lancia_e030.sh M1 forte:30 200 3400 3,6` (uscita `tcg/swarm/esperimenti/E-030_q026/M1/F_s3400`), stima 6.5 h su 4 core.
- **Regole:** `tcg/swarm/questioni/Q-026_feedback_playtest/esito_passata2.md`.
