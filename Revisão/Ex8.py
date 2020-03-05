# Crie uma classe pessoa
# Crie dois atributos para a classe: Nome, Sobrenome
# Crie 4 comportamentos:
#         1 - get_nome(): - > Não Implementado
#         2 - get_sobrenome(): - > Não Implementado
#         3 - set_nome(): - > Não Implementado
#         4 - set_nome(): - > Não Implementado
from Ex10 import Endereco


class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__sobrenome = ""
        self.__idade = 0
        self.__endereco = Endereco()

    def get_nome(self)->str:
        return self.__nome

    def get_sobrenome(self)->str:
        return self.__sobrenome

    def get_idade(self)->int:
        return self.__idade

    def get_endereco(self)->Endereco:
        return self.__endereco

    def set_endereco(self, endereco:Endereco)->None:
        self.__endereco = Endereco

    def set_nome(self, nome:str)->None:
        self.__nome = nome

    def set_sobrenome(self, sobrenome:str)->None:
        self.__sobrenome = sobrenome

    def set_idade(self, idade:int)->None:
        self.__idade = idade

    def cadastro(self, nome:str, sobrenome:str, idade:int, endereco:Endereco):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__endereco = endereco