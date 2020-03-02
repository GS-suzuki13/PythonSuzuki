# Definem o comportamento do objeto,
# podendo passar parâmetros a serem definidos
# e outros já pré-definidos
# opera sobre atributos e podem realizar
# "TROCA DE MENSAGENS" entre os objetos.
# E nada mais são que funções ou procedimentos
# dentro das classes

# TROCA DE MENSAGENS -> São as chamadas dos métodos

# Classe Contendo 3 métodos diferentes
class Pessoa():
    # MÉTODO CONTRUTOR
    def __init__(self, nome, comendo=False):
        self.nome = nome
        self.comendo = comendo

    # MÉTODO DA CLASSE
    def comer(self):
        print(f"{self.nome} comeu!")
        self.comendo = True

    # MÉTODO DA CLASSE COM PARÂMETRO
    def comer_alimento(self, alimento):
        print(f"{self.nome} irá comer {alimento} assim que possivel!")
        self.comendo = True