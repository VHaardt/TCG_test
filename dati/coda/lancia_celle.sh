#!/usr/bin/env bash
# Un braccio, per celle, con --riprendi; salta gli incroci finiti. Da eseguire dalla radice di una copia del simulatore.
#   bash lancia_celle.sh <input: cartella con carte.json, mazzi.json, traccia.txt> <variante> <uscita F_s...> <ia> <partite> <seed_base> <celle>
# celle: tutti | p:2,4 | 2-5,4-5 | -1-3,1-6,3-6 (tutti tranne questi). Seme dell'incrocio = seed_base+k, k = indice della coppia (1-2 → 1 … 5-6 → 15).
set -euo pipefail
SRC=$1; VAR=$2; OUT=$3; IA=$4; N=$5; SB=$6; CELLE=$7
TR=(--riprendi); [ -f "$SRC/traccia.txt" ] && TR+=(--traccia "$(cat "$SRC/traccia.txt")")
fatto() { ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
tocca() {
  case "$CELLE" in
    tutti) return 0 ;;
    p:*) for p in $(echo "${CELLE#p:}" | tr ',' ' '); do [ "$p" = "$1" ] || [ "$p" = "$2" ] && return 0; done; return 1 ;;
    -*) for c in $(echo "${CELLE#-}" | tr ',' ' '); do [ "$c" = "$1-$2" ] && return 1; done; return 0 ;;
    *) for c in $(echo "$CELLE" | tr ',' ' '); do [ "$c" = "$1-$2" ] && return 0; done; return 1 ;;
  esac
}
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1)); tocca $i $j || continue
  if fatto "$OUT/L$i-L$j"; then echo "L$i-L$j gia' fatto, salto"; continue; fi
  python3 -B -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
    --mazzi "$SRC/mazzi.json#${DK[$i]}" "$SRC/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$OUT/L$i-L$j" > /dev/null
  echo "$(date -u +%FT%TZ) L$i-L$j seed $((SB+k)) fatto"
done; done
