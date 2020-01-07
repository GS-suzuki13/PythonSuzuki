# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

tripulacao_terminal = ['Piloto', 'Oficial 1', 'Oficial 2', 'Chefe de Serviço', 'Comissária 1', 'Comissária 2', 'Policial', 'Maykon']

mov_ida = '''MOVIMENTAÇÃO FORTWO
\033[32mTERMINAL   ->   AVIÃO\033[0;0m'''
mov_volta = '''MOVIMENTAÇÃO FORTWO
\033[32mAVIÃO   ->   TERMINAL\033[0;0m'''
terminal = 'Tripulantes no Terminal -> '
aviao = 'Tripulantes no Avião -> '
trip_aviao = []
bunito = '-'
viagem = 0


def viagem_fortwo():

    global viagem
    viagem += 1
    print(f'\033[32m{bunito *15} VIAGEM {viagem} {bunito * 15}\033[0;0m')
    print(f'EMBARQUE {viagem} (IN FORTWO)  --\033[31m {tripulacao_terminal[0]} e {tripulacao_terminal[1]}\033[0;0m')
    print(mov_ida)
    print(f'{terminal} {tripulacao_terminal[2:]}')
    input('|')
    trip_aviao.append(tripulacao_terminal.pop(1))
    print(f'{aviao} {trip_aviao}')
    print(f'{mov_volta} -- IN FORTWO:\033[33m {tripulacao_terminal[0]}\033[0;0m')
    print(f'\033[32m{bunito *15} VIAGEM {viagem} {bunito * 15}\033[0;0m\n')


    if len(tripulacao_terminal) == 3:
        tripulacao_terminal[0], tripulacao_terminal[1] = tripulacao_terminal[1], tripulacao_terminal[0]

    if len(tripulacao_terminal) == 6:
        tripulacao_terminal[0], tripulacao_terminal[1] = tripulacao_terminal[1], tripulacao_terminal[0]
    
    elif len(tripulacao_terminal) == 1:
        trip_aviao.append(tripulacao_terminal.pop(0))
        print(f'\033[32m{aviao} {trip_aviao}\033[0;0m\n')

        

for i in range(0,7):
    viagem_fortwo()



































