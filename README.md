# 🎓 Generador Automático de Certificados en Python

Este proyecto es un automatizador desarrollado en Python que lee datos de alumnos desde una planilla de Excel (`pandas`) y genera certificados individuales e imprimibles en formato PDF de manera automática mediante la librería `reportlab`.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.14+
* **Procesamiento de Datos:** `pandas` / `openpyxl`
* **Generación de Documentos:** `reportlab`
* **Manejo de Rutas:** `pathlib`

---

## 📁 Estructura del Proyecto

```text
generador-certificados-python/
│
├── codigo/
│   └── main.py              # Script principal del sistema
├── datos/
│   └── alumnos.xlsx         # Base de datos de alumnos (Excel)
├── certificados/            # Carpeta generada automáticamente con los PDFs
└── README.md                # Documentación del proyecto

---

## 🚀 Características Principales

* **Automatización total:** Genera certificados de forma masiva en segundos a partir de una planilla de Excel.
* **Creación dinámica de carpetas:** Verifica y genera la estructura de directorios necesaria automáticamente.
* **Manejo robusto de errores:** Si un registro contiene un fallo, notifica la falla y continúa procesando los demás certificados.
* **Formateo inteligente:** Limpia caracteres especiales en los nombres y estandariza las fechas para evitar fallos de guardado.

---

## ⚙️ Cómo Ejecutar el Proyecto

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU-USUARIO/generador-certificados-python.git](https://github.com/TU-USUARIO/generador-certificados-python.git)
   cd generador-certificados-python