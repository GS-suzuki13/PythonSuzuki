# Aula 21 - 09-12-2019

# Crie uma classe cliente:

# 1) deve ter como atributos: codigo, cpf, nome, idade, sexo

# 2) como metodos: receber salario, comprar, pagar divida

# Quando recebe aumenta o dinheiro na carteira.

# quando compra aumenta os bens e diminui o dinheiro na carteira

# Se comprar e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira
# e aumentar a divida.

# Para pagar a divida tem que ter dinheiro o suficiente na carteira

# 3) atributos de estado: dinheiro na carteira, divida, bens

salario = float(input('Digite o salário a receber: '))
compras = float(input('Digite o valor da compra: '))


class Cliente:
    def __init__(self,codigo1, cpf1, nome1, idade1, sexo1):

        self.nome = nome1
        self.idade = idade1
        self.cpf = cpf1
        self.codigo = codigo1
        self.sexo = sexo1

        self.divida = 0
        self.carteira = 0
        self.bens = 0
    
    def receber (self, dinheiro):
        self.carteira += dinheiro
    
    def comprar (self, dinheiro):
        self.bens += dinheiro
        self.carteira -= dinheiro
        if self.carteira < 0:
            self.divida = (self.divida - self.carteira)
            self.carteira = 0

    def pagar_divida(self):
        if self.divida > 0:
            if self.carteira >= self.divida:
                self.carteira -= self.divida
                self.divida = 0
            elif self.carteira < self.divida:
                print('Não há dinheiro suficiente!')
        else:
            print('Não tem divida')
        
p = Cliente (900142, '08987839923','Gustavo Suzuki', 18, 'M')

p.receber(salario)
p.comprar(compras)


print(f'Nome: {p.nome}')
print(f'Idade: {p.idade}')
print(f'Sexo: {p.sexo}')
print(f'CPF: {p.cpf}')
print(f'Carteira: {p.carteira}')


