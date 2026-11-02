#!/usr/bin/env bash
# E-031 (Q-027): corsa sequenziale, IA forte:30, 200 partite per incrocio, semi 3400+k, preset V027. Parte solo dopo E-030.
# Da eseguire dalla radice della repo, sul motore con le primitive di R-026:
#   nohup bash /mnt/project-files/tcg/set/esperimenti/E-031_q027/esegui_e031.sh > /dev/null 2>&1 &
# Prima di ogni braccio gira `valida --variante V027`: un braccio con bozze non ancora supportate si ferma lì.
# Rilanciabile: gli incroci finiti si saltano, quello interrotto riprende (--riprendi).
# Stime (circa 13 s a partita su 4 core): vedi piano.md. Totale 8.400 partite, circa 30.3 h.
set -uo pipefail
DIR=/mnt/project-files/tcg/set/esperimenti/E-031_q027
OUT=${E031_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-031_q027}
mkdir -p "$OUT"; LOG=$OUT/avanzamento.log
[ -d sim/v02 ] || { echo "eseguire dalla radice della repo (manca sim/v02)"; exit 1; }
echo "$(date -u +%FT%TZ) E-031, motore $(git rev-parse --short HEAD 2>/dev/null || echo '?'), V027, --riprendi" >> "$LOG"
corsa() {   # braccio celle
  if ! python3 -B -m sim.v02.run valida "$DIR/$1/carte.json" --mazzi "$DIR/$1/mazzi.json" --variante V027 >> "$LOG" 2>&1; then
    echo "$(date -u +%FT%TZ) ERRORE $1: valida non passa (primitive di R-026?)" >> "$LOG"; return 1
  fi
  echo "$(date -u +%FT%TZ) inizio $1 forte:30 200 3400 $2" >> "$LOG"
  if E031_TRACCIA=$(cat "$DIR/$1/traccia.txt") bash "$DIR/lancia_e031.sh" "$1" forte:30 200 3400 "$2" >> "$LOG" 2>&1; then
    echo "$(date -u +%FT%TZ) fine $1" >> "$LOG"
  else
    echo "$(date -u +%FT%TZ) ERRORE $1" >> "$LOG"; return 1
  fi
}
corsa R1-2c 1-2,1-4,1-6  || exit 1     #  600 partite  ~2.2 h  riferimento delle celle r1
corsa A     p:2,4        || exit 1     # 1800 partite  ~6.5 h
corsa A-r5  2-5,4-5      || exit 1     #  400 partite  ~1.4 h
corsa A-r1  1-2,1-4      || exit 1     #  400 partite  ~1.4 h
corsa B     p:2,6        || exit 1     # 1800 partite  ~6.5 h
corsa B-r5  2-5,5-6      || exit 1
corsa B-r1  1-2,1-6      || exit 1
corsa C     p:2,6        || exit 1
corsa C-r5  2-5,5-6      || exit 1
corsa C-r1  1-2,1-6      || exit 1
touch "$OUT/FINE"
echo "$(date -u +%FT%TZ) fine E-031" >> "$LOG"
