# E-031_q027 / A-r1

- **Voto:** A, Reazioni (8/8): I04 e I05 in Thorn e Maera, I06 solo in Maera; celle extra sulla rottura di L1.
- **Carte nuove:** `NEW-I04` (bozza: da validare quando c'è la primitiva di R-026), `NEW-I05` (finale), `NEW-I06` (finale). Testi e JSON in `../carte_q027.json`.
- **Scambi (2 copie per carta; la carta che esce ha lo stesso tipo o lo stesso compito e costo vicino, così la curva resta):**
  - `rif_LDR04_stanca_e_smonta`: −BLU-023, −BLU-023 → +NEW-I04, +NEW-I04. Reazione 'il bersaglio ha +X' per Reazione 'il bersaglio ha +2' (costo 1 → 0).
  - `rif_LDR04_stanca_e_smonta`: −VER-024, −VER-025 → +NEW-I05, +NEW-I05. Reazioni 'l'attaccante ha −X' (−3 da 1, −5 e pesca da 2) per −2 e pesca da Cicatrice (costo 1).
  - `rif_LDR02_muro_di_parata`: −BLU-023, −BLU-023 → +NEW-I04, +NEW-I04. come in Thorn: +4 al bersaglio da 1 → +2 alla propria Unità da 0.
  - `rif_LDR02_muro_di_parata`: −BLU-009, −NER-023 → +NEW-I05, +NEW-I05. le due 'l'attaccante ha −3' semplici da 1 (gemelle G2) per la −2 da 1 con pesca da Cicatrice.
  - `rif_LDR02_muro_di_parata`: −NER-003, −NER-003 → +NEW-I06, +NEW-I06. Reazione nera da 1 con bonus da Cicatrice per Reazione nera da 1 con bonus da Cicatrice.
- **Liste di rottura:** `rif_LDR01_puntata_e_preda` sostituita da `rott_LDR01_2c` (nome della rif_ lasciato per il lanciatore).
- **Liste toccate, dopo gli scambi:**
  - `rif_LDR01_puntata_e_preda`: 40 carte, 28 Unità, 6 Reazioni, 0 Scudo, costo medio 2.33, colori G 14 R 22, massimo copie 2 (in B0c05: costo medio 2.30).
  - `rif_LDR02_muro_di_parata`: 40 carte, 17 Unità, 17 Reazioni, 11 Scudo, costo medio 2.52, colori B 22 K 8, massimo copie 2 (in B0c05: costo medio 2.58).
  - `rif_LDR04_stanca_e_smonta`: 40 carte, 27 Unità, 5 Reazioni, 10 Scudo, costo medio 2.42, colori B 12 G 19, massimo copie 2 (in B0c05: costo medio 2.50).
- **Si misura:** IA forte:30, 200 partite per incrocio, celle `1-2,1-4` (2 incroci, 400 partite, ~1.4 h su 4 core), semi 3400+k; contro E-031_q027/R1-2c F_s3400 (stesse celle e semi).
- **Comando:** `E031_TRACCIA=$(cat traccia.txt) bash ../lancia_e031.sh A-r1 forte:30 200 3400 1-2,1-4`.
