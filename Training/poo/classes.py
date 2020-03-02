# A classe é um molde para o objeto, sendo uma definição de tipo,
# é uma estrutura onde podemos definir atributos e comportamentos,
# é tambem um "TAMPLATE" para a criação de objetos e os seus construtores
# são implementados para definir um estado inicial de um objeto.

# TAMPLATE -> Molde da classe

class Pessoa:
    def __init__(self, nome, comendo=False):
        self.nome = nome
        self.comendo = comendo


    def comer(self):
        print(f"{self.nome} comeu!")
        self.comendo = True