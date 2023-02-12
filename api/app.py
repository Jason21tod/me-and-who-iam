import flask 
from flask import request
from logging import basicConfig, INFO
from logging import INFO, basicConfig, info


basicConfig(level=INFO, filename=r'api\logs\app.log')
app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('home_page.html')


@app.route('/jason_bot.html')
def jason_bot_page():
    info('Going to jason page')
    return flask.render_template('jason_bot.html')

@app.route('/bot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    from .msg_handlers import PrimaryMsgReceiver
    msg_receiver = PrimaryMsgReceiver()
    info('Going to bot page')
    req = request.values
    return str(msg_receiver.receive_and_response_msg(req))

def run_app():
    return app
    

if __name__ == '__main__':
    app.run(debug=True)