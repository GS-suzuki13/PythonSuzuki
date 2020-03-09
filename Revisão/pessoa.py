from endereco import Endereco

class Pessoa:
    def __init__(self):
        self.__nome = " "
        self.__endereco = Endereco()
        self.__salario = 0.0

    def get_nome(self)->str:
        return self.__nome

    def set_nome(self, nome)->None:
        self.__nome = nome

    def get_idade(self)->int:
        return self.__idade

    def set_idade(self, idade:int)->None:
        self.__idade = idade

    def get_salario(self)->float:
        return self.__salario

    def set_salario(self, salario)->None:
        self.__salario = salario

    def salario(self, hora:int, custo:float):
        salario = int(hora) * float(custo)
        return salario
