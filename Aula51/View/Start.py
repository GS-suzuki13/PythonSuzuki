from flask import Flask
from flask_restful import Api

from PythonSuzuki.Aula51.Controller.SuzukiController import SuzukiController

app = Flask(__name__)
api = Api(app)

api.add_resource(SuzukiController, '/api/smartphone', endpoint='smartphones')
api.add_resource(SuzukiController, '/api/smartphone/<int:id>', endpoint='smartphone')

app.run(debug=True)