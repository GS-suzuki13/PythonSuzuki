# Crie um método que receba dois parâmetros do tipo string
# verifique se o primeiro parâmetro esta dentro da lista
# caso o parâmetro esteja na lista substitua o dado pelo segundo parâmetro dentro da lista
# retorne informando que o dado foi alterado
# caso não encontre retorne informando que o dado não foi encontrado na lista

# Leia o nome de uma pessoa no console para realizar a alteração
# Leia o novo nome da pessoa
# Realize a chamada do método enviando o nome antigo e o novo nome
lista = ["Gustavo", "Galhardo", "Suzuki", "Letícia", "Marchi", "Klöppel"]
print(lista)


def listagem(lista, primeiro:str, segundo:str):
    if primeiro in lista:
        # Index Verifica Se Há e Passa Posição
        lista[lista.index(primeiro)]=segundo
        print(lista)
        return print("Dado Alterado!")
    return print("Dado Não Encontrado Na Lista!")
