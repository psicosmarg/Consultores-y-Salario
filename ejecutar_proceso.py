import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# --- CONFIGURACIÓN DE RUTAS ---
carpeta = r"C:\Users\UVANZ\Downloads\Workstation\Consultores y Salario"
archivo_in = os.path.join(carpeta, "base_datos_talento_2026.csv")
archivo_grafica = os.path.join(carpeta, "reporte_grafico.png")
archivo_pdf = os.path.join(carpeta, "ENTREGABLE_FINAL_AUTOMATIZADO.pdf")

def robot_automatizacion():
    print("🤖 Iniciando Robot de Reporteo...")

    try:
        # 1. LIMPIEZA Y PROCESAMIENTO (PANDAS)
        df = pd.read_csv(archivo_in)
        df = df.dropna(subset=['Salario', 'Nombre']) # Limpieza básica
        df['Nombre'] = df['Nombre'].str.strip().str.title()
        
        # 2. GENERACIÓN DE GRÁFICA (MATPLOTLIB)
        plt.figure(figsize=(12, 6))
        plt.bar(df['Nombre'], df['Salario'], color='#3498db')
        plt.xticks(rotation=45, ha='right')
        plt.title('Distribucion Salarial Actual')
        plt.tight_layout()
        plt.savefig(archivo_grafica)
        plt.close() # Cerramos para no saturar memoria
        print("✅ Datos limpios y grafica generada.")

        # 3. CREACIÓN DE REPORTE (FPDF)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "REPORTE AUTOMATIZADO DE NOMINA", 0, 1, 'C')
        pdf.ln(5)

        # Resumen Ejecutivo
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Total Consultores: {len(df)}", 0, 1)
        pdf.cell(0, 10, f"Presupuesto Total: ${df['Salario'].sum():,.2f}", 0, 1)
        
        # Insertar la gráfica que acabamos de crear
        pdf.image(archivo_grafica, x=10, y=50, w=190)
        
        # Guardar PDF
        pdf.output(archivo_pdf)
        print(f"✅ ¡Robot finalizado! Reporte listo en: {archivo_pdf}")

    except Exception as e:
        print(f"❌ Error en el proceso: {e}")

if __name__ == "__main__":
    robot_automatizacion()