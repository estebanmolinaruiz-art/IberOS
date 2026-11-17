# DISCOVER-25 · Motor de evidencia gráfico–fonética–función arqueológica

Fecha: **2026-11-17**. Ejecutado: [GitHub Actions #44039058005](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/44039058005), **SUCCESS**, con seis pruebas automáticas de seguridad.

## Cambio metodológico real
El nuevo algoritmo crea una retícula por **objeto físico → región/línea/posición editorial → ficha gráfica con procedencia → conjunto de lecturas editoriales alternativas → funciones candidatas → decisión de abstención**.

Las dos lecturas editorialmente posibles de un mismo grafema nunca reciben probabilidades numéricas arbitrarias y nunca se cuentan como observaciones independientes. Las referencias de figura publicada NO equivalen a coordenadas verificadas del signo en una fotografía. La función arqueológica queda `NOT_VERIFIED` hasta que exista evidencia externa independiente.

**Caso de ejecución:** plomo Casinos, ID IBR-PLM-0007; transcripción dual/no dual publicada por Ferrer i Jané y Escrivà Torres (2014, p. 212), ya transcrita en el registro de IberOS; cinco regiones gráficas del expediente con reproducción previamente inspeccionada, pero no cotejo de signos acreditado.

Resultados:
- **14 unidades posicionales editoriales**: **10 invariantes** y **4 con variantes** entre dual y no dual.
- **4 unidades con notación numérica editorial estable**, sin acreditación de los trazos en imagen ni denominación metrológica externa.
- **0 signos con coordenadas originales verificadas**, **0 funciones arqueológicas independientemente atribuidas**, **0 traducciones**.
- **14 abstenciones justificadas**. Las unidades numerales se señalan como candidatos de **notación cuantitativa**, no como números físicamente contados o palabras traducidas.
- Ningún resultado del Core se modifica.

## Archivos y reproducibilidad
- `research/core_association/discover25_evidence_model.py`: retícula con campos de trazabilidad y políticas de no invención.
- `research/core_association/test_discover25.py`: seis pruebas: no traducción ficticia, alternativas conservadas, gráfica no inventada, mismo objeto, numerales editoriales no promovidos, abstención.
- `.github/workflows/iberos-discover25.yml`: ejecución gratuita en GitHub Actions.
- Artefacto `iberos-discover25-uncertainty`: `report.json`, `evidence_lattice.json`, `review_queue.csv`; ejecución #44039058005.

## Regla experimental para futuras lecturas

Una unidad solo puede recibir `GRAPHIC_VERIFIED` si hay región de imagen, ancla geométrica, identificación del objeto y juicio independiente. Una función solo puede recibir `FUNCTION_INDEPENDENT` si proviene de contexto externo no utilizado al proponerla. Solo entonces podrá compararse cuantitativamente un modelo fonético, uno abreviativo, uno logográfico y uno no lingüístico. Hasta obtener verosimilitudes calibradas en muestras reservadas, mantener **conjuntos de posibilidades y abstención**, no porcentajes arbitrarios.

**Próxima acción concreta:** localizar o recuperar la imagen real de las figuras 1–2 de Casinos y revisar la relación de cada unidad con las regiones A1–B3, verificando por separado los cuatro usos de la notación romana `I`. Si no está disponible el facsímil real, no sustituirlo por recreaciones.

**Protección:** Core/FULL3406/C594/C474/C539/C541 sin alteraciones. Coste adicional 0 €.
