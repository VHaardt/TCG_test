# CICATRICI — Pilastri di design e obiettivi misurabili (v0.1, condivisi)

> Aggiornamento di `research/proposte/bozza_pilastri_B.md` al consenso del dibattito (`discussione/esito_dibattito.md`). Le regole sono in `regolamento_v0.1.md`.

## 1. Ogni colpo racconta una storia
Il danno subito non sparisce: diventa Cicatrici pubbliche che danno carte, Reazioni e Furia. Dopo **3 Vite perse** il Leader si Risveglia (Forza +1, Guardia +1), indipendentemente da quante Cicatrici hai recuperato. Chi è sotto ha sempre una risorsa nuova, ma deve guadagnarsela: recuperare una Cicatrice costa un'azione del Leader e abbassa la Furia.

## 2. Agire è esporsi
Attaccare, intercettare, usare abilità ⟳ e **Rimarginare** rendono il personaggio Esposto fino al suo prossimo Ripristino. Il Leader non colpisce gratis: con Forza 3 contro Tempra 5 deve investire Brace per ferire, e ogni turno sceglie tra attaccare e curarsi. Nessuna parola chiave permette di attaccare senza esporsi (Rinnovo lascia l'Unità Esposta).

## 3. Una risorsa, tre scelte
Nessuna carta-risorsa, quindi niente screw o flood. Ogni Brace si spende, si infonde o si accantona come Guardia. La Parata scalabile (+2 per Guardia) rende l'accantonamento una scelta graduata (0, 1, 2…) e pubblica: l'avversario la legge e decide quanto infondere per superarla.

## 4. Il turno avversario non è una pausa
A ogni attacco il difensore ha due decisioni in punti fissi: intercettare (e con chi) e reagire (Parata, Reazione dalla mano o dalle Cicatrici, abilità del Leader). Il budget è limitato e pubblico. Chi è Alle Corde ha un **Ultimo respiro** (2 reazioni) per una rimonta vera.

## 5. Niente vittorie in un turno, niente partite infinite
Saldo (massimo 2 Vite perse per turno) e colpo finale solo su un Leader già Alle Corde all'inizio del turno: nessuna OTK per costruzione, e nessuno attacca nel proprio primo turno. La **Clessidra** apre il finale senza punire (Saldo 3 dal turno 10, Alle Corde a 1 Vita dal turno 13). Dal turno 15 il **Crepuscolo terminale** è un limite duro: chi è Alle Corde nel proprio Ripristino perde, gli altri perdono 2 Vite. Ogni partita finisce entro il turno 17, e di norma entro il 15–16. Niente punti, niente patte. Obiettivo: 5–15 turni a testa, mediana 8–10.

## 6. Interazione che modifica, mai che annulla
- Nessuna carta annulla un'altra carta o vieta di giocare; l'attaccante non risponde mai.
- Niente scarto forzato dalla mano avversaria.
- Nessuna distruzione o riduzione della Fornace avversaria.
- Nessun effetto impedisce di tornare Pronti per più di 1 turno.
- Nessuna moneta o dado dopo una scelta.
- La rimozione economica colpisce solo chi si è Esposto; gli effetti che espongono non toccano mai il Leader.

## 7. Archetipi come ponti, non come recinti
Quattro colori con una filosofia ciascuno; ogni parola chiave in almeno due colori; Leader bicolori; Neutrali collante. Ogni colore ha almeno una risposta comune agli Scudo, e almeno 3 colori su 4 hanno effetti "Esponi" economici: nessun archetipo può murarsi in modo strutturale.

## 8. Testo corto, profondità alta
"Rimuovere complessità, non profondità." Una carta comune ha al massimo una parola chiave e una frase. Turni chiusi, nessuna pila, nessuna eccezione di timing: ogni azione si risolve subito in un ordine fisso.

## 9. Simulabile per costruzione
Stato discreto, azioni enumerabili, informazione nascosta solo in mano, ordine del mazzo e Vita coperta. Combattimento in 9 passi, controlli di stato in ordine fisso, glossario unico. Ogni costo non pagabile rende l'azione illegale. Ogni regola nuova deve potersi scrivere nel simulatore senza casi speciali, e ogni variante si introduce **una alla volta**.

---

## Obiettivi misurabili (verificati dal simulatore)

### Obiettivi di prodotto
| Metrica | Obiettivo |
|---|---|
| Durata partita (turni per giocatore) | ≥90% tra 5 e 15, mediana 8–10 |
| Vittorie del primo giocatore (mirror, per archetipo) | 48–52% |
| Vittorie per archetipo / Leader | 45–55% |
| Rimonte (vince chi era sotto di ≥2 Vite al turno 6) | 20–35% |
| Attacchi al Leader fermati da una reazione | 30–45% |
| Partite in cui la Clessidra è attiva alla fine (turno ≥10) | <15% |
| Partite che arrivano al turno 13 | <10% |
| Partite oltre il turno 15 | <2% (se superato: Crepuscolo terminale dal turno 14) |
| Partite oltre il turno 17 | 0 (garantito dalle regole) |
| Margine IA forte vs IA semplice | ≥65% di vittorie |

### Metriche di salute delle regole (nate dal dibattito)
| Metrica | Obiettivo / allarme | Collegata a |
|---|---|---|
| Quota di Vite perse per attacchi del Leader | <40% | Leader F3/T5 (test T1) |
| Guardia accantonata per turno | Distribuzione non degenere tra 0, 1 e 2 | Parata scalabile |
| Rimarginare usato quando possibile | <70% dei turni | Rimarginare ⟳ (test T3) |
| Partite all'anti-stallo nei matchup con mazzi da ≥5 Scudo | Allarme se >15% | Stallo da Scudo, legge 10 |
| Turni con ≥3 Unità Pronte che non attaccano | Da monitorare | Moduli Campo/zone |
| Turni con vantaggio di campo senza attacchi al Leader | Da monitorare | Risveglio a tempo (riserva) |
| Turni avversari con zero decisioni del difensore | Da monitorare | Modulo round condiviso |
| Azioni legali medie per turno | <60 | Branching per l'IA |
| Partite simulate oltre il turno 17 | 0 (altrimenti è un errore di implementazione) | Crepuscolo terminale |
| Vittorie di G1 nelle partite che arrivano al turno 10 | ≤52% | Asimmetria della Clessidra (V4) |
