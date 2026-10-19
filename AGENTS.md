# AGENTS.md - Directrices para el Agente (Generador de Certificados)

Este archivo define las reglas y el flujo de trabajo guiado por agentes para el proyecto **generador-certificados-python**.

## 🎯 Objetivo del Proyecto
Automatizar, depurar y robustecer la generación masiva de certificados individuales en formato PDF a partir de una planilla de datos en Excel utilizando Python (`pandas`, `openpyxl`, `reportlab`)[cite: 5, 6].

## 🛠️ Reglas Técnicas y de Calidad
1. **Estructura de Directorios:** Mantener una separación estricta y coherente entre el código (`codigo/` o módulos limpios), los datos de entrada (`datos/alumnos.xlsx`) y la salida (`certificados/`) tal como se documenta en el README[cite: 6].
2. **Validación de Datos:** El sistema debe verificar proactivamente la existencia del archivo de Excel, la presencia de columnas obligatorias (`Nombre`, `Curso`, `Fecha`) y el manejo de celdas vacías o tipos de datos erróneos antes de iniciar la renderización.
3. **Robustez Gráfica (ReportLab):** Evitar desbordamientos de texto en nombres o cursos largos mediante la validación de longitudes o ajustes dinámicos en las coordenadas de la capa de canvas[cite: 8].
4. **Buenas Prácticas (Clean Code):** Modularizar el código separando la capa de lectura/validación de datos de la capa de diseño gráfico del PDF.

## 📋 Flujo de Trabajo Operativo
- Consultar y actualizar siempre `MEMORY.md` antes y después de cada iteración o refactorización.
- Documentar claramente cualquier cambio en la estructura de dependencias o en la lógica de procesamiento.