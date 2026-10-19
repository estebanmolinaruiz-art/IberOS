# VALIDATION-01: fe de erratas de coordenadas de recorte (2026-10-19)

## Hallazgo durante revisión
Se inspeccionaron las imágenes de Fletcher con cuadrícula de píxeles y se detectó que las coordenadas de las bandas publicadas anteriormente NO correspondían correctamente al renglón declarado. Es una corrección de proceso de inspección, no una nueva lectura paleográfica.

**Sistema de referencia:** PNG girado 90° horario, 1830 × 1382 píxeles; coordenadas enteras (izquierda, arriba, derecha, abajo).

| Figura / línea | Coordenadas previas incorrectas | Nuevas franjas preliminares |
| --- | --- | --- |
| Orleyl V, fig. 22, línea 3 | (35,497,1400,565) | **(30,633,1420,706)** |
| Orleyl VII-B, fig. 25, línea 2 | (375,413,1250,474) | **(425,528,1350,613)** |

Las coordenadas antiguas recortaban partes del borde de la lámina o líneas diferentes. **Quedan anuladas para localizar signos**, incluidos recortes y reportes anteriores. Los nuevos recortes abarcan parte de renglones contiguos y son únicamente soporte de inspección, no cajas de los 17 signos ni lectura cotejada.

Datos de lectura editorial conocidos por Fletcher:
- Orleyl V V-19: `bi te r o ke te ti n e`.
- Orleyl VII-B VII-B-7: `bi te r o ke ti n e` más posible `ba s` anterior.

Ninguna de estas dos secuencias está segmentada en cajas por grafema a partir de los recortes nuevos; **M06 queda PENDING**, indicador preparación **30%**, `VALIDATION-01=NOT_EVALUATED`.

Acción siguiente: certificar el segmento físico mediante inicio/final de palabra en la línea, consultar aparato crítico y anotar cada signo con referencia visual y posible duda. La cifra del 40% requiere terminar las 17 localizaciones con comprobación paleográfica individual.
