from app.wpp_sys import FirstMsgReceiver, Container, ScrapMsgReceiver
from unittest import TestCase
from app import create_app
from typing import Any
import bs4
import requests


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


class TestScrapMsgReceiver(ScrapMsgReceiver, TestCase):
    url_mock = 'http://jasonuniver.com.br'

    def test_get_data(self):
        with create_app().app_context():
            mock_req = {
                    'ProfileName':'Mock author',
                    'From': '(XX)XXXXX-XXXX',
                    'content': 'analise http://jasonuniver.com.br',
                    'SmsStatus':'status ok'
                    }
            print(self.get_data(mock_req))

    def test_get_scrap(self):
        """Tenta capturar a scrap"""
        with create_app().app_context():
            print(self.get_scrap(url=self.url_mock))
            print(self.get_scrap(url='google.com'))
            print(self.get_scrap(url='instagram.com'))
            print(self.get_scrap(url='stackoverflow'))


    def test_get_from_url_without_http(self):
        """Tenta capturar o scrap sem especificar o protocolo de busca"""
        with create_app().app_context():
            print(self.get_from_url('jasonuniver.com.br'))

    def test_get_from_url_with_http(self):
        """Tenta capturar o scrap sem especificar o protocolo de busca"""
        with create_app().app_context():
            print(self.get_from_url(url=self.url_mock))

    def test_get_raw_datas(self):
        """Testa se ele é capaz de obter os dados corretamente"""
        with create_app().app_context():
            data_raw = requests.get(self.url_mock)
            data = bs4.BeautifulSoup(data_raw.text, features='html.parser')
            print(self.get_raw_datas(data))

    def test_get_strings_from_data(self):
        """testa se o jason é capaz de obter as strings das tags"""
        with create_app().app_context():
            data_raw = requests.get(self.url_mock)
            data = bs4.BeautifulSoup(data_raw.text, features='html.parser')
            raw_data = self.get_raw_datas(data)
            print(self.get_strings_from_datas(raw_data))

    def test_format_links(self):
        with create_app().app_context():
            data_raw = requests.get(self.url_mock)
            data = bs4.BeautifulSoup(data_raw.text, features='html.parser')
            print(self.format_links(data))

    def test_get_google(self):
        url = requests.get('http://google.com')
        scrap_infos = bs4.BeautifulSoup(url.text, features="html.parser")
        print(scrap_infos)