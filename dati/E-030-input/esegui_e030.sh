#!/usr/bin/env bash
# E-030 (Q-026): corsa sequenziale di tutti i bracci, su una macchina a 4 core.
# Da eseguire dalla radice della repo al commit 4e13d90 o successivo (dove c'e' sim/):
#   nohup bash /mnt/project-files/tcg/set/esperimenti/E-030_q026/esegui_e030.sh > /dev/null 2>&1 &
# P-2c è condizionale: si aggiunge solo se lo screening di E-029 dà Δ05 ≤ −1.5:
#   E030_P2C=1 nohup bash .../esegui_e030.sh > /dev/null 2>&1 &
#   (rilanciare con E030_P2C=1 dopo una corsa finita gioca solo P-2c: gli incroci finiti si saltano)
# Si può rilanciare dopo un'interruzione: gli incroci finiti si saltano, quello interrotto riprende (--riprendi).
#
# Stime su 4 core, dal ritmo di E-028/E-029 (forte:30, V026, circa 13 s a partita sulla macchina intera):
#   1. 00_B0c05  IA semplice  tutti     semi 2000  400/incrocio  15 incroci  6.000 partite  ~0.2 h
#   2. 00_B0c05  forte:30     tutti     semi 3400  200/incrocio  15 incroci  3.000 partite  ~10.8 h
#   3. M2        forte:30     1,4,6     semi 3400  200/incrocio  12 incroci  2.400 partite  ~8.7 h
#   4. M3        forte:30     6         semi 3400  200/incrocio   5 incroci  1.000 partite  ~3.6 h
#   5. P-2c      forte:30     1,5       semi 3400  200/incrocio   9 incroci  1.800 partite  ~6.5 h  (solo con E030_P2C=1)
#   Totale: 12.400 partite, circa 23.3 h senza P-2c; 14.200 partite, circa 29.8 h con P-2c.
#   Ordine: il riferimento prima, così M2 e M3 si leggono appena finiscono.
set -uo pipefail
DIR=/mnt/project-files/tcg/set/esperimenti/E-030_q026
OUT=${E030_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-030_q026}
mkdir -p "$OUT"; LOG=$OUT/avanzamento.log
[ -d sim/v02 ] || { echo "eseguire dalla radice della repo (manca sim/v02)"; exit 1; }
echo "$(date -u +%FT%TZ) E-030, motore $(git rev-parse --short HEAD 2>/dev/null || echo '?'), V026, --riprendi, P-2c=${E030_P2C:-0}" >> "$LOG"
corsa() {   # braccio ia partite seed_base protagonisti
  echo "$(date -u +%FT%TZ) inizio $1 $2 $3 $4 $5" >> "$LOG"
  if E030_TRACCIA=$(cat "$DIR/$1/traccia.txt") bash "$DIR/lancia_e030.sh" "$1" "$2" "$3" "$4" "$5" >> "$LOG" 2>&1; then
    echo "$(date -u +%FT%TZ) fine $1 $2 $4" >> "$LOG"
  else
    echo "$(date -u +%FT%TZ) ERRORE $1 $2 $4" >> "$LOG"; return 1
  fi
}
corsa 00_B0c05 semplice 400 2000 tutti  || exit 1
corsa 00_B0c05 forte:30 200 3400 tutti  || exit 1
corsa M2 forte:30 200 3400 1,4,6        || exit 1
corsa M3 forte:30 200 3400 6            || exit 1
if [ "${E030_P2C:-0}" = 1 ]; then
  corsa P-2c forte:30 200 3400 1,5      || exit 1
else
  echo "$(date -u +%FT%TZ) P-2c non lanciato (E030_P2C non è 1)" >> "$LOG"
fi
touch "$OUT/FINE"
echo "$(date -u +%FT%TZ) fine E-030" >> "$LOG"
