# config_loader.py – ładowanie configu z pytaniem o hasło do XTB
import getpass

def load_config():
    config = {
        "xtb_email": input("Podaj login (email) do XTB: "),
        "xtb_password": getpass.getpass("Podaj hasło do XTB: "),
        "mode": "auto",  # lub 'manual'
        "delay": 3  # opóźnienie między transakcjami (sekundy)
    }
    return config
