#!/usr/bin/env bash
# E-037 (ciclo 05, voto_lampo.md V1): vaglio delle leve dure su L5 e L6, V027 + Tempra 3 dal round 10 (A), solo gli
# incroci del protagonista. Copiato da lancia_e036.sh: --riprendi, salta gli incroci finiti, TIENE I RECORD PER PARTITA.
# Da eseguire dalla radice della repo (dove c'e' sim/). H5-t, H5-v e H6-v hanno bisogno di R-032 (campi 'life' e 'tempra'
# del Leader; H5-t anche 'tempra_fissa': A non abbassa la Tempra 3 di LDR-05): prima di ogni braccio il launcher lancia `valida` e salta il braccio se non passa.
#
#   bash dati/E-037-input/lancia_e037.sh <braccio|tutti> [ia] [partite_per_incrocio] [seed_base]
#
#   braccio   H5-t | H5-v | H5-r | H6-v | H6-c | tutti (in quest'ordine; quelli che non passano valida si saltano)
#   ia        default forte:30;  partite default 100;  seed_base default 3700 (gli stessi semi di E-036: le 100 partite
#             sono appaiate con le prime 100 di E-036 00_B0c06A e, per H6-v, di L6-a)
#   Seme dell'incrocio i-j = seed_base+k, k = indice della coppia (1-2 → 1 … 5-6 → 15).
#   E037_OUT facoltativa (default tcg/swarm/esperimenti/E-037_leve_dure); E037_RIPRENDI=0, E037_RIFAI=1 come in E-034.
#
# Stima su 4 core (~13 s a partita): 500 partite per braccio, ~1.8 h; i cinque ~9 h.
set -euo pipefail
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
B=$1; IA=${2:-forte:30}; N=${3:-100}; SB=${4:-3700}
OUTB=${E037_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-037_leve_dure}
[ -d sim/v02 ] || { echo "eseguire dalla radice della repo (manca sim/v02)"; exit 1; }
grep -q tempra_tardo sim/v02/config.py || { echo "motore senza R-028 (tempra_tardo)"; exit 1; }
if [ "$B" = tutti ]; then
  for b in H5-t H5-v H5-r H6-v H6-c; do bash "$DIR/lancia_e037.sh" "$b" "$IA" "$N" "$SB" || echo "$b non lanciato"; done
  exit 0
fi
case "$B" in
  H5-t|H5-v|H5-r) PROT=5 ;;
  H6-v|H6-c) PROT=6 ;;
  *) echo "braccio sconosciuto: $B"; exit 1 ;;
esac
SRC=$DIR/$B; VAR=$DIR/varianti/tempra_tardo.json
mkdir -p "$OUTB"; LOG=$OUTB/avanzamento.log
if ! python3 -B -m sim.v02.run valida "$SRC/carte.json" --mazzi "$SRC/mazzi.json" --variante "$VAR" > /dev/null 2>&1; then
  echo "$(date -u +%FT%TZ) $B: valida non passa su questo motore (R-032?): braccio saltato" | tee -a "$LOG"; exit 1
fi
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=$OUTB/$B/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(--traccia "$(cat "$DIR/traccia.txt")")
[ "${E037_RIPRENDI:-1}" = 1 ] && TR+=(--riprendi)
fatto() { [ "${E037_RIFAI:-0}" != 1 ] && ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
echo "$(date -u +%FT%TZ) inizio $B $IA $N $SB, motore $(git rev-parse --short HEAD 2>/dev/null || echo '?')" >> "$LOG"
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1)); [ "$i" = "$PROT" ] || [ "$j" = "$PROT" ] || continue
  O=$OUT/L$i-L$j
  if fatto "$O"; then echo "$B $IA L$i-L$j gia' fatto, salto" | tee -a "$LOG"; continue; fi
  mkdir -p "$O"
  if [ "${E037_RIPRENDI:-1}" = 1 ]; then
    [ -f "$O/.partite_fatte.pkl" ] || : > "$O/.partite_fatte.pkl"
    [ "$O/.partite_fatte.pkl" -ef "$O/partite.pkl" ] || ln -f "$O/.partite_fatte.pkl" "$O/partite.pkl"
  fi
  python3 -B -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
    --mazzi "$SRC/mazzi.json#${DK[$i]}" "$SRC/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$O" > /dev/null
  echo "$(date -u +%FT%TZ) $B $IA L$i-L$j seed $((SB+k)) fatto" | tee -a "$LOG"
done; done
echo "$(date -u +%FT%TZ) fine $B $IA $SB" >> "$LOG"
