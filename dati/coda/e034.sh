#!/usr/bin/env bash
# E-034 (Q-031, ciclo 05 B): riferimento B0c06, bracci 00_B0c06 e tempra_tardo, 15 incroci x 200, forte:30, semi 3500+k.
# Richiesta del thread delle carte (2026-11-15), input 06af014 (dati/E-034-input) estratti in /home/claude/e034_in.
# Motore: worktree /home/claude/tcg_e034 = main 8ff53fc (tabelle R-028, R-026, P9b, Scudo, Brecce). Parte dopo E-032 (P9b).
# Uscita locale dati/E-034 (la cartella condivisa può cadere), poi commit, push e copia. I partite.pkl restano fuori da git.
RES=/home/claude/e020_res; IN=/home/claude/e034_in; OUTB=$RES/dati/E-034
mkdir -p $OUTB; LOG=$OUTB/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
until [ -f $RES/dati/E-032/FINE ]; do sleep 300; done
cd /home/claude/tcg_e034
for b in 00_B0c06 tempra_tardo; do
  if E034_OUT=$OUTB bash $IN/lancia_e034.sh $b forte:30 200 3500 tutti >> $LOG 2>&1; then
    ( cd $RES && git add dati/E-034 ':!*.pkl' && git commit -qm "E-034 (Q-031): $b forte, 15 incroci x 200, semi 3500 (motore $(cd /home/claude/tcg_e034 && git rev-parse --short HEAD), input 06af014)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
      for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push $b forte ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO $b"; sleep $w; done )
    SH=/mnt/project-files/tcg/swarm/esperimenti/E-034_B0c06
    if timeout 60 mkdir -p $SH 2>/dev/null && ( cd $OUTB && tar -cf - --exclude='*.pkl' . | timeout 600 tar -xf - -C $SH ) 2>/dev/null; then log "copia nella cartella condivisa ok ($b)"; else log "cartella condivisa non raggiungibile ($b): resta su git"; fi
  else log "ERRORE $b"; exit 1; fi
done
touch $OUTB/FINE; log "E-034 finita"
