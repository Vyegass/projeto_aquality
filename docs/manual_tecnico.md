<h1 style='text-align: center;'>Meus Estudos - Projeto Aquality</h1>

### Estrutura para cada comando que eu aprender 

* O Comando (A sintaxe).
* O "Porquê" (Explicação humana, ou técnica).
* O Exemplo (Um pedacinho de código que funciona).

# 
## Ativando e Desativando o Ambiente Virtual no Windows - (.venv)

* Toda vez que abrir o VS code para trabalhar no projeto, abrir o terminal e certificar que o caminho aponta para o projeto (ex: C:\Users\nomeuser\projeto>)

* O windows usa uma estrutua diferente e o script fica em uma pasta diferente chamada `Scripts`.


### **Executando o Comando de Ativação**
### `.\.venv\Scripts\activate`

### **Executando o Comando Para Desativar**
### `deactivate` 

#

## Ativando e Desativando o Ambiente Virtual no Linux - (.venv)

* O Linux usa uma estrutura de pastas baseada em padrões Unix. O script de ativação fica dentro de uma pasta chamada bin.

### **Executando o Comando de Ativação**
### `source .venv/bin/activate`

### Por que o source? No Linux, o comando source serve para ler e executar o conteúdo de um arquivo dentro do seu terminal atual, aplicando as mudanças (como o prefixo (.venv)) imediatamente.

### **Executando o Comando de Desativar**
### `deactivate`

#

**Para que serve:** .venv - Isolamento de Ferramentas (O Filtro):

Ativar: Garante que o Python use as versões exatas das bibliotecas (como o Pandas 2.0 ou Streamlit) que o programador escolheu para o projeto. Isso evita que uma atualização em outro projeto quebre o seu código atual.

Desativar: Libera o terminal para usar as ferramentas globais do sistema, evitando conflitos se você precisar rodar um script que exige versões diferentes das que estão no projeto.

Organização do Sistema (Limpeza):

Se você instalar tudo no "ambiente global" (sem ativar o venv), seu Windows ficará cheio de bibliotecas pesadas e desnecessárias espalhadas por pastas invisíveis. O .venv mantém tudo dentro da pasta do projeto.

Previsibilidade:

Ao ativar, você tem a certeza de que o comando pip list mostrará apenas o que o seu projeto realmente precisa. Isso facilita muito na hora de gerar o arquivo requirements.txt.

**Exemplo Ativo:**
```Python
    (.venv) C:\Users\username\projeto>
```
* Confirmação: Verifique se o prefixo (.venv) apareceu antes do caminho no terminal. Se ele estiver lá, você está "dentro" do ambiente.

## 👑 Streamlit - Comandos de Exibição

### `st.set_page_config()`
**Para que serve:** É a "Configuração da Identidade" do site. É aqui que definimos a como a aba do navegador vai se 
comportar e como o conteúdo será distribuído na tela.

**Como ele se comporta:**
* `page_title`: É o texto que aparece na aba do navegador.
* `page_icon`: É o pequeno ícone (favicon) que fica ao lado do título na aba. Pode ser um emoji ou o caminho para uma imagem.
* `layout`: Define se o conteúdo fica centralizado e estreito ("centered") ou se ocupa toda a largura da tela ("wide").
* `initial_sidebar_state`: Define se a barra lateral começa aberta ("expanded"), fechada ("collapsed") ou automática.

**Exemplo Prático:**
```python
import streamlit as st 

# Chama a função que define as configurações estruturais da página web
st.set_page_config(

# Define o texto que aparecerá na aba do navegador (o título do site)
page_title="Meu Dashboard de Vendas",

# Define o ícone que aparece ao lado do título na aba (pode ser um emoji)
page_icon="📊",

# Define o preenchimento da tela: 'wide' usa toda a largura disponível
layout="wide",

# Garante que o menu lateral (sidebar) apareça aberto assim que o site carregar
initial_sidebar_state="expanded"
)
```
A Regra de Ouro
Este comando deve ser a primeira instrução do Streamlit no seu código. Se você colocar um st.write ou st.title antes dele, o Python vai gerar um erro, pois o navegador não pode mudar as configurações de "base" depois que a página já começou a ser desenhada.

# 

### `st.write()`
**Para que serve:** É a função "canivete suíço" do Streamlit. Ela consegue renderizar quase qualquer coisa (texto, tabelas, dicionários, gráficos e até mensagens de erro) sem que você precise especificar um comando detalhado.

**Como ele se comporta:**
* Se você passar uma **String**, ele exibe um texto comum.
* Se você passar um **DataFrame (Pandas)**, ele exibe uma tabela.
* Se você passar um **Dicionário**, ele exibe um objeto interativo que você pode abrir e fechar.
* Se você usar **Markdown** dentro dele, ele formata o texto (ex: `st.write("**Negrito**")`).

**Exemplo Prático:**
``` Python
import streamlit as st
import pandas as pd

# Escrevendo um texto simples
st.write("Olá, este é o controle da Aquality!")

# Escrevendo uma tabela (DataFrame)
df = pd.DataFrame({'Venda': [139.00], 'Tipo': ['Gás']})
st.write(df)

# Escrevendo uma conta matemática
st.write(10 + 20) # Vai exibir 30 no site
```
#

### O comando `st.markdown`

**Para que serve:** Serve para renderizar texto formatado, mas quando passamos o parâmentro `unsafe_allow_html=True`, abrimos uma porta para o navegador ler código **HTML** E **CSS** puro.

**Explicação:** Imagine que você está criando um relatório ou dashboard e quer deixar o texto mais claro, organizado e visualmente atraente — por exemplo, com títulos, listas, negrito ou links. O st.markdown permite que você faça isso de forma simples, sem precisar usar códigos complexos de HTML. É como escrever em um bloco de notas com formatação, mas direto no seu programa. 

**Como ele se comporta** O st.markdown se comporta interpretando strings com formatação Markdown (como negrito, itálico, títulos, listas, links, emojis, cores, etc.) e exibindo-as visualmente formatadas na interface do Streamlit.  Ele transforma texto simples em conteúdo rico, como em um editor de texto com formatação leve. 

Por exemplo, ao usar `:blue[texto]`, ele exibe o texto em azul. Ao usar `**negrito**`, o texto aparece em **negrito**.  Ele também pode interpretar LaTeX, símbolos tipográficos e até HTML `(se unsafe_allow_html=True)`.

**Exemplo Prático**
``` Python
import streamlit as st

st.markdown("""
# Olá, mundo!
Este é um exemplo de texto formatado com **Markdown**.

- Item 1
- Item 2
- [Clique aqui para ir ao Google](https://www.google.com)
""")
```
#

### A Tag `<style>`

**Para que serve:** Tag `<style>` no Markdown no Streamlit

A tag `<style>` permite adicionar estilos personalizados diretamente no código HTML dentro do Streamlit, como cores, fontes ou layout. Isso é útil quando você quer dar um toque visual específico a elementos da sua aplicação, como uma tabela ou um texto, sem precisar criar um arquivo CSS externo. 

Você pode usar a tag `<style>` dentro de um bloco HTML exibido com st.markdown, mas precisa habilitar o modo seguro `(unsafe_allow_html=True)` porque o Streamlit protege contra códigos maliciosos por padrão. 

**Exemplo:** 
``` Python
import streamlit as st

html_with_style = """
<style>
  .meu-titulo {
    color: #2E8B57;
    font-size: 24px;
    font-family: 'Arial', sans-serif;
    text-align: center;
  }
</style>

<h1 class="meu-titulo">Este é um título personalizado</h1>
"""

st.markdown(html_with_style, unsafe_allow_html=True)   
``` 
#

### O Seletor `.block-container`

**Para que serve:** 



``` Python
st.markdown(
    """
            <style>
            .block-container {  
                padding-top: 2rem;      /* Diminui o espaço interno superior */
                padding-bottom: 0rem;   /* Elimina o buraco no fundo da página */
                margin-top: -1rem;     /* Empurra a caixa inteira para cima */
            }
            </style>
            """,
            unsafe_allow_html=True
            )
```

*Funções principais do Streamlit
Exibição de conteúdo:

st.title(), st.header(), st.subheader(), st.markdown(), st.write(), st.code(), st.latex(), st.caption() 

#
Widgets de entrada:

st.text_input(), st.number_input(), st.date_input(), st.time_input(), st.text_area(), st.file_uploader(), st.color_picker(), st.checkbox(), st.button(), st.radio(), st.selectbox(), st.multiselect(), st.select_slider(), st.slider() 

#
Exibição de mídia:

st.image(), st.audio(), st.video()

#
Exibição de gráficos:

st.line_chart(), st.bar_chart(), st.area_chart(), st.altair_chart(), st.graphviz_chart(), st.map() 

#
Mensagens de status e progresso:

st.success(), st.error(), st.warning(), st.info(), st.exception(), st.balloons(), st.progress(), st.spinner() 

#
Organização de layout:

st.sidebar(), st.container(), st.columns(), st.tabs()

#
Caching e otimização:

@st.cache_data, @st.cache_resource*

#

Além das funções principais do Streamlit, existem métodos e ferramentas úteis que aprimoram a interatividade, organização e desempenho das aplicações.  Essas funcionalidades são essenciais para criar apps mais dinâmicos e profissionais. 

Funções e métodos secundários importantes
1. Gerenciamento de estado com st.session_state
Permite armazenar e acessar valores entre interações do usuário, mantendo o estado de widgets.

if 'contador' not in st.session_state:
    st.session_state.contador = 0

if st.button('Incrementar'):
    st.session_state.contador += 1

st.write(f"Contador: {st.session_state.contador}")