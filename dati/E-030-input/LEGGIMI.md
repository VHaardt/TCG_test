# E-030_q026 — input di Q-026 (B0c05, M2, M3, R5-2c, M1, P-2c)

Autore: programmatore (swarm), 2026-10-26. Esito dei voti: `tcg/swarm/questioni/Q-026_feedback_playtest/esito_passata2.md`.

- **Carte:** B0c03 (`E-025_B0c02/A-FV_c02/carte.json`, identica a `E-028_c04/00_B0c03`).
- **Liste:** B0c05 (`questioni/Q-026_feedback_playtest/liste_B0c05/mazzi.json`, del playtester competitivo). Contengono già le correzioni del critico (`liste_B0c05/verifica_critico.md`): in L4 −VER-012 +NEU-011, in L6 −VER-009 +NEU-012. Se le liste cambiano ancora, rilanciare `python3 -B genera_e030.py` e rivalidare. Se una carta tolta da M2 o M3 non c'è più, il generatore si ferma con un errore; in quel caso si riguarda la scelta.
- **Generatore:** `genera_e030.py`. Solo dati, nessuna regola nel codice.
- **Lanciatori:**
  - `lancia_e030.sh` lancia un braccio (`--riprendi`, salta gli incroci finiti);
  - `esegui_e030.sh` esegue tutta la corsa in sequenza.
- **Motore:** ab6f2dd o successivo (R-025: costi `stanca_own`/`any` per M1, contatori M5 nel report; i replay V026 sono identici a 4e13d90), variante V026. Tutti i bracci passano `valida --variante V027` (avviso: 43 carte di B0c03 con rarità NC, fuori dalla scala C/R/E/L).

| Braccio | Cosa cambia rispetto a B0c05 | IA, partite per incrocio | Protagonisti (incroci) | Semi | Stima su 4 core |
|---|---|---|---|---|---|
| 00_B0c05 | nulla (riferimento) | forte:30, 200 | tutti (15) | 3400+k | ~10.8 h |
| 00_B0c05 | nulla (riferimento) | semplice, 400 | tutti (15) | 2000+k | ~0.2 h |
| M2 | + NEW-V05 ×2 in L4 (−NEU-011, −VER-002), L6 (−2 VER-013) e L1 (−2 VER-013) | forte:30, 200 | 1,4,6 (12) | 3400+k | ~8.7 h |
| M3 | + NEW-B06 ×1 in L6 (−VER-023) | forte:30, 200 | 6 (5) | 3400+k | ~3.6 h |
| R5-2c | `rif_LDR05` sostituita da `rott_LDR05_2c` del critico (`verifica_critico.md`): +2 NEU-001, +2 ROS-008, +2 ROS-003, +1 BLU-003; −2 BLU-004, −1 ROS-004, −1 ROS-006, −1 NEU-009, −1 ROS-014, −1 ROS-019 | forte:30, 200 | 5 (5) | 3400+k | ~3.6 h |
| M1 | NER-002 e NER-019 con costo "perdi 1 Vita (floor 1) **oppure** Stanca una tua Unità Pronta" (`any`); in L6 −NEU-004, −VER-010, −VER-021, +2 NER-002, +1 NER-019 | forte:30, 200 | 3,6 (9) | 3400+k | ~6.5 h |
| P-2c | leve di P (NEU-013 F2, BLU-008 F1, LDR-05 senza Base) | forte:30, 200 | 1,5 (9) | 3400+k | ~6.5 h (si lancia: lo screening di E-029 dà Δ05 −2.5; `E030_P2C=0` lo esclude) |

Totale: circa 39.9 h (17.000 partite), circa 33.4 h senza P-2c (13 s a partita con forte:30 sulla macchina intera).

**Traccia.** È la stessa per tutti i bracci (`traccia.txt` in ogni cartella). Comprende:
- la traccia di E-029;
- i 6 Leader;
- VER-012, VER-013 e VER-023;
- le carte entrate nelle liste in B0c05 e in `rott_LDR05_2c`;
- NER-002, NER-019, NEU-004 e VER-021 (M1);
- NEW-V05 e NEW-B06.

**Contatori.** Il motore 4e13d90 riporta "Colpi del Leader senza gemme con Rimarginare legale" per Leader e lato (Q-017). L'uso di Rimarginare (`rim_used`) viene contato in ogni partita, ma non compare nel report. Con il motore ab6f2dd il report ha anche i contatori di M5 (Rimarginare e costi in Vita per round, costo scelto per carta).

**Rarità.** NEW-V05 è R e NEW-B06 è L, come da voto. Le altre carte hanno la scala di B0c03 (C, NC, R): la tabella dell'editor non è ancora applicata. La rarità è un campo descrittivo e non cambia le partite. Le copie per nome, la Leggendaria in 1 copia e la regola multicolore sono controllate da `valida --variante V027`: tutte le liste di tutti i bracci passano.
