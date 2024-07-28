import json
import requests

def api_v2(api_url, type, search):
    f = requests.get(f"{api_url}/{type}/{search}")
    if f.status_code == 200:
        out = f.json()["result"]
        l = []
        for item in out:
            for item2 in out[item]:
                l.append(item2)
                
        formatted_results = json.dumps(l, indent=2)  # Pretty print the results
        print("")
        print(formatted_results)
    else:
        print("La requête a échoué.")