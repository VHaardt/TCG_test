# Variante T3_riscossa

- Regole: `v0.1-condiviso`; moduli attivi: primo_turno, scintilla, saldo, clessidra, crepuscolo_terminale, risveglio, ultimo_respiro, riscossa
- Parametri diversi dal default: {"modules": ["primo_turno", "scintilla", "saldo", "clessidra", "crepuscolo_terminale", "risveglio", "ultimo_respiro", "riscossa"]}
- Partite: 2000; IA: semplice; tempo 9s
- Tra parentesi quadre: intervallo di confidenza al 95%.

## Metriche dei pilastri
| Metrica | Valore | Obiettivo | |
|---|---|---|---|
| Durata mediana (turni per giocatore) | 10.0 [10.0–11.0] (media 10.6) | 8–10 | ✅ |
| Partite tra 5 e 15 turni | 100.0% [99.7–100.0] | ≥90% | ✅ |
| Partite oltre il turno 15 | 0.1% [0.0–0.3] | <2% | ✅ |
| Vittorie del primo giocatore | 64.5% [62.4–66.6] | 48–52% | ❌ |
| Rimonte (sotto di ≥2 Vite al turno 6, n=649) | 27.7% [24.4–31.3] | 20–35% | ✅ |
| Attacchi al Leader fermati da una reazione (su 27897 minacce) | 25.4% [24.9–25.9] | 30–45% | ❌ |
| Partite chiuse dal Crepuscolo | 0.9% [0.6–1.4] | <15% | ✅ |
| Rimarginare usato quando possibile | nan% [nan–nan] | <70% | ❌ |
| Quota di Vite perse per attacchi del Leader | 4.3% | <40% | ✅ |

## Vittorie per mazzo (escluse le partite speculari)
| Mazzo | Vittorie | Obiettivo 45–55% |
|---|---|---|
| thorn_verde_blu | 64.8% [60.9–68.5] | ❌ |
| maera_blu_nero | 64.3% [60.4–68.1] | ❌ |
| arden_rosso_verde | 43.2% [39.3–47.2] | ❌ |
| vey_nero_rosso | 27.7% [24.2–31.4] | ❌ |

## Dettagli
- Fine partita: {"colpo_finale": 1982, "crepuscolo": 18}
- Durata (turni per giocatore → partite): {"8": 96, "9": 461, "10": 468, "11": 430, "12": 249, "13": 226, "14": 45, "15": 24, "16": 1}
- Attacchi al Leader andati a segno: 62.8% [62.3–63.3]
- Partite toccate dal Crepuscolo terminale: 1.2% [0.8–1.8]
- Vite perse per fonte: attacco_unita 88%, costo 7%, attacco_leader 4%, crepuscolo 0%
- Reazioni usate: {"parata": 5893, "muro": 2416, "leader": 577, "grido": 2350, "grido@cicatrice": 113, "muro@cicatrice": 74}
- Guardia accantonata in media per turno: 0.76

## Statistiche per carta
| Carta | Partite in cui pescata | Giocata quando pescata | Vittorie se giocata | Vittorie se rimasta in mano |
|---|---|---|---|---|
| Il Bastione Vivente | 1468 | 77% | 63% | 54% |
| [test] Guardiano Blu | 1595 | 91% | 59% | 77% |
| Lanterna del Pellegrino | 1438 | 92% | 56% | 52% |
| [test] Custode Blu | 1733 | 90% | 55% | 80% |
| Sentinella del Guado | 1676 | 77% | 54% | 72% |
| [test] Antico Verde | 720 | 72% | 53% | 68% |
| [test] Orso Verde | 1695 | 93% | 52% | 63% |
| [test] Leviatano Blu | 734 | 75% | 51% | 73% |
| Esca | 1700 | 96% | 51% | 56% |
| Lince del Sottobosco | 1656 | 74% | 50% | 58% |
| [test] Cacciatore Verde | 1669 | 89% | 50% | 68% |
| [test] Spettro Nero | 1700 | 96% | 48% | 55% |
| Matriarca del Branco | 1379 | 72% | 48% | 59% |
| [test] Veterano | 2416 | 92% | 46% | 70% |
| [test] Mercenario | 3297 | 77% | 46% | 62% |
| Carica della Fornace | 1388 | 78% | 45% | 30% |
| Recluta del Crocevia | 2256 | 78% | 44% | 59% |
| [test] Colosso Rosso | 722 | 75% | 44% | 46% |
| [test] Flagellante Nero | 1678 | 93% | 43% | 70% |
| Penitente delle Mille Ferite | 1632 | 83% | 43% | 67% |
| Colpo Mirato | 2961 | 83% | 43% | 81% |
| Patto di Sangue | 1475 | 67% | 42% | 46% |
| Scudiera di Brace | 1602 | 80% | 40% | 55% |
| Vesh, Lama Rovente | 1504 | 94% | 40% | 57% |
| [test] Fabbro Rosso | 1677 | 89% | 39% | 59% |
| [test] Razziatore Rosso | 1623 | 75% | 38% | 49% |
| [test] Orrore Nero | 651 | 73% | 31% | 47% |
| Muro di Scudi | 1640 | 0% | – | 59% |
| Grido dalla Cicatrice | 1575 | 0% | – | 47% |
