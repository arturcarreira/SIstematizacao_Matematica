import numpy as np
import pytest
from scipy import stats

from minhastats import amplitude, media, mediana, moda


TOLERANCIA = 1e-4

def test_media():
    dados = [10, 12, 12, 14, 18]
    esperado = np.mean(dados)
    assert media(dados) == pytest.approx(esperado, abs=TOLERANCIA)

def test_mediana():
    dados_impar = [10, 12, 12, 14, 18]
    dados_par = [2, 4, 6, 8]
    
    assert mediana(dados_impar) == np.median(dados_impar)
    assert mediana(dados_par) == np.median(dados_par)

def test_moda():
    dados = [10, 12, 12, 14, 18]
    esperado = stats.mode(dados)[0]
    
    assert moda(dados) == esperado


def test_amplitude():
    dados = [10, 12, 12, 14, 18]
    esperado = np.ptp(dados)
    
    assert amplitude(dados) == esperado