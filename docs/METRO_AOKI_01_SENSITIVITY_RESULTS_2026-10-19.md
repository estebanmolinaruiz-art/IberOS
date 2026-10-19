# IberOS — METRO-AOKI-01: sensibilidad retrospectiva de modelos
Fecha: 2026-10-19

Se compararon los modelos H (a/o=10,o/ki=12), D (10,10) y U (12,12) sobre 7 masas citadas por Ferrer i Jané; todas se consideran **IN_SAMPLE**.

## Valores de referencia: análisis de errores relativos RMSE
| o(g) | H RMSE % | D RMSE % | U RMSE % |
| --- | ---: | ---: | ---: |
| 41 | 2.06 | 9.29 | 9.35 |
| 42 | 1.78 | 10.17 | 10.80 |
| 43 | 3.61 | 11.39 | 12.40 |

En nueve puntos entre 41 y 43 g, cada 0,25g, H obtiene menor RMSE que D y U. Excluyendo una observación cada vez de las siete, con o=42g fijo, H obtiene menor error en 7 de 7 comparaciones. Son **análisis internos de sensibilidad, no HOLD, no predicción a ciegas, ni independencia estadística**.

## Limitaciones de inferencia
- Asignaciones de unidad por pieza proceden de la interpretación del autor y aún no están verificadas paleográficamente objeto por objeto.
- La masa de o y las relaciones se extraen de un contexto en el que se formuló la hipótesis.
- LOO de siete filas no implica siete experimentos independientes ni evalúa sensibilidad a eliminar series arqueológicas completas.
- No se ha modelado incertidumbre de balanza ni dispersión arqueológica, datos cronológicos o calibración global óptima por modelo.
- No hay examen del PDF íntegro ni verificación del valor de 41,29g del Puig de la Misericòrdia en tabla primaria.
- Mejor ajuste de masas no verifica la semántica `abaŕ`, `otar`, `kitar`.
- **METRO-AOKI-01: NOT_EXTERNALLY_VALIDATED. VALIDATION-01 (TE): NOT_EVALUATED.**

Reproducibilidad:
`python scripts/metro_aoki_sensitivity.py data/review/metro_aoki_01_exploratory_masses.csv`
