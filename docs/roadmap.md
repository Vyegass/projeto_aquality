# Planejamento do Projeto Aqualiy 

## Obejetivo Principal
Criar uma interface web local para registro manual de vendas, consulta de histórico e  geração de relatórios automáticos.

---


## Requisitos da Fase 1 

### 1. Interface Visual
- [ ] Criar a estrutura básica da página com **Streamlit**.
- [ ] Configurar o título e layout da aplicação.

### 2. Banco de Dados & Armazenamento
- [ ] Criar banco de dados **SQLite** (`data/aquality.db`).
- [ ] Definir a tabela de vendas com as Colunas:
 - `Data`, `Pedido`, `Tipo`, `Quantidade`, `Pagamento`, `Preço_Total`.

### 3. Fluxo de Opereção (User Flow)
1. **Tela Inicial:** Exibe o histórico de vendas do dia usando `st.dataframe`.
2. **Ação:** Botão ou área de "Nova Venda".
3. **Seleção Inteligente:** Listar produtos (Gás 13kg, Água 20L, etc.).
4. **Interação:** Usuário clica no produto -> Sistema preenche automaticamente o nome e preço base.
5. **Validação:** Script verifica se quantidade e forma de pagamento foram informadas.
6. **Persistência:** Salva os dados no SQLite.
7. **Atualização:** Limpa o formulário e atualiza a tabela na tela principal.

## Estrutura de Dados (Exemplo)

| Data | Pedido | TIPO | QUANTIDADE | FORMA DE PAGAMENTO | PREÇO TOTAL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 13/02/2026 |  GÁS 13KG | RECARGA |  1 | PIX | R$ 139,00 |


## Próximos Passos
- [x] Configurar ambiente (Python, Streamlit, Pandas).
- [ ] Desenvolver o formulário de entrada com botões de seleção de produto.
- [ ] Conectar o formulário ao banco de dados SQLite.
