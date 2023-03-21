from flask import request, Flask, render_template, redirect
from logging import basicConfig, INFO
from logging import INFO, basicConfig, info


basicConfig(level=INFO, filename=r'api\logs\app.log')
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    info(request.form)
    return render_template('home_page.html')

@app.route('/home_page.html', methods=['GET', 'POST'])
def form_post():
    info(request.form)
    return redirect('home_page.html')



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