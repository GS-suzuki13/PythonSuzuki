from musica import criar_musica, salvar_musica, ler_musica




musica = []
album = []
artista = []

menu = '''
===================================================================================
=                        I Festival de Cerveja em Itororó                         =
===================================================================================

1 - Cadasto de Música
2 - Cadastro de Album
3 - Cadastro de Artsista
4 - Ver Músicas Cadastradas
5 - Ver Albuns Cadastrados
6 - Ver Artistas Cadastrados
7 - Sair

Digite a opção desejada: '''

menu_musica = '''
===================================================================================
=                            Cadastro de Música                                   =
===================================================================================

1 - Cadastrar Outra Música
2 - Ver Músicas Cadastradas
3 - Sair

Digite a opção desejada: '''


while True:
    opcao = input(menu)
    
    if opcao == '1':

        
        while True:
            musica.append(input('Digite a Música: '))
            opcao = input(menu_musica)

            if opcao == '1':
                faixa1 = criar_musica(musica)
                salvar_musica(faixa1)
                lista = ler_musica()
            for n, musica in enumerate(lista, start=1):
                print(f"{n}- Música: {musica['musica']}")

            if opcao == '2':
                print( 'Ver Músicas Cadastradas')
                print(f'As músicas cadastradas são: {musica}')

                
            elif opcao == '3':
                print('Sair')
                break

            else:
                print('Opção Invalida')

        
    elif opcao == '2':
        album.append(input('Digite o Album: '))


    elif opcao == '3':
        artista.append(input('Digite o(a) Artista: '))

    elif opcao == '5':
        print('Ver Albuns Cadastrados')
        print(f'Os albuns cadastradas são: {album}')

    elif opcao == '6':
        print('Ver Artistas Cadastrados')
        print(f'O(A)s artistas cadastrados são: {artista}')

    elif opcao == '7':
        print('Sair')
        break


    else:
        print('Valor Invalido')