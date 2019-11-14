#--- Exercício 2 - For
#--- Escreva um programa que leia um número inteiro
#--- Calcule a toboada do número informado
#--- Imprima a taboada com a conta completa (n * i = r)

n=int(input('Digite um número inteiro: '))
for i in range(0,11):
    print(f'{i} x {n} = {i*n}')