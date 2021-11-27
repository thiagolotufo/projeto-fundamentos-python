class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

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
