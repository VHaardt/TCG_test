# Rilascio di CICATRICI 1.0 (2026-11-18)

La 1.0 congela le regole di v0.2.12 e il set del ciclo 05. Roadmap e criteri: `/mnt/project-files/tcg/roadmap_v1.md`; report finale: `/mnt/project-files/tcg/rilascio_v1/report_finale.md`.

## Cosa contiene la 1.0
| Parte | Dove |
|---|---|
| Regolamento | `docs/regolamento_v1.0.md` (copia in `tcg/regolamento_v1.0.md`) |
| Regolamento illustrato 2.0 | `docs/manuale/` → `build/`, copia in `tcg/regolamento_illustrato/` |
| Regole del simulatore | preset `V10` in `sim/v02/config.py` (= `V0212` con il limite tecnico a 18 round), default del runner e dell'app; `rilascio/regole_v1.0.json` |
| Set e mazzi | `tcg/set/v1.0/` (`set_v1.0.json`, `mazzi_v1.0.json`, `nomi_v1.0.json`, `regole_v1.0.json`, `valida.txt`, `SHA256SUMS`) |
| App | `app/dati` = set del ciclo 05; regole `V10` |

## File di questa cartella
| File | A cosa serve |
|---|---|
| `regole_v1.0.json` | regole della 1.0 come variante del simulatore (`{"base": "V10"}`) |
| `congela_v1.sh` | rifà la copia congelata: da `tcg/set/finale/` a `tcg/set/v1.0/`, rarità del set allineate alla scala C/R/E/L di Q-026 (69 etichette, nessun numero), `valida`, `SHA256SUMS`, `app/dati` |

## Dopo la 1.0
- Ogni cambio di regole o carte è una versione 1.1: si lavora su `tcg/set/finale/` e su un preset nuovo, mai su `set/v1.0/` né su `V10`.
- App pubblicata: nuovo deploy su Render dal blueprint di main (account di Vittorio).
