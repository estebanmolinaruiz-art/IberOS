# IberOS CORE — auditoría de validación ejecutable
Fecha: 2026-10-13
Estado: **NO CERTIFICADO** (no afirmar PASS sin resultado de job + comparación de snapshot).

## Material inspeccionado
- `.github/workflows/tests.yml`: ejecuta `pip install -e . pytest`, `pytest -q` y pruebas Node.
- `.github/workflows/benchmark.yml`: además ejecuta `python scripts/benchmark_snapshot.py --output /tmp/benchmark_results_v1.0.1.json` y `diff -u data/benchmark/benchmark_results_v1.0.1.json /tmp/benchmark_results_v1.0.1.json`.
- `scripts/benchmark_snapshot.py`: deriva los resultados de registro, independencia y matrices científicas.
- `data/benchmark/benchmark_results_v1.0.1.json`: referencia congelada de 38 objetos, 37 unidades, 1 colapso, 4 excluded controls, gates abiertos y sin promoción automática.
- Página pública GitHub Actions: el flujo `benchmark` cuenta con ejecuciones visibles para commits de los módulos de reconstrucción y métricas, pero la vista consultada no proporciona un resultado SUCCESS/FAIL inequívoco ni logs confirmados para un estado final actual.
- La descarga git desde el contenedor de ejecución no funciona por DNS (github.com); en consecuencia **no se ha realizado una ejecución local de pytest ni diff**.

## Protocolo reproducible exacto
```bash
python -m pip install -e . pytest
python -m pytest -q
python scripts/benchmark_snapshot.py --output /tmp/iberos_snapshot.json
diff -u data/benchmark/benchmark_results_v1.0.1.json /tmp/iberos_snapshot.json
node --test tests/test_write.mjs tests/test_talk.mjs
```

## Criterios de aceptación
1. `pytest` devuelve salida final inequívoca sin tests fallidos;
2. snapshot byte-idéntico (diff sin cambios);
3. tests Node finalizan correctamente;
4. ejecuciones registradas contra el SHA actual de `main` (o SHA explícito de release);
5. auditoría humana revisa si los gates y controles adversariales siguen intactos.

## Riesgos a revisar antes de certificar
- Asegurar que las identidades cruzadas PHYS_ID/LEAK_GROUP/Dependency_Group no mezclan testimonios heterogéneos por identificadores genéricos.
- Auditoría de reconstrucción comprueba registros de fuentes, **no su verdad paleográfica ni lectura**.
- Los tests sintéticos no constituyen evidencia independiente real.
- No modificar métricas `C594/C474/C539/C541` por estado técnico.

## Certificación verificable posterior — 2026-10-13
**Se conserva la auditoría anterior como registro de la incertidumbre inicial.** Se ha podido recuperar finalmente el estado de GitHub Actions mediante el endpoint público de ejecuciones y contrastar la misma ejecución con la API de trabajos conectada.

- Workflow: `benchmark`, ejecución **#28**, run ID **38465601249**.
- Commit evaluado: `e8b670c69f7cb0e71c6b2531b76a30cbd43d1ecc`.
- Estado de ejecución: `completed`; conclusión: **`success`**.
- Trabajo `benchmark` (ID **115531481927**): `completed`, **`success`**.
- URL: https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/38465601249
- El workflow versionado requiere `pytest -q`, regeneración de snapshot y `diff -u`; conclusión satisfactoria demuestra que la secuencia configurada pasó para el SHA señalado.
- **Alcance:** certificación técnica de CI del SHA evaluado, no revisión independiente del significado de las inscripciones ni de versiones posteriores. El último commit en main puede ser diferente.
- `CORE=27/45`, `CORE+INFER=28/45` y gates permanecen congelados.
