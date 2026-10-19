import pandas as pd

from config import CARPETA_DATOS


def leer_excel(ruta_archivo=CARPETA_DATOS):
    """Lee el archivo Excel de alumnos y retorna un DataFrame de pandas."""
    return pd.read_excel(ruta_archivo)


def validar_esquema(df):
    """Valida que el DataFrame contenga las columnas obligatorias y datos mínimos."""
    columnas_requeridas = ["Nombre", "Curso", "Fecha"]
    for col in columnas_requeridas:
        if col not in df.columns:
            raise ValueError(
                f"Error crítico: Falta la columna obligatoria '{col}' en el archivo Excel."
            )
    if df.empty:
        raise ValueError("Error crítico: El archivo Excel no contiene registros.")
    print("✅ Validación de esquema de Excel completada exitosamente.")


def preparar_datos(alumno, carpeta_certificados):
    """Extrae y da formato a los datos de cada alumno."""
    nombre = alumno["Nombre"]
    curso = alumno["Curso"]

    # Formato de fecha seguro
    if hasattr(alumno["Fecha"], "strftime"):
        fecha = alumno["Fecha"].strftime("%d/%m/%Y")
    else:
        fecha = str(alumno["Fecha"])

    nombre_archivo = nombre.replace(" ", "_")
    ruta_pdf = carpeta_certificados / f"certificado_{nombre_archivo}.pdf"

    return nombre, curso, fecha, ruta_pdf