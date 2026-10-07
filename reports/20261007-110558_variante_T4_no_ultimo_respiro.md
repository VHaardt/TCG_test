# Variante T4_no_ultimo_respiro

- Regole: `v0.1-condiviso`; moduli attivi: primo_turno, scintilla, saldo, clessidra, crepuscolo_terminale, risveglio, rimarginare
- Parametri diversi dal default: {"modules": ["primo_turno", "scintilla", "saldo", "clessidra", "crepuscolo_terminale", "risveglio", "rimarginare"]}
- Partite: 2000; IA: semplice; tempo 10s
- Tra parentesi quadre: intervallo di confidenza al 95%.

## Metriche dei pilastri
| Metrica | Valore | Obiettivo | |
|---|---|---|---|
| Durata mediana (turni per giocatore) | 10.0 [10.0–11.0] (media 10.5) | 8–10 | ✅ |
| Partite tra 5 e 15 turni | 100.0% [99.7–100.0] | ≥90% | ✅ |
| Partite oltre il turno 15 | 0.1% [0.0–0.3] | <2% | ✅ |
| Vittorie del primo giocatore | 64.0% [61.9–66.1] | 48–52% | ❌ |
| Rimonte (sotto di ≥2 Vite al turno 6, n=672) | 26.2% [23.0–29.6] | 20–35% | ✅ |
| Attacchi al Leader fermati da una reazione (su 27888 minacce) | 23.8% [23.3–24.3] | 30–45% | ❌ |
| Partite chiuse dal Crepuscolo | 0.4% [0.2–0.9] | <15% | ✅ |
| Rimarginare usato quando possibile | 32.9% [32.1–33.6] | <70% | ✅ |
| Quota di Vite perse per attacchi del Leader | 4.7% | <40% | ✅ |

## Vittorie per mazzo (escluse le partite speculari)
| Mazzo | Vittorie | Obiettivo 45–55% |
|---|---|---|
| maera_blu_nero | 67.0% [63.1–70.6] | ❌ |
| thorn_verde_blu | 62.7% [58.7–66.4] | ❌ |
| arden_rosso_verde | 38.2% [34.4–42.1] | ❌ |
| vey_nero_rosso | 32.2% [28.6–36.0] | ❌ |

## Dettagli
- Fine partita: {"colpo_finale": 1991, "crepuscolo": 9}
- Durata (turni per giocatore → partite): {"7": 3, "8": 124, "9": 478, "10": 426, "11": 442, "12": 256, "13": 226, "14": 32, "15": 12, "16": 1}
- Attacchi al Leader andati a segno: 64.3% [63.8–64.8]
- Partite toccate dal Crepuscolo terminale: 0.7% [0.4–1.1]
- Vite perse per fonte: attacco_unita 87%, costo 8%, attacco_leader 5%, crepuscolo 0%
- Reazioni usate: {"parata": 5530, "muro": 2136, "leader": 380, "grido@cicatrice": 401, "grido": 2009, "muro@cicatrice": 299}
- Guardia accantonata in media per turno: 0.72

## Statistiche per carta
| Carta | Partite in cui pescata | Giocata quando pescata | Vittorie se giocata | Vittorie se rimasta in mano |
|---|---|---|---|---|
| Il Bastione Vivente | 1395 | 76% | 64% | 55% |
| [test] Guardiano Blu | 1548 | 93% | 59% | 84% |
| [test] Custode Blu | 1708 | 92% | 56% | 85% |
| [test] Leviatano Blu | 692 | 74% | 56% | 68% |
| [test] Antico Verde | 669 | 70% | 55% | 66% |
| Lanterna del Pellegrino | 1376 | 93% | 55% | 69% |
| Sentinella del Guado | 1631 | 81% | 54% | 83% |
| [test] Spettro Nero | 1664 | 97% | 50% | 72% |
| [test] Orso Verde | 1659 | 94% | 50% | 69% |
| Esca | 1638 | 96% | 49% | 65% |
| [test] Cacciatore Verde | 1623 | 90% | 48% | 73% |
| [test] Flagellante Nero | 1629 | 94% | 47% | 80% |
| [test] Veterano | 2309 | 93% | 46% | 71% |
| Recluta del Crocevia | 2219 | 82% | 46% | 61% |
| Lince del Sottobosco | 1610 | 79% | 46% | 68% |
| Matriarca del Branco | 1343 | 71% | 45% | 60% |
| Patto di Sangue | 1472 | 75% | 45% | 50% |
| Penitente delle Mille Ferite | 1614 | 86% | 45% | 74% |
| [test] Mercenario | 3227 | 81% | 45% | 72% |
| Colpo Mirato | 2854 | 85% | 44% | 80% |
| Carica della Fornace | 1343 | 75% | 43% | 35% |
| [test] Colosso Rosso | 709 | 73% | 43% | 46% |
| Scudiera di Brace | 1562 | 83% | 40% | 53% |
| Vesh, Lama Rovente | 1476 | 95% | 40% | 68% |
| [test] Fabbro Rosso | 1634 | 92% | 40% | 68% |
| [test] Razziatore Rosso | 1585 | 80% | 39% | 52% |
| [test] Orrore Nero | 610 | 73% | 36% | 47% |
| Muro di Scudi | 1633 | 0% | – | 60% |
| Grido dalla Cicatrice | 1568 | 0% | – | 49% |
