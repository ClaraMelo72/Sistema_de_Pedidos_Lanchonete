from enum import Enum
from src.desconto import calcular_valor_final


class StatusPedido(str, Enum):
    CRIADO = "CRIADO"
    EM_PREPARACAO = "EM_PREPARACAO"
    PRONTO = "PRONTO"
    ENTREGUE = "ENTREGUE"
    CANCELADO = "CANCELADO"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.status = StatusPedido.CRIADO

    def adicionar_produto(self, nome: str, preco: float, quantidade: int):
        if preco < 0 or quantidade < 0:
            raise ValueError("Preço ou quantidade não podem ser negativos.")
        self.itens.append({"nome": nome, "preco": preco, "quantidade": quantidade})

    def calcular_subtotal(self) -> float:
        if not self.itens:
            raise ValueError("O pedido precisa ter ao menos um produto.")
        return sum(item["preco"] * item["quantidade"] for item in self.itens)

    def calcular_valor_final(self) -> float:
        subtotal = self.calcular_subtotal()
        return calcular_valor_final(subtotal)

    def alterar_status(self, novo_status: StatusPedido):
        if self.status == StatusPedido.ENTREGUE and novo_status == StatusPedido.CANCELADO:
            raise ValueError("Pedido entregue não pode ser cancelado.")
        if novo_status == StatusPedido.ENTREGUE and self.status != StatusPedido.PRONTO:
            raise ValueError("Pedido só pode ser marcado como ENTREGUE após estar PRONTO.")
        self.status = novo_status

    def consultar_status(self) -> StatusPedido:
        return self.status