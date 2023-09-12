import streamlit as st
import csv
import time

st.title('Cadastros')


def save_name(nome, nome_mae, numero_cartao, cpf, rg, data_nascimento, sexo, telefone, endereco, cep, municipio, estado, atendente):
    filename = 'C:/Users/welli/PycharmProjects/ProjetoFinal/cadastros.csv'
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, nome_mae, numero_cartao, cpf, rg, data_nascimento, sexo, telefone, endereco, cep, municipio, estado, atendente])
    delay = 5
    start_time = time.time()
    st.markdown('Cadastro efetuado')
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= delay:
            st._rerun()
            break


nome = st.text_input('Nome completo:')
nome_mae = st.text_input('Nome da mãe:')
numero_cartao = st.text_input('Numero do cartão:')
cpf = st.text_input('CPF')
rg = st.text_input('RG')
data_nascimento = st.text_input('Data de Nascimento')
sexo = st.selectbox('Sexo', ['Masculino', 'Feminino','Sexo'])
telefone = st.text_input('Telefone')
endereco = st.text_input('Endereço completo')
cep = st.text_input('CEP')
municipio = st.text_input('Município')
estado = st.text_input('Estado')
atendente = st.text_input('Nome do Atendente')
if st.button('Salvar'):
    save_name(nome, nome_mae, numero_cartao, cpf, rg, data_nascimento, sexo, telefone, endereco, cep, municipio, estado, atendente)
    st.experimental_rerun()