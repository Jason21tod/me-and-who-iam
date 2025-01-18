from flask import Flask, render_template, request, redirect
from logging import INFO
from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from .scrapbot_api.resources.resources import MessagePort
from flask_cors import CORS


import secrets 
# ESTE CODIGO FOI CRIADO COM BASTANTE RAIVA

def create_app():
    app = Flask(__name__)
    cors = CORS()
    api = Api(app)

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

    from .email_services import email_service
    app.register_blueprint(email_service)
    from .scrapbot import scrapbot_page
    app.register_blueprint(scrapbot_page)

    api.add_resource(MessagePort, '/message_port')


    @app.route('/', methods=['GET'])
    def home():
        return redirect('https://jason-universe.vercel.app/')
    


    return app


if __name__ == '__main__':
    from werkzeug.serving import make_ssl_devcert
    make_ssl_devcert('./ssl', host='localhost')
    create_app().run(ssl_context=('./ssl.crt', './ssl.key'), debug=True)