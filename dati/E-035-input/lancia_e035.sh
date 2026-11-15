#!/usr/bin/env bash
# E-035 (Q-031, ciclo 05 D): le 4 liste mix_ a 2 copie contro le 6 liste rif_ di B0c06. 24 incroci, nessun braccio.
# Copiato da lancia_e034.sh: passa --riprendi, salta gli incroci finiti e TIENE I RECORD PER PARTITA (partite.pkl in ogni cella).
# Da eseguire dalla radice della repo (dove c'e' sim/), su main 7ec6380 o successivo. In coda dopo E-034.
#
#   bash dati/E-035-input/lancia_e035.sh [ia] [partite_per_incrocio] [seed_base] [celle]
#
#   ia            default forte:30
#   partite       default 200 (partite per incrocio)
#   seed_base     default 3600: seme dell'incrocio = seed_base+k, k = 1..24 nell'ordine
#                 M1-L1, M1-L2, … M1-L6, M2-L1, … M4-L6 (k = 6·(m−1) + l)
#   celle         tutti (default) | p:M1,L5 (incroci che toccano una lista) | M1-L2,M3-L5 (incroci espliciti)
#   E035_OUT      facoltativa: cartella risultati (default tcg/swarm/esperimenti/E-035_mix)
#   E035_RIPRENDI facoltativa: 0 per non passare --riprendi (default 1; con 0 i record per partita non si tengono)
#   E035_RIFAI    facoltativa: 1 per rigiocare anche gli incroci già finiti
#
# Stima su 4 core (forte:30, ~13 s a partita sulla macchina intera): 4.800 partite, ~17.3 h.
set -euo pipefail
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
IA=${1:-forte:30}; N=${2:-200}; SB=${3:-3600}; CELLE=${4:-tutti}
OUTB=${E035_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-035_mix}
[ -d sim/v02 ] || { echo "eseguire dalla radice della repo (manca sim/v02)"; exit 1; }
grep -q render_breccia sim/v02/run.py || echo "attenzione: motore senza le tabelle Scudo/Brecce per carta (7ec6380)"
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=$OUTB/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(--traccia "$(cat "$DIR/traccia.txt")")
[ "${E035_RIPRENDI:-1}" = 1 ] && TR+=(--riprendi)
mkdir -p "$OUTB"; LOG=$OUTB/avanzamento.log
fatto() { [ "${E035_RIFAI:-0}" != 1 ] && ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
MX=(x mix_M1_maera_bunker mix_M2_vey_blitz mix_M3_thorn_lucchetto mix_M4_arden_sanguinante)
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
tocca() {
  case "$CELLE" in
    tutti) return 0 ;;
    p:*) for p in $(echo "${CELLE#p:}" | tr ',' ' '); do [ "$p" = "$1" ] || [ "$p" = "$2" ] && return 0; done; return 1 ;;
    *) for c in $(echo "$CELLE" | tr ',' ' '); do [ "$c" = "$1-$2" ] && return 0; done; return 1 ;;
  esac
}
echo "$(date -u +%FT%TZ) inizio E-035 $IA $N $SB $CELLE, motore $(git rev-parse --short HEAD 2>/dev/null || echo '?')" >> "$LOG"
for m in 1 2 3 4; do for l in 1 2 3 4 5 6; do
  k=$((6*(m-1)+l)); tocca "M$m" "L$l" || continue
  O=$OUT/M$m-L$l
  if fatto "$O"; then echo "M$m-L$l gia' fatto, salto" | tee -a "$LOG"; continue; fi
  mkdir -p "$O"
  if [ "${E035_RIPRENDI:-1}" = 1 ]; then
    [ -f "$O/.partite_fatte.pkl" ] || : > "$O/.partite_fatte.pkl"
    [ "$O/.partite_fatte.pkl" -ef "$O/partite.pkl" ] || ln -f "$O/.partite_fatte.pkl" "$O/partite.pkl"
  fi
  python3 -B -m sim.v02.run torneo --variante V027 --carte "$DIR/carte.json" \
    --mazzi "$DIR/mazzi.json#${MX[$m]}" "$DIR/mazzi.json#${DK[$l]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$O" > /dev/null
  echo "$(date -u +%FT%TZ) $IA M$m-L$l seed $((SB+k)) fatto" | tee -a "$LOG"
done; done
echo "$(date -u +%FT%TZ) fine E-035 $IA $SB" >> "$LOG"
