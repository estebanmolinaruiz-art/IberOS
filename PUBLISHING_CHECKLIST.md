# IberOS — estado de publicación y lista de verificación

Actualizado: 2026-10-11

## GitHub
- [x] Repositorio público `estebanmolinaruiz-art/IberOS`
- [x] Rama principal `main`
- [x] Tests automatizados
- [x] GitHub Pages habilitada
- [x] Releases `v1.0.0` y `v1.0.1`
- [x] Licencia Apache-2.0
- [x] CITATION.cff y .zenodo.json coherentes con v1.0.1

## PyPI
- [x] Paquete público `iberos`
- [x] Trusted Publishing mediante GitHub Actions
- [x] `iberos==1.0.1` publicado y verificado en la API pública de PyPI
- [x] Wheel y sdist de 1.0.1 publicados
- [x] Workflow de publicación completado correctamente
- [ ] Ejecutar una prueba de instalación desde PyPI en un entorno externo independiente
- [ ] Verificar CLI en ese entorno: `iberos --help`

## Zenodo — informe técnico
- [x] DOI de versión: `10.5281/zenodo.22939179`
- [x] DOI conceptual: `10.5281/zenodo.22939178`
- [x] Tipo verificado: Report
- [x] Publicado: 2026-09-24

## Zenodo — Case Studies I
- [x] DOI de versión: `10.5281/zenodo.22957236`
- [x] DOI conceptual: `10.5281/zenodo.22957235`
- [x] Tipo verificado: Data paper
- [x] Publicado: 2026-09-25
- [x] Relacionado explícitamente con el informe técnico

## Zenodo — software
- [x] `.zenodo.json` preparado para IberOS Open Research Kit v1.0.1
- [ ] No se ha verificado un registro Zenodo público específico para el software v1.0.1
- [ ] Obtener y registrar DOI de versión del software
- [ ] Obtener y registrar DOI conceptual del software
- [x] No confundir DOI del informe o Case Studies con DOI del software

## Software Heritage
- [x] Workflow de solicitud de archivado
- [ ] Recuperar y registrar SWHID verificable

## Web
- [x] GitHub Pages habilitada
- [x] Corpus y módulos web integrados en el repositorio
- [ ] Comprobar desde una sesión externa que la portada pública carga correctamente
- [ ] Comprobar navegación a metodología, software, documentación, research y contacto
- [ ] Sólo entonces marcar “sitio web dedicado estable” como cumplido para EpiHub

## Benchmark y marco académico
- [x] Informe técnico citable en Zenodo
- [x] Case Studies I citable en Zenodo
- [x] 38 objetos curados declarados y almacenados
- [x] Separación EVIDENCE / INFERENCE / HYPOTHESIS / ESTIMATED TRANSLATION
- [ ] Publicar protocolo de benchmark reproducible
- [ ] Publicar métricas/resultados y casos negativos

## Consistencia de versión

`GitHub v1.0.1 = pyproject.toml 1.0.1 = CITATION.cff 1.0.1 = .zenodo.json 1.0.1 = PyPI 1.0.1`

La cadena técnica está alineada. El bloqueo Zenodo restante es crear/verificar el registro específico de **software**.
