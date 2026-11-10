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

Totale: 4.500 partite, circa 19 h. La stima per bruciare viene dalla prova: la partita è stata circa il 50% più lenta, perché l'IA forte ha più giocate legali da valutare.

## Lancio
Dalla radice della repo, su main 636e83e o successivo (con la PR #22):

    nohup bash dati/E-033-input/lancia_e033.sh tutti > /dev/null 2>&1 &

- Il launcher gioca un braccio alla volta, oppure `tutti` (nell'ordine bruciare, tempra_tardo, allo_scoperto).
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

La colonna Breccia resta a 0, perché nessuna carta del vaglio ha la parola chiave.

## Verifiche fatte
- `python3 -B -m sim.v02.run valida carte.json --mazzi mazzi.json --variante <V027 | varianti/*.json>` dà 0 errori per la base e per i tre bracci. Resta un avviso noto: 43 carte di B0c03 hanno rarità NC, fuori dalla scala C/R/E/L.
- `rules_from` legge da ogni file solo il suo parametro (bruciare True / tempra_tardo 10 / allo_scoperto True); il resto è V027 (Tempra 4, 2 copie).
- Una partita di prova per braccio (L1-L2, seme 3401, forte:30) finisce senza errori:
  - bruciare: 5 carte bruciate per lato;
  - tempra_tardo e allo_scoperto: partite diverse dal riferimento.
- Il launcher, provato su un incrocio con `E033_OUT` in una cartella temporanea, dà lo stesso replay del comando diretto.
