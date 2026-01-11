import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Configuración de Rutas
ruta_base = r"C:\Users\UVANZ\Downloads\Workstation\Consultores y Salario"
archivo_csv = os.path.join(ruta_base, "base_datos_talento_2026.csv")
archivo_grafica = os.path.join(ruta_base, "grafica_salarios.png")

print("--- INICIANDO ANALISIS DE DATOS CON PANDAS ---")

try:
    # 2. Carga Masiva de Datos
    df = pd.read_csv(archivo_csv)

    # 3. Análisis Rápido (Cálculos automáticos)
    promedio = df['Salario'].mean()
    max_exp = df['Experiencia'].max()
    total_nomina = df['Salario'].sum()

    print(f"\n✅ Datos procesados con éxito.")
    print(f"💰 Nomina Total Mensual: ${total_nomina:,.2f}")
    print(f"📈 Salario Promedio: ${promedio:,.2f}")
    print(f"🎖️ Maxima Experiencia en el equipo: {max_exp} años")

    # 4. Creación de la Gráfica Visual
    plt.figure(figsize=(10, 6))
    
    # Creamos un gráfico de barras: Nombre vs Salario
    colores = ['#2c3e50', '#2980b9', '#3498db', '#1abc9c'] # Paleta profesional
    plt.bar(df['Nombre'], df['Salario'], color=colores, edgecolor='black')

    # Personalización del gráfico
    plt.title('Comparativa Salarial por Consultor', fontsize=14, fontweight='bold')
    plt.xlabel('Nombre del Consultor', fontsize=12)
    plt.ylabel('Salario Mensual (MXN)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Añadir una línea roja con el promedio
    plt.axhline(promedio, color='red', linestyle='--', label=f'Promedio: ${promedio:,.0f}')
    plt.legend()

    # 5. Guardar el resultado
    plt.tight_layout()
    plt.savefig(archivo_grafica)
    print(f"\n📊 Grafica generada y guardada en: {archivo_grafica}")

    # Mostrar la gráfica en pantalla
    plt.show()

except Exception as e:
    print(f"❌ Error al procesar los datos: {e}")
    