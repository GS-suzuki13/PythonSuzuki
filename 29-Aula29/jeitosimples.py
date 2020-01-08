# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

tripulacao_terminal = ['Piloto', 'Oficial 1', 'Oficial 2', 'Chefe de Serviço', 'Comissária 1', 'Comissária 2', 'Policial', 'Lula']

dentro_aviao = []

#------------- VIAGEM 1 ----------------
print(f'{tripulacao_terminal}')
print('Embarque 1:')
print(f'{tripulacao_terminal[0]} - {tripulacao_terminal[1]}')
print('Terminal -> Avião')
dentro_aviao.append(tripulacao_terminal.pop(1))
print(f'Dentro Do Avião{dentro_aviao}')
print(f'Dentro Do Terminal{tripulacao_terminal}')
print('\n')

#------------- VIAGEM 2 ----------------
print(f'{tripulacao_terminal}')
print('Embarque 2:')
print(f'{tripulacao_terminal[0]} - {tripulacao_terminal[1]}')
print('Terminal -> Avião')
dentro_aviao.append(tripulacao_terminal.pop(1))
print(f'Dentro Do Avião{dentro_aviao}')
print(f'Dentro Do Terminal{tripulacao_terminal}')
print('\n')

#------------- VIAGEM 3 ----------------
print(f'{tripulacao_terminal}')
print('Embarque 3:')
print(f'{tripulacao_terminal[0]} - {tripulacao_terminal[1]}')
print('Terminal -> Avião')
dentro_aviao.append(tripulacao_terminal.pop(0))
print(f'Dentro Do Avião{dentro_aviao}')
print(f'Dentro Do Terminal{tripulacao_terminal}')
print('\n')

#------------- VIAGEM 4 ----------------
print(f'{tripulacao_terminal}')
print('Embarque 4:')
print(f'{tripulacao_terminal[0]} - {tripulacao_terminal[1]}')
print('Terminal -> Avião')
dentro_aviao.append(tripulacao_terminal.pop(1))
print(f'Dentro Do Avião{dentro_aviao}')
print(f'Dentro Do Terminal{tripulacao_terminal}')
print('\n')


#------------- VIAGEM 5 ----------------
print(f'{tripulacao_terminal}')
print('Embarque 5:')
print(f'{tripulacao_terminal[0]} - {tripulacao_terminal[1]}')
print('Terminal -> Avião')
dentro_aviao.append(tripulacao_terminal.pop(1))
print(f'Dentro Do Avião{dentro_aviao}')
print(f'Dentro Do Terminal{tripulacao_terminal}')
print('\n')

#------------- VIAGEM 6 ----------------
print(f'{tripulacao_terminal}')
print('Embarque 6:')
print(f'{tripulacao_terminal[1]} - {tripulacao_terminal[2]}')
print('Terminal -> Avião')
dentro_aviao.append(tripulacao_terminal.pop(1))
dentro_aviao.append(tripulacao_terminal.pop(1))
print(f'Dentro Do Avião{dentro_aviao}')
print(f'Dentro Do Terminal{tripulacao_terminal}')
print('\n')

#------------- VIAGEM 7 ----------------
print(f'{tripulacao_terminal}')
print('Embarque 7:')
print(f'{dentro_aviao[1]}')
print('Terminal -> Avião')
tripulacao_terminal.append(dentro_aviao.pop(2))
print(f'Dentro Do Avião{dentro_aviao}')
print(f'Dentro Do Terminal{tripulacao_terminal}')
print('\n')

#------------- VIAGEM 8 ----------------
print(f'{tripulacao_terminal}')
print('Embarque 8:')
print(f'{tripulacao_terminal[0]} - {tripulacao_terminal[1]}')
print('Terminal -> Avião')
dentro_aviao.append(tripulacao_terminal.pop(1))
dentro_aviao.append(tripulacao_terminal.pop(0))
print(f'Dentro Do Avião{dentro_aviao}')
print(f'Dentro Do Terminal{tripulacao_terminal}')
print('\n')


