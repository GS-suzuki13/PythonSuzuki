# O comportamento de um objeto permanece oculto para o mundo externo,
# ou os objetos mantêm suas informações de estado como privadas.
# Os clientes não podem alterar o estado interno dos objetos atuando diretamente neles;
# em vez disso, eles requisitam o objeto enviando mensagens.
# Com base no tipo das requisições,
# os objetos podem responder alterando o seu estado interno
# utilizando funções-membro especiais como get e set.
# Eles protegem o código e isso permite que o objeto
# controle seu próprio estado e suas caracteristicas.

class Pessoa():

    def __init__(self, nome, comendo=False):
        # A adiçãos do _ antes da variável mostra que ela não deve ser alterada por fora
        # Fazendo com que ela fique "Encapsulada"
        self.__nome = nome
        self.__comendo = comendo

    def comer(self, alimento):
        print(f"{self.__nome} comeu {alimento}!")
        self.__comendo = True