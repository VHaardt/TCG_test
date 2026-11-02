# E-031_q027 / C-r5

- **Voto:** C, cimitero e Rimarginare (8/8, senza I07): I08 e I09 in Maera, I08 e I10 in LDR-06; celle extra sulla rottura di L5.
- **Carte nuove:** `NEW-I08` (bozza: da validare quando c'è la primitiva di R-026), `NEW-I09` (bozza: da validare quando c'è la primitiva di R-026), `NEW-I10` (bozza: da validare quando c'è la primitiva di R-026). Testi e JSON in `../carte_q027.json`.
- **Scambi (2 copie per carta; la carta che esce ha lo stesso tipo o lo stesso compito e costo vicino, così la curva resta):**
  - `rif_LDR02_muro_di_parata`: −NER-014, −NER-014 → +NEW-I09, +NEW-I09. Unità nera da 3 per Unità nera da 3 (F3 Scudo → F2 con Stanca al Rimarginare; gli Scudo della lista scendono da 11 a 9).
  - `rif_LDR02_muro_di_parata`: −BLU-016, −BLU-016 → +NEW-I08, +NEW-I08. Unità da 4 che fa carte (⟳ pesca 1) per Unità da 3 che fa carte (recupero).
  - `rif_LDR06_ferite_e_caccia`: −NER-001, −NER-013 → +NEW-I08, +NEW-I08. due Unità nere da 3 a Furia per l'Unità nera da 3 con recupero.
  - `rif_LDR06_ferite_e_caccia`: −VER-010, −VER-008 → +NEW-I10, +NEW-I10. le due Unità verdi da 2 a F1 più deboli per l'Unità verde da 2 a F2.
- **Liste di rottura:** `rif_LDR05_scudi_armati` sostituita da `rott_LDR05_2c` (nome della rif_ lasciato per il lanciatore).
- **Liste toccate, dopo gli scambi:**
  - `rif_LDR02_muro_di_parata`: 40 carte, 17 Unità, 17 Reazioni, 9 Scudo, costo medio 2.52, colori B 23 K 11, massimo copie 2 (in B0c05: costo medio 2.58).
  - `rif_LDR05_scudi_armati`: 40 carte, 32 Unità, 7 Reazioni, 15 Scudo, costo medio 2.50, colori B 18 R 18, massimo copie 2 (in B0c05: costo medio 2.40).
  - `rif_LDR06_ferite_e_caccia`: 40 carte, 27 Unità, 7 Reazioni, 2 Scudo, costo medio 2.70, colori G 17 K 18, massimo copie 2 (in B0c05: costo medio 2.70).
- **Si misura:** IA forte:30, 200 partite per incrocio, celle `2-5,5-6` (2 incroci, 400 partite, ~1.4 h su 4 core), semi 3400+k; contro E-030_q026/R5-2c F_s3400 (stesse celle e semi).
- **Comando:** `E031_TRACCIA=$(cat traccia.txt) bash ../lancia_e031.sh C-r5 forte:30 200 3400 2-5,5-6`.
