
from math import sqrt

def media(valores):
    soma = 0
    for v in valores:
        soma += v
    return soma / len(valores)


def mediana(valores):
    dados = sorted(valores)
    n = len(dados)
    meio = n // 2

    if n % 2 != 0:
        return dados[meio]
    else:
        return (dados[meio - 1] + dados[meio]) / 2

def moda(valores):
    freq = {}

    for v in valores:
        if v in freq:
            freq[v] += 1
        else:
            freq[v] = 1

    maior_frequencia = 0
    resultado = None

    for chave, quantidade in freq.items():
        if quantidade > maior_frequencia:
            maior_frequencia = quantidade
            resultado = chave

        elif quantidade == maior_frequencia and chave < resultado:
            resultado = chave

    return resultado

def amplitude(valores):
    menor = valores[0]
    maior = valores[0]

    for v in valores:
        if v < menor:
            menor = v
        if v > maior:
            maior = v

    return maior - menor


def variancia_populacional(valores):
    m = media(valores)
    soma_desvios = 0
    
    for v in valores:
        soma_desvios += (v - m) ** 2

    return soma_desvios / len(valores)


def variancia_amostral(valores):
    if len(valores) < 2:
        raise ValueError(
            "A variância amostral exige pelo menos dois valores."
        )

    m = media(valores)
    soma_desvios = 0

    for v in valores:
        soma_desvios += (v - m) ** 2

    return soma_desvios / (len(valores) - 1)


def desvio_padrao_populacional(valores):
    return sqrt(variancia_populacional(valores))


def desvio_padrao_amostral(valores):
    return sqrt(variancia_amostral(valores))

def percentil(valores, p):
    # Trava básica pra evitar percentual errado
    if not (0 <= p <= 100):
        raise ValueError("O percentual tem que ser de 0 a 100")

    dados = sorted(valores)
    n = len(dados)
    
    # Fórmula da posição
    pos = (n - 1) * (p / 100)
    
    idx_inf = int(pos)
    idx_sup = idx_inf + 1

    # Se caiu exatamente no último índice da lista, retorna ele direto
    if idx_sup >= n:
        return dados[idx_inf]

    # Interpolação entre os dois valores mais próximos
    decimal = pos - idx_inf
    v_inf = dados[idx_inf]
    v_sup = dados[idx_sup]

    return v_inf + (v_sup - v_inf) * decimal


def quartis(valores):
    # Q1 (25%), Q2/Mediana (50%), Q3 (75%)
    return {
        "Q1": percentil(valores, 25),
        "Q2": percentil(valores, 50),
        "Q3": percentil(valores, 75)
    }