from models.cartao_credito import Cartao_Credito
from models.pedido import Pedido
from Livro import Livro
from Game import Game

cartao = Cartao_Credito(123456, 1025, 123, 5000)

print(cartao.get_numero())
print(cartao.get_data_validade())
print(cartao.get_limite())
print(cartao.set_limite(10000))
print(cartao.debitar(11000))
print(cartao.get_limite())
print(cartao.estornar(4000))
print(cartao.get_limite())

pedido = Pedido("Thiago Silva", "Hamburguer", 1400)
pedido1 = Pedido("Nicole Roale", "Pizza", 1000)

print(pedido.get_cliente())
print(pedido.get_itens())
print(pedido.get_numero())

print('Pedido: ' + str(pedido.faturar_pedido(cartao)))
print('Estornar Pedido :' + str(pedido.estornar(pedido)))
print('Estornar Pedido :' + str(pedido.estornar(pedido1)))


l1 = Livro(2121, "Senhor dos Anéis", "Tolkien", 40)
l2 = Livro(3232, "Harry Potter", "JK Rowling", 45)

g1 = Game("Need for Speed","EA", 22)
g2 = Game("The Sims","EA", 30)


print(l1.getEstoque())
print(l2.getEstoque())
print(g1.getEstoque())
print(g2.getEstoque())
print(g1.getTitulo())
print(g2.getPreço())

print(l2.getPreço())

print(l1)
print(l2)
print(g1)
print(g2)