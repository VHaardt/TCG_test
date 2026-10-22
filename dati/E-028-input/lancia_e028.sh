#!/usr/bin/env bash
# E-028 (ciclo 04, Q-024): parte A 00_B0c03 e RB (R21 + B5); parte B diagnostici DT, D20-21, D20-15, D21-15, D20, D21, D15.
# Copiato da lancia_e027.sh.
# Da eseguire dalla radice della repo (dove c'e' sim/). Motore: 8e9290a o successivo, validato su 4e13d90 (preset V026, contatore R-017).
#
#   bash lancia_e028.sh <braccio> <ia> <partite_per_incrocio> <seed_base> <protagonisti|tutti> [mix]
#
#   seed_base     2000 semplice, 3000 forte (stessi indici di coppia di E-020/E-023/E-024/E-025);
#                 3200 = semi nuovi di Q-024 parte A (seed 3201..3215, mai usati per selezionare RB): scrive in <braccio>/F_s3200.
#                 3300 = semi della parte B (seed 3301..3315): scrive in <braccio>/F_s3300.
#                 Ogni seed_base diverso da 2000/3000 scrive in una cartella a parte: <braccio>/F_s<seed_base> (o S_s<seed_base>).
#   E028_VARIANTE facoltativa: preset o file JSON per --variante (default V026)
#   E028_OUT      facoltativa: cartella risultati (default tcg/swarm/esperimenti/E-028_c04)
#   E028_TRACCIA  facoltativa: ID per --traccia (anche le copie diagnostiche D-ROS-*) (es. LDR-05,ROS-020,ROS-021,ROS-003,LDR-01)
#   mix           se presente: anche mix_M3_thorn_lucchetto (serve mazzi_mix_M3.json nel braccio; i bracci E-028 non lo hanno)
set -euo pipefail
B=$1; IA=$2; N=$3; SB=$4; PROT=$5; MIX=${6:-}
BASE=/mnt/project-files/tcg/set/esperimenti/E-028_c04; SRC=$BASE/$B
VAR=${E028_VARIANTE:-V026}
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=${E028_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-028_c04}/$B/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(); [ -n "${E028_TRACCIA:-}" ] && TR=(--traccia "$E028_TRACCIA")
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
