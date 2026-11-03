# Recuperación de FULL3406 / LEGACY — auditoría del 03-11-2026

**Estado:** `LEGACY_3406_NOT_RECOVERED`. No sustituir esta capa por otro
corpus, ni producir predicciones HOLD sobre materiales no depurados.

## 1. Fuente original externa recuperada y localizada: NO es FULL3406

- Corpus Folch–Jiménez Huertas, febrero 2024.
- Archivo Excel original en Google Drive:
  https://docs.google.com/spreadsheets/d/1Ql7zSnjAORjlPMW4toqqK4sTBbkxpjIb/edit
- Copia nativa para consulta:
  https://docs.google.com/spreadsheets/d/19ct13SfIqjaUCFzJaROmwGdTIf92vSqvoHoNAAk8bs4/edit
- El archivo original está declarado por el manifiesto del repositorio como
  `ibers_febrer_24 (5).xls`, recibido el 19-10-2026; tamaño 1.208.320 bytes.
- SHA-256 **declarado**, no recalculado en esta auditoría:
  `85871b90401a9b7b5ac418644322026d6fcc7d7515f992b3ce3c966639a364a2`.
- Hojas `text` (4.509 filas de cuadrícula) y `cadenes` (4.472 filas de
  cuadrícula); sus filas no son equivalentes sin más a inscripciones físicas.
- El repositorio conserva `data/external/ibers_folch_jimenez_2024/manifest.json`
  y `README.md`; los archivos `text.csv` y `cadenes.csv` anunciados en
  el README **no se encontraron** por la API de contenidos de GitHub (404)
  durante la auditoría. La copia conectada de Drive sí es consultable.
- Mantener atribución: David Folch Flórez y Carme Jiménez Huertas;
  referencia original: https://ibers.cat/corpus.html.

## 2. Capa histórica específica de IberOS todavía pendiente

El `docs/BENCHMARK.md` oficial declara 3.406 `ENTRY`, capa
`LEGACY / FROZEN`, independiente del benchmark curado de 38 objetos.
`docs/CROSS_THREAD_SYNC_2026-10-16_FORMULAICITY.md` prohíbe alterar
`FULL3406`, `LEAK_GROUP` o los splits congelados.

**No se encontró el archivo original de esas 3.406 entradas** entre
los archivos IberOS localizados en el Google Drive conectado ni como
ruta documentada pública de descarga en el repositorio. Esto NO prueba
que no exista en un Codespace, una copia local o un respaldo privado.

Antes de registrar una recuperación válida es obligatorio:

1. Obtener el binario original o exportación literal de `FULL3406`, y su
   manifiesto con fecha, origen y SHA-256.
2. Contar exactamente las `ENTRY` reales, sin cabeceras ni filas vacías,
   y verificar 3.406 sin reconstruir ni borrar registros.
3. Preservar `ENTRY_ID`, `OBJECT_ID`, `PHYS_ID`, `LEAK_GROUP` y
   `TRAIN / VAL / HOLD`, incluidas las variantes editoriales.
4. Auditar aliases externos y objetos antes de desbloquear cualquier HOLD.
5. Mantener el original inmutable y generar auditorías aparte.

## 3. Hallazgos de cruce preliminar

- Xàbia / Fundació CIRNE (artículo AEspA 2022, vol. 95, e07):
  documentado en Folch 2024, fila **4354**, tanto en `text` como
  `cadenes`; por ello se excluyó de HOLD-01 mediante PR #101.
- La Mesa / Alcolea del Río: ninguna coincidencia **literal** de los
  topónimos en las columnas A:H de la hoja `text` de Folch 2024.
  Este resultado NO descarta un alias, una edición alternativa o presencia
  en FULL3406. HOLD-01-B permanece sin certificación.
- Caminreal y Andelo ya están en el registro curado de 38 objetos y no
  se cuentan como novedad de validación.

## 4. Dictamen

`FULL3406` = **PENDIENTE DE RECUPERAR**.

`FOLCH_2024` = **FUENTE ORIGINAL LOCALIZADA, RECUPERADA COMO
REFERENCIA EXTERNA**, sin ingreso automático al benchmark.

`HOLD01` = **NO_CERTIFICADO**. Métricas oficiales y capa D1 sin promoción.

Toda afirmación de recuperación de 3.406 entradas requiere una copia
verificada y un cotejo de filas; no inferirla de una nota o de otra fuente.
