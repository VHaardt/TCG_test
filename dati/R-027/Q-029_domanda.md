# Q-029: chiudere o confermare le regole "in prova" del regolamento v0.2.7 (aperta il 2026-11-02)

Livello 3 (nucleo): ogni cambio va approvato da Vittorio. Se una regola viene **confermata**, basta il voto dello swarm e il riquadro "in prova" sparisce.

## Perché
Vittorio, 2026-11-02 alle 22:32 UTC: "Alcune meccaniche sono segnate come in prova: valuta anche con gli altri thread se lo sono ancora."

Il thread del regolamento illustrato ne ha trovate tre ancora aperte. Per tutte e tre la condizione di revisione si è avverata.
- **P6**, compensazione di G2: +1 gemma nei round 1 e 3 (§17.1). Q-022 chiedeva una rimisura con l'IA forte dopo il ciclo carte 02, e il ciclo 02 è chiuso dal 2026-10-19.
- **P7**, lo Scudo vince i pareggi (§17.2). L'A/B contro "si oppone senza ruotarsi" su mazzi con almeno 5 Scudo non è mai stato fatto.
- **P9b**, le Reazioni si pagano con le gemme impegnate (§17.3). Con R-026 esistono le Reazioni a costo 0 (NEW-I04). Il dato oggi è 0.07 Reazioni per scontro, contro un obiettivo di 0.10.

Ne aggiungo una quarta, perché il set ora ha più costi in Vita:
- **P8**, il buco delle Cicatrici fresche (§17.4): una Vita persa nel turno avversario rende immuni al colpo finale. Va verificato che nessuna carta di Q-026 o di Q-027 lo apra.

## Che cosa decide lo swarm, per ogni regola
- **Conferma:** la regola resta com'è e il riquadro sparisce.
- **Cambio:** si propone un'alternativa misurata, da mandare a Vittorio.
- **Resta aperta:** solo se manca un dato, e si dice quale.

## Dati in corsa che servono
- **P6:** in E-030 (00_B0c05 con IA forte, semi 3400, 3000 partite) i posti sono alternati. Le vittorie di G1 per Leader e in totale si ricavano dai log senza nuove partite.
- **P9b:** il braccio A di E-031 (Reazioni I04–I06) e la tabella R-026 (Reazioni per scontro difeso).
- **P7:** serve una corsa nuova (R-027).

## Round 1 (alla cieca, al massimo 40 righe)
Ogni ruolo scrive `round1/r1_<ruolo>.md`. Per P6, P7, P9b e P8:
1. la posizione (conferma, cambio o aperta), con il perché;
2. una previsione numerica:
   - P6: G1 in % sull'IA forte, B0c05;
   - P7: round 13+ e Blu in % con "senza ruotarsi";
   - P9b: Reazioni per scontro con `reazione_da_cicatrice_costo` −1;
3. eventuali emendamenti al disegno di R-027 (`/mnt/project-files/tcg/set/richieste/R-027_regole_in_prova.md`). R-027 gira dopo E-031, quindi c'è tempo per cambiarla.

Seguono due passate di discussione, poi il voto: 6/8 per confermare; per cambiare, 6/8 e poi Vittorio.
