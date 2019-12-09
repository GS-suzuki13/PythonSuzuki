# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]


# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com

print(f'''Nome: {cadastroHBSIS[1][0]}       |   Telefone: {cadastroHBSIS[3][0]}
Email: {cadastroHBSIS[5][0]}   |   Idade: {cadastroHBSIS[7][0]}''')



# 2 - usando o for, imprima todos nomes um abaixo do outro
lista_nome = (cadastroHBSIS[1])
for nome in lista_nome:
    print(nome)

# 3 - Usando a indexação faça uma lista com 3 dicionarios contendo os dados 
# do Mateus, Paulo # e João contendo
# como chaves: nome, email, idade, telefone (nesta  sequencia)

dicio_mateus = {f"Nome: {cadastroHBSIS[1][3]}   |   Email: {cadastroHBSIS[3][3]}\nIdade: {cadastroHBSIS[7][4]}   |   Telefone: {cadastroHBSIS[5][3]}  "}
dicio_paulo = {f"Nome: {cadastroHBSIS[1][1] }    |   Email: {cadastroHBSIS[3][1]}\nIdade: {cadastroHBSIS[7][1]}   |   Telefone: {cadastroHBSIS[5][1]}  "}
dicio_joao = {f"Nome: {cadastroHBSIS[1][5]}     |   Email: {cadastroHBSIS[3][5]}\nIdade: {cadastroHBSIS[7][5]}   |   Telefone: {cadastroHBSIS[5][5]}  "}

print(f"{dicio_mateus}\n{dicio_paulo}\n{dicio_joao}")

