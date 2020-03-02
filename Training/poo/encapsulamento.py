# O comportamento de um objeto permanece oculto para o mundo externo,
# ou os objetos mantêm suas informações de estado como privadas.
# Os clientes não podem alterar o estado interno dos objetos atuando diretamente neles;
# em vez disso, eles requisitam o objeto enviando mensagens.
# Com base no tipo das requisições,
# os objetos podem responder alterando o seu estado interno
# utilizando funções-membro especiais como get e set.
# Eles protegem o código e isso permite que o objeto

class Pessoa():

    def __init__(self, nome, comendo=False):
        self._nome = nome
        self._comendo = comendo

    def comer(self, alimento):
        print(f"{self._nome} comeu {alimento}!")
        self._comendo = True