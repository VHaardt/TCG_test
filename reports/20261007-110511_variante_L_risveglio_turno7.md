# Variante L_risveglio_turno7

- Regole: `v0.1-condiviso`; moduli attivi: primo_turno, scintilla, saldo, clessidra, crepuscolo_terminale, risveglio, rimarginare, ultimo_respiro, risveglio_a_tempo
- Parametri diversi dal default: {"modules": ["primo_turno", "scintilla", "saldo", "clessidra", "crepuscolo_terminale", "risveglio", "rimarginare", "ultimo_respiro", "risveglio_a_tempo"]}
- Partite: 2000; IA: semplice; tempo 8s
- Tra parentesi quadre: intervallo di confidenza al 95%.

## Metriche dei pilastri
| Metrica | Valore | Obiettivo | |
|---|---|---|---|
| Durata mediana (turni per giocatore) | 10.0 [10.0–10.0] (media 10.4) | 8–10 | ✅ |
| Partite tra 5 e 15 turni | 100.0% [99.7–100.0] | ≥90% | ✅ |
| Partite oltre il turno 15 | 0.1% [0.0–0.3] | <2% | ✅ |
| Vittorie del primo giocatore | 67.6% [65.5–69.6] | 48–52% | ❌ |
| Rimonte (sotto di ≥2 Vite al turno 6, n=672) | 22.0% [19.1–25.3] | 20–35% | ✅ |
| Attacchi al Leader fermati da una reazione (su 27977 minacce) | 24.4% [23.9–24.9] | 30–45% | ❌ |
| Partite chiuse dal Crepuscolo | 0.8% [0.5–1.3] | <15% | ✅ |
| Rimarginare usato quando possibile | 28.9% [28.1–29.6] | <70% | ✅ |
| Quota di Vite perse per attacchi del Leader | 6.7% | <40% | ✅ |

## Vittorie per mazzo (escluse le partite speculari)
| Mazzo | Vittorie | Obiettivo 45–55% |
|---|---|---|
| maera_blu_nero | 65.2% [61.3–68.9] | ❌ |
| thorn_verde_blu | 61.8% [57.9–65.6] | ❌ |
| arden_rosso_verde | 38.5% [34.7–42.5] | ❌ |
| vey_nero_rosso | 34.5% [30.8–38.4] | ❌ |

## Dettagli
- Fine partita: {"colpo_finale": 1984, "crepuscolo": 16}
- Durata (turni per giocatore → partite): {"7": 3, "8": 133, "9": 551, "10": 477, "11": 370, "12": 222, "13": 181, "14": 41, "15": 21, "16": 1}
- Attacchi al Leader andati a segno: 63.9% [63.4–64.4]
- Partite toccate dal Crepuscolo terminale: 1.1% [0.7–1.7]
- Vite perse per fonte: attacco_unita 85%, costo 8%, attacco_leader 7%, crepuscolo 0%
- Reazioni usate: {"parata": 5794, "muro": 2158, "grido@cicatrice": 409, "leader": 127, "grido": 2027, "muro@cicatrice": 290}
- Guardia accantonata in media per turno: 0.74

## Statistiche per carta
| Carta | Partite in cui pescata | Giocata quando pescata | Vittorie se giocata | Vittorie se rimasta in mano |
|---|---|---|---|---|
| Il Bastione Vivente | 1386 | 75% | 63% | 54% |
| [test] Guardiano Blu | 1531 | 93% | 58% | 79% |
| [test] Custode Blu | 1698 | 92% | 56% | 79% |
| [test] Leviatano Blu | 697 | 73% | 55% | 63% |
| Sentinella del Guado | 1619 | 83% | 55% | 77% |
| Lanterna del Pellegrino | 1358 | 92% | 54% | 59% |
| [test] Antico Verde | 666 | 70% | 52% | 67% |
| [test] Spettro Nero | 1651 | 96% | 50% | 70% |
| [test] Orso Verde | 1636 | 93% | 49% | 69% |
| Esca | 1613 | 95% | 49% | 61% |
| Lince del Sottobosco | 1596 | 78% | 48% | 62% |
| [test] Cacciatore Verde | 1608 | 89% | 48% | 74% |
| [test] Flagellante Nero | 1627 | 94% | 47% | 75% |
| [test] Veterano | 2277 | 93% | 47% | 65% |
| Penitente delle Mille Ferite | 1598 | 86% | 46% | 71% |
| [test] Mercenario | 3188 | 82% | 46% | 70% |
| Recluta del Crocevia | 2191 | 83% | 46% | 62% |
| Matriarca del Branco | 1307 | 70% | 44% | 59% |
| Patto di Sangue | 1466 | 74% | 44% | 51% |
| Carica della Fornace | 1314 | 73% | 43% | 36% |
| Scudiera di Brace | 1547 | 83% | 42% | 54% |
| Colpo Mirato | 2809 | 83% | 42% | 81% |
| [test] Fabbro Rosso | 1610 | 90% | 41% | 62% |
| Vesh, Lama Rovente | 1450 | 95% | 40% | 65% |
| [test] Razziatore Rosso | 1565 | 79% | 40% | 49% |
| [test] Colosso Rosso | 670 | 73% | 39% | 48% |
| [test] Orrore Nero | 610 | 72% | 36% | 48% |
| Muro di Scudi | 1636 | 0% | – | 59% |
| Grido dalla Cicatrice | 1563 | 0% | – | 50% |
