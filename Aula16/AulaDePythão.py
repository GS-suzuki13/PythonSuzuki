# Aula 16 - 29 - 11 - 2019
# ????????

from faixa import criar_faixa, salvar_faixa, ler_faixa

# Cadastro de playlist
# Lendo música, artista e album

musica = input('Digite uma música: ')
artista = input('Digite o(a) artista: ')
album = input('Digite o nome do album: ')

faixa1 = criar_faixa(musica, album, artista)
salvar_faixa(faixa1)
lista = ler_faixa()

for n, faixa in enumerate(lista, start=1):
    print(f"{n}- Música: {faixa['musica']} - Album: {faixa['album']} - Artista: {faixa['artista']}")
