#--- Exercício 3 - Foreach
#--- Escreva um programa que leia as notas (4) de 10 alunos
#--- Armezene as notas e os nomes em listas
#--- Imprima:
#           1: Nome dos alunos
#           2: Média do aluno
#           3: Resultado (Aprovado>=7.0)
nome=str(input('Diga seu nome: '))
print(f'Olá {nome}, a seguir informar suas nota.')

n1=float(input('Primeira nota: '))
n2=float(input('seginda nota: '))
n3=float(input('terceira nota: '))
n4=float(input('quarta nota: '))

media=(n1+n2+n3+n4)/4
print(f'Sua média foi: {media}')
if media>=7.0:
    print('Parabéns você foi aprovado: ')
else:
    print('Você foi reprovado!')

