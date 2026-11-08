#!/usr/bin/env bash
# E-030, bracci restanti dopo il reset del container dell'8/11 (R5-2c da capo, M1, P-2c). Motore ab6f2dd, V026.
SC=/tmp/claude-0/-home-claude-tcg-test/0dd8df74-caeb-587a-b35a-4fd045d93fa9/scratchpad
RES=/home/claude/e020_res; IN=/home/claude/e030_in; LOG=$RES/dati/E-030/avanzamento.log
export E030_OUT=$RES/dati/E-030
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
pubblica() {  # messaggio braccio uscita
  ( cd $RES && git add dati/E-030 && git commit -qm "E-030: $1 (motore ab6f2dd, V026)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
    for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push $1 ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO $1"; sleep $w; done )
  SH=/mnt/project-files/tcg/swarm/esperimenti/E-030_q026
  if timeout 60 mkdir -p $SH/$2 2>/dev/null && timeout 300 cp -r $RES/dati/E-030/$2/. $SH/$2/ 2>/dev/null && timeout 30 cp $LOG $SH/ 2>/dev/null; then log "copia nella cartella condivisa ok ($1)"; else log "cartella condivisa non raggiungibile ($1): resta su git"; fi
}
run() {  # braccio ia N seed prot
  log "inizio $*"
  if E030_TRACCIA=$(cat $IN/$1/traccia.txt) bash $SC/lancia_e030_loc.sh "$@" >> $LOG 2>&1; then log "fine $1 $2 $4"; else log "ERRORE $*"; return 1; fi
}
cd /home/claude/tcg_e030
log "ripresa dopo il reset del container (R5-2c da capo), motore $(git rev-parse --short HEAD)"
run R5-2c forte:30 200 3400 5 && pubblica "R5-2c forte" R5-2c
run M1 forte:30 200 3400 3,6 && pubblica "M1 forte" M1
run P-2c forte:30 200 3400 1,5 && pubblica "P-2c forte" P-2c
touch $RES/dati/E-030/FINE; log "E-030 finita"
