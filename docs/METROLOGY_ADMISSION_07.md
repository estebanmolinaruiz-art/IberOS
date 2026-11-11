# METROLOGY-ADMISSION-07 — protocolo de admisión antes de interpretar signos

11-11-2026. Puerta **fail-closed** que distingue:

1. **Masa original verificable:** identificador físico, institución e inventario; masa, balanza, resolución, incertidumbre, calibración, fecha y conservación.
2. **Marca legible independientemente:** imagen original accesible con condiciones de uso, dos anotadores distintos que desconocían el peso y las hipótesis lingüísticas, e informe de discrepancias.
3. **Predicción genuinamente nueva:** identidad física revisada frente a FULL3406 y alias bibliográficos, objeto no publicado/visto previamente, hipótesis preregistrada ANTES de la lectura, y controles negativos declarados.

La función devuelve **ABSTAIN_PENDING_EVIDENCE** si falta cualquier campo. Las discordancias entre dos lecturas se conservan: no se inventa consenso. Incluso si un expediente sintético reúne todas las condiciones, la herramienta **no traduce automáticamente**; solo autoriza preparar una evaluación preregistrada posterior.

Estatus documental al 11-11-2026:
- Puig de la Misericòrdia, Museu de Belles Arts de Castelló, ficha 2309, masa publicada 41,29 g, lectura o del autor: **NO** incertidumbre instrumental acreditada ni segunda lectura independiente.
- Puig Castellar, MAC, masa publicada 423,78 g, inscripción discutida y anilla de hierro: **NO** incertidumbre acreditada ni doble lectura.
- Tos Pelat, Moncada, 418 g y diez puntos publicados: museo ha respondido que remitirá la información, sin datos primarios recibidos.

Correo a Castelló y MAC enviado el 11 de noviembre de 2026, sin coste. Mantener los tres expedientes abiertos; no activar GOLD científico ni reclamar desciframiento.

Ejemplo de uso con un nuevo archivo JSON de registros físicos (no FULL3406):
```bash
python -m iberos.metrology_admission_07 fichas_primarias.json --json dictamenes.json
pytest -q tests/test_metrology_admission_07.py
```

No se accede a FULL3406 ni se cambia una sola partición o métrica.
