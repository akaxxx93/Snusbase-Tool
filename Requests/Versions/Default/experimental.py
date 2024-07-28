import requests
import json
from Core.create_file import create_file

def api_experimental(snusbase_auth, snusbase_api_url, url, body=None, filename=None):
    headers = {
        'Auth': snusbase_auth,
        'Content-Type': 'application/json'
    }
    method = 'POST' if body else 'GET'
    data = json.dumps(body) if body else None
    try:
        response = requests.request(method, snusbase_api_url + url, headers=headers, data=data)
        print(json.dumps(response.json(), indent=4))
        create_file(response.json(), filename)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
