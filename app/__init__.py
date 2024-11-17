from flask import Flask, render_template
from logging import INFO
from flask_cors import CORS
import secrets 


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.logger.level = INFO
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jason.db'

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