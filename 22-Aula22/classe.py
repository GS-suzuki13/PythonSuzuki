# # 1) O que uma pessoa Tem? Quais as caracteristicas? 
# ##### Atributos ---- variaveis
# nome
# idade
# telefone
# sexo


# # 2) O que uma pessoa faz? 
# ##### Métodos (Função/procedimento)
# respira
# dorme
# corre
# come
# bebe
# multiplica

# # 3) Como a pessoa está agora? 
# ##### Atributos de estado - Variáveis
# divida
# cansada
# viva
# fome
# sede


class Pessoa:
    '''
    Esta classe é uma demonstração para aula
    '''

    def __init__(self, nome1, idade1, telefone1, sexo1):
        '''
        O __init__ é o motor que irá iniciar as variáveis da classe
        O self é o que irá conectar toda a classe
        '''
        ####### Atributos #######
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1
        ##########################
        self.divida = None
        self.cansada = 'Não'
        self.viva = True
        self.fome = 'Não'
        self.sede = 'Não'

    #### Metdos ###
    def respira (self, respirar):

        if self.viva == True:
            if respirar == True:
                self.viva == True
            else:
                self.viva == False

    def corre (self, distancia):
        if self.viva:
            if distancia >= 50 and distancia < 100:
                self.cansada = 'Pouco'
                self.sede = 'Pouco'
                self.fome = 'Pouco'
            elif distancia >= 100 and distancia < 200:
                self.cansada = 'Médio'
                self.sede = 'Médio'
                self.fome = 'Médio'
            elif distancia >= 100 and distancia < 200:
                self.cansada = 'Muito'
                self.sede = 'Muito'
                self.fome = 'Muito'

    def dorme (self):
        if self.viva:
            self.cansada = 'Não'

    def bebe (self):
        if self.viva:
            self.sede = 'Não'

    def come (self):
        if self.viva:
            self.fome = 'Não'


    def multiplica (self):
        pass


p = Pessoa('Gustavo Suzuki', 18, '997609807', 'M')

p.corre (50)
p.come()
p.bebe()
p.dorme()

print(f'Nome é: {p.nome}')
print(f'Você está vivo?: {p.viva}')
print(f'Está com fome?: {p.fome}')
print(f'Está com sede?: {p.sede}')
print(f'Está cansada?: {p.cansada}')


# class Pessoa:
#     ''' 
#     Classe demonstrativo para compreenção de como 
#     montar uma classe pessoa
#     '''
#     def __init__ (self,nome1,cpf1,data_de_nascimento1,altura1,salario1,endereço1):
#         ''' 
#         __init__ é o construtor da classe. Ela é responsável por
#         inicializar as variáveis impostantes para poder trabalhar com classe.
#         '''
#         ################################ Atributos
#         self.nome = nome1
#         self.cpf = cpf1
#         self.data_de_nascimento = data_de_nascimento1
#         self.altura = altura1
#         self.salario = salario1
#         self.endereço = endereço1
#         ############################### Atributos de estado
#         # Estado da pessoa
#         self.fome = None
#         self.sede = None
#         self.exausta = None

    
#     def correr(self,distancia):
#         '''
#         Adicione a distância em metros percorrida
#         '''
#         if distancia <= 50:
#             self.exausta = 'não'
#         elif distancia > 50 and distancia < 200:
#             self.exausta = 'levemente exausta'
#             self.sede = 'pouca'
#             self.fomr = 'pouca'
#         else:
#             self.exausta = 'exausta'
#             self.sede = 'muita'
#             self.fome = 'muita'
        

#     def beber(self,litro):
#         '''
#         Metodo para melhorar o status de sede
#         '''
#         if litro > 0.5 and litro < 1:
#             if self.sede == None or 'não':
#                 self.sede = 'não'
#             elif self.sede == 'pouca':
#                 self.sede = 'não'
#             elif self.sede == 'muita':
#                 self.sede = 'pouca'
#         elif litro >= 1:
#             if self.sede == None or 'não':
#                 self.sede = 'não'
#             elif self.sede == 'pouca':
#                 self.sede = 'não'
#             elif self.sede == 'muita':
#                 self.sede = 'não'

#     def comer(self):
#         self.fome = 'não'

#     def descansar(self,tempo):
#         if tempo < 5:
#             if self.exausta == None or 'não':
#                 self.exausta = 'não'
#             elif self.exausta == 'levemente exausta':
#                 self.exausta = 'não'
#             elif self.exausta == 'exausta':
#                 self.exausta = 'levemente exausta'
#         elif tempo >=5 :
#             if self.exausta == None or 'não':
#                 self.exausta = 'não'
#             elif self.exausta == 'levemente exausta':
#                 self.exausta = 'não'
#             elif self.exausta == 'exausta':
#                 self.exausta = 'não'

#     def jantar_noitesono(self):
#         self.exausta = 'não'
#         self.fome = 'não'
#         self.sede = 'não'


# ### Exemplo de uso de classe...

# pessoa1 = Pessoa('Alberto','04304304322','22/06/2001',198,1500.00,'R. Itapé, 20')


# # print(f'Exausta: {pessoa1.exausta}')
# # print(f'Sede: {pessoa1.sede}')
# # print(f'fome: {pessoa1.fome}')


# pessoa1.correr(300)

# print(f'Exausta: {pessoa1.exausta}')
# print(f'Sede: {pessoa1.sede}')
# print(f'fome: {pessoa1.fome}')

# #pessoa1.beber(1)

# # print(f'Exausta: {pessoa1.exausta}')
# # print(f'Sede: {pessoa1.sede}')
# # print(f'fome: {pessoa1.fome}')

# #pessoa1.comer()

# # print('\n')
# # print(f'Exausta: {pessoa1.exausta}')
# # print(f'Sede: {pessoa1.sede}')
# # print(f'fome: {pessoa1.fome}')

# #pessoa1.descansar(4)
# pessoa1.jantar_noitesono()

# print('\n')
# print(f'Exausta: {pessoa1.exausta}')
# print(f'Sede: {pessoa1.sede}')
# print(f'fome: {pessoa1.fome}')