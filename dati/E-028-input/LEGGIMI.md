# E-028_c04: braccio dichiarato R21 + B5 (Q-024, parte A)

Data: 2026-10-22. Preparati dal programmatore dello swarm. Sono solo dati, rigenerabili con `python3 -B genera_e028.py`.

**Base (B0c03).** È `tcg/set/esperimenti/E-025_B0c02/A-FV_c02/`, la stessa di E-027_c03, e resta intatta.

| Braccio | Cosa cambia rispetto a B0c03 | Ruolo |
|---|---|---|
| `00_B0c03` | nulla. È identica a `E-027_c03/00_B0c03` | riferimento, da rigiocare sui semi 3200+k |
| `RB` | due modifiche: ROS-021 da "Impeto 1: +3" a "Impeto 2: +3" (`abilities[0].if = [{"pugno_ge": 2}]`, `text`, `_note`), e Base di LDR-05 con `base[0].if = [{"pugno_ge": 2}]` e il nuovo `text` | braccio dichiarato, deciso prima dei dati |

Le liste sono quelle di B0c03, invariate: 6 `rif_*` da 40 carte. ROS-021 è in `rif_LDR01` (×2) e in `rif_LDR05` (×2), quindi RB tocca entrambi i Rossi.

**Diff campo per campo** (esclusi solo i metadati `version`, `note`, `set`, `autore`, `data`, `nota`):
- `00_B0c03` contro B0c03: nessuna differenza; mazzi uguali.
- `RB` contro B0c03: differisce solo in `cards[ROS-021]._note`, `cards[ROS-021].abilities`, `cards[ROS-021].text` e `leaders[LDR-05].base`; mazzi uguali.
- `RB` contro l'unione di `E-027_c03/R21` e `E-027_c03/B5`: identico.

**Validazione.** Motore **4e13d90**, l'ultimo commit di `claude/regolamento-v0.1`, successivo a 8e9290a, con preset V026.
- `valida`: 120 carte, 6 Leader, 0 errori per entrambi i bracci.
- Partita di fumo LDR-01 contro LDR-05 con V026: exit 0 sui seed 1, 2 e 3. Sul seed 3 la differenza è proprio il +1 della Base, che con 1 gemma non scatta più (Forza 5 contro 3 diventa 4 contro 3). Sul seed 2 la partita è identica, perché nessuna delle due leve entra in gioco.
- Lanciatore: `RB semplice 2 3200 5` produce 5 incroci (seed 3204–3215) in `S_s3200`.

**Il commit c16fca3 non va usato come motore.** Sta sul branch dati `dati/e020-v024-forte`, e il suo `sim/` è fermo a una versione vecchia (antenato 6d6f3a0, senza V026 e senza R-017).

**Lancio** (Q-024 §A: IA forte, 200 partite per incrocio, protagonisti 1 e 5, semi nuovi 3200+k, i due bracci appaiati sugli stessi semi):

```bash
E028_TRACCIA=LDR-01,LDR-05,ROS-021,ROS-020,ROS-015,ROS-023 bash /mnt/project-files/tcg/set/esperimenti/E-028_c04/lancia_e028.sh 00_B0c03 forte:30 200 3200 1,5
E028_TRACCIA=LDR-01,LDR-05,ROS-021,ROS-020,ROS-015,ROS-023 bash /mnt/project-files/tcg/set/esperimenti/E-028_c04/lancia_e028.sh RB       forte:30 200 3200 1,5
```

I risultati vanno in `tcg/swarm/esperimenti/E-028_c04/<braccio>/F_s3200/L<i>-L<j>/`. Il default del lanciatore è V026; si può cambiare con `E028_VARIANTE` e `E028_OUT`. Ogni comando gioca 9 incroci, cioè 1.800 partite.

---

## Parte B: diagnosi della ridondanza R/B (`tcg/swarm/cicli/ciclo-04/piano.md` §3)

Questi bracci sono diagnostici e non leve: non si votano.

**Copie diagnostiche `D-<ID>`.** Per ROS-020, ROS-021, ROS-015 e ROS-023:
- costo, Forza, colore, tipo e rarità restano quelli dell'originale;
- tolte la parola chiave `impeto`, la sua abilità e il testo dell'Impeto (D-ROS-023 tiene Assalto);
- le copie sono usate **solo in `rif_LDR05`**, al posto degli originali;
- gli originali restano nel set e nelle altre liste (`rif_LDR01` ha ROS-015 ×3, ROS-021 ×2 e ROS-023 ×1), quindi conta solo il protagonista 5.

Senza Impeto le copie perdono anche il +1 del Risvegliato di LDR-05, che vale per le Unità con Impeto: anche questo fa parte della capacità tolta.

| Braccio | In `rif_LDR05` | Domanda |
|---|---|---|
| `DT` | ROS-020 ×3, ROS-021 ×2, ROS-015 ×3, ROS-023 ×1 → D-* | tetto: quanto vale l'intera ridondanza |
| `D20-21` | ROS-020, ROS-021 → D-* | quanto vale ROS-015 (con ROS-023) da sola |
| `D20-15` | ROS-020, ROS-015 → D-* | quanto vale ROS-021 da sola |
| `D21-15` | ROS-021, ROS-015 → D-* | quanto vale ROS-020 da sola |
| `D20`, `D21`, `D15` (condizionali) | una fonte alla volta | solo se la lettura delle coppie resta ambigua |

**Diff.** Rispetto a B0c03 nessuna carta esistente cambia e i Leader sono identici. Ogni braccio aggiunge solo le sue carte `D-*`. Nei mazzi cambia solo `rif_LDR05`, dove gli originali sono sostituiti dalle copie con le stesse quantità; le altre 5 liste restano identiche. Tutte le liste hanno 40 carte, e i file della parte A (00_B0c03, RB) sono rimasti identici byte per byte dopo la rigenerazione.

**Validazione.** Motore 4e13d90, V026.
- `valida`: 0 errori su tutti i bracci (121–124 carte, perché ci sono le copie D-*, e 6 Leader).
- Partita di fumo LDR-01 contro LDR-05, seed 3: exit 0 su tutti i bracci. Le carte D-* compaiono nel log, tranne in D21, dove in quella partita D-ROS-021 non esce.
- Lanciatore: `DT semplice 2 3300 5` scrive 5 incroci in `S_s3300`, e la traccia mostra le carte D-* giocate da LDR-05.

**Lancio** (IA forte, 100 partite per incrocio, protagonista 5, semi 3300+k; prima il riferimento sugli stessi semi). La traccia è quella del ciclo 03 più le carte D-*:

```bash
TR=LDR-01,LDR-05,BLU-001,BLU-007,BLU-008,BLU-010,BLU-012,BLU-015,BLU-021,BLU-023,BLU-025,NEU-006,NEU-013,ROS-001,ROS-003,ROS-005,ROS-007,ROS-010,ROS-015,ROS-016,ROS-018,ROS-020,ROS-021,ROS-023,ROS-025,VER-001,VER-002,VER-009,VER-011,VER-019,VER-024,D-ROS-020,D-ROS-021,D-ROS-015,D-ROS-023
E028_TRACCIA=$TR bash /mnt/project-files/tcg/set/esperimenti/E-028_c04/lancia_e028.sh 00_B0c03 forte:30 100 3300 5
for b in DT D20-21 D20-15 D21-15; do E028_TRACCIA=$TR bash /mnt/project-files/tcg/set/esperimenti/E-028_c04/lancia_e028.sh $b forte:30 100 3300 5; done
# condizionali, solo se servono: D20 D21 D15, stessi argomenti
# TR = traccia del ciclo 03 (LDR-01, LDR-05, le 29 carte distinte di rif_LDR01 e rif_LDR05) più le 4 copie D-*
```

Ogni comando gioca 5 incroci, cioè 500 partite. I risultati vanno in `tcg/swarm/esperimenti/E-028_c04/<braccio>/F_s3300/`. Includere nella traccia un ID D-* che in un braccio non esiste è innocuo: la colonna risulta a 0.
