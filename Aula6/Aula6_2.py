#--- Exercício 1 - Listas
#--- Escreva um programa que leia o nome de 10 alunos
#--- Armezene os nomes em uma lista
#--- Imprima a Lista

nome=[]

for i in range(0,10):
    nome.append(input(f'Digite seu nome aluno {i+1}: '))
for alunos in nome:
    print(alunos)