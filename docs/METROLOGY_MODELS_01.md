# METROLOGY-MODELS-01 — comparativa descriptiva decimal/duodecimal

Fecha: 2026-11-04. Este análisis utiliza masas publicadas, **no
mediciones institucionales independientes**. Resultados post hoc:
las piezas ya fueron seleccionadas por la literatura sobre el modelo
\`a-o-ki\`, por lo que no son un conjunto ciego.

- Puig de la Misericòrdia (CS.02.01): ponderal marcado \`o\`, 41,29 g.
- Tos Pelat: ponderal de bronce, 418 g, diez puntos publicados.
- Puig Castellar: masa publicada 423,78 g.
- L'Alcúdia: masa publicada 424 g.

Con ancla **o = 41,29 g**, dos predicciones (idéntica ancla):

| Hipótesis | Peso a predicho | Error Tos Pelat | Error Puig Castellar | Error L'Alcúdia |
|---|---:|---:|---:|---:|
| 10 × o | 412,90 g | +5,10 g | +10,88 g | +11,10 g |
| 12 × o | 495,48 g | −77,48 g | −71,70 g | −71,48 g |

**El modelo decimal se ajusta mejor a estas tres masas publicadas
seleccionadas**; no demuestra la lectura léxica de \`abaŕ\` ni \`bi=2\`.
Las diez marcas son argumento adicional condicionado a su examen
fotográfico e interpretación epigráfica independiente.

**Control crítico:** Ferrer i Jané (2026) indica que el ponderal de
493 g publicado en 1930 para La Bastida presentaba una errata y retira
la única evidencia física que se había invocado para una relación pura
12:1 entre las unidades mayores. Este registro no debe usarse como
medida verificada.

Fuentes:
- Ferrer i Jané, *Archivo de Prehistoria Levantina* XXXVI (2026):
  https://mupreva.org/web_mupreva_dedalo/publicaciones/1642/va
- Análisis sobre metrología ibérica *Lucentum* 43 (2024):
  https://doi.org/10.14198/LVCENTVM.23777
- Contacto Tos Pelat verificado en página institucional de turismo:
  https://www.comunitatvalenciana.com/es/valencia/moncada/eventos/visitas-en-el-yacimiento-iberico-del-tos-pelat-de-moncada-ruta-de-los-iberos-valencia

Pendiente: informe de museo con inventario, error instrumental, marcas
fotografiadas y conservación; incorporar todas las pesas de la misma
familia, no únicamente las próximas a 420 g; definir plan predictivo
independiente **antes** de abrir lecturas de cualquier nuevo objeto.

\`\`\`bash
python -m iberos.metrology_models_01 --json /tmp/metrology_models_01.json
pytest -q tests/test_metrology_models_01.py
\`\`\`

No se incluye ni modifica FULL3406. Sin métricas de traducción ni
interpretaciones científicas promovidas automáticamente.
