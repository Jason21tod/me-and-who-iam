import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


message = client.messages.create(body='oia',
                    media_url='https://raw.githubusercontent.com/Jason21tod/me-and-who-iam/1bbf64b61024e17bd2037604c11e35ad06e34bd2/app/static/jason_whats_profile.png',
                    from_= 'whatsapp:+14155238886',
                    to= 'whatsapp:+5515997193465')