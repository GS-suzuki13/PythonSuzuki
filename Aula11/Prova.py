# Aula 11 - 21 - 11 - 2019 -
# Prova

# 1- Crie um rograma que calcule o imposto  ISS de um serviço de desenvolvimento de software
# -- Utilizar métodos
# 2- Crie um rograma que calcule a rentabilidade anual de um investimento
# -- baseando-se em sua rentabilidade mensal (juros compostos) 
# -- a rentabilidade deve ser apresentada em % e R$
# -- Utilizar métodos
# 3- Crie um programa para calculo de investimento
# -- Solicitar número de cotas à comprar
# -- solicitar valor a ser investido no Tesouro Selic
# -- (considerar valor do Tesouro hoje)
# -- Calcular o valor total até o vencimento do titulo
# -- Utilizar metodos

# Exercício 1

from Arquivos import calculo_iss

print('='* 25, '\t', 'Exercício 1', '\t'*2, '='* 25, '\n'*2)

ds = float(input(' Digite o custo do Desenvolvimento de Software: '))
custo = calculo_iss(ds)

resultado = ds - custo

print(f' Seu rendimento líquido será de: R$ {resultado}', '\n', f'E o custo seu imposto será de: R$ {custo}', '\n'*2)

print('='* 25, '\t', 'Exercício 1', '\t'*2, '='* 25)

# Exercício 2

from Arquivos import calculo_juros, calculo_montante, calculo_mensal

print('='* 25, '\t', 'Exercício 2', '\t'*2, '='* 25, '\n'*2)

investido = float(input(' Digite o valor investido: R$ '))
juros = float(input(' Digite o juros do investimento (Mês): '))
periodo = int(input(' Digite o período do investimento (Mês): '))

juros_dividido =float(calculo_juros (juros))

restante = calculo_montante (investido, juros_dividido, periodo)

mes =  calculo_mensal (investido, juros_dividido)

# juros_porcentagem =float(calculo_porcentagem (juros_dividido))

print(f' Sua rentabilidade durante o perído de {periodo} mês(mêses) será de: R$ {restante:0.2f} \n Sua rentabilidade mensal será de: R$ {mes:0.2f} \n Baseado nos juros mensal de {juros}%','\n'*2)

print('='* 25, '\t', 'Exercício 2', '\t'*2, '='* 25)

# Exercício 3

print('='* 25, '\t', 'Exercício 2', '\t'*2, '='* 25, '\n'*2)

print(' Tesouro Selic: R$ 10410.00')
print(' Compra miníma: 0.01 = R$ 104.10')
print(' Vencimento: 01/03/2025')

qntd = float(input(' Digite quantas cotas deseja comprar: '))
valor = 104.10

if qntd >= 0.01:
    taxa_juros =(5.0 + 0.02)/12
    qntd_total = qntd * valor
    valor_total = (qntd_total * (1 + taxa_juros))*64

    print(f' O total investido será de R$ {valor_total:0.02f}\n')

else:
    print('Quantidade inferior a de compra!\n')

print('='* 25, '\t', 'Exercício 2', '\t'*2, '='* 25)