# IberOS — control de edición y facsímil: Caminreal / Casinos (18-10-2026)

## Infraestructura
Commit `81f2ca6256f5ddc5268ded2729b5b3d552c6cf1a`: GitHub Actions `tests`, `Comprobaciones web gratuitas`, `pages` y `benchmark`: **success**. El resultado confirma integridad técnica, no lecturas paleográficas.

## Caminreal — IBR-MUS-0001
Edición: Ignacio Simón Cornago, *Palaeohispanica* 15 (2015), 87–127, DOI https://doi.org/10.36707/palaeohispanica.v0i15.39 ; PDF editorial: https://ifc.dpz.es/recursos/publicaciones/35/02/03simon.pdf.

El texto indexado del artículo muestra explícitamente la lectio editorial **`likinete · ekiar · usekeŕteku`** y la advertencia de que la tesela anterior a la inscripción podría ser o no interpunción. No constituye una lectura semántica. **Se ha consultado el texto indexado, pero no se ha conseguido una captura verificable del facsímil**; toda certificación individual de signos sigue pendiente.

## Casinos — IBR-PLM-0007
Edición: Joan Ferrer i Jané y Vicent Escrivà Torres, *Palaeohispanica* 14 (2014), 205–227, DOI https://doi.org/10.36707/palaeohispanica.v0i14.54 ; PDF editorial https://ifc-ojs.es/index.php/palaeohispanica/es/article/download/54/57/294 .

La indexación del artículo reproduce la transcripción dual y no dual publicada en pp. 212–213. **Advertencia de normalización:** las cadenas estructuradas en `data/review/editorial_readings_pending_v1.jsonl` normalizan espacios y segmentación, por lo que **no son transcripciones diplomáticas exactas**; deben compararse carácter a carácter antes de afirmar acuerdo. Fig. 2 (dibujos: A arriba, B abajo) aparece identificada en la edición, pero **no se ha inspeccionado gráficamente** su contenido en esta fase. El PDF ha dado un error de redirección al abrirlo con la herramienta: no se presenta como visto.

**Control experimental:** ninguna de estas dos lecturas está aprobada (`PENDING_GRAPHIC_REVIEW`) y ninguna interpretación se promociona. No convertir referencias textuales indexadas en verificaciones visuales.

## Cola de revisión manual
1. Inspeccionar la figura y la disposición exacta de la inscripción de Caminreal.
2. Casinos: cotejar Figura 2 y las lecturas de pp. 212–213 con la ficha estructurada, preservando las dos opciones dual/no dual.
3. Registrar variantes, lagunas, orden de caras, interpunctores y credenciales de reproducción fotográfica.
4. Solo tras revisión documentada establecer `APPROVED_READING` para análisis exploratorio sin validación semántica.
