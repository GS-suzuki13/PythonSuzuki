# Definem o comportamento do objeto,
# Classe Contendo 3 métodos diferentes
# Métodos realizam troca de mensagens entre objeto
# essa troca de mensagens são feitas chamando os métodos
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
        print(f"{self.nome} comeu {alimento}")
        self.comendo = True