#!/usr/bin/env bash
# E-033: porta 00_rif e tempra_tardo a 200 partite per incrocio (richiesta del thread delle carte, 2026-11-11).
# Le partite 0..99 vengono dai record tenuti (semi_keep) e restano quelle; si giocano solo le 100..199, stessi semi 3400+k.
# Motore: tcg_main 636e83e, lo stesso delle prime 100. Uscita: dati/E-033/<braccio>-200/F_s3400/Li-Lj.
set -euo pipefail
RES=/home/claude/e020_res; IN=/home/claude/e033_in; KEEP=/home/claude/semi_keep/E-033
B=$1; VAR=V027; [ "$B" != 00_rif ] && VAR=$IN/varianti/$B.json
OUT=$RES/dati/E-033/$B-200/F_s3400
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
cd /home/claude/tcg_main
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1)); O=$OUT/L$i-L$j
  if ls $O/*_torneo_*.md > /dev/null 2>&1 && [ ! -f $O/.partite_fatte.pkl ]; then echo "$B-200 L$i-L$j gia' fatto, salto"; continue; fi
  mkdir -p $O
  if [ ! -f $O/.partite_fatte.pkl ]; then
    [ -f $KEEP/$B/F_s3400/L$i-L$j/partite.pkl ] || { echo "ERRORE $B-200: mancano i record di L$i-L$j"; exit 1; }
    cp $KEEP/$B/F_s3400/L$i-L$j/partite.pkl $O/.partite_fatte.pkl
  fi
  python3 -B -m sim.v02.run torneo --variante "$VAR" --carte "$IN/carte.json" \
    --mazzi "$IN/mazzi.json#${DK[$i]}" "$IN/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci 200 --seed $((3400+k)) --ia forte:30 --traccia "$(cat $IN/traccia.txt)" --riprendi --out $O > /dev/null
  echo "$(date -u +%FT%TZ) $B-200 L$i-L$j seed $((3400+k)) fatto"
done; done
