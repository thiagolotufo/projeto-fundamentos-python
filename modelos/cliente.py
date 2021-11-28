class Cliente:
  def __init__(self, nome, cpf, email):
    self._nome = nome
    self._cpf = cpf
    self._email = email
    self._cartoescredito = []

  def getNome(self):
    return self._nome

  def getCPF(self):
    return self._cpf

  def getEmail(self):
    return self._email

  def getCartao(self):
    return self._cartoescredito

  def adicionarCartao(self, numero, data_validade, cvv, limite)
    cartao = Cartao_Credito (numero, data_validade, cvv, limite, self._nome)
    self._cartoescredito.append(cartao)
    
      
  
 
