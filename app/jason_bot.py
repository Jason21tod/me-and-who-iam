from flask import Blueprint, render_template,session, request, current_app, redirect
from .wpp_sys import first_msg_receiver
from.db import db, ConversationRegister, verify_is_in_db
import json

jason_bot = Blueprint('jason bot', __name__, url_prefix='/jason_bot')


@jason_bot.route('/')
def index():
    return render_template('jason_bot.html')

@jason_bot.route('/wppbot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    current_app.logger.info(f'Going to bot page -> {request.values}')
    req = request.values
    register_number(req.get('From'))
    return str(first_msg_receiver.process_msg(req))


@jason_bot.route('/data_input', methods=['GET', 'POST'])
def form_input() -> str:
    return render_template('data_input.html')

@jason_bot.route('/save_data', methods=['GET', 'POST'])
def save_data():
    print(request.values)
    if verify_is_in_db(request.values):
        create_session(request.values)
        return redirect('/jason_bot/data_input')
    else:
        return register_user_data(request=request)

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

def register_number(number):
    if number_is_registered(number):
        return
    with open(r'app\wpp_sys\users_chats.json', '+r', encoding='UTF-8') as arq:
        data:list = json.load(arq)
    data.append({number: []})
    with open(r'app\wpp_sys\users_chats.json', '+w', encoding='UTF-8') as arq:
        json.dump(data, arq, indent=2)

def number_is_registered(number):
    with open(r'app\wpp_sys\users_chats.json', '+r', encoding='UTF-8') as arq:
        data:list = json.load(arq)
        for item in data:
            if number in item:
                return True
        return False

def create_session(request_values):
    session_objt = ConversationRegister.query.filter_by(identification=request_values.get('celphone')).all()
    session['identification'] = session_objt[0].identification
    session['name'] = session_objt[0].name
    current_app.logger.info('Sessão criada com sucesso')
    return session
