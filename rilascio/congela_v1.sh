#!/bin/sh
# Congela il set della 1.0: copia set, mazzi e nomi da set/finale in set/v1.0, controlla tutto con
# `valida`, scrive le impronte SHA-256 e aggiorna app/dati. Non cambia regole né carte.
# Uso: rilascio/congela_v1.sh con_A|senza_A   (dall'esito del voto di Tempra 3 nel ciclo 05)
set -e
SCELTA=${1:?"serve con_A o senza_A"}
RADICE=$(cd "$(dirname "$0")/.." && pwd)
REGOLE="$RADICE/rilascio/regole_v1_$SCELTA.json"
[ -f "$REGOLE" ] || { echo "regole sconosciute: $REGOLE"; exit 1; }
TCG=${TCG:-/mnt/project-files/tcg}
SRC="$TCG/set/finale"
DST="$TCG/set/v1.0"
mkdir -p "$DST"
cp "$SRC/set_v02.json" "$DST/set_v1.0.json"
cp "$SRC/mazzi_v02.json" "$DST/mazzi_v1.0.json"
cp "$TCG/set/nomi/nomi_v02.json" "$DST/nomi_v1.0.json"
[ -f "$SRC/set_v02.xlsx" ] && cp "$SRC/set_v02.xlsx" "$DST/set_v1.0.xlsx"
[ -f "$SRC/set_v02.csv" ] && cp "$SRC/set_v02.csv" "$DST/set_v1.0.csv"
cp "$REGOLE" "$DST/regole_v1.0.json"
# Rarità della 1.0 = scala C/R/E/L di Q-026 V2 (in nomi_v02.json). Solo etichette: nessun numero cambia,
# e l'unica Leggendaria (limite di 1 copia) è la stessa nei due file.
python3 - "$DST/set_v1.0.json" "$DST/nomi_v1.0.json" <<'PY'
import json, sys
p, q = sys.argv[1], sys.argv[2]
s = json.load(open(p, encoding="utf-8")); r = json.load(open(q, encoding="utf-8"))["rarita"]
mancano = [c["id"] for c in s["cards"] if c["id"] not in r]
if mancano:
    sys.exit(f"carte senza rarità in nomi: {mancano}")
cambiate = sum(c.get("rarity") != r[c["id"]] for c in s["cards"])
for c in s["cards"]:
    c["rarity"] = r[c["id"]]
s["version"] = "1.0"
json.dump(s, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"rarità C/R/E/L allineate a nomi_v1.0.json: {cambiate} etichette cambiate")
PY
cd "$RADICE"
python3 -m sim.v02.run valida "$DST/set_v1.0.json" --mazzi "$DST/mazzi_v1.0.json" --variante "$DST/regole_v1.0.json" | tee "$DST/valida.txt"
( cd "$DST" && sha256sum set_v1.0.json mazzi_v1.0.json nomi_v1.0.json regole_v1.0.json > SHA256SUMS )
sh app/aggiorna_dati.sh "$SRC"
cp "$REGOLE" app/dati/regole_v1.0.json
echo "set congelato in $DST ($(git rev-parse --short HEAD)); app/dati aggiornata."
echo "Prossimi passi: rilascio/LEGGIMI.md, punti 3-6."
