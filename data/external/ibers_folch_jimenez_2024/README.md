# Corpus Folch–Jiménez Huertas (febrero de 2024)

Dataset externo de referencia integrado en IberOS a partir del archivo `ibers_febrer_24 (5).xls` facilitado por David Folch el 19-10-2026.

## Autoría y atribución

- Archivo Excel: **David Folch y Carme Jiménez Huertas**.
- Fuente tipográfica ibérica: **Carme Jiménez Huertas**.
- Página de referencia: https://ibers.cat/corpus.html

David Folch confirmó por correo que el uso del XLS y de la fuente es libre, solicitando la citación anterior.

## Función dentro de IberOS

Este material se trata como **fuente documental externa**. No se incorpora automáticamente al benchmark curado ni convierte sus lecturas en lecturas paleográficamente verificadas por IberOS.

Regla de uso:

`EXT_SOURCE -> UPSTREAM_ID -> ENTRY_ID / OBJECT_ID -> evaluación de dependencia -> posible uso curado`

Antes de emplear una fila como evidencia independiente se debe:
1. identificar la inscripción/objeto físico correspondiente;
2. resolver concordancias con MLH/Hesperia/Corpus Ibèrika u otras ediciones;
3. comprobar si deriva de una edición ya utilizada por IberOS;
4. registrar discrepancias de lectura;
5. asignar `PHYS_ID` / `LEAK_GROUP` cuando proceda.

## Archivos

- `manifest.json`: procedencia, autoría, hash y política de integración.
- `text.csv`: extracción textual de la hoja principal del XLS.
- `cadenes.csv`: extracción textual de la hoja de cadenas.
- `crosswalk_template.csv`: plantilla para vincular entradas externas con objetos IberOS.

La codificación de signos depende de la fuente ibérica original; por ello se conserva la representación extraída y no se normalizan silenciosamente los signos.
