# E-027_c03: bracci del ciclo 03 (Q-023, i due Leader rossi)

Data: 2026-10-19. Preparati dal programmatore dello swarm. Sono solo dati, rigenerabili con `python3 -B genera_e027.py`.

**Base (B0c03).** È `tcg/set/esperimenti/E-025_B0c02/A-FV_c02/` (`carte.json`, `mazzi.json`), che resta intatta. Ogni braccio ha un `carte.json` e un `mazzi.json` completi: le 6 liste `rif_*`, ciascuna di 40 carte.

| Braccio | Cosa cambia rispetto a B0c03 | Proponenti | Si misura contro |
|---|---|---|---|
| `00_B0c03` | nulla: copia di A-FV_c02, così il lanciatore copre anche il riferimento | — | — |
| `R20` | ROS-020: Forza 4 → 3, testo invariato (`power`, `vanilla_delta` −1, `_note`) | critico, rosso, competitivo, ponti | 00_B0c03 |
| `R21` | ROS-021: "Impeto 1: +3" → "Impeto 2: +3" (`abilities[0].if` `pugno_ge` 2, `text`, `_note`) | blu, rosso, verde | 00_B0c03 |
| `B5` | Base di LDR-05: "…se nell'impegno hai almeno **2** gemme" (`base[0].if` `pugno_ge` 2, `text`) | blu (L2), rosso (leva 3) | 00_B0c03 |
| `K-rott` | Carte di B0c03; `rif_LDR05_scudi_armati`: −3 ROS-020, +1 ROS-021 (da 2 a 3), +2 ROS-003 (da 0 a 2) | critico, competitivo | 00_B0c03 (e R20 per la regola di rottura) |
| `C` | R20 + R21 | combinazione (si lancia solo se lo dice la regola) | 00_B0c03 |

**Liste toccate.**
- ROS-020 è solo in `rif_LDR05` (×3).
- ROS-021 è in `rif_LDR01` ×2 e in `rif_LDR05` ×2, quindi R21 e C cambiano entrambi i mazzi rossi.
- ROS-003 era solo in `rif_LDR01` (×2).
- In K-rott la ROS-020 esce del tutto dalla lista di LDR-05, quindi la sua Forza non conta. Con le carte di R20 il braccio sarebbe identico.
- I colori di LDR-05 non cambiano in nessun braccio (R 18, B 19).

**B5.** Usa la condizione `pugno_ge` che il motore ha già: non serve nessuna primitiva nuova.

**Diff.** Ho confrontato ogni braccio con B0c03 campo per campo, escludendo solo `version`, `note`, `set`, `autore`, `data` e `nota`. Ogni braccio cambia soltanto i campi della tabella qui sopra.

**Validazione.**
- Validatore sul motore 8e9290a (`sim/v02`, `python3 -m sim.v02.run valida`): ogni braccio ha 120 carte, 6 Leader e 0 errori, e ogni lista ha 40 carte.
- Partita di fumo con `--variante V026`, LDR-01 contro LDR-05, seed 1: exit 0 su tutti i bracci.
- R20 è stato controllato anche sui seed 2–5 contro Vey, perché nella partita del seed 1 ROS-020 non esce. Dove ROS-020 entra in gioco, la partita cambia; dove non entra, la partita è identica.
- Lanciatore: prova con `K-rott semplice 2 3100 5`, 5 incroci e `--traccia` attivo.

**Lancio.**

```bash
E027_TRACCIA=<ID> bash /mnt/project-files/tcg/set/esperimenti/E-027_c03/lancia_e027.sh <braccio> <semplice|forte:30> <N> <2000|3000|3100> <protagonisti|tutti>
```

- Il preset di default è V026.
- I risultati vanno in `tcg/swarm/esperimenti/E-027_c03/<braccio>/<S|F>[_s<seed_base>]/L<i>-L<j>/`.
- `seed_base 3100` è il secondo blocco di semi della forte (seed 3101–3115). Non si sovrappone a 3000+k né a 3020+o, e scrive in `F_s3100`, così non si mescola con il blocco 3000.
