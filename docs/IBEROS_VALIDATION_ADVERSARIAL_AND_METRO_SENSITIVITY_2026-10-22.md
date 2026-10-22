# IberOS — Segunda batería de validaciones y pruebas, 22 octubre 2026

## A. VALIDATION-01: robustez de la evaluación ciega

Se actualizó `scripts/validation01_blind_score.py` para rechazar:
1. Duplicidad de `physical_group` dentro del mismo split (antes solo detectaba cruces de split). Se conserva la comprobación anterior `LEAKAGE_BETWEEN_SPLITS`.
2. Fechas de `prediction_locked_at` y `gold_reviewed_at` mal formadas, sin zona horaria, o congelación posterior/no anterior al gold; se comparan instantes reales en vez de cadenas.
3. El campo `predictions_frozen_sha256` exige 64 dígitos hexadecimales. **Importante:** esto valida el formato, **no** demuestra el compromiso criptográfico respecto de un archivo de predicciones ni garantiza que se guardó antes del gold.

Se añadieron cinco casos `tests/test_validation01_blind_score_adversarial.py`: dos grupos válidos solo con puntuación descriptiva; duplicados HOLD; fecha inválida; hash inválido; zona horaria que invierte el orden lexicográfico. **Pruebas escritas y subidas a GitHub. El estado de CI de este commit no se ha verificado en esta tanda; no afirmar que estén verdes.**

El corpus HOLD oficial sigue con 0 filas de prueba. La puntuación de preparación continúa 30/100 y el estado científico VALIDATION-01 **NOT_EVALUATED**.

## B. METRO-AOKI-01: sensibilidad numérica retrospectiva

Fuente: `data/review/metro_aoki_01_exploratory_masses.csv`, siete casos de las fuentes públicas ya utilizadas en el desarrollo. Familias de razones fijas: HÍBRIDO a/o=10 y o/ki=12; DECIMAL 10 y 10; DUODECIMAL 12 y 12. Predicción en gramos `a=(a/o)*o; o=o; ki=o/(o/ki)`. Métrica: raíz de la media de los cuadrados de errores relativos en % sobre las **7 masas**. Cálculo recomputado sin cambiar las masas ni asignaciones.

| o de referencia | RMS híbrido | RMS decimal | RMS duodecimal |
| --- | ---: | ---: | ---: |
| 40 g | 4.237 % | 8.933 % | 8.231 % |
| 41 g | 2.064 % | 9.289 % | 9.355 % |
| 42 g | **1.781 %** | 10.168 % | 10.802 % |
| 43 g | 3.605 % | 11.387 % | 12.405 % |
| 44 g | 5.680 % | 12.798 % | 14.070 % |

Resultado **descriptivo en la muestra conocida**, sin nuevos objetos independientes. El menor RMS del híbrido **en estos cinco escenarios** no proporciona significación estadística ni descarta selección retrospectiva de datos, clases y escala de referencia. METRO-AOKI-01 permanece **NOT_EXTERNALLY_VALIDATED**. Recomendado congelar reglas y obtener masas de objetos físicos distintos antes de evaluación ciega.

## Próximas pruebas separadas
- VALIDATION-01: completar lecturas paleográficas y prueba con evaluador humano; disponer de al menos 20 grupos físicos HOLD nuevos y predicciones congeladas antes del gold.
- METRO-AOKI-01: preregistro de predicción y denominador, búsqueda de pesos nuevos y controles negativos elegidos antes de inspeccionar masas.
- Seguridad de scoring: falta verificar correspondencia criptográfica real con archivo externo y auditar alias de grupos físicos y registros duplicados entre fuentes.

No se promociona ninguna hipótesis científica a validada ni se alteran los porcentajes.
