from flask import Flask, render_template, request, redirect
from logging import INFO
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


    @app.before_request
    def redirect_to_https():
        if not request.is_secure and request.headers.get('X-Forwarded-Proto', 'http') != 'https':
            url = request.url.replace("http://", "https://", 1)
            return redirect(url, code=301)
    

    app.secret_key = secrets.token_hex(50)
    print(app.secret_key)

    from .email_services import email_service
    app.register_blueprint(email_service)



    @app.route('/', methods=['GET', 'POST'])
    def home():
        return render_template('home_page.html')

    return app


if __name__ == '__main__':
    create_app().run(debug=True)