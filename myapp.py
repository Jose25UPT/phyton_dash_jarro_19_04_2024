import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title('Mi Primer Panel Streamlit')

# Obtener la lista de archivos en las carpetas
folder_paths = ['excel_2014', 'excel_2015']  # Rutas de las carpetas que contienen los archivos Excel
excel_files = []

for folder_path in folder_paths:
    files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]
    excel_files.extend(files)

# Permitir al usuario seleccionar un archivo Excel
selected_file = st.selectbox('Selecciona un archivo Excel:', excel_files)

# Cargar los datos desde el archivo seleccionado
file_path = os.path.join(folder_path, selected_file)
df = pd.read_excel(file_path)

# Permitir al usuario seleccionar una columna para el histograma
selected_column = st.selectbox('Selecciona una columna para el histograma:', df.columns)

# Crear el histograma utilizando Plotly Express
fig = px.histogram(x=df[selected_column])

# Mostrar el histograma en la aplicación Streamlit
st.plotly_chart(fig)
