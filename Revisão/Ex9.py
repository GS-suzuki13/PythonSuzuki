# Crie um objeto da classe pessoa
# Altere o valor dos dois atributos
# Imprima os valores de atributos
# nome = input("Digite um nome para ser alterado: ")
# sobrenome = input("Digite um sobrenome para ser alterado: ")
#
#
# class Pessoa:
#     def __init__(self, nome:str, sobrenome:str):
#         self.__nome = " "
#         self.__sobrenome = " "
#
#     def alterar_nome(self, nome:str):
#         self.__nome = nome
#         return print(f"O nome, {self.__nome}, foi alterado com sucesso")
#
#     def alterar_sobrenome(self, sobrenome:str):
#         self.__sobrenome = sobrenome
#         return print(f"O sobrenome, {self.__sobrenome}, foi alterado com sucesso")
#
#
# pessoa = Pessoa(nome, sobrenome)
# pessoa.alterar_nome(nome)
# pessoa.alterar_sobrenome(sobrenome)
from Ex8 import Pessoa
from Ex10 import Endereco


e = Endereco()
p = Pessoa()
print(""""\n
==== PESSOA ====""")

p.set_nome("Gustavo")
p.set_sobrenome("Suzuki")
p.set_idade(18)
print(f"Nome: {p.get_nome()}")
print(f"Sobrenome: {p.get_sobrenome()}")
print(f"Idade: {p.get_idade()}")

print("""\n
==== ENDEREÇO ====""")


e.set_logradouro("23 de Outubro")
e.set_numero("158")
e.set_bairro("Itoupava Norte")
print(f"Rua: {e.get_logradouro()}")
print(f"Número: {e.get_numero()}")
print(f"Bairro: {e.get_bairro()}")