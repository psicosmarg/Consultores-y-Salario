import csv
import os
from fpdf import FPDF

# RUTAS CENTRALIZADAS
carpeta = r"C:\Users\UVANZ\Downloads\Workstation\Consultores y Salario"
archivo_csv = os.path.join(carpeta, "base_datos_talento_2026.csv")
archivo_pdf = os.path.join(carpeta, "Reporte_Ejecutivo_2026.pdf")

class PDF(FPDF):
    def header(self):
        # Logo o Título principal
        self.set_font('Arial', 'B', 16)
        self.set_text_color(33, 37, 41) # Gris oscuro profesional
        self.cell(0, 10, 'REPORTE EJECUTIVO DE TALENTO HUMANO', 0, 1, 'C')
        self.set_draw_color(50, 50, 50)
        self.line(10, 22, 200, 22) # Línea decorativa
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def generar_pdf_profesional():
    try:
        with open(archivo_csv, mode="r", encoding="utf-8-sig") as f:
            lector = csv.DictReader(f)
            datos = list(lector)

        if not datos:
            print("No hay datos para procesar.")
            return

        pdf = PDF()
        pdf.add_page()
        
        # --- SECCIÓN DE RESUMEN ---
        total_salarios = sum(float(fila['Salario']) for fila in datos)
        pdf.set_font("Arial", 'B', 12)
        pdf.set_fill_color(240, 240, 240)
        pdf.cell(0, 10, " RESUMEN FINANCIERO", 0, 1, 'L', fill=True)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, f" Total de Consultores registrados: {len(datos)}", 0, 1)
        pdf.cell(0, 8, f" Presupuesto Mensual Total: ${total_salarios:,.2f} MXN", 0, 1)
        pdf.ln(5)

        # --- TABLA DE DATOS ---
        # Encabezados (Colores de fondo azul profesional)
        pdf.set_font("Arial", 'B', 10)
        pdf.set_fill_color(44, 62, 80) # Azul medianoche
        pdf.set_text_color(255, 255, 255) # Texto blanco
        
        pdf.cell(55, 10, " Nombre", 1, 0, 'C', True)
        pdf.cell(45, 10, " Categoria", 1, 0, 'C', True)
        pdf.cell(45, 10, " Salario", 1, 0, 'C', True)
        pdf.cell(45, 10, " Experiencia", 1, 1, 'C', True)

        # Filas de la tabla
        pdf.set_text_color(0, 0, 0) # Volver a texto negro
        pdf.set_font("Arial", size=10)
        
        for fila in datos:
            pdf.cell(55, 9, f" {fila['Nombre'][:22]}", 1)
            pdf.cell(45, 9, f" {fila['Categoria']}", 1)
            pdf.cell(45, 9, f" ${float(fila['Salario']):,.2f}", 1, 0, 'R')
            pdf.cell(45, 9, f" {fila['Experiencia']} años", 1, 1, 'C')

        pdf.output(archivo_pdf)
        print(f"✅ ¡Éxito! Reporte visual generado en: {archivo_pdf}")

    except Exception as e:
        print(f"❌ Error al generar el PDF: {e}")

generar_pdf_profesional()