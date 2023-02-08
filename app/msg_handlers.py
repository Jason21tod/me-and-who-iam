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
    def receive_and_response_msg(self, msg) -> messaging_response.MessagingResponse:
        msg_data: dict = _format_request_to_msg_dict(msg)
        message = messaging_response.MessagingResponse()
        message.message(body='OIIII', to=msg_data['from'], from_=msg_data['to'])
        info(f'Out -> {msg}')
        return message
        

