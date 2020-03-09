# Torna a variavel privada e inacessível externamente
# Protegendo assim seu código e possibilitando que
# o objeto controle seu comportamento e estado de
# acordo com o que se é requisitdado
class Pessoa():

    def __init__(self, nome, comendo=False):
        # A adiçãos do _ antes da variável mostra que ela não deve ser alterada por fora
        # Fazendo com que ela fique "Encapsulada"
        self.__nome = nome
        self.__comendo = comendo

    def get_nome(self)->str:
        return self.__nome

    def set_logradouro(self, nome)->None:
        self.__nome = nome

    def comer(self, alimento):
        print(f"{self.__nome} comeu {alimento}!")
        self.__comendo = True