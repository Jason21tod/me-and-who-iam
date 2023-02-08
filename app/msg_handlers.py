from abc import ABC, abstractmethod
from werkzeug.datastructures import CombinedMultiDict
from twilio.twiml import messaging_response
from twilio.rest import Client
from logging import info
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)



class MsgReceiver(ABC):
    @abstractmethod
    def receive_and_response_msg(self, msg):
        return


def _format_request_to_msg_dict(request: CombinedMultiDict) -> dict:
    """Generate a new msg_convertion to a compreensive dict

    Args:
        request (CombinedMultiDict): Dict from werkzeug datastructures

    Returns:
        dict|None: 
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
        


class PrimaryMsgReceiver(MsgReceiver):
    commom_response = """
    Hi my name is Jason, iam a bot system developed by Gian P. Nunes on Brazil.
    That is photo on my profile its not me, its the whatsapp enterprise where i live !
    My dev is developing my ohter functions, but, for a while, i have only this automatic message,
    send some feedbacks to him caso tenha alguma ideia dahora, seuge aí uma foto minha:
    """
    def receive_and_response_msg(self, msg) -> messaging_response.MessagingResponse:
        msg_data: dict = _format_request_to_msg_dict(msg)
        message = messaging_response.MessagingResponse()
        message.message(
            media_url='https://raw.githubusercontent.com/Jason21tod/me-and-who-iam/main/app/static/styles/jason.png',
            body=self.commom_response, to=msg_data['from'],
            from_=msg_data['to']
            )
        info(f'Out -> {msg}')
        return message
        

