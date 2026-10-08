# IberOS — Registros públicos y fuentes de la tesis
Fecha de comprobación: 2026-10-08.

## Publicación e identidad
- Autor: Esteban Molina Ruiz.
- Informe: *IberOS: marco experimental para el análisis interno y la validación reproducible de inscripciones ibéricas*.
- Zenodo: https://zenodo.org/records/22939179
- DOI de esta versión del informe: 10.5281/zenodo.22939179.
- DOI de concepto (familia de versiones): 10.5281/zenodo.22939178.
- Fecha pública del informe: 2026-09-24; tipo Report; licencia CC BY 4.0.
- El archivo público se denomina IberOS_Informe_Tecnico_v1.0.pdf. No se presupone idéntico al informe local con estructura de tesis del 23-09-2026.
- Software: https://github.com/estebanmolinaruiz-art/IberOS
- Releases verificadas mediante API pública: v1.0.0 y v1.0.1, publicadas el 01-10-2026.
- PyPI: https://pypi.org/project/iberos/ ; API pública indica 1.0.0 como última versión y única release.
- GitHub y PyPI presentan una discrepancia real de versión. No declarar publicado 1.0.1 en PyPI.
- CITATION.cff distingue el programa Apache-2.0 del informe relacionado CC BY 4.0; el DOI del informe no identifica una release del programa.
- .zenodo.json ya registra correctamente el informe como isSupplementTo; este archivo es configuración del repositorio, no prueba de una actualización del registro remoto.

## Fuentes bibliográficas añadidas
1. Martínez-Fernández, G.; Quesada-Moreno, J. F.; Riscos-Núñez, A.; Salguero-Lamillar, F. J. (2026). *Curation of a Palaeohispanic Dataset for Machine Learning*. arXiv:2604.13070v1. https://arxiv.org/html/2604.13070v1
   - El artículo declara 1751 instancias y 36 columnas de características, a partir de datos epigráficos de Hesperia.
   - Incluye registros FALSA/SUSPICIOUS: deben excluirse de validaciones ordinarias.
   - Scripts y CSV declarados por los autores: https://github.com/gonmarfer2/palaeohispanic-dataset-generator
   - Es fuente externa derivada; sus registros no son automáticamente objetos nuevos ni pruebas independientes de IberOS.
2. Ferrer i Jané, J. (2024). “Una nova mirada al plom ibèric Villares V (Kelin, Caudete de las Fuentes). Un text comptable amb deu transaccions”. *Elea* 21, 309–360.
   - Texto del autor consultado: https://www.academia.edu/106078209/Una_nova_mirada_al_plom_ib%C3%A8ric_Villares_V_Kelin_Caudete_de_las_Fuentes_Un_text_comptable_amb_deu_transaccions
   - Fuente para contrastar lecturas y estructura contable; no validación ciega retrospectiva de reglas construidas con esta pieza.
3. Folch, D. *Corpus Ibèrika*. https://cathalaunia.org/Iberika/Iberika
   - Portada consultada: 7122 entradas, 4402 numismáticas, 5368 grupos, máximo 4964 objetos.
   - Mantener ENTRY, GROUP y PHYS_ID separados y controlar TYPE_ID/DIE_ID en monedas.
   - Consulta y enlace bibliográfico no equivalen a autorización de redistribución masiva.

## Autoridad y límites
El registro docs/GITHUB_SYNC_2026-10-08.md mantiene C594 (release semántica), C474 (prospective lock), C539 (suelo técnico) y C541 (red ŔOK).
Esta actualización documental no cambia CORE, métricas, lecturas ni conclusiones científicas.
Fuentes externas: evidencia → candidato → prueba IberOS → control adversarial → adopción o rechazo.

## Pendientes
- Publicar y comprobar la siguiente versión del programa en PyPI mediante el flujo de publicación autorizado, después de los controles de release.
- El acceso de escritura a Zenodo no está disponible en esta sesión; no se ha creado una versión nueva del informe allí.
- No se han verificado hoy Software Heritage, Hugging Face ni todas las fichas individuales: no elevarlos a estado comprobado.
- Requisitos editoriales actuales de Palaeohispanica y estado de la consulta personal: pendientes de comprobación; no se infiere respuesta por la existencia de una página pública.

## Evidencia de comprobación
Metadatos consultados: https://zenodo.org/api/records/22939179 ; https://pypi.org/pypi/iberos/json ; https://api.github.com/repos/estebanmolinaruiz-art/IberOS/releases .
