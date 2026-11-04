# MORPH-STRATA-01 — primer ensayo exploratorio con 3.406 entradas

Auditoría ejecutada sobre la copia ORIGINAL LEAK-SAFE v3.4.9
(`FULL3406`, SHA-256 verificado), sin alterar los 3.406 registros ni
`split_v3_4_9`/`dependency_key_v3_4_9`. Se excluyen del análisis
morfográfico los 59 registros `EXCLUDED`, preservándolos en origen.

El corpus contiene secuencias de grafemas separadas por guiones, no
transcripciones normalizadas. El algoritmo nunca cruza `¦` ni
separadores editoriales, y distingue explícitamente `R` y `R1`.

Resultados **retrospectivos**, no prospectivos:

| Motivo literal | Ocurrencias | UID con patrón | Grupos de dependencia | Grupos TRAIN/VAL/HOLD |
| --- | ---: | ---: | ---: | --- |
| `BA-I-TE-S` | 12 | 9 | 9 | 2 / 5 / 2 |
| `BA-TI-R` + `BA-TI-R1` | 15 | 5 | 5 | 3 / 0 / 2 |
| `KU-TU-R` + `KU-TU-R1` | 10 | 10 | 9 | 5 / 3 / 1 |
| `BI-N` | 46 | 38 | 30 | 23 / 4 / 3 |
| `BI` como segmento completo | 11 | 11 | 6 | 3 / 0 / 3 |

`BA-I-TE-S` **no demuestra** una lectura `BAIDES`, y `BI-N`
**no demuestra** numeral 2 ni morfema gramatical. Las cifras combinadas
son solo agregados de grafías; nunca neutralizan signos en la entrada.

Una secuencia puede repetirse varias veces en un único documento. Por
ejemplo, `BA-TI-R` acumula 13 ocurrencias en 3 UID, por lo cual
la frecuencia ingenua exageraría la evidencia. Los grupos de
dependencia se contabilizan independientemente por split.

Se trata de una exploración sobre el corpus ya conocido. **No**
representa acierto lingüístico, prueba ciega, significado descifrado o
predicción independiente. No hay `gold` de gramática y no se
actualizan las métricas científicas oficiales.

Ejecución con la copia privada que el usuario ya recuperó:

```bash
python -m iberos.morph_strata_01 /ruta/IberOS_LEAK_SAFE_v3_4_9_FULL3406.json --json /tmp/MORPH-STRATA-01.json
pytest -q tests/test_morph_strata_01.py
```

Próximo paso: fijar previamente hipótesis rivales concretas, controles
negativos, criterios de abstención y corpus independiente no visto;
solo después medir su capacidad predictiva.
