def exportar_txt(lista_pessoas):
    with open('33-Aula33-1/Pessoa.txt', 'a') as arquivo:
        for p in lista_pessoas:
            arquivo.write(f"{p['ID']}|{p['Nome']}|{p['Sobrenome']}|{p['Idade']}|{p['Endereco_ID']}\n")