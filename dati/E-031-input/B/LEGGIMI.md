# E-031_q027 / B

- **Voto:** B, rimozioni e sacrificio (8/8): I01 e I02 in LDR-06 e Maera, I03 solo in Maera.
- **Carte nuove:** `NEW-I01` (finale), `NEW-I02` (bozza: da validare quando c'è la primitiva di R-026), `NEW-I03` (bozza: da validare quando c'è la primitiva di R-026). Testi e JSON in `../carte_q027.json`.
- **Scambi (2 copie per carta; la carta che esce ha lo stesso tipo o lo stesso compito e costo vicino, così la curva resta):**
  - `rif_LDR06_ferite_e_caccia`: −NER-011, −NER-011 → +NEW-I01, +NEW-I01. Tattica nera che toglie un'Unità Pronta dallo scontro (Stanca, costo 2) per Tattica nera che la sconfigge (costo 3).
  - `rif_LDR06_ferite_e_caccia`: −VER-013, −VER-013 → +NEW-I02, +NEW-I02. Tattica da 2 di Stanca per Tattica da 2 di rimozione: le rimozioni crescono, la curva no.
  - `rif_LDR02_muro_di_parata`: −NEU-003, −NER-021 → +NEW-I01, +NEW-I01. rimozione da 3 su Ruotata e Reliquia nera da 5 per la rimozione nera da 3 su Pronta.
  - `rif_LDR02_muro_di_parata`: −NEU-002, −NEU-002 → +NEW-I02, +NEW-I02. Reliquia da 2 (massimo di Guardia) per Tattica da 2: le Unità (17) restano tutte.
  - `rif_LDR02_muro_di_parata`: −BLU-017, −BLU-017 → +NEW-I03, +NEW-I03. Tattica blu di risposta da 4 per la Tattica blu di risposta da 3 (rimbalzo).
- **Liste toccate, dopo gli scambi:**
  - `rif_LDR02_muro_di_parata`: 40 carte, 17 Unità, 17 Reazioni, 11 Scudo, costo medio 2.48, colori B 25 K 12, massimo copie 2 (in B0c05: costo medio 2.58).
  - `rif_LDR06_ferite_e_caccia`: 40 carte, 27 Unità, 7 Reazioni, 2 Scudo, costo medio 2.75, colori G 15 K 20, massimo copie 2 (in B0c05: costo medio 2.70).
- **Si misura:** IA forte:30, 200 partite per incrocio, celle `p:2,6` (9 incroci, 1800 partite, ~6.5 h su 4 core), semi 3400+k; contro E-030_q026/00_B0c05 F_s3400 (stesse celle e semi).
- **Comando:** `E031_TRACCIA=$(cat traccia.txt) bash ../lancia_e031.sh B forte:30 200 3400 p:2,6`.
