import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Talent Dashboard", layout="wide")
st.title("🚀 Dashboard Interactivo de Consultores")

# RUTA RELATIVA (Indispensable para GitHub/Streamlit Cloud)
ruta_csv = "base_datos_talento_2026.csv" 

# 2. CARGA DE DATOS
if os.path.exists(ruta_csv):
    df = pd.read_csv(ruta_csv)

    # --- FILTROS (Barra Lateral) ---
    st.sidebar.header("Opciones de Filtrado")
    categorias = st.sidebar.multiselect(
        "Selecciona Categorías:",
        options=df["Categoria"].unique(),
        default=df["Categoria"].unique()
    )
    df_filtrado = df[df["Categoria"].isin(categorias)]

    # --- MÉTRICAS ---
    m1, m2, m3 = st.columns(3)
    m1.metric("Consultores", len(df_filtrado))
    m2.metric("Nómina Total", f"${df_filtrado['Salario'].sum():,.2f}")
    m3.metric("Promedio", f"${df_filtrado['Salario'].mean():,.2f}")

    # --- GRÁFICA ---
    st.subheader("Comparativa Salarial")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(df_filtrado["Nombre"], df_filtrado["Salario"], color="#2980b9")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

    # --- TABLA Y EXPORTACIÓN ---
    st.subheader("Registros Detallados")
    st.dataframe(df_filtrado, use_container_width=True)

    st.divider()
    st.subheader("📥 Exportar Datos")
    # Generamos el CSV para descarga
    csv_datos = df_filtrado.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="Descargar reporte filtrado",
        data=csv_datos,
        file_name='reporte_talento_limpio.csv',
        mime='text/csv',
    )

else:
    st.error("⚠️ El archivo 'base_datos_talento_2026.csv' no se encuentra en el repositorio.")
    st.info("Asegúrate de que el nombre del archivo en GitHub sea exacto.")