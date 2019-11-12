# Fazer um programa que leia 4 notas
# Imprima a maior nota
# Imprima a menor nota
# Imprima a média
# Imprima se o aluno foi aprovado ou reprovado (Média 7.0)

nota=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
nota3=float(input('Digite a terceira nota: '))
nota4=float(input('Digite a quarta nota: '))

print('A maior nota foi: ', max(nota, nota2, nota3, nota4))
print('A menor nota foi: ', min(nota, nota2, nota3, nota4))

media=(nota+nota2+nota3+nota4)/4
print(f'Sua média foi de: {media}')
if media >= 7:
    print('Parabéns, você foi aprovado!')
else:
    print('Você foi reprovado!')