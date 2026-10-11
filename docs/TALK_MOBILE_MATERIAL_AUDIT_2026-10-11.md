# Comprobación material de Talk y Mobile

11 de octubre de 2026. Autoridad conservada: C594+C474+C539+C541.

## Paquetes de Talk comprobados

Se han inspeccionado y ejecutado los controles de los paquetes originales
IberOS-TALK-SONO-v0.2.zip e IberOS-TALK-WEB-v0.1.zip, sin modificarlos ni
promover sus contenidos al núcleo científico.

| Comprobación | Resultado |
|---|---|
| SQLite y claves foráneas de SONO v0.2 | Correctas |
| Muestras independientes WAV y MP3 con hashes verificados | 12 pares |
| Vista available_whole_words de producción | 0 entradas |
| SETEBANE | BLOCKED; el resolver conserva fallback |
| Control del resolver con SETEBANE TE EKIAR MI | Todos fallback |
| Manifest del paquete web | 31 archivos; ningún hash discrepante |
| Entradas del lexicón web | 13; ninguna explícitamente aprobada |
| Pronunciación histórica validada por esta revisión | Ninguna |

Hashes SHA256 de los ZIP inspeccionados:

- SONO v0.2: fea211e367ccd267cbbab2dd12bbaa4c7ed0c4ea626eff0d3a088054b052b605
- WEB v0.1: 8fe7dc5f83107cffe54faa77c78984962aff6a11859d7a6cb5da0f188723a79d

El inventario documental no es un volcado del FULL3406. El snapshot C594
de SONO es metadata de autoridad documental; no acredita por sí mismo la
revalidación de cada lectura o de su pronunciación. La prueba técnica no
equivale a aprobación lingüística ni a valoración perceptiva de la voz.

## Discrepancia y corrección de la página pública

validation.json del paquete WEB v0.1 declara whole_word_ready=12. El lexicón
mantiene esas formas como CANDIDATE, explicitly_approved=false y con demos
pendientes. Esa etiqueta no puede interpretarse como 12 assets de producción
READY: el control estricto de SONO conserva cero entradas disponibles.
Los paquetes antiguos permanecen como fuentes históricas de esta auditoría.

La página pública previa utilizaba una lista de 12 formas y síntesis del
navegador. No estaba conectada al SQLite ni a los WAV/MP3 de esos paquetes.
Su tokenizador eliminaba signos y podía dividir BI-D(E/I)-ŔOK-(AN) en
fragmentos que luego recibían voz. También reproducía formas desconocidas
al pulsar la secuencia completa.

TALK-WEB v0.2-guarded separa ahora reconocimiento escrito, demostración
sintética y disponibilidad de producción. Conserva tokens exactos y no
neutraliza R/Ŕ o S/Ś. Los marcadores de Write, los huecos, SETEBANE y las
formas desconocidas impiden la reproducción automática de toda la secuencia.
Las 12 formas de la lista pública admiten únicamente una demostración
provisional con la voz del navegador; ninguna obtiene aprobación de
producción, categoría gramatical resuelta ni validación de fonética histórica.

El adaptador público sigue separado del banco sonoro. No se activan los
audios PENDING ni se declara un fallback fonosilábico validado.

## Mobile y tesis

Las búsquedas realizadas no han resuelto un paquete Mobile. En el árbol
GitHub inspeccionado no se ha identificado APK, IPA, manifest de instalación,
service worker o proyecto nativo Mobile. La web adaptable a pantallas pequeñas
no certifica una compilación Android o iPhone. Mobile conserva PENDIENTE DE
COMPROBACIÓN MATERIAL; esta revisión no establece que no exista otro paquete.

Esta auditoría y el complemento metodológico se incorporan al repositorio.
La incorporación a la tesis definitiva sigue pendiente de identificar y
comparar su archivo autoritativo. Los resultados y métricas congelados no
cambian.

## Validación del adaptador

59 pruebas Python y 35 pruebas Node pasan localmente. De estas últimas,
24 corresponden a Write y 11 a Talk, incluido el control de la salida Write
hacia Talk. El snapshot del benchmark es idéntico al JSON versionado.
Son pruebas del software; no constituyen evidencia lingüística independiente.
