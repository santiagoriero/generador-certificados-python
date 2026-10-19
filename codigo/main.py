from pathlib import Path

import pandas as pd

from config import CARPETA_CERTIFICADOS, CARPETA_DATOS, asegurar_carpetas
from data_loader import leer_excel, preparar_datos, validar_esquema
from pdf_generator import generar_certificado


# --- FLUJO PRINCIPAL DE EJECUCIÓN ---
if __name__ == "__main__":
    print("====================================")
    print("GENERADOR DE CERTIFICADOS")
    print("====================================\n")

    asegurar_carpetas()

    try:
        datos = leer_excel(CARPETA_DATOS)

        # Validar esquema antes de procesar
        validar_esquema(datos)

        for indice, alumno in datos.iterrows():
            try:
                if pd.isna(alumno["Nombre"]) or str(alumno["Nombre"]).strip() == "":
                    print(f"⚠️ Fila {indice} ignorada: Nombre vacío o inválido.")
                    continue

                nombre, curso, fecha, ruta_pdf = preparar_datos(
                    alumno, CARPETA_CERTIFICADOS
                )
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
    except ValueError as ve:
        print(f"❌ {ve}")