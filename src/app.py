import streamlit as st
import pandas as pd


# --- Configuração inicial da página ( Sempre a primeira linha de comando Streamlit ) ---

st.set_page_config(
    page_title='Aquality Distribuidora',  # Título da aba do navegador.
    
    page_icon='💧', # Define o ícone exibido na aba do navegador.                      
    
    layout='wide',  # Define o layout da págin como 'wide' para ocupar toda a largura da tela.
    
    initial_sidebar_state='expanded'    # Define o estado inicial da barra lateral como 'expanded' para que ela esteja aberta por padrão.
)

# --- Bloco de código para ajustar o espaçamento do container principal ---

st.markdown(
    """
   <style> 
    /* Reduz o espaço no topo da página principal */

    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    

    /* Remove o espaço reservado pelo cabeçalho sem esconder o botão da sidebar */

    header[data-testid="stHeader"] {
        height: 0px;
        background: transparent;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Centralizando o título principal --- 

st.markdown("<h1 style='text-align: center;'>Aquality Distribuidora</h1>", unsafe_allow_html=True)

st.divider()


# --- BARRA LATERAL --- 

with st.sidebar:
    # st.title('Aquality Distribuidora') # Título grande

    st.subheader('Controle de Vendas')

    st.divider() # Linha horizontal de separação
    
    aba_selecionada = st.segmented_control(
        'Menu', 
        options=['Vendas de Hoje', 'Todas as Vendas', 'Relatório'],
        default='Vendas de Hoje',
        key='menu_principal'
        )
        
if aba_selecionada == 'Vendas de Hoje':
    st.subheader('Vendas de Hoje')
    
        # Inicializa a variável de sessão para controlar a exibição do formulário de venda
    if 'mostrar_form_venda' not in st.session_state:
        st.session_state.mostrar_form_venda = False

    if st.button('Registrar Venda'):
        st.session_state.mostrar_form_venda = True
            
    if st.session_state.mostrar_form_venda:
        with st.form('form_Nova_Venda'):

            st.write('Selecione o Produto')

            produto = st.selectbox(
                'Produtos', 

                ['Garrafão 20L','Gás 13Kg', 'Gás 8Kg','Gás 5Kg', ],

                index=None,

                placeholder='Selecione o campo para visualizar os produtos'
            )
            
            # Fazer uma atualização de estado porque o streamlit fica em estado de congelamento, a ideia e mandar o pedido o script
            # fazer uma validação de acordo com os produtos selecionados e atualizar. 
            tipo = st.selectbox(
                'Selecione o Tipo',
                
                ['Recarga', 'Completo', 'Vazio'],

                index=None,

                placeholder='Selecione o campo para visualizar os tipos de venda'
            )

            # Futuramente atualizar para o limite máximo ser baseado no estoque disponível, e não um valor fixo.
            quantidade = st.number_input(
                'Quantidade', min_value=1, max_value=100, value=1, step=1  
            )
            
            forma_pagamento = st.selectbox(
                'Forma de Pagamento',

                ['Dinheiro', 'Cartão', 'Pix', 'Pix Fogas', 'Gás do Povo', 'Contrato'],

                index=None,

                placeholder='Selecione o campo para visualizar as formas de pagamento'
            )

            # Botões do formulário
            col1, col2 = st.columns([0.9, 10]) # Define a proporçãoo das colunas para os botões.
            with col1:
                 submit = st.form_submit_button('Salvar')
            
            with col2:
                 cancelar = st.form_submit_button('Cancelar')



            if cancelar:
                 st.session_state.mostrar_form_venda = False

                 st.success('Registro de venda cancelado.')

                 st.rerun() # Reinicia a aplicação para atualizar o estado
                 

            


elif aba_selecionada == 'Relatório':
    st.subheader('Relatório')



elif aba_selecionada == 'Todas as Vendas':
    st.subheader('Todas as Vendas')


