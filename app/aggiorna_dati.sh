#!/bin/sh
# Copia nell'app il set e i mazzi in vigore dalla cartella condivisa del progetto.
# Serve solo per l'app pubblicata fuori dal cloud del progetto: lì la cartella condivisa non c'è
# e il server usa app/dati. Dopo la copia: commit e nuovo deploy.
set -e
SRC=${1:-/mnt/project-files/tcg/set/finale}
B0C05=${2:-/mnt/project-files/tcg/swarm/questioni/Q-026_feedback_playtest/liste_B0c05/mazzi.json}
DST=$(dirname "$0")/dati
cp "$SRC/set_v02.json" "$SRC/mazzi_v02.json" "$DST/"
cp "$B0C05" "$DST/mazzi_B0c05.json"
echo "copiati set_v02.json e mazzi_v02.json da $SRC, mazzi_B0c05.json da $B0C05"
