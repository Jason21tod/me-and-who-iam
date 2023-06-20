from app.wpp_sys import FirstMsgReceiver, Container
from unittest import TestCase
from typing import Any


mock_request = dict()
mock_request['ProfileName']='Mock user'
mock_request['From'] = 'From other user'

mock_request['content'] = 'This is the body'
mock_request['SmsStatus'] ='Status ok'


class MockChildContainer(Container):
    current_process: Any = None

    @classmethod
    def process_msg(cls, request):
        return cls.current_process(request)

    @classmethod
    def process_success_msg(cls, request: dict):
        print(request)
        print('EXECUTANDO FUNÇÂO DE SUCESSO')
        return 'Message processed'
    
    @classmethod
    def process_fail_msg(cls, request: dict):
        print('EXECUTANDO FUNÇÃO DE ERRO')
        print(request)
        return False


class TestFirstMsgReceiver(FirstMsgReceiver, TestCase):
    _containers = []


    def test_success_process_msg(self):
        """Testa se a mensagem foi processada com sucesso"""
        self._containers.append(MockChildContainer)
        MockChildContainer.current_process = MockChildContainer.process_success_msg
        self.assertEqual(self.process_msg(request=mock_request)['content'], 'Message processed')
        self._containers.pop(0)

    
    def test_fail_process_msg(self):
        """Testa se a mensagem NÃO foi processada com sucesso"""
        self._containers.append(MockChildContainer)
        MockChildContainer.current_process = MockChildContainer.process_fail_msg
        self.assertEqual(self.process_msg(request=mock_request)['content'], self.default_error_msg)
        self._containers.pop(0)


