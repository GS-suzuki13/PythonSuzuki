#---- Exercíco 2 - Dicionário
#---- Escreva um programa que leia os dados de 11 jogadores
#---- jogador: Nome, Posição, Número, PernaBoa
#---- Crie um dicionário para armazenar os dados
#---- Imprima todos os jogadores e seus dados

jogador = []

for i in range(1,3):   
    nome=str(input('Digite o nome de um jogador: '))
    posicao=str(input('Qual sua posição: '))
    numero=int(input('Digite o número de seu jogador: '))
    pb=str(input('Qual sua melhor perna:  '))
    
    jogadores = {'Nome':nome, 'Posicao':posicao, 'Numero':numero, 'PernaBoa':pb}

    jogador.append(jogadores)

for jogadores in jogador:
    print('='*50, '\n',f"Jogador: {jogadores['Nome']} \n Posição: {jogadores['Posicao']} \n Número: {jogadores['Numero']} \n PernaBoa: {jogadores['PernaBoa']}", '\n', '='*50)

    
    