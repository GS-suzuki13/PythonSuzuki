import sys
sys.path.append('c:/Users/Gustavo Suzuki/Desktop/PythonSuzuki/37-Aula37')
from Dao.squadDao import SquadDao
from Model.squadModel import Squad

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
            squad.languagebackend = s[3]
            squad.frameworkfrontend = s[5]
            list_squad.append(squad)
        return list_squad
    
    def search_for_id(self, id):
        s = self.dao.search_for_id(id)
        squad = Squad()
        squad = Squad()
        squad.id =  s[0]
        squad.name = s[1]
        squad.description = s[2]
        squad.peoplenumber = s[3]
        squad.languagebackend = s[3]
        squad.frameworkfrontend = s[5]
        return squad

    def save(self, squad:Squad):
        squad.id = self.squad_controller(save)
        return self.dao.save(squad)

    def change(self, squad:Squad):
        self.squad_controller.change(squad)
        self.dao.change

    def delete(self, id):
        self.dao.delete(id)
