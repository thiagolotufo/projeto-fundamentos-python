from models.carrinho import CarrinhoDeCompras
from models.livro import Livro
from models.game import Game
from models.cliente import Cliente
from models.pedido import Pedido

print('1. Criação de 3 clientes diferentes onde um deles tem 2 cartões '
      'de crédito, enquanto os demais apenas um. Os limites dos 4 cartões '
      'devem ser diferentes')

cliente1 = Cliente('Ana', '000.000.000-00', 'ana@espois.com')
cliente1.adicionarCartao('1111 1111 1111 1111', '10/25', 111, 200.00)
cliente1.adicionarCartao('2222 2222 2222 2222', '06/22', 222, 50.00)

cliente2 = Cliente('Carolina', '111.111.111-11', 'carolina@espois.com')
cliente2.adicionarCartao('3333 3333 3333 3333', '10/26', 333, 1500.00)

cliente3 = Cliente('André', '222.222.222-22', 'andre@espois.com')
cliente3.adicionarCartao('4444 4444 4444 4444', '10/26', 444, 2500.00)

print(cliente1.getNome())
print(cliente1.getCartao()[0].getNumero())
print(cliente1.getCartao()[1].getNumero())
print(cliente2.getNome())
print(cliente2.getCartao()[0].getNumero())
print(cliente3.getNome())
print(cliente3.getCartao()[0].getNumero())

print('')
########################

print('2. Criação de 4 produtos: 2 livros e 2 games')
game1 = Game('EA Sports', 'Fifa 2021', 249.99, 5)
game2 = Game('EA', 'The Sims', 99.99, 0)

livro1 = Livro('4534631', 'Allan Ribeiro', 'Python 3.0', 49.99, 10)
livro2 = Livro('9184792', 'Machado de Assis', 'Dom Casmurro', 14.99, 50)

print(game1.getTitulo())
print(game1.getPreco())
print(game2.getTitulo())
print(game2.getPreco())

print(livro1.getTitulo())
print(livro1.getAutor())
print(livro2.getTitulo())
print(livro2.getAutor())

print('')
########################

print('3. O cliente com dois cartões faz 2 pedidos: um com um livro e um game, '
      'e outro com 2 livros')

carrinho1 = CarrinhoDeCompras()
carrinho1.inserirProduto(game1)
carrinho1.inserirProduto(livro2)

print(carrinho1.getProduto()[0].getTitulo())
print(carrinho1.getProduto()[0].getPreco())
print(carrinho1.getProduto()[1].getTitulo())
print(carrinho1.getProduto()[1].getPreco())

pedido1 = Pedido(cliente1, carrinho1.getProduto(), carrinho1.somaTotal())
print('Cliente: ' + str(pedido1.getCliente().getNome()))
print('Valor total: ' + str(pedido1.getValorTotal()))

carrinho2 = CarrinhoDeCompras()
carrinho2.inserirProduto(livro1)
carrinho2.inserirProduto(livro2)

print(carrinho2.getProduto()[0].getTitulo())
print(carrinho2.getProduto()[0].getPreco())
print(carrinho2.getProduto()[1].getTitulo())
print(carrinho2.getProduto()[1].getPreco())

pedido2 = Pedido(cliente1, carrinho2.getProduto(), carrinho2.somaTotal())
print('Cliente: ' + str(pedido2.getCliente().getNome()))
print('Valor total: ' + str(pedido2.getValorTotal()))

print('')
########################

print('4. Os outros clientes devem fazer 1 pedido cada com 1 livro ou 1 game')

carrinho3 = CarrinhoDeCompras()
carrinho3.inserirProduto(game1)
print(carrinho3.getProduto()[0].getTitulo())
print(carrinho3.getProduto()[0].getPreco())
pedido3 = Pedido(cliente2, carrinho3.getProduto(), carrinho3.somaTotal())
print('Cliente: ' + str(pedido3.getCliente().getNome()))
print('Valor total: ' + str(pedido3.getValorTotal()))

carrinho4 = CarrinhoDeCompras()
carrinho4.inserirProduto(game2)
print(carrinho4.getProduto()[0].getTitulo())
print(carrinho4.getProduto()[0].getPreco())
pedido4 = Pedido(cliente3, carrinho4.getProduto(), carrinho4.somaTotal())
print('Cliente: ' + str(pedido4.getCliente().getNome()))
print('Valor total: ' + str(pedido4.getValorTotal()))

print('')
########################

print('5. Mostre um cenário onde o pedido de um dos clientes não é efetivado por falta de limite no cartão')

print('Cliente: ' + str(pedido2.getCliente().getNome()))
print('Valor total: ' + str(pedido2.getValorTotal()))
pedido2 = carrinho2.finalizarCompra(cliente1.getCartao()[1], cliente1)
print('Limite do cartão: ' + str(cliente1.getCartao()[1].getLimite()))

print('')
########################

print('6. Mostre um cenário onde o pedido de um dos clientes não é efetivado por falta do produto no estoque')

print('Cliente: ' + str(pedido4.getCliente().getNome()))
print('Valor total: ' + str(pedido4.getValorTotal()))
pedido4 = carrinho4.finalizarCompra(cliente3.getCartao()[0], cliente3)
print(game2.getTitulo())
print(game2.validarEstoque())

print('')
########################

print('7. Mostre um cenário onde o pedido do cliente com mais cartões é efetivado corretamente')

print('Cliente: ' + str(pedido3.getCliente().getNome()))
print('Produto: ' + str(pedido3.getItens()))
print('Valor total: ' + str(pedido3.getValorTotal()))
pedido3 = carrinho3.finalizarCompra(cliente3.getCartao()[0], cliente3)
