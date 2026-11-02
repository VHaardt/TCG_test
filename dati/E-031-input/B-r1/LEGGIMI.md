# E-031_q027 / B-r1

- **Voto:** B, rimozioni e sacrificio (8/8): I01 e I02 in LDR-06 e Maera, I03 solo in Maera; celle extra sulla rottura di L1.
- **Carte nuove:** `NEW-I01` (finale), `NEW-I02` (bozza: da validare quando c'è la primitiva di R-026), `NEW-I03` (bozza: da validare quando c'è la primitiva di R-026). Testi e JSON in `../carte_q027.json`.
- **Scambi (2 copie per carta; la carta che esce ha lo stesso tipo o lo stesso compito e costo vicino, così la curva resta):**
  - `rif_LDR06_ferite_e_caccia`: −NER-011, −NER-011 → +NEW-I01, +NEW-I01. Tattica nera che toglie un'Unità Pronta dallo scontro (Stanca, costo 2) per Tattica nera che la sconfigge (costo 3).
  - `rif_LDR06_ferite_e_caccia`: −VER-013, −VER-013 → +NEW-I02, +NEW-I02. Tattica da 2 di Stanca per Tattica da 2 di rimozione: le rimozioni crescono, la curva no.
  - `rif_LDR02_muro_di_parata`: −NEU-003, −NER-021 → +NEW-I01, +NEW-I01. rimozione da 3 su Ruotata e Reliquia nera da 5 per la rimozione nera da 3 su Pronta.
  - `rif_LDR02_muro_di_parata`: −NEU-002, −NEU-002 → +NEW-I02, +NEW-I02. Reliquia da 2 (massimo di Guardia) per Tattica da 2: le Unità (17) restano tutte.
  - `rif_LDR02_muro_di_parata`: −BLU-017, −BLU-017 → +NEW-I03, +NEW-I03. Tattica blu di risposta da 4 per la Tattica blu di risposta da 3 (rimbalzo).
- **Liste di rottura:** `rif_LDR01_puntata_e_preda` sostituita da `rott_LDR01_2c` (nome della rif_ lasciato per il lanciatore).
- **Liste toccate, dopo gli scambi:**
  - `rif_LDR01_puntata_e_preda`: 40 carte, 28 Unità, 6 Reazioni, 0 Scudo, costo medio 2.33, colori G 14 R 22, massimo copie 2 (in B0c05: costo medio 2.30).
  - `rif_LDR02_muro_di_parata`: 40 carte, 17 Unità, 17 Reazioni, 11 Scudo, costo medio 2.48, colori B 25 K 12, massimo copie 2 (in B0c05: costo medio 2.58).
  - `rif_LDR06_ferite_e_caccia`: 40 carte, 27 Unità, 7 Reazioni, 2 Scudo, costo medio 2.75, colori G 15 K 20, massimo copie 2 (in B0c05: costo medio 2.70).
- **Si misura:** IA forte:30, 200 partite per incrocio, celle `1-2,1-6` (2 incroci, 400 partite, ~1.4 h su 4 core), semi 3400+k; contro E-031_q027/R1-2c F_s3400 (stesse celle e semi).
- **Comando:** `E031_TRACCIA=$(cat traccia.txt) bash ../lancia_e031.sh B-r1 forte:30 200 3400 1-2,1-6`.
