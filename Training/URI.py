# N = int(input())
# N(0<N<1000000.00)
#
# #notas 100
# n100 = N // 100
# r100 = N % 100
# #notas 50
# n50 = r100 // 50
# r50 = r100 % 50
# #notas 20
# n20 = n50 // 20
# r20 = n50 % 20
# #notas 10
# n10 = r20 // 10
# r10 = r20 % 10
# #notas 5
# n5 = r10 // 5
# r5 = r10 % 5
# #notas 2
# n2 = r5 // 2
# r2 = r5 % 2
# #moedas 1
# m1 = r2 // 1
# r1 = r2 % 1
# #moedas 0.50
# m05 = r1 // 0.50
# r050 = r1 % 0.50
# #moedas 0.25
# m25 = r050 // 0.25
# r025 = r050 % 0.25
# #moedas 0.10
# m10 = r025 // 0.10
# r010 = r025 % 0.10
# #moedas 0.05
# m005 = r010 // 0.05
# r005 = r010 % 0.05
# #moedas 0.01
# m001 = r005 // 0.01
# print('NOTAS:')
# print('{} nota(s) de R$ 100.00'.format(int(n100)))
# print('{} nota(s) de R$ 50.00'.format(int(n50)))
# print('{} nota(s) de R$ 20.00'.format(int(n20)))
# print('{} nota(s) de R$ 10.00'.format(int(n10)))
# print('{} nota(s) de R$ 5.00'.format(int(n5)))
# print('{} nota(s) de R$ 2.00'.format(int(n2)))
# print('MOEDAS:')
# print('{} moeda(s) de R$ 1.0'.format(int(m1)))
# print('{} moeda(s) de R$ 0.5'.format(int(m05)))
# print('{} moeda(s) de R$ 0.25'.format(int(m25)))
# print('{} moeda(s) de R$ 0.10'.format(int(m10)))
# print('{} moeda(s) de R$ 0.05'.format(int(m005)))
# print('{} moeda(s) de R$ 0.01'.format(int(m001)))

N = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    troco = int(N / nota)
    print("{} nota(s) de R$ {:.2f}".format(troco, nota))
    N -= troco * nota

print("MOEDAS:")
for moeda in moedas:
    troco = int(round(N, 2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(troco, moeda))
    N -= troco * moeda
