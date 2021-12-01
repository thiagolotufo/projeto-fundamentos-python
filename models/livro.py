from models.produto import Produto

class Livro(Produto):
    def __init__(self, isbn, autor, titulo, preco, estoque = 300):
        Produto.__init__(self, titulo, preco, estoque)
        self._isbn = isbn
        self._autor = autor
       
    def getIsbn(self):
        return self._isbn
    
    def getAutor(self):
        return self._autor

    def getTitulo(self):
        return self._titulo

    def getPreco(self):
        return float(self._preco)

    def getEstoque(self):
        return self._estoque