# METROLOGY-SENSITIVITY-05 — sensibilidad de los 37 pesos

Extensión de METROLOGY-ASSEMBLAGES-04. Se conservan **los mismos
37 pesos de los mismos cinco conjuntos** y las 12 razones publicadas,
sin retirar resultados discordantes ni cambiar los pesos.

| Tolerancia con unidad fija de 2,1 g | Casos dentro / 37 |
| --- | ---: |
| 1 % | 6 |
| 2 % | 10 |
| 3 % | 16 |
| 5 % | 22 |
| 7,5 % | 29 |
| 10 % | 32 |
| 15 % | 33 |
| 20 % | 35 |

| Unidad de referencia (tolerancia 5 %) | Casos dentro / 37 |
| --- | ---: |
| 2,00 g | 23 |
| 2,05 g | 24 |
| 2,10 g | 22 |
| 2,15 g | 17 |
| 2,20 g | 11 |

La cuadrícula no sirve para estimar retrospectivamente una nueva unidad
«ganadora». Sin incertidumbres de pesada, identificación de marcas y
selección prospectiva, la fracción de encaje no representa confianza
estadística ni prueba lingüística. La familia de 2,1 g y sus razones
proceden de la bibliografía previa, no de un dato independiente.

Referencia: Martínez Chico y González García (2018), *Florentia
Iliberritana* 29, 381–390.
https://revistaseug.ugr.es/index.php/florentia/article/download/8829/7412/25457

Ejecutar:
```bash
python -m iberos.metrology_sensitivity_05 --json /tmp/metrology_sensitivity_05.json
pytest -q tests/test_metrology_assemblages_04.py tests/test_metrology_sensitivity_05.py
```

No se accede a FULL3406, no se altera GOLD, se mantienen ambos PR
en revisión hasta completar CI.
