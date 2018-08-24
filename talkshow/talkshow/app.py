from decouple import config
from flask import Flask
from talkshow.ext import cli
from talkshow.ext import db
from talkshow.ext import bootstrap
from talkshow.ext import admin
from talkshow.ext import login
from talkshow.ext import apidocs
from talkshow.blueprints import webui
from talkshow.blueprints import restapi


def create_app():
    ''' Creates a new Flask app. '''
    app = Flask(__name__)
    # config
    app.config['SECRET_KEY'] = config('SECRET_KEY')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    # extensions
    db.configure(app)  # importante: o db deve vir primeiro.
    login.configure(app)
    cli.configure(app)
    bootstrap.configure(app)
    admin.configure(app)
    apidocs.configure(app)
    # blueprints
    webui.configure(app)
    restapi.configure(app)
    return app
