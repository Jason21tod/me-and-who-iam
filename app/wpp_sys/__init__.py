from .msg_handlers import *


cumpriment_receiver = CumprimentReceiver()
help_receiver = HelpMsgReceiver()

first_msg_receiver = FirstMsgReceiver()
first_msg_receiver._containers.append(cumpriment_receiver)
first_msg_receiver._containers.append(help_receiver)
