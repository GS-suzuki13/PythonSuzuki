from app.api_cep import ApiCep


def consulta_api_viacep():
    nova_consulta_api_cep = ApiCep()
    json_cep = nova_consulta_api_cep.execute(input('Informe o cep para consulta: '))
    print(json_cep)
    return 'Cep consultado com sucesso!'

# testar método -> consulta_api_viacep()
#
#     requisitos mínimos:
#         1. criar mock do método input().
#         2. criar mock do método print().
#         3. realizar assert para o mock do método input(),
#           afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do input().
#         4. realizar assert para o mock do método print(),
#           afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do print().
#         5. ensinar ao mock do método input(), qual valor ele deverá retornar quando ele for chamado.
#         6. verificar se o retorno ensinado ao mock do método input() foi passado como argumento ao mock do método print().
#         7. gerar html com a cobertura de código realizada pelo teste e garantir 100% de cobertura para o código do arquivo run.py
#
#     desafio:
#         1. criar mock do método execute() da classe ApiCep()
#         2. realizar assert do método execute() da classe ApiCep(), afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do execute().
#         3. gerar html com a cobertura de código realizada pelo teste e garantir que o teste está cobrindo somente o arquivo run.py