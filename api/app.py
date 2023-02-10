import flask 
from flask import request
from logging import basicConfig, INFO
from libs.msg_handlers import PrimaryMsgReceiver
from logging import INFO, basicConfig, info

basicConfig(level=INFO)

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/jason_bot.html')
def jason_bot_page():
    info('Going to jason page')
    return flask.render_template('jason_bot.html')

msg_receiver = PrimaryMsgReceiver()

basicConfig(level=INFO)


@app.route('/bot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    
    info('Going to bot page')
    req = request.values
    return str(msg_receiver.receive_and_response_msg(req))

def run_app():
    return app
    

if __name__ == '__main__':
    app.run(debug=True)