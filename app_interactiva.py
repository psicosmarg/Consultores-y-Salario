import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuración de la página (esto le da el look profesional)
st.set_page_config(page_title="Talent Dashboard", layout="wide")

st.title("🚀 Dashboard Interactivo de Consultores")
st.markdown("Filtra la información y visualiza los salarios en tiempo real.")

# Ruta de tu archivo
ruta_csv = r"C:\Users\UVANZ\Downloads\Workstation\Consultores y Salario\base_datos_talento_2026.csv"

if os.path.exists(ruta_csv):
    df = pd.read_csv(ruta_csv)

    # --- BARRA LATERAL (Filtros) ---
    st.sidebar.header("Opciones de Filtrado")
    categorias = st.sidebar.multiselect(
        "Selecciona Categorías:",
        options=df["Categoria"].unique(),
        default=df["Categoria"].unique()
    )

    # Filtrar datos según la selección
    df_filtrado = df[df["Categoria"].isin(categorias)]

    # --- MÉTRICAS ---
    m1, m2, m3 = st.columns(3)
    m1.metric("Consultores", len(df_filtrado))
    m2.metric("Nómina Total", f"${df_filtrado['Salario'].sum():,.2f}")
    m3.metric("Promedio", f"${df_filtrado['Salario'].mean():,.2f}")

    # --- GRÁFICA INTERACTIVA ---
    st.subheader("Comparativa Salarial")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(df_filtrado["Nombre"], df_filtrado["Salario"], color="#2980b9")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

    # --- TABLA DE DATOS ---
    st.subheader("Registros Detallados")
    st.dataframe(df_filtrado)

else:
    st.error("⚠️ Archivo CSV no encontrado. Registra datos primero.")
    # --- BOTÓN DE DESCARGA ---
st.divider() # Una línea divisoria estética
st.subheader("📥 Exportar Datos")

# Convertimos el DataFrame filtrado a un archivo CSV en memoria
csv_datos = df_filtrado.to_csv(index=False).encode('utf-8-sig')

st.download_button(
    label="Descargar datos filtrados (CSV)",
    data=csv_datos,
    file_name='reporte_consultores_filtrado.csv',
    mime='text/csv',
)