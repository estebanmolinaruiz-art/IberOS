# Mapa de fuente Folch → signos IberOS — v0.1

Fecha: 2026-10-22

## Criterio de verificación

Solo se acepta una correspondencia automática cuando una fila del corpus contiene exactamente un glifo en la columna de transcripción y exactamente una etiqueta de variante en la nota editorial.

Esto evita deducir qué carácter representa una etiqueta cuando la anotación acompaña una secuencia de varios signos.

## Correspondencias verificadas

- `}` → `ti`, variante Folch `Uti2` (fila 161).
- `]` → `be`, variante Folch `Ube2` (filas 474, 476 y 478).
- `E` → `tu`, variante Folch `Utu1` (fila 1319; la propia nota dice “Més aviat Utu1”).

Estas tres equivalencias pueden utilizarse en normalización automática con trazabilidad explícita.

## Correspondencias todavía abiertas

Etiquetas como `Us4`, `Uo3`, `Uka4`, `Uka5`, `Uka6`, `Utu3`, `Ube6`, `Ute16`, `Uku3`, `Ua2` y otras aparecen en secuencias de varios glifos. Se conservan como candidatos, pero no se asignan todavía a un carácter.

## Regla de uso

`RAW_FOLCH_CHAR -> VERIFIED_TAG -> IBEROS_BASE_SIGN`

Una correspondencia solo se usa en el diff automático si su estado es `VERIFIED_SINGLE_GLYPH`.

## Próximo nivel

Para ampliar el mapa sin inferencias:
1. localizar más filas de un solo signo;
2. usar la imagen original de la hoja para validar visualmente variantes;
3. obtener la TTF cuando el servidor de ibers.cat vuelva a responder;
4. contrastar con lecturas editoriales independientes ya fijadas en IberOS.
