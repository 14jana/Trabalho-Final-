#Nome:Janaina Vicente dos Santos RA:2302926 

import sqlalchemy as sqa
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#Dados em um DataFrame
df = pd.read_csv('../0_bases_originais/dados_originais.csv', delimiter=";")

# App Bilheteria 
st.header('APP BILHETERIA', divider='red')

# Lateral
st.sidebar.header('Selecione o Filme')

filme_selecionado = st.sidebar.selectbox('Filme', df['filme'])

# Informçao central 
filme_data = df[df['filme'] == filme_selecionado]

st.write('Dados do Filme Selecionado')
st.write(filme_data)

st.write('Relação Geral')
st.dataframe(df, width=1000, height=500, hide_index=True)  # Mesmo que st.write(df)


