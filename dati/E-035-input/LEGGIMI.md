# E-035-input — le 4 liste mix_ a 2 copie contro B0c06 (Q-031, ciclo 05 D)

Autore: programmatore (swarm), 2026-11-15. Questione: `tcg/swarm/questioni/Q-031_ciclo05.md`. Liste: `tcg/swarm/cicli/ciclo-05/mix_2copie.md` (playtester competitivo).

## Base
- **Carte:** `carte.json` = `tcg/set/finale/set_v02.json` (125 carte, le stesse di E-034).
- **Liste:** `mazzi.json` = `tcg/set/finale/mazzi_v02.json`. Contiene le 6 liste `rif_` di B0c06, identiche a quelle di E-034, e le 4 `mix_` rifatte a 2 copie nel ciclo 05:
  - `mix_M1_maera_bunker`
  - `mix_M2_vey_blitz`
  - `mix_M3_thorn_lucchetto`
  - `mix_M4_arden_sanguinante`
- **Versioni a 3 copie:** sono in `tcg/set/finale/storico/mazzi_v02_mix_da_rifare.json`.
- **Traccia:** quella di E-034, più le carte delle mix_ che non c'erano: BLU-018, NEW-I06, NER-005, NER-013, VER-017 e NEU-007.
- **Regole:** V027, senza bracci.

## Corsa
| Incroci | IA, partite per incrocio | Semi | Stima su 4 core |
|---|---|---|---|
| 24: ogni mix_ contro le 6 rif_ (M1-L1 … M4-L6) | forte:30, 200 | 3600+k, k = 6·(m−1) + l (M1-L1 → 1 … M4-L6 → 24) | ~17.3 h (4.800 partite) |

Lancio: **in coda dopo E-034**. Va eseguito dalla radice della repo, su main 7ec6380 o successivo:

    nohup bash dati/E-035-input/lancia_e035.sh > /dev/null 2>&1 &

- **Argomenti facoltativi:** `ia`, `partite`, `seed_base` e `celle`. Per `celle` si può scrivere `tutti`, `p:M3,L5` oppure `M1-L2,M3-L5`.
- **Ripresa:** il launcher passa `--riprendi` e salta gli incroci già finiti.
- **Uscite:** vanno in `tcg/swarm/esperimenti/E-035_mix/F_s3600/Mm-Ll/`, con il registro in `avanzamento.log`. `E035_OUT` cambia la cartella.
- **Record per partita:** si tengono come in E-034. In ogni cella resta `partite.pkl`, un collegamento fisso al checkpoint `.partite_fatte.pkl`, che `run.py` cancella a fine cella.

## Da leggere
- Per ogni mix_: le vittorie contro le 6 rif_, la media e il confronto con la rif_ dello stesso Leader in E-034 00_B0c06. Le previsioni del competitivo sono in `mix_2copie.md`: M1 44, M2 47, M3 51, M4 52.
- **Allarmi del competitivo:**
  - M3 sopra il 55%;
  - M2 con più dell'1% di vittorie entro il R5.
- **Contatori:** le stesse tabelle del report di E-034, cioè R-028 ritmo, R-026 interattività, R-027 P9b, Scudo, R-017 e M5. Per M2 si aggiungono le vittorie entro il R7 e R9-5.

## Verifiche fatte (main 8ff53fc)
- `valida --variante V027` su `carte.json` e su tutte le 10 liste di `mazzi.json`: 0 errori. Resta l'avviso noto delle 43 carte con rarità NC.
- Prova con il launcher su M2-L1 (seme 3607) e M3-L5 (seme 3617), 2 partite ciascuno, forte:30:
  - le partite finiscono senza errori;
  - i posti si alternano: in g = 0 la mix_ è G1;
  - `partite.pkl` contiene i 2 record.
- Questa prova non è la corsa.
