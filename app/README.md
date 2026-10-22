# CICATRICI online (POC)

App web minimale per giocare a CICATRICI fra amici e testare il gioco. Carte solo testo (ID, attributi, testo), nessun account, nessuna immagine.

- **Costruito**: ognuno sceglie un Leader e costruisce il suo mazzo (o parte da un mazzo di riferimento), poi si gioca.
- **Draft (Arena)**: si sceglie il Leader fra 3 a caso, poi 40 volte una carta fra 3. Le carte offerte sono solo dei colori del Leader o Neutrali e mai oltre le 3 copie; le 3 carte di ogni scelta hanno la stessa rarità (C 60%, NC 30%, R 10%).
- **Avversario**: un amico, che entra col codice della stanza o col link d'invito, oppure l'IA semplice del simulatore.

## Avvio in locale

```bash
pip install -r requirements-app.txt      # solo numpy, per l'IA
python -m app.server                     # http://localhost:8000
python tests/test_app.py                 # controlli
```

## Da dove prende regole e carte

L'app non contiene regole: usa il motore `sim/v02` come libreria.

| Cosa | Da dove (il primo che esiste) |
|---|---|
| Carte e Leader | `CICATRICI_SET`, poi `/mnt/project-files/tcg/set/finale/set_v02.json`, poi `app/dati/set_v02.json` |
| Mazzi di riferimento | `CICATRICI_MAZZI`, poi la cartella condivisa, poi `app/dati/mazzi_v02.json` |
| Regole | `CICATRICI_REGOLE` (nome di preset o file json di variante), poi il preset `V026`, poi `app/dati/regole_V026.json` |
| Costruzione | `sim/v02/decks.py`: 40 carte, max 3 copie per ID, colori del Leader o Neutrali |

Il set viene letto all'avvio del server: quando il bilanciamento cambia le carte basta riavviarlo. L'app pubblicata fuori dal cloud del progetto non vede la cartella condivisa: `app/aggiorna_dati.sh` copia il set in vigore in `app/dati`, poi si fa commit e nuovo deploy.

## Pubblicare

Serve un servizio che esegua un container. Il repo ha `Dockerfile` e `render.yaml`:
- **Render**: New → Blueprint → il repo `TCG_test`. Il piano gratuito si addormenta senza visite e le stanze aperte si perdono.
- **Qualsiasi host Docker**: `docker build -t cicatrici . && docker run -p 8000:8000 cicatrici`.

## Limiti voluti della POC

- Le stanze vivono in memoria: si perdono al riavvio, scadono dopo 6 ore senza visite.
- Il mulligan è quello automatico del simulatore (le carte di costo ≥5 tornano in fondo al mazzo).
- I bersagli dei trigger automatici li sceglie il motore, come nel simulatore.
- Il client interroga il server ogni secondo, niente websocket.
