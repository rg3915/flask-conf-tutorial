from flask import Flask
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
