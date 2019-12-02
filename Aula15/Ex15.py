def salvar_cerveja(cerveja_dicionario):
    arquivo = open('aula15.txt', 'a')
    arquivo.write(f"{cerveja_dicionario['marca']};{cerveja_dicionario['tipo']};{cerveja_dicionario['teor']}\n")
    arquivo.close()

def info():
    lista = []
    arquivo = open('aula15.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'marca':lista_linha[0], 'tipo':lista_linha[1], 'teor':lista_linha[2]}
        lista.append(cerveja)
    arquivo.close()
    return lista

marca = input('Digite a marca da cerveja: ')
tipo = input('Digite o tipo da cerveja: ')
teor = float(input('Digite o teor alcoolico: '))

cerveja = {'marca':marca, 'tipo':tipo, 'teor':teor}
salvar_cerveja(cerveja)

for c in info():
    print(f"{c['marca']} - {c['tipo']} - {c['teor']}")