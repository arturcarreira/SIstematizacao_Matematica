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
    variancia_amostral,
    variancia_populacional,
)

# Tolerância numérica (1e-4) documentada conforme exigência do Módulo 1.
# Serve para os testes não quebrarem por arredondamento do float.
TOLERANCIA = 1e-4


def test_media():
    dados = [10, 12, 12, 14, 18]
    esperado = np.mean(dados)
    
    # Usa approx pra garantir que a margem de erro seja respeitada
    assert media(dados) == pytest.approx(esperado, abs=TOLERANCIA)


def test_mediana():
    # Tem que testar par e ímpar porque a lógica de achar o meio muda
    dados_impar = [10, 12, 12, 14, 18]
    dados_par = [2, 4, 6, 8]
    
    assert mediana(dados_impar) == np.median(dados_impar)
    assert mediana(dados_par) == np.median(dados_par)


def test_moda():
    dados = [10, 12, 12, 14, 18]
    # O stats.mode retorna um objeto com moda e contagem. O [0] pega só o número da moda.
    esperado = stats.mode(dados)[0]
    
    assert moda(dados) == esperado


def test_amplitude():
    dados = [10, 12, 12, 14, 18]
    # ptp = peak to peak (é a função de amplitude no numpy)
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

def test_moda_com_empate():
    dados = [3, 3, 2, 2, 5]

    esperado = stats.mode(
        dados,
        keepdims=False
    ).mode

    assert moda(dados) == esperado