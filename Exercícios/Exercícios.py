# Fazer um programa que leia 4 notas
# Imprima a maior nota
# Imprima a menor nota
# Imprima a média
# Imprima se o aluno foi aprovado ou reprovado (Média 7.0)

nota=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
nota3=float(input('Digite a terceira nota: '))
nota4=float(input('Digite a quarta nota: '))
media=float(4.0)

if nota > nota2 and nota > nota3 and nota > nota4:
    print(f'A nota {nota} é a maior nota')
if nota2 > nota and nota2 > nota3 and nota2 > nota4:
    print(f'A nota {nota2} é a maior nota')
if nota3 > nota2 and nota3 > nota and nota3 > nota4:
    print(f'A nota {nota3} é a maior nota'),
if nota4 > nota2 and nota4 > nota3 and nota4 > nota:
    print(f'A nota {nota4} é a maior nota')
if nota < nota2 and nota < nota3 and nota < nota4:
    print(f'A nota {nota} é a menor nota')
if nota2 < nota and nota2 < nota3 and nota2 < nota4:
    print(f'A nota {nota2} é a menor nota')
if nota3 < nota2 and nota3 < nota and nota3 < nota4:
    print(f'A nota {nota3} é a menor nota'),
if nota4 < nota2 and nota4 < nota3 and nota4 < nota:
    print(f'A nota {nota4} é a menor nota')
resultado=nota+nota2+nota3+nota4
resultado2=resultado / media
print(f'Sua média é {resultado2}')
if resultado2 > 7.0:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')