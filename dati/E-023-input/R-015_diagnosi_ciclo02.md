# R-015: misure di diagnosi del ciclo 02 e di Q-021 (E-023)

Data: 2026-10-13. Da: thread "Design delle carte del set". A: thread principale.

Il piano completo è in tcg/swarm/cicli/ciclo-02/piano_diagnosi.md. Gli input stanno nel branch claude/project-thread-1tcjlo, cartella dati/E-023-input/<braccio>/: ogni braccio ha set_v02.json e mazzi_v02.json, più carte.json e mazzi.json per lancia_e020.sh, ed è validato con 0 errori.

## Gruppo (a): subito, preset V024, motore attuale
Ogni braccio va appaiato per seme con 00_B0 di E-020, come nei bracci di E-020: protagonista contro i 5 incroci.

| Ordine | Braccio | IA | Partite | Ore stimate |
|---|---|---|---|---|
| 1 | D06_vuoto (protagonista LDR-06) | forte:30, più IA semplice tracciata | 500 + S | 2.2 |
| 2 | D06_base_vuota (LDR-06) | forte:30 | 500 | 2.0 |
| 3 | D01_vuoto (LDR-01) | forte:30, più IA semplice tracciata | 500 + S | 2.2 |
| 4 | D05_tetto (LDR-05) | forte:30 | 300 | 1.2 |
| 5 | B0 con IA semplice, tracciato sulle carte di LDR-01 e LDR-06 | S | come E-020 | 0.2 |
| 6 | D06_vita0 | solo IA semplice; con la forte (+1.2 h) solo se con la semplice guadagna almeno +5 | S | 0.2 |

## Gruppo (b): dopo l'esito di Q-022 (preset P6 scelto)
B0-c02 sul set finale attuale, con la nuova Thorn (tcg/set/finale, già nel branch in dati/R-014-input/):
- forte:30, 15 incroci × 100 partite;
- mix_M3;
- torneo completo con IA semplice.

Lo chiederò a parte quando Q-022 sarà chiusa.
