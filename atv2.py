import streamlit as st

st.title('HM LANCHES')
st.header('Hambúrgueres')

item1 = st.checkbox('hambúrguer/ R$20')
if item1:
    print('hambúrguer/ R$20')
item2 = st.checkbox('x-egg búrguer/ R$23')
if item2:
    print('x-egg búrguer/ R$23')
item3 = st.checkbox('x-bacon/ R$25')
if item3: 
    print('x-bacon/ R$25')
item4 = st.checkbox('x-calabresa/ R$25')
if item4:
    print('x-calabresa/ R$25')
item5 = st.checkbox('hambúrguer artesanal/ R$35')
if item5:
    print('hambúrguer artesanal/ R$35')
    
st.markdown('---')

st.header('porções')

item1 = st.checkbox('fritas 400g/ R$25')
if item1:
    print('fritas 400g/ R$25')
item2 = st.checkbox('fritas com bacon e cheedar 400g/ R$40')
if item2: 
    print('fritas com bacon e cheedar 400g/ R$40')
item3 = st.checkbox('fritas com tiras de file mignon 400g/ R$70')
if item3: 
    print('fritas com tiras de file mignon 400g/ R$70')
    
st.markdown('---')

st.header('Formas de pagamento')
Lista = st.radio('pagamento', options = ('pix','cartão','dinheiro'))
print(Lista)

Lista = st.radio('caso for dinheiro, precisa de troco?', options = ('sim','não',))
print(Lista)


st.sidebar.header('Dados do pedido')


txt1 = st.sidebar.text_input('Qual o seu nome?')
st.sidebar.write('Bem-vindo ao HM LANCHES')

txt2 = st.sidebar.text_area('Entrega ou Retirada?',
                            max_chars = 20)
st.sidebar.write(txt2)
txt3 = st.sidebar.text_area('Informe seu endereço caso a for entrega',
                            max_chars= 200)
st.sidebar.write(txt3)
txt4 = st.sidebar.text_area('Qual a forma de pagamento?',
                            max_chars= 30)
st.sidebar.write(txt4)
