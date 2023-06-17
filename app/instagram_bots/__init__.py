from flask import Blueprint, render_template, current_app, request
from flask_restful import Api, Resource

from .setup import *
from .scrap_bots import *


ig_bot = Blueprint('intagram bots', __name__, url_prefix='/instagram_bot')

URL = "https://api.instagram.com/oauth/access_token"
CLIENT_ID = "1659663484497725"
CLIENT_SECRET = "bbd2b3d2eca79ca839f29f4d070cff21"
GRANT_TYPE = "authorization_code"
REDIRECT_URI = "https://jason-todd.herokuapp.com/jason_bot/instagram_callback"



@ig_bot.route('/')
def login():
    return ('instagram bot its here')

@ig_bot.route('/auth', methods=['GET', 'POST'])
def auth():
    """Autenticação do instagram"""
    current_app.logger.info(request.values.to_dict())
    return current_app.redirect("""https://api.instagram.com/oauth/authorize/?redirect_uri=https://jason-todd.herokuapp.com/jason_bot/instagram_callback&client_id=1659663484497725&response_type=code&scope=user_profile,user_media""")
 
@ig_bot.route('/callback')
def instagram_callback():
    """Devolve um Token de acesso de"""
    current_app.logger.info(request.values.to_dict())
    auth_code = request.values.to_dict()['code']
    code = auth_code

    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": GRANT_TYPE,
        "redirect_uri": REDIRECT_URI,
        "code": code
    }
    response = requests.post(URL, data=data)
    print(response)
    return render_template('jason_bot.html')

class InstagramResource(Resource):
    def get(self):
        fields = request.args.get('fields')

        return fields


