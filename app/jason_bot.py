from flask import Blueprint, render_template,session, request, current_app, redirect
from .wpp_sys import first_msg_receiver
from.db import db, ConversationRegister

jason_bot = Blueprint('jason bot', __name__, url_prefix='/jason_bot')


@jason_bot.route('/')
def index():
    return render_template('jason_bot.html')

@jason_bot.route('/wppbot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    current_app.logger.info('Going to bot page')
    req = request.values
    return str(first_msg_receiver.process_msg(req))


@jason_bot.route('/data_input', methods=['GET', 'POST'])
def form_input() -> str:
    return render_template('data_input.html')

@jason_bot.route('/save_data', methods=['GET', 'POST'])
def save_data():
    print(request.values)
    if verify_is_logged(request.values):
        create_session(request.values)
        return redirect('/jason_bot/data_input')
    else:
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

def verify_is_logged(request_values):
    result = ConversationRegister.query.filter_by(identification=request_values.get('celphone')).first()
    if result == None:
        return False
    return True

def create_session(request_values):
    session_objt = ConversationRegister.query.filter_by(identification=request_values.get('celphone')).all()
    session['identification'] = session_objt[0].identification
    session['name'] = session_objt[0].name
    current_app.logger.info('Sessão criada com sucesso')
    return session
