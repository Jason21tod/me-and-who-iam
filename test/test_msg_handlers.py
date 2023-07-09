from app.jason_bot import *
from app import create_app
from unittest import TestCase



class RequestMock:
    celphone = '15997193465'
    name = 'Gian Pereira'

    def get(self, what):
        values_dict = {
            'celphone': self.celphone,
            'name': self.name
            }
        return values_dict[what]


request= RequestMock()
request_2 = RequestMock()
request_2.celphone = 'xxxxxxxxxx'
request_2.name = 'wrong name'


class TestFunctions(TestCase):
    def test_veriy_is_logged_in(self):
        with create_app().app_context():
            self.assertTrue(verify_is_logged(request))

    def test_verify_is_not_logged_in(self):
        with create_app().app_context():
            self.assertFalse(verify_is_logged(request_2))

    def test_create_session(self):
        with create_app().test_request_context():
            print(create_session(request_values=request))

    