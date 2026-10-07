# Variante V1b_per_attack

- Regole: `v0.1-condiviso`; moduli attivi: primo_turno, scintilla, saldo, clessidra, crepuscolo_terminale, risveglio, rimarginare, reazione_per_attacco
- Parametri diversi dal default: {"modules": ["primo_turno", "scintilla", "saldo", "clessidra", "crepuscolo_terminale", "risveglio", "rimarginare", "reazione_per_attacco"]}
- Partite: 2000; IA: semplice; tempo 9s
- Tra parentesi quadre: intervallo di confidenza al 95%.

## Metriche dei pilastri
| Metrica | Valore | Obiettivo | |
|---|---|---|---|
| Durata mediana (turni per giocatore) | 11.0 [11.0–11.0] (media 10.9) | 8–10 | ❌ |
| Partite tra 5 e 15 turni | 98.4% [97.8–98.9] | ≥90% | ✅ |
| Partite oltre il turno 15 | 1.6% [1.1–2.2] | <2% | ✅ |
| Vittorie del primo giocatore | 64.1% [62.0–66.2] | 48–52% | ❌ |
| Rimonte (sotto di ≥2 Vite al turno 6, n=680) | 28.1% [24.8–31.6] | 20–35% | ✅ |
| Attacchi al Leader fermati da una reazione (su 30232 minacce) | 35.0% [34.4–35.5] | 30–45% | ✅ |
| Partite chiuse dal Crepuscolo | 3.1% [2.5–4.0] | <15% | ✅ |
| Rimarginare usato quando possibile | 30.8% [30.0–31.5] | <70% | ✅ |
| Quota di Vite perse per attacchi del Leader | 5.2% | <40% | ✅ |

## Vittorie per mazzo (escluse le partite speculari)
| Mazzo | Vittorie | Obiettivo 45–55% |
|---|---|---|
| maera_blu_nero | 73.3% [69.7–76.7] | ❌ |
| thorn_verde_blu | 55.7% [51.7–59.6] | ❌ |
| vey_nero_rosso | 36.3% [32.6–40.3] | ❌ |
| arden_rosso_verde | 34.7% [31.0–38.6] | ❌ |

## Dettagli
- Fine partita: {"colpo_finale": 1937, "crepuscolo": 63}
- Durata (turni per giocatore → partite): {"7": 3, "8": 120, "9": 409, "10": 423, "11": 371, "12": 245, "13": 262, "14": 59, "15": 76, "16": 29, "17": 3}
- Attacchi al Leader andati a segno: 55.3% [54.7–55.8]
- Partite toccate dal Crepuscolo terminale: 5.4% [4.5–6.5]
- Vite perse per fonte: attacco_unita 83%, costo 9%, attacco_leader 5%, crepuscolo 2%
- Reazioni usate: {"parata": 11136, "muro": 2291, "leader": 1397, "grido@cicatrice": 422, "grido": 2205, "muro@cicatrice": 318}
- Guardia accantonata in media per turno: 0.78

## Statistiche per carta
| Carta | Partite in cui pescata | Giocata quando pescata | Vittorie se giocata | Vittorie se rimasta in mano |
|---|---|---|---|---|
| Il Bastione Vivente | 1406 | 76% | 64% | 57% |
| [test] Leviatano Blu | 708 | 73% | 60% | 70% |
| [test] Guardiano Blu | 1552 | 93% | 59% | 85% |
| [test] Custode Blu | 1716 | 92% | 56% | 84% |
| Lanterna del Pellegrino | 1389 | 94% | 55% | 60% |
| Sentinella del Guado | 1644 | 82% | 53% | 84% |
| [test] Spettro Nero | 1680 | 96% | 53% | 76% |
| [test] Flagellante Nero | 1655 | 95% | 51% | 80% |
| [test] Antico Verde | 672 | 71% | 51% | 58% |
| Patto di Sangue | 1479 | 77% | 49% | 54% |
| Penitente delle Mille Ferite | 1641 | 85% | 48% | 74% |
| Recluta del Crocevia | 2242 | 83% | 48% | 66% |
| Esca | 1634 | 96% | 47% | 64% |
| [test] Orso Verde | 1673 | 94% | 46% | 74% |
| [test] Veterano | 2328 | 94% | 44% | 73% |
| [test] Mercenario | 3256 | 82% | 44% | 75% |
| Carica della Fornace | 1354 | 77% | 44% | 33% |
| [test] Cacciatore Verde | 1640 | 90% | 43% | 76% |
| Colpo Mirato | 2866 | 84% | 43% | 82% |
| Lince del Sottobosco | 1627 | 79% | 42% | 70% |
| Matriarca del Branco | 1350 | 72% | 41% | 58% |
| [test] Colosso Rosso | 702 | 74% | 41% | 46% |
| [test] Fabbro Rosso | 1652 | 92% | 40% | 66% |
| Scudiera di Brace | 1570 | 84% | 40% | 60% |
| [test] Orrore Nero | 627 | 73% | 40% | 48% |
| Vesh, Lama Rovente | 1484 | 96% | 40% | 69% |
| [test] Razziatore Rosso | 1598 | 81% | 36% | 62% |
| Muro di Scudi | 1655 | 0% | – | 60% |
| Grido dalla Cicatrice | 1594 | 0% | – | 54% |
