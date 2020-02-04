from flask_restful import Resource
from flask import request


from PythonSuzuki.Aula51.Dao.SuzukiDao import SmartphoneDao
from PythonSuzuki.Aula51.Model.SuzukiModel import SmartphoneModel

class SuzukiController(Resource):
    def __init__(self):
        self.dao = SmartphoneDao

    def get(self,id=None):
        if id:
            return self.dao.search_for_id(id)
        return self.dao.list_all()

    def post(self):
        name = request.json['name']
        model = request.json['model']
        date = request.json ['date']
        smartphone = SmartphoneModel(name, model, date)
        return self.dao.insert(smartphone)

    def put(self, id):
       name = request.json['name']
       model = request.json['model']
       date = request.json['date']
       smartphone = SmartphoneModel(name, model, date, id)
       return self.dao.change(smartphone)

    def delete(self, id):
       return self.dao.delete(id)

