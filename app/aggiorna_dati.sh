#!/bin/sh
# Copia nell'app il set e i mazzi in vigore dalla cartella condivisa del progetto.
# Serve solo per l'app pubblicata fuori dal cloud del progetto: lì la cartella condivisa non c'è
# e il server usa app/dati. Dopo la copia: commit e nuovo deploy.
set -e
SRC=${1:-/mnt/project-files/tcg/set/finale}
DST=$(dirname "$0")/dati
cp "$SRC/set_v02.json" "$SRC/mazzi_v02.json" "$DST/"
echo "copiati set_v02.json e mazzi_v02.json da $SRC"
