# IBEROS-ALIGN-16 · Registro de renglón completo, sin perder huecos

Fecha: 2026-11-16. Estado **ALINEACIÓN DE POSICIONES PROVISIONAL**, no prueba de OCR ni de desciframiento.

Se reabrió el PDF *Materiales de la necrópolis ibérica de Orleyl* (1981) aportado por el investigador. Dibujos: figura 22, Orleyl V (PDF p. 65), y figura 25, Orleyl VII-B (PDF p. 111); lecturas impresas en PDF pp. 66 y 110. Documento PDF SHA-256 registrado en paquete local.

**Procedimiento:** se aplicaron seis anclas provisionales de separadores al primer renglón de Orleyl V y tres al de Orleyl VII-B. Se hizo un inventario continuo por grupo; la partición de posibles posiciones minimizó densidad de tinta en los límites, **condicionada al número de tokens de la edición**. Las posiciones no identificadas permanecen sin lectura. Los separadores son registros independientes, no caracteres fonéticos. La restitución de tres tokens finales entre corchetes en la edición de VII-B se registra como `EDITORIAL_RESTORATION_NO_OBSERVED_GLYPH`, sin región de imagen.

Resultados:
- V línea 1: 7 grupos; 44 posiciones provisionales (una región inicial sin conteo editorial obligado); 6 separadores.
- VII-B línea 1: 4 grupos; 26 posiciones provisionales; 3 separadores; 3 restituciones editoriales sin evidencia visual.
- **Total 82 filas** en la matriz: 69 posiciones alineadas **solo por orden editorial**, 1 región inicial sin lectura, 9 separadores y 3 restituciones. **Cero signos leídos independientemente**, cero validaciones semánticas, precisión OCR desconocida.

Se registraron las cajas x/y, densidad de tinta, referencia de figura, SHA-256 y estatus; hay cortes que podrían atravesar signos. El algoritmo **NO recupera automáticamente el contorno íntegro de todos los signos**. Es una matriz de cobertura y corrección de huecos, no un alineamiento paleográfico definitivo. El orden editorial puede estar errado en casos de lagunas, signos unidos y variantes.

Artefacto reproducible del hilo: `IBEROS_FULL_LINE_ALIGN_16.zip` (CSV de posiciones y de grupos, overlays, zooms, programa y manifiesto). Las imágenes originales utilizadas proceden del PDF facilitado. No publicar el material gráfico original sin comprobar sus derechos.

**Siguiente puerta:** un segundo lector debe revisar manualmente cada frontera y los signos completos y registrar discrepancias. Luego congelar predicción de lectura y contrastar contra otra pieza física con grupos de filtración independientes. Coste adicional 0 €. Core, C594/C474/C539/C541 y FULL3406 intactos.
