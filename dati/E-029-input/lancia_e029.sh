#!/usr/bin/env bash
# E-029 (ciclo 04, misura X): bracci 00_B0c03, P, P-rott, D05b-200, D-2M. Copiato da lancia_e028.sh; passa --riprendi.
# Da eseguire dalla radice della repo (dove c'e' sim/). Motore: 4e13d90 o successivo (preset V026, contatore R-017, --riprendi).
#
#   bash lancia_e029.sh <braccio> <ia> <partite_per_incrocio> <seed_base> <protagonisti|tutti> [mix]
#
#   seed_base     2000 semplice, 3000 forte (stessi indici di coppia di E-020/E-023/E-024/E-025);
#                 3200 = semi di P (stessi di E-028 parte A: il riferimento 00_B0c03 F_s3200 a 200 è già in tcg/swarm/esperimenti/E-028_c04): F_s3200.
#                 3300 = semi di P-rott, D05b-200, D-2M e del riferimento 00_B0c03 a 200 per incrocio: F_s3300.
#                 Ogni seed_base diverso da 2000/3000 scrive in una cartella a parte: <braccio>/F_s<seed_base> (o S_s<seed_base>).
#   E029_VARIANTE facoltativa: preset o file JSON per --variante (default V026)
#   E029_OUT      facoltativa: cartella risultati (default tcg/swarm/esperimenti/E-029_c04)
#   E029_TRACCIA  facoltativa: ID per --traccia (ogni braccio ha il suo traccia.txt, con le copie D05B-* e D2M-*)
#   E029_RIPRENDI facoltativa: 0 per non passare --riprendi (default 1: ogni partita finita resta su disco, un rilancio gioca solo le mancanti)
#   E029_RIFAI    facoltativa: 1 per rigiocare anche gli incroci già finiti (default: un incrocio con il report e senza
#                 .partite_fatte.pkl è finito e si salta, così un rilancio dello script non ripete il lavoro fatto)
#   mix           se presente: anche mix_M3_thorn_lucchetto (serve mazzi_mix_M3.json nel braccio; i bracci E-029 non lo hanno)
set -euo pipefail
B=$1; IA=$2; N=$3; SB=$4; PROT=$5; MIX=${6:-}
BASE=/mnt/project-files/tcg/set/esperimenti/E-029_c04; SRC=$BASE/$B
VAR=${E029_VARIANTE:-V026}
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=${E029_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-029_c04}/$B/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(); [ -n "${E029_TRACCIA:-}" ] && TR=(--traccia "$E029_TRACCIA")
[ "${E029_RIPRENDI:-1}" = 1 ] && TR+=(--riprendi)
[ -f "$SRC/carte.json" ] || { echo "$B: nessun carte.json"; exit 1; }
fatto() { [ "${E029_RIFAI:-0}" != 1 ] && ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
DK=(x rif_LDR01_puntata_e_preda rif_LDR02_muro_di_parata rif_LDR03_sanguinare_per_accendere
    rif_LDR04_stanca_e_smonta rif_LDR05_scudi_armati rif_LDR06_ferite_e_caccia)
tocca() { [ "$PROT" = tutti ] && return 0; for p in ${PROT//,/ }; do [ "$p" = "$1" ] || [ "$p" = "$2" ] && return 0; done; return 1; }
k=0
for i in 1 2 3 4 5 6; do for j in $(seq $((i+1)) 6); do
  k=$((k+1)); tocca $i $j || continue
  if fatto "$OUT/L$i-L$j"; then echo "$B $IA L$i-L$j gia' fatto, salto"; continue; fi
  python3 -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
    --mazzi "$SRC/mazzi.json#${DK[$i]}" "$SRC/mazzi.json#${DK[$j]}" \
    --partite 0 --incroci "$N" --seed $((SB+k)) --ia "$IA" "${TR[@]}" --out "$OUT/L$i-L$j" > /dev/null
  echo "$B $IA L$i-L$j seed $((SB+k)) fatto"
done; done
if [ -n "$MIX" ]; then
  [ -f "$SRC/mazzi_mix_M3.json" ] || { echo "$B: manca mazzi_mix_M3.json"; exit 1; }
  for o in 1 2 3 5 6; do
    if fatto "$OUT/M3-L$o"; then echo "$B $IA M3-L$o gia' fatto, salto"; continue; fi
    python3 -m sim.v02.run torneo --variante "$VAR" --carte "$SRC/carte.json" \
      --mazzi "$SRC/mazzi.json#${DK[$o]}" "$SRC/mazzi_mix_M3.json#mix_M3_thorn_lucchetto" \
      --partite 0 --incroci "$N" --seed $((SB+20+o)) --ia "$IA" "${TR[@]}" --out "$OUT/M3-L$o" > /dev/null
    echo "$B $IA M3-L$o seed $((SB+20+o)) fatto"
  done
fi
