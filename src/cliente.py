class Cliente:
    def __init__(self, nome: str):
        if not nome or len(nome.strip()) < 3:
            raise ValueError("Nome do cliente inválido: deve ter pelo menos 3 caracteres.")
        self.nome = nome