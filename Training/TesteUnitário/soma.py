from unittest import TestCase


def soma(x, y):
    result = x + y
    return result


assert soma(2,2) == 4

class Pessoa():
    def __init__(self, nome:str, sobrenome:str)-> None:
        self.nome = nome
        self.sobrenome = sobrenome