# Regolamento illustrato (manuale per giocatori)

Presentazione per giocatori del regolamento di CICATRICI: testo semplice, esempi, schemi del tavolo, del turno, dell'attacco, delle gemme e delle Cicatrici, riepilogo rapido e glossario. **Non è una fonte di regole**: il testo di riferimento resta `docs/regolamento_v0.2.md`; se i due differiscono, vale il regolamento.

## File

| File | Cosa contiene |
|---|---|
| `manuale.md` | Il testo. Front matter: `versione` del manuale, `basato_su` (versione del regolamento), `preset` del simulatore |
| `figure/*.svg` | Gli schemi, SVG a mano con colori presi dal CSS (classi `riq-att`, `gemma`, `t-tenue`…) |
| `stile.css`, `modello.html` | Grafica e impaginazione (tema chiaro/scuro, stampa A4) |
| `build/` | Uscite generate: `regolamento_illustrato.html` (pagina completa), `.artifact.html` (per l'artifact su claude.ai), `.pdf` |
| `../../tools/manuale/build.py` | Lo script di generazione |

## Sintassi in `manuale.md`

- `{{nome}}`: un numero di regola, letto dal preset del simulatore (`sim/v02/config.py`) e da `sim/v02/decks.py`. Elenco completo: `python3 tools/manuale/build.py --parametri`. Un nome sconosciuto ferma la generazione. Funziona anche dentro le figure SVG.
- `[[figura:nome|didascalia]]` su una riga: inserisce `figure/nome.svg`. `tracciato` è disegnato dallo script a partire dai parametri.
- Riquadri: `::: esempio Titolo` … `:::` (tipi: `esempio`, `ricorda`, `attenzione`, `prova` per le regole in vigore ma ancora in test).
- `:gemma:` e `:ruota:` diventano icone. Il resto è Markdown normale (tabelle, liste, HTML con `markdown="1"`).

## Rigenerare

Dalla radice del repo (serve `pip install -r requirements-docs.txt`; il PDF usa Chromium):

```
python3 tools/manuale/build.py --pdf --copia /mnt/project-files/tcg/regolamento_illustrato
```

## Quando cambiano le regole

1. **Cambia solo un numero** (per esempio Tempra, Saldo, round del Crepuscolo): aggiorna il preset in `sim/v02/config.py` (o metti il nuovo preset nel front matter) e rigenera. Testo, tabelle, schemi e tracciato si aggiornano da soli.
2. **Cambia una regola o arriva una nuova versione del regolamento**: lo script avvisa quando `basato_su` non coincide con la versione in testa a `docs/regolamento_v0.2.md` (con `--rigido` si ferma). Leggi il registro modifiche del regolamento, correggi le sezioni toccate di `manuale.md` (e le figure, se serve), aggiorna `basato_su`, alza `versione` e rigenera.
3. **Regole "in prova"**: quando un default aperto viene deciso, togli il riquadro `::: prova` relativo.
4. Ripubblica l'artifact con `build/regolamento_illustrato.artifact.html` e fai il commit di sorgente e uscite insieme.
