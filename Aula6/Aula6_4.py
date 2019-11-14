#--- Exercício 3 - Foreach
#--- Escreva um programa que leia as notas (4) de 10 alunos
#--- Armezene as notas e os nomes em listas
#--- Imprima:
#           1: Nome dos alunos
#           2: Média do aluno
#           3: Resultado (Aprovado>=7.0)

nome=[]
nota=[]
n1=0
n2=1
n3=2
n4=3

for i in range(0,2):
    nome.append(input(f'Digite o nome do aluno {i+1}: '))
    for j in range(0,4):
        nota.append(float(input(f'Digite a nota {i+1}: ')))

for aluno in nome:
    media=(nota[n1]+nota[n2]+nota[n3]+nota[n4])/4
    resultado='Reprovado!'
    if media>=7:
        resultado='Aprovado!'
        print(f'Aluno: {aluno} - Média: {media} - Situação: {resultado}')
n1 += 4
n2 += 4
n3 += 4
n4 += 4
