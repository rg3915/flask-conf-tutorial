from decouple import config
from flask import Flask
from talkshow.ext import cli
from talkshow.ext import db
from talkshow.ext import bootstrap
from talkshow.blueprints import webui


def create_app():
    ''' Creates a new Flask app. '''
    app = Flask(__name__)
    # config
    app.config['SECRET_KEY'] = config('SECRET_KEY')
    # extensions
    db.configure(app)  # importante: o db deve vir primeiro.
    cli.configure(app)
    bootstrap.configure(app)
    # blueprints
    webui.configure(app)
    return app
