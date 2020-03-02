# Crie um objeto da classe pessoa
# Altere o valor dos dois atributos
# Imprima os valores de atributos
nome = input("Digite um nome para ser alterado: ")
sobrenome = input("Digite um sobrenome para ser alterado: ")


class Pessoa:
    def __init__(self, nome:str, sobrenome:str):
        self.__nome = " "
        self.__sobrenome = " "

    def alterar_nome(self, nome:str):
        self.__nome = nome
        return print(f"O nome, {self.__nome}, foi alterado com sucesso")

    def alterar_sobrenome(self, sobrenome:str):
        self.__sobrenome = sobrenome
        return print(f"O sobrenome, {self.__sobrenome}, foi alterado com sucesso")


pessoa = Pessoa(nome, sobrenome)
pessoa.alterar_nome(nome)
pessoa.alterar_sobrenome(sobrenome)