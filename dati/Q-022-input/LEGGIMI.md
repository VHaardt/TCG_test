# Q-022: richiesta al thread del simulatore (forte su tutta la partita)

Motore: questo branch, commit b977e9b o successivo (aggiunge le righe di stallo di Q-022 e corregge la perdita dei dati R13–14 al primo Crepuscolo; nessuna regola cambia per V024).
Set in vigore (Thorn T1 + V2 da Q-020): `set_v02.json`, mazzi `mazzi_v02.json`, i 6 `rif_LDR0*`.

Bracci, IA `forte:30` su tutta la partita, solo mirror, 100 partite per mazzo (600 mirror), seed 22 uguale per i due bracci (appaiati):
1. `V024`
2. `spec_P13.json` (V024 con P6 [1,3], `scintilla_extra_rounds` [])

Esempio:
python3 -m sim.v02.run torneo --variante V024 --ia forte:30 --partite 100 --incroci 0 --seed 22 --carte dati/Q-022-input/set_v02.json --mazzi dati/Q-022-input/mazzi_v02.json#rif_LDR01_puntata_e_preda ... (i 6 rif) --out <cartella>

Risultati: report .md su `dati/e020-v024-forte`, cartella `dati/Q-022/`.
