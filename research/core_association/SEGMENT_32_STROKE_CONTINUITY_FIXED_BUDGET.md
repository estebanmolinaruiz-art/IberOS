# SEGMENT-32 — Continuidad de trazos con presupuesto fijo

Fecha: 2026-11-21. Experimento local reproducible sobre Orleyl V y VII-B, imágenes originales cuya huella SHA-256 está registrada en SEGMENT-30. Coste adicional 0 €.

## Nuevo coste
El grafo de cortes permanece igual al anterior, pero el cálculo de rutas incorpora tres magnitudes **puramente gráficas**: densidad de tinta en la frontera, riesgo de atravesar componentes conexas y densidad local próxima. Función heurística: `1.25·ink + 1.10·component_crossing + 0.60·local_density + width_penalty + 0.22`. Los coeficientes son heurísticos y **no están calibrados en un conjunto independiente**.

Presupuesto fijo de 26 cortes para Orleyl V y 17 para VII-B, igual que SEGMENT-31. Las propuestas se guardan antes de consultar las posiciones editoriales.

| Renglón | Cortes | Coincidencias SEGMENT-31 | Coincidencias SEGMENT-32 | Referencias editoriales |
|---|---:|---:|---:|---:|
| Orleyl V | 26 | 23 | 23 | 42 |
| Orleyl VII-B | 17 | 11 | 12 | 25 |
| Total | **43** | **34** | **35** | **67** |

Precisión proxy: **79,07 % → 81,40 %** (+1 frontera real, sin cortes extra). Recuperación proxy: **50,75 % → 52,24 %**. El control de puntuación de tinta previo, reconstruido en el mismo algoritmo con presupuesto fijo, dio 34 coincidencias y confirmó la comparación.

**Significado:** mejora exploratoria muy pequeña en el conjunto conocido, concentrada en VII-B; no debe interpretarse como generalización ni precisión de lectura. Los límites editoriales son aproximaciones; no hay signos verificados de forma ciega. **0 traducciones**. Un test interyacimientos es indispensable antes de incorporar el método al Core.

Artefacto local `IBEROS_SEGMENT_32.zip`, incluye programa ejecutado, resultados JSON, imágenes comparativas y predicciones congeladas. Core/FULL3406/C594/C474/C539/C541 intactos.
