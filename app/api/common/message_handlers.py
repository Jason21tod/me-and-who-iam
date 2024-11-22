import abc
from .scrappers import *
from .responses import no_processed_message_response, _Response

CUMPRIMENT_RESPONSE = 'Hello Buddy !'
ANALYSE_RESPONSE = 'Analysing... \n\n'
WHO_IAM = """
Im Jason Scrapbot, Created by Gian ( or Jason if u want)

All my functionalites are made to get infos from the sites, if you want
to support, pls, help on github with a pull request: 
"""


class Handler(abc.ABC):
    """
    Class That Represents the handlers of messages.
    Every Handler should have a next(s) handler(s) or just a empty return.
    """
    def __init__(self) -> None:
        super().__init__()
        self.next_handlers: list[MessageHandler] = []


class MessageHandler(Handler):
    """Class that process a message on the server."""
    @abc.abstractmethod
    def process_message(self, content):
        """Method that process the message or pass to the next handlers"""
        print('receiving content: ', content, '- in ', self.__str__())
        return _Response()

class BaseMessageHandler(Handler):
    """Base Message Handler recieve the message then, send it to the next handlers"""
    def receive_message(self, data):
        """Receive the message data and send it to next handlers"""
        print("Receiving Message...")
        for handler in self.next_handlers:
            response_objt = handler.process_message(
                content=data
                )
            if type(response_objt) != bool:
                print('Response returned -> ', response_objt)
                return response_objt.build_response_json()
            else:
                pass
        print('ERROR - No response found ')
        return no_processed_message_response.build_response_json()


class CumprimentHandler(MessageHandler):
    """Handler that verify if the message is a cumpriment"""
    def __init__(self) -> None:
        super().__init__()
    
    def process_message(self, content):
        response_objt = super().process_message(content)
        if 'hello'.capitalize() in content['text'].capitalize():
            response_objt.text = CUMPRIMENT_RESPONSE
            response_objt.content_type = 'cumpriment'
            return response_objt
        else:
            return False


class AnalyseHandler(MessageHandler):
    """Handler that verify if the message is a analyse request"""
    def __init__(self) -> None:
        super().__init__()
    
    def process_message(self, content,):
        response_objt = super().process_message(content,)
        if 'analyse'.capitalize() in content['text'].capitalize():
            return self.build_message(content, response_objt)
        else:
            return False
        
    def build_message(self, content, response_objt: _Response):
        """Build the messages and return. If the 'http' is not on the text field, it should return a error text:
        
        'Please provide a valid link, i could not find'"""
        if 'http' in content['text']:
            url = self.format_url(content)
            soup = get_from_url(url)
            return self.is_soup(soup, response_objt)
        else:
            response_objt.text += 'Please provide a valid link, i could not find'
            return response_objt
    
    def is_soup(self, soup, response_objt: _Response):
        """Verify is the object its a valid soup"""
        if not soup: return self.build_no_soup_response(response_objt)
        return self.build_soup_response(soup, response_objt)

    def build_soup_response(self, soup, response_objt: _Response):
        """Use BeautifullSoup object to format the text"""
        response_objt.text += f'Here is it ;)  \n\n'
        response_objt.content_type = 'analyse'
        response_objt.content['title'] = f"{soup.title.contents}"
        response_objt.content['lang'] = f"{soup.html.attrs['lang']}"
        response_objt.content['links'] = separate_all_links(get_all_links(soup))
        response_objt.content['imgs'] = get_all_images(soup)
        return response_objt

    def build_no_soup_response(self, response_objt: _Response):
        """Return a 'error text' in text field"""
        response_objt.text += 'I couldnt analyse that link, maybe the server is down ?'
        return response_objt

    def format_url(self, content):
        """Method that find, format and extract url in the text field"""
        http_location = content['text'].find('http')
        formated_http = content['text'][http_location::]
        space_index = formated_http.find(' ')
        if space_index == -1:
            return formated_http
        return formated_http[:space_index]


class WhoIamAmHandler(MessageHandler):
    """Handler that Verify if the message is a request about who the robot is"""
    def __init__(self) -> None:
        super().__init__()

    def process_message(self, content):
        response_objt = super().process_message(content)
        if 'who are you'.capitalize() in content['text'].capitalize():
            response_objt.text = WHO_IAM
            response_objt.content_type = 'who_i_am'
            response_objt.content['respository_link'] = "https://github.com/Jason21tod/scrap-bot"
            return response_objt
        else:
            return False
        
