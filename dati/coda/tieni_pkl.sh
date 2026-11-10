#!/usr/bin/env bash
# Tiene i record per partita (posti G1/G2) delle celle F_s3400: run.py cancella .partite_fatte.pkl a fine cella.
while true; do
  for f in /home/claude/e020_res/dati/E-03[0-9]/*/F_s3400/*/.partite_fatte.pkl; do
    [ -f "$f" ] || continue
    r=${f#/home/claude/e020_res/dati/}; d=/home/claude/semi_keep/$(dirname "$r"); mkdir -p "$d"
    [ "$f" -ef "$d/partite.pkl" ] || ln -f "$f" "$d/partite.pkl"
  done
  sleep 60
done
