from decouple import config
from flask import Flask
from talkshow.ext import cli


def create_app():
    ''' Creates a new Flask app. '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config('SECRET_KEY')
    # extensions
    cli.configure(app)
    return app
