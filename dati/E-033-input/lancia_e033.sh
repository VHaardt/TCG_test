#!/usr/bin/env bash
# E-033 (R-028, Q-028): vaglio delle leve di ritmo. Copiato da lancia_e031.sh: passa --riprendi e salta gli incroci finiti.
# Da eseguire dalla radice della repo (dove c'e' sim/), su main con la PR #22 (636e83e o successivo: parametri
# bruciare, tempra_tardo, allo_scoperto e tabella "R-028 (Q-028): ritmo" nel report).
#
#   bash dati/E-033-input/lancia_e033.sh <braccio|tutti> [ia] [partite_per_incrocio] [seed_base] [celle]
#
#   braccio       bruciare | tempra_tardo | allo_scoperto | breccia | tutti (i quattro in quest'ordine)
#                 breccia = V027 senza leve, con carte, liste e traccia di breccia/ (NEW-BR1–BR6, Q-028 V3)
#                 00_rif = base B0c05 su V027 senza leve: NON fa parte del vaglio (il riferimento è E-030 00_B0c05 F_s3400),
#                 si lancia solo a mano se servono i contatori R-028 della base (vedi LEGGIMI.md)
#   ia            default forte:30
#   partite       default 100 (partite per incrocio)
#   seed_base     default 3400: seme dell'incrocio = seed_base+k, k = indice della coppia (1-2 → 1 … 5-6 → 15),
#                 come in E-030; le partite 0..99 hanno gli stessi semi delle prime 100 di 00_B0c05 F_s3400
#   celle         tutti (default) | p:2,4 (incroci che toccano un protagonista) | 2-5,4-5 (incroci espliciti i-j, i<j)
#   E033_OUT      facoltativa: cartella risultati (default tcg/swarm/esperimenti/E-033_ritmo)
#   E033_RIPRENDI facoltativa: 0 per non passare --riprendi (default 1)
#   E033_RIFAI    facoltativa: 1 per rigiocare anche gli incroci già finiti
#
# Stima su 4 core (forte:30, ~13 s a partita sulla macchina intera in E-030): 1.500 partite per braccio,
# ~5.4 h tempra_tardo e allo_scoperto, ~8 h bruciare (più scelte per l'IA forte: +50% circa nella prova), ~5.4 h breccia. Totale ~24.5 h.
set -euo pipefail
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
B=$1; IA=${2:-forte:30}; N=${3:-100}; SB=${4:-3400}; CELLE=${5:-tutti}
OUTB=${E033_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-033_ritmo}
[ -d sim/v02 ] || { echo "eseguire dalla radice della repo (manca sim/v02)"; exit 1; }
grep -q tempra_tardo sim/v02/config.py || { echo "motore senza R-028 (tempra_tardo): serve main 636e83e o successivo"; exit 1; }
if [ "$B" = tutti ]; then
  for b in bruciare tempra_tardo allo_scoperto breccia; do bash "$DIR/lancia_e033.sh" "$b" "$IA" "$N" "$SB" "$CELLE"; done
  exit 0
fi
SRC=$DIR
case "$B" in
  00_rif) VAR=V027 ;;
  breccia) VAR=V027; SRC=$DIR/breccia ;;
  bruciare|tempra_tardo|allo_scoperto) VAR=$DIR/varianti/$B.json ;;
  *) echo "braccio sconosciuto: $B"; exit 1 ;;
esac
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=$OUTB/$B/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(--traccia "$(cat "$SRC/traccia.txt")")
[ "${E033_RIPRENDI:-1}" = 1 ] && TR+=(--riprendi)
mkdir -p "$OUTB"; LOG=$OUTB/avanzamento.log
fatto() { [ "${E033_RIFAI:-0}" != 1 ] && ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
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
  if fatto "$OUT/L$i-L$j"; then echo "$B $IA L$i-L$j gia' fatto, salto" | tee -a "$LOG"; continue; fi
  python3 -B -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
    --mazzi "$SRC/mazzi.json#${DK[$i]}" "$SRC/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$OUT/L$i-L$j" > /dev/null
  echo "$(date -u +%FT%TZ) $B $IA L$i-L$j seed $((SB+k)) fatto" | tee -a "$LOG"
done; done
echo "$(date -u +%FT%TZ) fine $B $IA $SB" >> "$LOG"
