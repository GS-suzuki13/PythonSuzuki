# Aula 4 - 13 - 11 - 2019 -
# Estrutura de decisão

idade = 25
#---- If simples, validação de apensa uma codição
if idade == 18:
    print('Maior')

#---- If com else, 
#---- Caso a condição validada pelo If não seja verdadeira,
#---- O Else é executado

if (idade < 18):
    print('Mlk ainda')
else:
    print('Maior')

#---- If com Elif e Else
#---- Caso a confição validada no id se falsa
#---- É validada a condição Elif
#---- Caso a condição do Elif seja falsa
#---- Else é executado
if (idade < 18):
    print('Mlk ainda')
elif (idade == 18):
    print('Já foi pro exército?')
else:
    print('Mlk com responsabilidade')

#--- If com variável booleana
#--- Em caso de variável booleana, não é necessário a validacao(==True)
#--- Pois o If ja valida o se o conteúdo da variável é True, senão vai para o Else
ativo = True

if ativo:
    print('Logar')
else:
    print('Não logar')