# NUMERIC-EVIDENCE-GATE-01 · evidencia metrológica y BI/BIN

Una fuente externa puede respaldar un **contexto cuantitativo** sin validar
una traducción ni convertirse en material para un HOLD genuinamente nuevo.

- Ferrer i Jané y Escrivà Torres, *Palaeohispanica* 14 (2014), 205-227:
  https://doi.org/10.36707/palaeohispanica.v0i14.54
  Plomo de Casinos con expresiones metrológicas a-o-ki en ambas caras;
  los autores proponen bi/bin como posible numeral 2, pero advierten
  que el valor concreto NO queda confirmado. La localización exacta del
  hallazgo tampoco está establecida.
- Ferrer i Jané, *Palaeohispanica* 9 (2009), 451-479:
  https://doi.org/10.36707/palaeohispanica.v0i9.239
  Argumentos combinatorios y monedas, **revisión**, no nuevo objeto
  con valor cuantitativo gold verificado.

La **búsqueda en metadatos** del snapshot FULL3406 original con SHA-256
verificado localiza: \`P14,9 Casinos (València) cara A@R4128\` en
**HOLD**. Por tanto **NO elegible para evaluación ciega inédita**.
No se ha leído su firma en este nuevo examen. La ausencia de un
término en \`catalog_id\` NO certifica independencia física.

\`\`\`bash
python -m iberos.numeric_evidence_gate_01 /ruta/IberOS_LEAK_SAFE_v3_4_9_FULL3406.json --json /tmp/gate-01.json
pytest -q tests/test_numeric_evidence_gate_01.py
\`\`\`

Puerta futura: objeto con identidad y procedencia originales verificadas,
fuera de TODAS las particiones previas, apógrafo comprobado, anotación
cuantitativa externa sin acceso a BI/BIN, controles negativos y
predicciones prerregistradas antes de leer el nuevo texto. No subir el
JSON histórico a GitHub ni cambiar métricas/particiones existentes.
