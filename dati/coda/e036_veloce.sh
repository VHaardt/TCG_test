#!/usr/bin/env bash
# E-036 accelerata (richiesta di Vittorio 2026-11-17: finire entro oggi). Sostituisce e036.sh ed e036_r031.sh dopo L6-ab.
# Qui: chiude L6-ab (lanciato da e036.sh), poi L5-c su R-031 (tcg_e036b 3ce9705), poi, se nessun'altra sessione li ha presi,
# L6-ad (tcg_e036b) e L5-b (tcg_e034 8ff53fc). Un braccio con il file dati/E-036/<braccio>.esterno gira altrove e qui si salta.
RES=/home/claude/e020_res; IN=/home/claude/e036_in; OUTB=$RES/dati/E-036
LOG=$OUTB/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
salva() {   # braccio motore
  ( cd $RES && git ls-files -o -m --exclude-standard dati/E-036 | grep -v '\.pkl$' | xargs -r git add && git commit -qm "E-036 (ciclo 05): $1 forte, semi 3700 (motore $2, input 2a2cec8)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
    for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push $1 forte ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO $1"; sleep $w; done )
  SH=/mnt/project-files/tcg/swarm/esperimenti/E-036_vaglio
  if timeout 60 mkdir -p $SH 2>/dev/null && ( cd $OUTB && tar -cf - --exclude='*.pkl' . | timeout 600 tar -xf - -C $SH ) 2>/dev/null; then log "copia nella cartella condivisa ok ($1)"; else log "cartella condivisa non raggiungibile ($1): resta su git"; fi
}
# L6-ab: aspetta la fine (se il container riparte, lo rilancia da qui)
if ! grep -q "push L6-ab " $LOG; then
  if ! grep -q "fine L6-ab " $LOG; then
    if ! pgrep -f "lancia_e036.sh L6-ab" > /dev/null; then (cd /home/claude/tcg_e034 && E036_OUT=$OUTB bash $IN/lancia_e036.sh L6-ab forte:30 200 3700 >> $LOG 2>&1); fi
    until grep -q "fine L6-ab " $LOG; do sleep 60; done
  fi
  salva L6-ab 8ff53fc
fi
for b in L5-c L6-ad L5-b; do
  [ -f $OUTB/$b.esterno ] && { log "$b gira in un'altra sessione: salto"; continue; }
  grep -q "push $b " $LOG && continue
  if [ $b = L5-b ]; then W=/home/claude/tcg_e034; else W=/home/claude/tcg_e036b; fi
  if (cd $W && E036_OUT=$OUTB bash $IN/lancia_e036.sh $b forte:30 200 3700 >> $LOG 2>&1); then salva $b "$(cd $W && git rev-parse --short HEAD)"; else log "ERRORE $b"; exit 1; fi
done
touch $OUTB/FINE_A; log "E-036: bracci di questa sessione finiti"
