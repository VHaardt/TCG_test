#!/usr/bin/env bash
# E-035 (Q-031, ciclo 05 D): le 4 mix_ a 2 copie contro le 6 rif_ di B0c06, 24 incroci x 200, forte:30, V027, semi 3600+k.
# Richiesta del thread delle carte (2026-11-15), input 7ed91c5 (dati/E-035-input) estratti in /home/claude/e035_in.
# Motore: worktree /home/claude/tcg_e034 = main 8ff53fc. Parte dopo E-034 (dati/E-034/FINE).
# Uscita locale dati/E-035, poi commit, push e copia. I partite.pkl restano fuori da git (lista esplicita: con ':!*.pkl' git 2.43 non aggiunge i file nuovi).
RES=/home/claude/e020_res; IN=/home/claude/e035_in; OUTB=$RES/dati/E-035
mkdir -p $OUTB; LOG=$OUTB/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
until [ -f $RES/dati/E-034/FINE ]; do sleep 300; done
cd /home/claude/tcg_e034
if E035_OUT=$OUTB bash $IN/lancia_e035.sh forte:30 200 3600 tutti >> $LOG 2>&1; then
  ( cd $RES && git ls-files -o -m --exclude-standard dati/E-035 | grep -v '\.pkl$' | xargs -r git add && git commit -qm "E-035 (Q-031): mix_ a 2 copie contro B0c06, 24 incroci x 200, semi 3600 (motore $(cd /home/claude/tcg_e034 && git rev-parse --short HEAD), input 7ed91c5)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
    for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push E-035 forte ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO E-035"; sleep $w; done )
  SH=/mnt/project-files/tcg/swarm/esperimenti/E-035_mix
  if timeout 60 mkdir -p $SH 2>/dev/null && ( cd $OUTB && tar -cf - --exclude='*.pkl' . | timeout 600 tar -xf - -C $SH ) 2>/dev/null; then log "copia nella cartella condivisa ok"; else log "cartella condivisa non raggiungibile: resta su git"; fi
else log "ERRORE E-035"; exit 1; fi
touch $OUTB/FINE; log "E-035 finita"
