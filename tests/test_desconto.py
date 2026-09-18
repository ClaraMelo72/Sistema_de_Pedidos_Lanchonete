import pytest
from src.desconto import calcular_desconto, calcular_valor_final


def test_sem_desconto_ate_100():
    assert calcular_desconto(100) == 0
    assert calcular_desconto(50) == 0


def test_desconto_acima_de_100():
    assert calcular_desconto(200) == 20


def test_valor_final():
    assert calcular_valor_final(200) == 180
    assert calcular_valor_final(50) == 50


def test_subtotal_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-10)