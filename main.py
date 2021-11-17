from models.cartao_credito import Cartao_Credito

cartao = Cartao_Credito(123456, 1025, 123, 5000)

print(cartao.get_numero())
print(cartao.get_data_validade())
print(cartao.get_limite())
print(cartao.set_limite(10000))
print(cartao.debitar(11000))
print(cartao.get_limite())
print(cartao.estornar(4000))
print(cartao.get_limite())