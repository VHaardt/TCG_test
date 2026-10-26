# E-030_q026 / M3

- **Cosa cambia rispetto a B0c05 (carte B0c03 + liste B0c05):**
  - Nuova carta `NEW-B06` (Unità N/V, costo 6, F5, Caccia, rarità L): statica `power +2` con `if: [attacking, scars_ge 3]` (stessa forma di BLU-015 e VER-020, il +2 vale solo quando attacca).
  - `rif_LDR06_ferite_e_caccia`: −1 VER-023, +1 NEW-B06 (costo 6 per costo 6, come proposto dal designer ponti in round1). Colori: V −1, N/V +1 (la carta bicolore conta per entrambi).
- **Voto / ruolo:** M3, 8/8 (costo 6, F5).
- **Liste nel braccio:**
  - `rif_LDR01_puntata_e_preda`: 40 carte, 28 Unità, 0 Scudo, colori G 16 R 22, massimo copie 2.
  - `rif_LDR02_muro_di_parata`: 40 carte, 17 Unità, 11 Scudo, colori B 25 K 9, massimo copie 2.
  - `rif_LDR03_sanguinare_per_accendere`: 40 carte, 28 Unità, 0 Scudo, colori K 26 R 14, massimo copie 2.
  - `rif_LDR04_stanca_e_smonta`: 40 carte, 27 Unità, 10 Scudo, colori B 14 G 21, massimo copie 2.
  - `rif_LDR05_scudi_armati`: 40 carte, 32 Unità, 15 Scudo, colori B 19 R 18, massimo copie 2.
  - `rif_LDR06_ferite_e_caccia`: 40 carte, 27 Unità, 2 Scudo, colori G 17 K 19, massimo copie 2.
- **Si misura:** IA forte, 200 partite per incrocio, protagonisti `6` (5 incroci), semi 3400+k; contro E-030_q026/00_B0c05 F_s3400.
- **Comando:** `E030_TRACCIA=$(cat traccia.txt) bash ../lancia_e030.sh M3 forte:30 200 3400 6` (uscita `tcg/swarm/esperimenti/E-030_q026/M3/F_s3400`), stima 3.6 h su 4 core.
- **Regole:** `tcg/swarm/questioni/Q-026_feedback_playtest/esito_passata2.md`.
