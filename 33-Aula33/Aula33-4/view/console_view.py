import sys
sys.path.append('33-Aula33/Aula33-4')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)