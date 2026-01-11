import csv
import os
from fpdf import FPDF

# 1. RUTAS CENTRALIZADAS (Asegúrate de que esta carpeta exista)
ruta_base = r"C:\Users\UVANZ\Downloads\Workstation\Consultores y Salario"
archivo_csv = os.path.join(ruta_base, "base_datos_talento_2026.csv")
archivo_pdf = os.path.join(ruta_base, "Reporte_Ejecutivo_2026.pdf")

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'REPORTE EJECUTIVO DE NOMINA', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

def generar_reporte():
    try:
        # Validamos si el CSV existe antes de empezar
        if not os.path.exists(archivo_csv):
            print(f"❌ Error: No existe el archivo {archivo_csv}. Primero usa mi_salario.py")
            return

        with open(archivo_csv, mode="r", encoding="utf-8-sig") as f:
            datos = list(csv.DictReader(f))

        pdf = PDF()
        pdf.add_page()
        
        # --- TABLA PROFESIONAL ---
        pdf.set_font("Arial", 'B', 10)
        pdf.set_fill_color(50, 50, 50)
        pdf.set_text_color(255, 255, 255)
        
        pdf.cell(60, 10, " NOMBRE", 1, 0, 'C', True)
        pdf.cell(45, 10, " CATEGORIA", 1, 0, 'C', True)
        pdf.cell(45, 10, " SALARIO", 1, 0, 'C', True)
        pdf.cell(40, 10, " EXP.", 1, 1, 'C', True)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", size=10)

        for fila in datos:
            pdf.cell(60, 9, f" {fila['Nombre']}", 1)
            pdf.cell(45, 9, f" {fila['Categoria']}", 1)
            pdf.cell(45, 9, f" ${float(fila['Salario']):,.2f}", 1, 0, 'R')
            pdf.cell(40, 9, f" {fila['Experiencia']} años", 1, 1, 'C')

        pdf.output(archivo_pdf)
        print(f"✅ ¡PDF generado con exito en la carpeta de Consultores!")

    except PermissionError:
        print("❌ ERROR: El PDF esta abierto. Cierralo e intenta de nuevo.")
    except Exception as e:
        print(f"❌ Ocurrio un error: {e}")

if __name__ == "__main__":
    generar_reporte()