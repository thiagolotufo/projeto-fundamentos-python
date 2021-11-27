from Livro import Livro
from Game import Game

l1 = Livro(2121, "Senhor dos Anéis", "Tolkien", 40)
l2 = Livro(3232, "Harry Potter", "JK Rowling", 45)

g1 = Game("Need for Speed","EA", 22)
g2 = Game("The Sims","EA", 30)


print(l1.getEstoque())
print(l2.getEstoque())
print(g1.getEstoque())
print(g2.getEstoque())
print(g1.getTitulo())
print(g2.getPreço())

print(l2.getPreço())

print(l1)
print(l2)
print(g1)
print(g2)