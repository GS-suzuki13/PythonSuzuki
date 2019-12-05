def cadastro_cliente(numero_funcao)

    dados_cliente = ['Codigo_cliente', 'CPF', 'Nome_completo',
                    'Data_nascimento', 'Estado', 'Cidade',
                    'CEP', 'Bairro', 'Rua', 'Numero_casa', 'Complemento']
    lista = []

    for j in range(numero_funcao):
        dicionario = {}

        for i in dados_cliente:
            dicionario[i]= input(f'{i}: ')
        lista.append(dicionario)
    return lista




numero = int(input('Digite o número de cadastros: '))
lista_cadastro = cadastro_cliente(numero)

arquivo = open('cliente.txt', 'a')
for cliente in arquivo:
    salvar = f'{cliente['Codigo_cliente']};'




arquivo.write()

arquivo.close()