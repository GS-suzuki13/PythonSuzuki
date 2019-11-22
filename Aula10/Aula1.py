# Aula 10 - 20 - 11 - 2019 -
# --- WEB - Calculadora ---
nome_pagina = 'Suzuki Perfeito'
from flask import Flask, render_template, request
from exercicio import *

app =  Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo=nome_pagina)


@app.route('/calcular')
def calcular():
    n1 = int(request.args['n1'])
    n2 = int(request.args['n2'])
    r_soma = soma (n1,n2)
    r_subtracao = subtracao (n1,n2)
    r_multiplicacao = multiplicacao (n1,n2)
    r_divisao = divisao (n1,n2)
    r_divi_inteira = divi_inteira (n1,n2)
    r_resto = resto (n1,n2)
    r_raiz = raiz (n1,n2)
    r_resultados = {'soma':r_soma, 'subtracao':r_subtracao, 'multiplicacao':r_multiplicacao, 'divisao':r_divisao, 'divi_inteira':r_divi_inteira, 'resto':r_resto, 'raiz':r_raiz}
    
    return render_template('resultado.html', resultados = r_resultados, n1= n1, n2= n2)

app.run()
