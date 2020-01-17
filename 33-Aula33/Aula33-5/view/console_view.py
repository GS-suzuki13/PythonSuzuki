import sys
sys.path.append('33-Aula33/Aula33-5')
from controller.endereco_controller import EnderecoController

ec = EnderecoController()

for e in ec.listar_todos():
    print(e)