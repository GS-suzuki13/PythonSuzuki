# 1 - Lista interativa

menu = '''
===================================================================================
=                        I Festival de Cerveja em Itororó                         =
===================================================================================

1 - Cadasto de Cliente
2 - Ver Clientes Cadastrados
3 - Cadastro de Produtos
4 - Ver Produtos Cadastrados
5 - Vendas
6 - Relatório de Vendas
7 - Sair

Digite a opção desejada: '''

while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadatro do Cliente')
        
    elif opcao == '2':
        print('Ver Clientes Cadastrados')

    elif opcao == '3':
        print('Cadastro de Produtos')

    elif opcao == '4':
        print('Ver Produtos Cadastrados')

    elif opcao == '5':
        print('Vendas')

    elif opcao == '6':
        print('Relatório de Vendas')

    elif opcao == '7':
        print('Sair')
        break

    else:
        print('Valor Invalido')