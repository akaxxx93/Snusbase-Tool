import traceback
from colorama import Style
from Snusbase.Functions.Core.save_error_log import save_error_log


def handle_error():
    error = traceback.format_exc()
    print(Style.RESET_ALL + "Une erreur s'est produite. Veuillez consulter les logs pour plus de détails.")
    save_error_log(error)
