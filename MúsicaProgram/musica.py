# def criar_musica(musica,):
#     musica1 = {'musica':musica}
#     return musica1

def criar_musica(musica):
    musica1 = {'musica':musica}
    return musica1


def salvar_musica(musica):
    arquivo = open ('MúsicaProgram/musica.txt', 'a')
    arquivo.write(f"{musica}\n")
    arquivo.close()

def ler_musica():
    arquivo = open('MúsicaProgram/musica.txt', 'r')
    lista_musica = []
    for linha in arquivo:
        # linha = 'oitavo anjo\n' primeiro ciclo do for
        linha = linha.strip()
        # linha = 'oitavo anjo'
        # dados_faixa = linha
        # faixa = criar_musica(dados_faixa[0])
        faixa = criar_musica(linha)
        # linha[0] = 'o'
        # linha = 'oitavo anjo'
        lista_musica.append(faixa)
    arquivo.close()
    return lista_musica

if __name__ == "__main__":
    som = ler_musica()
    print(som)