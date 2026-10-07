# Variante T2_bozza_crepuscolo

- Regole: `v0.1-condiviso`; moduli attivi: primo_turno, scintilla, saldo, risveglio, rimarginare, ultimo_respiro, crepuscolo_bozza
- Parametri diversi dal default: {"modules": ["primo_turno", "scintilla", "saldo", "risveglio", "rimarginare", "ultimo_respiro", "crepuscolo_bozza"]}
- Partite: 2000; IA: semplice; tempo 8s
- Tra parentesi quadre: intervallo di confidenza al 95%.

## Metriche dei pilastri
| Metrica | Valore | Obiettivo | |
|---|---|---|---|
| Durata mediana (turni per giocatore) | 10.0 [10.0–10.0] (media 9.9) | 8–10 | ✅ |
| Partite tra 5 e 15 turni | 100.0% [99.8–100.0] | ≥90% | ✅ |
| Partite oltre il turno 15 | 0.0% [0.0–0.2] | <2% | ✅ |
| Vittorie del primo giocatore | 59.3% [57.1–61.4] | 48–52% | ❌ |
| Rimonte (sotto di ≥2 Vite al turno 6, n=672) | 24.1% [21.0–27.5] | 20–35% | ✅ |
| Attacchi al Leader fermati da una reazione (su 24216 minacce) | 23.4% [22.9–24.0] | 30–45% | ❌ |
| Partite chiuse dal Crepuscolo | 40.4% [38.3–42.6] | <15% | ❌ |
| Rimarginare usato quando possibile | 33.6% [32.7–34.4] | <70% | ✅ |
| Quota di Vite perse per attacchi del Leader | 2.9% | <40% | ✅ |

## Vittorie per mazzo (escluse le partite speculari)
| Mazzo | Vittorie | Obiettivo 45–55% |
|---|---|---|
| maera_blu_nero | 65.5% [61.6–69.2] | ❌ |
| thorn_verde_blu | 60.2% [56.2–64.0] | ❌ |
| arden_rosso_verde | 39.7% [35.8–43.6] | ❌ |
| vey_nero_rosso | 34.7% [31.0–38.6] | ❌ |

## Dettagli
- Fine partita: {"colpo_finale": 1192, "crepuscolo": 808}
- Durata (turni per giocatore → partite): {"7": 3, "8": 124, "9": 470, "10": 871, "11": 441, "12": 89, "13": 2}
- Attacchi al Leader andati a segno: 64.2% [63.6–64.7]
- Partite toccate dal Crepuscolo terminale: 70.2% [68.1–72.1]
- Vite perse per fonte: attacco_unita 75%, crepuscolo 15%, costo 8%, attacco_leader 3%
- Reazioni usate: {"parata": 4495, "muro": 1902, "leader": 327, "grido@cicatrice": 334, "grido": 1846, "muro@cicatrice": 227}
- Guardia accantonata in media per turno: 0.66

## Statistiche per carta
| Carta | Partite in cui pescata | Giocata quando pescata | Vittorie se giocata | Vittorie se rimasta in mano |
|---|---|---|---|---|
| Il Bastione Vivente | 1327 | 74% | 64% | 54% |
| [test] Guardiano Blu | 1492 | 93% | 60% | 78% |
| [test] Custode Blu | 1651 | 92% | 55% | 82% |
| [test] Leviatano Blu | 669 | 73% | 54% | 64% |
| Lanterna del Pellegrino | 1300 | 93% | 54% | 51% |
| Sentinella del Guado | 1593 | 80% | 53% | 77% |
| [test] Antico Verde | 645 | 69% | 53% | 62% |
| [test] Spettro Nero | 1616 | 97% | 51% | 68% |
| [test] Orso Verde | 1601 | 94% | 50% | 65% |
| Esca | 1594 | 96% | 50% | 50% |
| [test] Flagellante Nero | 1590 | 94% | 48% | 70% |
| [test] Veterano | 2226 | 93% | 48% | 64% |
| Recluta del Crocevia | 2151 | 81% | 48% | 59% |
| [test] Cacciatore Verde | 1596 | 89% | 48% | 69% |
| Carica della Fornace | 1291 | 73% | 47% | 34% |
| Lince del Sottobosco | 1573 | 78% | 46% | 64% |
| Penitente delle Mille Ferite | 1561 | 85% | 46% | 70% |
| Matriarca del Branco | 1287 | 70% | 46% | 59% |
| [test] Mercenario | 3130 | 80% | 46% | 68% |
| Colpo Mirato | 2730 | 83% | 45% | 72% |
| Patto di Sangue | 1422 | 75% | 43% | 54% |
| [test] Colosso Rosso | 678 | 71% | 43% | 51% |
| Scudiera di Brace | 1522 | 84% | 42% | 52% |
| Vesh, Lama Rovente | 1421 | 96% | 42% | 60% |
| [test] Fabbro Rosso | 1595 | 91% | 42% | 61% |
| [test] Razziatore Rosso | 1553 | 79% | 40% | 52% |
| [test] Orrore Nero | 597 | 71% | 38% | 47% |
| Muro di Scudi | 1589 | 0% | – | 59% |
| Grido dalla Cicatrice | 1539 | 0% | – | 50% |
