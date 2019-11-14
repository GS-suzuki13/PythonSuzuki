# Aula 6 - P2 - 13 - 11 - 2019 -
# Estruturas de repetição - FOR

#---- For simples usando range com incremento padrão de 1
for i in range(1,10):
    print(f'{i} - Eu te amo!')

#---- For usando range com incremento  de 2
for i in range(1,10,2):
    print(f'{i} - Pares')

#---- For em lista usando range
lista = ['Mateus', 'Matheus', 'Marcelo', 'Nicole', 'Tonho', 'Pablo']
for i in range(0,6):
    print(lista)

#---- Exemplifica o problema do uso de For em lista usando range
lista.append('Natan')
for sortudo in lista:
    print(sortudo)

#---- For usando os elemntos da própria lista
numero = 7
for i in range(0,11):
    print(f'{i} x {numero} = {i*numero}')