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
      😄 Hi my name is Jason, iam a bot system developed by Gian P. Nunes on Brazil.\n
    \nThat is photo on my profile its not me 🙃, its the whatsapp enterprise where i live !\n\n
    My dev is developing my ohter functions 🤖, for a while, i have only this automatic message,
    send some feedbacks to him if you have some cool feedbacks  🤜 🤛. Hah ! That its my real face on whatsapp:
    """
    def receive_and_response_msg(self, msg) -> messaging_response.MessagingResponse:
        msg_data: dict = _format_request_to_msg_dict(msg)
        message = messaging_response.MessagingResponse()
        message = client.messages.create(body=self.commom_response,
                            from_=msg_data['to'],
                            to=msg_data['from'])
        client.messages.create(
                            media_url='https://github.com/Jason21tod/me-and-who-iam/blob/main/app/static/styles/jason_whats_profile.png?raw=true',
                            body='Helloooo ( im beautifull in green )',
                            from_=msg_data['to'],
                            to=msg_data['from'])
        info(f'Out -> {message}')
        return message
        

