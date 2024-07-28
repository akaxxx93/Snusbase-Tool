import os
import json
from colorama import Style, Fore

def create_file(formatted_response, filename):
    get_file = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Voulez-vous enregistrer les informations dans un fichier ? (oui/non) ou (o/n) > ")

    if get_file.lower() == "oui" or get_file.lower() == "o" or get_file.lower() == "yes" or get_file.lower() == "y":
        if not os.path.exists("data"):
            os.mkdir("data")
        if os.path.exists(f"data/{filename}.json"):
            os.remove(f"data/{filename}.json")
        with open(f'data/{filename}.json', "w") as f:
            f.write(json.dumps(formatted_response, indent=1))
            f.close()

    print(Style.RESET_ALL + "[" + Fore.BLUE+"+"+Style.RESET_ALL + "]" + ' Le fichier est stocké dans "data/' + filename + '.json"')
