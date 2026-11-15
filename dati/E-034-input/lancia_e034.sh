#!/usr/bin/env bash
# E-034 (Q-031, ciclo 05 B): misura del riferimento B0c06. Copiato da lancia_e033.sh: passa --riprendi, salta gli incroci
# finiti e TIENE I RECORD PER PARTITA (partite.pkl in ogni cella, accanto al report).
# Da eseguire dalla radice della repo (dove c'e' sim/), su main 7ec6380 o successivo (tabelle R-028, R-026, Scudo e Brecce nel report).
#
#   bash dati/E-034-input/lancia_e034.sh <braccio|tutti> [ia] [partite_per_incrocio] [seed_base] [celle]
#
#   braccio       00_B0c06 (V027) | tempra_tardo (V027 + Tempra 3 dal round 10, varianti/tempra_tardo.json, lo stesso
#                 file di E-033) | tutti (i due in quest'ordine)
#   ia            default forte:30
#   partite       default 200 (partite per incrocio)
#   seed_base     default 3500 (semi nuovi): seme dell'incrocio = seed_base+k, k = indice della coppia (1-2 → 1 … 5-6 → 15)
#   celle         tutti (default) | p:2,4 (incroci che toccano un protagonista) | 2-5,4-5 (incroci espliciti i-j, i<j)
#   E034_OUT      facoltativa: cartella risultati (default tcg/swarm/esperimenti/E-034_B0c06)
#   E034_RIPRENDI facoltativa: 0 per non passare --riprendi (default 1; con 0 i record per partita non si tengono)
#   E034_RIFAI    facoltativa: 1 per rigiocare anche gli incroci già finiti
#
# Record per partita: run.py scrive ogni partita in <cella>/.partite_fatte.pkl e lo cancella a fine cella. Prima di giocare
# il launcher crea quel file e un collegamento fisso <cella>/partite.pkl allo stesso file: a fine cella il checkpoint sparisce,
# partite.pkl resta con tutte le partite (formato: pickle di (indice, record) in sequenza, come lo legge dati/coda/agg_q028.py).
#
# Stima su 4 core (forte:30, ~13 s a partita sulla macchina intera): 3.000 partite per braccio, ~10.8 h ciascuno, ~21.6 h in tutto.
set -euo pipefail
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
B=$1; IA=${2:-forte:30}; N=${3:-200}; SB=${4:-3500}; CELLE=${5:-tutti}
OUTB=${E034_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-034_B0c06}
[ -d sim/v02 ] || { echo "eseguire dalla radice della repo (manca sim/v02)"; exit 1; }
grep -q tempra_tardo sim/v02/config.py || { echo "motore senza R-028 (tempra_tardo): serve main 636e83e o successivo"; exit 1; }
grep -q render_breccia sim/v02/run.py || echo "attenzione: motore senza le tabelle Scudo/Brecce per carta (7ec6380)"
if [ "$B" = tutti ]; then
  for b in 00_B0c06 tempra_tardo; do bash "$DIR/lancia_e034.sh" "$b" "$IA" "$N" "$SB" "$CELLE"; done
  exit 0
fi
case "$B" in
  00_B0c06) VAR=V027 ;;
  tempra_tardo) VAR=$DIR/varianti/tempra_tardo.json ;;
  *) echo "braccio sconosciuto: $B"; exit 1 ;;
esac
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=$OUTB/$B/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(--traccia "$(cat "$DIR/traccia.txt")")
[ "${E034_RIPRENDI:-1}" = 1 ] && TR+=(--riprendi)
mkdir -p "$OUTB"; LOG=$OUTB/avanzamento.log
fatto() { [ "${E034_RIFAI:-0}" != 1 ] && ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
tocca() {
  case "$CELLE" in
    tutti) return 0 ;;
    p:*) for p in $(echo "${CELLE#p:}" | tr ',' ' '); do [ "$p" = "$1" ] || [ "$p" = "$2" ] && return 0; done; return 1 ;;
    *) for c in $(echo "$CELLE" | tr ',' ' '); do [ "$c" = "$1-$2" ] && return 0; done; return 1 ;;
  esac
}
echo "$(date -u +%FT%TZ) inizio $B $IA $N $SB $CELLE, motore $(git rev-parse --short HEAD 2>/dev/null || echo '?')" >> "$LOG"
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1)); tocca $i $j || continue
  O=$OUT/L$i-L$j
  if fatto "$O"; then echo "$B $IA L$i-L$j gia' fatto, salto" | tee -a "$LOG"; continue; fi
  mkdir -p "$O"
  if [ "${E034_RIPRENDI:-1}" = 1 ]; then
    [ -f "$O/.partite_fatte.pkl" ] || : > "$O/.partite_fatte.pkl"
    [ "$O/.partite_fatte.pkl" -ef "$O/partite.pkl" ] || ln -f "$O/.partite_fatte.pkl" "$O/partite.pkl"
  fi
  python3 -B -m sim.v02.run torneo --variante "$VAR" --carte "$DIR/carte.json" \
    --mazzi "$DIR/mazzi.json#${DK[$i]}" "$DIR/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$O" > /dev/null
  echo "$(date -u +%FT%TZ) $B $IA L$i-L$j seed $((SB+k)) fatto" | tee -a "$LOG"
done; done
echo "$(date -u +%FT%TZ) fine $B $IA $SB" >> "$LOG"
