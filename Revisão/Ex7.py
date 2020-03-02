from Revisão.Ex4 import recebeex4
from Revisão.Ex5 import recebeex5
from Revisão.Ex6 import listagem
lista = ["Gustavo", "Galhardo", "Suzuki", "Letícia", "Marchi", "Klöppel"]
recebeu = []
# Ex4
def ex4():
    print("~"*30)
    nome = input("Digite um nome: ")
    recebeex4(recebeu, nome)
    print("~"*30)

# Ex5
def ex5():
    print("~"*30)
    recebeex5(lista)
    print("~"*30)

# Ex6
def ex6():
    print("~"*30)
    nome1 = input("Digite Um Nome: ")
    nome2 = input("Digite Outro Nome: ")
    listagem(lista, "PRIMEIRO NOME", "SEGUNDO NOME")
    listagem(lista, nome1, nome2)
    print("~"*30)

ex4()
ex5()
ex6()