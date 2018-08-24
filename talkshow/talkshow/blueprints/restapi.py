from flask import Blueprint
from flask import current_app as app
from flask_restful import Api, Resource, reqparse
# from flask_simplelogin import login_required

bp = Blueprint('restapi', __name__, url_prefix='/api/v1')
api = Api(bp)


event_post_parser = reqparse.RequestParser()
event_post_parser.add_argument('name', required=True)
event_post_parser.add_argument('date', required=True)


class Event(Resource):

    def get(self):
        return {'events': list(app.db['events'].find())}

    # @login_required(basic=True)
    def post(self):
        """
        Creates new event
        ---
        parameters:
          - in: body
            name: body
            schema:
              id: Event
              properties:
                name:
                  type: string
                date:
                  type: string
        responses:
          201:
            description: Success or failure message
            schema:
              properties:
                event_created:
                  type: string
                  description: The id of the created event
        """
        event = event_post_parser.parse_args()
        new = app.db['events'].insert({'name': event.name, 'date': event.date})
        return {'event_created': new.inserted_id}, 201


proposal_post_parser = reqparse.RequestParser()
proposal_post_parser.add_argument('name', required=True)
proposal_post_parser.add_argument('email', required=True)
proposal_post_parser.add_argument('title', required=True)
proposal_post_parser.add_argument('description', required=True)


class EventItem(Resource):

    def get(self, event_id):
        event = app.db['events'].find_one({'_id': event_id})
        proposals = app.db['proposal'].find({'event_id': event_id})
        return {'event': event, 'proposals': list(proposals)}

    def post(self, event_id):
        event = app.db['events'].find_one({'_id': event_id})
        prop = proposal_post_parser.parse_args()
        new = app.db['proposal'].insert({
            'event_id': event['_id'],
            'name': prop.name,
            'email': prop.email,
            'title': prop.title,
            'description': prop.description,
            'approved': False
        })
        return {'proposal created': new.inserted_id}, 201


def configure(app):
    """Initialize API and register blueprint"""
    api.add_resource(Event, '/event/')
    api.add_resource(EventItem, '/event/<event_id>')

    app.register_blueprint(bp)
