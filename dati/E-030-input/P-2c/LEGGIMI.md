# E-030_q026 / P-2c

- **Cosa cambia rispetto a B0c05 (carte B0c03 + liste B0c05):**
  - Le leve di P di E-029, identiche: NEU-013 Forza 3 → 2, BLU-008 Forza 2 → 1 (`power`, testo invariato); LDR-05 Base senza testo (`base: []`), Risvegliato invariato.
  - `rif_LDR05_scudi_armati` è quella di B0c05: NEU-013 ×2, BLU-008 ×2 (in B0c03 erano ×3 e ×3).
- **Voto / ruolo:** C: P rimisurata su B0c05 (lo screening di E-029 dà Δ05 −2.5 ≤ −1.5: si lancia).
- **Liste nel braccio:**
  - `rif_LDR01_puntata_e_preda`: 40 carte, 28 Unità, 0 Scudo, colori G 16 R 22, massimo copie 2.
  - `rif_LDR02_muro_di_parata`: 40 carte, 17 Unità, 11 Scudo, colori B 25 K 9, massimo copie 2.
  - `rif_LDR03_sanguinare_per_accendere`: 40 carte, 28 Unità, 0 Scudo, colori K 26 R 14, massimo copie 2.
  - `rif_LDR04_stanca_e_smonta`: 40 carte, 27 Unità, 10 Scudo, colori B 14 G 21, massimo copie 2.
  - `rif_LDR05_scudi_armati`: 40 carte, 32 Unità, 15 Scudo, colori B 19 R 18, massimo copie 2.
  - `rif_LDR06_ferite_e_caccia`: 40 carte, 27 Unità, 2 Scudo, colori G 17 K 18, massimo copie 2.
- **Si misura:** IA forte, 200 partite per incrocio, protagonisti `1,5` (9 incroci), semi 3400+k; contro E-030_q026/00_B0c05 F_s3400.
- **Comando:** `E030_TRACCIA=$(cat traccia.txt) bash ../lancia_e030.sh P-2c forte:30 200 3400 1,5` (uscita `tcg/swarm/esperimenti/E-030_q026/P-2c/F_s3400`), stima 6.5 h su 4 core.
- **Regole:** `tcg/swarm/questioni/Q-026_feedback_playtest/esito_passata2.md`.
