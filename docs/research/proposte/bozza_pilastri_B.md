# Bozza di pilastri di design (scritta sulla proposta B, da discutere)

Bozza del coordinatore, non decisa. I pilastri generali (5, 6, 8, 9) e gli obiettivi misurabili valgono per qualsiasi proposta; i riferimenti alle Cicatrici valgono solo per B.

## 1. Ogni colpo racconta una storia
Il danno subito non sparisce: diventa Cicatrici pubbliche che danno carte, difese e alla fine risvegliano il Leader. Chi è sotto ha sempre una risorsa nuova, ma deve guadagnarsela (comeback guadagnato, non regalato).

## 2. Agire è esporsi
Attaccare, intercettare o usare abilità potenti rende un'unità attaccabile. Chi non agisce è al sicuro ma non avanza. Ogni azione è una promessa e un bersaglio.

## 3. Una risorsa, tre scelte
Nessuna carta-risorsa nel mazzo, quindi niente mana screw o flood. La Brace cresce da sola, ma ogni punto si spende, si infonde in un'unità o si accantona come Guardia per il turno avversario. La decisione è sempre interessante e mai solitaria: la Guardia è pubblica e l'avversario la legge.

## 4. Il turno avversario non è una pausa
Il difensore ha sempre almeno una decisione reale: intercettare, parare, giocare una Reazione dalla mano o dalle Cicatrici.

## 5. Niente vittorie in un turno, niente partite infinite
Massimo 2 Vite perse per turno e colpo finale solo su un Leader già a 0 all'inizio del turno: nessuna OTK per costruzione. Il Crepuscolo dal turno 10 chiude le partite. Obiettivo: 5–15 turni a testa, mediana 8–10.

## 6. Interazione che modifica, mai che annulla (leggi di design)
- Nessuna carta annulla un'altra carta o vieta di giocare.
- Niente scarto forzato dalla mano avversaria.
- Nessuna distruzione o riduzione della Fornace avversaria.
- Nessun effetto impedisce a un'unità di tornare Pronta per più di 1 turno.
- Nessuna moneta o dado che decide l'esito dopo una scelta (la casualità sta solo nella pescata).

## 7. Archetipi come ponti, non come recinti
Quattro colori, ognuno con una filosofia. Le parole chiave compaiono sempre in almeno due colori, i Leader sono bicolori e le carte Neutrali fanno da collante. Archetipi misti e combo trasversali sono un obiettivo, non un'eccezione.

## 8. Testo corto, profondità alta
"Rimuovere complessità, non profondità." Una carta comune ha al massimo una parola chiave e una frase. Nessuna pila, nessun timing a eccezioni: ogni azione si risolve subito in un ordine fisso.

## 9. Simulabile per costruzione
Stato discreto, azioni enumerabili, informazione nascosta solo in mano, mazzo e Vita coperta. Ogni regola nuova deve poter essere scritta nel simulatore senza casi speciali.

## Obiettivi misurabili (verificati dal simulatore)
| Metrica | Obiettivo |
|---|---|
| Durata partita (turni per giocatore) | ≥90% tra 5 e 15, mediana 8–10 |
| Vittorie del primo giocatore (mirror) | 48–52% |
| Vittorie per archetipo / Leader | 45–55% |
| Rimonte (vince chi era sotto di ≥2 Vite al turno 6) | 20–35% |
| Attacchi al Leader fermati da una reazione | 30–45% |
| Partite chiuse dal Crepuscolo | <15% |
| Margine IA forte vs IA semplice | ≥65% di vittorie (altrimenti poca profondità) |
