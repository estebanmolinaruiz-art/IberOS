# DISCOVER-26 · Ejecución multiyacimiento y pruebas contrafácticas

Fecha: 2026-11-17 · [GitHub Actions #44150930392](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/44150930392), **conclusión SUCCESS**; seis pruebas de guardarraíl completadas.

## Ejecución real
Se ha extendido el motor documental de DISCOVER-25, sin alterar el Core, a las transcripciones editoriales disponibles de **Sagunto** (IBR-LAP-0005), **Caminreal** (IBR-MUS-0001) y **Casinos** (IBR-PLM-0007). Fuente `data/review/editorial_readings_pending_v1.jsonl`; para regiones de Casinos también `data/review/casinos_graphic_uncertainties_v1.json`. Los archivos de entrada quedan identificados por SHA-256 en el resultado `report.json`.

Se generaron 19 unidades editoriales, distribuidas 4 Sagunto, 3 Caminreal y 12 Casinos. Se conservaron cuatro alternativas de lectura, cinco unidades dañadas/incompletas, cuatro unidades con marcadores numéricos en la **edición** y diez enlaces a fichas de región gráfica para futura revisión. Ninguna de esas fichas equivale a un signo localizado y verificado sobre una imagen.

## Falsaciones nuevas (ablaciones contrafácticas)
1. Base sin alterar.
2. Retirar el enlace a la región gráfica.
3. Forzar una sola alternativa editorial por unidad.
4. Retirar los indicadores numéricos tipográficos.

En las cuatro pruebas el motor produjo **0 afirmaciones semánticas admitidas y 19 abstenciones**. Esto verifica los guardarraíles contra inferencias sin soporte, **pero no valida el sistema como descifrador**. No se han calculado probabilidades fonéticas ni semánticas porque no hay datos de entrenamiento y evaluación independientes.

## Artefactos
`research/core_association/discover26_multisite.py`, `test_discover26.py` y `.github/workflows/iberos-discover26.yml`. Resultados entregados por Actions en `iberos-discover26-multisite` (run 44150930392, artifact 14359895008): `report.json`, `uncertainty_ledger.json`, `review_queue.csv`.

## Bloqueo y siguiente criterio
Un avance positivo exige una imagen primaria, ancla de píxel para cada signo, clasificación paleográfica independiente, identificación del objeto físico y evidencia de función externa que no se haya utilizado para construir la hipótesis. Una vez disponibles, comparar alternativas fonéticas/abreviativas/logográficas mediante evaluación preinscrita y controles negativos. No promover hipótesis al Core sin superar esas puertas.

**Coste adicional 0 €. Core, C594/C474/C539/C541 y FULL3406 protegidos.**