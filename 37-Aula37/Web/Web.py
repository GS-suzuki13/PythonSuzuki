from flask import Flask, render_template, request, redirect
import sys
sys.path.append(r'C:\Users\900142\Desktop\PythonSuzuki\37-Aula37')

from Controller.squadController import SquadController
from Model.SquadModel import Squad

app = Flask(__name__)
squad_controller = SquadController()
name = 'Squads HBSIS'

@app.route('/')
def inicio():
    return render_template('index.html', title_app = name)

@app.route('/list')
def list():
    squad = squad_controller.list_all()
    return render_template('list.html', title_app = name, lista = squad)

@app.route('/register')
def register():
    squad = Squad()
    if 'id' in request.args:
        id1 = request.args['id']
        squad = squad_controller.search_for_id(id1)
    return render_template('register.html', title_app = name, squad = squad)

@app.route('/delete')
def delete():
    id1 = int(request.args['id'])
    squad_controller.delete(id1)
    return redirect('/list')

@app.route('/save')
def salvar():
    squad = Squad()
    squad.create(**dict(request.args))
    # request.args.to_dict()

    # squad.id = request.args['id'] 
    # squad.name = request.args['name']
    # squad.description = request.args['description']
    # squad.peoplenumber = request.args['peoplenumber']
    # squad.languagebackend = request.args['languagebackend']
    # squad.frameworkfrontend = request.args['frameworkfrontend']

    if squad.id == 0:
        squad_controller.save(squad)
    else:
        squad_controller.change(squad)
    return redirect('/list')

app.run(debug=True)