from flask import Blueprint, render_template, request, current_app
from .wpp_sys import first_msg_receiver

jason_bot = Blueprint('jason bot', __name__, url_prefix='/jason_bot')


@jason_bot.route('/')
def index():
    return render_template('jason_bot.html')

@jason_bot.route('/wppbot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    current_app.logger.info('Going to bot page')
    req = request.values
    return str(first_msg_receiver.process_msg(req))
