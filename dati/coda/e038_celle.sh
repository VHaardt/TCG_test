#!/usr/bin/env bash
# E-038: gioca solo le celle indicate di una combinazione, con gli stessi argomenti di lancia_e038.sh (seme 3700+k, traccia, --riprendi, record).
# Serve a dividere E-038 fra più container. Le 6 celle senza L5 e L6 (L1-L2 L1-L3 L1-L4 L2-L3 L2-L4 L3-L4) sono identiche in tutte
# le combinazioni (carte.json e mazzi.json cambiano solo in LDR-05/LDR-06), quindi si giocano una volta sola con combinazione "comune".
# Uso, dalla radice della repo su 612057d:  E038_IN=<.../dati/E-038-input> E038_OUT=<dir> bash e038_celle.sh <combinazione|comune> <conA|senzaA> <cella>...
set -euo pipefail
D=${E038_IN:?cartella dati/E-038-input}; C=$1; V=$2; shift 2
SRC=$D/$C; [ "$C" = comune ] && SRC=$D/H5-r+H6-c
case "$V" in conA) VAR=$D/varianti/tempra_tardo.json; N=200 ;; senzaA) VAR=V027; N=100 ;; *) exit 1 ;; esac
OUTB=${E038_OUT:?uscita}; LOG=$OUTB/avanzamento.log; mkdir -p "$OUTB"
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
kof() { local k=0; for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do k=$((k+1)); [ "L$i-L$j" = "$1" ] && { echo "$k $i $j"; return; }; done; done; }
for cella in "$@"; do
  read k i j < <(kof "$cella")
  O=$OUTB/$C/$V/F_s3700/$cella
  if ls "$O"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$O/.partite_fatte.pkl" ]; then echo "$C $V $cella gia' fatto, salto" >> "$LOG"; continue; fi
  mkdir -p "$O"; [ -f "$O/.partite_fatte.pkl" ] || : > "$O/.partite_fatte.pkl"
  [ "$O/.partite_fatte.pkl" -ef "$O/partite.pkl" ] || ln -f "$O/.partite_fatte.pkl" "$O/partite.pkl"
  python3 -B -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" --mazzi "$SRC/mazzi.json#${DK[$i]}" "$SRC/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((3700+k)) --ia forte:30 --traccia "$(cat "$D/traccia.txt")" --riprendi --out "$O" > /dev/null
  echo "$(date -u +%FT%TZ) $C $V $cella seed $((3700+k)) fatto" >> "$LOG"
done
echo "$(date -u +%FT%TZ) fine celle $C $V $*" >> "$LOG"
