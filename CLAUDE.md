# CICATRICI — note per le sessioni Claude

- Regolamento e pilastri: `docs/regolamento_v0.2.md` e `docs/pilastri_design_v0.2.md` (copie di `/mnt/project-files/tcg/`; v0.1 resta per storia). Esito del rework: `docs/discussione/Q-013_esito.md`.
- Simulatore v0.2: `sim/v02/` (preset `V02` = nucleo ratificato); `sim/` principale = v0.1.
- Simulatore: `sim/` (istruzioni in `sim/README.md`). Regole e carte sono dati modificabili: niente regole scritte nel codice del motore.

## Standard di progetto: lo swarm di agenti

Ogni lavoro su regole, carte o bilanciamento di CICATRICI segue la strategia dello swarm (standard deciso da Vittorio).
- Punto di partenza: `/mnt/project-files/tcg/swarm/indice.md`, poi `strategia_swarm.md` e il protocollo adatto in `protocolli/`.
- Ogni decisione ha un livello (1 ritocco, 2 carta o meccanica, 3 nucleo) e segue il protocollo di quel livello, con gli agenti-ruolo (`ruoli/_comune.md` + `ruoli/<ruolo>.md`).
- Ogni modifica è una questione `Q-NNN` in `questioni/` e finisce in `changelog.md`.
- I disaccordi misurabili diventano esperimenti A/B del simulatore (`esperimenti/`), non scelte dall'alto.
- Le decisioni di design non si chiedono a Vittorio: a lui vanno solo i cambi di vincoli o di scopo e il report di una pagina a fine ciclo.
