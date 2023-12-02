from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

import sentimentos
import casas

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'luana'
app.config['BASIC_AUTH_PASSWORD'] = 'luana'

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return 'App'

@app.route('/sentimento/<frase>')
@basic_auth.required
def analisar_sentimento(frase):
    polaridade = sentimentos.analisar(frase)
    return 'A polaridade é ' + str(polaridade)

@app.route('/treinar_modelo_cotacao/')
def treinar_modelo_cotacao():
    casas.treinar_modelo()

    return 'OK'

@app.route('/cotacao/', methods=['POST'])
def cotacao():
    dados = request.get_json()
    dados = [dados[key] for key in dados.keys()]

    preco = round(casas.prever_preco([dados])[0], 2)

    return jsonify(preco=preco) 

app.run(debug=True)