import fade
import json
import os
from dotenv import load_dotenv
from colorama import Fore, Style
from Core.send_request import send_request
from Core.create_file import create_file

load_dotenv()

snusbase_api_url = os.getenv("SNUSBASE_API")

with open("Texts/welcome.txt", "r") as f:
    text_default = f.read()

def user_input(text, type, api_url=snusbase_api_url):

    os.system('cls' if os.name == 'nt' else 'clear')
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)

    search = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + text)

    if search == "exit" or search == "quitter":
        exit()
    else:
        search_response = send_request("data/search", type, search, api_url, search, {
            'terms': [search],
            'types': [type],
            'wildcard': False,
        })

        formatted_response = json.dumps(search_response, indent=2)
        if formatted_response == []:
            create_file(formatted_response, text)
            print(formatted_response)
            create_file(formatted_response, text)

        input("\nAppuyez sur la touche Entrée pour continuer...")
