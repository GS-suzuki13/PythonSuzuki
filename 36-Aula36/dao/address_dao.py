import MySQLdb
from model.address import Address

class AddressDao:
    connection = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = connection.cursor()

    def list_all(self):
        command = f"SELECT * FROM TortugaNinja_Endereço"
        self.cursor.execute(command)
        result = self.cursor.fetchall()

    def search_for_id(self, id):
        command = f"SELECT * FROM TortugaNinja WHERE ID = {id}"
        self.cursor.execute(command)
        result = self.cursor.fetchone()
        return result


    def save(self, address:Address):
       command = f"""INSERT INTO TortugaNinja_Endereco 
        (
            CEP
            ,Rua
            ,Número
            ,Bairro
            ,Cidade
        )
        
        VALUES
        (
            '{address.cep}'
            ,'{address.street}'
            ,'{address.number}'
            ,'{address.neighborhood}'
            ,'{address.city}'
        )"""
        self.cursor.execute(command)
        self.connection.commit()
        id_insert = self.cursor.lastrowid
        return id_insert


    def change(self, address:Address):
        command = f"""UPDATE TortugaNinja_Endereco
        SET
            CEP = {address.cep}
            Rua = {address.street}
            Número = {address.number}
            Bairro = {address.neighborhood}
            Cidade = {address.city}
        WHERE ID = {person.id}
            """
        self.cursor.execute(command)
        self.connection.commit()
        id_insert = self.cursor.lastrowid
        return id_insert

    def delete(self, id):
        command = f"DELETE FROM TortugaNinja_Endereco WHERE ID={id}"
        self.cursor.execute(command)
        result = self.cursor.fetchone()