import requests
from logging import log, WARN, INFO

"""Na criação deste módulo, é importante ressaltar, que uma vez criados, os tokens de
acesso de longa duração não podem ser acessados novamente até que expirem, caso voce
tente acessa-los usando o instagram/access_token usando o parametro ig_exchange_token,
ele retornará um erro.
"""

# token atual (APAGAR DPS)
# IGQVJVMXBTZAEJmRzJaRzhIYm1IVnNjZA3d2TVFZAOHRWSkUtLXFRMUQ5eGs1RzhPSjdZAWVl2YXd3UzZA0c3dlZAGpFTkp0NG5HM3JfcUY4SHNTR05EMGhSYWFBaHRMd2xJMEpxNGlQQjBn

def get_new_long_duration_token(app_secret, code):
    url = 'https://graph.instagram.com/access_token'

    params = {
        'grant_type':'ig_exchange_token',
        'client_secret': app_secret,
        'access_token':code
    }

    
    response = requests.get(url=url, params=params)
    log(INFO,response.text)
    if response.status_code == 400:
        log(WARN,' >>> Não foi possivel obter o token de acesso de longa duração\n - verifique se ele já não foi gerado')
        response = {'access_token': code}
    return response


def change_long_duration_token(code):
    """troca o token de longa duração por um outro"""
    url= 'https://graph.instagram.com/refresh_access_token'

    params = {
    "grant_type": "ig_refresh_token",
    "access_token": code
    }
    response = requests.get(url=url, params=params)
    print(response.text)
    

    if response.status_code == 200:
        response = response.json()
    else:
        print("A solicitação falhou com código de resposta:", response.status_code)
    return response