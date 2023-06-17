from flask import Blueprint, render_template, request, current_app, jsonify
from .msg_handlers import PrimaryMsgReceiver
import requests

jason_bot = Blueprint('jason bot', __name__, url_prefix='/jason_bot')


@jason_bot.route('/')
def index():
    return render_template('jason_bot.html')

@jason_bot.route('/wppbot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    msg_receiver = PrimaryMsgReceiver()
    current_app.logger.info('Going to bot page')
    req = request.values
    return str(msg_receiver.receive_and_response_msg(req))
