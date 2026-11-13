# SCI-PRED-01 — Works de predicción y traducción experimental

**Fecha:** 2026-11-12. **Programa:** Dama de IberOS. **Coste:** 0 €; sin APIs comerciales, sin entrenamiento cloud de pago ni cron periódico.

## Objetivo prioritario

Proponer **significados y posibles traducciones contrastables** de inscripciones ibéricas, comparar hipótesis rivales y registrar predicciones **antes** de conocer evidencia nueva. Medir aciertos, errores, falsos positivos, abstenciones y desempeño frente a baselines; publicar incluso resultados negativos. La traducción es el objetivo científico, no un efecto secundario del mantenimiento de la web.

## El punto de partida real

- CORE-X P01 (`scripts/corex_p01.py`) ya ofrece frecuencia y bigramas para predicción de caracteres cuando existen **seis o más grupos físicos independientes con lectura verificada**. Esto mide grafemas, no significados; no ejecutar sobre metadatos del catálogo fingiendo que son transcripciones.
- `src/iberos/semantic_hypothesis_engine.py` propone dominios de hipótesis, `interpretation_candidates.py` ordena expedientes por integridad documental y `prediction_compare.py` contrasta predicciones selladas con hallazgos externos; ninguna de esas operaciones constituye validación semántica.
- HOLD-01 conserva el bloqueo por falta de gold semántico y por incertidumbre de contaminación documental; no consumir sus textos como material de entrenamiento.
- La Serreta registra 8 alternativas de una pieza editorial D1; sirve para sensibilidad, no para multiplicar evidencia independiente.
- Los indicadores congelados CORE 27/45 o ICS 70,8 son internos y quedan intactos.

## Tres works y criterios de cierre

### WORK-01 — Material y predicción reproducible

1. Reconciliar identificadores físicos, ediciones y fuentes para evitar fugas TRAIN/VAL/HOLD, incluyendo Folch 2024 y FULL3406 sin alterar sus originales.
2. Obtener lectura de signos independiente y contexto extratextual verificable por pieza; nunca inventar signo, rol ni gold.
3. Ejecutar CORE-X P01 sobre corpus de lectura revisada: frecuencia, bigramas y ablataciones; reportar total por grupo, exactitud fuera de muestra, errores y abstenciones.
4. **Cierre:** fuente, SHA, particiones disjuntas, seis o más unidades independientes admitidas para el baseline y evaluación reproducible. No se infiere porcentaje de traducción.

### WORK-02 — Posibles traducciones rivales

1. Para cada objeto, describir lectura fuente, contexto, hipótesis en español, lectura alternativa, predicción falsable y observación capaz de refutarla.
2. Piloto inicial: **Caminreal (MLH E.7.1)**, lectura editorial *likine-te · ekiar · usekeŕte-ku*. Comparar la paráfrasis **Likine hizo/realizó [la obra]**, la alternativa **Likine encargó [la obra]** y la hipótesis nula **papel no determinable**. Son alternativas retrospectivas, no traducciones demostradas.
3. Enrollar como nuevo test solo piezas cuya información independiente no haya servido para formular la regla: por ejemplo, papeles *productor/comitente* acreditados desde documentación externa y no deducidos del sufijo examinado.
4. **Cierre:** dos o más hipótesis incompatibles con predicciones discriminativas por experimento, fijadas antes del test, fuentes y objeciones registradas. Sin gold: estado NOT_EVALUATED.

### WORK-03 — Evaluación ciega y publicación

1. Prerregistrar hipótesis exacta, criterio de victoria, baseline, métricas, tamaño mínimo e incertidumbre; registrar huella y sello cronológico verificable.
2. Separar por **pieza física y linaje editorial**, cotejar dos lecturas de signos independientes y utilizar exclusivamente gold contextual verificado fuera del texto objetivo.
3. Evaluar prospectivamente soporte, contradicción, cobertura, abstención y negativos; análisis de sensibilidad editorial y ablaciones por soporte y contexto.
4. **Cierre:** paquete público reproducible, dictamen externo sobre signos/roles, tabla completa de aciertos y fallos, manuscrito revisable. Una traducción necesita respaldo semántico independiente, no sólo passing CI.

## Ejecución en GitHub, sin saturación

El workflow `.github/workflows/science-prediction-translation.yml` solo se activa al abrir/modificar la PR en los archivos del experimento o manualmente desde Actions. **No** hay tarea horaria ni acceso a API externa. Ejecuta tests del docket y controles existentes, publica JSON de auditoría como artefacto y comprueba que la petición de confirmación científica se rechaza con código 2 hasta disponer de gold independiente.

Desde un checkout instalado: 

    python -m pip install -e . pytest
    python -m pytest -q tests/test_prediction_translation_work.py
    python scripts/run_prediction_translation_works.py --output /tmp/iberos-sci-pred-01.json
    python scripts/run_prediction_translation_works.py --require-scientific-confirmation

La última orden debe devolver 2. Un control técnico correcto no se convierte por ello en un hallazgo lingüístico.

## Trazabilidad de fuente y límites

- Texto del piloto y antecedentes: DOI [10.36707/palaeohispanica.v0i15.39](https://doi.org/10.36707/palaeohispanica.v0i15.39). La ficha IberOS es retrospectiva, y su texto editorial se ha consignado sin autopsia independiente.
- La documentación externa Hesperia permite contrastes bibliográficos, pero sus datos y licencias no se incorporan automáticamente al proyecto ni se cuenta una edición secundaria como segunda observación independiente.
- `data/review/prediction_translation_pilot_v1.json` contiene las **tres hipótesis posibles** y sus predicciones; `src/iberos/prediction_translation_work.py` verifica identidad, fuente, nivel documental y abstención; `scripts/run_prediction_translation_works.py` recopila los bloqueos originales de HOLD y gates.
- Los hashes SHA-256 de los enunciados permiten detectar cambios, **no** demuestran por sí solos prioridad temporal, preregistro, acierto o significado verdadero.
- No modificar FULL3406, métricas científicas congeladas, web, DNS ni despliegues en esta entrega.

**Veredicto inicial:** hipótesis lingüísticas preparadas, predicción semántica NO EVALUADA, traducciones validadas: 0. Próximo experimento decisivo: primer objeto nuevo con dos roles extratextuales diferenciados y una lectura independiente apta para evaluación ciega.
