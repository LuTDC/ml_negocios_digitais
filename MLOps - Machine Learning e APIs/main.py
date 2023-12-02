from flask import Flask

import Projeto

app = Flask(__name__)

@app.route('/')
def home():
    return 'App'

@app.route('/sentimento/<frase>')
def analisar_sentimento(frase):
    polaridade = Projeto.analisar(frase)
    return 'A polaridade é ' + str(polaridade)

app.run(debug=True)