# SCI-PRED-06 · Búsqueda de un caso real con dos roles acreditados externamente

**Fecha:** 2026-11-12 · **Prioridad Core:** predicción precomprometida antes de ver gold extralingüístico. **Coste:** 0 €. **Resultado:** NO ELIGIBLE GOLD FOUND; 0 traducciones confirmadas.

## Objetivo que no se puede rebajar

Solo una **nueva pieza física realmente distinta de TRAIN**, con dos participantes inequívocos y sus dos papeles certificados desde evidencia externa que no dependa de analizar el sufijo ibérico, permite probar SCI-PRED-02. La frase «dos nombres presentes» **no** constituye por sí sola «dos papeles contrastados». Los textos griegos con nombres ibéricos son controles históricos, no textos ibéricos sobre los que verificar un morfema ibérico.

## Candidatos reales recuperados y evaluados

| Expediente | Objeto y referencia | Personas | Contexto externo | Resultado |
|---|---|---|---|---|
| #159 | Fundació CIRNE, Museu Soler Blasco (Xàbia), plomo presentado en 2019 y editado en 2022, DOI 10.3989/aespa.095.022.07 | `sakaŕaŕgi` / `uŕkebeŕśe` (dativo `-e` *hipotético*), además de otros | Pieza física verificada por SEM y restauración; **procedencia arqueológica desconocida**; ninguna prueba extralingüística de remitente/destinatario. | **RETROSPECTIVE_ONLY / ROLE_GOLD_MISSING**; la lectura no activa el protocolo `-te` productor/comitente. |
| #160 | **Segunda** lámina de Masies de Sant Miquel (Banyeres), DOI 10.36707/palaeohispanica.v23i0.538, §5 fig. 5 | `edeśigi`, `tigirselgi`, `goroigi`, `tautini` | Procedencia **nivel superficial**, >500 fragmentos tras impacto de excavación; documento reconstituido parcialmente. `tiagu(ke)` no tiene significado/cargo certificado. | **RETROSPECTIVE_ONLY / ROLE_GOLD_MISSING**; no inventar jerarquías. |
| Control distinto | **Primera** lámina de Masies, misma edición §4, fig. 4 | Texto muy corto e incierto | UE-7043, nivel de calle, último cuarto del s. III a. C. | La estratigrafía verificable pertenece a **otra** pieza; no imputar su fecha o ambiente funcional al plomo largo. **NO TWO PERSON ROLES**. |
| Control comparativo | Plomo griego de Pech-Maho, IGF 135 / GEI007; https://www.persee.fr/doc/reg_0035-2039_2022_num_135_1_8733 | Testigos con nombres indígenas/ibéricos y protagonistas de negocio griego | Funciones de testigo/comprador/vendedor en **texto griego** | **OUT_OF_DOMAIN**: no es texto ibérico y no valida `-te`. |
| Control técnico | Plomos de Masies/Castellet, 5 en edición 2023 | No todos contienen dos nombres | Contextos de excavación heterogéneos: superficies y estratos; no crear una sola identidad de pieza | Excluir agregaciones como unidad lingüística. |

## Decisión de investigación (no crear un «acierto» artificial)

- **Xàbia** puede ser útil como material morfológico comparativo para el hipotético `-e`, pero la reconstrucción remitente/destinatario sería un **resultado circular**: es justamente la función del morfema lo que pretendemos verificar.
- **Masies largo** es útil para recuentos de antropónimos y estructuras sin sufijo; ni estrato de calle ni profesiones de participantes están demostrados. Si aparecen fuentes nuevas con roles **externos**, iniciar una prueba **nueva y predeclarada**, jamás reetiquetar como éxito prospectivo el resultado ya visto.
- **Pech-Maho griego** sí contiene roles textuales (testigos de venta) pero no constituye texto ibérico, por lo que podría ser entrenamiento contextual/onomástico, no test semántico del Core.
- Las estampillas K.5.4 siguen etiquetadas retrospectivas. Un texto latino con esclavo/propietario no equivale a verificar dos roles semánticos del mismo mensaje ibérico.

## Acciones de mayor rendimiento, sin duplicar validadores

1. **Localizar primero el gold externo**, sin abrirlo al módulo predictor: inventarios/epígrafes paralelos con dos personas en roles diferenciados probados desde fuentes arqueológicas/latinas independientes y asociados inequívocamente a **una inscripción ibérica** nueva. Registrar la fuente en un canal privado/independiente del predictor antes de ejecutar SCI-PRED-02.
2. Para cada nuevo hallazgo, anotar solo `physical_id`, `source_uri`, tipo de soporte y relaciones de dependencia editorial, comparándolo con FULL3406 y el catálogo. Sin auditoría de novedad, mantener `UNKNOWN`.
3. Exigir dos lecturas ciegas desde imagen original con hash; si una lectura es editorial, marcar D1. No contar dos autores de un mismo artículo como dos lectores ciegos.
4. Tras certificación externa de identidad y papeles, preparar `blind_packet_preview` sin gold; precomprometer SHA+Git commit **antes de desvelar** la evaluación y verificar cronología de forma independiente.
5. Evaluar con `prospective_role_evaluation`, conservar todos los intentos y resultados negativos. El umbral del protocolo SCI-PRED-02 se mantiene congelado, no lo suavizar al faltar muestra.

## Fuentes de acceso libre comprobadas

- Ferrer i Jané et al. (2022), Xàbia CIRNE, *Archivo Español de Arqueología* 95, e07: https://aespa.revistas.csic.es/index.php/aespa/article/view/619
- Ferrer i Jané et al. (2023), Masies/Tivissa, *Palaeohispanica* 23, pp. 311–328: https://www.ifc-ojs.es/index.php/palaeohispanica/es/article/view/538
- Edición abierta de Masies (secciones 4 y 5; identidad estratigráfica de dos plomos separada): https://ifc.dpz.es/recursos/publicaciones/40/18/20FERRER.pdf
- Rodríguez Somolinos (2022), texto griego de Pech-Maho: https://www.persee.fr/doc/reg_0035-2039_2022_num_135_1_8733
- Mnamon SNS, reservas de tipología sobre los plomos ibéricos: https://mnamon.sns.it/index.php?id=13&lang=en&page=Scrittura

## Estado al cierre

- Leads retrospectivos en la cola `sci_pred04_candidate_queue_v1.json`: **7** (incluye #159, #160, ambos explícitamente no elegibles).
- Casos que cumplen protocolo de dos papeles externos sin circularidad: **0**.
- Predicciones selladas sobre caso nuevo: **0**.
- Predicciones semánticas confirmadas: **0**.
- Traducciones validadas: **0**.
- Resultado del motor: **INSUFFICIENT_N / NOT_EVALUATED**.
- CORE oficial, FULL3406 y web **sin modificaciones**.
- Prioridad nueva: **priorizar búsqueda de evidencias independientes, no programación adicional hasta encontrar una pieza apta**.
