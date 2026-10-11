# IberOS Curated Benchmark v1.0.1

El benchmark público contiene la capa curada de **38 objetos** de IberOS.

Está diseñado para interoperabilidad, control de fuga, recuperación de familias, procedencia y comparación con otros sistemas.

## Alcance

No es una republicación completa del corpus epigráfico ibérico.

La capa histórica de 3.406 ENTRY permanece como **LEGACY / FROZEN** y sus métricas no deben extrapolarse automáticamente al corpus vivo de Cathalaunia / Iberika.

La integración con el corpus vivo es parcial y no debe describirse como ingestión total.

## Control separado de D(E/I)

`iberos dedi-benchmark evidencia.json` conecta la matriz formal con
`DEDI-COMBINED-GATE-01`. El JSON de entrada contiene `observations`,
`preregistered_rule`, `preregistration_id` y `preregistration_hash`.
Los campos de cada observación se documentan en
`src/iberos/core.py`: `evaluate_dedi_predictive_gate` y
`audit_dedi_prospective_provenance`.

El informe devuelve `formal_matrix` y `semantic_gate` por separado.
Reconocer la estructura no resuelve la oposición gramatical E/I. Evidencia
incompleta devuelve BLOCKED; evidencia documental y predictivamente completa
solo puede devolver AWAITING_INDEPENDENT_REVIEW con scientific_state UNVERIFIED.
Un resultado de software no es una validación epigráfica.

Los 38 objetos curados no se convierten automáticamente en HOLD prospectivo.
Las piezas utilizadas para construir las reglas siguen siendo retrospectivas.
Las pruebas sintéticas verifican controles del programa y no incrementan
D(E/I)=50 ni ninguna métrica oficial. Autoridad: C594+C474+C539+C541.
