import os
import json
import requests
from dotenv import load_dotenv
from Requests.Versions.Beta.V1 import api_v1
from Requests.Versions.Beta.V2 import api_v2
from Requests.Versions.Default.experimental import api_experimental
load_dotenv()

snusbase_auth = os.getenv("SNUSBASE_AUTH_TOKEN")
snusbase_api_url = os.getenv("SNUSBASE_API")

def send_request(url, type, search, api_url, filename, body=None):
    match api_url:
        case "https://beta.snusbase.com/v1":
            api_v1(api_url, type, search, snusbase_auth)
        case "https://beta.snusbase.com/v2":
            api_v2(api_url, type, search)
        case _:
            api_experimental(snusbase_auth, snusbase_api_url, url, body, filename)
