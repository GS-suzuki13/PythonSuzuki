import sys
sys.path.append(r'C:\Users\Gustavo Suzuki\Desktop\PythonSuzuki\37-Aula37')
from Dao.SquadDao import SquadDao
from Model.SquadModel import Squad

class SquadController:
    dao = SquadDao()
    
    def list_all(self):
        list_squad = []
        list_tuplas = self.dao.list_all()
        for s in list_tuplas:
            squad = Squad()
            squad.id =  s[0]
            squad.name = s[1]
            squad.description = s[2]
            squad.peoplenumber = s[3]
            squad.languagebackend = s[4]
            squad.frameworkfrontend = s[5]
            list_squad.append(squad)
        return list_squad
    
    def search_for_id(self, id):
        s = self.dao.search_for_id(id)
        squad = Squad()
        # squad.create(*s)
        squad.id =  s[0]
        squad.name = s[1]
        squad.description = s[2]
        squad.peoplenumber = s[3]
        squad.languagebackend = s[4]
        squad.frameworkfrontend = s[5]
        return squad

    def save(self, squad:Squad):
        self.dao.save(squad)

    def change(self, squad:Squad):
        self.dao.change(squad)

    def delete(self, id1):
        self.dao.delete(id1)
