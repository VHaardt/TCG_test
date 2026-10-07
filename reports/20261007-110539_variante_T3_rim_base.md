# Variante T3_rim_base

- Regole: `v0.1-condiviso`; moduli attivi: primo_turno, scintilla, saldo, clessidra, crepuscolo_terminale, risveglio, rimarginare, ultimo_respiro
- Parametri diversi dal default: {"rimarginare_mode": "base"}
- Partite: 2000; IA: semplice; tempo 9s
- Tra parentesi quadre: intervallo di confidenza al 95%.

## Metriche dei pilastri
| Metrica | Valore | Obiettivo | |
|---|---|---|---|
| Durata mediana (turni per giocatore) | 10.0 [10.0–11.0] (media 10.5) | 8–10 | ✅ |
| Partite tra 5 e 15 turni | 100.0% [99.7–100.0] | ≥90% | ✅ |
| Partite oltre il turno 15 | 0.1% [0.0–0.3] | <2% | ✅ |
| Vittorie del primo giocatore | 63.7% [61.6–65.8] | 48–52% | ❌ |
| Rimonte (sotto di ≥2 Vite al turno 6, n=673) | 27.6% [24.4–31.1] | 20–35% | ✅ |
| Attacchi al Leader fermati da una reazione (su 27488 minacce) | 23.0% [22.5–23.5] | 30–45% | ❌ |
| Partite chiuse dal Crepuscolo | 0.5% [0.3–1.0] | <15% | ✅ |
| Rimarginare usato quando possibile | 52.3% [51.5–53.1] | <70% | ✅ |
| Quota di Vite perse per attacchi del Leader | 4.1% | <40% | ✅ |

## Vittorie per mazzo (escluse le partite speculari)
| Mazzo | Vittorie | Obiettivo 45–55% |
|---|---|---|
| maera_blu_nero | 66.0% [62.1–69.7] | ❌ |
| thorn_verde_blu | 62.7% [58.7–66.4] | ❌ |
| arden_rosso_verde | 38.3% [34.5–42.3] | ❌ |
| vey_nero_rosso | 33.0% [29.4–36.9] | ❌ |

## Dettagli
- Fine partita: {"colpo_finale": 1989, "crepuscolo": 11}
- Durata (turni per giocatore → partite): {"7": 3, "8": 119, "9": 477, "10": 442, "11": 442, "12": 266, "13": 198, "14": 34, "15": 18, "16": 1}
- Attacchi al Leader andati a segno: 64.7% [64.2–65.3]
- Partite toccate dal Crepuscolo terminale: 0.9% [0.6–1.5]
- Vite perse per fonte: attacco_unita 87%, costo 8%, attacco_leader 4%, crepuscolo 0%
- Reazioni usate: {"parata": 5110, "muro": 2126, "leader": 481, "grido@cicatrice": 398, "grido": 2005, "muro@cicatrice": 286}
- Guardia accantonata in media per turno: 0.64

## Statistiche per carta
| Carta | Partite in cui pescata | Giocata quando pescata | Vittorie se giocata | Vittorie se rimasta in mano |
|---|---|---|---|---|
| Il Bastione Vivente | 1420 | 76% | 64% | 55% |
| [test] Guardiano Blu | 1566 | 93% | 59% | 77% |
| [test] Custode Blu | 1717 | 91% | 56% | 84% |
| Lanterna del Pellegrino | 1397 | 93% | 55% | 68% |
| [test] Leviatano Blu | 719 | 76% | 53% | 70% |
| [test] Antico Verde | 689 | 72% | 53% | 65% |
| Sentinella del Guado | 1644 | 81% | 53% | 82% |
| [test] Orso Verde | 1680 | 93% | 50% | 75% |
| [test] Spettro Nero | 1682 | 97% | 50% | 74% |
| Esca | 1639 | 96% | 49% | 65% |
| [test] Cacciatore Verde | 1632 | 90% | 48% | 71% |
| [test] Flagellante Nero | 1652 | 93% | 47% | 69% |
| [test] Veterano | 2349 | 93% | 46% | 66% |
| Matriarca del Branco | 1363 | 71% | 45% | 59% |
| Lince del Sottobosco | 1617 | 78% | 45% | 67% |
| Recluta del Crocevia | 2223 | 81% | 45% | 63% |
| Penitente delle Mille Ferite | 1634 | 85% | 45% | 70% |
| [test] Mercenario | 3249 | 81% | 45% | 72% |
| Patto di Sangue | 1475 | 75% | 45% | 51% |
| Carica della Fornace | 1354 | 75% | 44% | 34% |
| Colpo Mirato | 2878 | 84% | 44% | 79% |
| [test] Colosso Rosso | 720 | 74% | 43% | 47% |
| [test] Fabbro Rosso | 1643 | 91% | 40% | 64% |
| Vesh, Lama Rovente | 1483 | 95% | 40% | 63% |
| Scudiera di Brace | 1563 | 83% | 40% | 54% |
| [test] Razziatore Rosso | 1598 | 79% | 38% | 52% |
| [test] Orrore Nero | 634 | 74% | 36% | 48% |
| Muro di Scudi | 1633 | 0% | – | 59% |
| Grido dalla Cicatrice | 1572 | 0% | – | 50% |
