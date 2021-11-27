from Produto import Produto

class Game(Produto):
    def __init__(self, titulo, empresa, preço, estoque = 100):
        Produto.__init__(self, titulo, preço, estoque)
        self._titulo = titulo
        self._empresa = empresa
        self._preço = preço
        
    def getTitulo(self):
        return self._titulo

    def getEmpresa(self):
        return self._empresa

    def getPreço(self):
        return float(self._preço)

    def getEstoque(self):
        return self._estoque

    def __str__(self):
        return "Título: " + self.getTitulo() + ","+" Empresa: " + self.getEmpresa()+ "," + " Preço: " + str(self.getPreço())