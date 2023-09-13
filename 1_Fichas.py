import pandas as pd
import streamlit as st
import streamlit.components.v1 as components



df = pd.read_csv("cadastros.csv",
                 encoding="latin-1",
                 sep=",",
                 header=0)

busca = st.selectbox('Selecione um nome:', df.drop_duplicates('Nome_completo'))
#st.write(df[df.Nome_completo == busca][["Endereco"]].head())
endereco = df[df.Nome_completo == busca][["Endereco"]]
busca_completa = st.selectbox('Selecione o endereço:', endereco)
if st.button('Buscar Cadastro'):
    resultado = df[(df.Nome_completo == busca) & (df.Endereco == busca_completa)]
    st.write(resultado.head())


#===================== CONTAINER PARA IMPRESSÃO ===============
with st.container():
    def main():
        # Carregando o arquivo HTML
        with open("scripts/novo.html", "r") as file:
            html_content = file.read()
        # Exibindo o conteúdo HTML
        st.markdown(html_content, unsafe_allow_html=True)


    if __name__ == "__main__":
        main()
