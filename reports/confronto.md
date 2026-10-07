# Esperimento A/B appaiato

- Base: `default`; varianti: `V1b` = `V1b_per_attack`, `fissa` = `sim/varianti/esempio_parata_fissa.json`
- IA: semplice; mazzi: arden_rosso_verde, maera_blu_nero, thorn_verde_blu, vey_nero_rosso; 50 partite per abbinamento, posti alternati
- Partite per configurazione: 500; seed base 1; versione carte `cd97544c8d`
- Stesse partite (abbinamenti, posti, seed) per base e varianti. Tra parentesi: IC 95%.
- Verdetto rispetto all'obiettivo: **dentro** (tutto l'IC nell'obiettivo), **fuori** (tutto l'IC fuori), **incerto**.

## V1b contro base

| Metrica | Obiettivo | Base | Variante | Differenza | Verdetto base | Verdetto variante |
|---|---|---|---|---|---|---|
| Durata mediana (turni) | 8–10 | 10.0 [10.0–10.0] | 10.0 [10.0–11.0] | +0.0 [+0.0, +1.0] | dentro | incerto |
| Partite tra 5 e 15 turni | 90–100% | 100.0% [99.2–100.0] | 99.2% [98.0–99.7] | -0.8 [-1.6, -0.0] punti | dentro | dentro |
| Partite al turno 13 | 0–10% | 9.8% [7.5–12.7] | 18.0% [14.9–21.6] | +8.2 [+3.9, +12.5] punti | incerto | fuori |
| Clessidra attiva a fine partita | 0–15% | 70.8% [66.7–74.6] | 72.2% [68.1–75.9] | +1.4 [-4.2, +7.0] punti | fuori | fuori |
| Partite oltre il turno 15 | 0–2% | 0.0% [0.0–0.8] | 0.8% [0.3–2.0] | +0.8 [+0.0, +1.6] punti | dentro | incerto |
| Vittorie del primo giocatore | 48–52% | 64.8% [60.5–68.9] | 64.6% [60.3–68.7] | -0.2 [-6.1, +5.7] punti | fuori | fuori |
| Rimonte | 20–35% | 26.3% [20.3–33.4] | 26.4% [20.5–33.2] | +0.1 [-9.1, +9.3] punti | dentro | dentro |
| Attacchi al Leader fermati da reazione | 30–45% | 23.7% [22.7–24.7] | 34.3% [33.3–35.4] | +10.7 [+9.2, +12.1] punti | fuori | dentro |
| Partite chiuse dal Crepuscolo | 0–15% | 0.4% [0.1–1.4] | 1.6% [0.8–3.1] | +1.2 [-0.0, +2.4] punti | dentro | dentro |
| Rimarginare usato quando possibile | 0–70% | 33.0% [31.5–34.6] | 31.4% [29.8–32.9] | -1.7 [-3.9, +0.5] punti | dentro | dentro |
| Scarto di vittorie tra mazzi | piccolo | 26 punti | 35 punti | | | |
| Vite perse da attacchi del Leader | <40% | 4% | 5% | | | |

## fissa contro base

| Metrica | Obiettivo | Base | Variante | Differenza | Verdetto base | Verdetto variante |
|---|---|---|---|---|---|---|
| Durata mediana (turni) | 8–10 | 10.0 [10.0–10.0] | 10.0 [10.0–10.0] | +0.0 [+0.0, +0.0] | dentro | dentro |
| Partite tra 5 e 15 turni | 90–100% | 100.0% [99.2–100.0] | 100.0% [99.2–100.0] | +0.0 [+0.0, +0.0] punti | dentro | dentro |
| Partite al turno 13 | 0–10% | 9.8% [7.5–12.7] | 9.8% [7.5–12.7] | +0.0 [-3.7, +3.7] punti | incerto | incerto |
| Clessidra attiva a fine partita | 0–15% | 70.8% [66.7–74.6] | 70.6% [66.5–74.4] | -0.2 [-5.8, +5.4] punti | fuori | fuori |
| Partite oltre il turno 15 | 0–2% | 0.0% [0.0–0.8] | 0.0% [0.0–0.8] | +0.0 [+0.0, +0.0] punti | dentro | dentro |
| Vittorie del primo giocatore | 48–52% | 64.8% [60.5–68.9] | 65.0% [60.7–69.1] | +0.2 [-5.7, +6.1] punti | fuori | fuori |
| Rimonte | 20–35% | 26.3% [20.3–33.4] | 26.3% [20.3–33.4] | +0.0 [-9.3, +9.3] punti | dentro | dentro |
| Attacchi al Leader fermati da reazione | 30–45% | 23.7% [22.7–24.7] | 23.5% [22.5–24.5] | -0.2 [-1.6, +1.2] punti | fuori | fuori |
| Partite chiuse dal Crepuscolo | 0–15% | 0.4% [0.1–1.4] | 0.4% [0.1–1.4] | +0.0 [-0.8, +0.8] punti | dentro | dentro |
| Rimarginare usato quando possibile | 0–70% | 33.0% [31.5–34.6] | 33.0% [31.5–34.6] | -0.0 [-2.2, +2.2] punti | dentro | dentro |
| Scarto di vittorie tra mazzi | piccolo | 26 punti | 27 punti | | | |
| Vite perse da attacchi del Leader | <40% | 4% | 4% | | | |

Tempo totale: 4s.
