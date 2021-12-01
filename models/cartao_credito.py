class CartaoCredito:
    def __init__(self, numero, data_validade, cvv, limite):
        self._numero = numero
        self._data_validade = data_validade
        self._cvv = cvv
        self._limite = limite

    def getNumero(self):
        return self._numero

    def getDataValidade(self):
        return self._data_validade

    def getCvv(self):
        return self._cvv
    
    def getLimite(self):
        return self._limite

    def setLimite(self, limite):
        self._limite = limite
        return True

    def debitar(self, valor):
        if valor <= self.getLimite():
            valor_debitar = self.getLimite() - valor
            self.setLimite(valor_debitar)
            return True
        else: 
            return False

    def estornar(self, valor):
        valor_estornar = self.getLimite() + valor
        self.setLimite(valor_estornar)
        return True