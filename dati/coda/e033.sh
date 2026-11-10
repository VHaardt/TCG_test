#!/usr/bin/env bash
# E-033 (R-028, Q-028) dopo E-031: vaglio delle leve di ritmo. Motore: main 636e83e (worktree tcg_main), input dati/E-033-input a e9b7dcd.
# Ordine chiesto dal thread delle carte (2026-11-10): 00_rif (base rigiocata, prime 100 partite), bruciare, tempra_tardo, allo_scoperto.
RES=/home/claude/e020_res; IN=/home/claude/e033_in
export E033_OUT=$RES/dati/E-033
mkdir -p $E033_OUT; LOG=$E033_OUT/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
until [ -f $RES/dati/E-031/FINE ]; do sleep 300; done
pubblica() {  # braccio
  ( cd $RES && git add dati/E-033 && git commit -qm "E-033: $1 forte (motore $(cd /home/claude/tcg_main && git rev-parse --short HEAD), V027)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
    for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push $1 forte ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO $1"; sleep $w; done )
  SH=/mnt/project-files/tcg/swarm/esperimenti/E-033_ritmo
  if timeout 60 mkdir -p $SH 2>/dev/null && timeout 300 cp -r $E033_OUT/. $SH/ 2>/dev/null; then log "copia nella cartella condivisa ok ($1)"; else log "cartella condivisa non raggiungibile ($1): resta su git"; fi
}
corsa() {  # braccio
  V=V027; [ "$1" != 00_rif ] && V=$IN/varianti/$1.json
  if ! python3 -B -m sim.v02.run valida "$IN/carte.json" --mazzi "$IN/mazzi.json" --variante "$V" >> $LOG 2>&1; then
    log "ERRORE $1: valida non passa"; return 1
  fi
  if bash $IN/lancia_e033.sh "$1" forte:30 100 3400 tutti >> $LOG 2>&1; then
    log "fine braccio $1"; pubblica "$1"
  else log "ERRORE $1"; return 1; fi
}
cd /home/claude/tcg_main
log "E-033 (R-028, input e9b7dcd), motore $(git rev-parse --short HEAD), V027, --riprendi"
for b in 00_rif bruciare tempra_tardo allo_scoperto; do corsa $b || exit 1; done
touch $E033_OUT/FINE; log "E-033 finita"; pubblica "fine"
