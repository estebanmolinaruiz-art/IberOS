# IberOS CORE — Tanda 01: análisis de incertidumbre paleográfica (23-10-2026)

Se incorporó `scripts/iberos_core_sign_uncertainty.py`, analizador de solo lectura sobre `data/review/validation01_m06_mlh_17_candidate_matches_2026-10-22.csv`. El análisis preserva para cada posición el signo editorial, la familia de variantes candidatas MLH, una eventual variante exacta explícitamente acreditada, y el estado declarado de lectura independiente. La columna `semantic_translation` siempre se emite `null`: esta herramienta no infiere semántica.

En los datos actuales de Orleyl hay **17 posiciones**, **17 lecturas editoriales**, **17 variantes exactas no resueltas** y **0 lecturas independientes marcadas**. Se añadieron tres pruebas en `tests/test_iberos_core_sign_uncertainty.py` para asegurar ausencia de traducciones inventadas, conservación de la incertidumbre y separación entre bandera de lector independiente y validación científica.

Para reproducir:
```bash
python scripts/iberos_core_sign_uncertainty.py --output /tmp/iberos_sign_uncertainty.json
pytest -q tests/test_iberos_core_sign_uncertainty.py
```

La presencia de pruebas en el repositorio no equivale a certificar su paso por CI; tampoco representa mejora demostrada en reconocimiento óptico ni la resolución de M06/M07. Estos seguirán `PENDING`, con 30 % de preparación administrativa y `NOT_EVALUATED`.

Siguiente tanda propuesta: revisar transcripciones con créditos y fotografías fuente, preservar ambas orientaciones, entrenar solo con muestras DEVELOPMENT auditadas y contrastar falsos positivos con controles negativos reales.
