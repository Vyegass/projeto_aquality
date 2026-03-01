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



elif aba_selecionada == 'Todas as Vendas':
    st.subheader('Todas as Vendas')


elif aba_selecionada == 'Relatório':
    st.subheader('Relatório')
