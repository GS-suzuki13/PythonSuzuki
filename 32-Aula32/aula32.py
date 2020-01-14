# pip3 install flask_mysqldb
# referencia ao Mysql

import MySQLdb
#listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM TortugaNinja')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)
        
#buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM TortugaNinja WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM TortugaNinja WHERE Sobrenome like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print('\033[32m=-\033[0;0m'*5, 'Resultado da Busca', '\033[32m=-\033[0;0m'*10)
        print(p)
#salvar pessoa
def salvar(cn, cr, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"INSERT INTO TortugaNinja (Nome, Sobrenome, Idade, Endereco_ID ) VALUES ('{nome}', '{sobrenome}',{idade},{endereco_id})")
    cn.commit()
    cr.execute('SELECT * FROM TortugaNinja')
    pessoas = cr.fetchall()
    print('\033[32m=-\033[0;0m'*5, 'Tabela Atualizada Com Sucesso', '\033[32m=-\033[0;0m'*5)
    for p  in  pessoas:
        print(p)
    print('\n','\033[32m=-\033[0;0m'*5, 'Tabela Atualizada Com Sucesso', '\033[32m=-\033[0;0m'*5)
        

#alterar pessoa
def alterar(cn, cr):
    print('''
    ORDEM DE COLUNAS (separadas por ','):
ID | NOME | SOBRENOME | IDADE | ENDEREÇO ID''')
    cr.execute('SELECT * FROM TortugaNinja')
    pessoas = cr.fetchall()
    for p  in  pessoas:
        print(p)
    id_select = int(input('Digite o Número do ID desejado para alterar: '))
    nome = input('Digite o Nome desejado para alterar: ')
    sobrenome = input('Digite o Sobrenome desejado para alterar: ')
    idade = input('Digite a Idade desejada para alterar: ')
    endereco_id = input('Digite o Número do ID do endereço desejado para alterar: ')
    if endereco_id == ' ':
        endereco_id='NULL'
        cr.execute(f"UPDATE TortugaNinja SET Nome='{nome}', Sobrenome='{sobrenome}', Idade={idade}, Endereco_ID={endereco_id} WHERE ID={id_select} ")
        cn.commit()
    
    else:
        cr.execute(f"UPDATE TortugaNinja SET Nome='{nome}', Sobrenome='{sobrenome}', Idade={idade}, Endereco_ID={endereco_id} WHERE ID={id_select} ")
        cn.commit()
    print('\033[32m=-\033[0;0m'*5, 'Item Inserido Com Sucesso', '\033[32m=-\033[0;0m'*5)
    cr.execute('SELECT * FROM TortugaNinja')
    pessoas = cr.fetchall()
    for p  in  pessoas:
        print(p)
    print('\033[32m=-\033[0;0m'*5, 'Tabela Atualizada Com Sucesso', '\033[32m=-\033[0;0m'*5)

#deletar pessoa por ID
def deletar(cn, cr):
    cr.execute('SELECT * FROM TortugaNinja')
    pessoas = cr.fetchall()
    print('''
    ORDEM DE COLUNAS (separadas por ','):
ID | NOME | SOBRENOME | IDADE | ENDEREÇO ID''')
    for p  in  pessoas:
        print(p)
    id_select = int(input('Digite o Número do ID desejado para deletar: '))
    cr.execute(f'DELETE FROM TortugaNinja WHERE ID={id_select}')
    cn.commit()
    print('\033[32m=-\033[0;0m'*5, 'Tabela Atualizada Com Sucesso', '\033[32m=-\033[0;0m'*5)
    cr.execute('SELECT * FROM TortugaNinja')
    pessoas = cr.fetchall()
    for p  in  pessoas:
        print(p)
    print('\033[32m=-\033[0;0m'*5, 'Tabela Atualizada Com Sucesso', '\033[32m=-\033[0;0m'*5)

conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019' )
cursor = conexao.cursor()

# listar_todos(cursor)
# buscar_por_id(cursor, 1)
# buscar_por_sobrenome(cursor,'Gru')
# salvar(conexao, cursor, 'Junin', 'Gatão Da Carbura', 23)
alterar(conexao, cursor)
# deletar(conexao, cursor)















