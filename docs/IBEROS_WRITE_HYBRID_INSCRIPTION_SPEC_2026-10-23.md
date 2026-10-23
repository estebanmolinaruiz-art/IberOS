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
