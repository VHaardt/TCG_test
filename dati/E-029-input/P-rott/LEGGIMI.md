# E-029_c04 / P-rott

- **Cosa cambia rispetto a B0c03:**
  - NEU-013: Forza 3 → 2 (`power`), testo invariato.
  - BLU-008: Forza 2 → 1 (`power`), testo invariato.
  - LDR-05: Base senza testo (`base: []`); Risvegliato invariato.
  - Lista `rif_LDR05_scudi_armati` (rottura del competitivo): −3 NEU-013, −3 BLU-008, +2 ROS-003 (0 → 2), +1 ROS-021 (2 → 3), +1 BLU-012 (2 → 3), +1 BLU-010 (2 → 3), +1 BLU-001 (2 → 3). Le carte nerfate da P escono dalla lista: di P in questa lista conta solo la Base vuota di LDR-05.
- **Proponenti / ruolo:** competitivo (lista di rottura); P si vota solo se anche qui Δ05 ≤ −3 (critico).
- **`rif_LDR05` nel braccio:** 40 carte, 32 Unità, 8 non Unità, 12 copie con Scudo, colori R 21 B 19 N 0; massimo copie per ID 3.
- **Si misura:** IA forte, 200 partite per incrocio, protagonisti `5`, semi 3300+k; contro E-029_c04/00_B0c03 F_s3300 (200 per incrocio).
- **Comando:** `E029_TRACCIA=$(cat traccia.txt) bash ../lancia_e029.sh P-rott forte:30 200 3300 5` (uscita `tcg/swarm/esperimenti/E-029_c04/P-rott/F_s3300`), stima 3.6 h su 4 core.
- **Regole:** `tcg/swarm/cicli/ciclo-04/round1/punti_passata2.md` (punti 1–3, esito della passata 2).
