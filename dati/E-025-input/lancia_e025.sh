#!/usr/bin/env bash
# E-025 (ciclo 02, gruppo b): B0c02 sul set finale e D05b_c02. Come lancia_e024.sh, con la variante P6 = [1,3] e il mix M3.
# Da eseguire dalla radice della repo (dove c'e' sim/). Motore: 934a469 o successivo.
#
#   bash lancia_e025.sh <braccio> <ia> <partite_per_incrocio> <seed_base> <protagonisti|tutti> [mix]
#
#   seed_base     2000 semplice, 3000 forte (stessi indici di coppia di E-020/E-023/E-024)
#   E025_VARIANTE facoltativa: preset o file JSON per --variante (default: variante_V024_P13.json di questa cartella;
#                 quando il thread principale crea il preset nel motore, passarne il nome qui)
#   E025_OUT      facoltativa: cartella risultati (default tcg/swarm/esperimenti/E-025_B0c02)
#   E025_TRACCIA  facoltativa: ID per --traccia
#   mix           se presente: anche mix_M3_thorn_lucchetto contro i 5 rif non-Thorn, seed seed_base+20+o
set -euo pipefail
B=$1; IA=$2; N=$3; SB=$4; PROT=$5; MIX=${6:-}
BASE=/mnt/project-files/tcg/set/esperimenti/E-025_B0c02; SRC=$BASE/$B
VAR=${E025_VARIANTE:-$BASE/variante_V024_P13.json}
OUT=${E025_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-025_B0c02}/$B/$( [ "$IA" = semplice ] && echo S || echo F )
TR=(); [ -n "${E025_TRACCIA:-}" ] && TR=(--traccia "$E025_TRACCIA")
[ -f "$SRC/carte.json" ] || { echo "$B: nessun carte.json"; exit 1; }
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
tocca() { [ "$PROT" = tutti ] && return 0; for p in ${PROT//,/ }; do [ "$p" = "$1" ] || [ "$p" = "$2" ] && return 0; done; return 1; }
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1)); tocca $i $j || continue
  python3 -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
    --mazzi "$SRC/mazzi.json#${DK[$i]}" "$SRC/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$OUT/L$i-L$j" > /dev/null
  echo "$B $IA L$i-L$j seed $((SB+k)) fatto"
done; done
if [ -n "$MIX" ]; then
  for o in 1 2 3 5 6; do
    python3 -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
      --mazzi "$SRC/mazzi.json#${DK[$o]}" "$SRC/mazzi_mix_M3.json#mix_M3_thorn_lucchetto" \
      --partite 0 --incroci "$N" --seed $((SB+20+o)) --ia "$IA" "${TR[@]}" --out "$OUT/M3-L$o" > /dev/null
    echo "$B $IA M3-L$o seed $((SB+20+o)) fatto"
  done
fi
