# A sobre escrita é realizada
# quando ocorre a chamada de uma classe-mãe
# e dentro existe um metodo e você define
# uma nova funcionalidade ou altera um estado

# Importando uma classe-mãe
from metodo import Pessoa
class Aluno(Pessoa):
    def __init__(self):
        self.__id_aluno = 0

    def comer_alimento(self, alimento, id_aluno):
        self.__id_aluno = id_aluno
        # Utilizando método "super" eu faço a ligação
        # do método da classe-filha para a classe-mãe
        super().comer_alimento(alimento, id_aluno)
        