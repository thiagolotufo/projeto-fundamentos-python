class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def inserirProduto(self, produto):
        self._produtos.append(produto)

    def removerProduto(self, produto):
        self._produtos.remove(produto)

    def limparProdutos(self):
        self._produtos.clear()

    def listarProduto(self):
        for produto in self._produtos:
            print(produto.nome, produto.valor)
        return self._produtos

    def somaTotal(self):
        total = 0
        for produto in self._produtos:
            total += produto.valor
        return total

    # finalizarCompra(): gera o pedido e tenta faturá-lo