from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Olá mundo!'


@app.route('/rota1')
def view_da_rota1():
    return 'Nova rota!'
