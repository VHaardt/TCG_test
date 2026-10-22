# E-028_c04 / D21 (parte B, diagnostico)

- **Cosa cambia rispetto a B0c03:**
  - Solo `rif_LDR05`: ROS-021 ×2 → D-ROS-021 (F5, c5, nessuna parola chiave). Gli originali restano nel set e nelle altre liste (ROS-015, ROS-021 e ROS-023 in `rif_LDR01`). Senza la parola chiave Impeto le copie non ricevono nemmeno il +1 del Risvegliato di LDR-05 (che vale per le Unità con Impeto): è parte della capacità tolta.
- **Domanda:** condizionale: ROS-021 con le altre presenti.
- **Ruolo:** diagnostico della parte B (condizionale: ROS-021 con le altre presenti); non è una leva e non si vota.
- **Si misura:** IA forte, 100 partite per incrocio, protagonista 5, semi 3300+k, contro `00_B0c03` sugli stessi semi: `E028_TRACCIA=<traccia ciclo 03>,LDR-01,LDR-05,D-ROS-021,ROS-020,ROS-015,ROS-023 bash ../lancia_e028.sh D21 forte:30 100 3300 5` (uscita `F_s3300`).
- **Lettura:** `tcg/swarm/cicli/ciclo-04/piano.md` §3 (nessuna regola d'uscita).
