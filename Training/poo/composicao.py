# Quando determindo atributo de uma class

from endereco import Endereco

class Pessso:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = Endereco()

    def recebe_endereco(self, endereco:Endereco):
        pass