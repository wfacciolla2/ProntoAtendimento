import pandas as pd
import streamlit as st

df = pd.read_csv("C:/Users/welli/PycharmProjects/ProjetoFinal/cadastros.csv",
                 encoding="latin-1",
                 sep=",",
                 header=0)

busca = st.selectbox('Selecione um nome:', df.drop_duplicates('Nome_completo'))
st.write(df[df.Nome_completo == busca][["Endereco"]].head())
endereco = df[df.Nome_completo == busca][["Endereco"]]
busca_completa = st.selectbox('Selecione o endereço:', endereco)
if st.button('Buscar Cadastro'):
    resultado = df[(df.Nome_completo == busca) & (df.Endereco == busca_completa)]
    edited_df = st.data_editor(resultado)