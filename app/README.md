# CICATRICI online (POC)

App web minimale per giocare a CICATRICI fra amici e testare il gioco. Carte solo testo (ID, attributi, testo), nessun account, nessuna immagine.

- **Costruito**: ognuno sceglie un Leader e costruisce il suo mazzo (o parte da un mazzo di riferimento), poi si gioca.
- **Mazzi pronti**: ognuno sceglie uno dei mazzi di riferimento del set (già legali) e si gioca subito.
- **Draft (Arena)**: si sceglie il Leader fra 3 a caso, poi 40 volte una carta fra 3. Le carte offerte sono solo dei colori del Leader o Neutrali e mai oltre il limite di copie delle regole; le 3 carte di ogni scelta hanno la stessa rarità (pesi in `DRAFT_RARITA`, solo per le rarità che il set usa).
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
| Mazzi di riferimento | `CICATRICI_MAZZI`, poi le liste B0c05 di Q-026 (cartella condivisa, poi `app/dati/mazzi_B0c05.json`), poi i mazzi del set: vale il primo file con mazzi legali per le regole in vigore |
| Regole | `CICATRICI_REGOLE` (nome di preset o file json di variante), poi il preset `V027` (o `V026`), poi `app/dati/regole_V026.json` |
| Costruzione | `sim/v02/decks.problems` con `decks.limits(regole)`: con V027 40 carte, max 2 copie per nome, 1 per le Leggendarie, colori del Leader o Neutrali (le multicolore vogliono tutti i colori nel Leader) |

Il set viene letto all'avvio del server: quando il bilanciamento cambia le carte basta riavviarlo. L'app pubblicata fuori dal cloud del progetto non vede la cartella condivisa: `app/aggiorna_dati.sh` copia il set in vigore in `app/dati`, poi si fa commit e nuovo deploy.

## Pubblicare

Serve un servizio che esegua un container. Il repo ha `Dockerfile` e `render.yaml`:
- **Render**: New → Blueprint → il repo `TCG_test`. Il piano gratuito si addormenta senza visite e le stanze aperte si perdono.
- **Qualsiasi host Docker**: `docker build -t cicatrici . && docker run -p 8000:8000 cicatrici`.

## Limiti voluti della POC

- Le stanze vivono in memoria: si perdono al riavvio, scadono dopo 6 ore senza visite.
- Mulligan (§4.4) e bersagli dei trigger li scelgono i giocatori; per l'IA restano le scelte del simulatore.
  Il motore non ha punti di decisione per questi due casi, quindi l'app li aggiunge da fuori: il mulligan
  rigioca setup() con lo stesso seme applicando le scelte, e un'azione che innesca un trigger con più
  bersagli si prova su un clone finché ogni scelta è nota, poi si esegue sulla partita vera.
- Un colpo a segno sul Leader non toglie Vite quando il Saldo è pieno (§9.3) o quando il Leader è a 0 Vite con
  una Cicatrice fresca (§9.2, §9.5). Il motore lo tace; l'app aggiunge al registro una riga che dice perché
  e sotto i cuori di ogni Leader scrive lo stato (Saldo, Alle Corde, protezione della Cicatrice fresca).
- **Torna indietro**: si annulla la propria ultima scelta (anche più volte di fila) finché l'avversario umano non
  ha scelto nulla e non si è scoperta nessuna carta nascosta (pescate, Vite girate, carte dalla mano avversaria).
  È un aiuto da playtest, non una regola del gioco.
- **Modificatori dal vivo**: ogni Unità mostra i bonus alla Forza e da dove vengono (passandoci sopra), più i
  bonus da scontro già attivi (Furia); durante uno scontro Attacco e Difesa sono scomposti in base, gemme,
  Parata, Reazione e abilità.
- Il client interroga il server ogni secondo, niente websocket.
