from flask import Blueprint, render_template, request, current_app, redirect
from .wpp_sys import first_msg_receiver
from.db import db, ConversationRegister

jason_bot = Blueprint('jason bot', __name__, url_prefix='/jason_bot')


@jason_bot.route('/')
def index():
    return render_template('jason_bot.html')

@jason_bot.route('/wppbot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    current_app.logger.info(f'Going to bot page -> {request.values}')
    req = request.values
    return str(first_msg_receiver.process_msg(req))


@jason_bot.route('/data_input', methods=['GET', 'POST'])
def form_input() -> str:
    return render_template('data_input.html')

def register_user_data(request):
    try:
        model = ConversationRegister(
            identification = request.values.get('celphone'),
            name = request.values.get('name')
        )
        db.session.add(model)
        db.session.commit()
    except:
        current_app.logger.warning('Não foi possível adicionar esses dados... já adicionados...')
    finally:
        return redirect('/jason_bot/data_input')