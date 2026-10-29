#!/usr/bin/env bash
# E-020 (Q-020): lancia un braccio un incrocio alla volta, cosi' ogni report e' una cella della matrice 6x6.
# Da eseguire dalla radice della repo (dove c'e' sim/). Motore: feabc5c o successivo (on_attack del Leader, matrice, --traccia).
#
#   bash lancia_e020.sh <braccio> <ia> <partite_per_incrocio> <seed_base> <protagonisti|tutti> [mix]
#
#   braccio      cartella in tcg/set/esperimenti/E-020 (es. 08_T1)
#   ia           semplice | forte:30
#   seed_base    2000 per la semplice, 3000 per la forte (uguale in TUTTI i bracci: partite appaiate)
#   protagonisti "tutti" = 15 incroci; lista di Leader, es. "4" o "1,5" (solo gli incroci che li toccano); "nessuno" = solo mix
#   E020_OUT     variabile d'ambiente facoltativa: cartella dei risultati al posto di tcg/swarm/esperimenti/E-020
#   E020_TRACCIA variabile d'ambiente facoltativa: ID da tracciare, passati a --traccia (es. LDR-05,ROS-020,NEU-013)
#   mix          se presente: anche mix_M3_thorn_lucchetto contro i 5 rif non-Thorn (R9-5 del lucchetto)
#
# Seed di un incrocio = seed_base + indice fisso della coppia (1-2 -> 1, ..., 5-6 -> 15; mix contro LDR-0k -> 20+k),
# lo stesso in ogni braccio. Nella coppia il mazzo col Leader di numero minore e' sempre il primo (posti alternati dal motore).
set -euo pipefail
B=$1; IA=$2; N=$3; SB=$4; PROT=$5; MIX=${6:-}
SRC=/mnt/project-files/tcg/set/esperimenti/E-020/$B
OUT=${E020_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-020}/$B/$( [ "$IA" = semplice ] && echo S || echo F )
TR=(); [ -n "${E020_TRACCIA:-}" ] && TR=(--traccia "$E020_TRACCIA")
[ -f "$SRC/carte.json" ] || { echo "$B: nessun carte.json (braccio bloccato?)"; exit 1; }
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
  [ -f "$SRC/mazzi_mix_M3.json" ] || { echo "$B: manca mazzi_mix_M3.json"; exit 1; }
  for o in 1 2 3 5 6; do
    python3 -m sim.v02.run torneo --carte "$SRC/carte.json" \
      --mazzi "$SRC/mazzi.json#${DK[$o]}" "$SRC/mazzi_mix_M3.json#mix_M3_thorn_lucchetto" \
      --partite 0 --incroci "$N" --seed $((SB+20+o)) --ia "$IA" "${TR[@]}" --out "$OUT/M3-L$o" > /dev/null
    echo "$B $IA M3-L$o seed $((SB+20+o)) fatto"
  done
fi
