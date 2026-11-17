# E-038-input — combinazione finale del ciclo 05 (voto_lampo.md V2)

Autore: programmatore (swarm), 2026-11-17. Voto: `tcg/swarm/cicli/ciclo-05/voto_lampo.md` (V2, 8/8 con emendamenti). Gli input sono preparati in anticipo: si lancia la combinazione scelta appena chiude E-037.

## Combinazioni
Ci sono 7 cartelle. Sei sono le coppie di bracci H5-x+H6-y, con H5-x in {H5-t, H5-v, H5-r} e H6-y in {H6-v, H6-c}. La settima è **L5ref+H6-v**: LDR-05 resta quello di B0c06 (`set/finale`, senza modifiche) e LDR-06 è quello di H6-v. `genera_e038.py` le produce dai `carte.json` di E-037 (prima va rigenerato E-037):
- LDR-05 viene dal braccio H5-x;
- LDR-06 viene dal braccio H6-y;
- tutto il resto del set (125 carte) e le liste `rif_` di B0c06 (V4) restano invariati. Nessun braccio cambia le liste.

| Leva | LDR-05 / LDR-06 nel JSON |
|---|---|
| H5-t | `"tempra": 3, "tempra_fissa": true`: Tempra 3 per tutta la partita, A non la abbassa. Vale anche senza A |
| H5-v | `"life": 4` |
| H5-r | Base vuota; Risvegliato "Impeto +1 contro un'Unità" |
| H6-v | `"life": 6` e la Base di L6-a (E-036) |
| H6-c | Base "pari o inferiore alle tue Cicatrici" (due abilità ⟳) e Risvegliato "Caccia +2 contro un'Unità" |

## Versioni
| Versione | Regole | Partite per incrocio | Incroci | Semi | Stima su 4 core |
|---|---|---|---|---|---|
| conA | V027 + A (`varianti/tempra_tardo.json`) | 200 | tutti (15) | 3700+k | ~10.8 h |
| senzaA | V027 | 100 | tutti (15) | 3700+k | ~5.4 h |

- La versione con A decide il 42–58 sulla stima puntuale a 200 partite, con il suo IC.
- Le partite 100–199 vanno riportate a parte; se si scostano dalle prime 100 di oltre 2 punti, decidono loro (Esito del voto).
- La versione senza A è il test P1 di A, a bassa potenza (IC del Δ circa ±6).
- Le due versioni usano gli stessi semi, quindi le loro prime 100 partite sono appaiate.

## Lancio
Dalla radice della repo, su un motore con R-032 (612057d o successivo):

    nohup bash dati/E-038-input/lancia_e038.sh <combinazione> conA > /dev/null 2>&1 &
    nohup bash dati/E-038-input/lancia_e038.sh <combinazione> senzaA > /dev/null 2>&1 &

- Argomenti facoltativi: `[ia] [partite] [seed_base]`.
- Uscita: `$E038_OUT/<combinazione>/<conA|senzaA>/F_s3700/Li-Lj/`, di default `tcg/swarm/esperimenti/E-038_combinazione`.
- Come negli esperimenti precedenti, il launcher passa `--riprendi`, salta gli incroci finiti e tiene i record per partita (`partite.pkl`).
- Prima di giocare lancia `valida` e, se non passa, salta la combinazione.

## Verifiche fatte (motore 612057d, branch claude/r032-leader-vita-tempra)
- `valida` dà 0 errori su tutte e 7 le combinazioni, sia con `--variante varianti/tempra_tardo.json` sia con V027 (resta l'avviso delle 43 NC). Sullo stesso motore anche i 5 bracci di E-037 danno 0 errori.
- Partita di prova H5-t+H6-v con A, cella L5-L6, seme 3715:
  - parte con "Vite 5-6", quindi LDR-06 ha 6 Vite;
  - LDR-05 difende a 3 di Tempra senza gemme ("3 contro 3"), quindi H5-t è attivo.
