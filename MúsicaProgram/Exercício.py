from musica import criar_musica, salvar_musica, ler_musica


musica = []
album = []
artista = []

menu = '''
===================================================================================
=                        I Festival de Música em Itororó                         =
===================================================================================

1 - Cadasto de Música
2 - Cadastro de Album
3 - Cadastro de Artsista
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
            som = ler_musica()
            for n, musica in enumerate(som, start=1):
                # n = lista_musica()
                # musica = start
                
                print(f"{n}- Música: {musica['musica']}")

            if opcao == '2':
                lista = ler_musica()
                print( 'Ver Músicas Cadastradas')
                print(f'As músicas cadastradas são: {lista}')

                
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