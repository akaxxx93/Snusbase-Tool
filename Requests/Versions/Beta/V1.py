import requests

def api_v1(api_url, type, search, snusbase_auth):
    url = f"{api_url}/{type}/{search}"
    headers = {
        "authorization": snusbase_auth
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        print("")
        for key, value in result.items():
            print(f"{key}: {value}")
        else:
            print("La requête a échoué.")