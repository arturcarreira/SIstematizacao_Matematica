import os

import pandas as pd
import streamlit as st

from minhastats import (
    amplitude,
    coeficiente_variacao,
    desvio_padrao_amostral,
    media,
    mediana,
    moda,
    quartis,
    variancia_amostral,
)


st.set_page_config(
    page_title="Análise de Seguros",
    layout="wide"
)


@st.cache_data
def carregar_dados():
    caminho = os.path.join(
        os.path.dirname(__file__),
        "data",
        "insurance.csv"
    )

    return pd.read_csv(caminho)


st.title("📊 Análise de Custos de Seguro")

st.write(
    "Projeto da disciplina de Matemática e Estatística para Computação."
)

try:
    df = carregar_dados()
except FileNotFoundError:
    st.error("Erro: arquivo 'insurance.csv' não encontrado na pasta data.")
    st.stop()


# Menu lateral
menu = st.sidebar.radio(
    "Navegação",
    ["Visão geral", "Análise numérica"]
)


if menu == "Visão geral":
    c1, c2 = st.columns(2)

    c1.metric("Total de linhas", len(df))
    c2.metric("Total de colunas", len(df.columns))

    st.subheader("Amostra rápida")
    st.dataframe(df.head(10), width="stretch")

    st.subheader("Variáveis do dataset")
    st.write(", ".join(df.columns.tolist()))


else:
    st.header("Explorando variáveis numéricas")

    # Tradução dos nomes das colunas
    mapa = {
        "age": "Idade",
        "bmi": "IMC",
        "children": "Filhos",
        "charges": "Custos"
    }

    col = st.selectbox(
        "Selecione a coluna:",
        list(mapa.keys()),
        format_func=mapa.get
    )

    dados = df[col].tolist()
    q = quartis(dados)

    st.subheader(f"Estatísticas de {mapa[col]}")

    c1, c2, c3 = st.columns(3)

    c1.metric("Média", f"{media(dados):.2f}")
    c2.metric("Mediana", f"{mediana(dados):.2f}")
    c3.metric("Moda", f"{moda(dados):.2f}")

    c4, c5, c6 = st.columns(3)

    c4.metric("Amplitude", f"{amplitude(dados):.2f}")
    c5.metric("Variância", f"{variancia_amostral(dados):.2f}")
    c6.metric(
        "Desvio padrão",
        f"{desvio_padrao_amostral(dados):.2f}"
    )

    c7, c8, c9 = st.columns(3)

    c7.metric("Q1", f"{q['Q1']:.2f}")
    c8.metric("Q2 (Mediana)", f"{q['Q2']:.2f}")
    c9.metric("Q3", f"{q['Q3']:.2f}")

    st.metric(
        "Coeficiente de variação",
        f"{coeficiente_variacao(dados):.2f}%"
    )