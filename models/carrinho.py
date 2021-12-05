from models.pedido import Pedido

class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def getProduto(self):
        return self._produtos

    def inserirProduto(self, produto):
        self._produtos.append(produto)

    def removerProduto(self, produto):
        self._produtos.remove(produto)

    def limparProdutos(self):
        self._produtos.clear()

    def listarProduto(self):
        for produto in self._produtos:
            print(produto.getTitulo(), produto.getPreco())
        return self._produtos

    def somaTotal(self):
        total = 0
        for produto in self._produtos:
            total += produto.getPreco()
        return total

    def finalizarCompra(self, cartao_credito, cliente):
        pedido = Pedido(cliente, self.getProduto(), self.somaTotal())
        estoque = self.getProduto()[0].validarEstoque()
        if pedido.faturarPedido(cartao_credito) and estoque:
            print("Pagamento Aprovado")
            return True
        else:
            print("Pagamento Reprovado")
            return False