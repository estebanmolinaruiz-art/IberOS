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
