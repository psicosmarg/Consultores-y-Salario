# 🤖 Sistema Automatizado de Gestión de Talento (Python & Pandas)

Este proyecto es una herramienta profesional desarrollada en **Python** diseñada para automatizar el ciclo completo de gestión de datos de consultoría: desde la captura validada hasta la generación de reportes ejecutivos con analítica visual.

## 🚀 Capacidades del Sistema
- **Captura Inteligente:** Registro de consultores con validación de rangos (salarios y experiencia) para evitar datos erróneos (GIGO).
- **Procesamiento Masivo (ETL):** Uso de la librería **Pandas** para limpieza de datos, normalización de nombres y eliminación de duplicados.
- **Analítica Visual:** Generación automática de gráficos comparativos con **Matplotlib**, incluyendo líneas de promedio salarial para detección de desviaciones.
- **Reporteo Ejecutivo:** Creación de documentos **PDF** profesionales que integran tablas de datos y visualizaciones gráficas listos para la toma de decisiones.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.13
- **Librerías de Datos:** Pandas, Matplotlib
- **Generación de Documentos:** FPDF
- **Control de Versiones:** Git & GitHub

## 📂 Estructura del Proyecto
- `mi_salario.py`: Script de captura y validación de entrada.
- `ejecutar_proceso.py`: El "Robot" que integra limpieza, gráfica y PDF.
- `dashboard.py`: Análisis visual y estadístico.
- `Consultores y Salario/`: Directorio centralizado de la base de datos y entregables.

## 📈 Ejemplo de Visualización
*El sistema genera gráficas automáticas con rotación de etiquetas y alineación profesional para asegurar la legibilidad de cada consultor.*