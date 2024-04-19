import streamlit as st
import numpy as np
import plotly.express as px

st.title('Mi Primer Panel Streamlit')

value = st.slider('Seleccione un valor', min_value=0, max_value=1000, value=500)
data = np.random.randn(value)
fig = px.histogram(x=data)
st.plotly_chart(fig)
