# class Somas():
#     def __init__(self, fixoum=10, fixodois=20):
#         self.a = int(input("Primeiro Número: "))
#         self.b = int(input("Segundo Número: "))
#         self.fixoum = fixoum
#         self.fixodois = fixodois


#     def somaum(self):
#         resultadoum = self.fixoum + self.fixodois
#         return resultadoum


#     def soma(self):
#         resultadodois = self.a + self.b
#         return resultadodois


def soma(a, b):
    resultado = a + b
    return resultado

a = int(input("Primeiro Número: "))
b = int(input("Segundo Número: "))
resultado = soma(a, b)
print(f"Resultado Segunda Questão: {resultado}")