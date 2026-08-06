import numpy as np
import pytest
from scipy import stats

from minhastats import (
    amplitude,
    desvio_padrao_amostral,
    desvio_padrao_populacional,
    media,
    mediana,
    moda,
    percentil,
    quartis,
    variancia_amostral,
    variancia_populacional,
    coeficiente_variacao,
    covariancia,
    correlacao_pearson,
)

# Serve para os testes não quebrarem por arredondamento do float.
TOLERANCIA = 1e-4


def test_media():
    dados = [10, 12, 12, 14, 18]
    esperado = np.mean(dados)
    
    # Usa approx pra garantir que a margem de erro seja respeitada
    assert media(dados) == pytest.approx(esperado, abs=TOLERANCIA)


def test_mediana():
    # Tem que testar par e ímpar porque a lógica de achar o meio é diferente
    dados_impar = [10, 12, 12, 14, 18]
    dados_par = [2, 4, 6, 8]
    
    assert mediana(dados_impar) == np.median(dados_impar)
    assert mediana(dados_par) == np.median(dados_par)


def test_moda():
    dados = [10, 12, 12, 14, 18]
    # O stats.mode retorna um objeto com moda e contagem. O [0] pega só o número da moda.
    esperado = stats.mode(dados)[0]
    
    assert moda(dados) == esperado


def test_moda_com_empate():
    dados = [3, 3, 2, 2, 5]
    # Em caso de empate, pega o menor valor
    esperado = stats.mode(dados)[0]

    assert moda(dados) == esperado


def test_amplitude():
    dados = [10, 12, 12, 14, 18]
    # ptp = peak to peak
    esperado = np.ptp(dados)
    
    assert amplitude(dados) == esperado


def test_variancia_populacional():
    dados = [10, 12, 12, 14, 18]
    # ddof=0 no numpy significa cálculo populacional (sem tirar -1 dos graus de liberdade)
    esperado = np.var(dados, ddof=0)
    
    assert variancia_populacional(dados) == pytest.approx(esperado, abs=TOLERANCIA)


def test_variancia_amostral():
    dados = [10, 12, 12, 14, 18]
    # ddof=1 força o numpy a calcular a amostral (n - 1) igual a nossa função
    esperado = np.var(dados, ddof=1)
    
    assert variancia_amostral(dados) == pytest.approx(esperado, abs=TOLERANCIA)


def test_desvio_padrao_populacional():
    dados = [10, 12, 12, 14, 18]
    esperado = np.std(dados, ddof=0)
    
    assert desvio_padrao_populacional(dados) == pytest.approx(esperado, abs=TOLERANCIA)


def test_desvio_padrao_amostral():
    dados = [10, 12, 12, 14, 18]
    esperado = np.std(dados, ddof=1)
    
    assert desvio_padrao_amostral(dados) == pytest.approx(esperado, abs=TOLERANCIA)


def test_percentil():
    dados = [10, 12, 12, 14, 18]
    # Testando percentis contra o numpy
    assert percentil(dados, 25) == pytest.approx(np.percentile(dados, 25), abs=TOLERANCIA)
    assert percentil(dados, 70) == pytest.approx(np.percentile(dados, 70), abs=TOLERANCIA)


def test_quartis():
    dados = [10, 12, 12, 14, 18]
    resultado = quartis(dados)
    
    # Valida se o dicionário gerado bate com os percentis 25, 50 e 75
    assert resultado["Q1"] == pytest.approx(np.percentile(dados, 25), abs=TOLERANCIA)
    assert resultado["Q2"] == pytest.approx(np.percentile(dados, 50), abs=TOLERANCIA)
    assert resultado["Q3"] == pytest.approx(np.percentile(dados, 75), abs=TOLERANCIA)


def test_percentil_invalido():
    dados = [10, 12, 14]
    # Garante que a trava de segurança barra valores errados
    with pytest.raises(ValueError):
        percentil(dados, -1)
    with pytest.raises(ValueError):
        percentil(dados, 101)


def test_coeficiente_variacao():
    dados = [10, 12, 12, 14, 18]
    esperado = (np.std(dados, ddof=1) / np.mean(dados)) * 100
    
    assert coeficiente_variacao(dados) == pytest.approx(esperado, abs=TOLERANCIA)


def test_covariancia():
    x, y = [18, 25, 30, 40, 50], [2000, 3500, 4200, 6000, 8500]
    
    # ddof=1 pra calcular a covariância amostral igual a nossa função
    esperado = np.cov(x, y, ddof=1)[0][1]
    
    assert covariancia(x, y) == pytest.approx(esperado, abs=TOLERANCIA)


def test_correlacao_pearson():
    x, y = [18, 25, 30, 40, 50], [2000, 3500, 4200, 6000, 8500]
    
    # O corrcoef retorna uma matriz, a correlação x-y está na posição [0][1]
    esperado = np.corrcoef(x, y)[0][1]
    
    assert correlacao_pearson(x, y) == pytest.approx(esperado, abs=TOLERANCIA)