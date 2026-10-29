# IberOS — Verificación local de pruebas adversariales y metrología (22-10-2026)

## Validación ciega
Se recuperaron los contenidos actuales del repositorio de `scripts/validation01_blind_score.py` y `tests/test_validation01_blind_score_adversarial.py`. Se ejecutó Python pytest en copia local, cambiando **solo la ruta de importación** para importar el script local. **Resultado: 5 passed in 0.08s**. Casos: duplicidad de grupos HOLD, fechas inválidas, SHA-256 mal formado, inversión de zonas horarias, y aceptación de dos grupos válidos exclusivamente para puntuación descriptiva.

No se ha validado criptográficamente que la huella corresponda a un fichero congelado ni comprobado los alias arbitrarios de `physical_group`. No se ha verificado en esta tanda el CI de GitHub Actions.

## Sensibilidad METRO-AOKI
Recomputadas las siete filas de `data/review/metro_aoki_01_exploratory_masses.csv` (todas IN_SAMPLE). Error cuadrático medio de errores relativos porcentuales:
| o de referencia (g) | Híbrido (10,12) | Decimal (10,10) | Duodecimal (12,12) |
| ---: | ---: | ---: | ---: |
| 40 | 4.2374 | 8.9333 | 8.2308 |
| 41 | 2.0642 | 9.2887 | 9.3547 |
| 42 | 1.7812 | 10.1682 | 10.8016 |
| 43 | 3.6051 | 11.3866 | 12.4048 |
| 44 | 5.6802 | 12.7977 | 14.0695 |

El mejor ajuste retrospectivo no constituye superioridad predictiva externa; no se añaden muestras prospectivas ni gold independiente.

## Estados
VALIDATION-01 30 % de preparación administrativa, `NOT_EVALUATED`; M06/M07 pendientes; METRO-AOKI-01 `NOT_EXTERNALLY_VALIDATED`. Próximo refuerzo: alias y normalización de grupos físicos, comprobar hashes contra artefactos reales comprometidos y preparar catálogo de muestras realmente no expuestas al desarrollo.