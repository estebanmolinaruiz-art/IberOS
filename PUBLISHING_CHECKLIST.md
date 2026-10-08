# IberOS — estado de publicación y lista de verificación

Actualizado: 2026-10-08

## Ya demostrado

### GitHub
- [x] Repositorio público `estebanmolinaruiz-art/IberOS`
- [x] Rama principal `main`
- [x] Tests automatizados
- [x] GitHub Pages
- [x] Releases `v1.0.0` y `v1.0.1`

### PyPI
- [x] Trusted Publishing configurado
- [x] Paquete público `iberos`
- [x] `pip install iberos`
- [x] `skip-existing: true` en el workflow

### Zenodo
- [x] DOI principal `10.5281/zenodo.22939179`
- [x] Integración GitHub activada
- [x] `.zenodo.json`
- [ ] Verificar DOI específico de software de la release actual

### Software Heritage
- [x] Solicitud de archivado ejecutada
- [ ] Recuperar y registrar el SWHID

### Hugging Face
- [x] Repositorio de dataset creado
- [ ] Verificar carga de archivos
- [ ] Verificar licencia CC BY 4.0
- [ ] Verificar Dataset Card
- [ ] Verificar Dataset Viewer

### Web
- [x] GitHub Pages pública
- [x] Corpus y módulos web integrados
- [x] ZIP de fichas PDF preparado
- [ ] Subir fichas PDF y comprobar enlaces

## Consistencia de versión

Antes de cada release:
`tag GitHub = pyproject.toml = CITATION.cff = .zenodo.json`

Versión pública actual: `1.0.1`.
