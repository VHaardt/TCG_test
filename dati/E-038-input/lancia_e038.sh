#!/usr/bin/env bash
# E-038 (ciclo 05, voto_lampo.md V2): combinazione finale L5 × L6 sui 15 incroci, con A (200 partite) e senza A (100).
# Copiato da lancia_e037.sh: --riprendi, salta gli incroci finiti, TIENE I RECORD PER PARTITA, lancia `valida` prima di
# giocare e salta la combinazione se non passa. Da eseguire dalla radice della repo, su un motore con R-032 (612057d o
# successivo: campi life, tempra e tempra_fissa del Leader).
#
#   bash dati/E-038-input/lancia_e038.sh <combinazione> <conA|senzaA> [ia] [partite_per_incrocio] [seed_base]
#
#   combinazione  H5-t+H6-v | H5-t+H6-c | H5-v+H6-v | H5-v+H6-c | H5-r+H6-v | H5-r+H6-c
#                 (LDR-05 del braccio H5-x di E-037, LDR-06 del braccio H6-y; liste rif_ di B0c06 V4 invariate)
#   conA          V027 + Tempra 3 dal round 10 (varianti/tempra_tardo.json), default 200 partite per incrocio
#   senzaA        V027, default 100 partite per incrocio (test P1 di A, a bassa potenza)
#                 H5-t ha Tempra 3 fissa in tutte e due le versioni (tempra_fissa: A non la abbassa)
#   ia            default forte:30;  seed_base default 3700: seme dell'incrocio = seed_base+k (1-2 → 1 … 5-6 → 15)
#   E038_OUT facoltativa (default tcg/swarm/esperimenti/E-038_combinazione); uscita <combinazione>/<conA|senzaA>/F_s3700/Li-Lj
#   E038_RIPRENDI=0, E038_RIFAI=1 come in E-034.
#
# Stima su 4 core (~13 s a partita): con A 3.000 partite (~10.8 h), senza A 1.500 (~5.4 h).
set -euo pipefail
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
C=${1:?combinazione}; V=${2:?conA o senzaA}; IA=${3:-forte:30}; SB=${5:-3700}
case "$V" in
  conA) VAR=$DIR/varianti/tempra_tardo.json; N=${4:-200} ;;
  senzaA) VAR=V027; N=${4:-100} ;;
  *) echo "versione sconosciuta: $V (conA o senzaA)"; exit 1 ;;
esac
SRC=$DIR/$C
[ -f "$SRC/carte.json" ] || { echo "combinazione sconosciuta: $C"; exit 1; }
OUTB=${E038_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-038_combinazione}
[ -d sim/v02 ] || { echo "eseguire dalla radice della repo (manca sim/v02)"; exit 1; }
mkdir -p "$OUTB"; LOG=$OUTB/avanzamento.log
if ! python3 -B -m sim.v02.run valida "$SRC/carte.json" --mazzi "$SRC/mazzi.json" --variante "$VAR" > /dev/null 2>&1; then
  echo "$(date -u +%FT%TZ) $C $V: valida non passa su questo motore (serve R-032): saltato" | tee -a "$LOG"; exit 1
fi
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=$OUTB/$C/$V/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(--traccia "$(cat "$DIR/traccia.txt")")
[ "${E038_RIPRENDI:-1}" = 1 ] && TR+=(--riprendi)
fatto() { [ "${E038_RIFAI:-0}" != 1 ] && ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
echo "$(date -u +%FT%TZ) inizio $C $V $IA $N $SB, motore $(git rev-parse --short HEAD 2>/dev/null || echo '?')" >> "$LOG"
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1)); O=$OUT/L$i-L$j
  if fatto "$O"; then echo "$C $V L$i-L$j gia' fatto, salto" | tee -a "$LOG"; continue; fi
  mkdir -p "$O"
  if [ "${E038_RIPRENDI:-1}" = 1 ]; then
    [ -f "$O/.partite_fatte.pkl" ] || : > "$O/.partite_fatte.pkl"
    [ "$O/.partite_fatte.pkl" -ef "$O/partite.pkl" ] || ln -f "$O/.partite_fatte.pkl" "$O/partite.pkl"
  fi
  python3 -B -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
    --mazzi "$SRC/mazzi.json#${DK[$i]}" "$SRC/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$O" > /dev/null
  echo "$(date -u +%FT%TZ) $C $V $IA L$i-L$j seed $((SB+k)) fatto" | tee -a "$LOG"
done; done
echo "$(date -u +%FT%TZ) fine $C $V $IA $SB" >> "$LOG"
