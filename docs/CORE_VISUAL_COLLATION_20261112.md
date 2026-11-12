# IberOS Core — Cotejo visual independiente y registro de discrepancias (CORE-VIS-01)

**Versión:** 1.0 · **Fecha:** 2026-11-12 · **Estado:** evaluación documental, NO validación lingüística.

## Objetivo y avance real

Conectar **tres registros ya existentes**, sin duplicar piezas físicas ni añadir grafemas inventados:

| Fuente | Unidades de revisión | Soporte científico |
| --- | ---: | --- |
| `data/review/palaeographic_alignment_priority_v1.json` | 5 | Tivissa, Pech-Maho y Coimbra; revisión paleográfica pendiente |
| `site/data/serreta-variants-v1.json` | 7 | Variantes editoriales de **una sola** pieza, Serreta I, inventario 1.016 |
| `site/data/villares-v-discrepancies-v1.json` | 14 | A1–A9/B1–B5 de **una sola** pieza, Villares V, inventario 13411 |

**Total: 26 unidades de revisión / cinco objetos materiales distintos.** Una variante, un fragmento editorial y un renglón no equivalen a tres signos ni a tres inscripciones nuevas.

## Comprobaciones documentales concretas

- **La Serreta I:** Fletcher Valls y Silgo Gauche (1992), `Recerques del Museu d'Alcoi` 1, pp. 9–36. Las fotografías de caras A y B acreditadas a J. Untermann aparecen en **p. 10**. En **p. 11** los autores comparan lecturas de Gómez Moreno 1922/1962: `IUNSTIR/IUNSTIRI`, `SALIRG/SALIRIG` y `BIRINAR/BIRIGNAR`. La comparación textual se ha localizado en la edición; **la diferencia concreta de trazo en la fotografía sigue sin cotejarse**. La relación por cara/línea procede de registros editoriales anteriores, no de coordenadas nuevas.
- **Villares V:** Ferrer i Jané (2024), `ELEA` 21, pp. 309–360, fotografía de ambas caras **fig. 1, p. 312** y dibujos **fig. 2, p. 313**; ejemplar del museo valenciano 13411. Las autopsias del autor (2004 y 2014) no constituyen autopsias independientes de IberOS. La matriz incluye transcripción secundaria y no ha sido cotejada íntegramente signo a signo contra las figuras de 2024.
- **Cinco prioridades PAL:** reaprovechar los localizadores y advertencias de las fichas existentes; no sustituir una fotografía por un dibujo ajeno ni confundir dos piezas próximas por su procedencia.

**Fuentes:** [Archivo municipal Alcoi, número 1 de Recerques](https://www.alcoi.org/es/areas/cultura/museo/publicaciones/recerques/recerques_0001.html); [edición de Serreta I de 1992](https://box.inh.cat/histocat.cat/resource/FletcherSerreta.pdf); [Ferrer i Jané 2024](https://www.researchgate.net/publication/387054058_Una_nova_mirada_al_plom_iberic_Villares_V_Kelin_Caudete_de_las_Fuentes_Un_text_comptable_amb_deu_transaccions).

## Algoritmos del Core

- `editorial_delta(texto_a, texto_b)` compara **secuencias Unicode de una edición** (normalizadas a NFC), y conserva operaciones de inserción, sustitución y supresión con sus índices. **Estos índices corresponden a caracteres editoriales, no a posiciones de trazos de la pieza.**
- `build_queue(root)` reconstruye de manera reproducible las 26 unidades desde las fuentes originales. Rechaza identificadores de revisión duplicados y discordancias de identidad en Serreta y Villares.
- `assess_blind_collation(submission)` requiere identificación exacta de la pieza, página y figura, archivo visual con SHA-256, recorte con coordenadas normalizadas, identificación del objeto revisada y **dos lecturas humanas independientes, realizadas a ciegas desde la imagen idéntica**. Las transcripciones publicadas no cuentan como segunda lectura ciega. Una discrepancia entre lectores bloquea la candidatura.
- Incluso cuando ambos lectores independientes coinciden, la función solo devuelve `READY_FOR_HUMAN_ADJUDICATION`: **nunca emite `scientifically_validated=true` ni habilita una traducción o regla del Core**. Una adjudicación humana externa posterior es imprescindible.

## Comandos reproducibles y controles negativos

```bash
python -m pip install -e .
python -m pytest -q tests/test_visual_adjudication.py
python scripts/audit_visual_signs.py --output /tmp/iberos-visual-sign-readiness.json
python scripts/audit_visual_signs.py --require-adjudicated
```

El último comando **debe terminar con código 2**, porque hoy faltan cotejos independientes. No es un fallo del software, sino una salvaguarda científica comprobable. Tests sintéticos de QA verifican rechazo de un solo lector, dos lectores del mismo grupo, copia de transcripción editorial, falta de coordenadas, imágenes de diferente hash, discrepancia de signos y autopromoción.

## Próximas acciones experimentales

1. Obtener una fotografía o figura reproducible de la **misma pieza**, comprobando condiciones de acceso y derechos de publicación.
2. Fijar imagen, cara, línea, posición y SHA-256. Seleccionar como primeros controles `SER-VAR-05` (SALIRG/SALIRIG) y `VIL5-A3` (segmentación vinculada a bobaida).
3. Recabar dos lecturas independientes y ciegas, no derivadas de Gómez Moreno, Ferrer o de la propia hipótesis IberOS.
4. Registrar también desacuerdos, lecturas ilegibles y abstenciones; el Core no debe optimizarse solo con resultados favorables.
5. Decidir con adjudicación externa y controles negativos **antes** de actualizar una ficha científica o evaluar cualquier hipótesis morfológica o semántica.

**Costes:** ninguno. **Imágenes:** enlazar a la fuente original hasta contar con permisos de reproducción. **Traducciones promovidas:** cero.
