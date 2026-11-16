#!/usr/bin/env bash
# E-036 (ciclo 05, esito_piano.md P2): vaglio delle leve su L5 e L6, V027 + Tempra 3 dal round 10 (A), solo gli incroci
# del protagonista. Copiato da lancia_e034.sh: passa --riprendi, salta gli incroci finiti e TIENE I RECORD PER PARTITA.
# Da eseguire dalla radice della repo (dove c'e' sim/), su main 7ec6380 o successivo; L5-c e L6-ad solo con R-031.
#
#   bash dati/E-036-input/lancia_e036.sh <braccio|tutti> [ia] [partite_per_incrocio] [seed_base]
#
#   braccio   L5-c | L5-b | L6-a | L6-ab | L6-ad | tutti (i cinque, in quest'ordine; quelli senza la primitiva si saltano)
#             00_B0c06A = riferimento B0c06 + A sugli stessi semi e sulle stesse celle (L5, L6 e le due R5-2c): NON è
#             nel vaglio approvato, si lancia a mano solo se il thread vuole un confronto appaiato (vedi LEGGIMI.md)
#   ia        default forte:30;  partite default 200;  seed_base default 3700
#   celle     L5-*: i 5 incroci di L5; L5-b anche L1-R5 e L2-R5 (L1, L2 contro rott_LDR05_2c); L6-*: i 5 incroci di L6
#   Seme dell'incrocio i-j = seed_base+k, k = indice della coppia (1-2 → 1 … 5-6 → 15); L1-R5 usa il k di 1-5 (4),
#   L2-R5 quello di 2-5 (8).
#   E036_OUT facoltativa (default tcg/swarm/esperimenti/E-036_vaglio); E036_RIPRENDI=0, E036_RIFAI=1 come in E-034.
#
# Stima su 4 core (~13 s a partita): 1.000 partite per braccio (~3.6 h), L5-b 1.400 (~5 h); i cinque ~19 h.
set -euo pipefail
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
B=$1; IA=${2:-forte:30}; N=${3:-200}; SB=${4:-3700}
OUTB=${E036_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-036_vaglio}
[ -d sim/v02 ] || { echo "eseguire dalla radice della repo (manca sim/v02)"; exit 1; }
grep -q tempra_tardo sim/v02/config.py || { echo "motore senza R-028 (tempra_tardo)"; exit 1; }
if [ "$B" = tutti ]; then
  for b in L5-c L5-b L6-a L6-ab L6-ad; do bash "$DIR/lancia_e036.sh" "$b" "$IA" "$N" "$SB" || echo "$b non lanciato"; done
  exit 0
fi
case "$B" in
  L5-c)  PROT=5; NEED=first_attack_kw ;;
  L5-b)  PROT=5; NEED="" ;;
  L6-a|L6-ab) PROT=6; NEED="" ;;
  L6-ad) PROT=6; NEED=target_has ;;
  00_B0c06A) PROT="5 6"; NEED="" ;;
  *) echo "braccio sconosciuto: $B"; exit 1 ;;
esac
if [ -n "$NEED" ] && ! grep -q "\"$NEED\"" sim/v02/validate.py; then
  echo "$B: il motore non ha la condizione $NEED (R-031): braccio saltato"; exit 1
fi
SRC=$DIR/$B; VAR=$DIR/varianti/tempra_tardo.json
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=$OUTB/$B/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(--traccia "$(cat "$SRC/traccia.txt")")
[ "${E036_RIPRENDI:-1}" = 1 ] && TR+=(--riprendi)
mkdir -p "$OUTB"; LOG=$OUTB/avanzamento.log
fatto() { [ "${E036_RIFAI:-0}" != 1 ] && ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
cella() {   # nome mazzo1 mazzo2 k
  local O=$OUT/$1
  if fatto "$O"; then echo "$B $IA $1 gia' fatto, salto" | tee -a "$LOG"; return; fi
  mkdir -p "$O"
  if [ "${E036_RIPRENDI:-1}" = 1 ]; then
    [ -f "$O/.partite_fatte.pkl" ] || : > "$O/.partite_fatte.pkl"
    [ "$O/.partite_fatte.pkl" -ef "$O/partite.pkl" ] || ln -f "$O/.partite_fatte.pkl" "$O/partite.pkl"
  fi
  python3 -B -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
    --mazzi "$SRC/mazzi.json#$2" "$SRC/mazzi.json#$3" \
    --partite 0 --incroci "$N" --seed $((SB+$4)) --ia "$IA" "${TR[@]}" --out "$O" > /dev/null
  echo "$(date -u +%FT%TZ) $B $IA $1 seed $((SB+$4)) fatto" | tee -a "$LOG"
}
echo "$(date -u +%FT%TZ) inizio $B $IA $N $SB, motore $(git rev-parse --short HEAD 2>/dev/null || echo '?')" >> "$LOG"
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1))
  for p in $PROT; do
    if [ "$p" = "$i" ] || [ "$p" = "$j" ]; then cella "L$i-L$j" "${DK[$i]}" "${DK[$j]}" $k; break; fi
  done
done; done
if [ "$B" = L5-b ] || [ "$B" = 00_B0c06A ]; then
  cella L1-R5 "${DK[1]}" rott_LDR05_2c 4
  cella L2-R5 "${DK[2]}" rott_LDR05_2c 8
fi
echo "$(date -u +%FT%TZ) fine $B $IA $SB" >> "$LOG"
