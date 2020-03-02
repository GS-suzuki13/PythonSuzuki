# Eles representam entidades, são intâncias de classes,
# são capazes de reter um estado, e objetos  podem interagir
# entre si por "TROCA DE MENSAGENS".

# TROCA DE MENSAGENS -> São as chamadas dos métodos

# Importando classe de um arquivo externo
from Training.poo.metodo import Pessoa

# Criando Objeto "pessoa"
pessoa = Pessoa("Gustavo")
alimento = input("Digite o que comer: ")
print(pessoa.comer_alimento(alimento))