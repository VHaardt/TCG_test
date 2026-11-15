# E-034-input — misura del riferimento B0c06 (Q-031, ciclo 05 B)

Autore: programmatore (swarm), 2026-11-15. Questione: `tcg/swarm/questioni/Q-031_ciclo05.md`. Liste: `tcg/swarm/cicli/ciclo-05/liste_V4/`.

## Base
- **Carte:** `carte.json` è una copia di `tcg/set/finale/set_v02.json`, con 125 carte: B0c03, ciclo 04 (M1, NEW-V05, NEW-B06) e Q-027 A (NEW-I04, I05, I06).
- **Liste B0c06:** `mazzi.json` è una copia di `tcg/set/finale/mazzi_v02.json` e contiene le 6 liste `rif_`. Le liste L2, L4 e L6 hanno già la V4 del ciclo 05. Le liste `mix_` restano fuori.
- **Traccia:** `traccia.txt` è quella di E-033 più NEW-I04, NEW-I05 e VER-004.
- **Varianti:** V027. Il braccio `tempra_tardo` usa `varianti/tempra_tardo.json` (`{"base": "V027", "set": {"tempra_tardo": 10}}`), lo stesso file di E-033.

Differenze delle liste da B0c05, cioè le liste di E-033:

| Lista | Rispetto a B0c05 |
|---|---|
| L1 Arden | M2: −VER-013 ×2; +NEW-V05 ×2 |
| L2 Maera | Q-027 A: −BLU-009, −BLU-023 ×2, −NER-003 ×2, −NER-023; +NEW-I04 ×2, +NEW-I05 ×2, +NEW-I06 ×2. Poi V4: −NEW-I05 ×2, −NEW-I06 ×2, −BLU-022; +BLU-005 ×2, +BLU-004 ×2, +NEU-004 |
| L3 Vey | nessuna |
| L4 Thorn | M2: −NEU-011, −VER-002; +NEW-V05 ×2. Poi Q-027 A: −BLU-023 ×2, −VER-024, −VER-025; +NEW-I04 ×2, +NEW-I05 ×2. Poi V4: −NEU-003; +VER-002 |
| L5 | nessuna |
| L6 | M2: −VER-013 ×2; +NEW-V05 ×2. M3: −VER-023; +NEW-B06. V4: −NER-007, −VER-024; +NER-006, +VER-004 |

## Bracci
| Braccio | Regole | IA, partite per incrocio | Incroci | Semi | Stima su 4 core |
|---|---|---|---|---|---|
| 00_B0c06 | V027 | forte:30, 200 | tutti (15) | 3500+k (nuovi) | ~10.8 h |
| tempra_tardo | V027 + Tempra 3 dal round 10 | forte:30, 200 | tutti (15) | 3500+k | ~10.8 h |

Totale: 6.000 partite, circa 21.6 h.
- **Semi.** I due bracci usano gli stessi semi, quindi sono appaiati partita per partita. Il seme della partita è `seed·10⁶ + 500.000 + g`, con posti alternati su g.
- **Confronto con E-033.** I semi 3500+k sono nuovi: con E-033 (3400+k) il confronto si fa solo per incrocio, non partita per partita.

## Lancio
Dalla radice della repo, su main 7ec6380 o successivo (servono le tabelle Scudo e Brecce per carta):

    nohup bash dati/E-034-input/lancia_e034.sh tutti > /dev/null 2>&1 &

- Ogni braccio si può lanciare anche da solo. Gli argomenti facoltativi sono `ia`, `partite`, `seed_base` e `celle`, come in E-033.
- Il launcher passa `--riprendi` e salta gli incroci finiti.
- Le uscite vanno in `tcg/swarm/esperimenti/E-034_B0c06/<braccio>/F_s3500/Li-Lj/`. Il registro è `avanzamento.log`. `E034_OUT` cambia la cartella.

## Record per partita (tenuti)
In ogni cella resta `partite.pkl`, che contiene tutte le partite come pickle di `(indice, record)` in sequenza. È lo stesso formato che leggono `dati/coda/agg_q028.py` e gli altri aggregatori del thread principale.
- Come funziona: prima di giocare, il launcher crea `.partite_fatte.pkl` e un collegamento fisso `partite.pkl` allo stesso file. `run.py` cancella il checkpoint a fine cella, ma il collegamento resta. Non serve `tieni_pkl.sh`.
- Con `E034_RIPRENDI=0` non c'è checkpoint, quindi i record non si tengono.

## Contatori da leggere nel report
Il motore 7ec6380 stampa nel report di ogni cella:
- **R-028 (Q-028): ritmo**: Crepuscolo, serie senza Vite perse R4–R10, round dopo il primo 0 Vite, ribaltamenti, vittorie entro il R5, turni vuoti R1–3, turni senza giocare carte, mano piena senza giocate, Unità ferme "si è opposta" e "mai coinvolta", R-017 entro il R6;
- **R-026 (Q-027): interattività per Leader**;
- **R-027 P9b**: Reazioni per scontro difeso;
- **R-027 P7: Scudo per Leader**: opposizioni, opposizioni ripetute, rimozioni subite;
- le tabelle abituali: R-005, R-012 (matrice, contatori per mazzo, carte tracciate), R-017 e Q-026 M5.

La tabella delle Brecce per carta resta vuota, perché nessuna carta delle liste ha la Breccia.

Dai record per partita si ottengono anche le tabelle aggregate sull'intero braccio.

## Controlli da fare (Q-031 B)
- Q-028 G1:
  - Maera ≥ 43 con `tempra_tardo`;
  - nessun altro Leader si allontana dalla fascia di oltre 1.0 rispetto a 00_B0c06;
  - L5 − L2 ≤ 70.
- Guardia Q-027: Thorn ≥ 42.
- Da riportare per le liste V4: turni vuoti R1–3, passi al R1 e mano piena senza giocate di L2, L4 e L6, confrontati con E-033 00_rif-200.

## Verifiche fatte (main 8ff53fc)
- `valida` con `--variante V027` e con `--variante varianti/tempra_tardo.json` dà 0 errori su 125 carte e 6 liste. Resta l'avviso noto delle 43 carte con rarità NC.
- Partita di prova per braccio: L2-L6, seme 3509, forte:30, 2 partite per braccio, lanciate con il launcher.
  - Tutte le partite finiscono senza errori.
  - Il report ha le tabelle R-028, R-026, P9b e Scudo.
  - `partite.pkl` resta con i 2 record (semi 3509500000 e 3509500001), mentre `.partite_fatte.pkl` è cancellato.
