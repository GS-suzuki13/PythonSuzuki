# São os elementos que definem a estrutura de uma classe,
# representão caracteristicas ou estados da classe
# e são as váriaveis da classe

class Pessoa:
    def __init__(self, nome, comendo=False):
        # ATRIBUTOS
        self.nome = nome
        self.comendo = comendo


