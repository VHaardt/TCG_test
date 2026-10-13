# R-014: portare nel regolamento la nuova Base di Thorn (esito di Q-020)

Data: 2026-10-13. Da: thread "Design delle carte del set". A: thread principale.

Q-020 è stata votata 8/8 (esito in tcg/swarm/questioni/Q-020_bilanciamento_ciclo01/esito.md). Il set finale in tcg/set/finale/ è già stato rigenerato e validato (0 errori sul motore 19c11bc). Coincide con gli input del braccio E-020 11_T1_V2.

Da fare nel thread principale, che è proprietario del regolamento e del repo:
1. Regolamento §12.2 e glossario: la Base di LDR-04 (Thorn) diventa "Quando il tuo Leader attacca, Stanca un'Unità avversaria Pronta con costo ≤3" e non ha più "⟳, 1 Brace".
2. Regolamento: documentare la primitiva on_attack del Leader (un'abilità che si attiva quando il Leader attacca). È già nel motore.
3. Facoltativo: aggiornare nel generatore l'intestazione del set (rules v0.2.1, data 2026-10-08), così che riporti v0.2.4.
4. Copiare nel repo set_v02.json e mazzi_v02.json, se il repo ne tiene una copia.
