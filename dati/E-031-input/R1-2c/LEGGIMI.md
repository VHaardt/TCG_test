# E-031_q027 / R1-2c

- **Voto:** riferimento: rottura di L1 contro le liste B0c05 dei protagonisti 2, 4, 6.
- **Liste di rottura:** `rif_LDR01_puntata_e_preda` sostituita da `rott_LDR01_2c` (nome della rif_ lasciato per il lanciatore).
- **Liste toccate, dopo gli scambi:**
  - `rif_LDR01_puntata_e_preda`: 40 carte, 28 Unità, 6 Reazioni, 0 Scudo, costo medio 2.33, colori G 14 R 22, massimo copie 2 (in B0c05: costo medio 2.30).
- **Si misura:** IA forte:30, 200 partite per incrocio, celle `1-2,1-4,1-6` (3 incroci, 600 partite, ~2.2 h su 4 core), semi 3400+k; contro — (riferimento delle celle r1: B0c05 senza carte nuove).
- **Comando:** `E031_TRACCIA=$(cat traccia.txt) bash ../lancia_e031.sh R1-2c forte:30 200 3400 1-2,1-4,1-6`.
