# ======= Classes =======
import MySQLdb




def listar_todos():
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019' )

    cursor = conexao.cursor()


    comando_sql_select = "SELECT * FROM TortugaNinja"
    cursor.execute(comando_sql_select)

    resultado = cursor.fetchall()
    return resultado

def converter_tabela_dicionario(lista_tuplas):
    lista_pessoas = []
    for p in lista_tuplas:
        dicionario_pessoa = {'ID': 0, 'Nome': '', 'Sobrenome': '', 'Idade': 0, 'Endereco_ID': 0 }
        dicionario_pessoa['ID'] = p[0]
        dicionario_pessoa['Nome'] = p[1]
        dicionario_pessoa['Sobrenome'] = p[2]
        dicionario_pessoa['Idade'] = p[3]
        dicionario_pessoa['Endereco_ID'] = p[4]
        lista_pessoas.append(dicionario_pessoa)
    return lista_pessoas

def exportar_txt(lista_pessoas):
    with open('33-Aula33/Pessoa.txt', 'a') as arquivo:
        for p in lista_pessoas:
            arquivo.write(f"{p['ID']}|{p['Nome']}|{p['Sobrenome']}|{p['Idade']}|{p['Endereco_ID']}\n")

lpt = listar_todos()
lpd = converter_tabela_dicionario(lpt)
exportar_txt(lpd)



































