#importing libraries
import streamlit as st 
import pandas as pd
import plotly.express as px

st.header('Car Sales Data') #header
st.write('This is a web app to visualize car sales data') #description

car_df = pd.read_csv('P:/DevTools/Projects/Python/Web-App-Project/vehicles_us.csv') #read csv file
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_df, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)