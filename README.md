# Sistema de Pedidos - Lanchonete

## Sobre o projeto

Projeto desenvolvido para a disciplina de Verificação e Validação de Software, como exercício de aplicação de testes automatizados sobre regras de negócio.

- **Faculdade:** Faculdade Senac PE
- **Disciplina:** Verificação e Validação de Software
- **Professor:** Pedro Lins
- **Aluno:** Maria Clara

## O que o sistema faz

Simula o fluxo de atendimento de uma lanchonete, permitindo:

1. Cadastrar cliente
2. Criar pedido
3. Adicionar produtos ao pedido
4. Calcular subtotal e valor final (com desconto, quando aplicável)
5. Consultar e alterar o status do pedido

Feito em Python puro, sem framework — só `pytest` para os testes.

## Cardápio

| Item         | Valor    |
|--------------|----------|
| Hambúrguer   | R$ 20,00 |
| Batata       | R$ 10,00 |
| Refrigerante | R$ 7,00  |
| Sobremesa    | R$ 8,00  |

## Regras validadas por teste

- Nome de cliente vazio ou com menos de 3 caracteres → rejeitado
- Pedido sem nenhum produto → não permite calcular subtotal
- Preço acima de R$ 100 → aplica 10% de desconto automaticamente
- Preço ou quantidade negativos → rejeitados em qualquer ponto do fluxo
- Pedido `ENTREGUE` → não pode voltar para `CANCELADO`
- Pedido só vira `ENTREGUE` se já estiver `PRONTO`

## Rodando localmente

```bash
pip install -r requirements.txt
pytest -v
```

Saída esperada: todos os testes de `tests/test_cliente.py`, `tests/test_desconto.py` e `tests/test_pedido.py` passando.

## Organização das pastas

```
projeto-testes/
├── src/
│   ├── __init__.py
│   ├── cliente.py
│   ├── pedido.py
│   └── desconto.py
├── tests/
│   ├── __init__.py
│   ├── test_cliente.py
│   ├── test_pedido.py
│   └── test_desconto.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Testes automatizados

14 casos de teste, organizados em três arquivos — um por classe.

### `tests/test_cliente.py` (RN01)

- Nome válido é aceito
- Nome vazio é rejeitado
- Nome com menos de 3 caracteres é rejeitado

### `tests/test_desconto.py` (RN03, RN04)

- Subtotal até R$ 100 não recebe desconto (testa o limite)
- Subtotal acima de R$ 100 recebe 10% de desconto
- Valor final é calculado corretamente com e sem desconto
- Subtotal negativo é rejeitado

### `tests/test_pedido.py` (RN02, RN04, RN06, RN07)

- Pedido sem produtos não calcula subtotal
- Produtos adicionados somam corretamente o subtotal
- Preço ou quantidade negativos são rejeitados
- Pedido acima de R$ 100 já reflete o desconto no valor final
- Pedido `ENTREGUE` não pode virar `CANCELADO`
- Pedido não pode virar `ENTREGUE` sem antes estar `PRONTO`
- Pedido novo começa com status `CRIADO`

### Rodando

```bash
pytest -v
```

Cada regra de negócio é validada com `pytest.raises(ValueError)` (entradas inválidas) ou `assert` (cálculos e status esperados).

### Exemplo de uso

Execute o exemplo em um interpretador Python iniciado na raiz do projeto:

```python
from src.cliente import Cliente
from src.pedido import Pedido, StatusPedido

pedido = Pedido(Cliente("Mariana Costa"))
pedido.adicionar_produto("Hamburguer", 20, 4)
pedido.adicionar_produto("Sobremesa", 8, 2)

print(pedido.calcular_subtotal())     # 96.0
print(pedido.calcular_valor_final())  # 96.0 (sem desconto, pois não passa de R$ 100)
print(pedido.consultar_status())      # StatusPedido.CRIADO

pedido.alterar_status(StatusPedido.EM_PREPARACAO)
pedido.alterar_status(StatusPedido.PRONTO)
pedido.alterar_status(StatusPedido.ENTREGUE)
print(pedido.consultar_status())      # StatusPedido.ENTREGUE

