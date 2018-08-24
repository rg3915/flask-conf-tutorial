from flask import Flask
from flask import jsonify
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Olá mundo!'


@app.route('/rota1')
def view_da_rota1():
    return 'Nova rota!'


@app.route('/rota2/<nome>')
def view_da_rota2(nome):
    return 'Bem vindo, ' + nome + '! Essa é a view da /rota2!'


@app.route("/ola/<nome>")
def view_com_template(nome):
    return render_template("index.html", nome=nome)


@app.route("/api")
def view_com_json():
    return jsonify({"mensagem": "Bem vindo a sua primeira API REST!"})
