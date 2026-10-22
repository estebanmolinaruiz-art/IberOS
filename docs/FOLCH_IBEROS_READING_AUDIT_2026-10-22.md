# Auditoría Folch–IberOS de lecturas — v1

Fecha: 2026-10-22

## Objetivo

Comparar las coincidencias del corpus Folch–Jiménez Huertas con las lecturas y anclas actualmente utilizadas por IberOS, sin convertir diferencias editoriales o de codificación en discrepancias paleográficas ficticias.

## Hallazgo metodológico principal

El XLS de Folch conserva muchas transcripciones mediante una fuente ibérica específica. La extracción textual devuelve caracteres de codificación de fuente (por ejemplo `SDîM`, `ô9-ÈB...`) que **no pueden compararse de forma segura signo por signo** con transliteraciones Unicode de IberOS sin una tabla explícita de correspondencia.

Por ello esta auditoría distingue:
- `STRUCTURAL_MATCH`: la relación documental/funcional es verificable;
- `PARTIAL`: referencia y objeto coinciden, pero la comparación signo a signo está bloqueada por codificación, caras o segmentos;
- `REVIEW_REQUIRED`: existen varias ediciones/relecturas del mismo objeto y deben tratarse como dependientes.

## Resultados relevantes

1. **F.11.8 Sagunto**: Folch conserva explícitamente la cara latina `M.FABIVS.M.L.ISIDORVS.COERAVIT`; esto es coherente con el uso de IberOS como control bilingüe. Falta vincular en el crosswalk la cara ibérica exacta.
2. **B.7.38 Pech-Maho**: Folch conserva lectura inicial y relectura posterior. IberOS debe mantenerlas en un mismo grupo de dependencia editorial.
3. **Oliete / El Palomar**: varias lecturas y relecturas corresponden a una misma unidad física; no deben contarse como evidencias independientes.
4. **C.2.3, F.17.1 y F.9.8**: el corpus Folch identifica al menos una cara, mientras IberOS agrupa ambas. El siguiente nivel de normalización debe trabajar a nivel de cara/subentrada.
5. **C.18.7, D.12.1, F.14.1 y E.7.1**: la referencia es concordante, pero el cotejo signo a signo queda pendiente de decodificar de manera verificable la fuente ibérica original.

## Regla de seguridad

Ninguna diferencia entre los caracteres crudos del XLS y una transliteración IberOS se registrará como discrepancia paleográfica hasta disponer de una correspondencia documentada de la fuente original o de una lectura editorial externa verificable.

## Próximo paso

Crear una tabla `folch_font_to_iberos_sign.csv` a partir de correspondencias verificadas (no inferidas) y usarla para producir un diff por signo, conservando variantes, signos dudosos y marcas editoriales.
