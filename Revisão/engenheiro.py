from pessoa import Pessoa


class Engenheiro(Pessoa):
    def __init__(self):
        super().__init__()
        self.__horas = 0
        self.__custo = 0.0

    def get_hora(self) -> int:
        return self.__horas

    def set_hora(self, horas: int) -> None:
        self.__horas = horas

    def get_salario(self) -> float:
        return self.__salario

    def set_salario(self, salario) -> None:
        self.__salario = salario

    def salario(self, hora:int, custo:float):
        salario = int(hora) * float(custo)
        return salario