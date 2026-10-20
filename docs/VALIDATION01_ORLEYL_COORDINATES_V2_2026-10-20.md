# VALIDATION-01 — Sistema de coordenadas reproducible v2 (2026-10-20)

## Fuente y procedimiento exacto
Fuente: PDF aportado por el usuario, *Materiales de la necrópolis ibérica de Orleyl* (Fletcher et al. 1981), archivo `mupreva194_mupreva153_101.pdf`.

Renderizar **la página 65 y la 111 del PDF**, indexación humana desde 1, con PyMuPDF a **escala 3.0** y guardar PNG RGB. Girar 90 grados **en sentido horario** con Pillow `rotate(270, expand=True)`. La salida mide **2287 × 1727 píxeles** en ambas páginas.

### Bandas de líneas para inspección
Coordenadas absolutas `(x_left, y_top, x_right, y_bottom)` en **esta versión de 2287 × 1727 píxeles**:
- **Orleyl V, figura 22, línea física 3, página PDF 65:** `(80, 490, 2250, 572)`.
- **Orleyl VII, texto B, figura 25, línea física 2, página PDF 111:** `(415, 410, 2015, 475)`.

Las bandas son **aproximadas** y pueden incluir límites de líneas contiguas. No identifican el inicio ni final del vocablo V-19/VII-B-7, ni posiciones individuales de los 17 signos. La lectura editorial sigue siendo:
- V-19: `bi te r o ke te ti n e`.
- VII-B-7: `bi te r o ke ti n e` (más posible `ba s`).
No convertir automáticamente esas cadenas editoriales en «signos cotejados visualmente».

### Corrección de documentación previa
Los informes de recorte de 2026-10-19 utilizaron coordenadas para imágenes a otra resolución, algunas de las cuales resultaron desplazadas. **Quedan invalidadas todas esas coordenadas como localizadores de grafema**. Esta versión identifica exactamente la página, el giro, el tamaño y el marco de referencia. **La meta M06 sigue pendiente** hasta asignar cajas concretas verificadas a cada signo de las secuencias.

### Reproducción
```python
import fitz
from PIL import Image
pdf=fitz.open("mupreva194_mupreva153_101.pdf")
for page,bbox in [(65,(80,490,2250,572)),(111,(415,410,2015,475))]:
    p=pdf[page-1].get_pixmap(matrix=fitz.Matrix(3,3),alpha=False)
    im=Image.frombytes("RGB",[p.width,p.height],p.samples).rotate(270,expand=True)
    assert im.size==(2287,1727)
    im.crop(bbox).save(f"orleyl_{page}_line_v2.png")
```

### Veredicto de auditoría
- PDF original disponible: SÍ.
- Figura correcta, renglón físico identificado: SÍ.
- Recorte reproducible con marco inequívoco: SÍ.
- Delimitación gráfica de los 17 signos: NO.
- Revisión independiente: NO.
- Lecturas HOLD: 0.
- Preparación VALIDATION-01: **30/100**; ciencia: `NOT_EVALUATED`.
