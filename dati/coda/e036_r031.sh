#!/usr/bin/env bash
# E-036, bracci L5-c e L6-ad (servono le condizioni di R-031), stessi semi 3700+k degli altri bracci.
# Motore: worktree /home/claude/tcg_e036b = claude/r031-primitive 3ce9705 (PR #30; replay identici a main 8ff53fc).
# Parte dopo gli altri bracci di E-036 (dati/E-036/FINE_A).
RES=/home/claude/e020_res; IN=/home/claude/e036_in; OUTB=$RES/dati/E-036
mkdir -p $OUTB; LOG=$OUTB/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
until [ -f $OUTB/FINE_A ]; do sleep 300; done
cd /home/claude/tcg_e036b
for b in L5-c L6-ad; do
  if E036_OUT=$OUTB bash $IN/lancia_e036.sh $b forte:30 200 3700 >> $LOG 2>&1; then
    ( cd $RES && git ls-files -o -m --exclude-standard dati/E-036 | grep -v '\.pkl$' | xargs -r git add && git commit -qm "E-036 (ciclo 05): $b forte, semi 3700 (motore $(cd /home/claude/tcg_e036b && git rev-parse --short HEAD) = R-031, input 2a2cec8)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
      for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push $b forte ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO $b"; sleep $w; done )
    SH=/mnt/project-files/tcg/swarm/esperimenti/E-036_vaglio
    if timeout 60 mkdir -p $SH 2>/dev/null && ( cd $OUTB && tar -cf - --exclude='*.pkl' . | timeout 600 tar -xf - -C $SH ) 2>/dev/null; then log "copia nella cartella condivisa ok ($b)"; else log "cartella condivisa non raggiungibile ($b): resta su git"; fi
  else log "ERRORE $b"; exit 1; fi
done
touch $OUTB/FINE; log "E-036 finita"
