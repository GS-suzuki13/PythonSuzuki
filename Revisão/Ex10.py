# Crie uma classe pessoa
# Crie dois atributos para a classe: Nome, Sobrenome
# Crie 4 comportamentos:
#         1 - get_nome(): - > Não Implementado
#         2 - get_sobrenome(): - > Não Implementado
#         3 - set_nome(): - > Não Implementado
#         4 - set_nome(): - > Não Implementado

class Endereco:
    def __init__(self):
        self.__logradouro = ""
        self.__numero = ""
        self.__bairro = ""

    def get_logradouro(self)->str:
        return self.__logradouro

    def get_numero(self)->str:
        return self.__numero

    def get_bairro(self)->str:
        return self.__bairro

    def set_logradouro(self, logradouro)->None:
        self.__logradouro = logradouro

    def set_numero(self, numero)->None:
        self.__numero = numero

    def set_bairro(self, bairro)->None:
        self.__bairro = bairro