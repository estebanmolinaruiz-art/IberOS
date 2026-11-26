# VISUAL-AI-06 · Cotejo fotográfico de Orleyl (2026-11-14)

**Estado: experimental; sin reconocimiento fonético acreditado.**

Se procesó el PDF aportado por el investigador: *Materiales de la necrópolis ibérica de Orleyl* (1981), lámina XVIII, página 154 del PDF. Sobre la fotografía de Orleyl V se seleccionaron **15 regiones** candidatas (A01–A07, B01–B08), se generaron recortes anónimos para revisión y se calcularon **105 comparaciones** de descriptores HOG. La mayor similitud fue 0,8854; NO es una probabilidad de identidad epigráfica.

La revisión visual de la galería muestra recortes con múltiples trazos, con signos incompletos y con límites aproximados. Ninguno constituye por sí solo un signo completo previamente validado. Todas las observaciones pertenecen al **mismo objeto físico** y no pueden usarse como partición ciega de validación.

El signario externo de Cathalaunia contiene **286 variantes** y la auditoría previa separa **133 etiquetas fuente simples**, pero no se han proporcionado **133 imágenes arqueológicas rotuladas** ni se ha verificado la correspondencia fotografía→contorno→valor. Las 26 entradas de Write son referencias editoriales a SVG, no pruebas visuales en estas fotografías. No se convierte la comparación de etiquetas en reconocimiento óptico.

## Protocolo de cotejo estricto
1. Presentar regiones anónimas a un revisor para clasificar: SIGNO_COMPLETO, SIGNO_PARCIAL, MULTIPLES, NO_SIGNO o INDETERMINADO.
2. Revisar delimitaciones sobre fotografía y dibujo de la **misma pieza**, registrando incertidumbres; no infundir la lectura editorial en la segmentación.
3. Comparar contornos solo con **plantillas gráficas reales** de fuente y conservar nombre de variante, fuente, fecha y convenciones históricas.
4. Registrar tanto acuerdos como falsas coincidencias, rechazos y abstenciones; agrupar siempre por PHYS_ID y LEAK_GROUP.
5. Evaluar el valor fonético contra lectura independiente de otra pieza, congelada antes de revelar la edición.
6. No alterar Core, FULL3406 ni C594/C474/C539/C541.

**Datos y programa local:** `IBEROS_VISUAL_AI_06.zip` generado a partir del PDF facilitado en la conversación; contiene `report.json`, `photo_candidate_regions.csv`, `photographic_shape_similarity.csv`, 15 recortes, galería y código Python. Fotografías publicadas: permiso de redistribución pública sin verificar. No incluir el PDF ni fuente tipográfica en GitHub.

**Resultado científico:** 0 lecturas independientes validadas, 0 correspondencias verificadas con los 133 valores. Próxima tarea: delimitación paleográfica directa sobre fotografía de otro objeto y segundo lector sin acceso a sus etiquetas.
