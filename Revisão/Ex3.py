def multiplicacao(a, b, c=1.0):
    resultado = a * b * c
    return resultado

a = float(input("Primeiro Número: "))
b = float(input("Segundo Número: "))
resultado = multiplicacao(a, b)
print(f"Resultado Primeira Questão: {resultado}")

a = float(input("Primeiro Número: "))
b = float(input("Segundo Número: "))
c = float(input("Terceiro Número: "))
resultado = multiplicacao(a, b, c)
print(f"Resultado Segunda Questão: {resultado}")