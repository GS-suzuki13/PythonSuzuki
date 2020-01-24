import MySQLdb
import sys
sys.path.append(r'C:/Users/900142/Desktop/PythonSuzuki/37-Aula37')
from Model.SquadModel import Squad

class SquadDao:
    connection = MySQLdb.connect(host='mysql.padawans.dev', database='padawans12', user='padawans12', passwd='mg2019')
    cursor = connection.cursor()
   
    def list_all(self):
        command = f'SELECT * FROM padawans12.SuzukiSquad'
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        return result
    
    def search_for_id(self, id):
        command = f'SELECT * FROM padawans12.SuzukiSquad AS S WHERE S.ID = {id}'
        self.cursor.execute(command)
        result = self.cursor.fetchone()
        return result

    def save(self, squad:Squad):
        command = f""" INSERT INTO padawans12.SuzukiSquad ss
        (
            Name,
            Description,
            PeopleNumber,
            LanguageBackEnd,
            FrameworkFrontEnd
        )
        VALUES
        (
            '{squad.name}',
            '{squad.description}',
            {squad.peoplenumber},
            '{squad.languagebackend}',
            '{squad.frameworkfrontend}'
        )"""
        self.cursor.execute(command)
        self.connection.commit()
        id_inserted = self.cursor.lastrowid
        return id_inserted

    def change(self, squad:Squad):
        command = f"""UPDATE padawans12.SuzukiSquad ss
        SET
            Name = '{squad.name}',
            Description = '{squad.description}',
            PeopleNumber = {squad.peoplenumber},
            LanguageBackEnd = '{squad.languagebackend}',
            FrameworkFrontEnd = '{squad.frameworkfrontend}'
        WHERE ID = {squad.id}
        """
        self.cursor.execute(command)
        self.connection.commit()

    def delete(self, id1):
        command = f"DELETE FROM padawans12.SuzukiSquad WHERE ID = {id1}"
        self.cursor.execute(command)
        self.connection.commit()