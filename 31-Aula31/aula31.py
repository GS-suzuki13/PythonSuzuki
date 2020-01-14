# BANCO DE DADOS
# SGBD - Sistema Gerenciador de Banco de Dados
# Mysqlm SqlServe ....

import MySQLdb

def listar_todos(c):
    c.execute('SELECT * FROM TortugaNinja')
    pessoas = c.fetchall()
    for p in pessoas:
        print('\033[32m=-\033[0;0m'*5, 'Listando \033[33mTODOS\033[0;0m', '\033[32m=-\033[0;0m'*5)
        print(p)
        print('\033[32m=-\033[0;0m'*5, 'Listando \033[33mTODOS\033[0;0m', '\033[32m=-\033[0;0m'*5)

def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM TortugaNinja WHERE ID = {id}')
    pessoa = c.fetchone()
    print('\033[32m=-\033[0;0m'*5, 'Listando Apenas \033[35mUM\033[0;0m', '\033[32m=-\033[0;0m'*5)
    print(pessoa)
    print('\033[32m=-\033[0;0m'*5, 'Listando Apenas \033[35mUM\033[0;0m', '\033[32m=-\033[0;0m'*5) 

conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')

cursor = conexao.cursor()
cursor.execute('SELECT * FROM TortugaNinja')
# pessoas = cursor.fetchall()
listar_todos(cursor)
buscar_por_id(cursor, 1)
































