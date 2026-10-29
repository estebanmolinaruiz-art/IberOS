# IberOS Write — regla de inscripción híbrida

## Objetivo confirmado
El usuario introduce letras, palabras o frases en español y Write presenta el resultado **en una piedra con signos ibéricos**.

1. **Léxico documentado:** cuando una equivalencia léxica ibérica está respaldada por fuente y revisión suficiente, representar la palabra ibérica documentada, conservando exactamente su lectura y variante signaria acreditada.
2. **Lo que no esté resuelto:** no dejar la frase muda por abstención global; proponer, **como representación gráfica moderna sin equivalencia histórica demostrada**, una conversión convencional de las letras latinas a los signos ibéricos elegidos en un mapa trazable. Mantener cada tramo como `TRANSLITERACIÓN MODERNA` o `APROXIMACIÓN GRÁFICA`. Nunca confundir esa conversión con una traducción.
3. **Glifos ausentes o ambiguos:** marcar visiblemente el hueco o signo ambiguo, sin inventar su dibujo. No utilizar una letra latina como si fuese glifo antiguo certificado.
4. **Objeto visual:** componer todos los segmentos en una **piedra** con división entre los términos documentados y los convertidos; permitir exportar la imagen SVG/PNG.
5. **Sin bloquear la escritura por una frase no reconocida:** el motor semántico puede abstenerse de traducir; el renderizador gráfico debe seguir dando resultado donde exista una correspondencia signaria verificada.
6. **Rigor científico:** la grafía elegida y la traducción/interpretación son evidencias independientes. Advertencia visible: *recreación gráfica experimental; no inscripción antigua ni traducción validada*.

## Puertas técnicas para implementación
- Fuente gráfica ibérica licenciada o repertorio de glifos trazados desde originales autorizados.
- Tabla de equivalencias carácter latino → valor de signo → glifo específico + variante + fuente + licencia + estado de revisión.
- Palabras ibéricas documentadas vinculadas a edición, contexto, nivel de certeza y repertorio gráfico.
- Tratamiento explícito de oclusivas ibéricas: un signo silábico puede representar CV; no hay conversión carácter-a-carácter universal válida.
- Cobertura incompleta: mantener glifos no disponibles destacados y no sustituirlos por geometrías inventadas.

## Estado real a 2026-10-23
La web dispone de segmentación de valores y un modo semántico limitado. **No está implementada aún la piedra final con signario documentado completo.** Se retiró una visualización de pseudoglifos improvisados porque no cumplía el requisito de autenticidad.

## Especificación funcional cerrada — 2026-10-29

### Comportamiento obligatorio
- **Una sola entrada principal** acepta letras, palabras y frases. Pulsar *Escribir en ibérico* compone una piedra; el análisis semántico es una explicación secundaria y no bloquea la visualización.
- **Palabras ibéricas documentadas:** sustitución solamente cuando haya correspondencia léxica argumentada y registro de fuente, con etiqueta DOCUMENTADA o PROPUESTA y procedencia visible.
- **Resto de palabras:** representación fonográfica moderna usando únicamente valores signarios y variantes registrados; las conversiones deben quedar identificadas como FONOGRÁFICO MODERNO. Si falta un signo, mostrar un hueco marcado; no dibujar una supuesta forma antigua.
- **Inscripción en piedra:** textura mineral irregular y signos con efecto de incisión/cincel (sombra interna e iluminación de arista), de tamaño legible en móvil y PC; evitar apariencia de texto impreso o mosaico.
- **Exportar:** SVG/PNG debe contener la misma inscripción visual vista en pantalla, no solo valores latinos. Incluir metadatos de fuente, reglas, variantes, texto original y advertencias.
- **Reversibilidad:** conservar el texto fuente original y la secuencia exacta de tokens; recuperar el castellano desde esa traza no significa descifrar ibérico histórico.

### Criterios de aceptación (no aprobados hasta comprobar)
| ID | Prueba | Aceptación |
| --- | --- | --- |
| W01 | `iltiŕ` | Piedra con signos gráficos de repertorio y variante trazable, no cuatro letras latinas en recuadros |
| W02 | `Esteban` | Adaptación moderna visible y etiquetada; segmentos no representables indicados |
| W03 | `Esteban vende hierro` | Piedra con salida gráfica aun cuando el análisis lingüístico se abstenga |
| W04 | Frase mixta con léxico con evidencia | Segmentos documentados separados de adaptaciones fonográficas, cada uno con fuente/estado |
| W05 | Pulsar botón en iPhone y PC | Actualiza inscripción y no queda en «Sin signos» tras entrada válida |
| W06 | Descargar SVG y PNG | Inscripción, textura y grabado presentes en ambos archivos |
| W07 | Glifo externo no cargado | Fallo visible y legible; no sustitución por letras disfrazadas de signo histórico |
| W08 | GitHub Actions | Pruebas de navegación, motor y exportación verdes |
| W09 | Verificación humana | Revisión visual de signos representados y apariencia cincelada contra el diseño aprobado |

### Restricciones
No incorporar formas inventadas, glifos de licencia no verificada, ni dar por validadas propuestas semánticas abiertas. Una piedra bonita no sustituye un inventario de signos cotejado. La implementación actual **no ha superado** W01–W09 de forma conjunta.
