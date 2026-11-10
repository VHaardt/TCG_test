#!/usr/bin/env bash
# E-033 braccio breccia (Q-028 V3) dopo allo_scoperto e prima di R-027. Input dati/E-033-input a 4ec9ad2 (/home/claude/e033b_in),
# motore tcg_p7 (claude/r027-p7-contatori: main + contatori in sola lettura, con le Brecce per carta; replay identici).
RES=/home/claude/e020_res; IN=/home/claude/e033b_in
export E033_OUT=$RES/dati/E-033; LOG=$E033_OUT/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
until [ -f $RES/dati/E-033/FINE ]; do sleep 300; done
cd /home/claude/tcg_p7
if ! python3 -B -m sim.v02.run valida "$IN/breccia/carte.json" --mazzi "$IN/breccia/mazzi.json" --variante V027 >> $LOG 2>&1; then log "ERRORE breccia: valida non passa"; exit 1; fi
if bash $IN/lancia_e033.sh breccia forte:30 100 3400 tutti >> $LOG 2>&1; then
  log "fine braccio breccia"
  ( cd $RES && git add dati/E-033 && git commit -qm "E-033: breccia forte (motore $(git -C /home/claude/tcg_p7 rev-parse --short HEAD), V027)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
    for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push breccia forte ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO breccia"; sleep $w; done )
  SH=/mnt/project-files/tcg/swarm/esperimenti/E-033_ritmo
  if timeout 60 mkdir -p $SH 2>/dev/null && timeout 300 cp -r $E033_OUT/. $SH/ 2>/dev/null; then log "copia nella cartella condivisa ok (breccia)"; else log "cartella condivisa non raggiungibile (breccia): resta su git"; fi
  touch $RES/dati/E-033/FINE_BRECCIA
else log "ERRORE breccia"; exit 1; fi
