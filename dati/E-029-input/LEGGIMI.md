# E-029_c04: misura X del ciclo 04 (votata 8/8)

Data: 2026-10-26. Preparati dal programmatore dello swarm. Fonti: `tcg/swarm/cicli/ciclo-04/round1/punti_passata2.md` (punto 1 ed esito della passata 2) e la sezione "Passata 2" di `discussione_playtester_competitivo.md`, che contiene la lista di P-rott.

Sono solo dati, rigenerabili con `python3 -B genera_e029.py`. La base è B0c03 (`E-025_B0c02/A-FV_c02/`), che resta intatta. Il motore è **4e13d90**, con preset V026.

## Bracci

| Braccio | Cosa cambia rispetto a B0c03 | Protagonisti | Semi | Riferimento | Partite F | Ore stimate (4 core) |
|---|---|---|---|---|---|---|
| `P` | NEU-013 Forza 3 → 2; BLU-008 Forza 2 → 1; Base di LDR-05 senza testo (`base: []`). Testi invariati | 1, 5 | 3200+k | `E-028_c04/00_B0c03/F_s3200`, già giocato a 200, **non si rigioca** | 1.800 | ~6.5 |
| `00_B0c03` | nulla (riferimento, identico a quello di E-028) | 5 | 3300+k | — | 1.000 | ~3.6 |
| `P-rott` | P, più `rif_LDR05` con −3 NEU-013, −3 BLU-008, +2 ROS-003, +1 ROS-021, +1 BLU-012, +1 BLU-010, +1 BLU-001 | 5 | 3300+k | 00_B0c03 su 3300 | 1.000 | ~3.6 |
| `D05b-200` | Scudo tolto alle Unità di `rif_LDR05`: copie `D05B-*`, identiche a quelle di E-025 D05b_c02 | 5 | 3300+k | 00_B0c03 su 3300 | 1.000 | ~3.6 |
| `D-2M` | Scudo e Impeto tolti insieme alle Unità di `rif_LDR05`: copie `D2M-*`, 12 ID e 30 copie | 5 | 3300+k | 00_B0c03 su 3300 | 1.000 | ~3.6 |
| **Totale** | | | | | **5.800** | **~21** |

Le stime vengono dal ritmo di E-028 sulla stessa macchina: circa 13 s a partita su 4 core con `forte:30`. RB ha fatto 1.800 partite in 6.45 h, 00_B0c03 su 3300 ha fatto 500 partite in 1.81 h. Il piano stimava 21–23 h.

## Controlli
- **Liste.** Tutte le liste hanno 40 carte e rispettano i limiti di costruzione: al massimo 3 copie per ID e colori del Leader (`valida` dà 0 errori).
  - `rif_LDR05` in P, D05b-200 e D-2M: 32 Unità.
  - **P-rott:** 40 carte, **32 Unità, 12 copie con Scudo**, colori R 21 / B 19 / N 0, colore minore Blu al 47.5%. ROS-021, BLU-012, BLU-010 e BLU-001 arrivano a 3 copie, ROS-003 a 2. Le carte nerfate da P escono dalla lista, quindi di P in P-rott conta solo la Base vuota.
- **Diff campo per campo contro B0c03:**
  - P cambia solo `power` e `_note` di NEU-013 e BLU-008 e la `base` di LDR-05; i mazzi sono uguali. NEU-013 e BLU-008 fra i 6 `rif_*` stanno solo in `rif_LDR05`.
  - P-rott ha le stesse modifiche di P, più la sola `rif_LDR05` (le differenze sono quelle della tabella).
  - D05b-200 e D-2M non cambiano nessuna carta esistente né i Leader. Aggiungono solo le copie (`D05B-*` 6, `D2M-*` 12) e cambiano solo `rif_LDR05`.
  - D05b-200 ha le carte identiche a E-025 D05b_c02. Nei mazzi l'unica differenza è `rif_LDR06`, cioè la lista A-FV di B0c03.
- **Copie `D2M-*`:** tolte le parole chiave `scudo` e `impeto` e la statica di Forza dell'Impeto. Restano le altre abilità: BLU-001 tiene "Quando si oppone, +2", BLU-010 tiene Bracconiere 2, ROS-001 e ROS-023 tengono Assalto. Forza, costo, colore e rarità sono invariati. Senza Scudo e senza Impeto nella lista, la Base e il Risvegliato di LDR-05 non trovano più Unità a cui applicarsi.
- **Fumo** (motore 4e13d90, V026, LDR-01 contro LDR-05, seed 3):
  - tutti i bracci passano `valida` con 0 errori (120, 126 e 132 carte, 6 Leader) e la partita finisce con exit 0;
  - le partite di P, P-rott, D05b-200 e D-2M differiscono da quella del riferimento;
  - il lanciatore, con traccia e `--riprendi`, gioca 5 incroci di D-2M (`semplice 2 3300 5`) e al rilancio li salta;
  - la forte dà la stessa partita sullo stesso seed (provato due volte su 3304).

## Riferimento su 3300+k a 200 per incrocio
`--riprendi` non permette di estendere le 100 partite di B1. Il checkpoint `.partite_fatte.pkl` vive solo durante una corsa e il motore lo cancella quando la corsa finisce, quindi le 100 partite già giocate non sono più su disco.

Per questo il riferimento si **rigioca intero**: 200 partite per incrocio, circa 3.6 h, scritte in `tcg/swarm/esperimenti/E-029_c04/00_B0c03/F_s3300`. Le prime 100 partite di ogni incrocio hanno gli stessi semi di B1 e la forte è deterministica, quindi devono ridare esattamente B1: è un controllo gratuito.

Per non ripagare 1.8 h in futuro servirebbe nel motore un'opzione del tipo `--da-partita N`. È codice nuovo e la decisione spetta al thread principale.

## Traccia
È la stessa di E-028: R-012 e R-017, cioè LDR-01, LDR-05 e le 29 carte distinte di `rif_LDR01` e `rif_LDR05`, più le copie del braccio. Ogni cartella ha il suo `traccia.txt`:
- D05b-200 aggiunge `D05B-BLU-001, D05B-BLU-007, D05B-BLU-008, D05B-BLU-010, D05B-BLU-012, D05B-NEU-013`;
- D-2M aggiunge `D2M-BLU-001, D2M-BLU-007, D2M-BLU-008, D2M-BLU-010, D2M-BLU-012, D2M-NEU-013, D2M-ROS-001, D2M-ROS-005, D2M-ROS-015, D2M-ROS-020, D2M-ROS-021, D2M-ROS-023`.

## Lancio
Il comando parte dalla radice della repo al commit 4e13d90 o successivo:

```bash
nohup bash /mnt/project-files/tcg/set/esperimenti/E-029_c04/esegui_e029.sh > /dev/null 2>&1 &
```

- L'ordine è P, 00_B0c03 (3300), P-rott, D05b-200, D-2M.
- Lo stato si segue in `tcg/swarm/esperimenti/E-029_c04/avanzamento.log`, e alla fine compare `FINE`.
- Si può rilanciare dopo un'interruzione: gli incroci finiti si saltano e quello interrotto riprende da dove era.
- Un singolo braccio si lancia con `E029_TRACCIA=$(cat <braccio>/traccia.txt) bash lancia_e029.sh <braccio> forte:30 200 <3200|3300> <1,5|5>`.

## File
- `genera_e029.py`, `lancia_e029.sh` (copia di `lancia_e028.sh` con `--riprendi` e il salto degli incroci finiti), `esegui_e029.sh`;
- `00_B0c03/`, `P/`, `P-rott/`, `D05b-200/`, `D-2M/`, ognuna con `carte.json`, `mazzi.json`, `traccia.txt` e `LEGGIMI.md`.
