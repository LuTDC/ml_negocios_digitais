from flask import Flask

import sentimentos
import casas

app = Flask(__name__)

@app.route('/')
def home():
    return 'App'

@app.route('/sentimento/<frase>')
def analisar_sentimento(frase):
    polaridade = sentimentos.analisar(frase)
    return 'A polaridade é ' + str(polaridade)

@app.route('/cotacao/<int:tamanho>')
def cotacao(tamanho):
    modelo = casas.treinar_modelo()
    return 'O preço da casa é R$' + str(round(casas.prever_preco(modelo, [[tamanho]])[0], 2))

app.run(debug=True)