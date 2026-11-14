# SEMANTIC-EKIAR-CHALLENGE-02 — prueba retrospectiva fuera de cuatro ejemplos

**Evidencia lingüística, no simple infraestructura.** Se toma el patrón
nombre + -te/-de + ekiar/egiar definido en SEMANTIC-EKIAR-01 y se lo
aplica a tres testimonios **publicados en las fuentes consultadas**,
no presentes en las cuatro fichas del ensayo original. No son muestras
ciegas históricas: la bibliografía ya conocía su lectura.

- **F.11.28**: \`iltubokontekiar\`. El módulo reconoce
  \`iltubokon\` + \`te\` + \`kiar/ekiar\` según la segmentación
  normalizada convencional, y solo propone «realización asociada
  a Iltubokon». La identificación de persona está supeditada
  a una lectura original y a la edición del objeto.
- **F.17.7**: \`]balkarte ekiar\`. La secuencia morfológica es
  compatible con una fórmula, pero el nombre está incompleto;
  se registra abstención sobre identidad/rol.
- **Cálato de Ca n'Oliver**: \`adintaŕekiaḿi\`.
  Segmentación propuesta: nombre \`adintaŕ\`, \`ekia\` y \`ḿi\`.
  El sufijo y la morfología no son la fórmula exacta
  \`NP-te ekiar\`; **no** forzar lectura de autoría.
- **Control negativo artificial**: \`likine salir\`
  (NO es inscripción atestiguada); la regla debe abstenerse.

Fuentes:
- Moncunill (2007), *Lèxic d'inscripcions ibèriques*,
  Universitat de Barcelona, pp. 155–157:
  https://diposit.ub.edu/server/api/core/bitstreams/a72f4e19-1499-48ec-aa18-b1801ad11a46/content
- Francès, Velaza y Moncunill, *Un nuevo cálato inscrito de
  Ca n'Oliver*, fotografía y dibujo en la edición:
  https://www.academia.edu/144343400/Un_nuevo_c%C3%A1lato_inscrito_de_Ca_n_Oliver_Cerdanyola_del_Vall%C3%A8s_Barcelona_

**Resultado**: una nueva *aplicación local de IberOS* a un
testimonio publicado, dos abstenciones en testimonios históricamente
publicados, un negativo artificial. No es una nueva traducción
independientemente confirmada, ni una medición de precisión
lingüística. No se han contrastado dos papeles humanos diferentes
por una fuente externa. Evitar declarar éxito ciego.

Código y pruebas:
\`\`\`bash
python -m iberos.semantic_ekiar_challenge_02
pytest -q tests/test_semantic_ekiar_challenge_02.py
\`\`\`
