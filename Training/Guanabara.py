from time import sleep

# #Ex 96
# def area(com, larg):
#     area_terreno = com + larg
#     return area_terreno
#
#
# print(f"Resultado da soma: {area(2, 3)}")
#
# #Ex 97
# def escreva(msg):
#     print("~"*len(msg))
#     print(msg)
#     print("~"*len(msg))
#
#
# escreva("Olá, Mundo!")
#

# # Ex 98
# def contador(i, f, p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         print("0 NÃO PODE EFETUAR CONTAGEM !")
#     print("ª"*40)
#     print(f"De {i} até {f} pulando de {p} em {p}")
#     sleep(3.0)
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f"{cont} ", end="", flush=True)
#             cont += p
#             sleep(0.5)
#         print("FIM!")
#     if i > f:
#         cont = i
#         while cont >= f:
#             print(f"{cont} ", end="", flush=True)
#             cont -= p
#             sleep(0.5)
#         print("FIM!")
#
#
#
# contador(1, 10, 1)
# contador(10, 0, 2)
# a = int(input("Defina um inicio:    "))
# b = int(input("Defina um fim:       "))
# c = int(input("Defina Nº de passos: "))
# contador(a, b, c)

# # Ex 99
# def maior(* numeros):
#     list_numeros = list(numeros)
#     print("Números Informados: ")
#     for i in list_numeros:
#         print(f"{i} ")
#     print(f"Número de Algarismos Inforados:\n{len(list_numeros)}")
#     print(f"Maior Algarismos:\n{max(list_numeros)}")
#
#
# maior(1, 3, 6, 8, 516, 532, 51, 45, 2, 54, 48, 41, 15)
#
# #Ex 100

