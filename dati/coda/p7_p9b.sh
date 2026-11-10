#!/usr/bin/env bash
# R-027 (E-032) dopo E-033 e il braccio breccia: P7 Scudo, due bracci, poi P9b. Motore: worktree tcg_p7 (claude/r027-p7-contatori 44f97f0 = main + contatori dello Scudo, replay identici).
# P7: 12 incroci con un mazzo da ≥5 Scudo (tutti tranne 1-3, 1-6, 3-6) su B0c05 + rott_LDR05_2c in 1-5 e 2-5 (input di E-030 R5-2c),
#     forte:30, 200 partite, semi 3400+k; riferimento E-030 00_B0c05 e R5-2c (vince_pareggi).
# P9b: reazione_da_cicatrice_costo −1 sulle liste di E-031 A, incroci p:2,4, forte:30, 100 partite, semi 3400+k; riferimento E-031 A (prime 100).
RES=/home/claude/e020_res; C=$RES/dati/coda; OUTB=$RES/dati/E-032
mkdir -p $OUTB; LOG=$OUTB/avanzamento.log
log() { echo "$(date -u +%FT%TZ) $*" >> $LOG; }
until [ -f $RES/dati/E-033/FINE_BRECCIA ]; do sleep 300; done
pubblica() {  # braccio
  ( cd $RES && git add dati/E-032 && git commit -qm "E-032 (R-027): $1 forte (motore $(cd /home/claude/tcg_p7 && git rev-parse --short HEAD), V027)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QuaTVB8qUoSm5xLkGQbgcC";
    for w in 2 4 8 16 0; do git push -q -u origin dati/e020-v024-forte && { log "push $1 forte ok"; break; }; [ $w = 0 ] && log "PUSH FALLITO $1"; sleep $w; done )
  SH=/mnt/project-files/tcg/swarm/esperimenti/E-032_regole_in_prova
  if timeout 60 mkdir -p $SH 2>/dev/null && timeout 300 cp -r $OUTB/. $SH/ 2>/dev/null; then log "copia nella cartella condivisa ok ($1)"; else log "cartella condivisa non raggiungibile ($1): resta su git"; fi
}
corsa() {  # nome input variante partite celle
  if ! python3 -B -m sim.v02.run valida "$2/carte.json" --mazzi "$2/mazzi.json" --variante "$3" >> $LOG 2>&1; then log "ERRORE $1: valida non passa"; return 1; fi
  log "inizio $1 forte:30 $4 3400 $5"
  if bash $C/lancia_celle.sh "$2" "$3" "$OUTB/$1/F_s3400" forte:30 "$4" 3400 "$5" >> $LOG 2>&1; then log "fine $1"; pubblica "$1"
  else log "ERRORE $1"; return 1; fi
}
cd /home/claude/tcg_p7
log "E-032 R-027 P7 + P9b, motore $(git rev-parse --short HEAD), V027, --riprendi"
for a in oppone_senza_ruotarsi vince_pareggi_se_pronta; do
  corsa P7-$a    /home/claude/e033_in      $C/varianti/scudo_$a.json 200 -1-3,1-6,3-6 || exit 1
  corsa P7-$a-r5 /home/claude/e030_in/R5-2c $C/varianti/scudo_$a.json 200 1-5,2-5      || exit 1
done
corsa P9b /home/claude/e031_in/A $C/varianti/p9b_cicatrice_meno1.json 100 p:2,4 || exit 1
touch $OUTB/FINE; log "E-032 finita"; pubblica "fine"
