# Aula 9 - 19 - 11 - 2019
# Crie um programa que:
# 1 - Leia dois números inteiros:
# 2 - Calcule a soma entre dois números através de um metodo
# 3 - Calcule a subtração entre dois números através de um metodo
# 4 - Calcule a multiplicação entre dois números através de um metodo
# 5 - Calcule a divisão inteira entre dois números através de um metodo
# 6 - Calcule a divisão fracionada entre dois números através de um metodo
# 7 - Calcule a o resto da divisão entre dois números através de um metodo
# 8 - Calcule a raiz entre dois números através de um metodo
# 9 - Calcule a subtração entre dois números através de um metodo

def soma(n1, n2):
    soma1 = n1 + n2
    return soma1

def subtracao(n1, n2):
    subtracao1 = n1 - n2
    return subtracao1

def multiplicacao(n1, n2):
    multiplicacao1 = n1 * n2
    return multiplicacao1

def divisao(n1, n2):
    divisao1 = n1 / n2
    return divisao1

def divi_inteira(n1, n2):
    divi_inteira = n1 // n2
    return divi_inteira

def resto(n1, n2):
    resto1 = n1 % n2
    return resto1

def raiz(n1, n2):
    raiz11 = n1**(1/n2)
    return raiz11

def raiz2(n1, n2):
    raiz12 = n2**(1/n1)
    return raiz12
