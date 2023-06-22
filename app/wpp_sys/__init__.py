from .msg_handlers import *
from .data_scrap import *


cumpriment_receiver = CumprimentReceiver()
help_receiver = HelpMsgReceiver()
scrap_msg_receiver = ScrapMsgReceiver()

first_msg_receiver = FirstMsgReceiver()
first_msg_receiver._containers.append(scrap_msg_receiver)
first_msg_receiver._containers.append(cumpriment_receiver)
first_msg_receiver._containers.append(help_receiver)
