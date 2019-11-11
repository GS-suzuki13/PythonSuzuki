# Aula 4
# Fazer um programa que leia 2 numeros
# Realizar as 4 operações matemáticas
# Imprima o resultado das operações
# Diga qual numero é maior

n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))

resultado1 = n1 + n2
resultado2 = n1 - n2
resultado3 = n1 * n2
resultado4 = n1 / n2

print(f'A soma é {resultado1} 'end' a sub é {resultado2} 'end' a mult {resultado3} 'end' e a div {resultado4}')

if(n1)==(n2):
    print(f'Os númreos são iguais')
elif(n1)>(n2):
    print(f'O número {n1} é maior que o {n2}')
else:
    print(f'O número {n2} é maior que o {n1}')
