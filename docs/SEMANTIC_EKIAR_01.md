# SEMANTIC-EKIAR-01 — una lectura funcional ibérica con límites explícitos

**Objetivo:** volver desde los controles metrológicos al desciframiento.
Se contrasta la fórmula escrita **nombre personal + -te + ekiar**
en cuatro soportes heterogéneos, todos ya conocidos en la bibliografía:

| ID | Transcripción citada/normalizada | Soporte |
| -- | -- | -- |
| E.7.1 | likinete ekiar usekerdeku | mosaico de Caminreal |
| C.12.2 | bilo[s]árkertekiar | recipiente de plata |
| A.33.2 | arsakisteekiar | moneda (lecturas alternativas) |
| F.13.3 | ebirteekiar | cerámica pintada de Llíria |

**Interpretación contextual restringida:**
«obra/realización asociada a [nombre]», posiblemente «hecho por» o
«mandado hacer por», SIN determinar si el designado es artesano,
encargante o titular de una magistratura. No se afirma que ekiar sea
inequívocamente verbo: también se ha propuesto que sea nombre de acción.

El mosaico de Caminreal puede glosarse **tentativamente** como:
«obra relacionada con Likine; referencia a Usekerdeku / Osicerda
(interpretación toponímica)». NO se ofrece traducción palabra a
palabra de `usekerdeku`.

Fuentes de contraste:
- Orduña 2010, «En torno al lexema ibérico eki- y sus variantes»:
  https://ifc.dpz.es/recursos/publicaciones/30/23/20orduna.pdf
- Quintanilla, «Palabras de contenido verbal en ibérico»:
  https://ifc.dpz.es/recursos/publicaciones/26/22/21quintanilla.pdf
- Luján 2010, «Las inscripciones musivas ibéricas del valle medio del Ebro»:
  https://ifc.dpz.es/recursos/publicaciones/30/23/18lujan.pdf
- Lowe 2014, «Bilingualism and language contact in Republican Iberia»:
  https://www.epigraphica.it/wp-content/uploads/2025/01/2014-LXXVI_73196005.pdf

**Resultado admisible:** la fórmula se puede reconocer en cuatro
soportes y atribuir un papel general a la persona precedente.
**No es nuevo desciframiento de IberOS**, ni comprobación ciega.
La lectura monetal A.33.2 tiene discrepancias de edición, y las
cuatro frases ya se han interpretado previamente. Una futura prueba
de roles debe bloquear previamente el modelo y examinar objetos
físicos nuevos, con lectura y papel externo independientes.

El programa no consulta FULL3406 ni publica mejoras de precisión
y preserva el CORE oficial. Se trata de una línea SEMÁNTICA, no de
otra variante del modelo de pesos.

```bash
python -m iberos.semantic_ekiar_01 --json /tmp/semantic-ekiar.json
pytest -q tests/test_semantic_ekiar_01.py
```
