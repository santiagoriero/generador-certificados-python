from pathlib import Path
import pandas as pd
from reportlab.pdfgen import canvas

# --- DEFINICIÓN DE RUTAS BASE ---
BASE_DIR = Path(__file__).parent.parent
CARPETA_DATOS = BASE_DIR / "datos" / "alumnos.xlsx"
CARPETA_CERTIFICADOS = BASE_DIR / "certificados"


def asegurar_carpetas():
    """Crea la carpeta 'certificados' automáticamente si no existe."""
    CARPETA_CERTIFICADOS.mkdir(parents=True, exist_ok=True)


def generar_certificado(nombre, curso, fecha, ruta_pdf):
    """Genera la plantilla visual del certificado en PDF."""
    pdf = canvas.Canvas(str(ruta_pdf))

    # Borde y cabecera
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(306, 745, "GP")
    pdf.rect(40, 40, 520, 720)

    # Título principal
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(306, 720, "CERTIFICADO")

    # Subtítulo
    pdf.setFont("Helvetica", 13)
    pdf.drawCentredString(
        306, 680, "Se certifica que el alumno ha completado satisfactoriamente"
    )

    # Nombre del alumno
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(306, 630, nombre)
    pdf.line(180, 610, 430, 610)

    # Detalles del curso y fecha
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(306, 570, f"Curso: {curso}")
    pdf.drawCentredString(306, 535, f"Fecha: {fecha}")

    # Texto descriptivo
    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(306, 480, "Por haber completado satisfactoriamente")
    pdf.drawCentredString(306, 460, "el curso de formación.")

    # Firma
    pdf.line(190, 180, 420, 180)
    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(305, 165, "Firma del responsable")

    pdf.save()


def preparar_datos(alumno):
    """Extrae y da formato a los datos de cada alumno."""
    nombre = alumno["Nombre"]
    curso = alumno["Curso"]

    # Formato de fecha seguro
    if hasattr(alumno["Fecha"], "strftime"):
        fecha = alumno["Fecha"].strftime("%d/%m/%Y")
    else:
        fecha = str(alumno["Fecha"])

    nombre_archivo = nombre.replace(" ", "_")
    ruta_pdf = CARPETA_CERTIFICADOS / f"certificado_{nombre_archivo}.pdf"

    return nombre, curso, fecha, ruta_pdf


# --- FLUJO PRINCIPAL DE EJECUCIÓN ---
if __name__ == "__main__":
    print("====================================")
    print("GENERADOR DE CERTIFICADOS")
    print("====================================\n")

    asegurar_carpetas()

    try:
        datos = pd.read_excel(CARPETA_DATOS)

        for indice, alumno in datos.iterrows():
            try:
                nombre, curso, fecha, ruta_pdf = preparar_datos(alumno)
                generar_certificado(nombre, curso, fecha, ruta_pdf)
                print(f"✅ PDF generado exitosamente para: {nombre}")
            except Exception as e:
                print(
                    f"❌ Error al procesar al alumno en la fila {indice}: {e}"
                )

    except FileNotFoundError:
        print(
            f"⚠️ No se encontró el archivo Excel en la ruta: {CARPETA_DATOS}"
        )