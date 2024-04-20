import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Mi Primer Panel Streamlit')

# Cargar los datos desde el archivo Excel
file_path = 'ruta/a/tu/archivo.xlsx'  # Cambia 'ruta/a/tu/archivo.xlsx' por la ruta de tu archivo Excel
df = pd.read_excel(file_path)

# Filtrar los datos según la columna deseada (por ejemplo, 'Ejecucion al I Trimestre')
selected_column = 'Ejecucion al I Trimestre'
data = df[selected_column]

# Crear el histograma utilizando Plotly Express
fig = px.histogram(x=data)

# Mostrar el histograma en la aplicación Streamlit
st.plotly_chart(fig)
