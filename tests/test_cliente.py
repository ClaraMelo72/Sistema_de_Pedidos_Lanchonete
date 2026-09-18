import pytest
from src.cliente import Cliente


def test_criar_cliente_valido():
    cliente = Cliente("Ana Souza")
    assert cliente.nome == "Ana Souza"


def test_nome_vazio():
    with pytest.raises(ValueError):
        Cliente("")


def test_nome_curto():
    with pytest.raises(ValueError):
        Cliente("Jo")