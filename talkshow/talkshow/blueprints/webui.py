from flask import Blueprint
from flask import render_template
from flask import current_app as app


bp = Blueprint("webui", __name__)


@bp.route('/')
def index():
    """View to list all registered events"""
    events = app.db['events'].find()
    return render_template('index.html', events=events)


def configure(app):
    app.register_blueprint(bp)
