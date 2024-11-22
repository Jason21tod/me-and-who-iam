from flask_restful import Resource, reqparse
from api.common.message_handlers import *


class MessagePort(Resource):
    """Resource responsible for receive the content of the message and return a response"""
    message_handler = BaseMessageHandler()
    cumpriment_handler = CumprimentHandler()
    analyse_handler = AnalyseHandler()
    whoiam_handler = WhoIamAmHandler()

    message_handler.next_handlers.append(whoiam_handler)
    message_handler.next_handlers.append(cumpriment_handler)
    message_handler.next_handlers.append(analyse_handler)

    def post(self) -> dict[str, str] | None:
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, required=True, help='Message text invalid')
        parser.add_argument('user', type=bool, required=True, help='user type invalid or inexistent')
        args = parser.parse_args()
        data = self.message_handler.receive_message(args)
        return data
