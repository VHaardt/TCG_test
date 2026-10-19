#!/usr/bin/env bash
# E-027 (ciclo 03, Q-023, i due Leader rossi): bracci 00_B0c03, R20, R21, B5, K-rott, C. Copiato da lancia_e025.sh.
# Da eseguire dalla radice della repo (dove c'e' sim/). Motore: 8e9290a o successivo (preset V026, contatore R-017).
#
#   bash lancia_e027.sh <braccio> <ia> <partite_per_incrocio> <seed_base> <protagonisti|tutti> [mix]
#
#   seed_base     2000 semplice, 3000 forte (stessi indici di coppia di E-020/E-023/E-024/E-025);
#                 3100 = secondo blocco di semi della forte (seed 3101..3115, nessuna sovrapposizione con 3000+k e 3000+20+o).
#                 Ogni seed_base diverso da 2000/3000 scrive in una cartella a parte: <braccio>/F_s3100 (o S_s<seed_base>).
#   E027_VARIANTE facoltativa: preset o file JSON per --variante (default V026)
#   E027_OUT      facoltativa: cartella risultati (default tcg/swarm/esperimenti/E-027_c03)
#   E027_TRACCIA  facoltativa: ID per --traccia (es. LDR-05,ROS-020,ROS-021,ROS-003,LDR-01)
#   mix           se presente: anche mix_M3_thorn_lucchetto (serve mazzi_mix_M3.json nel braccio; i bracci E-027 non lo hanno)
set -euo pipefail
B=$1; IA=$2; N=$3; SB=$4; PROT=$5; MIX=${6:-}
BASE=/mnt/project-files/tcg/set/esperimenti/E-027_c03; SRC=$BASE/$B
VAR=${E027_VARIANTE:-V026}
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=${E027_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-027_c03}/$B/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(); [ -n "${E027_TRACCIA:-}" ] && TR=(--traccia "$E027_TRACCIA")
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
  [ -f "$SRC/mazzi_mix_M3.json" ] || { echo "$B: manca mazzi_mix_M3.json"; exit 1; }
  for o in 1 2 3 5 6; do
    python3 -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
      --mazzi "$SRC/mazzi.json#${DK[$o]}" "$SRC/mazzi_mix_M3.json#mix_M3_thorn_lucchetto" \
      --partite 0 --incroci "$N" --seed $((SB+20+o)) --ia "$IA" "${TR[@]}" --out "$OUT/M3-L$o" > /dev/null
    echo "$B $IA M3-L$o seed $((SB+20+o)) fatto"
  done
fi
