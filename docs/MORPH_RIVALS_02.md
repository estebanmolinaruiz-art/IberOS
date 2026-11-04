# MORPH-RIVALS-02 — Hipótesis rivales sobre BI-N y control BA-N

**Estado:** análisis retrospectivo post hoc sobre el histórico FULL3406.
La investigación previa ya vio patrones en TRAIN, VAL y HOLD: no se
presenta este estudio como validación genuinamente ciega. **En esta
ejecución HOLD queda sellado y no se consulta su firma**.

## Hipótesis rivales y regla de observación

- **H1 (posición terminal):** BI-N es una construcción que favorece el
  final de segmento por encima de un bigrama de control BA-N.
- **H2 (contextual/no terminación general):** BI-N aparece en posiciones
  diversas y podría ser parte de nombres o fórmulas, no un sufijo
  productivo de posición terminal general.
- **H3 (numeral/valor dos):** requiere etiquetas cuantitativas
  independientes y hallazgos numéricos; **NO EVALUABLE** solo con
  distribución de grafemas.

Controles: BA-N (comparador primario), A-N (comparador secundario) y
BI-R1 (misma sílaba inicial). Se cuentan apariciones, UID y grupos de
dependencia, más observaciones que terminan un segmento delimitado por
`¦`, `:`, `;`, `∏` o `│`. Los signos R/R1 se mantienen distintos.

### Lectura sobre el histórico (NO nuevo conjunto ciego)

| Métrica | TRAIN | VAL |
| --- | ---: | ---: |
| BI-N apariciones al final/total | 9/34 (26,5%) | 2/7 (28,6%) |
| BA-N apariciones al final/total | 78/165 (47,3%) | 18/33 (54,5%) |
| BI-N grupos con final/grupos con motivo | 5/23 | 2/4 |
| BA-N grupos con final/grupos con motivo | 43/103 | 12/19 |

El resultado **NO favorece** la versión general de H1 en estos datos.
No demuestra H2 como teoría gramatical ni refuta H3 (no se probó).

Las proporciones anteriores están tomadas de segmentos gráficos, sin
control paleográfico completo, de soporte ni de época. El reporte
incluye advertencia `RETROSPECTIVE_POST_HOC_LEGACY_DATA` y no
calcula p-valores de independencia espurios.

## Criterio futuro de una prueba verdaderamente prospectiva

Antes de ver nuevas lecturas, fijar selección de inscripciones nuevas
fuera del FULL3406 y fuera de toda documentación consultada durante el
diseño, cotejar piezas físicas, registrar lectura ciega y anotar el
contexto cuantitativo sin ver la hipótesis. Predefinir direcciones,
umbrales, controles y abstenciones. Los resultados de este histórico
solo generan hipótesis; no puntúan progreso científico ni rendimiento
gramatical oficial.

## Ejecución

```bash
python -m iberos.morph_rivals_02 /ruta/IberOS_LEAK_SAFE_v3_4_9_FULL3406.json --json /tmp/morph-rivals-02.json
pytest -q tests/test_morph_rivals_02.py
```

No se incluye JSON privado; verificaciones del SHA-256 original en
`legacy_bridge`. Mantener splits y métricas intactos.
