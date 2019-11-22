from exercicio import soma, subtracao,multiplicacao, divisao, divi_inteira, resto, raiz1, raiz2

print('='* 25, '\t', 'AMBEV', '\t'*2, '='* 25, '\n'*2)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(f'''A soma é: {soma(n1,n2)}
A subtração é: {subtracao(n1,n2)}
A multiplicação é: {multiplicacao(n1,n2)}
A divisão é: {divisao(n1,n2)}
A divisão inteira é: {divi_inteira(n1,n2)}
O resto da divisão é: {resto(n1,n2)}
A raiz é: {raiz1(n1,n2)}
A raiz é: {raiz2(n1,n2)}''', '\n'*2)

print('='* 25, '\t', 'AMBEV', '\t'*2, '='* 25)