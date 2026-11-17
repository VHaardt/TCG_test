#!/usr/bin/env bash
# E-037 (ciclo 05, voto lampo 8/8): leve dure H5-t, H5-v, H5-r, H6-v, H6-c, 100 partite, semi 3700+k, V027 + A, forte:30.
# Input 3e4dbf0 (dati/E-037-input) estratti in /home/claude/e037_in. Motore: worktree /home/claude/tcg_e037 = 612057d (R-031 + R-032).
# Parte quando questo container ha finito E-036 (dati/E-036/FINE_A). Un braccio con dati/E-037/<braccio>.esterno gira altrove.
RES=/home/claude/e020_res; IN=/home/claude/e037_in; OUTB=$RES/dati/E-037; W=/home/claude/tcg_e037
mkdir -p $OUTB; LOG=$OUTB/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
until [ -f $RES/dati/E-036/FINE_A ]; do sleep 60; done
for b in H5-t H5-v H5-r H6-v H6-c; do
  [ -f $OUTB/$b.esterno ] && { log "$b in un'altra sessione: salto"; continue; }
  grep -q "push $b " $LOG 2>/dev/null && continue
  if (cd $W && E037_OUT=$OUTB bash $IN/lancia_e037.sh $b forte:30 100 3700 >> $LOG 2>&1); then
    ( cd $RES && git ls-files -o -m --exclude-standard dati/E-037 | grep -v '\.pkl$' | xargs -r git add && git commit -qm "E-037 (ciclo 05): $b forte, 100 partite, semi 3700 (motore 612057d, input 3e4dbf0)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
      for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push $b forte ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO $b"; sleep $w; done )
    SH=/mnt/project-files/tcg/swarm/esperimenti/E-037_leve_dure
    if timeout 60 mkdir -p $SH 2>/dev/null && ( cd $OUTB && tar -cf - --exclude='*.pkl' . | timeout 600 tar -xf - -C $SH ) 2>/dev/null; then log "copia nella cartella condivisa ok ($b)"; else log "cartella condivisa non raggiungibile ($b): resta su git"; fi
  else log "ERRORE $b"; exit 1; fi
done
touch $OUTB/FINE_QUI; log "E-037: bracci di questa sessione finiti"
