from random import randint

class Pedido:
    def __init__(self, cliente, itens, valor_total):
        self._numero = randint(1000,2000)
        self._cliente = cliente
        self._itens = itens
        self._valor_total = valor_total
        self._status_pagamento = False

    def get_numero(self):
        return self._numero

    def get_cliente(self):
        return self._cliente
    
    def get_itens(self):
        return self._itens

    def get_status_pagamento(self):
        return self._status_pagamento

    def set_status_pagamento(self):
        self._status_pagamento = True
        return True

    def faturar_pedido(self, cartao_credito):
        if cartao_credito.debitar(self._valor_total):
            self.set_status_pagamento()
            return True
        else:
            return False
