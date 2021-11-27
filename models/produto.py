class Produto:
    def __init__(self, titulo, preço, estoque):
        self._titulo = titulo
        self._preço = preço
        self._estoque = estoque
        
    def getTitulo(self):
        return self._titulo

    def getPreço(self):
        return float(self._preço)

    def getEstoque(self):
        return self._estoque
