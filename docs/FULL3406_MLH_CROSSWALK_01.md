# FULL3406_MLH_CROSSWALK_01 — concordancias documentales controladas

Cruce de lectura entre el JSON original LEAK-SAFE v3.4.9 y el registro
público de 38 objetos. Se comprueba SHA-256 antes de consultar los registros
privados; el JSON congelado NO se incorpora ni publica en GitHub.

Uso:
\`\`\`bash
python -m iberos.catalog_crosswalk /ruta/IberOS_LEAK_SAFE_v3_4_9_FULL3406.json data/curated/iberos_objects_registry_v2.0.csv --json /tmp/mlh-crosswalk.json
pytest -q tests/test_catalog_crosswalk.py
\`\`\`

Hallazgos de ejecución local (04-11-2026), con el JSON original y los
38 identificadores editoriales del catálogo curado:

- 10 objetos con candidatos bibliográficos, 13 UID históricos distintos.
- 8 objetos con código editorial directo, 1 con citas incrustadas
  (B.7.38) y 1 familia editorial con dos particiones (D.12.1-2).
- 25 sin referencia MLH explícita en el campo analizado y 3 sin
  coincidencia textual.
- D.12.1 en HOLD frente a D.12.2 en TRAIN bajo el mismo campo de
  referencia del objeto curado IBR-LAP-0002. Esto exige revisión de
  identidad material. NO se declara una fuga física automáticamente.
- Las coincidencias F.13.3 y F.13.30 se mantienen separadas.

Todas las coincidencias son D1 de IDENTIFICADOR EDITORIAL, no pruebas
de identidad de objeto, morfología o significado. No se alteran los
splits originales, sus claves ni las métricas oficiales. Los casos
D.12.1-2 y B.7.38 son prioritarios para cotejo externo.


## Cotejo arqueológico de D.12.1 / D.12.2

Ignasi Garcés Estallo, «Nuevas interpretaciones sobre el monumento
ibérico de La Vispesa (Tamarite de Litera, Huesca)»,
*Cæsaraugusta* 78 (2007), pp. 337-354, identifica explícitamente los
dos testimonios editoriales: D.12.1 en el relieve con manos cortadas y
D.12.2 en el fragmento con caballos. La posible procedencia de un único
monumento y la relación física entre ambos fragmentos son objeto de
discusión bibliográfica. Fuente de contraste:
https://euskerarenjatorria.eus/wp-content/uploads/2013/06/Bin%C3%A9far-1.pdf

El hecho de que FULL3406 sitúe las dos referencias en HOLD y TRAIN
respectivamente **no prueba todavía** una fuga del mismo objeto físico.
Es una alerta para revisar fotografías, inventario del Museo de Huesca,
identidad de fragmentos y LEAK_GROUP original antes de puntuar resultados.
