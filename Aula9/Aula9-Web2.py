# Aula 9 - 19 - 11 - 2019
# Web 2

# nome_completo = input('Digite seu nome: ')
# cpf = input('Digite seu CPF: ')
# reg = int(input('Dgitie o número de registro: '))
# cargo = input('Digite seu cargo: ')
from calculo_impostos import calculo_inss, calculo_irrf

print('='* 25, '\t', 'AMBEV', '\t'*2, '='* 25, '\n'*2)

salario = float(input('Digite seu salário: '))

inss = calculo_inss(salario)
irrf = calculo_irrf(salario, inss)


salario_liquido = salario - inss - irrf

print(f'Seu salário liquído é {salario_liquido}', '\n'*2)

print('='* 25, '\t', 'AMBEV', '\t'*2, '='* 25)