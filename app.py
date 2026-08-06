import os

import pandas as pd
import streamlit as st


# Configuração básica da página
st.set_page_config(
    page_title="Trabalho de Estatística",
    layout="wide",
)


@st.cache_data
def carregar_dados():
    # Caminho do arquivo CSV
    caminho = os.path.join(
        os.path.dirname(__file__),
        "data",
        "insurance.csv"
    )

    return pd.read_csv(caminho)


st.title("Análise de Custos de Seguro Médico")

st.write(
    "Trabalho da disciplina de Matemática e Estatística para Computação."
)

# Carrega o conjunto de dados
try:
    df = carregar_dados()
except FileNotFoundError:
    st.error("Erro: arquivo insurance.csv não encontrado na pasta data.")
    st.stop()

# Exibe informações gerais da base
col1, col2 = st.columns(2)

col1.metric("Total de registros", len(df))
col2.metric("Quantidade de variáveis", len(df.columns))

st.subheader("Amostra dos dados")
st.dataframe(df.head(20), width="stretch")

st.subheader("Colunas disponíveis")
st.write(list(df.columns))