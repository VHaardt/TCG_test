#!/usr/bin/env bash
# E-024 (ciclo 02): come lancia_e020.sh, con le cartelle di E-024 e il mazzo di rottura M6 di LDR-06.
# Da eseguire dalla radice della repo (dove c'e' sim/). Motore: 934a469 o successivo. Preset: V024 (default del motore).
#
#   bash lancia_e024.sh <braccio> <ia> <partite_per_incrocio> <seed_base> <protagonisti|tutti> [mix]
#
#   braccio      cartella in tcg/set/esperimenti/E-024 (es. A-FV)
#   seed_base    2000 per la semplice, 3000 per la forte: gli stessi di E-023/00_B0, partite appaiate
#   protagonisti "tutti", oppure lista di Leader, es. "6" o "1,5"; "nessuno" = solo mix
#   E024_OUT     facoltativa: cartella dei risultati al posto di tcg/swarm/esperimenti/E-024
#   E024_TRACCIA facoltativa: ID passati a --traccia
#   E024_NMIX    facoltativa: partite per incrocio del mix (default = partite_per_incrocio)
#   mix          se presente: anche mix_M6_lucchetto_caccia (LDR-06) contro i 5 rif non-LDR-06, seed seed_base+20+o
set -euo pipefail
B=$1; IA=$2; N=$3; SB=$4; PROT=$5; MIX=${6:-}
SRC=/mnt/project-files/tcg/set/esperimenti/E-024/$B
OUT=${E024_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-024}/$B/$( [ "$IA" = semplice ] && echo S || echo F )
TR=(); [ -n "${E024_TRACCIA:-}" ] && TR=(--traccia "$E024_TRACCIA")
NM=${E024_NMIX:-$N}
[ -f "$SRC/carte.json" ] || { echo "$B: nessun carte.json"; exit 1; }
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
tocca() { [ "$PROT" = tutti ] && return 0; for p in ${PROT//,/ }; do [ "$p" = "$1" ] || [ "$p" = "$2" ] && return 0; done; return 1; }
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1)); tocca $i $j || continue
  python3 -m sim.v02.run torneo --carte "$SRC/carte.json" \
    --mazzi "$SRC/mazzi.json#${DK[$i]}" "$SRC/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$OUT/L$i-L$j" > /dev/null
  echo "$B $IA L$i-L$j seed $((SB+k)) fatto"
done; done
if [ -n "$MIX" ]; then
  [ -f "$SRC/mazzi_mix_M6.json" ] || { echo "$B: manca mazzi_mix_M6.json"; exit 1; }
  for o in 1 2 3 4 5; do
    python3 -m sim.v02.run torneo --carte "$SRC/carte.json" \
      --mazzi "$SRC/mazzi.json#${DK[$o]}" "$SRC/mazzi_mix_M6.json#mix_M6_lucchetto_caccia" \
      --partite 0 --incroci "$NM" --seed $((SB+20+o)) --ia "$IA" "${TR[@]}" --out "$OUT/M6-L$o" > /dev/null
    echo "$B $IA M6-L$o seed $((SB+20+o)) fatto"
  done
fi
