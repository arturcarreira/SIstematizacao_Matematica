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