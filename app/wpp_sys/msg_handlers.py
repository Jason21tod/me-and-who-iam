from abc import ABC, abstractmethod
from werkzeug.datastructures import CombinedMultiDict
from flask import current_app
from twilio.rest import Client
from logging import info
import os
from typing import Any
from app import db


"""
###Módulo de handlers de mensagens###

Responsável pelo controle e formatação de mensagens
"""


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


class Container(ABC):
    """Classe que representa um container, ela não tem nenhum comportamento
    necessário, somente uma função para que ela se comporte como um composite"""
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    
    @abstractmethod
    def process_msg(self, request: dict):
        pass

class Composite(Container):
    """Classe que representa um composite de containeres, ele possui um atributo privado
    chamado de container, onde ele guarda a lista de outros containers ou composites"""
    _containers: list = []

    @abstractmethod
    def process_msg(self, request: dict):
        pass


def _register_a_conversation(request: dict):
    """
    Registra um conversa no banco de dados sqlite, ela desaparece após alguns minutos
    """
    db.db.session.add(db.ConversationRegister(
        name='Joao',
        number='XX-XXXXXXX'
        ))
    db.db.session.commit()
    db.db.session.close()


def _format_request_to_msg_dict(request: CombinedMultiDict) -> dict:
    """
        Formata a mensagem para um dict com somente oque usaremos ao longo de toda a requisição
    """
    try:
        request_dict = {
            'profile_name':request.get('ProfileName'),
            'from': request.get('From'),
            'to': request.get('To'),
            'content': request.get('Body'),
            'status': request.get('SmsStatus')
        }
        info(f'receiving <- {request_dict}')
        return request_dict
    except:
        raise ValueError(f'The value its not the correct for formatation, must be a {CombinedMultiDict.__name__} not {request}')
        

class FirstMsgReceiver(Composite):
    """
    classe responsável por receber a mensagem em primeira linha, repassar para uma cadeia de containers
    que devolvem a mensagem formatada, ele então a devolve aos seu client, para que o mesmo trabalhe com
    requisição em forma de dicionário.
    """

    default_error_msg='Opa, não entendi, pode repetir ? derepente, vê se o comando ta certo 🙃, *Digita um Help*'
    

    def create_default_error_msg(self, msg_data):
        client.messages.create(
            body=self.default_error_msg,
            from_=msg_data['to'],
            to=msg_data['from'])

    def process_msg(self, request: Any) -> dict:
        """
        Executa a request por uma cadeia de childs, containers, aquele que retornar uma resposta,
        diferente de False, terá sua resposta validada
        """
        _register_a_conversation(request)
        dict_request = _format_request_to_msg_dict(request)
        current_app.logger.info(f'MSG: {dict_request}')
        for child_container in self._containers:
            print(f'executando: {child_container}')
            result = child_container.process_msg(dict_request)
            if not result:
                pass
            elif result != False: 
                dict_request['content'] = result
                return dict_request
        dict_request['content'] = self.default_error_msg
        self.create_default_error_msg(dict_request)
        return dict_request
    

class CumprimentReceiver(Container):

    commom_response_eng = """
    😄 Hi my name is Jason, iam a bot system developed by Gian P. Nunes on Brazil.\n
    \nThat is photo on my profile its not me 🙃, its the whatsapp enterprise where i live !\n\n
    My dev is developing my ohter functions 🤖, for a while, i have only this automatic message,
    send some feedbacks to him if you have some cool feedbacks  🤜 🤛. Hah ! That its my real face on whatsapp:
    """

    commom_response_pt = """    😄Olá ! Meu nome é Jason, sou um sistema de bot desenvolvido pelo Gian P Nunes no Brasil.\n
    \nEssa foto no meu perfil não sou eu 🙃, É do número de teste da empresa que eu uso !\n\n
    Meu dev está desenvolvendo outras funções 🤖, Digita um help aí pra ver quais mais eu tenho,
    Manda alguns feedbacks pra ele também ! Ele adora conversar 🤜🤛. ah ! Esse sou eu no whattsapp:
    """

    def create_msg(self, msg_data: dict, lang: str):
        current_app.logger.info(f'MSG: DETECTADO CUMPRIMENTO')
        response = self.commom_response_eng
        photo_body = 'iam beuatifull in green'
        if lang == 'pt':
            photo_body = 'Tô lindo usando verde'
            response = self.commom_response_pt
        client.messages.create(
                    body=response,
                    from_=msg_data['to'],
                    to=msg_data['from'])
        
        client.messages.create(
                    body=photo_body,
                    media_url='https://raw.githubusercontent.com/Jason21tod/me-and-who-iam/1bbf64b61024e17bd2037604c11e35ad06e34bd2/app/static/jason_whats_profile.png',
                    from_=msg_data['to'],
                    to=msg_data['from'])

    def process_msg(self, request:dict) -> bool | str:
        try:
            if request['content'].upper() in ['OI','OLA', 'OLÁ', 'TUDO BEM ?', 'OPA', 'BOM DIA', 'BOA NOITE', 'BOA TARDE']:
                self.create_msg(request, 'pt')
                return True
            elif request['content'].upper() in ['HELLO', 'HI', 'WHATS UP ?', 'YEAH', 'GOOD MORNING', 'GOOD EVENING', 'GOOD AFTERNOON']:
                self.create_msg(request, 'eng')
                return True
            else:
                current_app.logger.debug('Não foi detectado cumprimento')
                return False
        except:
            current_app.logger.warning(f'ACESSO FORA DO WHATSAPP')
            return 'Oi ! você acessou um ednpoint errado, tenta acessar pela plaforma do Jason bot'

class HelpMsgReceiver(Container):
    help_message = """
    Oi ! Precisa de uma ajuda ? 😄

    *- tente me cumprimentar*: Eu sei os cumprimentos mais basicos só por enquanto.
    *- Eu seu fazer analises simples de sites*: Digita "analise urldosite.com". não se esquece de digitar o endereço do site direitinho
    """

    def create_msg(self, msg_data):
        client.messages.create(
            body=self.help_message,
            from_=msg_data['to'],
            to=msg_data['from'])

    def process_msg(self, request: dict):
        try:
            if request['content'].upper() in ['HELP']:
                self.create_msg(request)
                return True
        except:
            return 'Provavelmente você acessou o endpoint errado, tente acessar pelo whatsapp'
