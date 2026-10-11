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
- [x] Wheel `iberos-1.0.1-py3-none-any.whl` publicado
- [x] Sdist `iberos-1.0.1.tar.gz` publicado
- [x] Workflow de publicación completado correctamente (run #6)
- [ ] Ejecutar una prueba de instalación desde PyPI en un entorno externo independiente
- [ ] Verificar CLI en ese entorno: `iberos --help`

## Zenodo
- [x] Informe técnico: DOI de versión `10.5281/zenodo.22939179`
- [x] Informe técnico: DOI conceptual `10.5281/zenodo.22939178`
- [x] `.zenodo.json` preparado para software v1.0.1
- [ ] Verificar DOI específico de la release de software v1.0.1
- [x] Mantener explícita la separación entre DOI del informe y DOI del software

## Software Heritage
- [x] Workflow de solicitud de archivado
- [ ] Recuperar y registrar SWHID verificable

## Hugging Face
- [x] Repositorio de dataset creado
- [ ] Verificar carga de archivos
- [ ] Verificar licencia CC BY 4.0
- [ ] Verificar Dataset Card
- [ ] Verificar Dataset Viewer

## Web
- [x] GitHub Pages habilitada
- [x] Corpus y módulos web integrados en el repositorio
- [x] ZIP de fichas PDF preparado
- [ ] Comprobar desde una sesión externa que la portada pública carga correctamente
- [ ] Comprobar navegación a metodología, software, documentación, research y contacto
- [ ] Subir fichas PDF y comprobar todos sus enlaces
- [ ] Sólo entonces marcar “sitio web dedicado estable” como cumplido para EpiHub

## Benchmark y marco académico
- [x] 38 objetos curados declarados y almacenados
- [x] Separación explícita EVIDENCE / INFERENCE / HYPOTHESIS / ESTIMATED TRANSLATION
- [ ] Publicar protocolo de benchmark reproducible
- [ ] Publicar métricas/resultados y casos negativos
- [ ] Publicar documento metodológico autónomo y citable

## Consistencia de versión

`GitHub v1.0.1 = pyproject.toml 1.0.1 = CITATION.cff 1.0.1 = .zenodo.json 1.0.1 = PyPI 1.0.1`

La cadena de versión técnica está alineada. Queda pendiente el DOI específico de software y la prueba externa independiente de instalación.
