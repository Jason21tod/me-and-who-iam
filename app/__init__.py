import smtplib
import os
import requests
from flask import request, Flask, render_template, redirect
from .msg_handlers import PrimaryMsgReceiver
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from werkzeug.datastructures import ImmutableMultiDict


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home_page.html')

@app.route('/jason_bot.html', methods=['GET'])
def jason_bot():
    return render_template('jason_bot.html')


@app.route('/post_info', methods=['GET', 'POST'])
def form_post():
    app.logger.info(request.form)
    send_invitation(request.form)
    return redirect('/')


@app.route('/bot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    msg_receiver = PrimaryMsgReceiver()
    app.logger.info('Going to bot page')
    req = request.values
    return str(msg_receiver.receive_and_response_msg(req))

@app.route('/auth/', methods=['GET', 'POST'])
def auth():
    req = requests.get("""https://api.instagram.com/oauth/authorize
    ?client_id={1659663484497725}
    &redirect_uri'={https://jason-todd.herokuapp.com/auth/}
    &scope=user_profile,user_media
    &response_type=code""")
    return req.text

SENDER_EMAIL = os.environ['EMAIL_SENDER']
RECEIVER_EMAIL = os.environ['EMAIL_RECEIVER']
PASSWORD = os.environ['EMAIL_APP_PASSWORD']


def send_invitation(form_post: ImmutableMultiDict):
    """Lida com as propostas e as envia para o alvo
    """
    if len(form_post) == 0:
        app.logger.info('sem dados para enviar...')
        return
    app.logger.info('enviando proposta...')
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = f"Proposta de {form_post.get('name')}"
    body = f"""
    Email:    {form_post.get('email')}
    Celular: {form_post.get('celphone')}
    {form_post.get('about')}
    """
    message.attach(MIMEText(body, "plain", "utf-8"))
    server = auth()
    send(server, message)
    

def auth():
    """Autentica e envia o email"""
    app.logger.info('Autenticando...')
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, PASSWORD)
    app.logger.info('Autenticado...')
    return server
    

def send(server, message:MIMEMultipart):
    """Envia o email"""
    app.logger.info('Enviando email...')
    text = message.as_string()
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
    server.quit()
    app.logger.info('Prontinho, email enviado...')

def run():
    return app


if __name__ == '__main__':
    app.run()