# Migración de IberOS a iberos-ia.com — 2026-11-12

## Política invariable
- **0 € de coste adicional**: GitHub Pages (repositorio público), HTTPS sin cargo y DNS del dominio ya registrado. No activar servicios de pago ni contratar hosting.
- **No tocar el sitio principal hasta pasar controles**. Respaldar código, recursos, rutas y datos antes del cambio.
- Rama inmutable de referencia inicial: `backup/pre-iberos-ia-2026-11-12` (fotografía de `main` al crearla; no es un alojamiento web independiente).
- Migración en `migration/iberos-ia-2026-11-12`; no fusionar sin comprobar DNS y tener un sitio de respaldo *publicado* independiente.

## Hallazgos comprobados
- Repositorio público: `estebanmolinaruiz-art/IberOS`.
- Web estática publicada por `.github/workflows/pages.yml`, carpeta `site/`.
- Destino actual de enlaces, canónicos y comprobación de despliegue: `https://estebanmolinaruiz-art.github.io/IberOS/`.
- `site/index.html` contiene URLs absolutas en canonical, hreflang, OpenGraph y JSON-LD.
- La publicación actual requiere disparador explícito y ejecuta validaciones CORE, integración, sitemap y rutas.
- Dominio nuevo visible como activo en captura de DonDominio. La captura NO comprueba registros DNS.

## Secuencia de migración sin pérdida
1. Inventariar todas las rutas, enlaces internos y externos, JS, CSS, JSON, imágenes, modelos 3D, widgets, buscador y Contactar; identificar referencias absolutas del hosting anterior y rutas bajo `/IberOS/`.
2. Crear **sitio de seguridad publicado de forma independiente** (no basta un branch). Conserva el sitio previo si cuenta con hospedaje propio; de lo contrario, publicar copia estática separada mediante otro proyecto gratuito.
3. Preparar versión bajo `site/`: todas las URLs públicas, `canonical`, `hreflang`, `og:url`, JSON-LD, `sitemap.xml`, `robots.txt`, manifiestos y enlaces de navegación al nuevo dominio. No cambiar DOI ni rutas externas de repositorios.
4. Actualizar `pages.yml` para verificar `https://iberos-ia.com` solo **después** de tener SSL/DNS operativo; evitar la comprobación hardcodeada del URL anterior. Mantener comprobaciones CORE y de integración.
5. En Settings → Pages del repositorio, dar de alta `iberos-ia.com` como custom domain **antes** de apuntar DNS. Verificar propiedad del dominio en GitHub.
6. En DonDominio, configurar los registros A del dominio apex que GitHub documenta oficialmente y CNAME `www` hacia `estebanmolinaruiz-art.github.io` si se desea el subdominio; **respetar MX, SPF, DKIM, DMARC y otros registros no web**. No cambiar nameservers ni borrar DNS del correo por defecto.
7. Comprobar HTTPS, `www`, búsqueda, menús, fichas, Corpus, Laboratorio, Atlas, 3D, Recursos, News, SEO y enlaces internos/externos en escritorio y móvil. Para enlaces viejos, definir estrategia de redirección sin destruir el respaldo.
8. Publicar una sola tanda consolidada después de tests exitosos, revisar despliegue final y decidir actualización de Search Console y enlaces de difusión.

## Riesgo importante
GitHub Pages redirige el dominio predeterminado `github.io` al dominio personalizado; por tanto, **la antigua URL github.io no debe considerarse una copia pública independiente** tras asociarle `iberos-ia.com`. Es obligatorio establecer un respaldo publicado por separado si esa es la única URL antigua.

## Estado
Preparación abierta. Sin activación de DNS, sin nuevo alojamiento facturado y sin cambio en la web pública.

## Zona DNS comprobada visualmente (12 de noviembre de 2026)

DonDominio, pestaña `Parking & Zona DNS`: dominio activo, registros autoritativos en `ns1.dondominio.com` y `ns2.dondominio.com`.

| Host | Tipo | Estado actual | Cambio previsto tras activar Pages |
| --- | --- | --- | --- |
| `iberos-ia.com` | ANAME | `parkingsrv0.dondominio.com` | **Editar** destino a `estebanmolinaruiz-art.github.io` (sin `https://` ni `/IberOS`) |
| `www.iberos-ia.com` | CNAME | `parkingsrv0.dondominio.com` | **Editar** destino a `estebanmolinaruiz-art.github.io` |
| `*.iberos-ia.com` | CNAME | `parkingsrv0.dondominio.com` | Retirar después de verificar que no cubre servicios necesarios; GitHub recomienda evitar comodines por riesgo de takeover |
| `iberos-ia.com` | TXT | registro SPF | **No modificar** |
| `imap`, `mail`, `pop`, `pop3`, `smtp`, `webmail`, `ftp`, `bbdd` | CNAME | registros auxiliares DonDominio | **No modificar** para esta migración |

GitHub admite un solo ANAME de raíz en lugar de cuatro registros A. No mezclar ANAME con registros A de la misma raíz. El DNS de correo y otros servicios deben conservarse aunque no se vean registros MX en la captura.

**Orden de seguridad:** respaldo público independiente → configuración `Settings > Pages > Custom domain` en GitHub → modificación de ANAME y CNAME en DonDominio → verificación SSL + navegación y datos → actualizar SEO y fuentes externas.

**Advertencia sobre GitHub Actions:** `site/CNAME` no configura el dominio, ya que la publicación se realiza con `actions/deploy-pages`. Se requiere el ajuste explícito en el repositorio (o API).

## Cambios preparados (solo rama/PR, no producción)
- `scripts/prepare_custom_domain.py` transforma URLs absolutas del sitio durante la generación del artefacto.
- `tests/test_prepare_custom_domain.py` preserva enlaces externos y archivos binarios.
- `.github/workflows/pages.yml` ejecuta transformación y comprobación, y apunta la prueba del despliegue al nuevo dominio.
- La PR continúa en borrador, sin fusionar ni publicar ni tocar DNS.
