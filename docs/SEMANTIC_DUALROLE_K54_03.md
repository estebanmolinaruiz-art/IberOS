# SEMANTIC-DUALROLE-K54-03 — el primer contraste de dos papeles documentados externamente

**14-11-2026. Calibración histórica NO ciega.** Dos morteros llevan
las mismas dos estampillas, una en latín y otra en ibérico:

- **La Caridad, Caminreal** y **La Corona, Fuentes de Ebro**.
- Latín: \`Fl(accus) · Atili · L(uci) · s(ervus)\`:
  **Flaccus, esclavo de Lucius Atilius**. Dos papeles distintos,
  sintácticamente explícitos en latín.
- Ibérico: \`bilakeaiunatin / en · abiner\` (MLH K.5.4,
  E.15.1; ediciones variables).

Se han propuesto **tres alternativas**:
H1: \`bilake\` corresponde a Flaccus; \`aiunatin\` a Atilius
y \`abiner\` a *servus*.
H2: \`bilake\` y \`aiunatin\` representan los nombres,
pero \`abiner\` es otro nombre, cognomen o elemento de la
fórmula personal.
H3: equivalencia de finalidad/firma, no traducción literal
entre ambos textos. **No hay consenso y no es válido etiquetar
H1 como gold científico.**

La investigadora M. J. Estarán Tolosa (2012), al estudiar K.5.4,
defiende una correspondencia funcional y la interpretación de
\`abiner\` como parte del nombre, mientras que otros autores lo
comparan con *servus*. La correspondencia \`bilake=Flaccus\` es
plausible, no certificada como lectura única. Las dos
apariciones son físicamente distintas pero repiten el mismo
texto: no constituyen dos pruebas lingüísticas independientes.

Fuentes cotejables:
- Estarán Tolosa (2012), *Las estampillas ibérico-latinas K.5.4*,
  Palaeohispanica 12, pp. 73–90:
  https://ifc-ojs.es/index.php/palaeohispanica/es/article/download/66/48/266
- Luján (2009), *Notas sobre algunas inscripciones paleohispánicas*:
  https://ifc.dpz.es/recursos/publicaciones/29/54/_ebook.pdf
- Moncunill (2007), entrada \`bilakeaiunatinen\`:
  https://diposit.ub.edu/server/api/core/bitstreams/a72f4e19-1499-48ec-aa18-b1801ad11a46/content
- Estarán, Moncunill et al., *Bilingualism and language contact in Republican Iberia*,
  reproducciones y discusión de morteros.

**Resultado de IberOS**: dos roles latinos con respaldo externo y
tres alineaciones ibéricas explícitas, sin decidir cuál es cierta.
No se proclaman valores nuevos de \`-en\` ni \`abiner\`.
La próxima falsación exige un **objeto nuevo**, lectura ibérica fijada
antes de consultar la etiqueta latina o arqueológica y evaluación
por tercero, sin reutilizar el mismo sello K.5.4.

\`\`\`bash
python -m iberos.semantic_dualrole_k54_03
pytest -q tests/test_semantic_dualrole_k54_03.py
\`\`\`

Conserva FULL3406, sus splits y métricas. Sin coste.


## Control externo especialmente discriminante: Isona (IRC V 11)

En un **objeto distinto** de Isona (Aeso) se publicó el grafito en
letras latinas \`Fulvius / Abiner(icus)\`. Aquí \`Abiner\` desempeña
función de **nombre personal** (posiblemente cognomen de liberto).
Moncunill y Velaza (*Abiner, Abinericus…*, SEBarc IX, 2011,
pp. 59-62) consideran por ello mucho más verosímil que \`abiner\`
de K.5.4 sea también un antropónimo. Esta evidencia **favorece
H2 frente a H1**, siempre bajo la premisa no demostrada de que el
segmento ibérico y el antropónimo latino representan la misma
unidad léxica. No demuestra que nunca haya existido una palabra
homónima equivalente a \`servus\`, ni que el ibérico sea traducción
literal del sello latino.

Fuente en repositorio académico de UB:
https://diposit.ub.edu/server/api/core/bitstreams/86761942-5b83-4cd1-93d9-546ba0dde2d4/content

**Observación falsable:** en nuevas inscripciones con \`abiner\`,
si aparece autónomamente como parte de un nombre en otros soportes,
la hipótesis antroponímica gana consistencia; si la distribución es
exclusivamente relacional y equivalente a \`servus\` en bilingües
independientes, ganaría la lectura léxica de servidumbre.
El grafito de Isona es conocido y nunca debe marcarse como
resultado ciego nuevo de IberOS.
