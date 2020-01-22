import MySQLdb
import sys
sys.path.append('/Users/900170/Desktop/PythonSuzuki/37-Aula37')
from Model.squadModel import Squad

class SquadDao:
    connection = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = connection.cursor()
   
    def list_all(self):
        command = f'SELECT * SuzukiSquad'
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        return result
    
    def search_for_id(self, id):
        command = f'SELECT * FROM SquadSuzuki AS S WHERE S.ID = {id}'
        self.cursor.execute(command)
        result = self.cursor.fetchone()
        return result

    def save(self, squad:Squad):
        command = f""" INSERT INTO SquadSuzuki
        (
            Name,
            Description,
            PeopleNumber,
            LanguageBackEnd,
            FrameworkFrontEnd,
        )
        VALUES
        (
            '{squad.name}',
            '{squad.description}',
            {squad.peopleNumber},
            '{squad.languageBackEnd}',
            '{squad.frameworkfrontend}

        )"""
        self.cursor.execute(command)
        self.connection.commit()
        id_inserted = self.cursor.lastrowid
        return id_inserted

    def change(self, squad:Squad):
        command = f""" UPDATE SquadSuzuki
        SET
            Name = '{squad.name}'
            Description = '{squad.description}'
            PeopleNumber = {squad.peopleNumber}
            LanguageBackEnd = '{squad.languageBackEnd}'
            FrameworkFrontEnd = '{squad.frameworkfrontend}'
        WHERE ID = {squad.id}
        """
        self.cursor.execute(command)
        self.cursor.commit()