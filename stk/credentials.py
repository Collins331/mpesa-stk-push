import json
import base64
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv


load_dotenv()


class Credentials:
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    passkey = os.getenv('PASSKEY')
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"


class MpesaAccessToken:
    token = requests.get(Credentials.api_url, auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret))
    access_token = json.loads(token.text)
    validated_token = access_token['access_token']


class MpesaPassword:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortcode = "174379"
    passkey = Credentials.passkey


    encode_str = shortcode + passkey + timestamp

    encoded = base64.b64encode(encode_str.encode())

    decoded_password = encoded.decode('utf-8')