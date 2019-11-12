# -- 2 --
# --- Mercado Tech ---
# Solicitar nome  do funcionário
# Solicitar idade
# Informar se o funcionário pode adquirir produtos alcoolicos

# -- 3 --
# Cadastro Produto Mercado Tech
# Solicitar o nome do produto
# Solicitar categoria do produto (Alcoolico e Não Alcoolico)
# Exibir o produto cadastrado

nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))

if idade>=18:
    print(f'Olá {nome}, você pode adquirir os produtos alcoolicos.')
    produto=input('Digite o nome do produto: ')
    categoria=input('Produto alcoolico ou Não alcoolico: ')
    print(f'O produto {produto}, {categoria}, foi cadastrado com sucesso!')
else:
    print(f'Olá {nome}, você NÃO pode adquirir os produtos alcoolicos.')
    produto=input('Digite o nome do produto: ')
    print(f'O produto {produto}, NÃO ALCOOLICO, foi cadastrado com sucesso!')

