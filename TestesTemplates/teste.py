class Viagem:

    def __init__ (self):
        self.fortwo = False
        self.aviao = False

        self.tripulacao_total = ['Piloto', 'Oficial 1', 'Oficial 2', 'Chefe de Serviço', 'Comissária 1', 'Comissária 2', 'Policial', 'Lula']
        self.tripulacao_possivel = []
        self.dentro_aviao = []
        self.dentro_fortwo = []
        self.tripulante1 = self.tripulacao_total[0]
        self.tripulante2 = self.tripulacao_total[3]
        self.tripulante3 = self.tripulacao_total[6]

    def embarque_fortwo (self, motorista):
        if self.fortwo == True:
                                    
            if self.tripulante1 == motorista:
                self.tripulacao_possivel.append(self.tripulacao_total[1:4])
                print('Terminal -> Avião')
                print(f'{self.tripulante1} - {self.tripulacao_possivel.pop(0)}')
                print(f'{self.tripulante1} - {self.tripulacao_possivel.pop(0)}')
                print(f'{self.tripulante1} - {self.tripulacao_possivel.pop(0)}')
            elif self.tripulante2 == motorista:
                self.tripulacao_possivel.append(self.tripulacao_total[4:5])
            elif self.tripulante3 == motorista:
                self.tripulacao_possivel.append(self.tripulacao_total[7])

        else:
            pass


viagem_classe = Viagem()
viagem_classe.embarque_fortwo('motorista')
