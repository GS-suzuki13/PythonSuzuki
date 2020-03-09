# A classe é um molde para o objeto, sendo uma definição de tipo,
# é a estrutura onde definimos atributos e comportamentos

# Criação de uma classe
class Pessoa:
    def __init__(self, nome, comendo=False):
        self.nome = nome
        self.comendo = comendo


    def comer(self):
        print(f"{self.nome} comeu!")
        self.comendo = True