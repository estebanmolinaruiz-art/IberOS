# G-112 — Textos y alusiones históricas en GeoRoutes

La nueva función `iberos.route_texts` registra testimonios antiguos, medievales
y modernos que puedan orientar la búsqueda de caminos desaparecidos.

## Principio científico
Una mención de un puerto, un movimiento comercial o una ruta tardía **no**
identifica por sí sola una calzada ni fecha su existencia siglos antes.
Se conservan por separado:
- identidad documental y grupo de dependencia;
- fragmento original, localizador y edición revisada;
- fecha del acontecimiento descrito;
- fecha de composición/copia;
- topónimos normalizados con incertidumbre;
- vinculación directa con el itinerario frente a mera asociación contextual.

La función agrupa menciones dependientes, descarta cronologías incompatibles
y devuelve `textual_route_candidate`, `contextual_hypothesis_only` o
`no_qualified_textual_evidence`; nunca devuelve un trazado geográfico.

## Caso La Picola–La Alcudia: fuentes históricas candidatas

1. **Ptolomeo, Geografía, II, 6, 14**, referencia al *Portus Ilicitanus*
   (siglo II d. C.), según la síntesis oficial de la declaración BIC.
   Es una referencia toponímica romana, **no** un itinerario terrestre del
   siglo V–IV a. C.:
   https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-4134
2. **Itinerario de Antonino** y **Anónimo de Rávena**, fuentes de itinerarios
   romanos y tardíos recogidas en investigación sobre la Via Augusta en Ilici.
   Requieren consulta de pasajes y control de topónimos antes de asignar
   geometrías al entorno de Santa Pola:
   https://rua.ua.es/dspace/bitstream/10045/60677/1/tesis_lorenzo_desanroman.pdf
3. **Catálogo MARQ, Santa Pola. Arqueología y Museo**: ofrece dos soluciones
   interpretativas de comunicaciones romanas y transmite noticia de Escolano
   (siglo XVII) acerca de un camino Real procedente de Cartagena por Catral
   y Hostalete. Son pistas para cartografía histórica, **no** evidencia del
   periodo ibérico temprano:
   https://marqalicante.com/contenido/publicaciones/pub2_87.pdf
4. **Relación territorial ibérica** en la declaración BIC de La Picola:
   conexión propuesta sobre argumentos arqueológicos, no testimonio textual
   primario que describa un camino.
   https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-4134

## Estado
No se ha identificado en estas fuentes un testimonio textual que nombre
inequívocamente un itinerario La Alcudia–La Picola entre 430 y 350 a. C.
Los documentos romanos y del siglo XVII quedan como controles comparativos,
no como datos aptos para desbloquear celdas fechadas de GeoRoutes G-111.

La búsqueda geográfica y documental debe contrastar cualquier topónimo
antiguo con varias localizaciones posibles y falsos positivos (vías modernas,
canales agrícolas y centuriación). No se infieren probabilidades numéricas sin
validación externa. Todo gratuito; sin modificación de las métricas epigráficas.
