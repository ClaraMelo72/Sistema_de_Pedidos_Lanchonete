import pytest
from src.pedido import Pedido, StatusPedido
from src.cliente import Cliente


@pytest.fixture
def cliente():
    return Cliente("Carlos Silva")


def test_subtotal_sem_produtos(cliente):
    pedido = Pedido(cliente)
    with pytest.raises(ValueError):
        pedido.calcular_subtotal()


def test_adicionar_produtos_e_calcular_subtotal(cliente):
    pedido = Pedido(cliente)
    pedido.adicionar_produto("Hambúrguer", 20, 2)
    pedido.adicionar_produto("Refrigerante", 7, 1)
    assert pedido.calcular_subtotal() == 47


def test_preco_ou_quantidade_negativos(cliente):
    pedido = Pedido(cliente)
    with pytest.raises(ValueError):
        pedido.adicionar_produto("Batata", -10, 1)
    with pytest.raises(ValueError):
        pedido.adicionar_produto("Batata", 10, -1)


def test_valor_final_com_desconto(cliente):
    pedido = Pedido(cliente)
    pedido.adicionar_produto("Hambúrguer", 20, 6)  # subtotal = 120
    assert pedido.calcular_valor_final() == 108


def test_nao_cancelar_pedido_entregue(cliente):
    pedido = Pedido(cliente)
    pedido.adicionar_produto("Hambúrguer", 20, 1)
    pedido.alterar_status(StatusPedido.EM_PREPARACAO)
    pedido.alterar_status(StatusPedido.PRONTO)
    pedido.alterar_status(StatusPedido.ENTREGUE)
    with pytest.raises(ValueError):
        pedido.alterar_status(StatusPedido.CANCELADO)


def test_nao_entregar_sem_estar_pronto(cliente):
    pedido = Pedido(cliente)
    pedido.adicionar_produto("Hambúrguer", 20, 1)
    with pytest.raises(ValueError):
        pedido.alterar_status(StatusPedido.ENTREGUE)


def test_consultar_status(cliente):
    pedido = Pedido(cliente)
    assert pedido.consultar_status() == StatusPedido.CRIADO