# IberOS — estado de publicación y lista de verificación

Actualizado: 2026-10-11

## GitHub
- [x] Repositorio público `estebanmolinaruiz-art/IberOS`
- [x] Rama principal `main`
- [x] Tests automatizados
- [x] GitHub Pages habilitada
- [x] Releases `v1.0.0` y `v1.0.1`
- [x] Licencia Apache-2.0
- [x] CITATION.cff coherente con v1.0.1 y DOI de software

## PyPI
- [x] Paquete público `iberos`
- [x] Trusted Publishing mediante GitHub Actions
- [x] `iberos==1.0.1` publicado
- [x] Wheel y sdist de 1.0.1 publicados
- [x] Workflow de publicación completado correctamente
- [x] Instalación limpia desde PyPI verificada en GitHub Actions run `38158352028`
- [x] CLI `iberos --help` verificada correctamente en ese entorno

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
- [x] Relacionado con el informe técnico

## Zenodo — software
- [x] Registro de software IberOS Open Research Kit v1.0.1 publicado
- [x] DOI de versión registrado: `10.5281/zenodo.22997623`
- [x] Recurso separado del informe técnico y de Case Studies I
- [ ] Verificar y registrar el DOI conceptual del software cuando Zenodo lo exponga públicamente

## Software Heritage
- [x] Workflow de solicitud de archivado
- [ ] Recuperar y registrar SWHID verificable

## Web
- [x] GitHub Pages habilitada
- [x] Corpus y módulos web integrados en el repositorio
- [x] Portada pública comprobada desde una sesión externa
- [x] Navegación pública comprobada: corpus, atlas, fichas, laboratorio, 3D, recursos, casos, comunidad, contactar y acerca
- [x] Sitio web público estable marcado como cumplido para EpiHub

## Documentación técnica
- [x] Mapa canónico de arquitectura publicado en `docs/ARCHITECTURE.md`
- [x] Arquitectura, datos, CLI, benchmark, workflows, publicación y límites enlazados desde una entrada única

## Benchmark y marco académico
- [x] Informe técnico citable en Zenodo
- [x] Case Studies I citable en Zenodo
- [x] Software v1.0.1 con DOI propio
- [x] 38 objetos curados declarados y almacenados
- [x] Separación EVIDENCE / INFERENCE / HYPOTHESIS / ESTIMATED TRANSLATION
- [x] Protocolo de benchmark reproducible publicado en `docs/BENCHMARK.md`
- [x] Snapshot machine-readable, métricas, gates abiertos y casos negativos publicados; GitHub Actions run `38158963423` verificado con éxito

## Consistencia de versión

`GitHub v1.0.1 = pyproject.toml 1.0.1 = CITATION.cff 1.0.1 = PyPI 1.0.1 = Zenodo software v1.0.1`

El bloqueo Zenodo de DOI específico de software y la prueba externa de instalación/CLI quedan cerrados. El benchmark reproducible queda cerrado. Permanece como mejora de archivo duradero recuperar el SWHID verificable.
