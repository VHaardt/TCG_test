# Variante V2_g2_six_nospark

- Regole: `v0.1-condiviso`; moduli attivi: primo_turno, saldo, clessidra, crepuscolo_terminale, risveglio, rimarginare, ultimo_respiro
- Parametri diversi dal default: {"modules": ["primo_turno", "saldo", "clessidra", "crepuscolo_terminale", "risveglio", "rimarginare", "ultimo_respiro"], "hand_g2": 6}
- Partite: 2000; IA: semplice; tempo 8s
- Tra parentesi quadre: intervallo di confidenza al 95%.

## Metriche dei pilastri
| Metrica | Valore | Obiettivo | |
|---|---|---|---|
| Durata mediana (turni per giocatore) | 10.0 [10.0–10.5] (media 10.6) | 8–10 | ✅ |
| Partite tra 5 e 15 turni | 100.0% [99.7–100.0] | ≥90% | ✅ |
| Partite oltre il turno 15 | 0.1% [0.0–0.3] | <2% | ✅ |
| Vittorie del primo giocatore | 64.3% [62.2–66.4] | 48–52% | ❌ |
| Rimonte (sotto di ≥2 Vite al turno 6, n=633) | 21.3% [18.3–24.7] | 20–35% | ✅ |
| Attacchi al Leader fermati da una reazione (su 28270 minacce) | 23.1% [22.6–23.6] | 30–45% | ❌ |
| Partite chiuse dal Crepuscolo | 0.8% [0.5–1.3] | <15% | ✅ |
| Rimarginare usato quando possibile | 29.1% [28.4–29.9] | <70% | ✅ |
| Quota di Vite perse per attacchi del Leader | 4.2% | <40% | ✅ |

## Vittorie per mazzo (escluse le partite speculari)
| Mazzo | Vittorie | Obiettivo 45–55% |
|---|---|---|
| maera_blu_nero | 66.5% [62.6–70.2] | ❌ |
| thorn_verde_blu | 61.2% [57.2–65.0] | ❌ |
| vey_nero_rosso | 38.7% [34.9–42.6] | ❌ |
| arden_rosso_verde | 33.7% [30.0–37.5] | ❌ |

## Dettagli
- Fine partita: {"colpo_finale": 1984, "crepuscolo": 16}
- Durata (turni per giocatore → partite): {"7": 5, "8": 106, "9": 470, "10": 469, "11": 452, "12": 232, "13": 204, "14": 40, "15": 21, "16": 1}
- Attacchi al Leader andati a segno: 64.9% [64.4–65.4]
- Partite toccate dal Crepuscolo terminale: 1.1% [0.7–1.7]
- Vite perse per fonte: attacco_unita 88%, costo 7%, attacco_leader 4%, crepuscolo 0%
- Reazioni usate: {"parata": 5238, "muro": 2202, "leader": 363, "grido@cicatrice": 406, "grido": 2135, "muro@cicatrice": 292}
- Guardia accantonata in media per turno: 0.68

## Statistiche per carta
| Carta | Partite in cui pescata | Giocata quando pescata | Vittorie se giocata | Vittorie se rimasta in mano |
|---|---|---|---|---|
| Il Bastione Vivente | 1441 | 73% | 63% | 54% |
| [test] Guardiano Blu | 1572 | 93% | 59% | 83% |
| [test] Leviatano Blu | 715 | 72% | 56% | 70% |
| Lanterna del Pellegrino | 1387 | 91% | 55% | 57% |
| Sentinella del Guado | 1645 | 80% | 55% | 70% |
| [test] Custode Blu | 1729 | 90% | 54% | 78% |
| [test] Antico Verde | 699 | 69% | 52% | 61% |
| [test] Spettro Nero | 1701 | 97% | 51% | 83% |
| [test] Orso Verde | 1653 | 94% | 49% | 67% |
| [test] Flagellante Nero | 1655 | 94% | 49% | 75% |
| Recluta del Crocevia | 2240 | 80% | 48% | 57% |
| Patto di Sangue | 1491 | 66% | 47% | 50% |
| Penitente delle Mille Ferite | 1638 | 86% | 47% | 71% |
| Esca | 1650 | 95% | 46% | 68% |
| [test] Veterano | 2354 | 94% | 46% | 66% |
| [test] Mercenario | 3268 | 82% | 46% | 66% |
| [test] Cacciatore Verde | 1649 | 87% | 46% | 66% |
| Lince del Sottobosco | 1648 | 79% | 45% | 64% |
| Matriarca del Branco | 1374 | 69% | 44% | 55% |
| Colpo Mirato | 2892 | 85% | 44% | 80% |
| Carica della Fornace | 1355 | 76% | 44% | 35% |
| Scudiera di Brace | 1599 | 81% | 41% | 47% |
| [test] Colosso Rosso | 693 | 71% | 41% | 41% |
| [test] Fabbro Rosso | 1636 | 89% | 40% | 59% |
| [test] Orrore Nero | 627 | 69% | 40% | 52% |
| [test] Razziatore Rosso | 1607 | 81% | 38% | 53% |
| Vesh, Lama Rovente | 1482 | 95% | 38% | 64% |
| Muro di Scudi | 1670 | 0% | – | 59% |
| Grido dalla Cicatrice | 1603 | 0% | – | 52% |
