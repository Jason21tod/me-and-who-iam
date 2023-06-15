from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    from .jason_bot import jason_bot
    app.register_blueprint(jason_bot)

    from .email_services import email_service
    app.register_blueprint(email_service)


    @app.route('/', methods=['GET', 'POST'])
    def home():
        return render_template('home_page.html')

    return app


if __name__ == '__main__':
    create_app.run(debug=True)