def calculo_iss (ds):
    custo = ds * 0.05
    return custo

def calculo_juros (juros):
    juros_dividido = juros/100
    return juros_dividido

def calculo_montante (investido, juros_dividido, periodo):
    restante = investido * ((1 + juros_dividido)**periodo)
    return restante

def calculo_porcentagem (juros_dividido):
    juros_porcentagem = juros_dividido*100
    return juros_porcentagem

def calculo_mensal (investido, juros_dividido):
    restante = (investido * ((1 + juros_dividido)**1)) - investido
    return restante
    

# Save all
