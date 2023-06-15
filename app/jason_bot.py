from flask import Blueprint, render_template, request, current_app
from .msg_handlers import PrimaryMsgReceiver
import requests

jason_bot = Blueprint('jason bot', __name__, url_prefix='/jason_bot')


@jason_bot.route('/')
def index():
    return render_template('jason_bot.html')

@jason_bot.route('/wppbot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    msg_receiver = PrimaryMsgReceiver()
    current_app.logger.info('Going to bot page')
    req = request.values
    return str(msg_receiver.receive_and_response_msg(req))


@jason_bot.route('/intagram_auth', methods=['GET', 'POST'])
def auth():
    return current_app.redirect("""https://api.instagram.com/oauth/authorize/?redirect_uri=https://jason-todd.herokuapp.com/&client_id=1659663484497725&response_type=code&scope=user_profile,user_media""")
 
@jason_bot.route('/callback')
def remake():
    url = "https://api.instagram.com/oauth/access_token"
    client_id = "1659663484497725"
    client_secret = "bbd2b3d2eca79ca839f29f4d070cff21"
    grant_type = "authorization_code"
    redirect_uri = "https://jason-todd.herokuapp.com/"
    code = "AQDtoc22IdrjcoFDoxh6UnYjUmUReSSjH7lt8FT-XakFHCu7d_lBrJmO6U8kmDDUh7gTxN8S4o4-p7U4XYNFYV3_A3TGxpoSMiJPX_b8GJ3H8huVRAOOZTjIwrYjlOOAdbjuJxrEnsKD1EUMkbyHFa7RawjifHWzRo5jBJEJNxgygdRGDIlvgNVAnsvRiCRGgLi8rc3_sgC5vWIZ2HLJdNxO85__VpcD78FQ3-6vgGv9Gg"

    # Faça a solicitação POST
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": grant_type,
        "redirect_uri": redirect_uri,
        "code": code
    }
    response = requests.post(url, data=data)

    """
    Jason bot
    """

    return response.text


