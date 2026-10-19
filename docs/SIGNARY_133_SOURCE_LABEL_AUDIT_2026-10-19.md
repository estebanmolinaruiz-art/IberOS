# IberOS — lote de cotejo formal de 133 candidatos simples
Fecha: 2026-10-19

## Resultado
Se clasificaron 286 códigos de `iber.ttf` de Cathalaunia, de los que 133 tienen etiqueta fuente simple; pertenecen a **25 valores base**. Se incorporó un auditor que compara **código Unicode decimal + etiqueta de variante** de la tabla fuente con el triaje. Esto detecta alteraciones o promociones indebidas en futuras ediciones.

Distribución de los 133: a=6, e=12, i=6, o=3, u=3, l=2, m=3, n=3, r=4, s=7, ba=2, ta=3, ka=6, be=12, te=15, ke=11, bi=3, ti=4, ki=8, bo=3, to=3, ko=3, tu=5, bu=2, ku=4.

**Advertencia de nivel de evidencia:** Coincidencia entre dos tablas del MISMO origen acredita consistencia de metadatos, NO verificación independiente. No se han cotejado 133 imágenes arqueológicas, no se han verificado valores fonéticos, y no se ha habilitado la lectura automática.

## Comprobación
```bash
python scripts/audit_cathalaunia_signary.py data/review/cathalaunia_signary_source_codes_v5_2026-10-19.csv data/review/cathalaunia_signary_review_queue_286_v2.csv
pytest -q tests/test_audit_cathalaunia_signary.py
```
Estas pruebas comprueban el programa y los datos publicados. No implican éxito de VALIDATION-01.

## Revisión próxima
1. Revisar primer lote de 15 códigos con etiqueta **te** (variantes de Cathalaunia) comparándolos con el signario y edición originales.
2. Asociar fotografías o calcos concretos a un objeto, edición y lectura editorial (sin inferir derechos de reutilización).
3. Revisión independiente y registro de variantes ambiguas (especialmente te?, teB7/bu2? y grafías duales).
4. Solo después proponer traducción técnica de los 133 candidatos a signario auditado, separados de códigos Huertas.
5. VALIDATION-01 exige predicción congelada y HOLD independiente; permanece **NOT_EVALUATED**.
