#!/usr/bin/env bash
# E-031 (Q-027): un braccio, per celle. Copiato da lancia_e030.sh; passa --riprendi e salta gli incroci finiti.
# Da eseguire dalla radice della repo (dove c'e' sim/), sul motore con le primitive di R-026 (bounce, on_rim, sacrifice,
# recover, Reazione a costo 0 con condizione di gioco): prima nessun braccio passa `valida` (le bozze di carte_q027.json).
#
#   bash lancia_e031.sh <braccio> <ia> <partite_per_incrocio> <seed_base> <celle>
#
#   celle         tutti | p:2,4 (ogni incrocio che tocca un protagonista) | 2-5,4-5 (incroci espliciti i-j, i<j)
#   seed_base     3400 (stessi semi di E-030: le celle si confrontano con E-030 00_B0c05 e R5-2c): uscita F_s3400.
#                 Il seme di un incrocio è seed_base+k, k = indice della coppia (1-2 → 1 … 5-6 → 15), come in E-020…E-030.
#   E031_VARIANTE facoltativa: preset o file JSON per --variante (default V027)
#   E031_OUT      facoltativa: cartella risultati (default tcg/swarm/esperimenti/E-031_q027)
#   E031_TRACCIA  facoltativa: ID per --traccia (ogni braccio ha il suo traccia.txt)
#   E031_RIPRENDI facoltativa: 0 per non passare --riprendi (default 1)
#   E031_RIFAI    facoltativa: 1 per rigiocare anche gli incroci già finiti
set -euo pipefail
B=$1; IA=$2; N=$3; SB=$4; CELLE=$5
BASE=/mnt/project-files/tcg/set/esperimenti/E-031_q027; SRC=$BASE/$B
VAR=${E031_VARIANTE:-V027}
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=${E031_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-031_q027}/$B/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(); [ -n "${E031_TRACCIA:-}" ] && TR=(--traccia "$E031_TRACCIA")
[ "${E031_RIPRENDI:-1}" = 1 ] && TR+=(--riprendi)
[ -f "$SRC/carte.json" ] || { echo "$B: nessun carte.json"; exit 1; }
fatto() { [ "${E031_RIFAI:-0}" != 1 ] && ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
tocca() {
  case "$CELLE" in
    tutti) return 0 ;;
    p:*) for p in $(echo "${CELLE#p:}" | tr ',' ' '); do [ "$p" = "$1" ] || [ "$p" = "$2" ] && return 0; done; return 1 ;;
    *) for c in $(echo "$CELLE" | tr ',' ' '); do [ "$c" = "$1-$2" ] && return 0; done; return 1 ;;
  esac
}
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1)); tocca $i $j || continue
  if fatto "$OUT/L$i-L$j"; then echo "$B $IA L$i-L$j gia' fatto, salto"; continue; fi
  python3 -B -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
    --mazzi "$SRC/mazzi.json#${DK[$i]}" "$SRC/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$OUT/L$i-L$j" > /dev/null
  echo "$B $IA L$i-L$j seed $((SB+k)) fatto"
done; done
