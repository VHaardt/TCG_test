#!/usr/bin/env bash
# E-031 (Q-027) dopo E-030. Motore: main (R-027 incluso, replay identici ad ad77242), V027, input dati/E-031-input al 54caf2a.
SC=/tmp/claude-0/-home-claude-tcg-test/0dd8df74-caeb-587a-b35a-4fd045d93fa9/scratchpad
RES=/home/claude/e020_res; IN=/home/claude/e031_in
export E031_OUT=$RES/dati/E-031
mkdir -p $E031_OUT; LOG=$E031_OUT/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
until [ -f $RES/dati/E-030/FINE ]; do sleep 300; done
pubblica() {  # messaggio braccio
  ( cd $RES && git add dati/E-031 && git commit -qm "E-031: $1 (motore $(cd /home/claude/tcg_e031 && git rev-parse --short HEAD), V027)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
    for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push $1 ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO $1"; sleep $w; done )
  SH=/mnt/project-files/tcg/swarm/esperimenti/E-031_q027
  if timeout 60 mkdir -p $SH 2>/dev/null && timeout 300 cp -r $E031_OUT/. $SH/ 2>/dev/null; then log "copia nella cartella condivisa ok ($1)"; else log "cartella condivisa non raggiungibile ($1): resta su git"; fi
}
corsa() {  # braccio celle
  if ! python3 -B -m sim.v02.run valida "$IN/$1/carte.json" --mazzi "$IN/$1/mazzi.json" --variante V027 >> $LOG 2>&1; then
    log "ERRORE $1: valida non passa"; return 1
  fi
  log "inizio $1 forte:30 200 3400 $2"
  if E031_TRACCIA=$(cat $IN/$1/traccia.txt) bash $SC/lancia_e031_loc.sh "$1" forte:30 200 3400 "$2" >> $LOG 2>&1; then
    log "fine $1"; pubblica "$1 forte"
  else log "ERRORE $1"; return 1; fi
}
cd /home/claude/tcg_e031
log "E-031 (R-026, input 54caf2a), motore $(git rev-parse --short HEAD), V027, --riprendi"
corsa R1-2c 1-2,1-4,1-6 || exit 1
corsa A     p:2,4       || exit 1
corsa A-r5  2-5,4-5     || exit 1
corsa A-r1  1-2,1-4     || exit 1
corsa B     p:2,6       || exit 1
corsa B-r5  2-5,5-6     || exit 1
corsa B-r1  1-2,1-6     || exit 1
corsa C     p:2,6       || exit 1
corsa C-r5  2-5,5-6     || exit 1
corsa C-r1  1-2,1-6     || exit 1
touch $E031_OUT/FINE; log "E-031 finita"; pubblica "fine"
