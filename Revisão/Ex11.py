from Ex8 import Pessoa
from Ex10 import Endereco


class PessoaFisica(Pessoa):
    def __init__(self):
        self.__cpf = ""

    def get_cpf(self)->str:
        return self.__cpf

    def set_nome(self, cpf:str)->None:
        self.__cpf = cpf

    def cadastro(self, nome:str, sobrenome:str, idade:int, endereco:Endereco, cpf:str):
        self.__cpf = cpf
        super().cadastro(nome, sobrenome, idade, endereco)

p = PessoaFisica()
p.cadastro("Gustavo", "Suzuki", 18, Endereco(), "089.878.399-23")
print(p.get_nome())
print(p.get_sobrenome())
print(p.get_idade())
print(p.get_cpf())
