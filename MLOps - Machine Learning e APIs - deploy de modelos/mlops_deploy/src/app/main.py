from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

import config

import sentimentos
import casas

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = config.BASIC_AUTH_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = config.BASIC_AUTH_PASSWORD

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
@basic_auth.required
def treinar_modelo_cotacao():
    casas.treinar_modelo()

    return 'OK'

@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados = [dados[key] for key in dados.keys()]

    preco = round(casas.prever_preco([dados])[0], 2)

    return jsonify(preco=preco) 

app.run(debug=True, host='0.0.0.0')