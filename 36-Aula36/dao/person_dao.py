import MySQLdb
from model.person import Person

class PersonDao:
    connection = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = connection.cursor()

    def list_all(self):
        command = f"SELECT * FROM TortugaNinja"
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        return result


    def search_for_id(self, id):
        command = f"SELECT * FROM TortugaNinja WHERE ID={id}"
        self.cursor.execute(command)
        result = self.cursor.fetchone()
        return result

    def save(self, person:Person):
        command = f"""INSERT INTO TortugaNinja 
        (
            Nome
            ,Sobrenome
            ,Idade
            ,Endereco_Id
        )
        
        VALUES
        (
            '{person.name}'
            ,{person.last_name}
            ,{person.age}
            ,{person.address_id}
        )"""
        self.cursor.execute(command)
        self.cursor.commit()


    def change(self, person:Person):
        pass

    def delete(self, id):
        command = f"DELETE FROM TortugaNinja WHERE ID={id}"
        self.cursor.execute(command)
        result = self.cursor.fetchone()








































