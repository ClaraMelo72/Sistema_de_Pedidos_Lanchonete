def calcular_desconto(subtotal: float) -> float:
    if subtotal < 0:
        raise ValueError("Subtotal não pode ser negativo.")
    return subtotal * 0.1 if subtotal > 100 else 0


def calcular_valor_final(subtotal: float) -> float:
    desconto = calcular_desconto(subtotal)
    return subtotal - desconto