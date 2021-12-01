class Produto:
    def __init__(self, titulo, preco, estoque):
        self._titulo = titulo
        self._preco = preco
        self._estoque = estoque
        
    def getTitulo(self):
        return self._titulo

    def getPreco(self):
        return float(self._preco)

    def getEstoque(self):
        return self._estoque