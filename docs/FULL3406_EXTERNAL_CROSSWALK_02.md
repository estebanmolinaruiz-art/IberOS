# FULL3406-EXT-02 — enlaces Corpus Ibèrika/Hesperia/BDH, sin falsos emparejamientos

Aprovecha el registro público de concordancias
\`data/curated/iberos_partial_entry_link_v2.4.csv\` y el catálogo de
38 objetos. Exige SHA-256 y auditoría del FULL3406 privado antes de
intentar cotejos de etiquetas bibliográficas.

Se mantienen **tres identidades diferentes**:
1. \`OBJECT_ID\` interno IberOS, agrupación curada.
2. \`Ixxxxx\` código de entrada de Corpus Ibèrika/Cathalaunia, a veces
   cara, segmento o registro editorial, NO un objeto físico completo.
3. \`uid\` de LEAK-SAFE v3.4.9, en FULL3406 privado.

Los enlaces ya existentes llevan \`Link_Status\` y \`Confidence\`.
Un \`PARTIAL_GROUP\` o \`MULTI_ENTRY_REVIEW\` **no se promociona** por
encontrar una etiqueta textual. Los códigos BDH no se convierten
automáticamente en identificadores MLH.

Ejemplos cotejados documentalmente en Corpus Ibèrika:
- \`I01320\`: la ficha identifica \`d.12.1 a\`, grupo del monumento de
  La Vispesa y enlace BDH \`HU.01.01\`.
  https://cathalaunia.org/Iberika/I01320
- \`I03095\`/\`I03096\`: fichas de dos caras de la fusayola de
  Can Rodon; enlace BDH \`B.44.39\`.
  https://cathalaunia.org/Iberika/I03095
- \`I03622\`/\`I03623\`: dos caras del pequeño plomo del Pico
  de los Ajos, referencia de web \`V.13.07\`.
  https://cathalaunia.org/Iberika/I03622
- \`I02572\`: plomo de Tivissa, ficha con referencia web
  \`T.07.03\`.
  https://cathalaunia.org/Iberika/I02572

Las etiquetas y los códigos aportan candidatos documentales,
NO equivalencias físicas demostradas, ni nuevas lecturas D2/D3.
Revisión signo a signo, objetos físicos y posibles copias pendientes.

## Ejecución

\`\`\`bash
python -m iberos.external_crosswalk \
  /ruta/IberOS_LEAK_SAFE_v3_4_9_FULL3406.json \
  data/curated/iberos_objects_registry_v2.0.csv \
  data/curated/iberos_partial_entry_link_v2.4.csv \
  --json /tmp/full3406-external-crosswalk-02.json
pytest -q tests/test_external_crosswalk.py
\`\`\`

No modificar el archivo congelado ni las particiones originales,
ni usar el resultado para entrenamiento o medición de traducción.
