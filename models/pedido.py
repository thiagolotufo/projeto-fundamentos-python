from random import randint

class Pedido:
    def __init__(self, cliente, itens, valor_total):
        self._numero = randint(1000, 2000)
        self._cliente = cliente
        self._itens = itens
        self._valor_total = valor_total
        self._status_pagamento = False

    def getNumero(self):
        return self._numero

    def getCliente(self):
        return self._cliente

    def getItens(self):
        for item in self._itens:
            print(item.getTitulo())
        return self._itens

    def getValorTotal(self):
        return self._valor_total

    def getStatusPagamento(self):
        return self._status_pagamento

    def setStatusPagamento(self, status):
        self._status_pagamento = status
        return True

    def faturarPedido(self, cartao_credito):
        if cartao_credito.debitar(self._valor_total):
            self.setStatusPagamento(status=True)
            return True
        else:
            return False

    def estornar(self, pedido):
        if self.getNumero() == pedido.getNumero():
            self.setStatusPagamento(status=False)
            return True
        return False