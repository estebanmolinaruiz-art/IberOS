# IberOS — actualización de evidencia institucional (29-10-2026)

## Alcance

Esta actualización registra respuestas institucionales recibidas para objetos del corpus IberOS. Se incorpora como trazabilidad documental y no modifica automáticamente ninguna lectura, hipótesis semántica ni estado CORE.

## IBR-PLM-0011 — Moleta del Remei

El Museu de les Terres de l'Ebre confirma la custodia actual de la pieza y su número de registro **09618**.

La ficha institucional adjunta aporta:
- yacimiento: Moleta del Remei;
- procedencia: Alcanar;
- excavación: 1988;
- unidad estratigráfica: E II, N 3, H-52;
- dimensiones: 6,1 × 2,6 cm;
- material: plomo;
- datación general: ferro-ibèric;
- estado de conservación: bueno;
- forma de ingreso: depósito;
- fecha de ingreso: 08/03/1993;
- fuente del ingreso: Departament de Cultura de la Generalitat de Catalunya.

El museo dispone de fotografías de buena calidad, pero no de documentación macro/RTI con las características solicitadas. La reproducción fotográfica debe tramitarse mediante el procedimiento del museo.

### Efecto en IberOS

`CUSTODY_CONFIRMED + MUSEUM_METADATA_ENRICHED`

No cambia la lectura paleográfica ni la interpretación. Mejora procedencia, identidad física y trazabilidad documental.

## IBR-PLM-0012 — Illeta dels Banyets

El MARQ confirma recepción de la solicitud de fotografía original en alta resolución del detalle del signo dudoso **bo/ko**.

Estado del procedimiento:
1. solicitud recibida;
2. documento de aceptación de normas remitido para firma del investigador;
3. la firma electrónica continúa pendiente por no disponer en este momento de un certificado personal admitido por la sede;
4. después de la firma del investigador debe firmar el Director;
5. Enric Verdú prevé realizar una primera tanda de fotografías;
6. envío posterior a la autorización, posiblemente vía WeTransfer.

La incidencia es administrativa y no constituye evidencia paleográfica nueva.

### Efecto en IberOS

`PRIMARY_VISUAL_EVIDENCE_PENDING`

No se modifica la lectura bo/ko hasta recibir y revisar las nuevas fotografías.

## La Serreta — Plomo I

El Museu Arqueològic Municipal Camil Visedo Moltó de Alcoi comunica que no dispone de las fotografías específicas solicitadas y que, por razones de conservación, el Plomo I no puede extraerse de su protección para realizar una nueva sesión fotográfica en esas condiciones.

El museo sí indica que puede solicitarse **consulta presencial de la pieza**.

### Efecto en IberOS

`REMOTE_SPECIFIC_PHOTOS_UNAVAILABLE + IN_PERSON_CONSULTATION_AVAILABLE`

La respuesta no resuelve ninguna lectura dudosa ni modifica el estado paleográfico. Abre una vía de comprobación directa presencial y debe mantenerse separada de cualquier inferencia obtenida de ediciones o reproducciones secundarias.

## Regla científica

Estas respuestas institucionales se registran en la capa `EVIDENCE`. Solo una revisión posterior de documentación visual o material primario podrá alimentar nuevas inferencias.

`INSTITUTIONAL_RESPONSE → EVIDENCE UPDATE → REVIEW → possible INFERENCE`

Nunca:
`INSTITUTIONAL_RESPONSE → automatic CORE promotion`
