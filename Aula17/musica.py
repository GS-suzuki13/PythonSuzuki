def criar_musica(musica,):
    musica1 = {'musica':musica}
    return musica1

def salvar_musica(musica):
    arquivo = open ('Aula17/musica.txt', 'a')
    arquivo.write(f"{musica}\n")
    arquivo.close()

def ler_musica():
    arquivo = open('Aula17/musica.txt', 'r')
    lista_musica = []
    for linha in arquivo:
        linha = linha.strip()
        dados_faixa = linha 
        faixa = criar_musica(dados_faixa[0])
        lista_musica.append(faixa)
    arquivo.close()
    return lista_musica