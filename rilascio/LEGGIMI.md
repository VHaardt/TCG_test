# Pacchetto di rilascio di CICATRICI 1.0

Tutto quello che serve per chiudere la 1.0 appena il ciclo 05 (Q-031) ha l'esito. Roadmap e criteri: `/mnt/project-files/tcg/roadmap_v1.md`. Nessun file qui cambia regole o carte: le decisioni restano dello swarm e di Vittorio.

## File
| File | A cosa serve |
|---|---|
| `regole_v1_con_A.json` | regole della 1.0 se Tempra 3 dal round 10 entra (V027 + `tempra_tardo` 10) |
| `regole_v1_senza_A.json` | regole della 1.0 se resta fuori (V027) |
| `congela_v1.sh con_A\|senza_A` | copia set, mazzi e nomi da `tcg/set/finale/` in `tcg/set/v1.0/`, allinea le rarità del set alla scala C/R/E/L di Q-026 (69 etichette, nessun numero; l'unica Leggendaria è la stessa), lancia `valida` con le regole scelte, scrive `SHA256SUMS` e aggiorna `app/dati` |

Provato il 2026-11-17 su una copia del set di oggi: 125 carte, 6 Leader, 0 errori, nessun avviso di rarità.

## Procedura del freeze (in ordine)
Presupposti: ciclo 05 chiuso con il voto finale; il ciclo 06 solo se la regola di arresto lo chiede (roadmap §3); modifiche di carte e liste già scritte in `tcg/set/finale/` dal thread del set.

1. **Set.** `sh rilascio/congela_v1.sh con_A` (o `senza_A`). Controllare che `valida.txt` dica 0 errori.
2. **Simulatore.** In `sim/v02/config.py` aggiungere il preset `V10` = V027 (+ `"tempra_tardo": 10` se A entra) e renderlo il default del runner e dell'app. Il regolamento illustrato legge i numeri da lì.
3. **Regolamento testuale** (`docs/regolamento_v0.2.md` → `docs/regolamento_v1.0.md`, copia in `tcg/regolamento_v1.0.md`):
   - intestazione: versione 1.0, data, stato "congelato";
   - se A entra: Tempra "4 (3 dal round 10)" nel §2 (valori dei Leader), §9 (Risveglio), §10 (attacco del Leader), §13 (carte d'esempio), §16 (tabella dei parametri), glossario;
   - testi delle Basi di LDR-05 e LDR-06 se il ciclo 05 li cambia (§12.2);
   - §17: titolo "Storia delle varianti" (non più "aperte"), le code dei test (§17.5–§17.8) spostate nella lista "dopo la 1.0";
   - se un Leader resta fuori 45–55 ma dentro 42–58: una riga nel §16 "da ribilanciare in 1.1", con il suo valore e l'IC;
   - registro modifiche: riga 1.0.
4. **Regolamento illustrato** (`docs/manuale/manuale.md`): `basato_su: 1.0`, `preset: V10`, versione del manuale 2.0; rigenerare con `python3 tools/manuale/build.py --pdf --copia /mnt/project-files/tcg/regolamento_illustrato`.
5. **Torneo di controllo** sulle liste congelate (IA forte, 15 incroci × 200, semi nuovi). Se il voto finale del ciclo 05 è già stato preso su queste liste esatte, quella misura vale come controllo e il torneo si salta.
6. **Report di una pagina a Vittorio** con la tabella dei criteri C1–C11 compilata (bozza: `tcg/rilascio_v1/report_vittorio_bozza.md`).
7. **Dopo il sì di Vittorio:** merge della PR del rilascio, tag `v1.0` su main, nuovo deploy su Render (account di Vittorio), riga "1.0" in `swarm/changelog.md`, `indice.md` e memoria del progetto.
