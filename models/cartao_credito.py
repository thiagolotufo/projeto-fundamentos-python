class Cartao_Credito:
    def __init__(self, numero, data_validade, cvv, limite):
        self._numero = numero
        self._data_validade = data_validade
        self._cvv = cvv
        self._limite = limite

    def get_numero(self):
        return self._numero

    def get_data_validade(self):
        return self._data_validade
    
    def get_limite(self):
        return self._limite

    def set_limite(self, limite):
        self._limite = limite
        return True

    def debitar(self, valor):
        if valor <= self.get_limite():
            valor_debitar = self.get_limite() - valor
            self.set_limite(valor_debitar)
            return True
        else: 
            return False

    def estornar(self, valor):
        valor_estornar = self.get_limite() + valor
        self.set_limite(valor_estornar)
        return True