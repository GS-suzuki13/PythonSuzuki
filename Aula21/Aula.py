import os 
menu_conta = '''
===================================================================================
=                            C A L C U L A D O R A                                =
===================================================================================

1 - Fazer Conta
2 - Sair

Digite a opção desejada: '''


while True:
    os.system('cls')
    conta = input(menu_conta)



    if conta == '1':

        n1 = int(input('Digite um Número: '))
        n2 = int(input('Digite outro número: '))

        soma = n1 + n2
        subtr = n1 - n2
        mult = n1 * n2
        div = n1 / n2

        print (f'Soma: {soma} - Subtração: {subtr} - Multiplicação: {mult} - Divisão: {div}')
        none = input()
    


    if conta == '2':
        opcao = input("Digite 's' para sair\n Digite 'c' para NÃO sair:  ")

        if opcao == 's':
            break

