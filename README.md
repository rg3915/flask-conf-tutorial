# flask-conf-tutorial

FlaskConf Tutorial https://2018.flask.python.org.br/tutorial.html

## Basic

[Tutorial](https://docs.google.com/presentation/d/1evXzneWfo9MeAbSu5mwBmKjvnTLnT1eYBfv7Ce9PoHE/edit#slide=id.p2)

Para executar o `hello.py` digite:

```
export FLASK_APP=hello.py
flask run
```

## [Tutorial Talkshow](https://github.com/rochacbruno/talkshow/)

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

### DB

```
$ flask shell
>>> app.db
>>> app.db['events']
>>> app.db['events'].insert({'name': 'FlaskConf', 'date': '2018-08-24'})
>>> app.db['events'].find()  # É um generator
>>> app.db['events'].find_one({'name': 'FlaskConf'})
```



#### Blueprint

```
blueprints/webui.py
```

```
pip install flask-bootstrap flask-wtf
```


## API REST

```
http --form POST localhost:5000/api/v1/event/ name="JSConf"
```

URL

```
http://localhost:5000/api/v1/event/
```

### Docs

```
http://localhost:5000/apidocs/
```


### Login


#### Criando um usuário

```
flask adduser -u "admin" -p 1234
```