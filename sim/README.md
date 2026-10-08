# Simulatore di CICATRICI

Ambiente di simulazione per il regolamento in `docs/regolamento_v0.1.md`. Serve allo swarm di agenti per giocare migliaia di partite, misurare le metriche dei pilastri (`docs/pilastri_design.md`) e decidere i disaccordi con i dati.

Il gioco è **in fase di creazione**: regole e carte cambieranno spesso. Per questo il motore contiene solo lo scheletro e tutto il resto è modificabile senza toccarlo.

| Cosa vuoi cambiare | Dove | Serve toccare il motore? |
|---|---|---|
| Un numero (Vita, Saldo, Guardia, turno del Crepuscolo…) | `sim/config.py`, classe `Rules` | No |
| Accendere o spegnere una regola | `Rules.modules` in `sim/config.py` | No |
| Aggiungere una regola nuova | una classe in `sim/rules.py` + il suo nome in `Rules.modules` | No |
| Aggiungere o modificare una carta o un Leader | `sim/data/cards_v0.json` | No |
| Un mazzo | `sim/decks/*.json` | No |
| Una variante da confrontare | `VARIANTS` in `sim/config.py` | No |

## Uso rapido

```bash
python -m sim.run torneo --games 200                 # tutti i mazzi contro tutti, IA semplice
python -m sim.run torneo --games 50 --agents forte:200
python -m sim.run varianti --games 200 --variants default V1b_per_attack V2_g2_six
python -m sim.run ia --games 6 --strong forte:150    # controllo: l'IA forte batte la semplice?
python -m sim.run trappola --games 100              # controllo: il mazzo con la carta rotta vince?
python -m sim.run partita arden_rosso_verde maera_blu_nero --seed 3   # replay leggibile
python -m sim.esperimento --base default --variante V1b=V1b_per_attack --partite 200 --out <cartella>
python tests/test_engine.py
```

### Giocare una partita a mano (playtester)

Un lato lo gioca un agente o una persona, una decisione per comando; l'altro lo gioca l'IA.
Si vede solo l'informazione visibile a quel giocatore e le azioni legali numerate.

```bash
python -m sim.gioca nuova --mazzo maera_blu_nero --contro arden_rosso_verde --ia semplice --seed 3 --file p.json
python -m sim.gioca mossa --file p.json 2      # sceglie l'azione numero 2
python -m sim.gioca stato --file p.json --log  # stato e registro completo
```

Ogni comando scrive un report in markdown e i dati grezzi in json dentro `reports/`. Il report riporta la versione delle regole, i moduli attivi e i parametri diversi dal default, così ogni numero è tracciabile.

## Architettura

- `engine.py` — lo scheletro: zone, turno, Fornace/Brace/Guardia, giocare carte, infondere, combattimento in 9 passi con le due decisioni del difensore (intercetto e reazione), Vita/Cicatrici e colpo finale. È una macchina a punti di decisione: `decider()`, `legal_actions()`, `step(azione)`.
- `rules.py` — i moduli di regola: `primo_turno`, `scintilla`, `saldo`, `clessidra`, `crepuscolo_terminale`, `risveglio`, `rimarginare`, `ultimo_respiro`, più quelli delle varianti (`reazione_per_attacco`, `riscossa`, `crepuscolo_bozza`, `risveglio_a_tempo`). Ogni modulo usa solo gli "agganci" elencati in cima al file.
- `effects.py` — interprete del linguaggio delle carte (sotto).
- `cards.py` — carica carte e Leader dai json e controlla la legalità dei mazzi.
- `agents.py` — IA `random`, `semplice` (priorità scritte a mano, veloce) e `forte` (Monte Carlo tree search con campionamento delle informazioni nascoste).
- `run.py` — partite in parallelo, metriche con intervallo di confidenza al 95%, statistiche per carta, report.

## Linguaggio delle carte

Una carta è un oggetto json:

```json
{"id": "sentinella", "name": "Sentinella del Guado", "type": "unit", "cost": 2, "colors": ["B"], "power": 3,
 "keywords": ["scudo"],
 "abilities": [{"trigger": "on_intercept", "do": [{"op": "gain_guard", "n": 1}]}],
 "text": "Scudo. Quando intercetta, ottieni 1 Guardia."}
```

- `type`: `unit`, `tactic`, `reaction`, `relic`.
- `keywords`: `assalto`, `scudo`, `bracconiere` (valore in `kw_params`), più parole descrittive libere (`furia`, `infuso`).
- `abilities`: lista di abilità.
  - Trigger: `{"trigger": EVENTO, "if": [CONDIZIONI], "once_per_turn": true, "do": [OPERAZIONI]}`.
    Eventi: `on_enter`, `on_attack`, `on_intercept`, `on_intercepted` (sull'Unità attaccante quando viene intercettata, dopo `on_intercept`), `on_infuse`, `on_defeats_attacker`, `on_own_unit_defeats_exposed`, `on_guard_discarded` (nel Ripristino, se la Guardia scartata è almeno 1; il numero è `"@n"`).
  - Statiche: `{"static": "power", "value": 3, "if": [{"furia": 2}]}` (sulla carta stessa) oppure con `"applies_to": SELETTORE` (aura su altre Unità); `{"static": "guard_max", "value": 1, "cap": 4}` (`cap` facoltativo: il massimo di Guardia non supera 4 per effetto di questa carta; vale da Leader, Reliquie e Unità).
- `play` (Tattiche): `{"target": SELETTORE, "costs": [{"lose_life": 1, "floor": 1}], "do": [...]}`.
- `react` (Reazioni): `{"costs": [...], "do": [...], "do_from_scars": [...]}`; il costo in Guardia è `cost`.
- Costi extra su qualsiasi carta: `"costs": [{"lose_life": N, "floor": F}]` al livello della carta (Unità, Reliquie, Tattiche, Reazioni) o dentro `play`/`react`. La carta è giocabile solo se restano almeno F Vite e il Saldo lo permette; le Vite pagate contano nel Saldo e diventano Cicatrici.
- Condizioni: `furia N`, `scars_ge N`, `infusion_count N`, `awakened true/false`, `is_second_player true/false` (il proprietario è G2), `life_behind_ge N` (Vite avversarie − Vite proprie ≥ N), `life_le N`.
- Selettori: `{"side": "own"|"opp", "kind": "unit", "cost_le": 3, "exposed": true, "power_le": 4, "inf_ge": 2, "keyword": "assalto"}`. `cost_le` e `power_le` accettano anche valori dinamici, per esempio `"power_le": "@scars"`.
- Operazioni: `draw`, `gain_guard`, `temp_power`, `perm_power`, `expose`, `defeat`, `give_renew`, `att_mod`, `def_mod`, `after_combat_ready_interceptor`, `steal_infusion`, `unblockable` (il bersaglio non può essere intercettato fino a fine turno; usata in `on_attack` vale già per quell'attacco). Bersagli: `self`, `infused`, `chosen`.
- Un numero può essere scritto `"@nome"` (o `"-@nome"`):
  - valori dinamici visti dal proprietario della carta: `@scars`, `@opp_scars`, `@life`, `@opp_life`, `@hand`, `@guard`;
  - `@n`: il numero portato dall'evento (per esempio la Guardia scartata);
  - qualsiasi altro nome legge il parametro da `Rules`, così un valore da tarare resta nella configurazione.

I Leader hanno `base` e `awakened`, liste di abilità con in più: `{"activated": true, "exhaust": true, "cost": 2, "target": ..., "do": [...]}`, `{"reaction": true, "guard_cost": 1, "do": [...]}` e `{"modifier": NOME, "value": ...}` (`parry_per_guard`, `rim_free_once`, `rim_keeps_furia`).

Se una carta nuova ha bisogno di un'operazione o di un evento che non esiste, si aggiunge a `effects.py` (una funzione, nessuna modifica al motore) e si documenta qui.

## Limiti noti (v0)

- Le carte `[test]` sono riempitivi senza testo, servono solo a fare mazzi da 40 finché il passo 3 non produce il set vero.
- L'IA semplice usa priorità fisse; l'IA forte campiona le informazioni nascoste ma gioca i rollout con l'IA semplice, quindi sottovaluta combo che la semplice non conosce.
- L'IA forte con 100 iterazioni batte la semplice solo nel 53% dei casi (obiettivo 65%) e costa circa 4 secondi a partita per core: per i tornei di massa si usa la semplice, la forte serve per i controlli a campione.
- Mulligan e scarti per limite di mano usano una regola fissa, non una decisione dell'IA.

## Nucleo v0.2 (`sim/v02/`)

Motore, IA e runner del nucleo v0.2 ratificato (Q-013, `docs/regolamento_v0.2.md`). Le regole sono un dataclass (`sim/v02/config.py`): ogni scelta aperta è un parametro, ogni variante un preset o un file JSON `{"base": preset, "set": {...}}`. Preset `V02` (default) = nucleo ratificato; `B0` = base dell'esperimento; `V1B_sequenziale`, `V2B_scoperto`, `V3B_opposizione_dopo`, `V4B_raddrizzo_fine`, `S_scudo_pareggi`.

```bash
python3 -m sim.v02.run torneo --partite 500            # metriche e fasce dei pilastri, mirror su tutti i mazzi
python3 -m sim.v02.run torneo --partite 0 --incroci 400 # incroci fra mazzi diversi
python3 -m sim.v02.run ab --base V02 --variante mia.json --partite 2500   # A/B appaiato
python3 -m sim.v02.run collaudo --variante V02          # sfruttabilità dell'IA del pugno
python3 -m sim.v02.run forte --forte forte:30 --partite 75               # IA forte contro semplice
python3 -m sim.v02.run partita arden_rosso_verde maera_blu_nero          # una partita con log
python3 tests/test_v02.py
```

IA: `semplice` (euristiche + equilibrio del pugno con regret matching, prezzo-ombra λ=0.03 per gemma), `det` (pugno deterministico), `br` (miglior risposta, per il collaudo), `forte:N` (MCTS con rollout semplici, ~1–2 s a partita con Tempra 4). Carte convertite da v0.1 in `sim/v02/cards_v02.json`. Esperimenti in `/mnt/project-files/tcg/swarm/esperimenti/E-014/`.
