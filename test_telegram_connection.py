import requests

TOKEN = '7600816191:AAHglqWYgD2aVfiCba6m6m6qS3_aG-prlXQ'
CHAT_ID = '6673294456'

def send_test_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': 'ScalperX: Test połączenia z Telegramem działa!'
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("SUKCES: Wiadomość testowa wysłana na Telegram!")
    else:
        print(f"BŁĄD: {response.status_code} -> {response.text}")

if __name__ == "main":
    send_test_message()