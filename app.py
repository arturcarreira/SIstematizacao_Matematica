import os

import pandas as pd
import plotly.express as px
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


# Configuração da página
st.set_page_config(
    page_title="Análise de Seguros",
    layout="wide"
)


# Carrega o arquivo CSV
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


# Tenta carregar a base
try:
    df = carregar_dados()

except FileNotFoundError:
    st.error(
        "Erro: arquivo 'insurance.csv' não encontrado na pasta data."
    )
    st.stop()


# Menu lateral
menu = st.sidebar.radio(
    "Navegação",
    [
        "Visão geral",
        "Análise numérica",
        "Análise categórica"
    ]
)


# Página inicial
if menu == "Visão geral":
    c1, c2 = st.columns(2)

    c1.metric(
        "Total de linhas",
        len(df)
    )

    c2.metric(
        "Total de colunas",
        len(df.columns)
    )

    st.subheader("Amostra rápida")

    st.dataframe(
        df.head(10),
        width="stretch"
    )

    st.subheader("Variáveis do dataset")

    st.write(
        ", ".join(df.columns.tolist())
    )


# Página de análise numérica
elif menu == "Análise numérica":
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

    st.subheader(
        f"Estatísticas de {mapa[col]}"
    )

    # Média, mediana e moda
    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Média",
        f"{media(dados):.2f}"
    )

    c2.metric(
        "Mediana",
        f"{mediana(dados):.2f}"
    )

    c3.metric(
        "Moda",
        f"{moda(dados):.2f}"
    )

    # Medidas de dispersão
    c4, c5, c6 = st.columns(3)

    c4.metric(
        "Amplitude",
        f"{amplitude(dados):.2f}"
    )

    c5.metric(
        "Variância",
        f"{variancia_amostral(dados):.2f}"
    )

    c6.metric(
        "Desvio padrão",
        f"{desvio_padrao_amostral(dados):.2f}"
    )

    # Quartis
    c7, c8, c9 = st.columns(3)

    c7.metric(
        "Q1",
        f"{q['Q1']:.2f}"
    )

    c8.metric(
        "Q2 (Mediana)",
        f"{q['Q2']:.2f}"
    )

    c9.metric(
        "Q3",
        f"{q['Q3']:.2f}"
    )

    st.metric(
        "Coeficiente de variação",
        f"{coeficiente_variacao(dados):.2f}%"
    )

        # Tabela de frequências
    st.subheader("Distribuição de frequências")

    if col in ["bmi", "charges"]:
        grupos = pd.cut(df[col], bins=10)
        freq = grupos.value_counts().sort_index()

        classes = []

        for intervalo in freq.index:
            classes.append(
                f"{intervalo.left:.2f} até {intervalo.right:.2f}"
            )

        tabela = pd.DataFrame({
            "Faixa": classes,
            "Quantidade": freq.values
        })

    else:
        freq = df[col].value_counts().sort_index()

        tabela = pd.DataFrame({
            mapa[col]: freq.index,
            "Quantidade": freq.values
        })

    tabela["Percentual"] = (
        tabela["Quantidade"] / len(df) * 100
    ).round(2)

    st.dataframe(
        tabela,
        hide_index=True,
        width="stretch"
    )


    # Gráficos
    st.subheader("Visualização dos dados")

    c1, c2 = st.columns(2)

    # Idade e filhos ficam melhores em gráfico de barras
    if col in ["age", "children"]:
        dados_grafico = (
            df[col]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        dados_grafico.columns = [
            mapa[col],
            "Quantidade"
        ]

        grafico_principal = px.bar(
            dados_grafico,
            x=mapa[col],
            y="Quantidade",
            title=f"Frequência de {mapa[col]}"
        )

    # IMC e custos são contínuos
    else:
        grafico_principal = px.histogram(
            df,
            x=col,
            nbins=15,
            labels={
                col: mapa[col]
            },
            title=f"Distribuição de {mapa[col]}"
        )

    boxplot = px.box(
        df,
        y=col,
        labels={
            col: mapa[col]
        },
        title=f"Boxplot de {mapa[col]}"
    )

    c1.plotly_chart(
        grafico_principal,
        width="stretch"
    )

    c2.plotly_chart(
        boxplot,
        width="stretch"
    )


    # Cálculo dos outliers pelo IQR
    iqr = q["Q3"] - q["Q1"]

    limite_inferior = q["Q1"] - 1.5 * iqr
    limite_superior = q["Q3"] + 1.5 * iqr

    outliers = df[
        (df[col] < limite_inferior)
        | (df[col] > limite_superior)
    ]

    st.subheader("Análise de outliers")

    st.write(
        f"Foram encontrados **{len(outliers)} valores** "
        f"fora dos limites definidos pela regra do IQR."
    )

    st.caption(
        f"Limites calculados: "
        f"{limite_inferior:.2f} até {limite_superior:.2f}"
    )

    if not outliers.empty:
        tabela_outliers = (
            outliers[[col]]
            .head(10)
            .reset_index(drop=True)
        )

        tabela_outliers.columns = [
            mapa[col]
        ]

        st.write("Primeiros valores identificados:")

        st.dataframe(
            tabela_outliers,
            hide_index=True,
            width="stretch"
        )
    # Interpretação da distribuição
    assimetria = (
        3
        * (media(dados) - mediana(dados))
        / desvio_padrao_amostral(dados)
    )

    st.subheader("Interpretação estatística")

    if assimetria > 0.5:
        texto = (
            "Assimetria à direita: valores mais altos "
            "puxam a média para cima."
        )

    elif assimetria < -0.5:
        texto = (
            "Assimetria à esquerda: valores mais baixos "
            "puxam a média para baixo."
        )

    else:
        texto = "Distribuição aproximadamente simétrica."

    st.write(
        f"{texto} "
        f"(coeficiente de assimetria de Pearson: {assimetria:.2f})"
    )

else:
    st.header("Análise de variáveis categóricas")

    nomes = {
        "sex": "Sexo",
        "smoker": "Fumante",
        "region": "Região"
    }

    coluna = st.selectbox(
        "Escolha uma variável:",
        list(nomes.keys()),
        format_func=nomes.get
    )
    
    traducao = {
        "male": "Masculino",
        "female": "Feminino",
        "yes": "Sim",
        "no": "Não",
        "southeast": "Sudeste",
        "southwest": "Sudoeste",
        "northwest": "Noroeste",
        "northeast": "Nordeste"
    }

    # Conta quantas vezes cada categoria aparece
    contagem = df[coluna].value_counts()

    tabela = pd.DataFrame({
        "Categoria": contagem.index,
        "Quantidade": contagem.values
    })

    tabela["Categoria"] = tabela["Categoria"].replace(traducao)


    # Calcula o percentual de cada categoria
    tabela["Percentual"] = (
        tabela["Quantidade"] / len(df) * 100
    ).round(2)

    st.subheader("Tabela de frequências")

    st.dataframe(
        tabela,
        hide_index=True,
        width="stretch"
    )

    # Gráficos
    st.subheader("Gráficos")

    c1, c2 = st.columns(2)

    grafico_barras = px.bar(
        tabela,
        x="Categoria",
        y="Quantidade",
        title=f"Quantidade por {nomes[coluna]}"
    )

    grafico_pizza = px.pie(
        tabela,
        names="Categoria",
        values="Quantidade",
        title=f"Distribuição por {nomes[coluna]}"
    )

    c1.plotly_chart(
        grafico_barras,
        width="stretch"
    )

    c2.plotly_chart(
        grafico_pizza,
        width="stretch"
    )

    # Mostra a categoria que mais aparece
    mais_frequente = tabela.iloc[0]

    st.subheader("Resumo")

    st.write(
        f"A categoria que mais aparece é "
        f"**{mais_frequente['Categoria']}**, com "
        f"**{mais_frequente['Quantidade']} registros** "
        f"({mais_frequente['Percentual']:.2f}% da base)."
    )    