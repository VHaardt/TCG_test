# E-030_q026 / M2

- **Cosa cambia rispetto a B0c05 (carte B0c03 + liste B0c05):**
  - Nuova carta `NEW-V05` (Tattica verde, costo 2, rarità R): `play` con bersaglio `{side: opp, ready: true, keyword: scudo}`, `stanca` sul bersaglio; nessun `cost_le`.
  - `rif_LDR04_stanca_e_smonta`: −1 NEU-011, −1 VER-002, +2 NEW-V05. Escono le due Tattiche di Stanca più simili: NEU-011 (Stanca ≤3 da 2, entrata con la correzione del critico al posto di VER-012) è la sola altra Stanca da 2; resta 1 VER-002 per la curva bassa. Colori: neutra −1, verde +1.
  - `rif_LDR06_ferite_e_caccia`: −2 VER-013, +2 NEW-V05. VER-013 (Stanca ≤3 da 2) è la sola Tattica di Stanca della lista ed è entrata in B0c05 al posto di NER-015.
  - `rif_LDR01_puntata_e_preda`: −2 VER-013, +2 NEW-V05. VER-013 ×2 sono entrate in B0c05 come riempitivi (sostituti di Reazioni gemelle G2) e sono le carte più simili; restano le 2 VER-002.
  - Copie per nome ≤2; in L1 e L6 colori invariati (verde per verde).
- **Voto / ruolo:** M2, 8/8; LDR-01 su richiesta del critico (round1/discussione_critico.md).
- **Liste nel braccio:**
  - `rif_LDR01_puntata_e_preda`: 40 carte, 28 Unità, 0 Scudo, colori G 16 R 22, massimo copie 2.
  - `rif_LDR02_muro_di_parata`: 40 carte, 17 Unità, 11 Scudo, colori B 25 K 9, massimo copie 2.
  - `rif_LDR03_sanguinare_per_accendere`: 40 carte, 28 Unità, 0 Scudo, colori K 26 R 14, massimo copie 2.
  - `rif_LDR04_stanca_e_smonta`: 40 carte, 27 Unità, 10 Scudo, colori B 14 G 22, massimo copie 2.
  - `rif_LDR05_scudi_armati`: 40 carte, 32 Unità, 15 Scudo, colori B 19 R 18, massimo copie 2.
  - `rif_LDR06_ferite_e_caccia`: 40 carte, 27 Unità, 2 Scudo, colori G 17 K 18, massimo copie 2.
- **Si misura:** IA forte, 200 partite per incrocio, protagonisti `1,4,6` (12 incroci), semi 3400+k; contro E-030_q026/00_B0c05 F_s3400.
- **Comando:** `E030_TRACCIA=$(cat traccia.txt) bash ../lancia_e030.sh M2 forte:30 200 3400 1,4,6` (uscita `tcg/swarm/esperimenti/E-030_q026/M2/F_s3400`), stima 8.7 h su 4 core.
- **Regole:** `tcg/swarm/questioni/Q-026_feedback_playtest/esito_passata2.md`.
