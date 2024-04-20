import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title('Panel Presupuesto Institucional  Del año 2014-2015')

# Obtener la lista de archivos en las carpetas
folder_paths = ['excel 2014', 'excel 2015']  # Rutas de las carpetas que contienen los archivos Excel
excel_files = []

for folder_path in folder_paths:
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.xlsx')]
    excel_files.extend(files)

# Permitir al usuario seleccionar un archivo Excel
selected_file = st.selectbox('Selecciona un archivo Excel:', excel_files)

# Cargar los datos desde el archivo seleccionado
df = pd.read_excel(selected_file)

# Permitir al usuario seleccionar una columna para la visualización
selected_column = st.selectbox('Selecciona una columna:', df.columns)

# Crear cinco tipos diferentes de gráficos

# Gráfico de barras
st.subheader('Gráfico de Barras')
fig_bar = px.bar(df[selected_column].value_counts(), x=df[selected_column].value_counts().index, y=df[selected_column].value_counts().values)
st.plotly_chart(fig_bar)

# Gráfico de dispersión
st.subheader('Gráfico de Dispersión')
fig_scatter = px.scatter(df, x=selected_column, y=df.columns[0])  # Utiliza la primera columna como eje y
st.plotly_chart(fig_scatter)

# Gráfico de líneas
st.subheader('Gráfico de Líneas')
fig_line = px.line(df, x=df.index, y=selected_column)
st.plotly_chart(fig_line)

# Diagrama de caja
st.subheader('Diagrama de Caja')
fig_box = px.box(df, y=selected_column)
st.plotly_chart(fig_box)

# Mapa de calor
st.subheader('Mapa de Calor')
numeric_columns = df.select_dtypes(include='number')
if not numeric_columns.empty:
    correlation_matrix = numeric_columns.corr()
    fig_heatmap = px.imshow(correlation_matrix)
    st.plotly_chart(fig_heatmap)
else:
    st.write("No se pueden calcular correlaciones ya que no hay columnas numéricas en el DataFrame.")

