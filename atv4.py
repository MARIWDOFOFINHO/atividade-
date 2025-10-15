import streamlit as st
import pandas as pd

st.title('entrada e saida de dados')

dados = st.file_uploader('carregar dados')
if dados is not None:
    df = pd.read_csv(dados)
    st.success('dados carregados')
else: 
    df = []
    
st.dataframe(df)

st.sidebar.header('novos dados')
FORMULARIO = st.sidebar.form('formulario',clear_on_submit = True)
novo_nome = FORMULARIO.text_input('novo nome:')
nova_idade = FORMULARIO.text_input('nova idade:')

bt1 = FORMULARIO.form_submit_button('enviar')
if bt1:
    novo = ('nome'[novo_nome],
            'idade'[int(nova_idade)])
    x = pd.DataFrame(novo)
    DF = pd.concat([df,x],ignore_index= True)
    st.dataframe(DF)
    DF.to_csv("C:/Users/Aluno/Desktop/maria clara/dados.csv", index = False)