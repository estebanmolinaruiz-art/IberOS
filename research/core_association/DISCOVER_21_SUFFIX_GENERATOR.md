# DISCOVER-21 · Inducción de reglas de final de grupo

**Fecha:** 2026-11-16. **Estado:** EXPLORATORIO, sin reconocimiento visual ni traducción validados. **Coste adicional:** 0 €. Core/FULL3406/C594/C474/C539/C541 intactos.

## Hallazgo algorítmico independiente de W
A partir de `IBEROS_FULL_LINE_ALIGN_17/aligned_slots.csv` (primera línea de Orleyl V y VII-B, valores editoriales Fletcher 1981) se han generado todos los sufijos de 1, 2 y 3 signos por grupo puntuado. La única terminación de 2 valores con dos ocurrencias en entrenamiento V es `N-E` y vuelve a aparecer al final de un grupo de VII-B. Sus tres ocurrencias en ambas líneas son finales de grupo.

Una regla alternativa de **terminación recurrente**, fonética/morfológica o formularia, merece contraste. **No implica «cada signo es una palabra».** Los contornos no están validados y los grupos están condicionados por la edición.

## Controles ejecutados
- 30.000 permutaciones dentro de grupos con V fijo: la aparición de la regla aprendida en VII-B tiene p exploratoria ≈ **0,0668**; no alcanza 0,05.
- Un segundo generador de permutaciones para `N-E` fijo da ≈ **0,0678**.
- Máximo conjunto para sufijos de longitud 1–3: p ≈ **0,3218**, sin evidencia global de anomalía.
- Sin grupos que contienen valor editorial `W`: persiste un `N-E` final en cada objeto, pero se pierde la repetición 2× en V.
- Un resultado extremadamente bajo para `N-E` seleccionado a posteriori es **sesgado por selección** y NO se usa como validación.

La evidencia soporta **una candidatura formal específica H21-A**, no un descubrimiento. Contrastar en un tercer objeto físico de distinta procedencia con predicción congelada; comparar contra fonética, signo-palabra, y marca no lingüística, incluyendo controles de posiciones internas y errores de lectura.

**Reproducibilidad:** paquete local `IBEROS_DISCOVER_21.zip` (Python estándar, `results.json`, `groups.csv`, informe). Requiere ALIGN-17. Ninguna modificación del Core.
