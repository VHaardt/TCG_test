#!/usr/bin/env bash
# E-029 (ciclo 04, misura X, 8/8): corsa sequenziale di tutti i bracci con l'IA forte, su una macchina a 4 core.
# Da eseguire dalla radice della repo al commit 4e13d90 o successivo (dove c'e' sim/):
#   nohup bash /mnt/project-files/tcg/set/esperimenti/E-029_c04/esegui_e029.sh > /dev/null 2>&1 &
# Si può rilanciare dopo un'interruzione: gli incroci finiti si saltano, quello interrotto riprende (--riprendi).
#
# Stime su 4 core, dal ritmo di E-028 (forte:30, V026, circa 13 s a partita sulla macchina intera:
# RB 1.800 partite in 6.45 h, 00_B0c03 su 3300 500 partite in 1.81 h):
#   1. P          protagonisti 1,5  semi 3200  200/incrocio  9 incroci  1.800 partite  ~6.5 h  (riferimento: E-028_c04/00_B0c03/F_s3200, già fatto)
#   2. 00_B0c03   protagonista 5    semi 3300  200/incrocio  5 incroci  1.000 partite  ~3.6 h  (riferimento della parte su 3300, rigiocato intero)
#   3. P-rott     protagonista 5    semi 3300  200/incrocio  5 incroci  1.000 partite  ~3.6 h
#   4. D05b-200   protagonista 5    semi 3300  200/incrocio  5 incroci  1.000 partite  ~3.6 h
#   5. D-2M       protagonista 5    semi 3300  200/incrocio  5 incroci  1.000 partite  ~3.6 h
#   Totale: 5.800 partite, circa 21 h.
set -uo pipefail
DIR=/mnt/project-files/tcg/set/esperimenti/E-029_c04
OUT=${E029_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-029_c04}
mkdir -p "$OUT"; LOG=$OUT/avanzamento.log
[ -d sim/v02 ] || { echo "eseguire dalla radice della repo (manca sim/v02)"; exit 1; }
echo "$(date -u +%FT%TZ) E-029, motore $(git rev-parse --short HEAD 2>/dev/null || echo '?'), V026, --riprendi" >> "$LOG"
corsa() {   # braccio seed_base protagonisti
  echo "$(date -u +%FT%TZ) inizio $1 forte:30 200 $2 $3" >> "$LOG"
  if E029_TRACCIA=$(cat "$DIR/$1/traccia.txt") bash "$DIR/lancia_e029.sh" "$1" forte:30 200 "$2" "$3" >> "$LOG" 2>&1; then
    echo "$(date -u +%FT%TZ) fine $1 forte:30 $2" >> "$LOG"
  else
    echo "$(date -u +%FT%TZ) ERRORE $1 forte:30 $2" >> "$LOG"; return 1
  fi
}
corsa P 3200 1,5        || exit 1
corsa 00_B0c03 3300 5   || exit 1
corsa P-rott 3300 5     || exit 1
corsa D05b-200 3300 5   || exit 1
corsa D-2M 3300 5       || exit 1
touch "$OUT/FINE"
echo "$(date -u +%FT%TZ) fine E-029" >> "$LOG"
