import os

# DEFINIMOS LA RUTA MAESTRA
carpeta = r"C:\Users\UVANZ\Downloads\Workstation\Consultores y Salario"
archivo = os.path.join(carpeta, "base_datos_talento_2026.csv")

# Crear la carpeta si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

# Crear encabezados
if not os.path.exists(archivo):
    with open(archivo, "w", encoding='utf-8-sig') as f:
        f.write("Nombre,Salario,Categoria,Experiencia\n")

print("--- REGISTRO PROFESIONAL (RUTA CENTRALIZADA) ---")

while True:
    nombre = input("\nNombre del consultor (o 'salir'): ").strip().title()
    if nombre.lower() == "salir": break
        
    try:
        salario = float(input(f"Salario para {nombre}: "))
        exp = int(input(f"Experiencia para {nombre}: "))
        
        if salario <= 0 or exp < 0:
            print("❌ Datos invalidos.")
            continue

        categoria = "Senior Premium" if salario > 70000 and exp > 5 else "Especialista" if salario > 30000 else "Asistente"

        with open(archivo, "a", encoding='utf-8-sig') as f:
            f.write(f"{nombre},{salario},{categoria},{exp}\n")
        print(f"✅ Guardado en: {carpeta}")

    except ValueError:
        print("❌ Error de formato.")
        