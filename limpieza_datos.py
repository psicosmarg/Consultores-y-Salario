import pandas as pd
import os

# 1. Configuración de Rutas
ruta_base = r"C:\Users\UVANZ\Downloads\Workstation\Consultores y Salario"
archivo_csv = os.path.join(ruta_base, "base_datos_talento_2026.csv")
archivo_limpio = os.path.join(ruta_base, "base_datos_LIMPIA.csv")

print("--- INICIANDO PROCESO DE LIMPIEZA DE DATOS ---")

try:
    # 2. Cargar el archivo original
    df = pd.read_csv(archivo_csv)
    print(f"Filas originales: {len(df)}")

    # 3. LIMPIEZA 1: Eliminar filas que estén completamente vacías
    df = df.dropna(how='all')

    # 4. LIMPIEZA 2: Limpiar la columna 'Nombre'
    # .str.strip() quita espacios extra; .str.title() pone formato de nombre propio
    df['Nombre'] = df['Nombre'].str.strip().str.title()

    # 5. LIMPIEZA 3: Asegurar que Salario y Experiencia sean números
    # errors='coerce' convierte cualquier letra o error en "NaN" (Not a Number)
    df['Salario'] = pd.to_numeric(df['Salario'], errors='coerce')
    df['Experiencia'] = pd.to_numeric(df['Experiencia'], errors='coerce')

    # Eliminamos las filas que resultaron con errores en salario (datos inservibles)
    df = df.dropna(subset=['Salario'])

    # 6. LIMPIEZA 4: Eliminar duplicados (si alguien registró dos veces al mismo consultor)
    df = df.drop_duplicates(subset=['Nombre'], keep='last')

    # 7. Guardar la versión purificada
    df.to_csv(archivo_limpio, index=False, encoding='utf-8-sig')
    
    print(f"✅ ¡Limpieza terminada!")
    print(f"Filas finales: {len(df)}")
    print(f"Archivo guardado como: base_datos_LIMPIA.csv")

except Exception as e:
    print(f"❌ Error durante la limpieza: {e}")