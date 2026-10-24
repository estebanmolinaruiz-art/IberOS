# IberOS — actualización de evidencia institucional (24-10-2026)

## Alcance

Esta actualización registra respuestas institucionales recibidas para dos objetos del corpus IberOS. Se incorpora como trazabilidad documental y no modifica automáticamente ninguna lectura, hipótesis semántica ni estado CORE.

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
2. documento de aceptación de normas enviado a firma del investigador;
3. después debe firmar el Director;
4. Enric Verdú prevé realizar una primera tanda de fotografías;
5. envío posterior a la autorización, posiblemente vía WeTransfer.

La firma desde móvil no ha funcionado. La acción pendiente se mantiene como trámite administrativo a completar desde un entorno de escritorio compatible con firma digital.

### Efecto en IberOS

`PRIMARY_VISUAL_EVIDENCE_PENDING`

No se modifica la lectura bo/ko hasta recibir y revisar las nuevas fotografías.

## Regla científica

Estas respuestas institucionales se registran en la capa `EVIDENCE`. Solo una revisión posterior de documentación visual o material primario podrá alimentar nuevas inferencias.

`INSTITUTIONAL_RESPONSE → EVIDENCE UPDATE → REVIEW → possible INFERENCE`

Nunca:
`INSTITUTIONAL_RESPONSE → automatic CORE promotion`