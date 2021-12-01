from models.cartao_credito import CartaoCredito
from models.pedido import Pedido
from models.livro import Livro
from models.game import Game
from models.cliente import Cliente

# Criação de 3 clientes diferentes onde um deles tem 2 cartões de crédito, enquanto os demais apenas um.
# Os limites dos 4 cartões devem ser diferentes

cartao1 = CartaoCredito(1111111111, '10/25', 123, 5000)
cartao2 = CartaoCredito(2222222222, '06/22', 321, 25000)
cliente1 = Cliente('Ana', '10076695786', 'ana@espois.com')

print(cliente1.getCartao())
print(cartao1.getNumero())


# Criação de 4 produtos: 2 livros e 2 games

game1 = Game('EA Sports', 'Fifa 2021', 250)
game2 = Game('EA', 'The Sims', 99)

livro1 = Livro('4534631', 'Allan Ribeiro', 'Python 3.0', 50)
livro2 = Livro('9184792', 'Machado de Assis', 'Dom Casmurro', 15)

print(game1.getTitulo())
print(game2.getPreco())

print(livro1.getTitulo())
print(livro2.getAutor())


# O cliente com dois cartões faz 2 pedidos: um com um livro e um game, e outro com 2 livros



# Os outros clientes devem fazer 1 pedido cada com 1 livro ou 1 game




# Mostre um cenário onde o pedido de um dos clientes não é efetivado por falta de limite no cartão




# Mostre um cenário onde o pedido de um dos clientes não é efetivado por falta do produto no estoque




# Mostre um cenário onde o pedido do cliente com mais cartões é efetivado corretamente




"""
fifa = Game('EA Sports', 'Fifa 2021', 100)
fifa.getTitulo()

ana = Cliente('Ana', '10076695786', 36)
pedido = Pedido(ana, fifa, 5)
print(pedido.getIValorTotal())
print(pedido.getCliente().getNome())
print(fifa.getEstoque())

python = Livro('Python 3.0', '12345', 'Allan Ribeiro', 50)
python.getTitulo()

carol = Cliente('Carolina', '10076695786', 25)
pedido2 = Pedido(carol, python, 1)
print(pedido2.getIValorTotal())
print(pedido2.getCliente().getNome())
print(python.getEstoque())

cartao = CartaoCredito(123456, '10/25', 123, 5000)
print(cartao.getNumero())
print(cartao.getDataValidade())
print(cartao.getLimite())
print(cartao.setLimite(10000))
print(cartao.debitar(11000))
print(cartao.getLimite())
print(cartao.estornar(4000))
print(cartao.getLimite())

pedido = Pedido("Thiago Silva", "Hamburguer", 1400)
pedido1 = Pedido("Nicole Roale", "Pizza", 1000)

print(pedido.getCliente())
print(pedido.getItens())
print(pedido.getIValorTotal())

print('Pedido: ' + str(pedido.faturarPedido(cartao)))
print('Estornar Pedido :' + str(pedido.estornar(pedido)))
print('Estornar Pedido :' + str(pedido.estornar(pedido1)))
"""