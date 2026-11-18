# IBEROS-FEED-27: Alimentación del motor con evidencia gráfica real

Fecha: 2026-11-18. Ejecución local reproducible sobre **cuatro imágenes existentes en el entorno IberOS**; sin modificación del Core.

**Fuente efectiva**: edición de Fletcher 1981 facilitada en PDF, páginas impresas de dibujos de Orleyl V y VII-B, previamente rotadas a PNG en `IBEROS_VISUAL_AI_02`, y dos imágenes fotográficas de las páginas PDF 154 y 155 ya procesadas en `IBEROS_LIGHT_CONTRAST_10`. Se han reutilizado los 70 límites de `IBEROS_FULL_LINE_ALIGN_17/aligned_slots.csv` y las 40 cajas de `IBEROS_SIGN_CROPS_11/candidate_signs.csv`.

Resultado material:
- **110 recortes gráficos reales**, identificados por coordenadas y SHA-256 de imagen y recorte; **70 de dibujos editoriales** y **40 de páginas fotográficas**.
- De la matriz original de 82 registros no se generaron recortes para 9 separadores y 3 signos editoriales restituidos sin evidencia física.
- **109** recortes superan un control *simple* de presencia de píxeles oscuros; **1** contiene escasa información gráfica. Esto NO demuestra que sean grafemas completos.
- La identidad física de la inscripción correspondiente a las dos páginas fotográficas **no se ha resuelto**: sus 40 regiones se marcan `ORLEYL_UNKNOWN_PHOTO_PAGE` y no pueden contarse como confirmación independiente.
- **0** valores fonéticos identificados independientemente; **0** funciones arqueológicas externas verificadas; **0** traducciones; **110 abstenciones correctas** tras pasar el filtro de admisión.

El motor ha recibido **imágenes y metadatos**, no etiquetas semánticas ni lecturas artificiales. Los valores de la matriz ALIGN-17 quedan en `editorial_value_REFERENCE_ONLY`. Los recortes dibujados pertenecen a una edición arqueológica, no a fotografías de surcos originales. La prueba de píxeles oscuros es solo un control básico de ingestión.

Archivos reproducibles generados localmente y entregados en conversación: `IBEROS_FEED_27.zip` incluye `feed27.py`, `evaluate27.py`, `manifest.json`, `evidence_ledger.json`, `ingested_regions.csv`, `evidence_gate_results.json`, una vista de diagnóstico y 110 PNG recortados. ZIP verificado íntegro con CRC. **Estos recursos gráficos no se publican en GitHub para no redistribuir láminas de edición con derechos sin comprobar**.

La búsqueda del PDF original de Casinos localizó la página editorial oficial https://ifc-ojs.es/index.php/palaeohispanica/es/article/download/54/57/294 , pero en este turno no fue posible descargar los bytes de su PDF para crear recortes verificables. Por tanto no debe declararse Casinos alimentado por imágenes originales.

**Próxima puerta de calidad:** revisión del contorno de signos en las 70 posiciones, recuperación de la lámina de Casinos y cotejo independiente de una fotografía con su objeto físico antes de cualquier asignación fonética.

Sin gastos. Core, C594/C474/C539/C541 y FULL3406 intactos.
