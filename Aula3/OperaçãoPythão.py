nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))

print('Olá', nome, 'sua idade é', idade,'?')
print(f'Nome: {nome} 
 Idade: {idade}')

if (idade) < 18:
     print('Menor de idade')
else:
    print('Maior de idade')