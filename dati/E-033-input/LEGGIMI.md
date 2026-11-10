# E-033-input — vaglio delle leve di ritmo (R-028, Q-028)

Autore: programmatore (swarm), 2026-11-10. Richiesta: `tcg/set/richieste/R-028_ritmo_Q028.md` (copia in `dati/R-028/`).

## Base
- **Carte e liste:** B0c05, identiche byte per byte agli input di `00_B0c05` di E-030 (`tcg/set/esperimenti/E-030_q026/00_B0c05/`, `dati/E-030-input/00_B0c05/`):
  - `carte.json`: le carte B0c03, 120 carte;
  - `mazzi.json`: le 6 liste `rif_`;
  - `traccia.txt`: la traccia di E-030, così la tabella R-012 si confronta con il riferimento.
- Q-027 non è ancora votata e i suoi bracci non migliorano la base. La Breccia non entra nel vaglio, quindi non ci sono carte nuove.
- **Variante:** V027, con le liste B0c05. Ogni braccio è un file `varianti/<braccio>.json` (`{"base": "V027", "set": {...}}`) che cambia un solo parametro di regola (PR #22). Non ci sono regole nel codice né carte cambiate.

| Braccio | Parametro | IA, partite per incrocio | Incroci | Semi | Stima su 4 core |
|---|---|---|---|---|---|
| bruciare | `bruciare: true` (`bruciare_min_mano` 0) | forte:30, 100 | tutti (15) | 3400+k | ~8 h |
| tempra_tardo | `tempra_tardo: 10` | forte:30, 100 | tutti (15) | 3400+k | ~5.4 h |
| allo_scoperto | `allo_scoperto: true` | forte:30, 100 | tutti (15) | 3400+k | ~5.4 h |
| breccia | nessun parametro (V027); carte e liste di `breccia/` (NEW-BR1–BR6, Q-028 V3) | forte:30, 100 | tutti (15) | 3400+k | ~5.4 h |

Totale: 6.000 partite, circa 24.5 h (il braccio breccia è in coda, dopo i tre del vaglio). La stima per bruciare viene dalla prova: la partita è stata circa il 50% più lenta, perché l'IA forte ha più giocate legali da valutare.

## Lancio
Dalla radice della repo, su main 636e83e o successivo (con la PR #22):

    nohup bash dati/E-033-input/lancia_e033.sh tutti > /dev/null 2>&1 &

- Il launcher gioca un braccio alla volta, oppure `tutti` (nell'ordine bruciare, tempra_tardo, allo_scoperto, breccia).
- Passa `--riprendi` e salta gli incroci già finiti, quindi dopo un'interruzione si può rilanciare.
- Le uscite vanno in `tcg/swarm/esperimenti/E-033_ritmo/<braccio>/F_s3400/Li-Lj/`. Il registro è `avanzamento.log`. `E033_OUT` cambia la cartella.
- Gli argomenti facoltativi sono `ia`, `partite`, `seed_base` e `celle`, nello stesso formato di E-031.

## Riferimento e appaiamento
- **Riferimento:** E-030 `00_B0c05/F_s3400`, già giocato con forte:30, 200 partite per incrocio, semi 3400+k e preset V026. V027 ha le stesse regole di gioco di V026 e aggiunge solo i controlli sulla costruzione del mazzo. Non serve una nuova corsa della base.
- **I semi sono gli stessi.** Nel torneo, il seme di una partita dipende solo dal seme dell'incrocio e dall'indice g della partita (`seed·10⁶ + 500.000 + g`, posti alternati con g). Le 100 partite di ogni braccio hanno quindi gli stessi semi, mazzi e posti delle partite g = 0..99 del riferimento.
- **Controllo fatto su main 7a1118e.** La partita g = 0 di L1-L2 (seme 3401, V027, a leve spente) riproduce byte per byte il `_replay.txt` del riferimento. Con ognuna delle tre leve la stessa partita va diversamente, come deve.
- **L'appaiamento partita per partita non si può fare con i soli file del riferimento.** Il torneo salva solo il report aggregato delle 200 partite e il replay della prima. I record per partita non restano: il checkpoint `.partite_fatte.pkl` si cancella a fine incrocio. Restano due strade:
  - (a) confrontare i report a livello di incrocio. I semi sono comuni, ma il riferimento conta 200 partite e il braccio 100: le prime 100 sono un sottoinsieme, non un campione appaiato;
  - (b) se il thread vuole un vero confronto appaiato sulle stesse 100 partite, oppure i contatori R-028 della base, rigiocare la base con `bash dati/E-033-input/lancia_e033.sh 00_rif`. Sono 1.500 partite, circa 5.4 h. Riproduce le prime 100 partite del riferimento e il suo report ha la tabella R-028. Non fa parte del vaglio: è una scelta del thread.
- **Il riferimento non ha la tabella "R-028 (Q-028): ritmo"**, perché è stato giocato su ab6f2dd, prima della PR #22. Per i contatori di ritmo della base servono la strada (b) oppure le misure di Q-028 (`tcg/swarm/questioni/Q-028_divertimento/dati/`, script `metriche_f.py` e `metriche_f_extra.py`, su altri semi).

## Contatori da leggere nel report
Sono quelli della sezione "Contatori nel report" di R-028. Il motore li stampa tutti nella tabella "R-028 (Q-028): ritmo", per mazzo e in totale:
- partite chiuse dal Crepuscolo;
- serie più lunga senza Vite perse nei round 4–10, media per partita;
- round giocati dopo il primo 0 Vite;
- % di ribaltamenti di chi è a 0 Vite;
- turni vuoti nei round 1–3;
- turni senza giocare carte;
- mano piena senza nulla di giocabile;
- carte bruciate a partita (diverso da 0 solo nel braccio bruciare);
- Unità ferme, divise in "si è opposta" e "mai coinvolta" (M6);
- vittorie entro il round 5;
- R-017 entro il round 6.

Accanto a questi contatori vanno letti anche quelli abituali: la matrice degli incroci e la durata in round.

La colonna Breccia resta a 0 nei tre bracci del vaglio, perché nessuna loro carta ha la parola chiave. Per il braccio breccia vedi la sezione sotto.

## Verifiche fatte
- `python3 -B -m sim.v02.run valida carte.json --mazzi mazzi.json --variante <V027 | varianti/*.json>` dà 0 errori per la base e per i tre bracci. Resta un avviso noto: 43 carte di B0c03 hanno rarità NC, fuori dalla scala C/R/E/L.
- `rules_from` legge da ogni file solo il suo parametro (bruciare True / tempra_tardo 10 / allo_scoperto True); il resto è V027 (Tempra 4, 2 copie).
- Una partita di prova per braccio (L1-L2, seme 3401, forte:30) finisce senza errori:
  - bruciare: 5 carte bruciate per lato;
  - tempra_tardo e allo_scoperto: partite diverse dal riferimento.
- Il launcher, provato su un incrocio con `E033_OUT` in una cartella temporanea, dà lo stesso replay del comando diretto.

## Braccio breccia (Q-028 V3)
Esito del voto: in fondo a `tcg/swarm/questioni/Q-028_divertimento/proposta_breccia.md` (B1 8/8 con gli emendamenti, B3 6/8). La base è la stessa di 00_rif: preset V027 senza leve, liste B0c05 e semi 3400+k.

**Carte** (`breccia/carte.json`). Il file contiene le 120 carte di `carte.json`, identiche e nello stesso ordine, più 6 Comuni nuove in coda. Ognuna usa la parola chiave `breccia` del motore (main 636e83e). Tolgono la parola chiave o il testo della carta da cui derivano; costo e Forza restano gli stessi, salvo dove indicato:

| ID | Deriva da | Colori | Costo / F | Cambio |
|---|---|---|---|---|
| NEW-BR1 | VER-015 | G | 3 / 3 | Scudo → Breccia |
| NEW-BR2 | VER-019 | G | 4 / 4 | Impeto 1: +2 → Breccia (forma del verde) |
| NEW-BR3 | NER-009 | K | 2 / 3 | Caccia → Breccia; tiene il costo "perdi 1 Vita" (floor 1) |
| NEW-BR4 | NER-001 | K | 3 / 3 | Furia 2: +3 → Breccia; F da 2 a 3 |
| NEW-BR5 | BLU-012 | B/K | 3 / 3 | Scudo → Breccia (solo Maera) |
| NEW-BR6 | BLU-015 | G/B | 4 / 4 | "Quando attacca, +1" → Breccia (solo Thorn) |

Il testo di ogni carta è "Breccia *(se questa Unità batte chi si oppone, il Leader avversario perde 1 Vita, nel rispetto del Saldo)*.". NEW-BR3 aggiunge il costo in Vita di NER-009. I nomi si danno solo se il braccio viene adottato.

**Liste** (`breccia/mazzi.json`). Ogni nuova carta sostituisce 1 a 1, nella stessa posizione, la carta da cui deriva:

| Lista | Sostituzioni |
|---|---|
| L2 Maera | BLU-012 ×2 → NEW-BR5 ×2 |
| L3 | NER-009 ×2 → NEW-BR3 ×2, NER-001 ×2 → NEW-BR4 ×2 |
| L4 Thorn | VER-015 ×1 → NEW-BR1 ×1, VER-019 ×1 → NEW-BR2 ×1, BLU-015 ×2 → NEW-BR6 ×2 |
| L6 | VER-019 ×2 → NEW-BR2 ×2, NER-009 ×2 → NEW-BR3 ×2, NER-001 ×1 → NEW-BR4 ×1 |

L1 e L5 sono identiche a B0c05. NEW-BR2 non entra mai in L1, che tiene VER-019 ×2. Verifica: la partita g = 0 di L1-L5 (seme 3404) riproduce byte per byte il replay di 00_B0c05 F_s3400.

**Traccia** (`breccia/traccia.txt`): la traccia di E-030, più le 6 carte nuove e le carte di origine che ancora non c'erano (VER-015, NER-009, NER-001, BLU-012, BLU-015). Gli altri tre bracci restano con `traccia.txt`.

**Contatori da chiedere.**
- **Brecce riuscite per carta (obbligatorio, analista): il motore NON lo ha.** Il motore conta le Vite tolte da Breccia solo per mazzo, nella colonna "Breccia" della tabella R-028 (`stats["breccia"]`, per giocatore). Non le conta per carta. Per avere il numero esatto serve un contatore per carta nel motore, del tipo `breccia_by[cid]` accanto a `kills_by`: è una richiesta per il thread del motore. Nell'attesa c'è un'approssimazione. Nella tabella R-012 delle carte tracciate, il quarto numero ("Unità sconfitte") di NEW-BR1–BR6 conta le Unità che si opponevano e che la carta ha sconfitto, perché queste carte non hanno Caccia. È un tetto alle Brecce riuscite: comprende anche le Brecce bloccate dal Saldo e i pareggi (vedi sotto).
- **Unità ferme divise in "si è opposta" e "mai coinvolta" (M6): il motore le ha**, nelle colonne "Unità ferme: si è opposta" e "mai coinvolta (M6)" della tabella R-028, per mazzo.
- Da riportare anche, come chiede l'esito:
  - Vite perse per Breccia sul totale delle Vite perse;
  - livello di Maera e R9-5 nelle sue celle (guardia blu: Maera perde 2 Scudo e parte da 52.6);
  - Thorn non sotto 42 (guardia del critico di Q-027, misurata sulla base B0c05);
  - vittorie entro il R6, per un eventuale braccio successivo con BR3 a F2 (non è una correzione automatica).

**Pareggi.** Nel motore (`engine.py`, risoluzione dello scontro) la Breccia scatta ogni volta che l'Unità che si oppone viene sconfitta, anche nel pareggio fra Unità, dove sono sconfitte tutte e due. Una lettura stretta di "batte chi si oppone" escluderebbe il pareggio. Non ho cambiato nulla: lo segnalo perché chi legge i dati ne tenga conto, oppure perché il thread del motore lo corregga prima della corsa.

**Prove fatte** (main 7a1118e):
- `valida --variante V027` su `breccia/carte.json` con `breccia/mazzi.json`: 0 errori su 126 carte (resta l'avviso noto delle 43 NC).
- forte:30, L4-L6 ×2 e L1-L5 ×1: le partite finiscono senza errori, le carte BR si giocano e il replay di L1-L5 è identico al riferimento.
- IA semplice, 40 partite in L2-L4 e in L3-L6: le carte BR si giocano e sconfiggono chi si oppone. La Breccia toglie 1 Vita in L2 (0.03 a partita). Le altre sconfitte di chi si opponeva non tolgono Vite: le ha bloccate il Saldo oppure il Leader era già a 0 Vite (`lose_life`).
