from Produto import Produto

class Livro(Produto):
    def __init__(self, isbn, titulo, autor, preço, estoque = 300):
        Produto.__init__(self, titulo, preço, estoque)
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        self._preço = preço
       
    def getIsbn(self):
        return self._isbn

    def getTitulo(self):
        return self._titulo

    def getAutor(self):
        return self._autor

    def getPreço(self):
        return float(self._preço)

    def getEstoque(self):
        return self._estoque

    def __str__(self):
        return "Isbn: "+ str(self.getIsbn()) + "," + " Título: "+self.getTitulo() + "," + " Autor: " + self.getAutor() + "," +" Preço: "+ str(self.getPreço())

    