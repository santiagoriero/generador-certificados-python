from pathlib import Path

# --- DEFINICIÓN DE RUTAS BASE ---
BASE_DIR = Path(__file__).parent.parent
CARPETA_DATOS = BASE_DIR / "datos" / "alumnos.xlsx"
CARPETA_CERTIFICADOS = BASE_DIR / "certificados"


def asegurar_carpetas():
    """Crea la carpeta 'certificados' automáticamente si no existe."""
    CARPETA_CERTIFICADOS.mkdir(parents=True, exist_ok=True)