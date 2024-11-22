from flask import Flask
from flask_restful import Resource, Api
from .resources.resources import MessagePort
from flask_cors import CORS

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
    'UnsupportedMediaType': {
        'message': 'No content supported on our database, please try another type :D',
        'status': 415
    }

}


app = Flask(__name__)
CORS(app)
api = Api(app, errors=errors)

class HelloWorld(Resource):
    """Add a resource of our API"""
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(MessagePort, '/message_port')


if __name__ == '__main__':
    app.run(debug=True)

