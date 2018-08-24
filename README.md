# flask-conf-tutorial

FlaskConf Tutorial https://2018.flask.python.org.br/tutorial.html

## Basic

[Tutorial](https://docs.google.com/presentation/d/1evXzneWfo9MeAbSu5mwBmKjvnTLnT1eYBfv7Ce9PoHE/edit#slide=id.p2)

Para executar o `hello.py` digite:

```
export FLASK_APP=hello.py
flask run
```

## Tutorial Talkshow

Instalando os pacotes a partir do `setup.py`.

```
pip install -e .
```

#### Variáveis de ambiente

No arquivo `.env`

```
FLASK_APP=talkshow/app.py
FLASK_ENV=development
```

Depois digite:

```
$ flask run
```

#### Rotas

```
$ flask routes
```

#### Shell

```
$ flask shell
```

### Evento

```
flask addevent -n "FlaskConf" -d 2018-08-24
```

