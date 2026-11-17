#!/usr/bin/env bash
# E-038, celle di L5 in questo container (combinazione finale H5-v+H6-v, conferma del thread delle carte 15:45 UTC), dopo e038_qui.sh.
RES=/home/claude/e020_res; OUTB=$RES/dati/E-038; LOG=$OUTB/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
salva() {
  ( cd $RES && git ls-files -o -m --exclude-standard dati/E-038 | grep -v '\.pkl$' | xargs -r git add && git commit -qm "E-038: $1 (motore 612057d, input d770cbf)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
    for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push $1 ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO $1"; sleep $w; done )
}
until [ -f $OUTB/FINE_L6_QUI ]; do sleep 60; done
cd /home/claude/tcg_e037
export E038_IN=/home/claude/e038_in E038_OUT=$OUTB
bash $RES/dati/coda/e038_celle.sh H5-v+H6-v conA L5-L6 >> $LOG 2>&1 && salva "H5-v+H6-v conA L5-L6" || { log "ERRORE conA L5-L6"; exit 1; }
bash $RES/dati/coda/e038_celle.sh H5-v+H6-v senzaA L3-L5 L4-L5 L5-L6 >> $LOG 2>&1 && salva "H5-v+H6-v senzaA L3-L5 L4-L5 L5-L6" || { log "ERRORE senzaA L5"; exit 1; }
touch $OUTB/FINE_QUI; log "E-038: celle di questo container finite"
