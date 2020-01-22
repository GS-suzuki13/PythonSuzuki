import MySQLdb
from Model.SquadModel import Squad

class SquadDao:
    connection = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = connection.cursor()
   
    def list_all(self):
        command = f'SELECT *'