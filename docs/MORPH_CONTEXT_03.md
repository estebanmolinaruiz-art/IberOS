# MORPH-CONTEXT-03 — contextos de BI-N frente a controles

Diagnóstico **retrospectivo** sobre FULL3406 original, verificado por
SHA-256. Solo TRAIN y VAL. HOLD (623 registros) y EXCLUDED (59)
se excluyen sin consultar sus \`signature\` en esta ejecución; el
archivo original conserva sus 3.406 registros y particiones.

Se cuentan signos inmediatos antes y después de los bigramas BI-N,
BA-N, A-N y BI-R1, sin cruzar \`¦\` ni otros límites editoriales.
El soporte \`support\` se trata como categoría literal editorial:
\`plom\` no permite inferir automáticamente transacción comercial;
falta de soporte no implica ausencia arqueológica.

Resultados del primer cotejo local:

| Métrica BI-N | TRAIN | VAL |
| --- | ---: | ---: |
| Apariciones | 34 | 7 |
| UID distintos | 31 | 4 |
| Grupos de dependencia | 23 | 4 |
| Inicio de segmento | 15 | 0 |
| Precedido por R1 | 11 | 1 |
| Seguido por KE | 5 | 0 |
| Seguido por Y | 4 | 2 |
| Fin de segmento | 9 | 2 |
| Apariciones con soporte \`plom\` | 11 | 0 |
| Apariciones sin soporte anotado | 6 | 5 |

Las categorías de contexto se superponen (una misma aparición puede
estar al inicio y seguida por un signo). **Ninguna constituye por sí
sola una identificación de sufijo, nombre o numeral.** Las ediciones
dependientes no son observaciones independientes.

Ejecución:
\`\`\`bash
python -m iberos.morph_context_03 /ruta/IberOS_LEAK_SAFE_v3_4_9_FULL3406.json --json /tmp/morph-context03.json
pytest -q tests/test_morph_context_03.py
\`\`\`

Siguiente puerta científica: revisar soportes originales y lecturas
epigráficas, prerregistrar criterios de contexto cuantitativo con
evidencia independiente y aplicar los modelos a inscripciones no vistas.
Sin nuevos datos independientes, esto sigue siendo descripción.
