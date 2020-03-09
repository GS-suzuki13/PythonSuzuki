# Eles representam entidades, são intâncias de classes,
# são capazes de reter um estado, e objetos  podem interagir
# com outros objetos fazendo troca de mensagem(ver método).

# Importando classe de um arquivo externo
from metodo import Pessoa

# Criando Objeto "pessoa"
pessoa = Pessoa("Gustavo")
# Definindo valor para o parâmetro
alimento = input("Digite o que comer: ")
print(pessoa.comer_alimento(alimento))