valores = input().split(" ")

if int(valores[1]) > int(valores[2]) and int(valores[3]) > int(valores[0]):
    if (int(valores[2])+int(valores[3])) > (int(valores[0])+int(valores[1])):
        if int(valores[2]) and int(valores[3]) > 0:
            if (int(valores[0])%2) == 0:
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")\