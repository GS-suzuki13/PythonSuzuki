# Aula 6 - 13 - 11 - 2019 -
# Listas

#---- Iniciação de uma variável tipo lista
lista1 = []

#---- Iniciação de uma variável lista, com elemtenos
lista2 = ['Marcela', 'Nicole', '*Matheus']

#---- Lista com inteiros
lista3 = [1, 2, 3, 4, 5]

#---- Lista com tipos diferentes
lista4 = [1, 'Gustavo', 12.5]

#---- Impressão de listas criadas
print(lista1)
print(lista2)
print(lista3)
print(lista4)

#---- Impressão de listas criadas
lista1.append(lista2)
lista1.append(lista3)

#---- Crianção de lista com dados vindos da funçãi Input
lista_pergunta = [input('Digite seu artista favorito: '),input('Digite seu guitarrista favorito: ')]
print(lista_pergunta)

#---- Recuperando um dado de uma posição específica da lista
posicao = int(input('Digite a posição: '))
print(lista2[posicao-1])