from models.pedido import Pedido

class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def getProduto(self):
        return self._produtos

    def inserir_produto(self, produto):
        self._produtos.append(produto)

    def remover_produto(self, produto):
        self._produtos.remove(produto)

    def limpar_produtos(self):
        self._produtos.clear()

    def listar_produto(self):
        for produto in self._produtos:
            print(produto.nome, produto.valor)
        return self._produtos
    
    def soma_total(self):
        total = 0
        for produto in self._produtos:
            total += produto.valor
        return total

    def finalizarCompra(self, cartao_credito, cliente):
        pedido = Pedido(cliente, self.getProduto(), self.soma_total())
        if pedido.faturarPedido(cartao_credito):
            print("Pagamento Aprovado")
            return True
        else:	
	        return False