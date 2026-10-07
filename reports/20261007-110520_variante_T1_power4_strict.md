# Variante T1_power4_strict

- Regole: `v0.1-condiviso`; moduli attivi: primo_turno, scintilla, saldo, clessidra, crepuscolo_terminale, risveglio, rimarginare, ultimo_respiro
- Parametri diversi dal default: {"leader_power": 4, "leader_power_awakened": 5, "leader_tempra": 4, "leader_hit_strict": true}
- Partite: 2000; IA: semplice; tempo 9s
- Tra parentesi quadre: intervallo di confidenza al 95%.

## Metriche dei pilastri
| Metrica | Valore | Obiettivo | |
|---|---|---|---|
| Durata mediana (turni per giocatore) | 11.0 [11.0–11.0] (media 10.7) | 8–10 | ❌ |
| Partite tra 5 e 15 turni | 100.0% [99.8–100.0] | ≥90% | ✅ |
| Partite oltre il turno 15 | 0.0% [0.0–0.2] | <2% | ✅ |
| Vittorie del primo giocatore | 60.7% [58.5–62.8] | 48–52% | ❌ |
| Rimonte (sotto di ≥2 Vite al turno 6, n=665) | 35.6% [32.1–39.4] | 20–35% | ❌ |
| Attacchi al Leader fermati da una reazione (su 30812 minacce) | 25.9% [25.4–26.4] | 30–45% | ❌ |
| Partite chiuse dal Crepuscolo | 0.9% [0.6–1.4] | <15% | ✅ |
| Rimarginare usato quando possibile | 10.8% [10.4–11.3] | <70% | ✅ |
| Quota di Vite perse per attacchi del Leader | 16.1% | <40% | ✅ |

## Vittorie per mazzo (escluse le partite speculari)
| Mazzo | Vittorie | Obiettivo 45–55% |
|---|---|---|
| maera_blu_nero | 66.2% [62.3–69.8] | ❌ |
| thorn_verde_blu | 56.5% [52.5–60.4] | ❌ |
| arden_rosso_verde | 40.8% [37.0–44.8] | ❌ |
| vey_nero_rosso | 36.5% [32.7–40.4] | ❌ |

## Dettagli
- Fine partita: {"colpo_finale": 1982, "crepuscolo": 18}
- Durata (turni per giocatore → partite): {"7": 1, "8": 74, "9": 362, "10": 510, "11": 512, "12": 290, "13": 201, "14": 29, "15": 21}
- Attacchi al Leader andati a segno: 62.8% [62.3–63.3]
- Partite toccate dal Crepuscolo terminale: 1.1% [0.7–1.6]
- Vite perse per fonte: attacco_unita 76%, attacco_leader 16%, costo 8%, crepuscolo 0%
- Reazioni usate: {"parata": 7205, "muro": 2301, "leader": 263, "grido": 2161, "grido@cicatrice": 426, "muro@cicatrice": 382}
- Guardia accantonata in media per turno: 0.86

## Statistiche per carta
| Carta | Partite in cui pescata | Giocata quando pescata | Vittorie se giocata | Vittorie se rimasta in mano |
|---|---|---|---|---|
| Il Bastione Vivente | 1355 | 76% | 65% | 54% |
| [test] Leviatano Blu | 673 | 71% | 59% | 64% |
| [test] Guardiano Blu | 1517 | 95% | 58% | 75% |
| [test] Custode Blu | 1687 | 94% | 56% | 80% |
| Lanterna del Pellegrino | 1360 | 93% | 54% | 66% |
| Sentinella del Guado | 1626 | 87% | 54% | 78% |
| [test] Antico Verde | 666 | 72% | 52% | 58% |
| [test] Flagellante Nero | 1630 | 96% | 51% | 78% |
| [test] Spettro Nero | 1623 | 98% | 51% | 91% |
| [test] Orso Verde | 1627 | 96% | 49% | 73% |
| Penitente delle Mille Ferite | 1612 | 91% | 48% | 76% |
| [test] Cacciatore Verde | 1631 | 93% | 48% | 71% |
| Recluta del Crocevia | 2218 | 86% | 48% | 62% |
| Esca | 1632 | 96% | 48% | 70% |
| [test] Colosso Rosso | 672 | 72% | 48% | 46% |
| [test] Mercenario | 3222 | 87% | 47% | 71% |
| Lince del Sottobosco | 1620 | 83% | 47% | 64% |
| Patto di Sangue | 1479 | 73% | 46% | 57% |
| [test] Veterano | 2267 | 95% | 46% | 74% |
| Matriarca del Branco | 1329 | 70% | 46% | 56% |
| Carica della Fornace | 1319 | 79% | 44% | 44% |
| Colpo Mirato | 2803 | 86% | 44% | 79% |
| Vesh, Lama Rovente | 1447 | 96% | 43% | 58% |
| Scudiera di Brace | 1574 | 87% | 43% | 61% |
| [test] Fabbro Rosso | 1618 | 94% | 41% | 72% |
| [test] Razziatore Rosso | 1592 | 85% | 41% | 58% |
| [test] Orrore Nero | 594 | 71% | 39% | 43% |
| Muro di Scudi | 1648 | 0% | – | 57% |
| Grido dalla Cicatrice | 1579 | 0% | – | 52% |
