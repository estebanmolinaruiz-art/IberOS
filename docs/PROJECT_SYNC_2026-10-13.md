# IberOS — sincronización entre hilos y continuidad científica
**Fecha de corte:** 2026-10-13
**Ámbito:** consolidación de conversaciones disponibles en el proyecto y comprobación de archivos del repositorio `main`.
**Naturaleza:** documento de coordinación; **no** es una nueva decisión científica, benchmark, release ni validación independiente.

## Separación permanente de responsabilidades

1. **Hilo CORE científico (este hilo):** corpus, evidencia, hipótesis, independencia documental, gates prospectivos, controles negativos, pruebas, reproducibilidad. La autoridad científica solo se modifica con decisión explícita versionada y soporte verificable.
2. **Hilo web pública:** experiencia de uso, accesibilidad, navegación, fichas, Laboratorio, despliegue, integración del CORE. No puede adjudicar por sí mismo validez lingüística.
3. **Hilos de aplicación móvil / Write / Talk:** interfaces, empaquetado e interacciones experimentales. Deben consumir estados del CORE sin promover hipótesis.
4. **Hilos publicación, EpiHub y seguimiento exterior:** documentación, DOI, repositorio, comunicación pública y condiciones de reevaluación. No sustituyen validación independiente.
5. **Red Hermana y seguimiento de menciones:** ámbitos diferenciados, sin equivalencia con evidencia del corpus.

## Inventario contrastado en GitHub (main)

- `README.md` y `docs/ARCHITECTURE.md`: mapa de arquitectura y versión pública descrita como 1.0.1.
- `src/iberos/core.py`: funciones de registro, auditoría de independencia, gates familiares y prospectivos, controles adversariales y matrices.
- `src/iberos/reconstruction.py`: validación de segmentos y construcción conservadora de reconstrucciones; salida `scientific_state=UNVERIFIED`, `automatic_core_promotion=false`.
- `tests/test_reconstruction.py`: pruebas de reglas y entradas adversariales, añadidas al árbol.
- `site/ficha/index.html`: bloque central de reconstrucción de gran tamaño; color por clasificación documental expresa.
- `site/laboratorio/index.html`: cuaderno de investigación de lectura visual y exportación.
- `site/webengine/index.html`: explorador documental que debe distinguirse explícitamente del CORE Python.

## Autoridad y restricciones científicas preservadas

- Cadena: `C594` (semántica), `C474` (cierre prospectivo), `C539` (suelo técnico), `C541` (red ROK).
- Capas: EVIDENCE → INFERENCE → HYPOTHESIS → ESTIMATED_TRANSLATION.
- Independencia: PHYS_ID > LEAK_GROUP > grupo de dependencia específico > OBJECT_ID.
- Splits: HOLD > VAL > TRAIN.
- Benchmark documentado de v1.0.1: 38 objetos curados, 37 unidades documentales independientes, 4 controles excluidos.
- Gates semánticos estrechos abiertos (según `docs/BENCHMARK.md`): ROK, KA/KE/KU, SALIR, KUTUR, rótulos exactos BAIDES/BATIR, valores exactos 7/8/9, oposición gramatical exacta D(E/I).
- Indicadores oficiales congelados de release: CORE 27/45 (60,0 %) y CORE+INFER 28/45 (62,2 %); no son porcentaje de desciframiento.

## Norma de reconstrucción compartida

Si no hay traducción demostrada, presentar reconstrucción parcial apoyada en evidencia; distinguir gráficamente lectura documentada, reconstrucción plausible, ambigüedad y elemento irresuelto. El color de una lectura atestiguada **no** implica que su significado esté demostrado. Cada propuesta interpretativa requiere procedencia, explicación y límites. La visualización no puede realizar promoción científica automática.

## Riesgos y tareas pendientes

1. **Ejecutar y certificar tests completos** de Python y JS en una ejecución actual; el mero almacenamiento de archivos de prueba no acredita su resultado.
2. **Auditar el contrato de segmentos:** identidad exacta del objeto, trazabilidad a pasajes de la fuente, revisión de validez documental real (una cadena `source` sin más es una declaración, no comprobación), ortografía, equivalencias y controles sobre inferencias.
3. **Comprobar reproducción del benchmark** contra snapshot y verificar que el nuevo código no altera autoridad ni gates abiertos.
4. **Integración web–CORE:** comprobar que la interfaz solo muestra resultados que procedan de objetos efectivamente validados; el WebEngine navegador actualmente es un explorador documental, no ejecuta todo el CORE Python.
5. **Pruebas independientes** y revisión experta antes de elevar cualquier hipótesis.
6. **Publicación:** verificar por separado DOI específico de software, snapshot Software Heritage y despliegue web; no deducirlos de menciones antiguas.

## Regla de cierre

No marcar **CORE definitivamente depurado** hasta tests ejecutados, regresiones resueltas, benchmark reproducido, controles prospectivos preservados, trazabilidad de segmentos auditada y documentación final coherente. Las conclusiones científicas no se infieren de funcionalidades web ni de métricas de ingeniería.

## Fuentes internas de coordinación

Resumen de conversaciones del proyecto disponible en este contexto (hilos web pública, app móvil, EpiHub, publicación, red hermana, seguimiento); archivos comprobados en el repositorio al 2026-10-13. No existe acceso garantizado al texto íntegro de **todos** los hilos, por lo que esta sincronización es de los avances visibles y verificables, no una auditoría exhaustiva de conversaciones.
