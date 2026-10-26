#!/usr/bin/env bash
# E-030 (Q-026, esito_passata2.md): bracci 00_B0c05, M2, M3, P-2c. Copiato da lancia_e029.sh; passa --riprendi.
# Da eseguire dalla radice della repo (dove c'e' sim/). Motore: 4e13d90 o successivo (preset V026, contatore R-017, --riprendi).
#
#   bash lancia_e030.sh <braccio> <ia> <partite_per_incrocio> <seed_base> <protagonisti|tutti>
#
#   seed_base     2000 semplice (uscita S), 3400 forte (uscita F_s3400; ogni seed_base diverso da 2000/3000 ha la sua cartella).
#   E030_VARIANTE facoltativa: preset o file JSON per --variante (default V026)
#   E030_OUT      facoltativa: cartella risultati (default tcg/swarm/esperimenti/E-030_q026)
#   E030_TRACCIA  facoltativa: ID per --traccia (ogni braccio ha il suo traccia.txt, con NEW-V05 e NEW-B06)
#   E030_RIPRENDI facoltativa: 0 per non passare --riprendi (default 1: un rilancio gioca solo le partite mancanti)
#   E030_RIFAI    facoltativa: 1 per rigiocare anche gli incroci già finiti (default: report presente e niente
#                 .partite_fatte.pkl = finito, si salta)
#   Le liste B0c05 non hanno mix_: niente braccio mix.
set -euo pipefail
B=$1; IA=$2; N=$3; SB=$4; PROT=$5
BASE=/mnt/project-files/tcg/set/esperimenti/E-030_q026; SRC=$BASE/$B
VAR=${E030_VARIANTE:-V026}
SUF=""; [ "$SB" != 2000 ] && [ "$SB" != 3000 ] && SUF="_s$SB"
OUT=${E030_OUT:-/mnt/project-files/tcg/swarm/esperimenti/E-030_q026}/$B/$( [ "$IA" = semplice ] && echo S || echo F )$SUF
TR=(); [ -n "${E030_TRACCIA:-}" ] && TR=(--traccia "$E030_TRACCIA")
[ "${E030_RIPRENDI:-1}" = 1 ] && TR+=(--riprendi)
[ -f "$SRC/carte.json" ] || { echo "$B: nessun carte.json"; exit 1; }
fatto() { [ "${E030_RIFAI:-0}" != 1 ] && ls "$1"/*_torneo_*.md > /dev/null 2>&1 && [ ! -f "$1/.partite_fatte.pkl" ]; }
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
