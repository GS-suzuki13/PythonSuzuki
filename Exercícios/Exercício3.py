#---- Exercíco 3 - Dicionário
#---- Escreva um programa que leia os dados da cerveja
#---- Cerveja: Marca, Tipo, IBU, ABV, EBC, Volume
#---- Crie um dicionário para armazenar os dados
#---- Imprima os dados do dicionário (não dicionário completo)

marca=input('Marca: ')
tipo=input('Tipo: ')
ibu=float(input('IBU: '))
abv=float(input('ABV: '))
ebc=float(input('EBC: '))
volume=int(input('Volume: '))

dicinario={'Marca: ':marca, 'Tipo: ':tipo, 'IBU: ':ibu, 'ABV: ':abv, 'EBC: ':ebc, 'Volume: ':volume}

print(f"{dicinario['Marca: ']}\n{dicinario['Tipo: ']}\n{dicinario['IBU: ']}\n{dicinario['ABV: ']}\n{dicinario['EBC: ']}\n{dicinario['Volume: ']}")
