from reportlab.pdfgen import canvas


def ajustar_texto_a_ancho(pdf, texto, fuente, tamaño_inicial, ancho_maximo):
    """Reduce el tamaño de fuente progresivamente mientras el texto exceda
    el ancho máximo permitido, evitando desbordamientos en el canvas."""
    tamaño = tamaño_inicial
    pdf.setFont(fuente, tamaño)
    ancho_texto = pdf.stringWidth(texto, fuente, tamaño)
    while ancho_texto > ancho_maximo and tamaño > 10:
        tamaño -= 1
        pdf.setFont(fuente, tamaño)
        ancho_texto = pdf.stringWidth(texto, fuente, tamaño)
    return fuente, tamaño


def generar_certificado(nombre, curso, fecha, ruta_pdf):
    """Genera la plantilla visual del certificado en PDF con diseño profesional
    y ajuste dinámico de fuentes para evitar desbordamientos de texto."""
    pdf = canvas.Canvas(str(ruta_pdf), pagesize=(612, 792))  # Tamaño carta

    # Constantes de diseño
    MARGEN = 50
    ANCHO_CERT = 612 - 2 * MARGEN          # 512 puntos de ancho útil
    CENTRO_X = 306
    LIMITE_TEXTO = ANCHO_CERT - 70         # Límite seguro para texto centrado

    # Borde exterior con grosor profesional
    pdf.setLineWidth(3)
    pdf.setStrokeColorRGB(0.18, 0.18, 0.25)
    pdf.rect(MARGEN, 40, ANCHO_CERT, 712)

    # Borde interior decorativo
    pdf.setLineWidth(0.8)
    pdf.setStrokeColorRGB(0.5, 0.5, 0.6)
    pdf.rect(MARGEN + 14, 54, ANCHO_CERT - 28, 684)

    # Cabecera / logotipo
    pdf.setFont("Helvetica-Bold", 20)
    pdf.setFillColorRGB(0.18, 0.18, 0.25)
    pdf.drawCentredString(CENTRO_X, 738, "GP")

    # Línea decorativa bajo cabecera
    pdf.setLineWidth(1.2)
    pdf.line(CENTRO_X - 90, 723, CENTRO_X + 90, 723)

    # Título principal
    pdf.setFont("Helvetica-Bold", 28)
    pdf.setFillColorRGB(0.1, 0.1, 0.15)
    pdf.drawCentredString(CENTRO_X, 688, "CERTIFICADO")

    # Subtítulo
    pdf.setFont("Helvetica-Oblique", 13.5)
    pdf.setFillColorRGB(0.38, 0.38, 0.44)
    pdf.drawCentredString(
        CENTRO_X, 648,
        "Se certifica que el alumno ha completado satisfactoriamente"
    )

    # Nombre del alumno con ajuste dinámico de fuente
    pdf.setFillColorRGB(0.1, 0.1, 0.15)
    fuente_nombre, tamaño_nombre = ajustar_texto_a_ancho(
        pdf, nombre, "Helvetica-Bold", 24, LIMITE_TEXTO
    )
    pdf.setFont(fuente_nombre, tamaño_nombre)
    pdf.drawCentredString(CENTRO_X, 580, nombre)
    pdf.setLineWidth(1.6)
    pdf.setStrokeColorRGB(0.18, 0.18, 0.25)
    pdf.line(CENTRO_X - 140, 560, CENTRO_X + 140, 560)

    # Detalles del curso y fecha (curso con ajuste dinámico)
    pdf.setFont("Helvetica", 13)
    pdf.setFillColorRGB(0.28, 0.28, 0.34)
    fuente_curso, tamaño_curso = ajustar_texto_a_ancho(
        pdf, f"Curso: {curso}", "Helvetica", 13, LIMITE_TEXTO
    )
    pdf.setFont(fuente_curso, tamaño_curso)
    pdf.drawCentredString(CENTRO_X, 515, f"Curso: {curso}")
    pdf.drawCentredString(CENTRO_X, 480, f"Fecha: {fecha}")

    # Texto descriptivo
    pdf.setFont("Helvetica", 11.5)
    pdf.setFillColorRGB(0.4, 0.4, 0.46)
    pdf.drawCentredString(CENTRO_X, 425, "Por haber completado satisfactoriamente")
    pdf.drawCentredString(CENTRO_X, 405, "el curso de formación.")

    # Firma
    pdf.setLineWidth(1.4)
    pdf.setStrokeColorRGB(0.18, 0.18, 0.25)
    pdf.line(CENTRO_X - 120, 210, CENTRO_X + 120, 210)
    pdf.setFont("Helvetica-Oblique", 11.5)
    pdf.setFillColorRGB(0.32, 0.32, 0.38)
    pdf.drawCentredString(CENTRO_X, 195, "Firma del responsable")

    pdf.save()