from flask import Flask, render_template, request, redirect
from logging import INFO
from flask_cors import CORS
from flask import Flask
from flask_restful import Resource, Api
from .scrapbot_api.resources.resources import MessagePort
from flask_cors import CORS


import secrets 
# ESTE CODIGO FOI CRIADO COM BASTANTE RAIVA

def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.logger.level = INFO
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jason.db'
    cors.init_app(app)

    @app.before_request
    def enforce_www():
        if request.host == 'jasonuniverse.com.br':
            url = request.url.replace('jasonuniverse.com.br', 'www.jasonuniverse.com.br', 1)
            return redirect(url, code=301)
        if not request.is_secure and request.headers.get('X-Forwarded-Proto', 'http') != 'https':
            url = request.url.replace("http://", "https://", 1)
            return redirect(url, code=301)
    

    app.secret_key = secrets.token_hex(50)
    print(app.secret_key)

    from .email_services import email_service
    app.register_blueprint(email_service)

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

    api.add_resource(MessagePort, '/message_port')


    @app.route('/', methods=['GET', 'POST'])
    def home():
        return render_template('home_page.html')

    return app


if __name__ == '__main__':
    create_app().run(debug=True)