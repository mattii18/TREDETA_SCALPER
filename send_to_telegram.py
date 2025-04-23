import requests

TOKEN = '7600816191:AAHglqWYgD2aVfiCba6m6m6qS3_aG-prlXQ'
CHAT_ID = '6673294456'

def send_file(file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': CHAT_ID}
    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print(f"Plik {file_path} został wysłany na Telegram.")
    else:
        print(f"Błąd wysyłania: {response.text}")

if __name__ == "__main__":
    # PRZYKŁAD: Wpisz tutaj nazwę pliku do wysłania
    send_file("main.py")

