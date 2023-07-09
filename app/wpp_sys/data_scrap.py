import bs4
import requests
import os
from flask import current_app
from .msg_handlers import Container
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def verify_various_values(various_values: str|list):
    data = ""
    if isinstance(various_values, list):
        for value in various_values:
            if value == None:
                data += 'Não foi possivel obter essa informação' + '\n'
            else:
                data += '-' + value.replace('\n', '') +'\n'
        return data
    if various_values == None:
        return ' Não foi possivel obter essa informação'
    return various_values.replace('\n', '')


class ScrapMsgReceiver(Container):
    def process_msg(self, request: dict):
        try:
            if  'ANALISE' in request['content'].upper() or 'ANÁLISE' in request['content'].upper():
                current_app.logger.info('Scrap command activated.')
                request['content'] =request['content'].strip()
                self.create_msg(request)
                current_app.logger.info('Scrap MSG send')
                return True
        except:
            return 'Você provavelmente ta tentando se comunicar com o jason bot, mas tenta acessar ele pelo whatsapp, funciona la'

    def create_msg(self, request):
        data = self.get_data(request)
        if 'error' in data:
            body = data['error']
        else:
            body = f"""
            🤓 *Claro ! buscando iformações da {data['url']}...* 🤓

                *Título* 📚
{verify_various_values(data['title'])}

                *Cabeçalho* 🖹
{verify_various_values(data['header'])}

                *Legendas encontradas* 🔍
{verify_various_values(data['legend'])}

                *Navegação* 🚀
{verify_various_values(data['navigation'])}

                *Links* 🔗
{verify_various_values(data['links'])}
                    """
        client.messages.create(body=body,from_=request['to'],to=request['from'])
    
    def get_data(self, request):
        body: str = request['content']
        url_pos = body.find(' ')
        url = body[url_pos:].strip()
        data = self.get_scrap(url)
        data['url'] = url
        return data

    def get_scrap(self, url):
        print(url)
        try:
            data= self.get_from_url(url)
            if isinstance(data, dict):
                return data
            scrap_infos = bs4.BeautifulSoup(data.text, features="html.parser")
            data_set = self.get_raw_datas(scrap_infos)
            data_set = self.get_strings_from_datas(data_set)
            data_set['links'] = self.format_links(scrap_infos)
            return data_set
        except:
            return {'error': """
                Não foi possivel acessar o site 😕

Tenta verificar se digitou o link corretamente.
Verifica também, se esse site n tem nenhum tipo de autenticação, como um site de login por exemplo
            """}
    
    def get_from_url(self, url):
        with current_app.app_context():
            try:
                current_app.logger.info(f'Verificando link... {url}')
                if 'http://' not in url:
                    current_app.logger.info(f'Sem metodo especificado... {url}')
                    try:
                        return requests.get('https://'+url)
                    except:
                        return requests.get('http://'+url)
                return requests.get(url)
            except:
                return {'error':'Site não encontrado, tenta verificar se escreveu a URL certinha: com o ".com" e os ".br" ou outros'}

    def get_strings_from_datas(self, scrap_infos: dict):
        new_scrap_infos = {}
        for data in scrap_infos.items():
            try:
                if str(data[0]) != 'links': new_scrap_infos[str(data[0])] = data[1].string
                else: new_scrap_infos[str(data)] = data[1]
            except:
                new_scrap_infos[str(data[0])] ='Não foi possível localizar essa informação'
        return new_scrap_infos

    def get_raw_datas(self,scrap_infos: bs4.BeautifulSoup) -> dict:
            title = scrap_infos.title
            legend = scrap_infos.legend
            nav = scrap_infos.nav
            header = scrap_infos.h1
            return {
                'title':title,
                'header':header, 
                'legend':legend,
                'navigation': nav,
                'links': self.format_links(scrap_infos)}
    

    def format_links(self, scrap_infos):
        links = []
        try:
            for link in scrap_infos.find_all('a'):
                links.append(link.get('href'))
            if len(links) >5:
                current_app.logger.info('Links demais encontrados')
                return links[0:8]
            return links
        except:
            return 'Não foi possivel obter os links'
