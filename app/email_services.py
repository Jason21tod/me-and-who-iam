import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from werkzeug.datastructures import ImmutableMultiDict


from flask import Blueprint, request, current_app


email_service = Blueprint('email services', __name__, url_prefix='/email_service')


@email_service.route('/', methods=['GET', 'POST'])
def form_post():
    """Endpoint para me enviar os emails"""
    current_app.logger.info(request.form)
    send_invitation(request.form)
    return current_app.redirect('/')


SENDER_EMAIL = os.environ['EMAIL_SENDER']
RECEIVER_EMAIL = os.environ['EMAIL_RECEIVER']
PASSWORD = os.environ['EMAIL_APP_PASSWORD']


def send_invitation(form_post: ImmutableMultiDict):
    """Lida com as propostas e as envia para o alvo
    """
    if len(form_post) == 0:
        current_app.logger.info('sem dados para enviar...')
        return
    current_app.logger.info('enviando proposta...')
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
    current_app.logger.info('Autenticando...')
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, PASSWORD)
    current_app.logger.info('Autenticado...')
    return server


def send(server, message:MIMEMultipart):
    """Envia o email"""
    current_app.logger.info('Enviando email...')
    text = message.as_string()
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
    server.quit()
    current_app.logger.info('Prontinho, email enviado...')
