# SCI-PRED-03 — Core científico, comparador real de predicciones selladas

**Fecha de revisión:** 2026-11-12. **Coste monetario:** 0 €. **PR:** #152. **Estado científico:** NOT_EVALUATED.

## Qué se ha implementado

1. `src/iberos/prospective_role_lock.py` ata ahora la predicción a `physical_id` y a los dos `participant_ids`, además del hash del protocolo original. Esto permite impedir que se evalúe una predicción sobre otra pieza.
2. `src/iberos/prospective_role_evaluation.py` admite **solo tras sellar** el expediente de roles declarado por dos evaluadores distintos, coteja identidades y hashes, fechas declaradas y linaje documental, y computa acierto/error por hipótesis, abstenciones, desacuerdos entre lectores, cobertura y desempeño frente a un baseline fijado previamente.
3. `scripts/evaluate_prospective_roles.py` proporciona un comando determinista para el cotejo: sin `--evidence` registra cero ensayos; los archivos de evidencia real deben suministrarse explícitamente. No consulta corpus HOLD ocultos.
4. `tests/test_prospective_role_evaluation.py` cubre **exclusivamente fixtures sintéticos**: predicción correcta, fallo, contradicción entre evaluadores, abstención, repeticiones físicas y de punzón, error de hash, cronología imposible y falta de baseline; un conjunto sintético de 16/20 produce *threshold candidate* **pero nunca promoción científica**.

## Auditoría documental que condiciona la prueba

Fuentes internas **sin modificación de origen**:

| Archivo | Lo que consta | Consecuencia |
| --- | --- | --- |
| `data/review/validation01_external_opaque_readings_batch01.csv` | 12 entradas de Cathalaunia/Corpus Ibèrika codificadas con fuente tipográfica opaca; sus estados son `NOT_DECODED` y `prospective_eligible=NO` | No pueden admitirse como lectura verificable ni como signos descifrados |
| `data/review/validation01_independent_review_register_v1.csv` | Dos entradas Orleyl con primera y segunda lecturas vacías y decisión `PENDING` | Ni siquiera la identidad paleográfica está doblemente certificada |
| `data/review/validation01_holdout_v1.csv` | Solo cabecera de evaluación, ninguna pieza HOLD con gold | No existe muestra ciega que pueda puntuarse |
| `data/review/validation01_new_hold_candidate_intake_v1.csv` | Solo cabecera de admisión | No puede marcarse ninguna pieza como HOLD nuevo |
| `data/review/editorial_readings_pending_v1.jsonl` | Lecturas de Sagunto, Caminreal y Casinos pendientes de cotejo; contienen advertencias explícitas de no usar significado o numerales sin fuente independiente | Pueden alimentar hipótesis retrospectivas, no un resultado prospectivo |

La copia de consulta del **Corpus Folch-Jiménez Huertas (febrero 2024)** en Drive contiene pestañas `text` y `cadenes` de hasta **4.509 y 4.472 filas de cuadrícula**, respectivamente. Sus grafías/codificaciones de fuente especial son material editorial; **no** son equivalentes a 8.981 signos o piezas con lectura verificada. No se ha importado ni recalculado `FULL3406`.

## Contraste científico adicional: parentela de Badalona

- **B.41.02 y B.41.03 (estelas funerarias de Baetulo/Badalona)** proporcionan una comparación útil entre una fórmula antroponímica simple y otra con `ebanen` asociada a dos nombres. Comas, Padrós y Velaza (2001, pp. 291–299) plantean la posible relación padre/hijo a partir de la propia lectura y de paralelos onomásticos.
- [Edición de 2001 (Palaeohispanica 1)](https://ifc.dpz.es/recursos/publicaciones/20/39/_ebook.pdf) y [Moncunill sobre el cambio de fórmulas onomásticas](https://una-editions.fr/se-nommer-devant-lautre-ladaptation-des-noms-iberiques-a-la-formule-onomastique-romaine/).
- **Veredicto:** candidato de **entrenamiento/retrospectivo**, no gold de parentesco independiente. La procedencia compartida y la reutilización de ambas piezas en una cubierta de colector tampoco demuestran por sí mismas una relación familiar biológica.
- Línea futura separada `H-EBAN`: buscar **nuevos** emparejamientos padre/hijo con fuente extralingüística independiente. No utilizar este caso para evaluar `-te` productor/comitente ni adaptar a posteriori el protocolo SCI-PRED-02.

## Ejecución local y lectura del resultado

```bash
python -m pip install -e . pytest
python -m pytest -q tests/test_prospective_role_lock.py tests/test_prospective_role_evaluation.py
python scripts/evaluate_prospective_roles.py --output /tmp/iberos-roles-audit.json
```

La ejecución sin entrada GOLD produce `INSUFFICIENT_N`, `total_attempted_physical_objects=0`, `scientific_pass=false` y `translation_validated=false`. Éste es **un diagnóstico correcto**, no un fracaso operativo del software.

Cuando exista un **nuevo objeto con evidencias independientes**, el proceso será:
- Selección física y resolución de aliases/punzón.
- Doble lectura ciega de signos y etiquetado de papeles externos por dos evaluadores.
- Sellado de predicción sobre entrada **sin gold**, con identificación de pieza/participantes y archivo comprometido antes de revelar etiquetas.
- Publicación/revisión externa de la anterioridad del compromiso y de la independencia de etiquetas.
- Evaluación con `--evidence` sobre predicción congelada y roles desvelados después.
- No cambiar regla, exclusiones o baseline al conocer fallos. Incluir todas las abstenciones. Solo un arbitraje científico externo puede declarar éxito.

## Siguiente bloqueo concreto que debe resolverse

**No falta otro validador técnico:** faltan **lecturas revisadas, referencia física inequívoca y papeles independientes del texto ibérico** en un objeto nuevo. Priorizar una colaboración gratuita de paleógrafos/arqueólogos, ediciones de acceso abierto y contactos institucionales ya iniciados, evitando solicitudes repetidas a instituciones que han respondido que no disponen de nuevas fotografías.

## Límites

- `scientific_pass=false` incluso con resultados sintéticos perfectos; ninguna declaración de un evaluador es una prueba automática de independencia.
- Las fechas introducidas, hashes y URL no constituyen verificación independiente de la cronología: deben contrastarse con una publicación/commit inmutable y tercero.
- No se actualizan CORE (27/45), ICS, FULL3406, web ni DNS.
- El resultado ya puede contener **errores predictivos reales** cuando se aporten datos, pero por ahora **0 casos semánticos adjudicados y 0 traducciones confirmadas**.
