import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração da Página Web (Tem que ser o primeiro comando)
st.set_page_config(page_title="Dashboard de Churn", layout="wide")

st.title("📊 Painel de Análise de Retenção de Clientes (Churn)")
st.write("Análise interativa para identificar os principais motivos de cancelamento de cartões de crédito.")
st.divider() # Linha de separação

# 2. Carregar e Limpar os Dados (O Streamlit guarda isso na memória para ficar rápido)
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("ClientesBanco (1).csv", encoding="latin1")
    tabela = tabela.drop("CLIENTNUM", axis=1)
    tabela = tabela.dropna()
    return tabela

tabela = carregar_dados()

# 3. Criar o Layout em Duas Colunas
col1, col2 = st.columns(2)

# --- COLUNA DA ESQUERDA ---
with col1:
    st.subheader("1. A Regra dos Contatos")
    fig1 = px.histogram(tabela, x="Contatos 12m", color="Categoria", text_auto=True)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("3. Engajamento de Produtos")
    fig3 = px.histogram(tabela, x="Produtos Contratados", color="Categoria", text_auto=True)
    st.plotly_chart(fig3, use_container_width=True)
    
    st.subheader("5. Engajamento Diário (Transações)")
    fig5 = px.histogram(tabela, x="Valor Transacoes 12m", color="Categoria", text_auto=True)
    st.plotly_chart(fig5, use_container_width=True)

# --- COLUNA DA DIREITA ---
with col2:
    st.subheader("2. Perfil Financeiro (Salário)")
    fig2 = px.histogram(tabela, x="Faixa Salarial Anual", color="Categoria", text_auto=True)
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("4. Termômetro de Fuga (Meses Inativos)")
    fig4 = px.histogram(tabela, x="Inatividade 12m", color="Categoria", text_auto=True)
    st.plotly_chart(fig4, use_container_width=True)
    
    st.subheader("6. Frustração com Limite de Crédito")
    # Lembre-se de checar se o nome da coluna de limite é esse mesmo na sua base!
    fig6 = px.histogram(tabela, x="Limite", color="Categoria", text_auto=True)
    st.plotly_chart(fig6, use_container_width=True)

st.success("Análise desenvolvida em Python | Pandas | Plotly | Streamlit")