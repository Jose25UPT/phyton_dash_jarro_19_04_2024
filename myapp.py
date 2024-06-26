import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title('Panel Presupuesto Institucional Del año 2014-2015')

# Obtener la lista de archivos en las carpetas
folder_paths = ['excel 2014', 'excel 2015']  # Rutas de las carpetas que contienen los archivos Excel
excel_files = []

for folder_path in folder_paths:
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.xlsx')]
    excel_files.extend(files)

# Cargar los datos de todos los archivos Excel en un solo DataFrame
dfs = {}
for file in excel_files:
    year = file.split("/")[-2].split()[-1]
    if year not in dfs:
        dfs[year] = []
    df = pd.read_excel(file)
    dfs[year].append(df)

# Combine the data of each year into a single DataFrame
combined_dfs = {year: pd.concat(dfs[year], ignore_index=True) for year in dfs}

# Permitir al usuario seleccionar un año
st.sidebar.title("Selecciona un año:")
selected_year = st.sidebar.radio("", list(combined_dfs.keys()))

# Obtener las columnas del DataFrame seleccionado
columns = combined_dfs[selected_year].columns

# Permitir al usuario seleccionar una columna para la visualización
selected_column = st.selectbox('Selecciona una columna:', columns)

# Crear cinco tipos diferentes de gráficos

# Gráfico de barras
st.subheader('Gráfico de Barras')
fig_bar = px.bar(combined_dfs[selected_year][selected_column].value_counts(), x=combined_dfs[selected_year][selected_column].value_counts().index, y=combined_dfs[selected_year][selected_column].value_counts().values)
st.plotly_chart(fig_bar)

# Gráfico de dispersión
st.subheader('Gráfico de Dispersión')
fig_scatter = px.scatter(combined_dfs[selected_year], x=selected_column, y=combined_dfs[selected_year].columns[0])  # Utiliza la primera columna como eje y
st.plotly_chart(fig_scatter)

# Gráfico de líneas
st.subheader('Gráfico de Líneas')
fig_line = px.line(combined_dfs[selected_year], x=combined_dfs[selected_year].index, y=selected_column)
st.plotly_chart(fig_line)

# Diagrama de caja
st.subheader('Diagrama de Caja')
fig_box = px.box(combined_dfs[selected_year], y=selected_column)
st.plotly_chart(fig_box)

# Mapa de calor
st.subheader('Mapa de Calor')
numeric_columns = combined_dfs[selected_year].select_dtypes(include='number')
if not numeric_columns.empty:
    correlation_matrix = numeric_columns.corr()
    fig_heatmap = px.imshow(correlation_matrix)
    st.plotly_chart(fig_heatmap)
else:
    st.write("No se pueden calcular correlaciones ya que no hay columnas numéricas en el DataFrame.")
