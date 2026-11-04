# EPI-IDENTITY-RESOLUTION-01 — La Vispesa y Pech-Maho

## Resultado del examen del FULL3406 original

**Pech-Maho B.7.38:** registros `@R3657` y `@R4192`
contienen secuencias de signos; `@R4467` es una **nota editorial**
con `signature=""`. Los tres tienen la misma
`dependency_key_v3_4_9` (`DEP341_28c9c6ea4262b500`) y están en
`VAL`. Corresponden al mismo documento de plomo B.7.38 en dos
lecturas editoriales más una nota. No son tres testimonios lingüísticos
independientes. La nota se excluye SOLO del cálculo derivado de textos,
sin borrarla de FULL3406 ni cambiar sus etiquetas.

**La Vispesa:** `D.12.1` (relieve de manos cortadas, inscripción en
relieve, `HOLD`) y `D.12.2` (fragmento de caballos, texto inciso,
`TRAIN`) son **dos conjuntos de piedra con inscripciones**.
Garcés (2007, pp. 341 y 347) trata como posible pero dudosa su
pertenencia a un mismo monumento; Velaza (2017, p. 243 n. 38)
considera la diferencia de técnica indicio contra la unidad.
Por tanto, hay dos identidades epigráficas materiales, pero la
dependencia de monumento/contexto no está resuelta; ambos se
bloquean como posibles parejas independientes TRAIN↔HOLD en una
nueva evaluación. La partición histórica original queda intacta.

Fuentes:
- https://euskerarenjatorria.eus/wp-content/uploads/2013/06/Bin%C3%A9far-1.pdf
- https://ifc.dpz.es/recursos/publicaciones/36/49/14velaza.pdf

## Ejecución

```bash
python -m iberos.epigraphic_identity_resolution /ruta/IberOS_LEAK_SAFE_v3_4_9_FULL3406.json --json /tmp/epi-identity-01.json
pytest -q tests/test_epigraphic_identity_resolution.py
```

El script obliga a comprobar SHA-256 y la integridad del FULL3406
original antes de generar el informe. No sube ni modifica el archivo,
no produce `gold` gramatical, no reentrena y no libera métricas. Las
pruebas de CI usan datos sintéticos y comprueban rechazos explícitos.
