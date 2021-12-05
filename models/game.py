from models.produto import Produto

class Game(Produto):
    def __init__(self, empresa, titulo, preco, estoque):
        Produto.__init__(self, titulo, preco, estoque)
        self._empresa = empresa
        
    def getTitulo(self):
        return self._titulo

    def getEmpresa(self):
        return self._empresa

    def getPreco(self):
        return float(self._preco)

    def getEstoque(self):
        return self._estoque