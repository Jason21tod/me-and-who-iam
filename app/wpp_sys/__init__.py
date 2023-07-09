from .msg_handlers import *
from .data_scrap import *



cumpriment_receiver = CumprimentReceiver('Cumprimento')
help_receiver = HelpMsgReceiver('Help')
scrap_msg_receiver = ScrapMsgReceiver('Analise')

first_msg_receiver = FirstMsgReceiver('Inicio da conversa')
first_msg_receiver._containers.append(scrap_msg_receiver)
first_msg_receiver._containers.append(cumpriment_receiver)
first_msg_receiver._containers.append(help_receiver)

