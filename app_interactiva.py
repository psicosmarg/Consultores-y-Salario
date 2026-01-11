import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Talent Dashboard", layout="wide")

st.title("🚀 Dashboard Interactivo de Consultores")

# --- CAMBIO CLAVE: RUTA RELATIVA ---
# Ahora Python buscará el archivo en la misma carpeta donde está el script
ruta_csv = "base_datos_talento_2026.csv" 

if os.path.exists(ruta_csv):
    df = pd.read_csv(ruta_csv)

    # ... (Aquí va todo tu código de filtros y métricas que ya tienes) ...
    # Asegúrate de que los filtros y la gráfica estén AQUÍ ADENTRO.

    # --- BOTÓN DE DESCARGA (Ahora seguro dentro del IF) ---
    st.divider()
    st.subheader("📥 Exportar Datos")
    csv_datos = df_filtrado.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="Descargar datos filtrados (CSV)",
        data=csv_datos,
        file_name='reporte_consultores_filtrado.csv',
        mime='text/csv',
    )

else:
    st.warning("⚠️ No se encontró el archivo CSV en el repositorio.")
    st.info("Asegúrate de haber subido 'base_datos_talento_2026.csv' a la misma carpeta en GitHub.")