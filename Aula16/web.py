from flask import Flask, render_template
from faixa import ler_faixa
app  = Flask(__name__)


@app.route('/lista')
def listar_faixa():
    return render_template("lista.html", nome = 'Lista de faixas', lista = ler_faixa())


app. run()