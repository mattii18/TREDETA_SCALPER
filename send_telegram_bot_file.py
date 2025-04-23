import requests
import os

TOKEN = '7600816191:AAHglqWYgD2aVfiCba6m6m6qS3_aG-prlXQ'
CHAT_ID = '6673294456'

def send_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Błąd: Plik '{file_path}' nie istnieje w folderze!")
        return
    print(f"Próba wysłania pliku: {file_path} ...")
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': CHAT_ID}
    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print(f"SUKCES: Plik {file_path} został wysłany na Telegram.")
    else:
        print(f"BŁĄD WYSYŁKI: {response.status_code} -> {response.text}")

if __name__ == "main":
    send_file("telegram_bot.py")