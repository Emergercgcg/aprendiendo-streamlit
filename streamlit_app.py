
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar los datos
@st.cache
def load_data():
    data = pd.read_csv('tu_archivo.csv')  # Asegúrate de poner el nombre correcto del archivo
    return data

data = load_data()

# Título de la aplicación
st.title('Buscador de Películas')

# Caja de búsqueda
search_query = st.text_input('Ingrese el nombre de la película a buscar:')

# Filtrar datos
if search_query:
    filtered_data = data[data['titulo'].str.contains(search_query, case=False)]  # Asegúrate de que 'titulo' es el nombre de la columna correcta

    # Mostrar datos filtrados
    st.write(filtered_data)

    # Crear un gráfico con Matplotlib (ejemplo: histograma de calificaciones)
    if not filtered_data.empty:
        plt.figure(figsize=(10, 4))
        plt.hist(filtered_data['calificacion'], bins=20, color='blue')  # Asegúrate de que 'calificacion' es la columna correcta
        plt.title('Distribución de Calificaciones')
        plt.xlabel('Calificación')
        plt.ylabel('Frecuencia')
        st.pyplot(plt)

        # Crear un gráfico con Plotly (ejemplo: gráfico de dispersión de duración vs calificación)
        fig = px.scatter(filtered_data, x='duracion', y='calificacion', color='genero')  # Asegúrate de que estas columnas existen
        st.plotly_chart(fig)
else:
    st.write(data)
