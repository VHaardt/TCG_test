# Q-028: partite commentate (programmatore)

Quattro partite con l'IA forte (forte:30) su entrambi i lati, preset V027, motore main ad77242, carte B0c03, liste B0c05 corrette dal critico. Il protagonista è sempre P1.

| File | Partita | Seme | Esito |
|---|---|---|---|
| `P1_L5-L4.md` | rif_LDR05 contro rif_LDR04 | 3701 | vince L5 al round 9, Vite 4-0 |
| `P2_L1-L6.md` | rif_LDR01 contro rif_LDR06 | 3702 | vince L1 al round 12, Vite 1-0 |
| `P3_L2-L3.md` | rif_LDR02 contro rif_LDR03 | 3703 | vince L2 al round 11, Vite 2-0 |
| `P4_L4-L6.md` | rif_LDR04 contro rif_LDR06 | 3704 | vince L4 al round 10, Vite 3-0 |

**Log grezzi:** sono in `log/`, prodotti da `script/partita_annotata.py`. Sono identici riga per riga a quelli di `sim.v02.run partita` con gli stessi argomenti (verificato con diff), più una riga `[opzioni]` alla fine di ogni turno. Quella riga dice, alla prima scelta del turno:
- quante azioni legali c'erano: G carte giocabili, A attacchi, R Rimarginare, ⟳ abilità; «fine» è sempre compresa;
- la mano e le gemme;
- quante scelte sono state fatte nel turno.

**Come leggere il log:**
- `pugni: attaccante a, difensore d -> X contro Y` vuol dire che l'attaccante ha messo a gemme e il difensore d.
- Contro il Leader serve X ≥ 4 (Tempra 4), e il pareggio colpisce.
- Una riga "Stancata" subito prima di "attacca con Leader LDR-04" è la Base di Thorn: quando il suo Leader attacca, Stanca.

**Limite:** l'IA forte gioca entrambi i lati. "Opzioni sensate" è il mio giudizio sulle azioni legali della riga `[opzioni]`. Le scelte di gemme, opposizioni e Reazioni non sono contate lì.
